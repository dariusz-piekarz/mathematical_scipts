# LST-01 distributivity — stabilization and separate final audit (2026-11-22)

## Scope and immutable evidence
- Pilot stage 2, same theorem `thm:logic-distributivity`; no transition to LST-02 or LA-01.
- Branch `biblioteka-matematyczna-iteracja-6`; HEAD before report commit: `2d97e305a7d570927c4aa0646a14ea8948c81b34`.
- Canonical source: `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex`, Git blob `03f0971888288934e47c3453fd8f0de0a2c71469`, source SHA256 pinned in manifest `9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0`.
- Lean source: `application/lean/src/LST01_SyntaxValuations.lean`, Git blob `71f5206b8642f53c45d28004ced57d02e0ebe984`; manifest blob `b9e6c77112af51b59c9221681d034b7302215c23`.
- Read current `application/docs/LEAN_FORMALIZATION_PLAN.md`, `application/ROADMAP_I_DZIENNIK.md`, `AGENTS.md`, original TeX, Lean and manifest.
- GitHub compare `664b5ede5ea0ebebb83fc34495b1953f0f4e4497...2d97e305a7d570927c4aa0646a14ea8948c81b34`: no changed files under `application/lean/` or the source TeX; thus the relevant Lean CI evidence remains applicable to these unchanged blobs.

## Review after preceding re-audit (clean control 2)
The source has three independent clauses for arbitrary formulas: double negation, conjunction over disjunction, and disjunction over conjunction. The three manifest declarations `lst01_syntax_double_negation`, `lst01_syntax_and_over_or`, `lst01_syntax_or_over_and` each universally quantify valuations `Nat → Bool` through `LST01.equivalent`. Arbitrary formulas may share atoms; the proof splits on evaluated Boolean values, without assuming independent atomic variables. No missing source clause or extra premise was found.

Independent exhaustive Boolean checks were actually executed in this iteration: 8 triples × 3 identities = **24/24**. Manual inspection found no `sorry`, `admit`, or user-added axioms in the three declarations. These checks are not a substitute for the Lean kernel.

## Real CI evidence and version
GitHub Actions run [45023719378](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023719378), commit `664b5ede5ea0ebebb83fc34495b1953f0f4e4497`, completed **success**. Its `lean-pilot` job specifically reports successful steps `Check exact Lean and Mathlib revisions`, `Compile registered Lean files and check axioms`, and `Execute real Lean MetaM constant introspection (mandatory, no skips)`. Workflow declares Lean **v4.26.0** and Mathlib commit `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`. This is **actual remote Lean execution**, not a locally run command. The workflow step conclusions were checked through GitHub API; raw stdout and full per-declaration axiom log were not downloaded in this iteration.
Local `command -v lake` and `command -v lean` both found no executable: local `lake env lean` = `toolchain_unavailable/not_run`. Remote CI provides a successful run on identical relevant source blobs, not a local execution.

## Separate skeptical final audit (after positive CI and clean review)
A second, separately reasoned pass compared the literal three LaTeX identities to the three Lean AST constructions, checking parentheses, order of `conj`/`disj`, universal formula variables, evaluation of shared atoms, and whether `equivalent` is a universally quantified equality rather than object-language `iff`. All three correspondences agree. Verified that the manifest groups all three declarations under the exact source label and the pinned source digest. No correction identified; this pass is separate from the preceding truth-table check. No new code or manifest changes, so no reset of the clean-review count.

## Status and limits
- Corrections to theorem/manifest in this iteration: **0**.
- Clean semantic/static reviews since last theorem-source change: **2** (previous re-audit and current review); extra separate final skeptical audit: **1**, clean.
- Lean execution: **remote CI success** for unchanged relevant blobs; local unavailable.
- For this particular mapped theorem, the stabilization criteria of source correspondence, CI kernel compilation, axiom audit and an additional independent clean audit are met **at the pinned source and Lean blob versions only**. This is not a global project certificate or guarantee against future changes. `certificate=false` remains unchanged.
- Pilot corpus: **5/20–30 mapped source theorem labels**. All five entries are `statement_status=approved` in manifest and the relevant Lean files are unchanged since the successful CI above. **5/5 mapped labels have current applicable successful remote CI compilation and source-level semantic review**; no additional label added here. The corpus target is not met.
- Remaining: extend to LST-02/LA-01 only after treating this pinned theorem as stable; rerun CI if Lean, source, manifest or dependencies change. Full raw log was not independently inspected in this run.
