"""Local, version-bound records of actual Lean subprocess results.

Never treats a cached success as a proof certificate. No canonical TeX/SQLite writes.
"""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import tempfile
from typing import Any

from backend import lean_environment

DEFAULT_RESULTS_DIR = Path(__file__).resolve().parents[1] / "data" / "lean_runs"
ID_PATTERN = re.compile(r"[A-Za-z0-9_-]{1,100}\Z")
HEX_DIGEST = re.compile(r"[0-9a-f]{64}\Z")
STORED_STATUSES = {"compiled", "failed", "timeout"}
SCHEMA_VERSION = 5
MAX_STORED_LOG = 16000
MAX_RECORD_BYTES = 30000
FINGERPRINT_DIGEST_FIELDS = (
    "source_document_sha256", "source_binding_sha256", "lean_sha256",
    "project_sources_sha256", "external_packages_sha256",
    "compiled_artifacts_sha256", "executable_toolchain_sha256",
    "toolchain_sha256",
)
FINGERPRINT_FIELDS = frozenset((*FINGERPRINT_DIGEST_FIELDS, "declared_toolchain"))
RECORD_FIELDS = frozenset((
    *FINGERPRINT_FIELDS, "schema_version", "formalization_id",
    "proof_status", "detail", "log", "finished_at", "certificate",
))


def _valid_fingerprint_fields(value: object) -> bool:
    return (
        isinstance(value, dict) and set(value) == FINGERPRINT_FIELDS
        and all(isinstance(value[field], str) and HEX_DIGEST.fullmatch(value[field])
                for field in FINGERPRINT_DIGEST_FIELDS)
        and isinstance(value["declared_toolchain"], str)
        and len(value["declared_toolchain"]) <= 160
    )


def _unique_json_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    """Reject duplicate JSON members rather than accepting last-key-wins."""
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate Lean run record field")
        result[key] = value
    return result


def result_dir(override: Path | None = None) -> Path:
    if override is not None:
        return Path(override)
    return Path(os.environ.get("MATLIB_LEAN_RESULTS_DIR", str(DEFAULT_RESULTS_DIR))).expanduser()


def _project_sources_sha256(lean_root: Path) -> str:
    """Digest every local Lean source, not only the selected source's direct imports.

    This is deliberately a conservative superset of local imports. The file
    names and their bytes are both hashed, so adding/removing/renaming a module
    also invalidates stored results. External Mathlib sources and binaries are
    NOT covered; see the security audit.
    """
    root = lean_root / "src"
    if not root.is_dir() or root.is_symlink():
        raise ValueError("Missing or symlinked Lean src root")
    sources: list[Path] = []
    for directory, dirs, files in os.walk(root, followlinks=False):
        base = Path(directory)
        if any((base / name).is_symlink() for name in dirs):
            raise ValueError("Symlinked Lean source directory")
        for name in files:
            file = base / name
            if file.is_symlink():
                raise ValueError("Symlinked Lean source file")
            if file.suffix == ".lean":
                sources.append(file)
    if not sources:
        raise ValueError("No local Lean sources")
    if len(sources) > 4096:
        raise ValueError("Too many local Lean sources to fingerprint")
    digest = hashlib.sha256()
    # Separate names and contents with explicit length prefixes.
    for file in sorted(sources, key=lambda f: f.relative_to(root).as_posix()):
        rel = file.relative_to(root).as_posix().encode("utf-8")
        digest.update(len(rel).to_bytes(4, "big"))
        digest.update(rel)
        try:
            size = file.stat().st_size
            if size > 64 * 1024 * 1024:
                raise ValueError("Oversized local Lean module")
            digest.update(size.to_bytes(8, "big"))
            with file.open("rb") as inp:
                for chunk in iter(lambda: inp.read(64 * 1024), b""):
                    digest.update(chunk)
        except OSError:
            raise
    return digest.hexdigest()


