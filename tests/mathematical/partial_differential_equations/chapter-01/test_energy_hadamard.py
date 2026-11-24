"""Finite regression checks, not substitutes for PDE proofs."""
import math
import unittest
from fractions import Fraction
from itertools import product


class Chapter01Regression(unittest.TestCase):
    def test_wave_flux_PDE_01_031(self):
        for c, p, q in product((1, 2, 3), (-3, -1, 0, 1, 3), (-2, 0, 2)):
            e = Fraction(p*p + c*c*q*q, 2)
            self.assertEqual(c*c*p*q - c*e, -Fraction(c*(p-c*q)**2, 2))
            self.assertEqual(-c*c*p*q - c*e, -Fraction(c*(p+c*q)**2, 2))

    def test_laplace_asymptotic_PDE_01_034(self):
        for k in (1, 5, 10, 20, 40):
            exact = math.sqrt(math.pi/2)*math.exp(-k/2)/k*math.sinh(3*k/4)
            asym = math.sqrt(math.pi/8)*math.exp(k/4)/k
            self.assertAlmostEqual(exact/asym, 1-math.exp(-1.5*k), places=12)

    def test_torus_norm_PDE_01_035(self):
        for k in (1, 5, 10, 20, 40):
            n = 256
            norm_squared = math.fsum(
                math.sin(2*math.pi*k*j/n)**2 for j in range(n)
            ) * 2*math.pi/n
            self.assertAlmostEqual(norm_squared, math.pi, places=12)


if __name__ == "__main__":
    unittest.main()
