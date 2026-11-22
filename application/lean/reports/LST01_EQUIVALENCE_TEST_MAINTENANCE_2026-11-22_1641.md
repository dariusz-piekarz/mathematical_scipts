# Lean 4 — LST-01 thm:equiv-test: maintenance inspection (2026-11-22)

## Provenance and scope
- Existing branch: `biblioteka-matematyczna-iteracja-6`; HEAD at inspection: `daa892cd009b37ab0e77ecb6fb8b35e6fb6e2c83`.
- Read current `application/docs/LEAN_FORMALIZATION_PLAN.md`, `application/ROADMAP_I_DZIENNIK.md`, `AGENTS.md`, original `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex`, `application/lean/manifest.json`, and `application/lean/src/LST01_SyntaxValuations.lean` from this branch.
- Source label `thm:equiv-test`, canonical TeX Git blob `03f0971888288934e47c3453fd8f0de0a2c71469`; Lean blob `71f5206b8642f53c45d28004ced57d02e0ebe984`; manifest blob `b9e6c77112af51b59c9221681d034b7302215c23`.
- Scope is the same existing theorem, not a new mapping. No modifications to theorem code, manifest, canonical TeX or application code.

## Critical semantic inspection
- Source: for all propositional formulas φ, ψ, semantic equivalence φ ≡ ψ iff the object-language biconditional φ ⇔ ψ is a tautology.
- Lean: `lst01_syntax_equivalence_test (p q : LST01.Formula) : LST01.equivalent p q ↔ LST01.tautology (.iff p q)`.
- `LST01.Formula` is inductive object-language syntax; `LST01.Valuation := Nat → Bool` assigns consistent truth values to repeated atoms. `equivalent` and `tautology` quantify over all valuations; the outer Lean `↔` is meta-logical, whereas `.iff` is object-language syntax. The theorem has no additional hypotheses.
- Proof inspection: forward direction rewrites Boolean equality under each valuation; reverse direction extracts equality from `decide (eval ν p = eval ν q) = true`. No `sorry`, `admit`, or custom axioms in this declaration.

## Executed checks and limitations
- Independent Python semantic regression: six explicit formulas over two atoms (`p`, `q`, `¬p`, `¬q`, `p∧q`, `p→q`); 36 ordered formula pairs and 144 valuation rows; compared equality of formula values with independently computed biconditional `(p∧q)∨(¬p∧¬q)`: **36/36 pairs passed**. This is a finite model test, not a Lean proof.
- Local `which lake`: executable absent; `lake env lean` **not_run / toolchain_unavailable**; no local Lean version or compiler log. Declared project toolchain in the existing plan: Lean v4.26.0 / Mathlib commit `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`, not independently executed in this run.
- Previous remote CI success [45023719378](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023719378) is historical evidence; this run did **not** fetch raw kernel/compiler/axiom logs or execute a new Lean compilation. Do not upgrade proof status solely from Python tests.
- Separate skeptical inspection revisited quantifier scope, shared atoms, distinction between `Prop` and syntax, and object-level biconditional; no new issue found. This is not a substitute for fresh Lean execution.

## Stabilization status
- Stage 2, existing `thm:equiv-test`; this iteration: one clean semantic inspection and one separately performed skeptical check, **0 corrections**, **0 new formalizations**. The prior report documents earlier controls; current clean-control count must not be conflated with a fresh Lean run.
- Manifest currently contains **5/20–30** mapped labels, all marked `statement_status=approved`; this run independently checked one of them, with **0 newly kernel-verified**. Earlier CI coverage of five labels is documented separately and not re-certified here.
- **No new PASS/stability certificate**: local toolchain unavailable and no fresh raw CI evidence. Maintain the same theorem until requirements for any stronger current certification are met; application certificate remains false.
