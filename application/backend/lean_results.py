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
import tempfile
from typing import Any

DEFAULT_RESULTS_DIR = Path(__file__).resolve().parents[1] / "data" / "lean_runs"
ID_PATTERN = re.compile(r"[A-Za-z0-9_-]{1,100}\Z")
HEX_DIGEST = re.compile(r"[0-9a-f]{64}\Z")
STORED_STATUSES = {"compiled", "failed", "timeout"}
SCHEMA_VERSION = 1
MAX_STORED_LOG = 16000
MAX_RECORD_BYTES = 30000


def result_dir(override: Path | None = None) -> Path:
    if override is not None:
        return Path(override)
    return Path(os.environ.get("MATLIB_LEAN_RESULTS_DIR", str(DEFAULT_RESULTS_DIR))).expanduser()


def fingerprint(source_sha256: str, lean_file: Path, lean_root: Path) -> dict[str, str]:
    """Bind a result to the indexed source, Lean bytes, and declared toolchain/Mathlib lock."""
    if not HEX_DIGEST.fullmatch(source_sha256):
        raise ValueError("Invalid indexed document SHA256")
    lean_sha256 = hashlib.sha256(lean_file.read_bytes()).hexdigest()
    inputs: dict[str, str | None] = {}
    for name in ("lean-toolchain", "lakefile.toml", "lake-manifest.json"):
        path = lean_root / name
        inputs[name] = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
    toolchain_sha256 = hashlib.sha256(
        json.dumps(inputs, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return {"source_document_sha256": source_sha256,
            "lean_sha256": lean_sha256,
            "toolchain_sha256": toolchain_sha256}


def _record_path(identifier: str, override: Path | None) -> Path:
    if not ID_PATTERN.fullmatch(identifier):
        raise ValueError("Invalid formalization ID")
    return result_dir(override) / (identifier + ".json")


def last_run(identifier: str, expected: dict[str, str], *,
             results_root: Path | None = None) -> dict[str, Any]:
    """Return only a matching real execution result; invalidate any changed dependency."""
    path = _record_path(identifier, results_root)
    if not path.is_file():
        return {"proof_status": "not_run", "run_cached": False}
    try:
        if path.stat().st_size > MAX_RECORD_BYTES:
            raise ValueError("oversized")
        record = json.loads(path.read_text(encoding="utf-8"))
        if (not isinstance(record, dict) or record.get("schema_version") != SCHEMA_VERSION
                or record.get("formalization_id") != identifier
                or record.get("proof_status") not in STORED_STATUSES):
            raise ValueError("invalid schema")
    except (OSError, ValueError, UnicodeError, TypeError):
        return {"proof_status": "not_run", "run_cached": False,
                "run_record_invalid": True}
    if any(record.get(key) != value for key, value in expected.items()):
        return {"proof_status": "not_run", "run_cached": False,
                "previous_run_outdated": True}
    return {"proof_status": record["proof_status"], "run_cached": True,
            "last_run_at": record.get("finished_at"),
            "last_run_detail": record.get("detail", ""),
            "last_run_log": record.get("log", "")[:MAX_STORED_LOG],
            "certificate": False}


def save_run(identifier: str, expected: dict[str, str], *, proof_status: str,
             detail: str, log: str = "", results_root: Path | None = None) -> dict[str, Any]:
    """Atomically save the latest actual result; callers must not store synthetic success."""
    if proof_status not in STORED_STATUSES:
        raise ValueError("Not an actual Lean process outcome")
    if set(expected) != {"source_document_sha256", "lean_sha256", "toolchain_sha256"}:
        raise ValueError("Incomplete run fingerprint")
    if not all(isinstance(value, str) and HEX_DIGEST.fullmatch(value)
               for value in expected.values()):
        raise ValueError("Invalid run fingerprint")
    path = _record_path(identifier, results_root)
    record = {"schema_version": SCHEMA_VERSION, "formalization_id": identifier,
              **expected, "proof_status": proof_status,
              "detail": str(detail)[:1000], "log": str(log)[-MAX_STORED_LOG:],
              "finished_at": datetime.now(timezone.utc).isoformat(),
              "certificate": False}
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         prefix=f".{identifier}.", suffix=".tmp",
                                         delete=False) as out:
            temporary = Path(out.name)
            json.dump(record, out, ensure_ascii=False, sort_keys=True)
            out.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return record
