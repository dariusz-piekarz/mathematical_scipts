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

from backend import lean_catalog, lean_formalization as lean, lean_source_provenance

REPORT_SCHEMA_VERSION = 1
REPORT_ITEM_FIELDS = (
    "formalization_id", "source_module", "source_label", "source_entity_id",
    "lean_file", "lean_theorem", "lean_theorems", "index_status",
    "formalization_status", "statement_status",
)
# Compare both manifest generations, including path fields not in the
# public catalogue. A changed canonical path must not inherit old approval.
MANIFEST_IDENTITY_FIELDS = (
    "source_module", "source_label", "source_document_sha256",
    "source_document_path", "statement_status", "lean_file",
    "lean_theorem", "lean_theorems",
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

    # Keep an initial, bounded manifest and exact indexed-entity snapshot.
    # Catalogue owner_status and a later owner_status can both say "ok" for
    # the *same entity ID* even if the entity's title or span changed between
    # the calls. Compare the actual indexed binding, not only its owner ID.
    initial_registry = lean._registry(lean_root)
    if len(initial_registry) > lean_catalog.MAX_ENTRIES:
        raise HTTPException(503, "Zbyt duży rejestr formalizacji Lean.")
    initial_items = {item["id"]: item for item in initial_registry
                     if item["source_module"] == module_id}
    initial_bindings = {}
    if index_current:
        for item in initial_items.values():
            status, owner = lean_source_provenance.owner_status(
                con, module_id, item["source_label"], content)
            if status == "ok" and owner is not None:
                initial_bindings[item["id"]] = (
                    lean_source_provenance.indexed_binding(
                        con, module_id, item["source_label"], owner)
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
    # Catalogue "ready" may be based on a pinned manifest SHA without a
    # canonical .tex path. Require an independently readable canonical file,
    # and check it again after the catalogue pass. This remains diagnostics:
    # no cryptographic attestation or atomic filesystem snapshot is implied.
    latest_registry = lean._registry(lean_root)
    if len(latest_registry) > lean_catalog.MAX_ENTRIES:
        raise HTTPException(503, "Zbyt duży rejestr formalizacji Lean.")
    registry = {item["id"]: item for item in latest_registry}
    # The catalogue may have read an earlier manifest generation. Compare
    # identities for the entire chapter, not merely the items returned before
    # an addition or deletion. Never mix an old approval with a newer manifest.
    actual_ids = {item["id"] for item in latest_registry
                  if item["source_module"] == module_id}
    listed_ids = {entry["formalization_id"] for entry in entries}
    changed_manifest = (actual_ids != listed_ids
                        or set(initial_items) != listed_ids
                        or len(listed_ids) != len(entries))
    for entry in entries:
        if changed_manifest:
            entry["index_status"] = "changed_manifest_during_report"
            entry["formalization_status"] = "stale"
            entry["statement_status"] = "needs_review"
            continue
        if entry["formalization_status"] not in ("ready", "draft"):
            continue
        registered = registry.get(entry["formalization_id"])
        before = initial_items.get(entry["formalization_id"])
        changed_item = (
            registered is None or before is None
            or any(before.get(name) != registered.get(name)
                   for name in MANIFEST_IDENTITY_FIELDS)
            or registered.get("source_module") != module_id
            or registered.get("source_label") != entry["source_label"]
            or registered.get("statement_status") != entry["statement_status"]
            or registered.get("lean_file") != entry["lean_file"]
            or registered.get("lean_theorem") != entry["lean_theorem"]
            or registered.get("lean_theorems",
                              [registered.get("lean_theorem")]) != entry["lean_theorems"]
            or (entry["formalization_status"] == "ready"
                and registered.get("source_document_sha256") != indexed_sha)
        )
        if changed_item:
            entry["index_status"] = "changed_manifest_during_report"
            entry["formalization_status"] = "stale"
            entry["statement_status"] = "needs_review"
            continue
        # Label ownership is a separate SQLite relation and can change
        # without changing the document's content SHA256.
        owner_status, owner_id = lean_source_provenance.owner_status(
            con, module_id, entry["source_label"], content)
        actual_binding = (
            lean_source_provenance.indexed_binding(
                con, module_id, entry["source_label"], owner_id)
            if owner_status == "ok" and owner_id is not None else None
        )
        if (owner_status != "ok" or owner_id != entry["source_entity_id"]
                or actual_binding is None
                or initial_bindings.get(entry["formalization_id"]) != actual_binding):
            entry["index_status"] = "changed_index_binding"
            entry["formalization_status"] = "stale"
            entry["statement_status"] = "needs_review"
            continue
        # The catalogue inspected the canonical TeX earlier. A physical
        # source change after that read invalidates drafts with registered
        # canonical paths as well as approved/ready mappings. Preserve legacy
        # pathless drafts, but never treat pathless "ready" as verified.
        source_path = registered.get("source_document_path")
        source_unverifiable = (
            (entry["formalization_status"] == "ready" and not source_path)
            or (bool(source_path) and
                not lean._source_file_current(registered, indexed_sha, lean_root))
        )
        if source_unverifiable:
            entry["index_status"] = "unverifiable_canonical_source"
            entry["formalization_status"] = "stale"
            entry["statement_status"] = "needs_review"

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
