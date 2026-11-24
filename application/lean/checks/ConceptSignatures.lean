/-! Trusted static CI fixture, appended to LST01_SyntaxValuations.lean. -/
section AtlasConceptSignatureChecks

-- concept: logic.prop.iff
#check Iff
example : Prop → Prop → Prop := Iff

-- concept: logic.prop.and
#check And
example : Prop → Prop → Prop := And

-- concept: logic.prop.or
#check Or
example : Prop → Prop → Prop := Or

-- concept: logic.syntax.formula
#check LST01.Formula
example : Type := LST01.Formula

-- concept: logic.syntax.equivalent
#check LST01.equivalent
example : LST01.Formula → LST01.Formula → Prop := LST01.equivalent

-- concept: logic.syntax.tautology
#check LST01.tautology
example : LST01.Formula → Prop := LST01.tautology

-- concept: set.type
#check Set
example (α : Type) : Type := Set α

-- concept: set.subset
#check Set.Subset
example (α : Type) (s t : Set α) : Prop := Set.Subset s t
example (α : Type) (s t : Set α) :
    Set.Subset s t ↔ (s ⊆ t) := Iff.rfl

-- concept: linear_algebra.linear_map
#check LinearMap
example (R V W : Type) [Field R] [AddCommGroup V] [AddCommGroup W]
    [Module R V] [Module R W] : Type :=
  LinearMap (RingHom.id R) V W

-- concept: linear_algebra.submodule
#check Submodule
example (R V : Type) [Field R] [AddCommGroup V] [Module R V] : Type :=
  Submodule R V

-- concept: linear_algebra.independent
#check LinearIndependent
example (R V ι : Type) [Field R] [AddCommGroup V] [Module R V]
    (v : ι → V) : Prop := LinearIndependent R v

end AtlasConceptSignatureChecks
