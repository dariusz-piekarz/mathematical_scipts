"""L1.5.1: read-only, offline preparation for experimental transcription.

No provider, subprocess, filesystem writes or registry changes. The source
is an indexed snapshot, not an attestation of current canonical disk bytes.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3

from fastapi import HTTPException
from backend import lean_formalization, lean_source_provenance

MAX_SOURCE_BYTES = 32_768


def prepare(con: sqlite3.Connection, *, entity_id: str,
            expected_source_sha256: str, consent: bool) -> dict:
    if consent is not True:
        raise HTTPException(400, "Przygotowanie eksperymentu wymaga jawnej zgody.")
    # Restrict the first pilot to one exact, uniquely labelled theorem.
    # In particular, do not infer a theorem from a proof or an arbitrary range.
    entity = con.execute("SELECT kind FROM entities WHERE id=?", (entity_id,)).fetchone()
    if entity is None:
        raise HTTPException(404, "Nieznany obiekt matematyczny.")
    if entity["kind"] != "theorem":
        raise HTTPException(400, "Eksperyment wymaga pełnego twierdzenia.")
    doc, source, labels, first, last, eid, linkage = lean_formalization._find_source(
        con, entity_id=entity_id, module_id=None, start_line=None, end_line=None)
    if eid != entity_id or linkage != "exact_entity" or len(labels) != 1:
        raise HTTPException(409, "Wymagana jedna jednoznaczna etykieta twierdzenia.")
    encoded = source.encode("utf-8")
    if len(encoded) > MAX_SOURCE_BYTES:
        raise HTTPException(413, "Fragment przekracza limit 32 KiB UTF-8.")
    doc_digest = hashlib.sha256(doc["content"].encode("utf-8")).hexdigest()
    if doc_digest != doc["sha256"]:
        raise HTTPException(409, "Niezgodność SHA-256 rozdziału w indeksie.")
    source_digest = hashlib.sha256(encoded).hexdigest()
    if source_digest != expected_source_sha256:
        raise HTTPException(409, "Fragment zmienił się; odczytaj go ponownie.")
    label = labels[0]
    status, owner = lean_source_provenance.owner_status(con, doc["id"], label, doc["content"])
    if status != "ok" or owner != entity_id:
        raise HTTPException(409, "Niejednoznaczne lub niepoprawne pochodzenie etykiety.")
    binding = lean_source_provenance.indexed_binding(con, doc["id"], label, owner)
    if binding is None:
        raise HTTPException(409, "Brak powiązania źródłowego.")
    identity = {
        "source_module": doc["id"], "source_entity": entity_id,
        "source_label": label, "start_line": first, "end_line": last,
        "source_document_sha256": doc_digest, "source_sha256": source_digest,
        "source_binding_sha256": lean_source_provenance.binding_sha256(doc["id"], label, binding),
    }
    request_id = hashlib.sha256(json.dumps(identity, sort_keys=True, ensure_ascii=False,
                                          separators=(",", ":")).encode("utf-8")).hexdigest()
    return {
        "schema_version": 1, "request_id": request_id, "status": "prepared",
        "experimental": True, "source_scope": "indexed_snapshot_only",
        **identity, "source_latex": source, "source_bytes": len(encoded),
        "candidate_status": "not_generated", "lean_code": None,
        "statement_status": "unreviewed", "proof_status": "not_run",
        "certificate": False, "external_provider": None,
        "external_transfer_allowed": False, "license_status": "unreviewed",
        "external_budget_minor_units": 0, "external_cost_minor_units": 0,
        "registry_written": False, "canonical_source_written": False,
    }
