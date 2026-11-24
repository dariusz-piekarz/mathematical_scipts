"""L1.5.5a: read-only, versioned concept lookup, not a theorem translator.

Exact aliases and explicit semantic scopes only. A match is a proposal,
not proof of the declaration's type, availability, or source correspondence.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
import hashlib
import json

SCHEMA_VERSION = 1
DICTIONARY_VERSION = "0.1.0"
LEAN_TOOLCHAIN = "leanprover/lean4:v4.26.0"
MATHLIB_REV = "2df2f0150c275ad53cb3c90f7c98ec15a56a1a67"
MAX_QUERY_CHARS = 128
SCOPES = frozenset(("logic.prop", "logic.syntax", "set", "linear_algebra"))


@dataclass(frozen=True)
class Concept:
    id: str
    scope: str
    aliases: tuple[str, ...]
    declaration: str
    origin: str
    source_hint: str


# Source hints are navigation metadata, not permission to resolve a theorem
# or proof of a reviewed mapping. All entries still require semantic review.
_CONCEPTS = (
    Concept("logic.prop.iff", "logic.prop", ("równoważność", r"\iff", "↔"), "Iff", "lean_core", "Prop → Prop → Prop"),
    Concept("logic.prop.and", "logic.prop", ("koniunkcja", r"\land", "∧"), "And", "lean_core", "Prop → Prop → Prop"),
    Concept("logic.prop.or", "logic.prop", ("alternatywa", r"\lor", "∨"), "Or", "lean_core", "Prop → Prop → Prop"),
    Concept("logic.syntax.formula", "logic.syntax", ("formuła", "formuła zdaniowa"), "LST01.Formula", "local", "LST-01:def:propositional-grammar-xli"),
    Concept("logic.syntax.equivalent", "logic.syntax", ("równoważność", r"\equiv"), "LST01.equivalent", "local", "LST-01:thm:de-morgan-logic"),
    Concept("logic.syntax.tautology", "logic.syntax", ("tautologia",), "LST01.tautology", "local", "LST-01:thm:equiv-test"),
    Concept("set.type", "set", ("zbiór",), "Set", "mathlib", "type of subsets"),
    Concept("set.subset", "set", ("zawieranie", r"\subseteq", "⊆"), "Set.Subset", "mathlib", "non-strict inclusion"),
    Concept("linear_algebra.linear_map", "linear_algebra", ("odwzorowanie liniowe",), "LinearMap", "mathlib", "requires scalar and module context"),
    Concept("linear_algebra.submodule", "linear_algebra", ("podprzestrzeń liniowa",), "Submodule", "mathlib", "requires scalar and module context"),
    Concept("linear_algebra.independent", "linear_algebra", ("niezależność liniowa",), "LinearIndependent", "mathlib", "requires indexed family and scalar context"),
)


def _payload():
    return {"schema_version": SCHEMA_VERSION, "dictionary_version": DICTIONARY_VERSION,
            "lean_toolchain": LEAN_TOOLCHAIN, "mathlib_rev": MATHLIB_REV,
            "concepts": [asdict(c) for c in _CONCEPTS]}


def dictionary_sha256() -> str:
    raw = json.dumps(_payload(), ensure_ascii=False, sort_keys=True,
                     separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _candidate(concept):
    # asdict constructs a separate dictionary, never exposes mutable registry.
    result = asdict(concept)
    result["aliases"] = list(result["aliases"])
    result["mapping_status"] = "needs_review"
    result["declaration_check"] = "not_run"
    return result


def lookup(alias: str, scope: str | None = None) -> dict:
    """Resolve one exact alias only inside an explicitly supplied scope.

    Without scope return candidates, never a selected declaration. No Unicode
    normalisation, stemming, fuzzy match, implicit context or code generation.
    """
    result = {"schema_version": SCHEMA_VERSION,
              "dictionary_version": DICTIONARY_VERSION,
              "dictionary_sha256": dictionary_sha256(),
              "lean_toolchain": LEAN_TOOLCHAIN, "mathlib_rev": MATHLIB_REV,
              "certificate": False, "candidate_status": "not_generated",
              "proof_status": "not_run", "external_transfer_allowed": False,
              "lean_code": None, "selected": None, "candidates": []}
    if (type(alias) is not str or not 1 <= len(alias) <= MAX_QUERY_CHARS
            or not alias.isprintable() or not alias.strip()):
        return {**result, "status": "invalid_input", "error": "invalid_alias"}
    if scope is not None and (type(scope) is not str or scope not in SCOPES):
        return {**result, "status": "invalid_input", "error": "invalid_scope"}
    matches = [c for c in _CONCEPTS if alias in c.aliases
               and (scope is None or c.scope == scope)]
    result["candidates"] = [_candidate(c) for c in matches]
    if not matches:
        return {**result, "status": "unsupported"}
    if len(matches) > 1:
        return {**result, "status": "ambiguous"}
    if scope is None:
        return {**result, "status": "needs_context"}
    return {**result, "status": "matched_candidate", "selected": _candidate(matches[0])}
