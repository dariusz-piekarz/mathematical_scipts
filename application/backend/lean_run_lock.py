"""Non-blocking, cross-process lock for the trusted local Lean runner.

Only one compilation for an application checkout may be active at a time.
The OS lock is released automatically if the owning process crashes.
This is resource coordination, not an isolation boundary for untrusted code.
"""
from __future__ import annotations

from contextlib import contextmanager
import errno
import os
from pathlib import Path
import stat
from typing import Iterator


class RunnerBusy(RuntimeError):
    """Another process is currently compiling a Lean file for this checkout."""


class RunnerLockUnavailable(RuntimeError):
    """The runner cannot safely acquire its shared lock file."""


@contextmanager
def exclusive(lean_root: Path) -> Iterator[None]:
    """Hold an exclusive OS lock through compilation AND result persistence.

    The path is stable across workers/processes using the same checkout.
    We do not delete the lock file: unlinking it would allow split lock
    ownership if two processes kept different open file descriptors.
    """
    lock_dir = lean_root.resolve().parent / "data" / "lean_runs"
    try:
        lock_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
        path = lock_dir / ".runner.lock"
        flags = os.O_CREAT | os.O_RDWR | getattr(os, "O_BINARY", 0)
        flags |= getattr(os, "O_NOFOLLOW", 0)
        fd = os.open(path, flags, 0o600)
    except OSError as exc:
        raise RunnerLockUnavailable("Nie można otworzyć blokady runnera Lean.") from exc
    locked = False
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise RunnerLockUnavailable("Blokada runnera Lean nie jest zwykłym plikiem.")
        # Windows msvcrt.locking requires a nonempty file and a stable offset.
        if os.fstat(fd).st_size == 0:
            os.write(fd, b"\0")
        os.lseek(fd, 0, os.SEEK_SET)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(fd, msvcrt.LK_NBLCK, 1)
            elif os.name == "posix":
                import fcntl
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            else:
                raise RunnerLockUnavailable("Brak bezpiecznej blokady na tym systemie.")
            locked = True
        except OSError as exc:
            if exc.errno in (errno.EACCES, errno.EAGAIN, errno.EWOULDBLOCK) or getattr(exc, "winerror", None) in (32, 33):
                raise RunnerBusy("Inny proces już uruchamia formalizację Lean.") from exc
            raise RunnerLockUnavailable("Nie można uzyskać blokady runnera Lean.") from exc
        yield
    except OSError as exc:
        raise RunnerLockUnavailable("Błąd pliku blokady runnera Lean.") from exc
    finally:
        try:
            if locked:
                os.lseek(fd, 0, os.SEEK_SET)
                if os.name == "nt":
                    import msvcrt
                    msvcrt.locking(fd, msvcrt.LK_UNLCK, 1)
                elif os.name == "posix":
                    import fcntl
                    fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)
