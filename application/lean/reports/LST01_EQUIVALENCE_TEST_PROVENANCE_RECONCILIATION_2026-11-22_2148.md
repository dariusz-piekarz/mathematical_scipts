# LST-01 thm:equiv-test — evidence reconciliation, 2026-11-22 21:48 CET

## Scope and provenance
- Stage: same theorem `LST-01:thm:equiv-test`; no progression to a different theorem.
- Branch: `biblioteka-matematyczna-iteracja-6`.
- First observed HEAD: `7be364c1c3e5b5cf1d3fb58682e62c8912ef8de2`. HEAD before manifest write: `caf5e553dde0e76a91b40bb50e6e1c5cd5c78f17` (parallel work); manifest update commit: `86a3ed1c1772345bf84234eba60395792a86e941`.
- Read current `application/docs/LEAN_FORMALIZATION_PLAN.md`, `application/ROADMAP_I_DZIENNIK.md`, `AGENTS.md`, canonical `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex`, manifest and Lean source.
- Canonical label: `thm:equiv-test`; source states that any two propositional formulas are logically equivalent iff their biconditional is a tautology. Its definition explicitly requires one common valuation over all letters occurring in either formula.

## Independent source/CI provenance check
Historical CI run: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023719378, head `664b5ede5ea0ebebb83fc34495b1953f0f4e4497`, job `137212099319`, conclusion `success`. Downloaded the real job log this iteration.
- Log identifies Lean `4.26.0` (Lean commit `d8204c9fd894f91bbb2cdfec5912ec8196fd8562`) and Mathlib `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`.
- Log includes `'lst01_syntax_equivalence_test' depends on axioms: [propext]`. `propext` is a standard Lean axiom, not an ad hoc axiom. Compilation and axiom check succeeded in the historical job.
- The historical job's `test_current_repo_approved_manifest_matches_canonical_tex` and `test_digest_guard_rejects_modified_tex` both passed, providing historical evidence for the SHA256 pin.
- Independent GitHub blob comparison, historical CI commit versus current first-observed HEAD: canonical TeX `03f0971888288934e47c3453fd8f0de0a2c71469` = same; Lean source `71f5206b8642f53c45d28004ced57d02e0ebe984` = same; `lean-toolchain` `e59446d59f6a2bf7f43d60788e2088a603ae6bd4` = same; `lakefile.toml` `b5ae0482a5ef5b0632209576491c3e61c344ad68` = same; `application/scripts/lean_ci_audit.py` `a88a5f672c2d042e93674cfb37773c8a75e86cee` = same.
- Workflow file has **changed**: old blob `c012c766a14e772672360a144d58d763d6fa9400`, newer blob `eec430a4aea6be0304e9fe90c3278e4e40df2e76`. Thus the old run does **not** establish that the current workflow passes unchanged. Recheck current workflow separately.
- Manifest SHA256 recorded for source: `9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0`. Fresh independent SHA256 calculation was not performed in this run. Historical digest test and identical Git blob are evidence, not a new SHA256 computation.

## Semantics
`LST01.Formula` is an inductive syntax (`atom`, `neg`, `conj`, `disj`, `imp`, `iff`), not merely `Prop`. `Valuation := Nat → Bool`; `equivalent p q := ∀ ν, eval ν p = eval ν q`; `tautology (.iff p q) := ∀ ν, eval ν (.iff p q) = true`. The theorem proves both directions for arbitrary `p q : Formula`, with one shared valuation. This agrees with the canonical definition, including variables occurring only on one side. No `sorry` or `admit` in the examined declaration.

## Changes and status
- Corrected stale `semantic_review` text in `application/lean/manifest.json` that previously said `Lean compilation pending`; replaced with narrowly scoped historical CI evidence. No claim of a fresh execution or application certificate.
- No changes to canonical TeX, backend, frontend, Lean theorem code, or other audits.
- Local `lake env lean`: **not_run / toolchain_unavailable** (neither `lake` nor `lean` present in the execution environment).
- New Lean kernel verifications this iteration: **0**; historical compiled mappings: **5 of target 20–30** according to current manifest and historical CI; independently rechecked theorem here: **1**.
- Stability: **NOT CONFIRMED**. Manifest metadata changed, so clean-audit counter since last correction = **0**. Separate final clean audit = **not performed**. A current workflow run and subsequent independent clean audits remain necessary; do not issue PASS or certificate.
