"""Finite regression checks for PDE chapter 10; not proofs of analytic theorems."""
from fractions import Fraction as F
from itertools import product
from math import factorial
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "chapters/pl/partial_differential_equations/10-zanurzenia-i-zwartosc-sobolewa.tex"


class EmbeddingChecks(unittest.TestCase):
    def test_PDE_10_009_011_sobolev_exponents(self):
        for d in range(2, 10):
            for p in [F(i, 2) for i in range(2, 2*d)]:
                critical = d*p/(d-p)
                gamma = p*(d-1)/(d-p)
                self.assertEqual(gamma*d/(d-1), critical)
                self.assertEqual(1-d/p+d/critical, 0)
                self.assertLess(1-d/p+d/(critical+1), 0)
                if p > 1:
                    self.assertEqual((gamma-1)*p/(p-1), critical)
                    self.assertGreater(gamma, 1)

    def test_PDE_10_023_028_exponents(self):
        for d in range(2, 10):
            for q in range(d+1, d+12):
                p0 = F(d*q, d+q)
                self.assertTrue(1 < p0 < d)
                self.assertEqual(d*p0/(d-p0), q)
                p = F(q)
                conjugate = p/(p-1)
                delta = d-(d-1)*conjugate
                self.assertGreater(delta, 0)
                self.assertEqual(delta/conjugate, 1-d/p)

    def test_PDE_10_037_039_cube_averages(self):
        # Exact piecewise-constant averages of affine functions on [0,1]^d.
        # Integrate the squared difference cellwise using the variance h^2/12.
        for d in range(1, 4):
            slopes = tuple(F(i+1, 3) for i in range(d))
            gradient_squared = sum(a*a for a in slopes)
            for n in (1, 2, 3, 5):
                h = F(1, n)
                averages = []
                for cell in product(range(n), repeat=d):
                    center = [(F(i)+F(1, 2))*h for i in cell]
                    averages.append(sum(a*x for a,x in zip(slopes,center)))
                self.assertEqual(sum(averages)*h**d, sum(slopes)/2)
                squared_error = n**d*h**d*h*h*gradient_squared/12
                self.assertLessEqual(squared_error, d*h*h*gradient_squared)
                self.assertEqual(squared_error, h*h*gradient_squared/12)

    def test_PDE_10_043_interpolation(self):
        for a in range(1, 5):
            for b in range(a+2, a+8):
                for q in range(a+1,b):
                    theta = (F(1,q)-F(1,b))/(F(1,a)-F(1,b))
                    self.assertTrue(0 < theta < 1)
                    self.assertEqual(theta/a+(1-theta)/b, F(1,q))
                    self.assertEqual(q*theta/a+q*(1-theta)/b, 1)

    def test_PDE_10_051_052_radial_integrals(self):
        # Recurrence for I_n = integral_0^infty t^n exp(-dt) dt.
        for d in range(2, 10):
            value = F(1,d)
            for n in range(1,d+1):
                value *= F(n,d)
            self.assertEqual(value,F(factorial(d),d**(d+1)))
            # Integral_1^R t^-d, increasing to 1/(d-1).
            for R in (2, 10, 100):
                finite = (1-F(1,R**(d-1)))/(d-1)
                self.assertTrue(0 < finite < F(1,d-1))

    def test_PDE_10_069_graph_shift(self):
        # Exact rational samples for the stated support-clearance estimate.
        for L in (F(0), F(1,2), F(2), F(5)):
            a = 2+L
            eps = F(1,20)
            for slope in (-L, L):
                for x in (F(-1),F(0),F(1)):
                    for z1 in (-eps, F(0),eps):
                        for z2 in (-eps, F(0),eps):
                            y1 = x+z1
                            y2 = slope*x+a*eps+z2
                            self.assertGreaterEqual(y2-slope*y1,(a-1-L)*eps)
            self.assertGreater(a-1-L,0)

    def test_PDE_10_075_summary_scope(self):
        source = SOURCE.read_text(encoding="utf-8")
        section = source.split(r"\label{sec:pde10-summary}",1)[1]
        diagram = section.split(r"\begin{tikzpicture}",1)[1].split(r"\end{tikzpicture}",1)[0]
        self.assertIn(r"d\ge2",diagram)
        self.assertIn(r"\beta<\alpha",diagram)
        self.assertIn(r"q<p^*",diagram)
        self.assertIn(r"q<\infty",diagram)
        # Source-level check only: rendered layout is reviewed separately.
        self.assertRegex(section,r"0\\le\\beta<\\alpha")


if __name__ == "__main__":
    unittest.main()
