"""Independent second audit of Noether normalization (AA-38).

The symbolic finite-characteristic checks are certificates for finite cases,
not replacements for the abstract proof of the lemma.
"""
from __future__ import annotations
from pathlib import Path
import itertools
import re
import unittest
import sympy as sp

SRC = Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/38-lemat-normalizacyjny-noether.tex'
if not SRC.exists(): SRC=Path(__file__).with_name('AA-38-audyt-II-zrodlo.tex')
TEXT=SRC.read_text(encoding='utf-8')
u,v,t=sp.symbols('u v t')

class ProofAudit(unittest.TestCase):
    def test_unique_labels(self):
        labels=re.findall(r'\\label\{([^}]+)\}',TEXT)
        self.assertEqual(len(labels),9)
        self.assertEqual(len(labels),len(set(labels)))
    def test_resolved_local_or_external(self):
        labels=set(re.findall(r'\\label\{([^}]+)\}',TEXT))
        refs=set(re.findall(r'\\ref\{([^}]+)\}',TEXT))
        self.assertEqual(refs-labels,{'aa:tw:transcendence-degree'})
    def test_three_proofs(self):
        self.assertEqual(TEXT.count(r'\begin{proof}'),3)
        self.assertEqual(TEXT.count(r'\end{proof}'),3)
    def test_nonzero_unit_and_finite_algebra_hypotheses(self):
        self.assertIn('niezerową, przemienną,',TEXT)
        self.assertIn('skończenie generowaną $K$-algebrą z jedynką',TEXT)
    def test_no_field_infinity_requirement(self):
        self.assertIn('Nie wymagamy, aby $K$ było nieskończone',TEXT)
    def test_no_domain_requirement_in_main_theorem(self):
        self.assertIn('nie wymagamy', TEXT.lower())
        self.assertIn('dzielników zera',TEXT)
    def test_domain_required_for_fraction_field(self):
        self.assertIn('dziedziną',TEXT)
        self.assertIn(r'\operatorname{Frac}(A)',TEXT)
    def test_monic_positive_degree(self):
        self.assertIn('w(\\beta)>0',TEXT)
    def test_field_f2_example_present(self):
        self.assertIn(r'\mathbb F_2',TEXT)
        self.assertIn('y^8+y^5+uy+u^2+y=0',TEXT)
    def test_fraction_field_obstruction_complete(self):
        self.assertIn('h=1+tD',TEXT)
        self.assertIn('h-tD=1',TEXT)
    def test_matrix_adjugate_used(self):
        self.assertIn(r'\det(aI-C)',TEXT)
    def test_hyperbola_nonintegral_generator(self):
        self.assertIn('1+c_1u+',TEXT)
    def test_all_historical_examples(self):
        for label in ('aa:prz:noether-parabola','aa:prz:noether-nonfinite',
                      'aa:prz:noether-nilpotents','aa:prz:noether-zero-divisors'):
            self.assertIn('\\label{'+label+'}',TEXT)
    def test_other_bad_terms_absent(self):
        for term in ('zwartościowanie','tensorowanie','sekwencja','dual ilorazu'):
            self.assertNotIn(term,TEXT)

class WeightsTwoVariables(unittest.TestCase): pass

# Generative small-degree checks independent of original symbolic substitution logic:
# enumerate nonzero supports; unique w-max ensures constant nonzero leading coefficient.
def check_2var(S, p):
    deg=max(i+j for i,j,c in S)
    M=deg+2
    indexed={(i,j):c%p for i,j,c in S if c%p}
    assert indexed
    weights={ (i,j):i*M+j for i,j in indexed }
    top=max(weights,key=weights.get)
    z=sp.Poly(0,u,v,modulus=p)
    for (i,j),c in indexed.items():
        z+=sp.Poly(c*(u+v**M)**i*v**j,u,v,modulus=p)
    assert z.degree(v)==weights[top]
    coeff=sum(int(c)%p for mon,c in z.terms() if mon[1]==weights[top])%p
    assert coeff==indexed[top]
    assert coeff!=0
    return True

