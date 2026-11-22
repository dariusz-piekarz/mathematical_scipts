"""Independent second-pass verification for Abstract Algebra AA-29.

Intentionally different from baseline AA-29 arithmetic implemented over F4/F9:
uses SymPy polynomial arithmetic over prime fields, direct factorization,
Frobenius divisibility and enumerations plus source invariants.
"""
import itertools
import re
import unittest
from pathlib import Path
from sympy import Poly, symbols, mobius, divisors, gcd

X = symbols('X')
ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'chapters/pl/abstract_algebra/29-struktura-cial-skonczonych-i-wielomiany-nierozkladalne.tex'
TEXT = SRC.read_text(encoding='utf-8')


def irreducible_count_by_sympy(q, n):
    assert q in (2, 3, 5, 7)
    count = 0
    for c in itertools.product(range(q), repeat=n):
        p = Poly(X**n + sum(c[k] * X**k for k in range(n)), X, modulus=q)
        if p.is_irreducible:
            count += 1
    return count


def mobius_count(q, n):
    numerator = sum(int(mobius(d)) * q ** (n//d) for d in divisors(n))
    assert numerator % n == 0
    return numerator // n


def polynomial_pow_mod(base, exponent, divisor, characteristic):
    """Compute base^exponent mod divisor without constructing huge powers."""
    acc=Poly(1,X,modulus=characteristic)
    while exponent:
        if exponent & 1:
            acc=(acc*base).rem(divisor)
        base=(base*base).rem(divisor)
        exponent >>= 1
    return acc


def frobenius_fixed_mod(f,p,n):
    x=Poly(X,X,modulus=p)
    for _ in range(n):
        x=polynomial_pow_mod(x,p,f,p)
    return (x-Poly(X,X,modulus=p)).rem(f).is_zero


class Structure(unittest.TestCase):
    def test_01_labeled_results_unique(self):
        labels = re.findall(r'\\label\{([^}]+)\}', TEXT)
        self.assertEqual(len(labels), 11)
        self.assertEqual(len(labels), len(set(labels)))

    def test_02_all_references_resolve_locally_except_aa21(self):
        labels = set(re.findall(r'\\label\{([^}]+)\}', TEXT))
        refs = set(re.findall(r'\\ref\{([^}]+)\}', TEXT))
        self.assertEqual(refs-labels, {'aa:ch:embeddings-normal-separable'})

    def test_03_environment_balance(self):
        for env in ('twierdzenie','wniosek','definicja','lemat','przyklad','uwaga','proof'):
            with self.subTest(env=env):
                self.assertEqual(TEXT.count(r'\begin{' + env + '}'),
                                 TEXT.count(r'\end{' + env + '}'))

    def test_04_math_delimiters(self):
        self.assertEqual(TEXT.count(r'\['), TEXT.count(r'\]'))
        self.assertEqual(TEXT.count(r'\('), TEXT.count(r'\)'))

    def test_05_theorem_hypotheses(self):
        self.assertIn('Niech $p$ będzie liczbą pierwszą, $m,n\\ge1$ liczbami', TEXT)
        self.assertIn('$q=p^m$, a $E_q$ ciałem o $q$ elementach', TEXT)
        self.assertIn('Niech $N_q(n)$ oznacza liczbę', TEXT)

    def test_06_frobenius_fixed_field_justification(self):
        self.assertIn('$(x^q)^{q^s}=x^q$', TEXT)
        self.assertIn('jest również surjektywne.', TEXT)
        self.assertIn('$E_q(\\alpha)$ jest podciałem $E_{q^r}$', TEXT)

    def test_07_bound_for_proper_subfields(self):
        self.assertIn(r'\lfloor n/2\rfloor', TEXT)
        self.assertIn('q(q^k-1)/(q-1)<q^{k+1}', TEXT)

    def test_08_no_forbidden_spellings(self):
        self.assertNotIn('injektyw', TEXT)
        self.assertNotIn('sekwencyjn', TEXT)
        self.assertNotIn('tensorowanie', TEXT)


class ExternalArithmetic(unittest.TestCase):
    def test_09_direct_irreducible_count_F2(self):
        for n in range(1, 8):
            with self.subTest(n=n):
                self.assertEqual(irreducible_count_by_sympy(2,n),mobius_count(2,n))

    def test_10_direct_irreducible_count_F3(self):
        for n in range(1, 6):
            with self.subTest(n=n):
                self.assertEqual(irreducible_count_by_sympy(3,n),mobius_count(3,n))

    def test_11_direct_irreducible_count_F5(self):
        for n in range(1, 5):
            with self.subTest(n=n):
                self.assertEqual(irreducible_count_by_sympy(5,n),mobius_count(5,n))

    def test_12_direct_irreducible_count_F7(self):
        for n in range(1, 4):
            with self.subTest(n=n):
                self.assertEqual(irreducible_count_by_sympy(7,n),mobius_count(7,n))

    def test_13_factorization_F2(self):
        for n in range(1, 7):
            poly = Poly(X**(2**n)-X, X, modulus=2)
            unit, factors = poly.factor_list()
            self.assertEqual(unit,1)
            self.assertEqual(sum(g.degree()*e for g,e in factors),2**n)
            self.assertTrue(all(e==1 and n % g.degree()==0 for g,e in factors))

    def test_14_factorization_F3(self):
        for n in range(1, 5):
            poly=Poly(X**(3**n)-X, X, modulus=3)
            _, factors=poly.factor_list()
            self.assertEqual(sum(g.degree()*e for g,e in factors),3**n)
            self.assertTrue(all(e==1 and n % g.degree()==0 for g,e in factors))

    def test_15_factorization_F5(self):
        for n in range(1, 4):
            poly=Poly(X**(5**n)-X, X, modulus=5)
            _, factors=poly.factor_list()
            self.assertEqual(sum(g.degree()*e for g,e in factors),5**n)
            self.assertTrue(all(e==1 and n % g.degree()==0 for g,e in factors))

    def test_16_squarefree_frobenius_F2(self):
        for n in range(1,9):
            poly=Poly(X**(2**n)-X,X,modulus=2)
            self.assertEqual(gcd(poly,poly.diff()).degree(),0)

    def test_17_squarefree_frobenius_F3(self):
        for n in range(1,6):
            poly=Poly(X**(3**n)-X,X,modulus=3)
            self.assertEqual(gcd(poly,poly.diff()).degree(),0)

    def test_18_frobenius_period_degree3_F2(self):
        f=Poly(X**3+X+1,X,modulus=2)
        self.assertTrue(f.is_irreducible)
        for n in range(1,11):
            self.assertEqual(frobenius_fixed_mod(f,2,n),n%3==0)

    def test_19_frobenius_period_degree2_F3(self):
        f=Poly(X**2+1,X,modulus=3)
        self.assertTrue(f.is_irreducible)
        for n in range(1,10):
            self.assertEqual(frobenius_fixed_mod(f,3,n),n%2==0)

    def test_20_frobenius_period_degree2_F5(self):
        f=Poly(X**2+2,X,modulus=5)
        self.assertTrue(f.is_irreducible)
        for n in range(1,10):
            self.assertEqual(frobenius_fixed_mod(f,5,n),n%2==0)

    def test_21_two_cubic_factors_F2(self):
        factors = Poly(X**8-X,X,modulus=2).factor_list()[1]
        cubics={str(g.as_expr()) for g,e in factors if g.degree()==3}
        self.assertEqual(len(cubics),2)
        self.assertTrue(all(e==1 for g,e in factors))

    def test_22_three_quadratics_F3(self):
        factors=Poly(X**9-X,X,modulus=3).factor_list()[1]
        self.assertEqual(sum(1 for f,e in factors if f.degree()==2),3)

    def test_23_nonreduced_quotient_counterexample(self):
        g=Poly(X**2+X+1,X,modulus=2)
        h=Poly(X**4+X**2+1,X,modulus=2)
        self.assertEqual(g*g,h)
        self.assertTrue(h.diff().is_zero)
        self.assertFalse(g.rem(h).is_zero)
        self.assertTrue((g*g).rem(h).is_zero)

    def test_24_degree_identity_large_range(self):
        for q in (2,3,4,5,7,8,9,11,16,25):
            for n in range(1,27):
                self.assertEqual(q**n,sum(d*mobius_count(q,d) for d in divisors(n)))

    def test_25_mobius_numerator_integral_positive(self):
        for q in (2,3,4,5,7,8,9,16,25):
            for n in range(1,31):
                self.assertGreater(mobius_count(q,n),0)

    def test_26_degree_one_count(self):
        for q in (2,3,4,5,7,8,9,11,16,25):
            self.assertEqual(mobius_count(q,1),q)

if __name__=='__main__': unittest.main(verbosity=2)
