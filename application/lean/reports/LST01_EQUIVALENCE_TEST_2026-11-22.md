# Lean pilot — LST-01 equivalence test (2026-11-22)

## Source and exact statement
- Branch: `biblioteka-matematyczna-iteracja-6`.
- Canonical file: `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex`.
- Source label: `thm:equiv-test`, theorem “Test równoważności”.
- Source SHA256: `9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0`.
- Statement: for any propositional formulas φ, ψ, semantic equivalence φ ≡ ψ holds if and only if the formula (φ ⇔ ψ) is a tautology.

## Mapping and semantics
- Lean declaration: `lst01_syntax_equivalence_test` in `src/LST01_SyntaxValuations.lean`.
- `LST01.Formula` is the inductive grammar, `LST01.Valuation := Nat → Bool`; `LST01.equivalent` quantifies over *all* valuations and compares evaluations; `LST01.tautology` requires evaluation to `true` for *all* valuations.
- Both sides quantify over the same unrestricted valuation type. Repeated atoms share one assigned Boolean value. The biconditional is a constructor of `Formula`, not a meta-level `Prop` biconditional; only the **statement about evaluations** uses `↔`.
- This is an exact semantic translation of the theorem under the chapter's countable propositional alphabet; status `statement_status=approved` for the pinned source version. Approval is not a Lean execution result.

## Execution
- Local command intended: `cd application/lean && lake env lean src/LST01_SyntaxValuations.lean`.
- Local `lake` and `lean` executables: not found in PATH; **proof_status=toolchain_unavailable / not_run** for this new theorem.
- Toolchain declared by project: Lean v4.26.0; Mathlib commit `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`. These are configuration declarations, not a version measured during this run.
- No compiler log exists for this declaration. `#print axioms lst01_syntax_equivalence_test` was added for subsequent CI kernel checks. No `sorry`, `admit` or additional axioms were introduced.
- Previous CI confirmation of 14 other declarations does not establish compilation of this new one. Do not mark verified or issue a certificate before successful CI plus axiom audit.

## Corpus count
- Before: 3 distinct source labels, 6 main mapped clauses, 14 total Lean declarations in the four files, per prior report.
- After this change: **4 distinct source labels**, **7 mapped clauses**, **15 Lean declarations** (including helpers); **3 previously approved source labels with earlier successful Lean CI**, **1 newly semantically reviewed label awaiting Lean execution**.
- Strictly confirmed *in this run*: **0 newly compiled/verified**. Target remains **20–30 source theorem examples**; current count **4/20–30** mapped and reviewed, at most **3/20–30** with earlier compilation evidence (subject to current SHA and CI checks).

## Follow-up
Check the next Lean GitHub Actions run for the new declaration, actual `#print axioms` output, and manifest source digest; investigate any compilation errors before claiming verification. Then continue with `thm:valuation-well-defined-xli` or LST-02/LA-01 without modifying canonical TeX.
