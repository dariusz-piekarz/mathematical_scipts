# Lean 4 — LST-01 distributivity, 2026-11-22

## Scope and source
Branch: `biblioteka-matematyczna-iteracja-6`. Initial branch HEAD read: `dcd8bd2e8931c8aa3b09b1779bcdcad3e7a6cb40`.
Read `application/docs/LEAN_FORMALIZATION_PLAN.md`, `application/ROADMAP_I_DZIENNIK.md`, `AGENTS.md`, and canonical `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex` directly from the branch. Source label: `thm:logic-distributivity`; three clauses: double negation, conjunction distributing over disjunction, disjunction distributing over conjunction. Pinned source SHA256: `9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0` (previously audited source fingerprint; not recomputed in this runner).

## Formalization
Extended `application/lean/src/LST01_SyntaxValuations.lean` with:
- `lst01_syntax_double_negation`
- `lst01_syntax_and_over_or`
- `lst01_syntax_or_over_and`

All quantify over arbitrary `LST01.Formula`, and `LST01.equivalent` quantifies over **every** valuation `Nat → Bool`. Each proof splits on the values of the constituent formulas (2 or 8 combinations), and simplifies the exact truth-functional semantics. These are not replacements by bare `Prop` tautologies. Source statement comparison: `approved` for the pinned source. Three source clauses, one theorem label, one manifest entry. No `sorry`, `admit`, or additional axioms; each declaration has a `#print axioms` request.

## Execution evidence
`lake env lean`: **not_run / toolchain_unavailable** in the present environment; `which lake` returned no path. Network DNS resolution of github.com also failed in the local container, but GitHub connector reads/writes succeeded. Declared project toolchain: Lean `v4.26.0`; pinned Mathlib revision `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`. No current local compiler version/log can be reported. CI may execute after commit; do **not** treat that as already passed. The CI script discovers the three new declarations through the existing module and requires their axiom logs. No certificate awarded.

## Corpus accounting
Five distinct mapped source theorem labels in `manifest.json` (four pre-existing, one new); six source clauses in the first three labels, one equivalence-test clause, and three new clauses: **10 source clauses total** (2+3+1+1+3 = 10). The three earlier labels have previously recorded successful compilation and semantic audit. The equivalence-test label and the newly added distributivity label remain **unverified in this run**. Thus **3/20–30 source theorem labels** have historical compile+semantic evidence, **5/20–30** are mapped and semantically reviewed; no new compiled verification is claimed.

## Constraints
No changes to backend, frontend, canonical TeX, or other audits. Initial separate Lean module was consolidated into the already directly compiled module after inspecting the CI workflow, which invokes `lake env lean` on each source file without building a local import artifact. The redundant module was deleted. Final branch commit and CI must be checked before upgrading status.