def fingerprint(source_sha256: str, lean_file: Path, lean_root: Path,
                source_binding_sha256: str) -> dict[str, str]:
    """Bind execution to source bytes AND exact indexed theorem ownership."""
    if not HEX_DIGEST.fullmatch(source_sha256):
        raise ValueError("Invalid indexed document SHA256")
    if not isinstance(source_binding_sha256, str) or not HEX_DIGEST.fullmatch(source_binding_sha256):
        raise ValueError("Missing or invalid indexed source binding SHA256")
    lean_sha256 = hashlib.sha256(lean_file.read_bytes()).hexdigest()
    project_sources_sha256 = _project_sources_sha256(lean_root)
    external_packages_sha256 = lean_environment.external_packages_sha256(lean_root)
    compiled_artifacts_sha256 = lean_environment.compiled_artifacts_sha256(lean_root)
    executable_toolchain_sha256 = lean_environment.executable_toolchain_sha256(lean_root)
    inputs: dict[str, str | None] = {}
    for name in ("lean-toolchain", "lakefile.toml", "lakefile.lean",
                 "lake-manifest.json", "manifest.json"):
        path = lean_root / name
        inputs[name] = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
    toolchain_sha256 = hashlib.sha256(
        json.dumps(inputs, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    declared_toolchain = (lean_root / "lean-toolchain").read_text(encoding="utf-8").strip() \
        if (lean_root / "lean-toolchain").is_file() else "unavailable"
    return {"source_document_sha256": source_sha256,
            "source_binding_sha256": source_binding_sha256,
            "lean_sha256": lean_sha256,
            "project_sources_sha256": project_sources_sha256,
            "external_packages_sha256": external_packages_sha256,
            "compiled_artifacts_sha256": compiled_artifacts_sha256,
            "executable_toolchain_sha256": executable_toolchain_sha256,
            "toolchain_sha256": toolchain_sha256,
            "declared_toolchain": declared_toolchain[:160]}


def _record_path(identifier: str, override: Path | None) -> Path:
    if not ID_PATTERN.fullmatch(identifier):
        raise ValueError("Invalid formalization ID")
    return result_dir(override) / (identifier + ".json")


def last_run(identifier: str, expected: dict[str, str], *,
             results_root: Path | None = None) -> dict[str, Any]:
    """Return only a well-formed, version-matching local Lean execution result.

    Cached execution diagnostics are never proof certificates. A writable local
    file is not cryptographic attestation of a past execution.
    """
    path = _record_path(identifier, results_root)
    invalid = {"proof_status": "not_run", "run_cached": False,
               "run_record_invalid": True}
    if not _valid_fingerprint_fields(expected):
        return invalid
    try:
        if path.is_symlink():
            return invalid
        if not path.is_file():
            return {"proof_status": "not_run", "run_cached": False}
        # The path may change after the checks above. O_NOFOLLOW prevents
        # following the final symlink on supporting POSIX filesystems.
        # A descriptor identity check is also needed on Windows, where
        # O_NOFOLLOW may not exist. Parent directories remain outside this
        # local trust boundary.
        flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(path, flags)
        with os.fdopen(descriptor, "rb") as stream:
            opened = os.fstat(stream.fileno())
            named = path.lstat()
            def common_identity(info: os.stat_result) -> tuple[int, int, int, int]:
                # Windows Path.lstat and os.fstat can report different st_ctime
                # semantics for the *same* file (creation vs change time).
                # Use the stable file ID, size and modification time for the
                # cross-API check; compare ctime only within the same API.
                return (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns)
            def same_object(left: os.stat_result, right: os.stat_result) -> bool:
                return (common_identity(left) == common_identity(right)
                        and (os.name == "nt"
                             or left.st_ctime_ns == right.st_ctime_ns))
            if (not stat.S_ISREG(opened.st_mode)
                    or not stat.S_ISREG(named.st_mode)
                    or not same_object(opened, named)):
                raise ValueError("Lean run record was replaced before reading")
            # Bound actual bytes even if the file grows after the first stat.
            raw = stream.read(MAX_RECORD_BYTES + 1)
            named_after = path.lstat()
            opened_after = os.fstat(stream.fileno())
            if (not stat.S_ISREG(named_after.st_mode)
                    or not same_object(opened, opened_after)
                    or not same_object(named, named_after)
                    or not same_object(opened, named_after)
                    or opened.st_ctime_ns != opened_after.st_ctime_ns
                    or named.st_ctime_ns != named_after.st_ctime_ns):
                raise ValueError("Lean run record changed during reading")
        if len(raw) > MAX_RECORD_BYTES:
            raise ValueError("Oversized Lean run record")
        record = json.loads(raw.decode("utf-8"), object_pairs_hook=_unique_json_keys)
        if (not isinstance(record, dict)
                or set(record) != RECORD_FIELDS
                or type(record["schema_version"]) is not int
                or record["schema_version"] != SCHEMA_VERSION
                or record["formalization_id"] != identifier
                or not isinstance(record["proof_status"], str)
                or record["proof_status"] not in STORED_STATUSES
                or record["certificate"] is not False
                or not _valid_fingerprint_fields({
                    name: record[name] for name in FINGERPRINT_FIELDS
                })
                or not isinstance(record["finished_at"], str)
                or not isinstance(record["detail"], str)
                or not isinstance(record["log"], str)
                or len(record["detail"]) > 1000
                or len(record["log"]) > MAX_STORED_LOG):
            raise ValueError("Invalid Lean run record schema")
        completed = datetime.fromisoformat(record["finished_at"])
        if completed.tzinfo is None or completed.utcoffset() is None:
            raise ValueError("Lean run timestamp is missing timezone")
    except (OSError, ValueError, UnicodeError, TypeError, OverflowError,
            RecursionError):
        return invalid
    if any(record[key] != expected[key] for key in FINGERPRINT_FIELDS):
        return {"proof_status": "not_run", "run_cached": False,
                "previous_run_outdated": True}
    return {"proof_status": record["proof_status"], "run_cached": True,
            "last_run_at": record["finished_at"],
            "last_run_detail": record["detail"],
            "last_run_log": record["log"],
            "certificate": False}

def save_run(identifier: str, expected: dict[str, str], *, proof_status: str,
             detail: str, log: str = "", results_root: Path | None = None) -> dict[str, Any]:
    """Atomically save the latest actual result; callers must not store synthetic success."""
    if proof_status not in STORED_STATUSES:
        raise ValueError("Not an actual Lean process outcome")
    if not _valid_fingerprint_fields(expected):
        raise ValueError("Incomplete or invalid run fingerprint")
    path = _record_path(identifier, results_root)
    record = {"schema_version": SCHEMA_VERSION, "formalization_id": identifier,
              **expected, "proof_status": proof_status,
              "detail": str(detail)[:1000], "log": str(log)[-MAX_STORED_LOG:],
              "finished_at": datetime.now(timezone.utc).isoformat(),
              "certificate": False}
    # The read path enforces a *byte* limit. Truncating logs only by Unicode
    # code points could otherwise create a successful save which cannot be read
    # back (e.g. a long Lean error log containing non-ASCII names or symbols).
    def serialized() -> bytes:
        return (json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")

    payload = serialized()
    if len(payload) > MAX_RECORD_BYTES:
        original_log = record["log"]
        lower, upper = 0, len(original_log)
        # Preserve the most recent diagnostic lines; JSON escaping and UTF-8
        # can take more than one byte per input character.
        while lower < upper:
            middle = (lower + upper + 1) // 2
            record["log"] = original_log[-middle:] if middle else ""
            if len(serialized()) <= MAX_RECORD_BYTES:
                lower = middle
            else:
                upper = middle - 1
        record["log"] = original_log[-lower:] if lower else ""
        payload = serialized()
        if len(payload) > MAX_RECORD_BYTES:
            raise ValueError("Lean run metadata exceeds record byte limit")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(mode="wb", dir=path.parent,
                                         prefix=f".{identifier}.", suffix=".tmp",
                                         delete=False) as out:
            temporary = Path(out.name)
            out.write(payload)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return record
