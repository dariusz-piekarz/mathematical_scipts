import Mathlib

/-!
LST-02: quantifiers over arbitrary types, including empty types.

Theorems below are candidates for the named LaTeX statements:
  thm:negation-quantifiers: two negation laws (classical first direction).
  thm:same-quantifier-order: commute two universal/existential quantifiers.
  thm:swap-mixed: only (exists-forall) implies (forall-exists).
  thm:unique-expansion-xli: unfold exists-unique, including empty domains.

A separate semantic review must establish fidelity to the exact source.
Successful compilation is not a Lean–LaTeX semantic certificate.
-/

universe u v

theorem lst02_not_forall {D : Type u} (P : D → Prop) :
    (¬ ∀ x : D, P x) ↔ ∃ x : D, ¬ P x := by
  classical
  constructor
  · intro h
    by_contra hnone
    apply h
    intro x
    by_contra hx
    exact hnone ⟨x, hx⟩
  · rintro ⟨x, hx⟩ h
    exact hx (h x)

theorem lst02_not_exists {D : Type u} (P : D → Prop) :
    (¬ ∃ x : D, P x) ↔ ∀ x : D, ¬ P x := by
  constructor
  · intro h x hx
    exact h ⟨x, hx⟩
  · intro h
    rintro ⟨x, hx⟩
    exact h x hx

theorem lst02_swap_forall {D : Type u} {E : Type v}
    (P : D → E → Prop) :
    (∀ x : D, ∀ y : E, P x y) ↔
      (∀ y : E, ∀ x : D, P x y) := by
  constructor
  · intro h y x
    exact h x y
  · intro h x y
    exact h y x

theorem lst02_swap_exists {D : Type u} {E : Type v}
    (P : D → E → Prop) :
    (∃ x : D, ∃ y : E, P x y) ↔
      (∃ y : E, ∃ x : D, P x y) := by
  constructor
  · rintro ⟨x, y, h⟩
    exact ⟨y, x, h⟩
  · rintro ⟨y, x, h⟩
    exact ⟨x, y, h⟩

theorem lst02_mixed_quantifier_forward {D : Type u} {E : Type v}
    (P : D → E → Prop) :
    (∃ y : E, ∀ x : D, P x y) →
      (∀ x : D, ∃ y : E, P x y) := by
  rintro ⟨y, hy⟩ x
  exact ⟨y, hy x⟩

/-- The reverse implication is false even when both domains are empty. -/
theorem lst02_mixed_empty_counterexample :
    (∀ x : Empty, ∃ y : Empty, False) ∧
      ¬ (∃ y : Empty, ∀ x : Empty, False) := by
  constructor
  · intro x
    exact x.elim
  · rintro ⟨y, _⟩
    exact y.elim


/-- The source's exact arithmetic counterexample for the non-equivalence
    of mixed quantifiers: for every natural x there is y > x,
    but no fixed natural y is greater than every natural x. -/
theorem lst02_mixed_nat_counterexample :
    (∀ x : ℕ, ∃ y : ℕ, x < y) ∧
      ¬ (∃ y : ℕ, ∀ x : ℕ, x < y) := by
  constructor
  · intro x
    exact ⟨x + 1, Nat.lt_succ_self x⟩
  · rintro ⟨y, hy⟩
    exact (lt_irrefl y) (hy y)

theorem lst02_unique_exists_expansion {D : Type u} (P : D → Prop) :
    (∃! x : D, P x) ↔
      ∃ x : D, P x ∧ ∀ y : D, P y → y = x := by
  rfl

#print axioms lst02_not_forall
#print axioms lst02_not_exists
#print axioms lst02_swap_forall
#print axioms lst02_swap_exists
#print axioms lst02_mixed_quantifier_forward
#print axioms lst02_mixed_empty_counterexample
#print axioms lst02_mixed_nat_counterexample
#print axioms lst02_unique_exists_expansion
