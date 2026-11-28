"""Regression checks for functional analysis chapter 15.

These tests check finite-dimensional witnesses, not the full Banach-space proofs.
"""
import math
import unittest
from fractions import Fraction
from pathlib import Path
from itertools import permutations
from math import factorial


class Chapter15RegressionTests(unittest.TestCase):
    def test_positive_hessian_without_uniform_lower_bound(self):
        # f(t e_n) = t^2/(2n) - |t|^3; choose t=1/n.
        for n in (2, 5, 20, 100):
            t = 1.0 / n
            self.assertLess(t * t / (2 * n) - t**3, 0.0)
            self.assertGreater(t * t / n, 0.0)

    def test_neumann_scalar_inverse_and_error_bound(self):
        for t in (-0.7, -0.2, 0.0, 0.4, 0.8):
            partial = sum(t**j for j in range(21))
            exact = 1.0 / (1.0 - t)
            self.assertLessEqual(abs(partial - exact), abs(t)**21 / (1 - abs(t)) + 1e-13)
            self.assertAlmostEqual((1 - t) * exact, 1.0)

    def test_inverse_map_rank_one_example(self):
        # Along span(v), f(sv)=(s+s^2||v||^2)v.
        norm_v_sq = 2.0
        for s in (-0.1, 0.0, 0.2):
            derivative = 1 + 2 * s * norm_v_sq
            self.assertGreater(derivative, 0)
            eps = 1e-6
            f = lambda z: z + norm_v_sq * z*z
            central = (f(s+eps)-f(s-eps))/(2*eps)
            self.assertAlmostEqual(central, derivative, places=8)

    def test_implicit_operator_first_two_derivatives(self):
        # u(lambda)=g/(1-lambda*k): u'(0)=kg, u''(0)=2k^2g.
        k, g = 0.3, 2.0
        u = lambda lam: g / (1 - lam*k)
        h = 1e-4
        first = (u(h)-u(-h))/(2*h)
        second = (u(h)-2*u(0)+u(-h))/(h*h)
        self.assertAlmostEqual(first, k*g, places=7)
        self.assertAlmostEqual(second, 2*k*k*g, places=6)



    def test_audit26_source_contracts(self):
        root = Path(__file__).resolve().parents[2]
        source = (root / "chapters/pl/functional_analysis/15-pochodne-wyzszych-rzedow-i-lokalne-twierdzenia-analizy-nieliniowej.tex").read_text(encoding="utf-8")
        for fragment in (
            "D^2f(x+\\alpha sh+\\beta tk)[k,h]",
            "\\frac{\\gamma^{(m)}(0)}{m!}",
            "d(x_p,x_n)\\le q^n d(x_1,x_0)/(1-q)",
            "(A^{-1}Df(g(y)))^{-1}A^{-1}",
            "U_0\\times V_0\\subseteq\\mathcal U",
            "R^{n-m}/(n-m)!",
            "e^{(m+1)\\|A\\|}",
            "P_{m+1}(A)[H,\\cdot]",
        ):
            self.assertIn(fragment, source)

    def test_taylor_integral_remainder_monomials(self):
        # Exact scalar monomial witnesses for the beta integral in Taylor.
        for m in range(1, 6):
            for n in range(m, 10):
                derivative_factor = factorial(n) // factorial(n-m)
                integral = sum(
                    Fraction((-1)**j * math.comb(m-1, j), n-m+j+1)
                    for j in range(m)
                )
                self.assertEqual(derivative_factor * integral / factorial(m-1), 1)

    def test_inverse_second_derivative_noncommutative(self):
        def matmul(a,b):
            return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                               for j in range(2)) for i in range(2))
        b = ((Fraction(1,2),0),(0,Fraction(1,3)))
        h = ((0,1),(0,0))
        k = ((0,0),(1,0))
        terms = []
        for u,v in permutations((h,k)):
            terms.append(matmul(matmul(matmul(matmul(b,u),b),v),b))
        total = tuple(tuple(sum(t[i][j] for t in terms) for j in range(2)) for i in range(2))
        # Coefficient of s*t in inverse of [[2,s],[t,3]].
        self.assertEqual(total, ((Fraction(1,12),0),(0,Fraction(1,18))))

    def test_exponential_simplex_coefficients(self):
        # Exact integral of a simplex monomial via repeated beta integrals.
        for k0 in range(4):
            for k1 in range(4):
                for k2 in range(4):
                    beta1 = Fraction(factorial(k0)*factorial(k1),factorial(k0+k1+1))
                    p = k0+k1+1
                    beta2 = Fraction(factorial(p)*factorial(k2),factorial(p+k2+1))
                    self.assertEqual(beta1*beta2,
                        Fraction(factorial(k0)*factorial(k1)*factorial(k2),
                                 factorial(k0+k1+k2+2)))

if __name__ == "__main__":
    unittest.main()
