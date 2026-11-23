"""Version-sensitive, bounded evidence about local Lake dependencies and tool binaries.

Only used for cache invalidation. Not a sandbox or a complete reproducible
build attestation: ignored build artifacts and remote sources are not hashed.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess

MAX_PACKAGES = 64
MAX_BINARY_BYTES = 512 * 1024 * 1024
SHA_PATTERN = re.compile(r"[0-9a-f]{40,64}\Z")


def _digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _git(directory: Path, *arguments: str) -> str:
    git = shutil.which("git")
    if git is None:
        raise ValueError("Git is required to inspect installed Lake dependencies")
    try:
        process = subprocess.run(
            [git, "-c", "core.fsmonitor=false", "-C", str(directory), *arguments],
            stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, check=False, timeout=15, text=True,
            encoding="utf-8", errors="replace",
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ValueError("Cannot inspect installed Lake dependency") from exc
    if process.returncode != 0:
        raise ValueError("Installed Lake dependency cannot be checked with Git")
    return process.stdout.strip()


def external_packages_sha256(lean_root: Path) -> str:
    """Hash materialized package identities; reject dirty/unverifiable Git trees.

    A missing .lake/packages is recorded distinctly, not treated as verified.
    Each installed package must be a clean Git checkout. This catches tracked
    edits and ordinary untracked changes; ignored build outputs are excluded.
    """
    packages = lean_root / ".lake" / "packages"
    if not packages.exists():
        return _digest({"state": "not_installed"})
    if packages.is_symlink() or not packages.is_dir():
        raise ValueError("Lake packages root is not a real directory")
    paths = sorted(packages.iterdir(), key=lambda p: p.name)
    if len(paths) > MAX_PACKAGES:
        raise ValueError("Too many Lake packages")
    found: list[dict[str, str]] = []
    for package in paths:
        if package.is_symlink() or not package.is_dir() or not (
            (package / ".git").exists()
        ):
            raise ValueError("Lake dependency is not a Git checkout")
        # Reject repos whose toplevel is not this package (parent repo fallback).
        top = Path(_git(package, "rev-parse", "--show-toplevel")).resolve()
        if top != package.resolve():
            raise ValueError("Lake dependency Git root does not match package path")
        commit = _git(package, "rev-parse", "HEAD")
        if not SHA_PATTERN.fullmatch(commit):
            raise ValueError("Invalid Lake dependency commit")
        if _git(package, "status", "--porcelain", "--untracked-files=normal"):
            raise ValueError("Modified or untracked Lake dependency (fail closed)")
        found.append({"name": package.name, "commit": commit})
    return _digest({"state": "materialized", "packages": found})


def _binary_identity(executable: str | None) -> dict[str, str]:
    if executable is None:
        return {"state": "missing"}
    path = Path(executable).expanduser().resolve()
    if not path.is_file():
        # A PATH advertisement is not a verified executable. Record that
        # uncertainty in the digest rather than pretending its bytes were read.
        return {"state": "unresolved", "path": str(path)}
    size = path.stat().st_size
    if size > MAX_BINARY_BYTES:
        raise ValueError("Unusually large Lean tool executable")
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for part in iter(lambda: stream.read(64 * 1024), b""):
            digest.update(part)
    return {"state": "present", "path": str(path), "sha256": digest.hexdigest()}


def _elan_which(lean_root: Path, command: str) -> str | None:
    elan = shutil.which("elan")
    if elan is None or shutil.which("lake") is None:
        return None
    try:
        result = subprocess.run(
            [elan, "which", command],
            cwd=lean_root, stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            check=False, timeout=4, text=True, encoding="utf-8",
            errors="replace",
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0:
        return None
    target = result.stdout.strip()
    return target if target else None


def executable_toolchain_sha256(lean_root: Path) -> str:
    """Digest actual executable bytes, using elan's resolved paths when possible.

    When elan cannot resolve a toolchain, PATH executables are still hashed and
    the resolution mode is recorded. This is provenance evidence, not a claim
    that the environment is fully reproducible.
    """
    record = {}
    for tool in ("lean", "lake"):
        resolved = _elan_which(lean_root, tool)
        fallback = shutil.which(tool)
        binary = _binary_identity(resolved or fallback)
        if binary["state"] != "present":
            # An inaccessible/advertised-but-missing program cannot establish
            # executable provenance. Use one stable unverified state even when
            # another component temporarily overrides PATH resolution.
            record[tool] = {"resolution": "not_verified",
                            "binary": {"state": "missing"}}
        else:
            record[tool] = {
                "resolution": "elan" if resolved else "path",
                "binary": binary,
            }
    return _digest(record)


MAX_OLEAN_FILES = 120000
MAX_OLEAN_HASH_BYTES = 64 * 1024 * 1024


def _olean_tree(root: Path, *, label: str, budget: list[int],
                counter: list[int] | None = None) -> dict[str, object]:
    """Inspect one installed Lake .olean tree without unbounded I/O.

    Every artifact contributes its name, size, mtime, ctime and file identity.
    File content is additionally SHA256-hashed while the global I/O budget
    permits. Partial coverage is explicitly encoded in the fingerprint.
    """
    if root.is_symlink():
        raise ValueError("Symlinked Lake artifact root")
    if not root.exists():
        return {"label": label, "state": "not_built"}
    if not root.is_dir():
        raise ValueError("Lake artifact root is not a directory")
    if counter is None:
        counter = [0]
    # Store lexical relative names once; they determine both sorting and
    # the serialized identity. No filesystem observation is cached.
    paths: list[tuple[str, Path]] = []
    for directory, dirs, names in os.walk(root, followlinks=False):
        base = Path(directory)
        if any((base / name).is_symlink() for name in dirs):
            raise ValueError("Symlinked Lake artifact directory")
        # Resolve the lexical relative directory at most once, and only if
        # it contains an .olean candidate. os.walk yields basename entries,
        # so joining the POSIX relative prefix preserves the existing schema.
        relative_directory: str | None = None
        for name in names:
            # Avoid allocating Path objects for unrelated build outputs.
            # Path(".olean").suffix is empty; keep that legacy exclusion.
            if not name.endswith(".olean") or name == ".olean":
                continue
            artifact = base / name
            if artifact.is_symlink():
                raise ValueError("Symlinked Lake .olean artifact")
            if relative_directory is None:
                relative_directory = base.relative_to(root).as_posix()
            relative_name = (name if relative_directory == "."
                             else f"{relative_directory}/{name}")
            paths.append((relative_name, artifact))
            counter[0] += 1
            if counter[0] > MAX_OLEAN_FILES:
                raise ValueError("Too many Lake .olean artifacts")
    entries: list[dict[str, object]] = []
    metadata_only = 0
    for relative_name, artifact in sorted(paths, key=lambda entry: entry[0]):
        info = artifact.stat()
        # Reuse the same stat snapshot for type and identity checks; a
        # second Path.is_file() stat cannot strengthen the later fd/path
        # comparisons, and adds an OS call for every .olean artifact.
        if not stat.S_ISREG(info.st_mode):
            raise ValueError("Lake .olean artifact is not a regular file")
        entry: dict[str, object] = {
            "name": relative_name,
            "size": info.st_size,
            "mtime_ns": info.st_mtime_ns,
            "ctime_ns": info.st_ctime_ns,
            "inode": info.st_ino,
        }
        if info.st_size <= budget[0]:
            digest = hashlib.sha256()
            # The stat-based budget must bound actual reads too. A growing
            # file must not turn a 64 MiB fingerprint budget into unlimited I/O.
            with artifact.open("rb") as stream:
                remaining = info.st_size
                while remaining:
                    chunk = stream.read(min(128 * 1024, remaining))
                    if not chunk:
                        raise ValueError("Lake .olean artifact truncated while fingerprinting")
                    digest.update(chunk)
                    remaining -= len(chunk)
                if stream.read(1):
                    raise ValueError("Lake .olean artifact grew while fingerprinting")
                # Stat the *opened descriptor*, not merely its path. An
                # artifact swapped between path.stat() and open() can have
                # identical size while pointing at different file contents.
                opened = os.fstat(stream.fileno())
                if (not stat.S_ISREG(opened.st_mode)
                        or info.st_dev != opened.st_dev
                        or info.st_ino != opened.st_ino):
                    raise ValueError("Lake .olean artifact identity changed while fingerprinting")
            # Windows may report different creation-time semantics for fstat
            # versus stat(path). Compare timestamp fields using path.stat()
            # before and after, but demand descriptor identity as above.
            after = artifact.stat()
            if (info.st_size != opened.st_size or info.st_size != after.st_size
                    or info.st_mtime_ns != after.st_mtime_ns
                    or info.st_ctime_ns != after.st_ctime_ns
                    or info.st_ino != after.st_ino
                    or info.st_dev != after.st_dev):
                raise ValueError("Lake .olean artifact changed while fingerprinting")
            entry["sha256"] = digest.hexdigest()
            budget[0] -= info.st_size
        else:
            entry["content"] = "metadata_only"
            metadata_only += 1
        entries.append(entry)
    return {"label": label, "state": "built",
            "coverage": "metadata_only" if metadata_only else "content_sha256",
            "artifacts": entries}


def compiled_artifacts_sha256(lean_root: Path) -> str:
    """Fingerprint project and package .olean caches with explicit I/O bounds.

    Mathlib may have gigabytes of .olean files. This function deliberately
    does not claim full content verification once the content budget is spent.
    A missing build tree and a populated build tree never have the same digest.
    """
    budget = [MAX_OLEAN_HASH_BYTES]
    counter = [0]
    roots: list[tuple[str, Path]] = [
        ("project", lean_root / ".lake" / "build" / "lib" / "lean"),
    ]
    packages = lean_root / ".lake" / "packages"
    if packages.is_symlink():
        raise ValueError("Symlinked Lake packages root")
    if packages.exists():
        if not packages.is_dir():
            raise ValueError("Lake packages root is not a directory")
        for package in sorted(packages.iterdir(), key=lambda p: p.name):
            if package.is_symlink() or not package.is_dir():
                raise ValueError("Invalid Lake package directory")
            roots.append((f"package/{package.name}",
                          package / ".lake" / "build" / "lib" / "lean"))
    if len(roots) > MAX_PACKAGES + 1:
        raise ValueError("Too many Lake artifact roots")
    records = [_olean_tree(path, label=label, budget=budget, counter=counter)
               for label, path in roots]
    return _digest({"schema": 1, "hash_budget_bytes": MAX_OLEAN_HASH_BYTES,
                    "roots": records})
