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
        record[tool] = {
            "resolution": "elan" if resolved else "path" if fallback else "missing",
            "binary": _binary_identity(resolved or fallback),
        }
    return _digest(record)
