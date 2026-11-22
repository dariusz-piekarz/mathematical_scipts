"""Bounded output capture for locally approved Lean processes.

A registered Lean file is trusted input to the local toolchain. This is not a
sandbox for arbitrary user-supplied Lean code or an isolation boundary.
"""
from __future__ import annotations

import os
from pathlib import Path
import signal
import subprocess
import threading

MAX_LOG_BYTES = 16000
READ_CHUNK_BYTES = 8192


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
    log_limit: int = MAX_LOG_BYTES,
) -> tuple[int | None, str, bool]:
    """Return (exit code, output tail, timed out) using bounded RAM for output.

    stdout and stderr share one pipe. A daemon reader drains it continuously
    while retaining only the latest ``log_limit`` bytes in memory. Descendants
    that retain stdout open after the main process exits are treated as an error.
    """
    if timeout <= 0 or log_limit <= 0:
        raise ValueError("Execution limits must be positive.")
    process = subprocess.Popen(
        command, cwd=cwd, stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=0,
        start_new_session=(os.name == "posix"),
        creationflags=(subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0),
    )
    assert process.stdout is not None
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
