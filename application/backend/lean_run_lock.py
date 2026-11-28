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



def _link_or_junction(path: Path) -> bool:
    """Refuse link-based redirection, including Windows directory junctions."""
    return path.is_symlink() or bool(getattr(path, "is_junction", lambda: False)())


def _same_regular_file(fd: int, path: Path) -> bool:
    """Reject replaced lock paths (particularly when O_NOFOLLOW is unavailable)."""
    try:
        opened = os.fstat(fd)
        visible = path.lstat()
    except OSError:
        return False
    return (stat.S_ISREG(opened.st_mode)
            and stat.S_ISREG(visible.st_mode)
            and opened.st_ino != 0
            and opened.st_dev == visible.st_dev
            and opened.st_ino == visible.st_ino)



@contextmanager
def exclusive(lean_root: Path) -> Iterator[None]:
    """Hold an exclusive OS lock through compilation AND result persistence.

    The path is stable across workers/processes using the same checkout.
    We do not delete the lock file: unlinking it would allow split lock
    ownership if two processes kept different open file descriptors.
    """
    lock_dir = lean_root.resolve().parent / "data" / "lean_runs"
    try:
        # Windows has no O_NOFOLLOW. Reject known symlink/junction parents
        # before creating or opening a lock path, then verify the opened inode.
        if _link_or_junction(lock_dir.parent) or _link_or_junction(lock_dir):
            raise RunnerLockUnavailable("Katalog blokady Lean jest dowiązaniem.")
        lock_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
        if _link_or_junction(lock_dir.parent) or _link_or_junction(lock_dir):
            raise RunnerLockUnavailable("Katalog blokady Lean został przekierowany.")
        path = lock_dir / ".runner.lock"
        if _link_or_junction(path):
            raise RunnerLockUnavailable("Plik blokady Lean jest dowiązaniem.")
        if path.exists() and not stat.S_ISREG(path.lstat().st_mode):
            raise RunnerLockUnavailable("Plik blokady Lean nie jest zwykłym plikiem.")
        flags = os.O_CREAT | os.O_RDWR | getattr(os, "O_BINARY", 0)
        flags |= getattr(os, "O_NOFOLLOW", 0)
        fd = os.open(path, flags, 0o600)
    except OSError as exc:
        raise RunnerLockUnavailable("Nie można otworzyć blokady runnera Lean.") from exc
    locked = False
    try:
        try:
            if not _same_regular_file(fd, path):
                raise RunnerLockUnavailable("Ścieżka blokady Lean nie wskazuje otwartego pliku.")
            # Windows msvcrt.locking requires a nonempty file and a stable offset.
            if os.fstat(fd).st_size == 0:
                os.write(fd, b"\0")
            os.lseek(fd, 0, os.SEEK_SET)
        except OSError as exc:
            raise RunnerLockUnavailable("Błąd pliku blokady runnera Lean.") from exc
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
            if (not _same_regular_file(fd, path)
                    or _link_or_junction(lock_dir.parent)
                    or _link_or_junction(lock_dir)):
                raise RunnerLockUnavailable("Ścieżka blokady Lean zmieniła się podczas blokowania.")
        except OSError as exc:
            if (exc.errno in (errno.EACCES, errno.EAGAIN, errno.EWOULDBLOCK)
                    or getattr(exc, "winerror", None) in (32, 33)):
                raise RunnerBusy("Inny proces już uruchamia formalizację Lean.") from exc
            raise RunnerLockUnavailable("Nie można uzyskać blokady runnera Lean.") from exc
        yield
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
