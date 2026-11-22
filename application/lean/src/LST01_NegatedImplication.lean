import Mathlib

/-!
LST-01, thm:negated-implication-xli (Negacja implikacji).
This states the classical propositional equivalence for values of formulas.
A full syntactic-formula/valuation formalization and semantic alignment review
remain separate tasks; this is not an approval of equivalence with the LaTeX.
-/

theorem lst01_negated_implication (p q : Prop) :
    ¬ (p → q) ↔ (p ∧ ¬ q) := by
  classical
  tauto

#print axioms lst01_negated_implication
