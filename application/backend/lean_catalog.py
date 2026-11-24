"""Read-only navigator for indexed Lean formalizations, not a proof verifier."""
from __future__ import annotations

import hashlib
import sqlite3
from pathlib import Path

from fastapi import HTTPException
from backend import lean_formalization as lean, lean_source_provenance

MAX_ENTRIES = 250


def list_formalizations(con: sqlite3.Connection, *,
                        lean_root: Path = lean.LEAN_ROOT,
                        module_id: str | None = None) -> dict:
    """List all mappings or only one module; always validate the full registry."""
    registry = lean._registry(lean_root)
    if len(registry) > MAX_ENTRIES:
        raise HTTPException(503, "Zbyt duży rejestr formalizacji Lean.")
    documents = {}
    # L1.4.2: cache *only* the digest of the SQLite row already fetched once
    # per module in this invocation. Never cache across requests or skip the
    # per-label owner_status / per-file canonical provenance checks.
    document_validity = {}
    items = []
    for item in registry:
        module, label = item["source_module"], item["source_label"]
        # Filter only after global registry validation and its size limit.
        # Do not skip any integrity/provenance check for a selected entry.
        if module_id is not None and module != module_id:
            continue
        if module not in documents:
            doc = con.execute(
                "SELECT id,sha256,content FROM documents WHERE id=?", (module,)
            ).fetchone()
            documents[module] = doc
            document_validity[module] = bool(
                doc is not None and isinstance(doc["content"], str)
                and hashlib.sha256(doc["content"].encode("utf-8")).hexdigest()
                == doc["sha256"])
        doc = documents[module]
        entity_id = None
        if doc is None:
            index_status = "missing_document"
        elif not document_validity[module]:
            index_status = "corrupt_document"
        else:
            index_status, entity_id = lean_source_provenance.owner_status(
                con, module, label, doc["content"])
        pinned = item.get("source_document_sha256")
        current = bool(index_status == "ok" and
                       (not pinned or pinned == doc["sha256"]) and
                       lean._source_file_current(item, doc["sha256"], lean_root))
        status = "stale" if not current else "ready" if pinned else "draft"
        items.append({
            "formalization_id": item["id"], "source_module": module,
            "source_label": label, "source_entity_id": entity_id,
            "lean_file": item["lean_file"], "lean_theorem": item["lean_theorem"],
            "lean_theorems": item.get("lean_theorems", [item["lean_theorem"]]),
            "index_status": index_status, "formalization_status": status,
            "statement_status": item["statement_status"] if current else "needs_review",
            "certificate": False,
        })
    items.sort(key=lambda x: (x["source_module"], x["source_label"], x["formalization_id"]))
    return {
        "items": items, "total": len(items),
        "ready": sum(x["formalization_status"] == "ready" for x in items),
        "draft": sum(x["formalization_status"] == "draft" for x in items),
        "stale": sum(x["formalization_status"] == "stale" for x in items),
        "proof_status_included": False,
    }
