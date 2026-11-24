"""L1.5.5d: contextual hints for already registered LST theorems.

Only explicit, version-bound links. Existing manifest approval is metadata
about the registered statement, never approval of a new translation.
"""
from __future__ import annotations

import hashlib
import sqlite3

from fastapi import HTTPException
from backend import lean_concept_context, lean_concepts, lean_formalization
from backend import lean_transcription

RULE_VERSION = "0.1.0"
# Curated contextual dependencies, not claims that the source explicitly cites
# these labels, nor a complete proof dependency graph.
_RULES = {
    ("LST-01", "thm:de-morgan-logic"): (
        "lst01-de-morgan", ("def:propositional-grammar-xli", "def:tautology"),
        ("logic.syntax.formula", "logic.syntax.equivalent")),
    ("LST-01", "thm:equiv-test"): (
        "lst01-equivalence-test", ("def:propositional-grammar-xli", "def:tautology"),
        ("logic.syntax.formula", "logic.syntax.equivalent", "logic.syntax.tautology")),
}


def resolve_theorem(con: sqlite3.Connection, *, entity_id: str,
                    expected_source_sha256: str, consent: bool) -> dict:
    result = {"status": "unsupported", "rule_version": RULE_VERSION,
              "dictionary_sha256": lean_concepts.dictionary_sha256(),
              "registered_mapping": None, "candidates": [], "trace": [],
              "candidate_status": "not_generated", "statement_status": "unreviewed",
              "proof_status": "not_run", "certificate": False, "lean_code": None,
              "external_transfer_allowed": False}
    if type(entity_id) is not str or not 1 <= len(entity_id) <= 512:
        return {**result, "status": "invalid_input"}
    try:
        prepared = lean_transcription.prepare(
            con, entity_id=entity_id, expected_source_sha256=expected_source_sha256,
            consent=consent)
        module, label = prepared["source_module"], prepared["source_label"]
        rule = _RULES.get((module, label))
        if rule is None:
            return result
        mapping_id, definition_labels, concept_ids = rule
        registry = lean_formalization._registry()
        matching = [m for m in registry if
                    (m["source_module"], m["source_label"]) == (module, label)]
        if len(matching) != 1 or matching[0]["id"] != mapping_id:
            return {**result, "status": "invalid_registry"}
        item = matching[0]
        if item["statement_status"] != "approved":
            return {**result, "status": "mapping_needs_review"}
        digest = prepared["source_document_sha256"]
        if (item.get("source_document_sha256") != digest
                or not item.get("source_document_path")
                or not lean_formalization._source_file_current(
                    item, digest, lean_formalization.LEAN_ROOT)):
            return {**result, "status": "stale_mapping"}
        candidates, trace = {}, []
        for definition_label in definition_labels:
            anchors = [a for a in lean_concept_context._ANCHORS
                       if (a["module"], a["label"]) == (module, definition_label)]
            if len(anchors) != 1:
                return {**result, "status": "missing_context"}
            source_sha = hashlib.sha256(anchors[0]["source"].encode("utf-8")).hexdigest()
            context = lean_concept_context.resolve_definition(
                con, module, definition_label, source_sha)
            if context["status"] != "context_candidates":
                return {**result, "status": "invalid_context",
                        "context_status": context["status"]}
            for candidate in context["candidates"]:
                if candidate["id"] in concept_ids:
                    candidates[candidate["id"]] = candidate
                    trace.append({"rule": "curated_definition_context",
                                  "definition_label": definition_label,
                                  "definition_sha256": source_sha,
                                  "concept_id": candidate["id"]})
        if set(candidates) != set(concept_ids):
            return {**result, "status": "missing_context"}
        return {**result, "status": "context_candidates",
                "registered_mapping": {"id": mapping_id,
                    "statement_status": "approved",
                    "source_document_sha256": digest,
                    "source_sha256": prepared["source_sha256"],
                    "source_binding_sha256": prepared["source_binding_sha256"],
                    "lean_theorems": list(item["lean_theorems"])},
                "candidates": [candidates[k] for k in concept_ids], "trace": trace}
    except HTTPException as exc:
        return {**result, "status": "source_or_registry_rejected",
                "http_status": exc.status_code}
    except (sqlite3.Error, OSError, ValueError, TypeError, UnicodeError):
        return {**result, "status": "invalid_context"}
