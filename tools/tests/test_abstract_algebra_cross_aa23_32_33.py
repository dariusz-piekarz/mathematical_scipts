"""AA-X19: exact bridge between trace-form and polynomial discriminants and resultants.

In the monogenic separable field K(alpha)=K[X]/(f) with monic irreducible
minimal polynomial f, the Gram determinant in the power basis equals
disc(f)=(-1)^(n(n-1)/2) R_{n,n-1}(f,f') in AA-33 convention.
"""
from pathlib import Path
import re
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
x = sp.symbols("x")


def multiplication_matrix(f, h=x, modulus=None):
    """Matrix of multiplication by h in K[x]/(f), in power basis."""
    kw = {"modulus": modulus} if modulus is not None else {"domain": sp.QQ}
    polynomial = sp.Poly(f, x, **kw)
    n = polynomial.degree()
    assert n >= 1 and polynomial.LC() == 1
    cols = [
        sp.Matrix([sp.Poly(h * x ** j, x, **kw).rem(polynomial).nth(i)
                   for i in range(n)])
        for j in range(n)
    ]
    return sp.Matrix.hstack(*cols)


def trace_gram(f, modulus=None):
    n = sp.degree(f, x)
    M = multiplication_matrix(f, modulus=modulus)
    return sp.Matrix(
        n, n, lambda i, j: sp.trace(M ** (i + j))
    )


def formal_resultant(f, g, m, n):
    """AA-33 R_(m,n) with ascending coefficient rows and explicit formal degrees."""
    assert m >= 1 and n >= 1
    assert sp.degree(f, x) <= m
    assert g == 0 or sp.degree(g, x) <= n
    columns = [sp.Poly(f * x ** j, x).all_coeffs() for j in range(n)]
    columns += [sp.Poly(g * x ** j, x).all_coeffs() if g != 0 else [0]
                for j in range(m)]
    def ascending_column(c):
        # all_coeffs is descending order, and shorter vectors are padded with 0s.
        v = list(reversed(c))
        return [v[i] if i < len(v) else 0 for i in range(m + n)]
    A = sp.Matrix.hstack(*(sp.Matrix(ascending_column(c)) for c in columns))
    return sp.expand((-1) ** (m * n) * A.det())


