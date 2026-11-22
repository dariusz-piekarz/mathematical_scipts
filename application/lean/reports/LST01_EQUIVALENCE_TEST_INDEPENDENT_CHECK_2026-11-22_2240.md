# Lean pilot — independent semantic check, LST-01 thm:equiv-test

- Date: 2026-11-22 (Europe/Warsaw)
- Stage: stabilization of the **same** theorem `LST-01:thm:equiv-test`, not a new theorem.
- Branch: `biblioteka-matematyczna-iteracja-6`
- HEAD inspected before report: `dff6f5843a98ea5c6377bafff501f8c5261a1355`
- Source: `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex`, lines 384–397, label `thm:equiv-test`, Git blob `03f0971888288934e47c3453fd8f0de0a2c71469`.
- Lean: `application/lean/src/LST01_SyntaxValuations.lean`, Git blob `71f5206b8642f53c45d28004ced57d02e0ebe984`; declaration `lst01_syntax_equivalence_test`.
- Manifest: `application/lean/manifest.json`, blob `7c63531f4a63bea56eab4dfaaf285616b94f1733`; source SHA256 as recorded: `9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0`. This SHA256 was **not independently recomputed** in this run.
- Toolchain declaration: `leanprover/lean4:v4.26.0`; Mathlib revision `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`.

## Independent semantic audit

The source states for arbitrary propositional formulas φ and ψ: semantic equivalence iff their biconditional is a tautology. The Lean `Formula` datatype has atomic letters indexed by Nat and five connectives; a valuation is `Nat → Bool`. `equivalent p q` means equality of Boolean evaluations for **every common valuation**, and `tautology (.iff p q)` means that the biconditional evaluates to true for **every** valuation. This matches the original theorem, including letters occurring in only one formula and repeated letters.

The declaration proves both directions using `constructor`, and the definition of `eval` for `.iff` is `decide (eval ν p = eval ν q)`. No new axioms, `sorry`, or `admit` appear in the inspected declaration. This is a manual syntactic and semantic inspection, **not** a new kernel proof check.

Independent exhaustive Boolean regression: enumerated all 16 Boolean functions on two propositional variables, all 256 ordered pairs, and all 4 assignments per pair (1024 checks). At every assignment, equality of the two function values agreed with the biconditional truth value; 1024/1024 checks succeeded. This is a test of the semantics, not a Lean compilation.

## Execution and stabilization

- Fresh local `lake env lean`: **not_run / toolchain_unavailable**. Both `lake` and `lean` were absent from PATH in the available container.
- Fresh Lean version output and compiler log: unavailable; only declared version above.
- Historical CI run [45023719378](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023719378) was documented in prior reports; **not rerun** here. Do not treat it as fresh verification.
- Fresh independent SHA256 of the canonical TeX: not performed.
- Clean **full** audits since the latest manifest change: **0 established by this run** (semantic regression is only a partial check).
- Separate final skeptical audit: **not performed** because prerequisites are not met.
- Stage status: **open; stability not certified**.

## Pilot totals

Current manifest contains **5 mapped source labels** from LST-01, out of target 20–30; all 5 carry `statement_status=approved`. This run adds **0** new Lean-kernel verifications. Previous reports record historical CI evidence for the mapped module; current proof status must be determined by actual execution and source integrity, not inferred from the manifest.

No changes to backend, frontend, canonical TeX, other audits, or formalization code. The next check must establish a fresh Lean execution (or explicitly remain blocked), independently recompute source SHA256, and perform the required clean full audits plus an additional final audit.
