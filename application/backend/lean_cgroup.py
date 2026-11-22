"""Opt-in Linux cgroup v2 aggregate-memory protection for local Lean runs.

Requires a delegated writable cgroup v2 subtree with the memory controller
already enabled. Never modifies the parent's controller configuration.
"""
from __future__ import annotations

import os
from pathlib import Path
import re
import sys
import tempfile
import time

CGROUP_MOUNT = Path("/sys/fs/cgroup")
MIN_MEMORY_MB = 512
MAX_MEMORY_MB = 65536


class CgroupUnavailable(RuntimeError):
    """Requested aggregate-memory protection cannot be enforced."""


def configured_total_memory_mb() -> int | None:
    raw = os.environ.get("MATLIB_LEAN_TOTAL_MEMORY_MB")
    if raw is None:
        return None
    if not re.fullmatch(r"[1-9][0-9]{0,4}", raw):
        raise ValueError("MATLIB_LEAN_TOTAL_MEMORY_MB musi być liczbą 512–65536 MiB.")
    limit = int(raw)
    if not MIN_MEMORY_MB <= limit <= MAX_MEMORY_MB:
        raise ValueError("MATLIB_LEAN_TOTAL_MEMORY_MB musi być z zakresu 512–65536 MiB.")
    return limit


def _delegated_parent() -> Path:
    if not sys.platform.startswith("linux") or not (CGROUP_MOUNT / "cgroup.controllers").is_file():
        raise CgroupUnavailable("Brak hierarchii Linux cgroup v2.")
    try:
        lines = Path("/proc/self/cgroup").read_text(encoding="ascii").splitlines()
        entries = [line[3:] for line in lines if line.startswith("0::")]
        if len(entries) != 1 or not entries[0].startswith("/"):
            raise CgroupUnavailable("Brak jednoznacznej ścieżki własnej cgroup v2.")
        root = CGROUP_MOUNT.resolve()
        parent = (root / entries[0].lstrip("/")).resolve()
        if not parent.is_relative_to(root) or not parent.is_dir():
            raise CgroupUnavailable("Ścieżka cgroup wykracza poza punkt montowania.")
        if "memory" not in (parent / "cgroup.subtree_control").read_text(encoding="ascii").split():
            raise CgroupUnavailable("Kontroler memory nie jest delegowany do podgrup.")
    except (OSError, UnicodeError) as exc:
        raise CgroupUnavailable("Nie można sprawdzić delegacji Linux cgroup v2.") from exc
    return parent


def available() -> bool:
    try:
        _delegated_parent()
    except CgroupUnavailable:
        return False
    return True  # Actual filesystem permission is checked during creation.


class ProcessGroup:
    def __init__(self, path: Path):
        self.path = path

    @classmethod
    def create(cls, limit_mb: int) -> "ProcessGroup":
        if type(limit_mb) is not int or not MIN_MEMORY_MB <= limit_mb <= MAX_MEMORY_MB:
            raise ValueError("Niepoprawny limit pamięci cgroup.")
        parent = _delegated_parent()
        try:
            path = Path(tempfile.mkdtemp(prefix="matlib-lean-", dir=parent))
        except OSError as exc:
            raise CgroupUnavailable("Nie można utworzyć izolowanej cgroup Lean.") from exc
        group = cls(path)
        try:
            if not (path / "cgroup.kill").exists():
                raise CgroupUnavailable("Jądro nie udostępnia cgroup.kill.")
            (path / "memory.max").write_text(str(limit_mb * 1024 * 1024), encoding="ascii")
            (path / "memory.oom.group").write_text("1", encoding="ascii")
            (path / "memory.swap.max").write_text("0", encoding="ascii")
            if (path / "memory.max").read_text(encoding="ascii").strip() != str(limit_mb * 1024 * 1024):
                raise CgroupUnavailable("Limit pamięci cgroup nie został przyjęty.")
        except (OSError, CgroupUnavailable) as exc:
            try:
                path.rmdir()
            except OSError:
                pass
            raise CgroupUnavailable("Nie można wymusić limitu pamięci cgroup.") from exc
        return group

    def kill_and_remove(self) -> bool:
        """Kill remaining descendants; return whether any tasks survived the main PID."""
        populated: bool | None = None
        try:
            events = dict(line.split(maxsplit=1) for line in
                          (self.path / "cgroup.events").read_text(encoding="ascii").splitlines())
            populated = events.get("populated") == "1"
        except (OSError, ValueError):
            pass
        try:
            (self.path / "cgroup.kill").write_text("1", encoding="ascii")
        except OSError as exc:
            raise CgroupUnavailable("Nie udało się zakończyć procesów cgroup Lean.") from exc
        for _ in range(20):
            try:
                self.path.rmdir()
                if populated is None:
                    raise CgroupUnavailable("Nie można zweryfikować zakończenia procesów cgroup Lean.")
                return populated
            except OSError:
                time.sleep(0.05)
        raise CgroupUnavailable("Nie można usunąć cgroup Lean po zatrzymaniu procesu.")