class TraceDiscriminantResultantInterface(unittest.TestCase):
    def test_power_basis_trace_form_discriminants(self):
        for f in (x - 4, x ** 2 - 5, x ** 3 - 2,
                  x ** 3 - 3 * x + 1, x ** 4 - 2):
            with self.subTest(f=str(f)):
                self.assertTrue(sp.Poly(f, x, domain=sp.QQ).is_irreducible)
                G = trace_gram(f)
                self.assertEqual(sp.simplify(G.det() - sp.discriminant(f, x)), 0)
                self.assertNotEqual(G.det(), 0)
                n = sp.degree(f, x)
                M = multiplication_matrix(f)
                self.assertEqual(M.trace(), -sp.Poly(f, x).nth(n - 1))
                self.assertEqual(M.det(), (-1) ** n * sp.Poly(f, x).nth(0))

    def test_resultant_equals_norm_of_polynomial_value(self):
        for f in (x ** 2 - 5, x ** 3 - 2, x ** 3 - 3 * x + 1):
            for h in (2 * x + 3, x ** 2 + x + 1, x - 1):
                with self.subTest(f=str(f), h=str(h)):
                    N = multiplication_matrix(f, h).det()
                    R = formal_resultant(f, h, sp.degree(f, x), sp.degree(h, x))
                    self.assertEqual(N, R)
                    self.assertEqual(R, sp.resultant(f, h, x))

    def test_signed_derivative_resultant_and_formal_degrees(self):
        for f in (x ** 2 - 5, x ** 3 - 2,
                  x ** 3 - 3 * x + 1, x ** 4 - 2, (x - 1) ** 2):
            n = sp.degree(f, x)
            with self.subTest(f=str(f)):
                R = formal_resultant(f, sp.diff(f, x), n, n - 1)
                expected = (-1) ** (n * (n - 1) // 2) * R
                self.assertEqual(expected, sp.discriminant(f, x))
                self.assertEqual(expected, trace_gram(f).det())
        # AA-33 intentionally distinguishes formal and actual degrees.
        f, g = 2 * x + 1, x + 3
        self.assertEqual(formal_resultant(f, g, 1, 1), 5)
        self.assertEqual(formal_resultant(f, g, 1, 2), 10)
        self.assertEqual(formal_resultant(f, g, 2, 1), -5)
        self.assertEqual(formal_resultant((x - 1) ** 2, x + 2, 2, 1), 9)

    def test_change_of_basis_quadratic_extension(self):
        G = trace_gram(x ** 2 - 5)
        self.assertEqual(G, sp.diag(2, 10))
        S = sp.Matrix([[1, sp.Rational(1, 2)], [0, sp.Rational(1, 2)]])
        H = S.T * G * S
        self.assertEqual(H, sp.Matrix([[2, 1], [1, 3]]))
        self.assertEqual(G.det(), 20)
        self.assertEqual(H.det(), 5)
        self.assertEqual(H.det(), S.det() ** 2 * G.det())
        # Polynomial discriminant remains 20; basis discriminant need not.
        self.assertEqual(sp.discriminant(x ** 2 - 5, x), 20)

    def test_characteristic_two_and_three(self):
        cases = (
            (2, x ** 2 + x + 1, 1),  # separable, irreducible in F2
            (2, x ** 2 + 1, 0),      # repeated root in F2
            (3, x ** 2 + 1, 2),      # irreducible/separable in F3
            (3, x ** 3 + 1, 0),      # derivative is zero in F3
        )
        for p, f, want in cases:
            with self.subTest(p=p, f=str(f)):
                n = sp.degree(f, x)
                G = trace_gram(f, modulus=p)
                D = sp.discriminant(f, x) % p
                self.assertEqual(D, want)
                self.assertEqual(G.det() % p, D)
                R = formal_resultant(f, sp.diff(f, x), n, n - 1)
                self.assertEqual(((-1) ** (n * (n - 1) // 2) * R) % p, D)
        # Over F2(t), X^2+t is irreducible (t is not a square), but inseparable.
        t = sp.symbols("t")
        M = sp.Matrix([[0, t], [1, 0]])
        self.assertEqual(M ** 2, t * sp.eye(2))
        self.assertEqual(M.trace(), 0)
        self.assertTrue(sp.Poly(sp.trace(M ** 2), t, modulus=2).is_zero)
        self.assertTrue(sp.Poly(sp.discriminant(x ** 2 + t, x),
                                t, modulus=2).is_zero)

    def test_source_compatibility_and_links(self):
        focus = [
            "23-slad-norma-i-wyroznik.tex",
            "32-wyroznik-i-grupa-galois.tex",
            "33-wypadkowa-wielomianow-i-macierz-sylvestera.tex",
        ]
        prerequisites = [
            "03-dzialania-grup-orbity-i-rownanie-klas.tex",
            "11-pierscienie-wielomianow-i-kryteria-nierozkladalnosci.tex",
            "20-rozszerzenia-cial-i-ciala-rozkladu-wielomianow.tex",
            "21-zanurzenia-automorfizmy-i-rozszerzenia-galois.tex",
            "22-twierdzenie-artina-i-odpowiedniosc-galois.tex",
            "29-struktura-cial-skonczonych-i-wielomiany-nierozkladalne.tex",
            "31-wielomiany-symetryczne-i-wzory-viete.tex",
        ]
        folder = ROOT / "chapters/pl/abstract_algebra"
        fs = {p: (folder / p).read_text(encoding="utf-8") for p in focus + prerequisites}
        labels = [z for src in fs.values() for z in re.findall(r"\\label\{([^{}]+)\}", src)]
        self.assertEqual(len(labels), len(set(labels)))
        self.assertEqual(sum(len(re.findall(r"\\label\{", fs[p])) for p in focus), 49)
        refs = [z for p in focus for z in re.findall(
            r"\\(?:ref|eqref|pageref|autoref)\{([^{}]+)\}", fs[p])]
        self.assertEqual(len(refs), 26)
        self.assertFalse(set(refs) - set(labels), set(refs) - set(labels))
        for req in (
            "aa:def:trace-discriminant", "aa:tw:trace-nondegenerate",
            "aa:lem:trace-discriminant-base-change",
            "aa:def:polynomial-discriminant", "aa:tw:disc-separable",
            "aa:def:sylvester", "aa:tw:res-roots", "aa:tw:disc-resultant",
        ):
            self.assertIn(req, labels)


if __name__ == "__main__":
    unittest.main()
