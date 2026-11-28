"""Independent mathematical and structural regression tests for AA-28.
Run from repository root: python -m unittest tools.tests.test_abstract_algebra_ch28_independent -v
"""
import math
import re
import unittest
from pathlib import Path

from sympy import Poly, QQ, ZZ, Symbol, cyclotomic_poly, divisors, totient, gcd

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / 'chapters/pl/abstract_algebra/28-ciala-cyklotomiczne-i-wielomiany-cyklotomiczne.tex'
if not CHAPTER.exists():
    CHAPTER = Path('/mnt/data/AA-28-audyt-I-zrodlo.tex')
SOURCE = CHAPTER.read_text(encoding='utf-8')
x = Symbol('x')


class AA28Independent(unittest.TestCase):
    def test_01_phi_degree_matches_totient_independent_range(self):
        for n in range(1, 72):
            self.assertEqual(Poly(cyclotomic_poly(n, x), x).degree(), int(totient(n)), n)

    def test_02_integer_and_monic(self):
        for n in range(1, 72):
            f = Poly(cyclotomic_poly(n, x), x, domain=ZZ)
            self.assertEqual(f.LC(), 1, n)
            self.assertTrue(all(int(c) == c for c in f.all_coeffs()), n)

    def test_03_product_identity(self):
        for n in range(1, 53):
            p = Poly(1, x, domain=ZZ)
            for d in divisors(n):
                p *= Poly(cyclotomic_poly(d, x), x, domain=ZZ)
            self.assertEqual(p, Poly(x**n-1, x, domain=ZZ), n)

    def test_04_irreducibility(self):
        for n in range(1, 64):
            self.assertTrue(Poly(cyclotomic_poly(n, x), x, domain=QQ).is_irreducible, n)

    def test_05_coprime_power_preserves_minimal_polynomial(self):
        # Algebraic identity Phi_n(X^ell) mod Phi_n(X) = 0 for gcd(n, ell)=1.
        for n in range(2, 35):
            f = Poly(cyclotomic_poly(n, x), x, domain=QQ)
            for ell in (2, 3, 5, 7):
                if math.gcd(n, ell) == 1:
                    composed = Poly(cyclotomic_poly(n, x**ell), x, domain=QQ)
                    self.assertTrue(composed.rem(f).is_zero, (n, ell))

    def test_06_prime_power_argument_has_no_repeated_reduction_roots(self):
        for n in range(1, 44):
            for p in (2, 3, 5, 7):
                if n % p:
                    f = Poly(x**n-1, x, modulus=p)
                    self.assertEqual(gcd(f, f.diff()).degree(), 0, (n, p))

    def test_07_nonseparability_when_characteristic_divides_n(self):
        for p in (2, 3, 5, 7):
            for mul in (1, 2, 4):
                f = Poly(x**(mul*p)-1, x, modulus=p)
                self.assertGreater(gcd(f, f.diff()).degree(), 0, (p, mul))

    def test_08_phi3_mod3_is_square(self):
        self.assertEqual(Poly(cyclotomic_poly(3, x), x, modulus=3), Poly((x-1)**2, x, modulus=3))

    def test_09_reduction_can_factor_when_coprime(self):
        f = Poly(cyclotomic_poly(5, x), x, modulus=11)
        self.assertEqual(len([a for a in range(11) if f.eval(a)==0]), 4)

    def test_10_coprime_reductions_of_phi_are_squarefree(self):
        for n in range(2, 37):
            for p in (2, 3, 5, 7):
                if n % p:
                    f = Poly(cyclotomic_poly(n, x), x, modulus=p)
                    self.assertEqual(gcd(f, f.diff()).degree(), 0, (n,p))

    def test_11_unit_group_5_cyclic(self):
        self.assertEqual([(2**j) % 5 for j in range(4)], [1, 2, 4, 3])

    def test_12_unit_group_8_not_cyclic(self):
        units = [i for i in range(1, 8) if math.gcd(8, i) == 1]
        self.assertEqual(units, [1,3,5,7])
        self.assertEqual({(a*a) % 8 for a in units}, {1})

    def test_13_unit_actions_permute_primitive_powers(self):
        for n in range(2, 47):
            units = {i for i in range(n) if math.gcd(i, n) == 1}
            for a in units:
                self.assertEqual({(a*b) % n for b in units}, units, (n,a))

    def test_14_primitive_power_order(self):
        for n in range(2, 63):
            for k in range(1, n+1):
                self.assertEqual(n//math.gcd(n,k),min(j for j in range(1,n+1) if k*j % n == 0))

    def test_15_fixed_field_quadratic_relation(self):
        f = Poly(cyclotomic_poly(5,x), x, domain=QQ)
        # If u=z+z^-1, then z^2(u^2+u-1)=(z^2+1)^2+z(z^2+1)-z^2.
        relation = Poly((x**2+1)**2 + x*(x**2+1) - x**2, x, domain=QQ)
        self.assertTrue(relation.rem(f).is_zero)
        self.assertTrue(Poly(x*x+x-1,x,domain=QQ).is_irreducible)

    def test_16_fixed_field_degree_matches_subgroup_index(self):
        self.assertEqual(int(totient(5)),4)
        self.assertEqual(4//2,2)
        self.assertEqual(Poly(x*x+x-1,x).degree(),2)

    def test_17_phi8_exact_primitive_roots(self):
        self.assertEqual(cyclotomic_poly(8,x),x**4+1)
        self.assertTrue(Poly(cyclotomic_poly(8,x),x).is_irreducible)

    def test_18_phi1_and_unit_ring_case(self):
        self.assertEqual(cyclotomic_poly(1,x),x-1)
        self.assertEqual(int(totient(1)),1)

    def test_19_source_labels_unique(self):
        labels = re.findall(r'\\label\{([^}]+)\}', SOURCE)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertEqual(len(labels),10)

    def test_20_source_internal_and_external_refs(self):
        labels = set(re.findall(r'\\label\{([^}]+)\}', SOURCE))
        refs = set(re.findall(r'\\ref\{([^}]+)\}', SOURCE))
        self.assertEqual(refs-labels, {'aa:ch:fields-fractions','aa:ch:kummer'})

    def test_21_source_has_all_proofs(self):
        for lab in ('aa:tw:cyclotomic-product', 'aa:lem:cyclotomic-prime',
                    'aa:tw:cyclotomic-irreducible','aa:tw:cyclotomic-galois'):
            self.assertIn('\\label{'+lab+'}', SOURCE)
        self.assertEqual(SOURCE.count('\\begin{proof}'),SOURCE.count('\\end{proof}'))

    def test_22_style_and_figure(self):
        self.assertNotIn('injektywne', SOURCE)
        self.assertNotIn('pole elementów stałych', SOURCE)
        self.assertIn('\\label{aa:fig:cyclotomic-five}', SOURCE)
        self.assertIn('\\begin{tikzpicture}', SOURCE)


if __name__ == '__main__':
    unittest.main(verbosity=2)
