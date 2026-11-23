"""AA-X24: Eisenstein for translated prime-power cyclotomic polynomials.

Exact integral and finite-field arithmetic, with full 50-chapter reference scan.
"""
from math import comb
from pathlib import Path
import re
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
X = sp.symbols("X")
PRIMES = (2, 3, 5, 7, 11)


def cyclo(n):
    return sp.Poly(sp.cyclotomic_poly(n, X), X, domain=sp.ZZ)


def prime_power_cases():
    for p in PRIMES:
        for k in (1, 2, 3):
            degree = (p - 1) * p ** (k - 1)
            if degree <= 120:
                yield p, k, p**k, degree


class EisensteinCyclotomicInterface(unittest.TestCase):
    def test_prime_power_formula_and_shifted_eisenstein(self):
        cases = list(prime_power_cases())
        self.assertEqual(len(cases), 13)
        for p, k, n, degree in cases:
            with self.subTest(p=p, k=k):
                f = cyclo(n)
                geometric = sp.Poly(
                    sum(X ** (j * p**(k-1)) for j in range(p)),
                    X, domain=sp.ZZ,
                )
                self.assertEqual(f, geometric)
                self.assertEqual(f.degree(), degree)
                self.assertEqual(f.LC(), 1)
                shifted = sp.Poly(f.as_expr().subs(X, X+1),
                                  X, domain=sp.ZZ)
                coeff = [int(a) for a in shifted.all_coeffs()]
                self.assertEqual(len(coeff), degree + 1)
                self.assertEqual(coeff[0], 1)
                self.assertEqual(coeff[-1], p)
                self.assertTrue(all(a % p == 0 for a in coeff[1:]))
                self.assertNotEqual(coeff[-1] % (p*p), 0)
                self.assertEqual(
                    sp.Poly(shifted.as_expr(), X, modulus=p),
                    sp.Poly(X**degree, X, modulus=p))
                self.assertEqual(
                    sp.Poly(f.as_expr(), X, modulus=p),
                    sp.Poly((X-1)**degree, X, modulus=p))
                self.assertTrue(sp.Poly(f, X, domain=sp.QQ).is_irreducible)

    def test_integer_cyclotomic_product_and_translation_inversion(self):
        for n in range(1, 46):
            with self.subTest(n=n):
                factors = [cyclo(d).as_expr() for d in sp.divisors(n)]
                self.assertEqual(sp.expand(sp.prod(factors)), X**n-1)
                f = cyclo(n).as_expr()
                self.assertEqual(sp.expand(
                    sp.expand(f.subs(X, X+1)).subs(X, X-1)), f)

    def test_values_at_one_characterize_prime_powers(self):
        self.assertEqual(cyclo(1).eval(1), 0)
        for n in range(2, 101):
            fac = sp.factorint(n)
            expected = next(iter(fac)) if len(fac) == 1 else 1
            with self.subTest(n=n):
                self.assertEqual(cyclo(n).eval(1), expected)
                self.assertEqual(
                    sp.Poly(cyclo(n).as_expr().subs(X, X+1),
                            X, domain=sp.ZZ).nth(0), expected)
        for n in (6, 10, 12, 15, 18, 20, 21, 30, 42, 60):
            self.assertEqual(cyclo(n).eval(1), 1)
            self.assertTrue(sp.Poly(cyclo(n), X, domain=sp.QQ).is_irreducible)

    def test_general_modp_prime_part_cyclotomic_identity(self):
        # For n=p^k*m, gcd(m,p)=1:
        # Phi_n(X) mod p = (Phi_m(X) mod p)^(phi(p^k)).
        tested = 0
        for n in range(2, 86):
            for p, k in sp.factorint(n).items():
                with self.subTest(n=n, p=p):
                    m = n // p**k
                    exponent = (p-1)*p**(k-1)
                    reduced = sp.Poly(cyclo(n).as_expr(), X, modulus=p)
                    h = sp.Poly(cyclo(m).as_expr(), X, modulus=p)
                    self.assertEqual(reduced, h**exponent)
                    # If p does not divide m, Phi_m divides squarefree
                    # X^m-1 in F_p[X]; thus it is itself squarefree.
                    self.assertEqual(h.gcd(h.diff()).degree(), 0)
                    expected_gcd_degree = (exponent-1)*h.degree()
                    self.assertEqual(reduced.gcd(reduced.diff()).degree(),
                                     expected_gcd_degree)
                    self.assertEqual(
                        expected_gcd_degree == 0,
                        p == 2 and k == 1,
                    )
                    tested += 1
        self.assertGreaterEqual(tested, 100)

    def test_independent_binomial_coefficient_eisenstein_check(self):
        # Independently compute each translated coefficient from
        # sum_{j=0}^{p-1} (1+X)^(j*p^(k-1)).
        for p, k, n, degree in prime_power_cases():
            with self.subTest(n=n):
                coeff = [
                    sum(comb(j*p**(k-1), t)
                        for j in range(p) if t <= j*p**(k-1))
                    for t in range(degree+1)
                ]
                self.assertEqual(coeff[-1], 1)
                self.assertEqual(coeff[0], p)
                self.assertTrue(all(v % p == 0 for v in coeff[:-1]))
                shifted = sp.Poly(cyclo(n).as_expr().subs(X, X+1),
                                  X, domain=sp.ZZ)
                self.assertEqual(tuple(coeff),
                                 tuple(int(shifted.nth(t))
                                       for t in range(degree+1)))

    def test_edge_cases_and_eisenstein_not_converse(self):
        # Phi_1(X+1)=X, constant coefficient 0: no Eisenstein p.
        self.assertEqual(sp.expand(cyclo(1).as_expr().subs(X, X+1)), X)
        # Prime power p=2,k=1: degree one is separable mod 2.
        self.assertEqual(cyclo(2).as_expr(), X+1)
        self.assertEqual(
            sp.Poly(cyclo(2).as_expr(), X, modulus=2).gcd(
                sp.Poly(cyclo(2).as_expr(), X, modulus=2).diff()
            ).degree(), 0)
        # The AA-11 example Phi_8=X^4+1.
        self.assertEqual(cyclo(8).as_expr(), X**4+1)
        self.assertEqual(
            sp.expand(cyclo(8).as_expr().subs(X, X+1)),
            X**4+4*X**3+6*X**2+4*X+2)
        # An irreducible polynomial need not be Eisenstein at any p
        # after the same shift, because its constant term can be 1.
        self.assertEqual(sp.expand(cyclo(6).as_expr().subs(X, X+1)),
                         X**2+X+1)

    def test_source_labels_refs_and_stable_chapter_contract(self):
        folder = ROOT / "chapters/pl/abstract_algebra"
        paths = sorted(folder.glob("[0-9][0-9]-*.tex"))
        self.assertEqual(len(paths), 50)
        all_sources = {p.name: p.read_text(encoding="utf-8")
                       for p in paths}
        labels = [m for s in all_sources.values()
                  for m in re.findall(r"\\label\{([^{}]+)\}", s)]
        self.assertEqual(len(labels), len(set(labels)))
        focus = (
            "11-pierscienie-wielomianow-i-kryteria-nierozkladalnosci.tex",
            "28-ciala-cyklotomiczne-i-wielomiany-cyklotomiczne.tex",
        )
        self.assertEqual(
            sum(len(re.findall(r"\\label\{", all_sources[f]))
                for f in focus), 47)
        refs = [z for f in focus
                for z in re.findall(
                    r"\\(?:ref|eqref|pageref|autoref)\{([^{}]+)\}",
                    all_sources[f])]
        self.assertEqual(len(refs), 24)
        self.assertEqual(set(refs) - set(labels), set())
        for label in (
            "aa:tw:eisenstein", "aa:prz:x4plus1",
            "aa:tw:cyclotomic-product",
            "aa:tw:cyclotomic-irreducible",
            "aa:tw:cyclotomic-galois",
        ):
            self.assertIn(label, labels)
        self.assertIn("p^2\\nmid a_0", all_sources[focus[0]])
        self.assertIn("\\Phi_1(X)=X-1", all_sources[focus[1]])


if __name__ == "__main__":
    unittest.main()
