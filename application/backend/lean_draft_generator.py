"""L1.5.6a: deterministic, non-executing draft generator for the controlled pilot.

Only a fresh complete parse can enter the renderer. Names and syntax are
constructed from fixed templates; source strings and display names are never
interpolated as Lean commands. This module is not a sandbox or a runner.
"""
from __future__ import annotations

import hashlib
from backend import lean_parser

VERSION = "0.2.0"
# Fixed, measured on the pinned Mathlib toolchain; never caller-supplied.
IMPORTS = (
    "Mathlib.Data.Real.Basic",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.Tauto",
    "Aesop",
    "Lean.Elab.Tactic.Omega",
)
IMPORT_HEADER = "".join("import " + name + "\n" for name in IMPORTS)
MAX_CODE_BYTES = 65536
_BINARY = {"and": "∧", "or": "∨", "implies": "→", "iff": "↔",
           "eq": "=", "lt": "<", "le": "≤", "add": "+", "mul": "*", "sub": "-"}
_TYPES = {t: t for t in ("Prop", "Nat", "Int", "Real")}
_PROOF = "by\n  repeat\' intro\n  first\n  | assumption\n  | rfl\n  | exact True.intro\n  | exact ⟨0, rfl⟩\n  | tauto\n  | omega\n"


def _render(document):
    names = {}
    def bind(binding):
        # Alpha-renaming is injective even when source binders shadow.
        name = "v" + str(len(names) + 1)
        names[binding["id"]] = name
        return name + " : " + _TYPES[binding["type"]]

    def expr(node):
        kind = node["kind"]
        if kind == "var":
            return names[node["binding_id"]]
        if kind == "numeral":
            return "(" + node["digits"] + " : " + _TYPES[node["type"]] + ")"
        if kind == "truth":
            return "True"
        if kind == "falsehood":
            return "False"
        if kind in ("forall", "exists"):
            binder = bind(node["binding"])
            return "(" + ("∀" if kind == "forall" else "∃") + " (" + binder + "), " + expr(node["body"]) + ")"
        if kind in ("not", "neg"):
            return "(" + ("¬ " if kind == "not" else "-") + expr(node["arg"]) + ")"
        return "(" + expr(node["left"]) + " " + _BINARY[kind] + " " + expr(node["right"]) + ")"

    params = ["(" + bind(b) + ")" for b in document["parameters"]]
    assumptions = ["(h" + str(i) + " : " + expr(a) + ")"
                   for i, a in enumerate(document["assumptions"], 1)]
    signature = "theorem atlas_draft " + " ".join(params + assumptions) + " : " + expr(document["conclusion"])
    return signature, names


def generate(source: str, *, segments: list | None = None, consent: bool = False) -> dict:
    """Return an unreviewed text candidate; never execute or write anything.

    Input is an explicitly selected pilot formula, not an indexed theorem or
    a claim of complete natural-language translation. No caller-supplied AST,
    imports, tactics, identifier names, or proof snippets are accepted.
    """
    result = {"generator_version": VERSION, "status": "blocked",
              "candidate_status": "not_generated", "statement_status": "unreviewed",
              "proof_status": "not_run", "certificate": False, "lean_code": None,
              "external_transfer_allowed": False, "external_cost_minor_units": 0,
              "execution_allowed": False, "execution_blocker": "isolated_runner_required"}
    if consent is not True:
        return {**result, "error": "explicit_consent_required"}
    parsed = (lean_parser.parse_formula(source) if segments is None
              else lean_parser.parse_pilot_statement(source, segments))
    if parsed["status"] not in ("parsed_formula", "parsed_pilot_statement"):
        return {**result, "status": parsed["status"], "error": parsed.get("error"),
                "diagnostic": {k: parsed[k] for k in ("span", "path") if k in parsed}}
    signature, names = _render(parsed["ast"])
    code = (IMPORT_HEADER + "\nset_option maxHeartbeats 100000\n"
            "set_option maxRecDepth 512\n\n" + signature + " := " + _PROOF)
    encoded = code.encode("utf-8")
    if len(encoded) > MAX_CODE_BYTES:
        return {**result, "status": "invalid_input", "error": "code_byte_limit"}
    return {**result, "status": "generated", "candidate_status": "draft",
            "statement_status": "needs_review", "coverage": parsed["coverage"],
            "source_sha256": parsed["source_sha256"], "ast_sha256": parsed["ast_sha256"],
            "lean_code_sha256": hashlib.sha256(encoded).hexdigest(), "lean_code": code,
            "signature": signature, "binding_names": names, "trace": parsed["trace"]}
