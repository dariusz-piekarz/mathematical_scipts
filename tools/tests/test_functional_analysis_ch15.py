"""Regression checks for functional analysis chapter 15.

These tests check finite-dimensional witnesses, not the full Banach-space proofs.
"""
import math
import unittest


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


if __name__ == "__main__":
    unittest.main()
