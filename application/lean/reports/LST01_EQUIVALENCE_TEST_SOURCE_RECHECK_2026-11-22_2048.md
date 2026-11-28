# LST-01 — thm:equiv-test: source and provenance recheck

Date: 2026-11-22; stage: stabilization of the SAME theorem, not a new theorem.
Branch: `biblioteka-matematyczna-iteracja-6`; HEAD at pre-write check: `203542b7f508c3d3e543732af80d04c43665a39e`.

## Source and mapping
- Canonical TeX: `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex`, Git blob `03f0971888288934e47c3453fd8f0de0a2c71469`.
- Source label: `thm:equiv-test`. Original assertion: for any propositional formulas phi and psi, semantic equivalence holds iff the biconditional is a tautology.
- Lean: `application/lean/src/LST01_SyntaxValuations.lean`, Git blob `71f5206b8642f53c45d28004ced57d02e0ebe984`; declaration `lst01_syntax_equivalence_test`.
- Manifest: `application/lean/manifest.json`, Git blob `b9e6c77112af51b59c9221681d034b7302215c23`; 5 mapped labels, all in LST-01; LST-02/LA-01 not yet mapped.
- The manifest pins the TeX SHA256 `9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0`. This run did NOT independently recompute SHA256 from raw bytes: Git blob SHA-1 is not SHA256.

## Critical review
`LST01.Formula` is inductive syntax (atoms indexed by Nat, negation, conjunction, disjunction, implication, biconditional), not a synonym for `Prop`. `Valuation := Nat → Bool` supplies a single consistent value for every occurrence of an atom. `equivalent p q` quantifies over ALL valuations and compares evaluations; `tautology (.iff p q)` quantifies over the SAME valuations. The `iff` evaluation is `decide (eval ν p = eval ν q)`. Both implications of the Lean theorem therefore match the source, with no additional assumptions.

The proof uses `simp [LST01.eval, h ν]` forward and `simpa [LST01.eval] using h ν` backward. No `sorry` or `admit` occurs in the reviewed declaration; this is a textual check, not kernel verification. A full source-to-kernel audit remains required.

## Execution and blockers
- Local `lake env lean`: **not_run / toolchain_unavailable** (no local `lake` executable); no new Lean version output or kernel log.
- Prior CI evidence is documented in earlier reports, including run 45023719378 (Lean 4.26.0, Mathlib 2df2f0150c275ad53cb3c90f7c98ec15a56a1a67). This run did not independently re-download the compiler log or establish exact source-byte identity with that run.
- Manifest `semantic_review` for this item still says “Lean compilation pending”; this is historical text, not a reliable current proof status. It should be reconciled only against independently checked run provenance.
- Clean full audits since last correction in THIS run: **0 certified**. Separate final skeptical audit: **not performed**, as fresh Lean execution and SHA256 comparison remain blocked. Stability: **NOT CONFIRMED**; certificate remains false.
- Corpus: 5/20–30 labels mapped and semantically marked approved; 0 newly kernel-verified this run. Do not infer current full certification from historical CI.

No changes to code, manifest, canonical TeX, backend, frontend or other audits. This report is an audit artifact, not a claim of completed stabilization.
