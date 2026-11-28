import Mathlib

/-!
Formalizacyjny szkic dla LST-01, thm:de-morgan-logic.
Źródłowy skrypt formułuje prawa dla dowolnych FORMUŁ i ich wartościowań.
Poniższe prawa dla Prop są poprawnymi odpowiednikami po ewaluacji,
ale zgodność pełnego twierdzenia o składni formuł wymaga osobnego audytu.
BRAK CERTYFIKATU semantycznego; BRAK wykonania Lean w tej iteracji.
-/

theorem lst01_de_morgan_and (p q : Prop) :
    ¬ (p ∧ q) ↔ (¬ p ∨ ¬ q) := by
  classical
  tauto

theorem lst01_de_morgan_or (p q : Prop) :
    ¬ (p ∨ q) ↔ (¬ p ∧ ¬ q) := by
  tauto

#print axioms lst01_de_morgan_and
#print axioms lst01_de_morgan_or
