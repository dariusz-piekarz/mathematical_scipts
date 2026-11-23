"""L1.4: conservative read-only, per-chapter Lean registration report.

This report validates indexed source provenance only. It deliberately does not
consult persisted Lean executions or attempt to compute a toolchain fingerprint.
Neither registered nor approved mappings imply successful compilation.
"""
from __future__ import annotations

import hashlib
import sqlite3
from pathlib import Path

from fastapi import HTTPException

from backend import lean_catalog, lean_formalization as lean

REPORT_SCHEMA_VERSION = 1
REPORT_ITEM_FIELDS = (
    "formalization_id", "source_module", "source_label", "source_entity_id",
    "lean_file", "lean_theorem", "lean_theorems", "index_status",
    "formalization_status", "statement_status",
)


def chapter_report(con: sqlite3.Connection, module_id: str, *,
                   lean_root: Path = lean.LEAN_ROOT) -> dict:
    """Report one indexed chapter without interpreting a cached Lean result."""
    if not isinstance(module_id, str) or not lean.VALID_ID.fullmatch(module_id):
        raise HTTPException(400, "Niepoprawny identyfikator rozdziału.")
    doc = con.execute(
        "SELECT id,sha256,content FROM documents WHERE id=?", (module_id,)
    ).fetchone()
    if doc is None:
        raise HTTPException(404, "Nieznany rozdział.")

    content = doc["content"]
    indexed_sha = doc["sha256"]
    index_current = (
        isinstance(content, str) and isinstance(indexed_sha, str)
        and lean_results_hex(indexed_sha)
        and hashlib.sha256(content.encode("utf-8")).hexdigest() == indexed_sha
    )

    # Reuse the existing, bounded catalogue: it checks label ownership,
    # manifest SHA and canonical on-disk TeX. Do not invent proof statuses.
    catalog = lean_catalog.list_formalizations(con, lean_root=lean_root)
    # Project a fixed allowlist. Future catalogue additions (including any
    # eventual cached proof status) must not silently enter this report.
    entries = [
        {**{name: item[name] for name in REPORT_ITEM_FIELDS}, "certificate": False}
        for item in catalog["items"] if item["source_module"] == module_id
    ]
    # The catalogue reads the same SQLite index separately. Detect a generation
    # switch in between these reads, including a new *internally valid* SHA.
    # No version of a changing chapter may acquire a positive report status.
    after = con.execute(
        "SELECT sha256,content FROM documents WHERE id=?", (module_id,)
    ).fetchone()
    changed = (
        after is None or after["sha256"] != indexed_sha
        or after["content"] != content
    )
    source_index_status = (
        "changed_during_report" if changed else
        "ok" if index_current else "corrupt_document"
    )
    if source_index_status != "ok":
        for item in entries:
            item["index_status"] = source_index_status
            item["formalization_status"] = "stale"
            item["statement_status"] = "needs_review"

    return {
        "report_schema_version": REPORT_SCHEMA_VERSION,
        "source_module": module_id,
        "source_index_status": source_index_status,
        "source_document_sha256": indexed_sha if source_index_status == "ok" else None,
        "total": len(entries),
        "ready": sum(x["formalization_status"] == "ready" for x in entries),
        "draft": sum(x["formalization_status"] == "draft" for x in entries),
        "stale": sum(x["formalization_status"] == "stale" for x in entries),
        "statement_approved": sum(
            x["statement_status"] == "approved"
            and x["formalization_status"] == "ready" for x in entries
        ),
        "items": entries,
        "scope": "manifest_and_index_only",
        "run_history_checked": False,
        "dependency_fingerprint_checked": False,
        "proof_status_included": False,
        "certificate": False,
    }


def lean_results_hex(value: str) -> bool:
    """Check canonical lowercase SHA256 without accepting non-string values."""
    return len(value) == 64 and all(c in "0123456789abcdef" for c in value)
