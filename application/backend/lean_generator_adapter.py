"""L1.5.8a: explicit selection of non-executing draft generators.

Only the existing rule generator is integrated. No model transport,
network, installation, provider callbacks or automatic fallback.
"""
from __future__ import annotations

import hashlib
from backend import lean_draft_generator as rules

VERSION = "0.1.0"
MAX_SOURCE_BYTES = 32768


def capabilities() -> dict:
    return {"schema_version": 1, "adapter_version": VERSION,
            "generators": {
                "rules": {"available": True, "version": rules.VERSION},
                "local_model": {"available": False, "version": None},
                "external_provider": {"available": False, "version": None}},
            "automatic_fallback": False, "external_transfer_allowed": False,
            "external_cost_minor_units": 0, "execution_allowed": False,
            "certificate": False}


def generate(source: str, *, generator: str, expected_source_sha256: str,
             segments: list | None = None, consent: bool = False) -> dict:
    """Bind the selection to exact UTF-8 source bytes, never execute a draft."""
    base = {"schema_version": 1, "adapter_version": VERSION,
            "generator": generator if type(generator) is str and generator in
            ("rules", "local_model", "external_provider") else None,
            "generator_version": None, "model": None, "source_sha256": None,
            "ast_sha256": None, "lean_code_sha256": None, "lean_code": None,
            "status": "blocked", "candidate_status": "not_generated",
            "statement_status": "unreviewed", "proof_status": "not_run",
            "model_called": False, "automatic_fallback": False,
            "external_transfer_allowed": False, "external_cost_minor_units": 0,
            "execution_allowed": False, "certificate": False}
    if consent is not True:
        return {**base, "error": "explicit_consent_required"}
    if base["generator"] is None:
        return {**base, "error": "unknown_generator"}
    if type(source) is not str or len(source) > MAX_SOURCE_BYTES:
        return {**base, "error": "invalid_source"}
    try:
        raw = source.encode("utf-8")
    except UnicodeError:
        return {**base, "error": "invalid_source"}
    if not raw or len(raw) > MAX_SOURCE_BYTES:
        return {**base, "error": "invalid_source"}
    digest = hashlib.sha256(raw).hexdigest()
    if type(expected_source_sha256) is not str or expected_source_sha256 != digest:
        return {**base, "error": "stale_source"}
    base["source_sha256"] = digest
    if generator == "external_provider":
        return {**base, "error": "external_provider_disabled"}
    if generator == "local_model":
        return {**base, "error": "local_model_not_integrated"}
    result = rules.generate(source, segments=segments, consent=True)
    if result["status"] == "generated" and (
        result["source_sha256"] != digest or
        hashlib.sha256(result["lean_code"].encode("utf-8")).hexdigest()
        != result["lean_code_sha256"]
    ):
        return {**base, "error": "candidate_identity_mismatch"}
    return {**base, **result, "source_sha256": digest,
            "schema_version": 1, "adapter_version": VERSION,
            "generator": "rules", "model": None, "model_called": False,
            "automatic_fallback": False, "external_transfer_allowed": False,
            "external_cost_minor_units": 0, "execution_allowed": False,
            "certificate": False, "proof_status": "not_run"}
