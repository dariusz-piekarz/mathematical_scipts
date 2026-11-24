"""Finite formula regressions; not a proof or a parser of the TeX source."""
import cmath
import math
import unittest
from fractions import Fraction as F


class LaplacePoissonTests(unittest.TestCase):
    def test_radial_fundamental_flux(self):
        # h' and h'' with the common sphere-area factor removed.
        for n in range(2, 9):
            for r in (F(1, 5), F(1, 2), F(3), F(7, 3)):
                with self.subTest(n=n, r=r):
                    hp = -r ** (1 - n)
                    hpp = (n - 1) * r ** (-n)
                    self.assertEqual(hpp + (n - 1) * hp / r, 0)
                    self.assertEqual(-hp * r ** (n - 1), 1)

    def test_green_correction(self):
        for R in (F(1), F(2), F(3, 2)):
            for y in (F(0), R / 4, -R / 2):
                for x in (-R, -R / 3, R / 2, R):
                    with self.subTest(R=R, x=x, y=y):
                        Q = R * R - 2 * x * y + x * x * y * y / (R * R)
                        self.assertEqual(Q, (R - x * y / R) ** 2)
                        self.assertGreaterEqual(Q, (R - abs(y)) ** 2)
                        if y:
                            self.assertEqual(Q, y * y * (x - R * R / y) ** 2 / (R * R))
                        if abs(x) == R:
                            self.assertEqual(Q, (x - y) ** 2)
                            self.assertEqual((x-y)*x-(y*y*x/(R*R)-y)*x, R*R-y*y)

    def test_poisson_disk_modes(self):
        # Periodic trapezoid rule, checked against independent exact modes.
        N = 1024
        for r in (0., .2, .6, .85):
            for theta in (0., .37, 1.2):
                z = r * cmath.exp(1j * theta)
                nodes = [cmath.exp(2j * math.pi * j / N) for j in range(N)]
                weights = [(1-r*r)/abs(z-w)**2/N for w in nodes]
                self.assertTrue(all(w > 0 for w in weights))
                self.assertAlmostEqual(sum(weights), 1., places=10)
                for k in (1, 2, 5, 9):
                    with self.subTest(r=r, theta=theta, k=k):
                        value = sum(w * t**k for w, t in zip(weights, nodes))
                        self.assertAlmostEqual(value.real, (z**k).real, places=10)
                        self.assertAlmostEqual(value.imag, (z**k).imag, places=10)

    def test_harnack_ratios(self):
        for n in range(2, 9):
            for s in (.0, .2, .5, .8):
                lo = (1-s)/(1+s)**(n-1)
                hi = (1+s)/(1-s)**(n-1)
                for t in (-1., -.4, 0., .6, 1.):
                    ratio = (1-s*s)/(1-2*s*t+s*s)**(n/2)
                    self.assertLessEqual(lo, ratio+1e-10)
                    self.assertLessEqual(ratio, hi+1e-10)

    def test_quadratic_barrier(self):
        for n in range(2, 9):
            for R in (F(1), F(3, 2), F(4)):
                b = lambda x: (R*R-x*x)/(2*n)
                h = R/7
                self.assertEqual(n*(b(h)-2*b(0)+b(-h))/h**2, -1)
                self.assertEqual(b(R), 0)
                self.assertEqual(b(0), R*R/(2*n))

    def test_analytic_majorant(self):
        for n in range(2, 17):
            c = F(1, 2) + F(1, 16*n)
            self.assertLessEqual(c, F(9, 16))
            # Binomial majorant ratio eventually below 1.
            k = 4*n
            self.assertLess(c*(F(n, 2)+k)/(k+1), 1)

    def test_punctured_ball_comparison(self):
        for n in range(2, 9):
            for s in (.2, .5, .9):
                prev = 1.
                for eps in (s/2, s/10, s/100, s/1000):
                    v = (math.log(s)/math.log(eps) if n == 2 else
                         (s**(2-n)-1)/(eps**(2-n)-1))
                    self.assertGreaterEqual(v, 0.)
                    self.assertLess(v, prev)
                    prev = v


if __name__ == '__main__':
    unittest.main()
