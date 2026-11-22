# Lean pilot — LST-01 equivalence-test: independent re-audit (2026-11-22)

## Scope and provenance
- Stage 2, source label `thm:equiv-test` (same theorem as earlier initial formalization; no new theorem introduced).
- Branch `biblioteka-matematyczna-iteracja-6`; HEAD inspected immediately before this report: `39a918aa53e5dc58c2b2842bddc8bc8770448633`.
- Read `AGENTS.md`, `application/docs/LEAN_FORMALIZATION_PLAN.md`, `application/ROADMAP_I_DZIENNIK.md`, canonical `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex`, `application/lean/manifest.json`, and `application/lean/src/LST01_SyntaxValuations.lean`.
- Canonical TeX Git blob `03f0971888288934e47c3453fd8f0de0a2c71469`, manifest source SHA256 `9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0`; Lean Git blob `71f5206b8642f53c45d28004ced57d02e0ebe984`; manifest blob `b9e6c77112af51b59c9221681d034b7302215c23`.

## Exact semantic correspondence
Source: for arbitrary propositional formulas φ and ψ, φ ≡ ψ iff (φ ⇔ ψ) is a tautology. `lst01_syntax_equivalence_test (p q : LST01.Formula)` states `LST01.equivalent p q ↔ LST01.tautology (.iff p q)`. `equivalent` is equality of evaluations at **every** valuation `Nat → Bool`; `tautology` quantifies over the same valuations; `.iff` is an object-language constructor, distinct from the outer meta-level `↔`. The source's alphabet is countable; every finite source formula is represented. Repeated atoms use the same valuation value. No independence assumption is made for shared atoms.

## Actual controls
1. Read and manually checked both directions of the Lean proof: forward uses equality of Boolean evaluations; backward extracts equality from `decide (eval ν p = eval ν q) = true`. The source requires no extra assumptions. No `sorry`, `admit`, or user-added axioms in the checked declaration.
2. Independently executed Python exhaustive Boolean test for the four pairs of values of φ and ψ: **4/4 passed**. This tests truth-functional semantics, **not** the Lean kernel.
3. GitHub Actions [45023719378](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023719378) at commit `664b5ede5ea0ebebb83fc34495b1953f0f4e4497`: API reports `lean-pilot=success`; `Check exact Lean and Mathlib revisions`, `Compile registered Lean files and check axioms`, `Execute real Lean MetaM constant introspection (mandatory, no skips)`, and `Upload Lean compilation and axiom evidence` all concluded `success`. Workflow declares Lean v4.26.0 and Mathlib `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`. The raw compiler/axiom log was **not** downloaded or independently inspected in this iteration.
4. GitHub compare `664b5ede...39a918aa53e5dc58c2b2842bddc8bc8770448633` returned no changes to canonical TeX, Lean source or manifest; only an unrelated-to-theorem Lean stabilization report was added under `application/lean/`. Thus CI evidence applies to unchanged theorem bytes.
5. Local `command -v lake` and `command -v lean` returned no executables; local `lake env lean`: **toolchain_unavailable / not_run**, with no local compiler log.

## Separate skeptical final inspection
After the truth-table test and CI check, independently re-examined quantifier scopes, `Prop` versus syntax, parenthesization, and the possibility that two formulas share an atom. No new semantic discrepancy found. This is a separate source-to-declaration review, not an additional Lean execution.

## Status and limitations
- New corrections to theorem/manifest: **0**. Current iteration's clean semantic review count since last theorem edit: **1**, plus **1** separate skeptical final inspection; an earlier initial semantic review is documented in `LST01_EQUIVALENCE_TEST_2026-11-22.md`.
- Compilation: applicable **remote CI success**, not a locally executed `lake env lean`; raw per-declaration compiler and axiom output not independently inspected. Do not infer an application certificate; `certificate=false` remains appropriate. No unconditional global PASS or full-corpus stability claimed.
- Corpus: **5/20–30** source labels mapped and semantically approved in manifest; **5/5** map to unchanged files covered by the successful remote CI run (subject to its audit checks). **0 new labels** and **0 newly executed local Lean proofs** in this iteration.
- No edits to backend, frontend, canonical TeX, other audit reports or existing Lean source/manifest.
