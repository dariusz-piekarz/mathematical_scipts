"""RT-09b: bounded, read-only manifests of a selected artifact tree.

The expected manifest SHA must arrive through a trusted channel. A digest
shipped beside an untrusted bundle is not authentication. This does not prove
an import closure, reproducibility, executable provenance or offline readiness.
No artifact is executed or extracted; the existing Lean runner is unchanged.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import time

from scripts import lean_mathlib_source_probe as sources

MAX_ENTRIES = 20000
MAX_FILE_BYTES = 512 * 1024 * 1024
MAX_TOTAL_BYTES = 2 * 1024 * 1024 * 1024
SCOPED_FIXTURE_BYTES = 5 * 1024**3 // 2
DEFAULT_SCOPE = 'selected_artifact_tree'
SCOPED_FIXTURE_SCOPE = 'trusted_scoped_fixture_tree'
MAX_MANIFEST_BYTES = 8 * 1024 * 1024
MAX_DEPTH = 32
SCAN_SECONDS = 120
CHUNK = 1024 * 1024
HEX = re.compile(r"[0-9a-f]{64}\Z")
COMPONENT = re.compile(r"[A-Za-z0-9_.-]{1,120}\Z")
RESERVED = {"con", "prn", "aux", "nul", *(f"com{i}" for i in range(1, 10)),
            *(f"lpt{i}" for i in range(1, 10))}


def total_budget(scope: str) -> int:
    if scope == DEFAULT_SCOPE:
        return MAX_TOTAL_BYTES
    if scope == SCOPED_FIXTURE_SCOPE:
        return SCOPED_FIXTURE_BYTES
    raise ValueError('Unknown artifact scope')


def encoded(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=True) + "\n").encode("ascii")


def digest(value: object) -> str:
    return hashlib.sha256(encoded(value)).hexdigest()


def component(name: str) -> None:
    if (not COMPONENT.fullmatch(name) or name in {".", ".."}
            or name.endswith((".", " ")) or name.split(".")[0].lower() in RESERVED):
        raise ValueError("Nonportable artifact path")


def identity(info: os.stat_result) -> tuple:
    # Windows path queries may return cached change times unlike fstat. Use
    # creation time for cross-query identity there; compare descriptor change
    # times separately across the actual read below. Content is always hashed.
    stamp = info.st_birthtime_ns if os.name == "nt" else info.st_ctime_ns
    return (info.st_dev, info.st_ino, info.st_mode, info.st_nlink,
            info.st_size, info.st_mtime_ns, stamp)


def checked_stat(path: Path) -> os.stat_result:
    info = path.lstat()
    if (stat.S_ISLNK(info.st_mode)
            or getattr(info, "st_file_attributes", 0) & 0x400
            or not (stat.S_ISDIR(info.st_mode) or stat.S_ISREG(info.st_mode))):
        raise ValueError("Linked, reparse or special artifact path")
    if stat.S_ISREG(info.st_mode) and info.st_nlink != 1:
        raise ValueError("Hardlinked artifact file")
    return info


def root_path(root: Path) -> Path:
    # Check lexical ancestors before resolving: resolving first hides links.
    root = Path(os.path.abspath(root))
    for path in reversed((root, *root.parents)):
        if not stat.S_ISDIR(checked_stat(path).st_mode):
            raise ValueError("Artifact root must be a real directory")
    # Normalize Windows 8.3 aliases only after checking lexical ancestors.
    # Output containment must compare two canonical paths, not short vs long.
    return root.resolve(strict=True)


def inventory(root: Path, deadline: float) -> dict[str, tuple]:
    found = {}
    pending = [(root, "", 0)]
    while pending:
        directory, prefix, depth = pending.pop()
        if time.monotonic() >= deadline:
            raise ValueError("Artifact scan deadline exceeded")
        found[prefix] = identity(checked_stat(directory))
        with os.scandir(directory) as entries:
            names = set()
            for entry in entries:
                if time.monotonic() >= deadline:
                    raise ValueError("Artifact scan deadline exceeded")
                component(entry.name)
                key = entry.name.casefold()
                if key in names:
                    raise ValueError("Case-colliding artifact paths")
                names.add(key)
                relative = prefix + "/" + entry.name if prefix else entry.name
                if relative in found or len(found) >= MAX_ENTRIES:
                    raise ValueError("Artifact entry budget exceeded")
                info = checked_stat(Path(entry.path))
                found[relative] = identity(info)
                if stat.S_ISDIR(info.st_mode):
                    if depth >= MAX_DEPTH:
                        raise ValueError("Artifact depth budget exceeded")
                    pending.append((Path(entry.path), relative, depth + 1))
    return found


def hash_file(path: Path, before: tuple, deadline: float) -> str:
    size = before[4]
    if size > MAX_FILE_BYTES:
        raise ValueError("Artifact file byte budget exceeded")
    if identity(checked_stat(path)) != before:
        raise ValueError("Artifact changed before read")
    flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(path, flags)
    with os.fdopen(fd, "rb") as handle:
        opened = os.fstat(handle.fileno())
        if identity(opened) != before:
            raise ValueError("Artifact changed while opening")
        remaining = size
        sha = hashlib.sha256()
        while remaining:
            if time.monotonic() >= deadline:
                raise ValueError("Artifact hash deadline exceeded")
            block = handle.read(min(CHUNK, remaining))
            if not block:
                raise ValueError("Artifact truncated during read")
            sha.update(block)
            remaining -= len(block)
        extra = handle.read(1)
        finished = os.fstat(handle.fileno())
        if (extra or identity(finished) != before
                or finished.st_ctime_ns != opened.st_ctime_ns):
            raise ValueError("Artifact changed during read")
    if identity(checked_stat(path)) != before:
        raise ValueError("Artifact path changed after read")
    return sha.hexdigest()


def provenance(report: dict) -> dict:
    """Validate source evidence shape, without claiming to authenticate it."""
    expected = {"schema", "status", "checkout_sha", "lean_toolchain", "mathlib_revision",
                "package_count", "packages", "lock_sha256", "upstream_manifest_sha256",
                "clean_checkout_sha256", "artifact_bytes_verified", "offline_ready",
                "execution_allowed", "certificate"}
    if type(report) is not dict or set(report) != expected:
        raise ValueError("Incomplete source closure evidence")
    if (type(report["schema"]) is not int or report["schema"] != 1
            or report["status"] != "mathlib_source_closure_verified"
            or type(report["checkout_sha"]) is not str
            or not sources.REV.fullmatch(report["checkout_sha"])
            or report["lean_toolchain"] != sources.TOOLCHAIN
            or report["mathlib_revision"] != sources.PIN
            or type(report["package_count"]) is not int or report["package_count"] != 9):
        raise ValueError("Unexpected source closure identity")
    for field in ("lock_sha256", "upstream_manifest_sha256", "clean_checkout_sha256"):
        if type(report[field]) is not str or not HEX.fullmatch(report[field]):
            raise ValueError("Invalid source closure digest")
    for field in ("artifact_bytes_verified", "offline_ready", "execution_allowed", "certificate"):
        if report[field] is not False:
            raise ValueError("Unsupported source evidence claim")
    lock = sources.read_json(Path(__file__).resolve().parents[1] / "lean/mathlib-source-lock.json")
    if (sources.package_map(report["packages"], lake=False) != sources.validate_lock(lock)
            or report["lock_sha256"] != sources.environment._digest(lock)):
        raise ValueError("Source closure differs from pinned lock")
    return json.loads(encoded(report))


def create_manifest(root: Path, source_report: dict, *, scope=DEFAULT_SCOPE) -> dict:
    byte_budget = total_budget(scope)
    source_report = provenance(source_report)
    root = root_path(root)
    deadline = time.monotonic() + SCAN_SECONDS
    before = inventory(root, deadline)
    files = [(name, info) for name, info in before.items() if stat.S_ISREG(info[2])]
    total = sum(info[4] for _, info in files)
    if not files or total > byte_budget:
        raise ValueError("Empty artifact set or total byte budget exceeded")
    records = []
    for name in sorted(before):
        if not name:
            continue
        info = before[name]
        if stat.S_ISDIR(info[2]):
            records.append({"path": name, "kind": "directory"})
        else:
            records.append({"path": name, "kind": "file", "size": info[4],
                            "sha256": hash_file(root / name, info, deadline)})
    if inventory(root, deadline) != before:
        raise ValueError("Artifact tree changed during scan")
    manifest = {"schema": 1, "scope": scope,
                "source_closure": source_report, "entries": records,
                "file_count": len(files), "total_bytes": total,
                "offline_ready": False, "execution_allowed": False, "certificate": False}
    if len(encoded(manifest)) > MAX_MANIFEST_BYTES:
        raise ValueError("Artifact manifest byte budget exceeded")
    return manifest


def validate_manifest_structure(manifest: dict, *, scope=DEFAULT_SCOPE) -> None:
    """Check persisted structure and counts without authenticating tree bytes."""
    byte_budget = total_budget(scope)
    fields = {"schema", "scope", "source_closure", "entries", "file_count", "total_bytes",
              "offline_ready", "execution_allowed", "certificate"}
    if (type(manifest) is not dict or set(manifest) != fields
            or type(manifest["schema"]) is not int or manifest["schema"] != 1
            or manifest["scope"] != scope
            or any(manifest[key] is not False for key in
                   ("offline_ready", "execution_allowed", "certificate"))):
        raise ValueError("Invalid artifact manifest structure")
    records = manifest["entries"]
    if type(records) is not list or not records or len(records) >= MAX_ENTRIES:
        raise ValueError("Invalid artifact entry budget")
    paths, portable_paths = {}, set()
    count = total = 0
    for record in records:
        if type(record) is not dict:
            raise ValueError("Invalid artifact entry")
        kind, path = record.get("kind"), record.get("path")
        if kind not in ("file", "directory") or type(path) is not str:
            raise ValueError("Invalid artifact entry kind or path")
        expected = {"path", "kind", "size", "sha256"} if kind == "file" else {"path", "kind"}
        if set(record) != expected:
            raise ValueError("Unexpected artifact entry fields")
        parts = path.split("/")
        if len(parts) > MAX_DEPTH + (kind == "file"):
            raise ValueError("Artifact depth budget exceeded")
        for part in parts:
            component(part)
        if path.casefold() in portable_paths:
            raise ValueError("Duplicate or case-colliding artifact path")
        paths[path] = kind
        portable_paths.add(path.casefold())
        if kind == "file":
            size, sha = record["size"], record["sha256"]
            if (type(size) is not int or not 0 <= size <= MAX_FILE_BYTES
                    or type(sha) is not str or not HEX.fullmatch(sha)):
                raise ValueError("Invalid artifact file size or digest")
            count += 1
            total += size
    for path in paths:
        parent = path.rpartition("/")[0]
        if parent and paths.get(parent) != "directory":
            raise ValueError("Missing artifact parent directory")
    if (type(manifest["file_count"]) is not int or manifest["file_count"] != count or count < 1
            or type(manifest["total_bytes"]) is not int or manifest["total_bytes"] != total
            or total > byte_budget or len(encoded(manifest)) > MAX_MANIFEST_BYTES):
        raise ValueError("Invalid artifact manifest counts or byte budget")


def verify_manifest(root: Path, raw: bytes, *, expected_sha256: str,
                    expected_source_report: dict, scope=DEFAULT_SCOPE) -> dict:
    total_budget(scope)
    if (type(expected_sha256) is not str or not HEX.fullmatch(expected_sha256)
            or len(raw) > MAX_MANIFEST_BYTES
            or hashlib.sha256(raw).hexdigest() != expected_sha256):
        raise ValueError("Untrusted or oversized artifact manifest")
    try:
        manifest = json.loads(raw, object_pairs_hook=sources.unique_object)
    except (RecursionError, json.JSONDecodeError) as exc:
        raise ValueError("Invalid artifact manifest JSON") from exc
    # Reconstruct the complete selected tree, including empty directories.
    # Exact comparison rejects unknown schema/fields, unsafe paths and claims;
    # none of the paths in the supplied manifest are opened.
    actual = create_manifest(root, expected_source_report, scope=scope)
    if encoded(manifest) != encoded(actual):
        raise ValueError("Artifact manifest or selected tree mismatch")
    return {"status": "selected_artifact_bytes_verified", "manifest_sha256": expected_sha256,
            "file_count": actual["file_count"], "total_bytes": actual["total_bytes"],
            "offline_ready": False, "execution_allowed": False, "certificate": False}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("create", "verify"))
    parser.add_argument("bundle", type=Path)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--lean-root", type=Path, required=True)
    parser.add_argument("--checkout-sha", required=True)
    parser.add_argument("--expected-sha256")
    args = parser.parse_args()
    report = sources.inspect_sources(args.lean_root, expected_sha=args.checkout_sha)
    if args.action == "create":
        # Writing into the bundle would change the very tree being described.
        root = root_path(args.bundle)
        if args.manifest.resolve().is_relative_to(root):
            raise ValueError("Manifest output must be outside artifact tree")
        manifest = create_manifest(root, report)
        raw = encoded(manifest)
        with args.manifest.open("xb") as handle:
            handle.write(raw)
        print(json.dumps({"manifest_sha256": hashlib.sha256(raw).hexdigest(),
                          "file_count": manifest["file_count"],
                          "total_bytes": manifest["total_bytes"]}))
    else:
        checked_stat(args.manifest)
        with args.manifest.open("rb") as handle:
            raw = handle.read(MAX_MANIFEST_BYTES + 1)
        print(json.dumps(verify_manifest(args.bundle, raw, expected_sha256=args.expected_sha256,
                                         expected_source_report=report)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
