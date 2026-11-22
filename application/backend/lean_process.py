"""Bounded output capture for locally approved Lean processes.

A registered Lean file is trusted input to the local toolchain. This is not a
sandbox for arbitrary user-supplied Lean code or an isolation boundary.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path
import signal
import subprocess
import threading

from backend import lean_cgroup, lean_windows_job

try:
    import resource
except ImportError:  # Windows
    resource = None

MAX_LOG_BYTES = 16000
READ_CHUNK_BYTES = 8192
MIN_MEMORY_MB = 512
MAX_MEMORY_MB = 65536


class MemoryLimitUnavailable(RuntimeError):
    """Requested memory ceiling is not enforceable on this host."""


def configured_memory_limit_mb() -> int | None:
    """Read an opt-in, strictly validated per-process virtual memory ceiling."""
    raw = os.environ.get("MATLIB_LEAN_MEMORY_MB")
    if raw is None:
        return None
    if not re.fullmatch(r"[1-9][0-9]{0,4}", raw):
        raise ValueError("MATLIB_LEAN_MEMORY_MB musi być liczbą całkowitą od 512 do 65536.")
    value = int(raw)
    if not MIN_MEMORY_MB <= value <= MAX_MEMORY_MB:
        raise ValueError("MATLIB_LEAN_MEMORY_MB musi być z zakresu 512–65536 MiB.")
    return value


def memory_limit_supported() -> bool:
    """Limit verified for Linux RLIMIT_AS; other OSes fail closed when requested."""
    return sys.platform.startswith("linux") and resource is not None and hasattr(resource, "RLIMIT_AS")


def _limited_command(command: list[str], memory_limit_mb: int | None) -> list[str]:
    if memory_limit_mb is None:
        return command
    if not isinstance(memory_limit_mb, int) or not MIN_MEMORY_MB <= memory_limit_mb <= MAX_MEMORY_MB:
        raise ValueError("Unsupported memory limit.")
    if not memory_limit_supported():
        raise MemoryLimitUnavailable("Nie można wymusić limitu pamięci na tym systemie.")
    helper = Path(__file__).with_name("lean_memory_exec.py")
    if not helper.is_file():
        raise MemoryLimitUnavailable("Brak programu ustawiającego limit pamięci Lean.")
    return [sys.executable, str(helper), str(memory_limit_mb * 1024 * 1024), "--", *command]


def _stop_process_group(process: subprocess.Popen[bytes]) -> None:
    """Best-effort cleanup of the Lake/Lean process family after timeout."""
    if os.name == "posix":
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        except OSError:
            if process.poll() is None:
                process.kill()
    elif os.name == "nt":
        try:
            subprocess.run(
                ["taskkill", "/F", "/T", "/PID", str(process.pid)],
                stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL, check=False, timeout=5,
            )
        except (OSError, subprocess.TimeoutExpired):
            pass
        if process.poll() is None:
            process.kill()
    elif process.poll() is None:
        process.kill()


def execute_registered(
    command: list[str], cwd: Path, *, timeout: float,
    log_limit: int = MAX_LOG_BYTES, memory_limit_mb: int | None = None,
    total_memory_mb: int | None = None,
) -> tuple[int | None, str, bool]:
    """Launch approved code; opt-in cgroup caps aggregate memory of all children.

    Cgroup creation and limit setup happen before spawning. The child joins
    the new group before executing the actual toolchain. Cleanup kills any
    surviving descendants and refuses to report their run as successful.
    """
    if timeout <= 0 or log_limit <= 0:
        raise ValueError("Execution limits must be positive.")
    command = _limited_command(command, memory_limit_mb)
    group = None
    windows_job = None
    startup = None
    if total_memory_mb is not None:
        if lean_windows_job.available():
            windows_job = lean_windows_job.ProcessJob.create(total_memory_mb)
            helper = Path(__file__).with_name("lean_windows_exec.py")
            if not helper.is_file():
                windows_job.kill_and_close()
                raise lean_windows_job.JobUnavailable(
                    "Brak programu Windows do uruchamiania kompilatora Lean.")
            command = [sys.executable, str(helper), "--", *command]
            startup = windows_job.start
        else:
            group = lean_cgroup.ProcessGroup.create(total_memory_mb)
            helper = Path(__file__).with_name("lean_cgroup_exec.py")
            if not helper.is_file():
                group.kill_and_remove()
                raise lean_cgroup.CgroupUnavailable(
                    "Brak programu dołączającego proces do cgroup.")
            command = [sys.executable, str(helper), str(group.path), "--", *command]
    try:
        result = _execute_process(
            command, cwd, timeout=timeout, log_limit=log_limit, startup=startup)
    finally:
        surviving_tasks = False
        if windows_job is not None:
            surviving_tasks = windows_job.kill_and_close()
        elif group is not None:
            surviving_tasks = group.kill_and_remove()
    if windows_job is not None:
        if surviving_tasks and not result[2]:
            raise lean_windows_job.JobUnavailable(
                "Procesy Lean pozostawały w Job Object po zakończeniu kompilatora.")
        if result[0] == 125 and "Windows Lean job guard" in result[1]:
            raise lean_windows_job.JobUnavailable(
                "Nie udało się uruchomić kompilatora w Job Object.")
    if group is not None:
        if surviving_tasks and not result[2]:
            raise lean_cgroup.CgroupUnavailable(
                "Procesy Lean pozostawały w cgroup po zakończeniu kompilatora.")
        if result[0] == 125 and "Lean cgroup guard" in result[1]:
            raise lean_cgroup.CgroupUnavailable(
                "Nie udało się dołączyć kompilatora do ograniczonej cgroup.")
    return result


def _execute_process(command: list[str], cwd: Path, *,
                     timeout: float, log_limit: int,
                     startup=None) -> tuple[int | None, str, bool]:
    """Drain merged stdout/stderr into a bounded tail while enforcing timeout."""
    process = subprocess.Popen(
        command, cwd=cwd,
        stdin=subprocess.PIPE if startup is not None else subprocess.DEVNULL,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=0,
        start_new_session=(os.name == "posix"),
        creationflags=(subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0),
    )
    assert process.stdout is not None
    if startup is not None:
        # The helper is blocked on stdin. Failure to attach must never allow
        # any toolchain subprocess to start.
        try:
            startup(process)
        except Exception:
            if process.poll() is None:
                process.kill()
            try:
                process.wait(timeout=5)
            finally:
                if process.stdin is not None:
                    process.stdin.close()
                process.stdout.close()
            raise
    tail = bytearray()
    read_errors: list[OSError] = []

    def drain() -> None:
        try:
            while True:
                chunk = process.stdout.read(READ_CHUNK_BYTES)
                if not chunk:
                    break
                tail.extend(chunk)
                if len(tail) > log_limit:
                    del tail[:-log_limit]
        except OSError as exc:
            read_errors.append(exc)
        finally:
            process.stdout.close()

    reader = threading.Thread(target=drain, name="lean-output-drain", daemon=True)
    reader.start()
    timed_out = False
    try:
        process.wait(timeout=timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        _stop_process_group(process)
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            if process.poll() is None:
                process.kill()
            process.wait(timeout=5)

    reader.join(timeout=2)
    if reader.is_alive():
        # A descendant may have inherited stdout even if Lake has already
        # exited. Never report success before the captured output is complete.
        _stop_process_group(process)
        reader.join(timeout=2)
        # A surviving descendant means the process tree did not finish cleanly.
        # Never record a successful compilation after forcibly killing it.
        raise RuntimeError("Lean stdout pipe was left open by a child process.")
    if read_errors:
        raise RuntimeError("Could not capture Lean output.") from read_errors[0]
    return process.returncode if not timed_out else None, tail.decode("utf-8", "replace"), timed_out
