"""Read-only navigator for indexed Lean formalizations, not a proof verifier."""
from __future__ import annotations

import hashlib
import sqlite3
from pathlib import Path

from fastapi import HTTPException
from backend import lean_formalization as lean

MAX_ENTRIES = 250


def list_formalizations(con: sqlite3.Connection, *,
                        lean_root: Path = lean.LEAN_ROOT) -> dict:
    registry = lean._registry(lean_root)
    if len(registry) > MAX_ENTRIES:
        raise HTTPException(503, "Zbyt duży rejestr formalizacji Lean.")
    documents = {}
    items = []
    for item in registry:
        module, label = item["source_module"], item["source_label"]
        if module not in documents:
            documents[module] = con.execute(
                "SELECT id,sha256,content FROM documents WHERE id=?", (module,)
            ).fetchone()
        doc = documents[module]
        entity_id = None
        if doc is None:
            index_status = "missing_document"
        elif (not isinstance(doc["content"], str) or
              hashlib.sha256(doc["content"].encode("utf-8")).hexdigest() != doc["sha256"]):
            index_status = "corrupt_document"
        else:
            matches = con.execute(
                "SELECT DISTINCT e.id FROM labels l JOIN entities e ON e.id=l.entity_id "
                "WHERE e.document_id=? AND l.name=? ORDER BY e.id LIMIT 2",
                (module, label)
            ).fetchall()
            index_status = "ok" if len(matches) == 1 else (
                "ambiguous_label" if matches else "unlinked_label")
            if len(matches) == 1:
                entity_id = matches[0]["id"]
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
