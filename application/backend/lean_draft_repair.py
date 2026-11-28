"""L1.5.7a: bounded, offline planning of proof-only repair candidates.

Diagnostics are untrusted observations, not proof or execution authority.
No subprocess, transport, file write, model call or network operation occurs.
The existing runner admission remains unchanged and cannot execute repairs.
"""
from __future__ import annotations

import hashlib
import re

from backend import lean_draft_generator as generator

MAX_ATTEMPTS = 3  # Includes the original candidate.
MAX_DIAGNOSTIC_BYTES = 16000
VERSION = "0.1.2"
# Fixed tactic text only. Never interpolate diagnostics.
# A branch of `first` must close all goals, not merely make progress.
_REPAIRS = (
    "by\n  repeat' intro\n  first\n  | solve_by_elim <;> done\n  | simp_all <;> done\n  | omega <;> done\n",
    "by\n  repeat' intro\n  first\n  | aesop <;> done\n  | omega <;> done\n  | ring <;> done\n",
)
_ERROR = re.compile(r"^(?:/tmp/)?Draft\.lean:([0-9]{1,6}):([0-9]{1,6}): error: (.+)$")
# Deliberately narrow: a diagnostic about an unknown tactic, elaboration,
# resource exhaustion or the statement itself cannot authorize a repair.
_TACTIC_FAILED = re.compile(
    r"tactic (?:'(assumption|rfl|tauto|omega|solve_by_elim|simp_all|aesop|ring)'"
    r"|\x60(assumption|rfl|tauto|omega|solve_by_elim|simp_all|aesop|ring)\x60) failed"
)


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _failure_kind(record, expected_hash, code, prefix):
    if (type(record) is not dict or set(record) !=
            {"code_sha256", "exit_code", "diagnostic"}
            or type(record["code_sha256"]) is not str
            or record["code_sha256"] != expected_hash
            or type(record["exit_code"]) is not int
            or type(record["diagnostic"]) is not bytes
            or len(record["diagnostic"]) > MAX_DIAGNOSTIC_BYTES):
        return "invalid_observation"
    if record["exit_code"] == 0:
        return "reported_success"
    if record["exit_code"] != 1:
        return "non_repairable_failure"
    try:
        log = record["diagnostic"].decode("utf-8")
    except UnicodeError:
        return "invalid_observation"
    # Fail closed on unknown errors, including errors without source locations.
    errors = [line for line in log.splitlines() if "error:" in line.lower()]
    if not errors:
        return "non_repairable_failure"
    # Lean uses one-based line numbers and zero-based columns.
    proof_line = prefix.count("\n") + 1
    proof_column = len(prefix.rsplit("\n", 1)[-1])
    lines = code.splitlines()
    for line in errors:
        match = _ERROR.fullmatch(line)
        if match is None:
            return "non_repairable_failure"
        row, col, message = int(match[1]), int(match[2]), match[3]
        if (row < proof_line or row > len(lines)
                or (row == proof_line and col < proof_column)
                or col > len(lines[row-1])):
            return "non_repairable_failure"
        if message != "unsolved goals" and not _TACTIC_FAILED.fullmatch(message):
            return "non_repairable_failure"
    # No claim about authenticity of this diagnostic is made here.
    return "reported_proof_failure"


def plan_next(source: str, *, segments: list | None = None,
              expected_source_sha256: str, expected_ast_sha256: str,
              expected_initial_code_sha256: str, observations: list,
              consent: bool = False) -> dict:
    """Regenerate the original statement and replay a bounded attempt history.

    Observations must refer to the exact previously planned candidate. A
    reported success, timeout, malformed diagnostic, stale hash or exhausted
    budget stops planning. This is not a trusted runner result or a certificate.
    """
    base = {"repair_version": VERSION, "status": "blocked", "lean_code": None,
            "proof_status": "not_run", "statement_status": "needs_review",
            "certificate": False, "execution_allowed": False,
            "external_transfer_allowed": False, "external_cost_minor_units": 0,
            "max_attempts": MAX_ATTEMPTS}
    if consent is not True:
        return {**base, "error": "explicit_consent_required"}
    if type(observations) is not list or not 1 <= len(observations) <= MAX_ATTEMPTS:
        return {**base, "error": "invalid_attempt_history"}
    original = generator.generate(source, segments=segments, consent=True)
    if original["status"] != "generated":
        return {**base, "error": "regeneration_rejected"}
    keys = ("source_sha256", "ast_sha256", "lean_code_sha256")
    expected = (expected_source_sha256, expected_ast_sha256, expected_initial_code_sha256)
    if any(type(x) is not str for x in expected) or tuple(original[k] for k in keys) != expected:
        return {**base, "error": "stale_candidate"}
    # Preserve the entire prefix, including imports, limits, parameters,
    # assumptions and conclusion. Only the exact original proof suffix changes.
    suffix = " := " + generator._PROOF
    code = original["lean_code"]
    if not code.endswith(suffix):
        return {**base, "error": "generator_contract_changed"}
    prefix = code[:-len(suffix)] + " := "
    if not prefix.endswith(original["signature"] + " := "):
        return {**base, "error": "generator_contract_changed"}
    identity = {"source_sha256": original["source_sha256"],
                "ast_sha256": original["ast_sha256"],
                "signature": original["signature"],
                "initial_code_sha256": original["lean_code_sha256"]}
    trace = []
    for i, record in enumerate(observations):
        digest = _sha(code.encode("utf-8"))
        kind = _failure_kind(record, digest, code, prefix)
        if kind != "reported_proof_failure":
            return {**base, **identity, "error": kind, "attempts": trace}
        trace.append({"attempt": i+1, "code_sha256": digest,
                      "diagnostic_sha256": _sha(record["diagnostic"]),
                      "observation": kind})
        if i+1 >= MAX_ATTEMPTS:
            return {**base, **identity, "status": "exhausted",
                    "error": "attempt_limit", "attempts": trace}
        code = prefix + _REPAIRS[i]
    payload = code.encode("utf-8")
    if len(payload) > generator.MAX_CODE_BYTES:
        return {**base, **identity, "error": "code_byte_limit"}
    return {**base, **identity, "status": "repair_planned",
            "candidate_status": "draft", "attempt": len(trace)+1,
            "attempts": trace, "lean_code": code,
            "lean_code_sha256": _sha(payload)}
