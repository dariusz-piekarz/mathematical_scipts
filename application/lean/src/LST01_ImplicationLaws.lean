import Mathlib

/-!
LST-01, thm:implication-laws (Rozwinięcie i przeciwstawienie implikacji).
The Polish theorem refers to equivalence of arbitrary syntactic formulas under
all valuations. These statements describe their classical Prop-level values,
not an encoding of formula syntax and valuation functions.
All three asserted laws are represented below. Semantic review pending.
-/

theorem lst01_implication_as_disjunction (p q : Prop) :
    (p → q) ↔ (¬ p ∨ q) := by
  classical
  tauto

theorem lst01_implication_contrapositive (p q : Prop) :
    (p → q) ↔ (¬ q → ¬ p) := by
  classical
  tauto

theorem lst01_modus_ponens (p q : Prop) :
    ((p → q) ∧ p) → q := by
  intro h
  exact h.1 h.2

#print axioms lst01_implication_as_disjunction
#print axioms lst01_implication_contrapositive
#print axioms lst01_modus_ponens
