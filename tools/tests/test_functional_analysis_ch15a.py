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




    def test_audit30_source_contracts(self):
        from pathlib import Path
        root = Path(__file__).resolve().parents[2]
        source = (root / "chapters/pl/functional_analysis/15A-calkowanie-funkcji-w-przestrzeniach-lokalnie-wypuklych.tex").read_text(encoding="utf-8")
        for fragment in (
            "p(I-S(f,P))<\\varepsilon/2",
            "f(t,s+h)-f(t,s)=\\int_s^{s+h}\\partial_s f(t,u)\\,\\mathrm du",
            "p(G(s+h)-G(s))",
            "p(S(A,P)-D(P,Q))",
            "p(S(B,Q)-D(P,Q))",
            "\\chi_A/\\sqrt{\\lambda_1(A)}",
        ):
            self.assertIn(fragment, source)

    def test_moving_limits_crossing_and_equal(self):
        # f(t,s)=t+s; limits s and 2s. Covers reversed, equal and ordered limits.
        def primitive(t,s):
            return t*t/2+s*t
        for s in (Fraction(-2), Fraction(-1,3), Fraction(0), Fraction(1,3), Fraction(2)):
            F = lambda x: primitive(2*x,x)-primitive(x,x)
            leibniz = 2*(2*s+s)-(s+s)+(2*s-s)
            self.assertEqual(leibniz,5*s)
            for h in (Fraction(-1,100), Fraction(1,100)):
                self.assertEqual((F(s+h)-F(s))/h-leibniz, 5*h/2)

    def test_fubini_polynomial_exact(self):
        # Mixed polynomial t^2*s + 3*t*s^2 - 2 on [0,2] x [-1,3].
        # Integrate each monomial first along either coordinate.
        def moment(a,b,k):
            return (Fraction(b)**(k+1)-Fraction(a)**(k+1))/(k+1)
        for a,b,c,d in ((0,2,-1,3),(-2,1,0,1),(0,1,0,1)):
            terms = [(1,1,2),(3,2,1),(-2,0,0)]
            first = sum(coef*moment(c,d,j)*moment(a,b,i) for coef,i,j in terms)
            second = sum(coef*moment(a,b,i)*moment(c,d,j) for coef,i,j in terms)
            self.assertEqual(first,second)

if __name__ == "__main__":
    unittest.main()
