"""Finite-coordinate witnesses for the 15A incomplete-space counterexample."""
from fractions import Fraction
import cmath
import math
import unittest


class Chapter15ARegressionTests(unittest.TestCase):
    def test_reflected_bumps_cancel_but_half_has_nonzero_coordinates(self):
        # eta(s)=max(0, 1/4-|s-1/2|), area 1/16.
        def eta(s):
            return max(Fraction(0), Fraction(1, 4)-abs(s-Fraction(1, 2)))

        def bump(n, t):
            return Fraction(1, 2**n)*eta(2**(n+1)*t-1)

        # Exact trapezoidal integration on all breakpoints of each bump.
        for n in range(1, 33):
            knots = [Fraction(0)] + [
                (1+s)/2**(n+1) for s in
                (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4))
            ] + [Fraction(1)]
            half = sum((b-a)*(bump(n,a)+bump(n,b))/2
                       for a,b in zip(knots, knots[1:]))
            reflected = [2-t for t in reversed(knots)]
            other = sum(-(b-a)*(bump(n,2-a)+bump(n,2-b))/2
                        for a,b in zip(reflected, reflected[1:]))
            self.assertEqual(half, Fraction(1, 2**(2*n+5)))
            self.assertGreater(half, 0)
            self.assertEqual(half+other, 0)

    def test_complex_modulation_not_norm_continuous(self):
        # Complex-valued L2: U_t f(x) = exp(i*t*x)*f(x).
        # At x = pi/t the multiplier differs from 1 in modulus by 2.
        # Continuity of the multiplier then gives essential supremum 2
        # on R; finite samples only witness the sharp lower bound.
        for t in (-2.0, -0.5, 0.25, 3.0):
            x = math.pi / t
            self.assertAlmostEqual(abs(cmath.exp(1j*t*x) - 1), 2.0, places=12)
            self.assertLessEqual(abs(cmath.exp(1j*t*x) - 1), 2.0 + 1e-12)



if __name__ == "__main__":
    unittest.main()
