# Lean pilot — independent re-audit of LST-01 distributivity (2026-11-22)

## Scope and provenance
- Stage: 2, stabilization of the *same* mapped source theorem `thm:logic-distributivity`; no transition to another theorem.
- Branch: `biblioteka-matematyczna-iteracja-6`; HEAD checked before write: `1244136f6c5bebec44ab3b444b44769566f8ce90`. Initial read: `efda2f273a77395bea5631629db79a977c5c1f32`; concurrent movement observed. Do not interpret this report as a snapshot of unrelated concurrent changes.
- Canonical source: `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex`, Git blob `03f0971888288934e47c3453fd8f0de0a2c71469`, manifest SHA256 `9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0`.
- Lean source: `application/lean/src/LST01_SyntaxValuations.lean`, Git blob `71f5206b8642f53c45d28004ced57d02e0ebe984`.
- Manifest: `application/lean/manifest.json`, Git blob `b9e6c77112af51b59c9221681d034b7302215c23`.
- Read `application/docs/LEAN_FORMALIZATION_PLAN.md`, `application/ROADMAP_I_DZIENNIK.md` and `AGENTS.md` before the audit.

## Source-to-formal-statement comparison
The single source theorem has three clauses, all quantified over arbitrary propositional formulas:
1. `¬¬p ≡ p` maps to `lst01_syntax_double_negation`.
2. `p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)` maps to `lst01_syntax_and_over_or`.
3. `p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)` maps to `lst01_syntax_or_over_and`.

The Lean domain is `LST01.Formula`, with an inductive syntax of atoms and five connectives, not unrestricted `Prop`. `LST01.equivalent` universally quantifies `ν : Nat → Bool`; repeated atoms therefore share their value. This agrees with the source's logical equivalence (distinct from a biconditional formula). Source `p,q,r` are formulas, not independently assigned Boolean variables. The proofs case-split on their *evaluations* for an arbitrary valuation, which is valid even when formulas share letters. There is no extra hypothesis or excluded class of formulas. The three statements are semantically aligned with the inspected LaTeX.

## Independent tests and limitations
- Executed independent exhaustive Python truth-table checks for all 8 Boolean triples: 24/24 clause evaluations passed. This is a test of the mathematical identities, **not** a Lean elaboration or kernel proof.
- Manually inspected all three declarations and proof scripts: no `sorry`, `admit` or added axioms in these proofs. `#print axioms` directives are present in the Lean file but **were not executed in this run**.
- `command -v lake` and `command -v lean` returned no executable in the available container. Therefore `lake env lean` could not be run; Lean version is **not locally observed**. Repository declares v4.26.0; this is configuration, not an executed version check.
- Execution status for this audit: `toolchain_unavailable` / `not_run`; no new `verified` result. Historical CI claims in README are not a substitute for a fresh build of the current tree. No new GitHub Actions conclusion was confirmed here.
- Source/manifest full-byte SHA256 integrity and current HEAD compilation were not independently reproduced by the truth-table test. Git blob IDs above identify inspected content; manifest's SHA256 is read from manifest.
- No changes to the existing theorem or manifest were justified by this inspection.

## Stabilization protocol
- Stage: LST-01 `thm:logic-distributivity`, re-audit 1.
- Corrections in this iteration: 0.
- Clean independent semantic/static reviews since last source change: **1** (this review); actual Lean/CI tests since last change: **0** in this run.
- Extra final independent audit: **not performed**; prerequisite of fresh positive kernel compilation and regression checks is unmet.
- Stability: **NOT ESTABLISHED**. Do not label PASS/verified/certified.
- Pilot corpus: **5/20–30 mapped source theorem labels**, **3 historically compiled and semantically reviewed labels as documented in earlier project records**, **0 newly formally verified in this run**. The two newer labels await confirmed compilation; this audit does not increase the verified count.

Next: obtain a genuine pinned `lake env lean src/LST01_SyntaxValuations.lean` run and axioms output, recheck source SHA and all manifest entries against the current HEAD, then repeat a clean independent review and a separate final audit before moving to the next source theorem.
