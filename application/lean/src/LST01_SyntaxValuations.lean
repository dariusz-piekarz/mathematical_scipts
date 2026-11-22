import Mathlib

/-!
LST-01: propositional syntax and valuations, rather than only Prop-level laws.

Correspondence:
  def:propositional-grammar-xli: inductive Formula with all five constructors
    (atomic letter, negation, conjunction, disjunction, implication, equivalence).
  thm:de-morgan-logic: both De Morgan laws for arbitrary Formula values.
  thm:implication-laws: disjunction, contraposition, modus ponens.
  thm:negated-implication-xli: negation of material implication.

Equivalence means equality of evaluations under EVERY valuation. A single
valuation is a function Nat -> Bool and therefore repeated occurrences of
one letter always have the same value. The displayed #print axioms commands
form an independent kernel-level check in CI.

This is a faithful candidate for the selected propositional fragment, but
the human review of the LaTeX-to-Lean correspondence is separate.
-/

namespace LST01

inductive Formula : Type where
  | atom : Nat → Formula
  | neg : Formula → Formula
  | conj : Formula → Formula → Formula
  | disj : Formula → Formula → Formula
  | imp : Formula → Formula → Formula
  | iff : Formula → Formula → Formula
  deriving Repr, DecidableEq

abbrev Valuation := Nat → Bool

def eval (ν : Valuation) : Formula → Bool
  | .atom n => ν n
  | .neg p => !(eval ν p)
  | .conj p q => (eval ν p) && (eval ν q)
  | .disj p q => (eval ν p) || (eval ν q)
  | .imp p q => (!(eval ν p)) || (eval ν q)
  | .iff p q => decide (eval ν p = eval ν q)

def equivalent (p q : Formula) : Prop :=
  ∀ ν : Valuation, eval ν p = eval ν q

def tautology (p : Formula) : Prop :=
  ∀ ν : Valuation, eval ν p = true

end LST01

theorem lst01_syntax_de_morgan_and (p q : LST01.Formula) :
    LST01.equivalent (.neg (.conj p q)) (.disj (.neg p) (.neg q)) := by
  intro ν
  cases hp : LST01.eval ν p <;> cases hq : LST01.eval ν q <;>
    simp [LST01.eval, hp, hq]

theorem lst01_syntax_de_morgan_or (p q : LST01.Formula) :
    LST01.equivalent (.neg (.disj p q)) (.conj (.neg p) (.neg q)) := by
  intro ν
  cases hp : LST01.eval ν p <;> cases hq : LST01.eval ν q <;>
    simp [LST01.eval, hp, hq]

theorem lst01_syntax_implication_as_disjunction (p q : LST01.Formula) :
    LST01.equivalent (.imp p q) (.disj (.neg p) q) := by
  intro ν
  rfl

theorem lst01_syntax_implication_contrapositive (p q : LST01.Formula) :
    LST01.equivalent (.imp p q) (.imp (.neg q) (.neg p)) := by
  intro ν
  cases hp : LST01.eval ν p <;> cases hq : LST01.eval ν q <;>
    simp [LST01.eval, hp, hq]

theorem lst01_syntax_modus_ponens (p q : LST01.Formula) :
    LST01.tautology (.imp (.conj (.imp p q) p) q) := by
  intro ν
  cases hp : LST01.eval ν p <;> cases hq : LST01.eval ν q <;>
    simp [LST01.eval, hp, hq]

theorem lst01_syntax_negated_implication (p q : LST01.Formula) :
    LST01.equivalent (.neg (.imp p q)) (.conj p (.neg q)) := by
  intro ν
  cases hp : LST01.eval ν p <;> cases hq : LST01.eval ν q <;>
    simp [LST01.eval, hp, hq]

/-- Truth-functional iff is equivalent to the conjunction of both implications. -/
theorem lst01_syntax_iff_as_two_implications (p q : LST01.Formula) :
    LST01.equivalent (.iff p q) (.conj (.imp p q) (.imp q p)) := by
  intro ν
  cases hp : LST01.eval ν p <;> cases hq : LST01.eval ν q <;>
    simp [LST01.eval, hp, hq]

/-- One letter has one value even if it occurs more than once in a formula. -/
theorem lst01_syntax_repeated_atom (n : Nat) :
    LST01.equivalent (.conj (.atom n) (.atom n)) (.atom n) := by
  intro ν
  cases hn : ν n <;> simp [LST01.eval, hn]

#print axioms lst01_syntax_de_morgan_and
#print axioms lst01_syntax_de_morgan_or
#print axioms lst01_syntax_implication_as_disjunction
#print axioms lst01_syntax_implication_contrapositive
#print axioms lst01_syntax_modus_ponens
#print axioms lst01_syntax_negated_implication
#print axioms lst01_syntax_iff_as_two_implications
#print axioms lst01_syntax_repeated_atom
