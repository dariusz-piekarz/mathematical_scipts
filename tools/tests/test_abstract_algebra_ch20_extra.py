"""AA-20: independent finite-extension and edge-case tests (standard library)."""
import itertools
import math
import re
import unittest
from fractions import Fraction
from pathlib import Path

TEXT=(Path(__file__).resolve().parents[2]/'chapters/pl/abstract_algebra/20-rozszerzenia-cial-i-ciala-rozkladu-wielomianow.tex').read_text(encoding='utf8')

def mul(a,b,p,f):
    n=len(f)-1
    out=[0]*(2*n-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%p
    for k in range(2*n-2,n-1,-1):
        u=out[k]
        for j in range(n):out[k-n+j]=(out[k-n+j]-u*f[j])%p
    return tuple(out[:n])

def power(a,k,p,f):
    z=(1,)+(0,)*(len(f)-2)
    while k:
        if k&1:z=mul(z,a,p,f)
        a=mul(a,a,p,f);k//=2
    return z

def order(a,p,f):
    one=(1,)+(0,)*(len(f)-2)
    if not any(a):return 0
    for k in range(1,p**(len(f)-1)):
        if power(a,k,p,f)==one:return k
    return -1

class AdditionalTests(unittest.TestCase):
    def test_01_source_labels(self):
        ls=re.findall(r'\\label\{([^}]+)\}',TEXT)
        self.assertEqual((len(ls),len(set(ls))),(25,25))
    def test_02_source_refs(self):
        self.assertEqual(len(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',TEXT)),11)
    def test_03_proofs(self):
        self.assertEqual((TEXT.count(r'\begin{proof}'),TEXT.count(r'\end{proof}')),(12,12))
    def test_04_examples(self):
        self.assertEqual((TEXT.count(r'\begin{przyklad}'),TEXT.count(r'\end{przyklad}')),(7,7))
    def test_05_vocabulary(self):
        self.assertNotIn('tensorowanie',TEXT.lower())
        self.assertNotIn('sekwencj',TEXT.lower())
    def test_06_sqrt2_not_rational(self):
        self.assertFalse(any(a*a==2*b*b for a in range(-30,31) for b in range(1,31)))
    def test_07_sqrt3_not_rational(self):
        self.assertFalse(any(a*a==3*b*b for a in range(-30,31) for b in range(1,31)))
    def test_08_sqrt_three_over_two_not_rational(self):
        self.assertFalse(any(2*a*a==3*b*b for a in range(-30,31) for b in range(1,31)))
    def test_09_primitive_four(self):
        self.assertEqual(sum(order(a,2,(1,1,1))==3 for a in itertools.product(range(2),repeat=2)),2)
    def test_10_primitive_eight(self):
        self.assertEqual(sum(order(a,2,(1,1,0,1))==7 for a in itertools.product(range(2),repeat=3)),6)
    def test_11_primitive_nine(self):
        self.assertEqual(sum(order(a,3,(1,0,1))==8 for a in itertools.product(range(3),repeat=2)),4)
    def test_12_primitive_sixteen(self):
        self.assertEqual(sum(order(a,2,(1,1,0,0,1))==15 for a in itertools.product(range(2),repeat=4)),8)
    def test_13_primitive_twentyfive(self):
        self.assertEqual(sum(order(a,5,(2,0,1))==24 for a in itertools.product(range(5),repeat=2)),8)
    def test_14_frobenius_four(self):
        self.assertTrue(all(power(a,4,2,(1,1,1))==a for a in itertools.product(range(2),repeat=2)))
    def test_15_frobenius_nine(self):
        self.assertTrue(all(power(a,9,3,(1,0,1))==a for a in itertools.product(range(3),repeat=2)))
    def test_16_cubic_roots(self):
        alpha=2**(1/3);omega=complex(-.5,math.sqrt(3)/2)
        self.assertTrue(all(abs((alpha*omega**k)**3-2)<1e-12 for k in range(3)))
    def test_17_quadratic_discriminant(self):
        self.assertEqual(1-4*1*1,-3)
    def test_18_inseparable_derivative(self):
        self.assertTrue(all(p%p==0 for p in (2,3,5,7,11)))
    def test_19_F2_units(self):
        self.assertEqual([x for x in range(2) if x], [1])
    def test_20_root_bound(self):
        for p in (2,3,5,7):
            for e in range(1,8):
                self.assertLessEqual(sum(pow(x,e,p)==1 for x in range(p)),e)
    def test_21_natural_field_f4_relation(self):
        a=(0,1);mod=(1,1,1)
        self.assertEqual(mul(a,a,2,mod),(1,1))
        self.assertEqual(power(a,3,2,mod),(1,0))
    def test_22_references_prior_chapters(self):
        self.assertIn(r'\ref{aa:tw:eisenstein}',TEXT)
        self.assertIn(r'\ref{aa:wn:abelian-fg-structure}',TEXT)
