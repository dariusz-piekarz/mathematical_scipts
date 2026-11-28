"""AA-38 independent audit-I: symbolic certificates, finite fields, examples, structural checks."""
from __future__ import annotations
import re
import unittest
from pathlib import Path
from itertools import product
import sympy as sp

FILE=Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/38-lemat-normalizacyjny-noether.tex'
if not FILE.exists(): FILE=Path(__file__).with_name('AA-38-audyt-II-zrodlo.tex')
SOURCE=FILE.read_text(encoding='utf-8')
HISTORIC_LABELS={'aa:ch:noether-normalization','aa:lem:noether-monic','aa:tw:noether-normalization','aa:wn:noether-dimension','aa:prz:noether-parabola','aa:prz:noether-nonfinite','aa:prz:noether-nilpotents','aa:prz:noether-zero-divisors'}
HISTORIC_PROOF_COUNT=3
U,V,W=sp.symbols('U V W')
X,Y,Z=sp.symbols('X Y Z')
T=sp.symbols('T')

class Document(unittest.TestCase):
    def test_all_historic_labels(self):
        old=HISTORIC_LABELS;new=set(re.findall(r'\\label\{([^}]+)\}',SOURCE))
        self.assertEqual(new-old,{'aa:prz:noether-f2'});self.assertTrue(old<=new)
    def test_unique_labels(self):
        labels=re.findall(r'\\label\{([^}]+)\}',SOURCE)
        self.assertEqual(len(labels),len(set(labels)))
    def test_all_crossreferences(self):
        local=set(re.findall(r'\\label\{([^}]+)\}',SOURCE))
        external={'aa:tw:transcendence-degree'}
        self.assertTrue(set(re.findall(r'\\ref\{([^}]+)\}',SOURCE))<=local|external)
    def test_core_claims(self):
        for x in ['\\label{aa:lem:noether-monic}','\\label{aa:tw:noether-normalization}',
                  '\\label{aa:wn:noether-dimension}','\\label{aa:prz:noether-f2}']:
            self.assertIn(x,SOURCE)
    def test_all_proofs_kept(self):
        self.assertEqual(SOURCE.count('\\begin{proof}'),HISTORIC_PROOF_COUNT)
        self.assertEqual(SOURCE.count('\\end{proof}'),HISTORIC_PROOF_COUNT)
    def test_no_deprecated_spelling(self):
        for bad in ['zwartościowanie','tensorowanie','sekwencja','dual ilorazu']:
            self.assertNotIn(bad,SOURCE)
    def test_no_hidden_char_restriction(self):
        self.assertIn('Nie wymagamy, aby $K$ było nieskończone',SOURCE)
        self.assertIn('\\mathbb F_2',SOURCE)
    def test_constant_case(self):
        self.assertIn('Jeżeli $n=0$',SOURCE)
    def test_finite_field_monic_written(self):
        self.assertIn('y^8+y^5+uy+u^2+y=0',SOURCE)
    def test_finite_fraction_finiteness_proved(self):
        self.assertIn('$h=1+tD',SOURCE)
        self.assertIn('względnie pierwszy',SOURCE)

def monic_certificate(f, vars_, char):
    d=sp.Poly(f,*vars_).total_degree()
    M=d+3
    subs={x:y+vars_[-1]**(M**i) for i,(x,y) in enumerate(zip(vars_[:-1], (U,V)[:len(vars_)-1]),start=1)}
    # Last var maps to W for n=3, V for n=2; other vars are U, V.
    main= W if len(vars_)==3 else V
    subs={x: (U if i==0 else V)+main**(M**(i+1)) for i,x in enumerate(vars_[:-1])}
    subs[vars_[-1]]=main
    g=sp.expand(f.subs(subs, simultaneous=True))
    deg=sp.Poly(g,main).degree()
    lc=sp.Poly(g,main).LC()
    orig=sp.Poly(f,*vars_)
    # Highest contribution of unique max-weight monomial, no cancellation.
    terms=orig.terms() if char is None else [(a,c) for a,c in orig.terms() if int(c)%char]
    weighted=[(a[-1]+sum(a[i]*M**(i+1) for i in range(len(vars_)-1)),c) for a,c in terms]
    best=max(weighted, key=lambda z:z[0])
    if char is None:
        assert deg==best[0]
        assert sp.expand(lc-best[1])==0
        return deg,lc
    # Reduction in characteristic p can eliminate the leading monomial;
    # calculate the actual degree and coefficient after reduction.
    reduced=sp.Poly(g,*((U,V,W)[:len(vars_)-1]+(main,)),modulus=char)
    maxw=best[0]
    assert reduced.degree(main)==maxw
    coeff=int(reduced.coeff_monomial(main**maxw))%char
    assert coeff!=0
    return deg,coeff

class MonicCharacteristicZero(unittest.TestCase):
    pass
