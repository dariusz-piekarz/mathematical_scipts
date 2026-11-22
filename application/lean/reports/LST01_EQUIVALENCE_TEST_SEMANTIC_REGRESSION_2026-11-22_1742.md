# Lean 4 — LST-01 `thm:equiv-test`: independent semantic regression (2026-11-22)

## Stage and provenance
- Stage: 2 (pilot), repeated inspection of **the same** theorem `thm:equiv-test`; no new theorem or scope expansion.
- Branch: `biblioteka-matematyczna-iteracja-6`; inspected HEAD: `fbe5c066defa8cc53fcee073f9ae06182d8f2715`.
- Read at current branch: `application/docs/LEAN_FORMALIZATION_PLAN.md`, `application/ROADMAP_I_DZIENNIK.md`, `AGENTS.md`, `application/lean/manifest.json`, `application/lean/src/LST01_SyntaxValuations.lean`, and `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex`.
- Source: `LST-01`, `thm:equiv-test`; mapped declaration: `lst01_syntax_equivalence_test`. Manifest currently contains 5 mapped labels, all marked `statement_status=approved`. The source SHA256 recorded there is `9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0` (manifest assertion, not recomputed in this run).

## Independent skeptical semantic review
- Canonical statement quantifies over **arbitrary formulas** φ and ψ; semantic equivalence means agreement for every common valuation. It asserts equivalence to tautologicity of the **object-language** biconditional.
- Lean statement: `LST01.equivalent p q ↔ LST01.tautology (.iff p q)` with `p q : LST01.Formula`. Here `Formula` is an inductive syntax with atom/neg/conj/disj/imp/iff; `Valuation := Nat → Bool`; `equivalent` and `tautology` quantify over **all** valuations. Outer `↔` is metalogical; `.iff` is syntax evaluated by `decide (eval ν p = eval ν q)`.
- Distinct letters can vary independently; repeated occurrences of the same letter share one valuation. Quantification over valuations on all `Nat` is equivalent for this finite-support syntax to quantification over letters occurring in either formula: unused assignments cannot affect evaluation.
- Both proof directions inspect correctly at source level: `decide` of Boolean equality is true exactly when evaluations agree. No extra theorem hypotheses, `sorry`, `admit` or declared custom axioms found in the inspected declaration.

## Executed tests
- Executed an independent Python regression over the complete **16 distinct Boolean truth functions of two atoms** (built by closing the two coordinate projections under negation, conjunction, disjunction, material implication and biconditional). For each of **256 ordered pairs** and each of four valuations (**1024 valuation rows**), compared pointwise equality of values against independently expanded biconditional `(x and y) or ((not x) and (not y))`. **256/256 pairs, 1024/1024 rows passed**. This is exhaustive over Boolean functions of two variables, **not** a proof about all formula trees or a Lean kernel run.
- Local `command -v lake` and `command -v lean`: neither executable found. Thus `lake env lean` = **not_run / toolchain_unavailable**; no local compiler version or compiler log.
- Checked GitHub Actions run [45023719378](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023719378) jobs endpoint: `lean-pilot` concluded `success`; steps `Check exact Lean and Mathlib revisions`, `Compile registered Lean files and check axioms`, and `Execute real Lean MetaM constant introspection` each concluded `success`. This is **historical CI evidence**, not a fresh compiler execution; raw compilation/axiom output was not fetched. Project pins from plan: Lean v4.26.0, Mathlib `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67` (declared, not independently inspected from raw logs).
- Source-level review and the independent truth-function regression were separate checks, with no detected corrections. **Clean checks this run: 2** (source review + semantic regression); **extra final full audit: not claimed** because the fresh kernel/integration precondition is absent. Corrections this run: 0.

## Status and restrictions
- Pilot corpus: **5/20–30** mapped source labels, **5** manifest entries marked semantically approved, **0 newly Lean-verified in this iteration**. The number currently independently kernel-verified against current source fingerprints **cannot be established from this run alone**; previous CI evidence is historical and requires artifact/fingerprint reconciliation.
- No source code, manifest, canonical TeX, application backend/frontend, or other audit modified. Only this dedicated report is added.
- **No new PASS, stability declaration, application certificate or publication claim.** Next run should inspect raw CI evidence or execute actual pinned Lean, verify exact source/Lean hashes, and repeat a distinct final skeptical audit before advancing.
