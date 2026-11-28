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
    # A provider result is not an authority grant. Reject malformed or
    # contradictory envelopes instead of propagating arbitrary extra fields.
    common = {"generator_version", "status", "candidate_status",
              "statement_status", "proof_status", "certificate", "lean_code",
              "external_transfer_allowed", "external_cost_minor_units",
              "execution_allowed", "execution_blocker"}
    def reject(error="invalid_generator_result"):
        return {**base, "error": error}
    if type(result) is not dict or not common <= result.keys():
        return reject()
    if (result["generator_version"] != rules.VERSION
            or result["proof_status"] != "not_run"
            or result["execution_blocker"] != "isolated_runner_required"
            or any(result[k] is not False for k in
                   ("certificate", "external_transfer_allowed", "execution_allowed"))
            or type(result["external_cost_minor_units"]) is not int
            or result["external_cost_minor_units"] != 0):
        return reject()
    if result["status"] == "generated":
        fields = {"coverage", "source_sha256", "ast_sha256", "lean_code_sha256",
                  "signature", "binding_names", "trace"}
        if (set(result) != common | fields
                or result["candidate_status"] != "draft"
                or result["statement_status"] != "needs_review"
                or result["coverage"] != "controlled_pilot_only"
                or type(result["lean_code"]) is not str
                or not result["lean_code"]
                or len(result["lean_code"]) > rules.MAX_CODE_BYTES
                or type(result["signature"]) is not str
                or type(result["binding_names"]) is not dict
                or type(result["trace"]) is not dict):
            return reject()
        try:
            code = result["lean_code"].encode("utf-8")
        except UnicodeError:
            return reject()
        if len(code) > rules.MAX_CODE_BYTES:
            return reject()
        if (result["source_sha256"] != digest or
                hashlib.sha256(code).hexdigest() != result["lean_code_sha256"]):
            return reject("candidate_identity_mismatch")
        # Reparse the exact selection, including its segment roles. A digest
        # of arbitrary code alone cannot establish source/AST correspondence.
        parsed = (rules.lean_parser.parse_formula(source) if segments is None
                  else rules.lean_parser.parse_pilot_statement(source, segments))
        if (parsed["status"] not in ("parsed_formula", "parsed_pilot_statement")
                or parsed["ast_sha256"] != result["ast_sha256"]
                or parsed["trace"] != result["trace"]):
            return reject("candidate_identity_mismatch")
        signature, names = rules._render(parsed["ast"])
        # Rules are deterministic: authenticate the entire template, not
        # only the declaration prefix. A rehashed, altered proof or appended
        # command is not an output of this generator.
        expected_code = (rules.IMPORT_HEADER + "\nset_option maxHeartbeats 100000\n"
                         "set_option maxRecDepth 512\n\n" + signature + " := " + rules._PROOF)
        if (signature != result["signature"] or names != result["binding_names"]
                or result["lean_code"] != expected_code):
            return reject("candidate_identity_mismatch")
    else:
        if (result["status"] not in ("unsupported", "invalid_input", "blocked")
                or not set(result) <= common | {"error", "diagnostic"}
                or result["candidate_status"] != "not_generated"
                or result["statement_status"] != "unreviewed"
                or result["lean_code"] is not None
                or type(result.get("error")) is not str):
            return reject()
        # A negative result is also deterministic. Reconstruct the diagnostic
        # from the parser, never forward unchecked nested provider fields.
        parsed = (rules.lean_parser.parse_formula(source) if segments is None
                  else rules.lean_parser.parse_pilot_statement(source, segments))
        if parsed["status"] in ("parsed_formula", "parsed_pilot_statement"):
            signature, _ = rules._render(parsed["ast"])
            expected_code = (rules.IMPORT_HEADER + "\nset_option maxHeartbeats 100000\n"
                             "set_option maxRecDepth 512\n\n" + signature + " := " + rules._PROOF)
            if (len(expected_code.encode("utf-8")) <= rules.MAX_CODE_BYTES
                    or set(result) != common | {"error"}
                    or result["status"] != "invalid_input"
                    or result["error"] != "code_byte_limit"):
                return reject("candidate_identity_mismatch")
        else:
            diagnostic = {k: parsed[k] for k in ("span", "path") if k in parsed}
            if (set(result) != common | {"error", "diagnostic"}
                    or result["status"] != parsed["status"]
                    or result["error"] != parsed.get("error")
                    or type(result["diagnostic"]) is not dict
                    or result["diagnostic"] != diagnostic):
                return reject("candidate_identity_mismatch")
            result = {**result, "diagnostic": diagnostic}
    return {**base, **result, "source_sha256": digest,
            "schema_version": 1, "adapter_version": VERSION,
            "generator": "rules", "model": None, "model_called": False,
            "automatic_fallback": False, "external_transfer_allowed": False,
            "external_cost_minor_units": 0, "execution_allowed": False,
            "certificate": False, "proof_status": "not_run"}
