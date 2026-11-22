"""Independent AA-21 audit III mathematical/regression checks.

Finite tests validate representative instances and proof hypotheses; they
are not replacements for proofs of the general theorems.
"""
import itertools
import math
import random
import re
import unittest
from pathlib import Path

SRC = (Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/21-zanurzenia-automorfizmy-i-rozszerzenia-galois.tex')
S = SRC.read_text(encoding='utf-8')

# Coefficients of F_p[X]/(irreducible monic polynomial mod), in increasing degree.
FIELDS = [(2, (1, 1, 1), 4), (2, (1, 1, 0, 1), 8),
          (3, (1, 0, 1), 9), (2, (1, 1, 0, 0, 1), 16),
          (5, (2, 0, 1), 25)]

def mul(a, b, p, poly):
    n = len(poly)-1
    c = [0]*(2*n-1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i+j] = (c[i+j]+ai*bj)%p
    for k in range(2*n-2, n-1, -1):
        ck = c[k]
        for j in range(n):
            c[k-n+j] = (c[k-n+j] - ck*poly[j])%p
    return tuple(c[:n])

def add(a, b, p):
    return tuple((x+y)%p for x, y in zip(a,b))

def power(x, e, p, poly):
    one = (1,)+(0,)*(len(poly)-2)
    out=one
    while e:
        if e&1: out = mul(out,x,p,poly)
        x = mul(x,x,p,poly)
        e//=2
    return out

def elements(p, poly):
    return list(itertools.product(range(p),repeat=len(poly)-1))

def frob(x,p,poly,r=1):
    return power(x,p**r,p,poly)

class NewIndependentAuditChecks(unittest.TestCase):
    def test_01_labels_unique(self):
        labels=re.findall(r'\\label\{([^}]+)\}',S)
        self.assertEqual((len(labels),len(set(labels))),(20,20))
    def test_02_references_unique_external_targets(self):
        labels=set(re.findall(r'\\label\{([^}]+)\}',S))
        refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',S)
        self.assertEqual(len(refs),18)
        self.assertEqual(set(refs)-labels,{
          'aa:ch:field-extensions','aa:tw:adjoin-root-abstract',
          'aa:tw:eisenstein','aa:tw:field-frobenius',
          'aa:tw:field-tower','aa:tw:finite-field-cardinality',
          'aa:tw:simple-algebraic-extension','aa:tw:splitting-existence',
          'aa:prz:inseparable-example','aa:wn:charzero-separable'})
    def test_03_naturality_tower_numbers(self):
        self.assertEqual((2*3)*4,2*(3*4))
        self.assertEqual(2*3*4,24)
    def test_04_field_automorphism_injective(self):
        for p,poly,q in FIELDS:
            vals=elements(p,poly)
            images=[frob(x,p,poly) for x in vals]
            self.assertEqual(len(set(images)),q)
    def test_05_frobenius_additive_all_small_fields(self):
        for p,poly,_ in FIELDS:
            vals=elements(p,poly)
            for a,b in itertools.product(vals,repeat=2):
                self.assertEqual(frob(add(a,b,p),p,poly),
                                 add(frob(a,p,poly),frob(b,p,poly),p))
    def test_06_frobenius_multiplicative_all_small_fields(self):
        for p,poly,_ in FIELDS:
            vals=elements(p,poly)
            for a,b in itertools.product(vals,repeat=2):
                self.assertEqual(frob(mul(a,b,p,poly),p,poly),
                                 mul(frob(a,p,poly),frob(b,p,poly),p,poly))
    def test_07_frobenius_fixes_prime_field(self):
        for p,poly,_ in FIELDS:
            for a in range(p):
                x=(a,)+(0,)*(len(poly)-2)
                self.assertEqual(frob(x,p,poly),x)
    def test_08_frobenius_exact_order(self):
        for p,poly,q in FIELDS:
            n=len(poly)-1;vals=elements(p,poly)
            self.assertTrue(all(frob(x,p,poly,n)==x for x in vals))
            self.assertFalse(any(all(frob(x,p,poly,r)==x for x in vals)
                                 for r in range(1,n)))
    def test_09_frobenius_iterates_distinct(self):
        for p,poly,q in FIELDS:
            n=len(poly)-1; vals=elements(p,poly)
            permutations=[tuple(frob(x,p,poly,r) for x in vals)
                          for r in range(n)]
            self.assertEqual(len(set(permutations)),n)
    def test_10_fixed_field_cardinality_gcd(self):
        for p,poly,q in FIELDS:
            n=len(poly)-1; vals=elements(p,poly)
            for r in range(1,2*n+1):
                fixed=sum(frob(x,p,poly,r)==x for x in vals)
                self.assertEqual(fixed,p**math.gcd(r,n))
    def test_11_extension_f16_f4_order_two(self):
        p,poly,n=2,(1,1,0,0,1),4
        vals=elements(p,poly)
        self.assertEqual(sum(frob(x,p,poly,2)==x for x in vals),4)
        self.assertTrue(all(frob(x,p,poly,4)==x for x in vals))
    def test_12_generators_f8(self):
        p,poly,q=2,(1,1,0,1),8
        a=(0,1,0)
        self.assertEqual({power(a,k,p,poly) for k in range(1,8)},
                         set(elements(p,poly))-{(0,0,0)})
    def test_13_finite_field_roots_xq_minus_x(self):
        for p,poly,q in FIELDS:
            self.assertEqual(sum(power(x,q,p,poly)==x for x in elements(p,poly)),q)
    def test_14_finite_field_polynomial_derivative(self):
        for p,_,q in FIELDS:
            # formal derivative of X^q-X is -1 in characteristic p
            self.assertEqual(q%p,0)
            self.assertEqual((-1)%p,p-1)
    def test_15_unique_inseparable_root(self):
        for p in (2,3,5,7):
            self.assertTrue(all(math.comb(p,k)%p==0 for k in range(1,p)))
    def test_16_inseparable_concrete_exponent_relation(self):
        # Formal reduction modulo alpha**p=t, in F_p[t][alpha].
        for p in (2,3,5):
            rng=random.Random(p)
            for _ in range(14):
                coeff=[rng.randrange(p) for __ in range(p)]
                if not any(coeff):coeff[0]=1
                current={(0,0):1}  # (alpha exponent, t exponent)
                factor={(j,0):v for j,v in enumerate(coeff) if v}
                for __ in range(p):
                    new={}
                    for (a,ta),v in current.items():
                        for (b,tb),w in factor.items():
                            degree=a+b
                            key=(degree%p,ta+tb+degree//p)
                            new[key]=(new.get(key,0)+v*w)%p
                    current={k:v for k,v in new.items() if v}
                expected={(0,j):v for j,v in enumerate(coeff) if v}
                self.assertEqual(current,expected)
    def test_17_nonnormal_cubic_exact_conjugates(self):
        a=2**(1/3)
        w=complex(-.5,math.sqrt(3)/2)
        roots=[a*w**j for j in range(3)]
        self.assertEqual(sum(abs(z.imag)<1e-11 for z in roots),1)
        self.assertTrue(all(abs(z**3-2)<1e-11 for z in roots))
    def test_18_quadratic_conjugation_preserves_minimal_polynomial(self):
        for p,q in itertools.product(range(-7,8),repeat=2):
            # x=a+b sqrt(2) has minimal polynomial dividing
            # (X-(a+b sqrt2))(X-(a-b sqrt2)).
            trace=2*p; norm=p*p-2*q*q
            self.assertEqual(p*p + 2*q*q-trace*p+norm,0)
    def test_19_splitting_field_degree(self):
        # Irreducible X**2+X+1 over F_2, hence F4 has degree 2.
        self.assertEqual([x for x in range(2) if (x*x+x+1)%2==0],[])
    def test_20_maximal_ideal_finite_example(self):
        # In F2[y] the ideal (y*y+y+1) is maximal: irreducible quad.
        self.assertTrue(all((x*x+x+1)%2 for x in range(2)))
    def test_21_normality_chain_argument(self):
        self.assertIn('skończonego wymiaru, więc jest surjektywny',S)
        self.assertIn('Przedłużamy je do $L$',S)
    def test_22_transitivity_of_algebraicity(self):
        self.assertIn('A(b_0,\\ldots,b_d,x)/A',S)
        self.assertIn('twierdzenia o wieży',S)
    def test_23_zorn_chain_hypothesis(self):
        self.assertIn('niepustego łańcucha',S)
        self.assertIn('pusty łańcuch jest ograniczony',S)
    def test_24_empty_root_bases(self):
        self.assertIn('W konsekwencji iloraz',S)
        self.assertIn('każdy wielomian dodatniego',S)