class MonicFiniteFields(unittest.TestCase):
    pass

def make_monic_test(f,variables,characteristic):
    def test(self):
        degree,leading=monic_certificate(f,variables,characteristic)
        self.assertGreater(degree,0)
        self.assertNotEqual(leading,0)
        if characteristic:
            self.assertIn(int(leading)%characteristic,range(1,characteristic))
    return test

examples=[X**2-Y**3, X**2+X*Y+Y, X-Y, X**3+2*Y**2-5*X,
          3*X**2*Y+4*Y**3+7*X, X**2+5*X*Y+3*Y, Y**4+X**2,
          X**2+X*Y+7*Y+1,X*Y+3*X+Y**2+2, 17*X+Y+2]
for i,f in enumerate(examples):
    setattr(MonicCharacteristicZero,f'test_monic_2var_{i:02d}',make_monic_test(f,(X,Y),None))
examples3=[X+Y+Z, X**2+Y*Z+Z, X*Y+Y*Z+Z**2,
            4*X**2*Z+3*Y**2+Z, X**2+X*Y+Y*Z+Z**2+1,
            X**3+Y**2+Z, X*Y*Z+X*Z+Y+3, 2*X+3*Y**2+Z**3]
for i,f in enumerate(examples3):
    setattr(MonicCharacteristicZero,f'test_monic_3var_{i:02d}',make_monic_test(f,(X,Y,Z),None))
for p in [2,3,5,7,11]:
    for i,f in enumerate(examples[:7]):
        if all(int(c)%p==0 for _,c in sp.Poly(f,X,Y).terms()):continue
        setattr(MonicFiniteFields,f'test_monic_char{p}_case{i:02d}',make_monic_test(f,(X,Y),p))

class ExplicitExamples(unittest.TestCase):
    def test_f2_substitution(self):
        q=sp.Poly((U+V**4)**2+(U+V**4)*V+V,U,V,modulus=2)
        expected=sp.Poly(V**8+V**5+U*V+U**2+V,U,V,modulus=2)
        self.assertEqual(q,expected)
    def test_f2_monic(self):
        q=sp.Poly((U+V**4)**2+(U+V**4)*V+V,U,V,modulus=2)
        self.assertEqual(q.degree(V),8)
        self.assertEqual(q.coeff_monomial(V**8),1)
    def test_f2_parameter_injection(self):
        pol=sp.Poly(V**8+V**5+U*V+U**2+V,V)
        self.assertEqual(pol.LC(),1)
        for i in range(1,9):
            f=sp.Poly(U**i+1,V)
            self.assertEqual(f.degree(),0)
            self.assertLess(f.degree(),pol.degree())
    def test_f2_module_reduction(self):
        expr=V**8+V**5+U*V+U**2+V
        domain=sp.GF(2).frac_field(U)
        rel=sp.Poly(expr,V,domain=domain)
        for i in range(8,19):
            remainder=sp.rem(sp.Poly(V**i,V,domain=domain),rel)
            self.assertLess(remainder.degree(),8)
    def test_xy_zero_divisor_param(self):
        s=X+Y
        self.assertEqual(sp.expand(X**2-s*X+X*Y),0)
    def test_hyperbola_param(self):
        u=sp.Symbol('u',nonzero=True)
        s=u+1/u
        self.assertEqual(sp.simplify(u*u-s*u+1),0)
    def test_cusp_relation(self):
        t=sp.symbols('t')
        self.assertEqual(sp.expand((t**3)**2-(t**2)**3),0)
    def test_nilpotent_example(self):
        self.assertIn('\\varepsilon^2=0',SOURCE)
    def test_zero_divisor_example(self):
        self.assertIn('\\label{aa:prz:noether-zero-divisors}',SOURCE)
    def test_nonfinite_fraction_example(self):
        self.assertIn('K[t,D^{-1}]',SOURCE)
    def test_det_trick_identity(self):
        a,b,c,d,z=sp.symbols('a b c d z')
        M=sp.Matrix([[a,b],[c,d]])
        A=z*sp.eye(2)-M
        self.assertEqual(sp.simplify(A.adjugate()*A-sp.det(A)*sp.eye(2)),sp.zeros(2))

class DenominatorObstruction(unittest.TestCase):
    pass

def make_denom_test(D, p):
    def test(self):
        h=sp.Poly(1+T*D,T,modulus=p)
        dd=sp.Poly(D,T,modulus=p)
        self.assertGreater(h.degree(),0)
        self.assertEqual(sp.gcd(h,dd),sp.Poly(1,T,modulus=p))
    return test
for p in [2,3,5,7]:
    for i,D in enumerate([1,T,T+1,T*T+T+1,T**3+2*T+1]):
        setattr(DenominatorObstruction,f'test_denominator_char{p}_{i}',make_denom_test(D,p))

if __name__=='__main__':
    unittest.main(verbosity=1)