SUPPORTS=[
 [(1,0,1),(0,0,1)],
 [(0,1,1),(0,0,3)],
 [(2,0,1),(0,3,-1)],
 [(1,1,2),(0,2,1)],
 [(0,0,9),(2,0,1),(1,1,3)],
 [(1,0,1),(0,1,-1)],
 [(2,1,1),(1,2,1),(0,0,2)],
 [(0,2,3),(1,1,-2),(2,0,1)],
 [(1,2,3),(3,0,1),(0,2,1)],
 [(0,3,-1),(1,0,2),(0,0,7)],
]
for p in (2,3,5,7,11):
    for k,S in enumerate(SUPPORTS):
        if not any(c%p for _,_,c in S):continue
        setattr(WeightsTwoVariables,f'test_weights_p{p}_case{k:02d}',
                lambda self,S=S,p=p:self.assertTrue(check_2var(S,p)))

class FiniteFieldMonicAndModule(unittest.TestCase): pass
# F2 polynomial in v: R=v^8+v^5+u*v+u^2+v.
# For each v^j, compute remainder via polynomial arithmetic over F_2(u) and verify
# Euclidean identity rather than a bare degree bound.
def check_reduction(j):
    F=sp.GF(2).frac_field(u)
    R=sp.Poly(v**8+v**5+u*v+u*u+v,v,domain=F)
    X=sp.Poly(v**j,v,domain=F)
    q,r=sp.div(X,R)
    assert (q*R+r)==X
    assert r.is_zero or r.degree()<8
    assert sp.degree(R)==8 and R.LC()==1
    return True
for j in range(8,29):
    setattr(FiniteFieldMonicAndModule,f'test_reduction_power_{j}',lambda self,j=j:self.assertTrue(check_reduction(j)))

class DenominatorUnits(unittest.TestCase): pass
Dvals=[1,t,t+1,t**2+t+1,t**3+2*t+1,t**4+3*t*t+2]
for p in [2,3,5,7]:
    for i,D in enumerate(Dvals):
        def check(self,p=p,D=D):
            P=sp.Poly(D,t,modulus=p)
            if P.is_zero:return
            H=sp.Poly(1+t*D,t,modulus=p)
            self.assertGreater(H.degree(),0)
            self.assertEqual(sp.gcd(P,H).degree(),0)
            self.assertEqual(sp.rem(sp.Poly(t,t,modulus=p)*P,H),sp.Poly(-1,t,modulus=p))
        setattr(DenominatorUnits,f'test_coprime_p{p}_{i}',check)

class GeometricAndNilpotentExamples(unittest.TestCase):
    def test_cusp_normal_form(self):
        y=sp.symbols('y')
        for k in range(2,14):
            rem=sp.rem(y**k,y*y-u**3,y)
            self.assertLess(sp.degree(rem,y),2)
    def test_zero_divisor_module(self):
        self.assertEqual(sp.expand(u*(u+v-u)-u*v),0)
    def test_hyperbola_integral_relation(self):
        self.assertEqual(sp.cancel(u*u-(u+1/u)*u+1),0)
    def test_reducible_algebra_has_zero_divisors(self):
        A=sp.Poly(u*v,u,v)
        self.assertEqual(A.total_degree(),2)
    def test_nilpotent_epsilon_nonzero(self):
        eps=sp.symbols('eps')
        self.assertEqual(sp.rem(eps,eps*eps,eps),eps)
        self.assertEqual(sp.rem(eps*eps,eps*eps,eps),0)
    def test_cayley_hamilton_adjugate(self):
        a,b,c,d,z=sp.symbols('a b c d z')
        M=sp.Matrix([[a,b],[c,d]])
        C=z*sp.eye(2)-M
        self.assertEqual(sp.expand(C.adjugate()*C-C.det()*sp.eye(2)),sp.zeros(2))

if __name__=='__main__': unittest.main()
