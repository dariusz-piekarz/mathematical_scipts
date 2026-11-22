import Mathlib
import LST01_SyntaxValuations

/-!
LST-01, thm:logic-distributivity. Three clauses for arbitrary propositional
formulas under every Boolean valuation. No Prop-level replacement.
-/

theorem lst01_syntax_double_negation (p : LST01.Formula) :
    LST01.equivalent (.neg (.neg p)) p := by
  intro ν
  cases hp : LST01.eval ν p <;> simp [LST01.eval, hp]

theorem lst01_syntax_and_over_or (p q r : LST01.Formula) :
    LST01.equivalent (.conj p (.disj q r))
      (.disj (.conj p q) (.conj p r)) := by
  intro ν
  cases hp : LST01.eval ν p <;>
    cases hq : LST01.eval ν q <;>
    cases hr : LST01.eval ν r <;>
    simp [LST01.eval, hp, hq, hr]

theorem lst01_syntax_or_over_and (p q r : LST01.Formula) :
    LST01.equivalent (.disj p (.conj q r))
      (.conj (.disj p q) (.disj p r)) := by
  intro ν
  cases hp : LST01.eval ν p <;>
    cases hq : LST01.eval ν q <;>
    cases hr : LST01.eval ν r <;>
    simp [LST01.eval, hp, hq, hr]

#print axioms lst01_syntax_double_negation
#print axioms lst01_syntax_and_over_or
#print axioms lst01_syntax_or_over_and
