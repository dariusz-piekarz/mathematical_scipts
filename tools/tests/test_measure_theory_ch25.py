"""Finite atomic regressions for relative differentiation; not a general proof."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import re
import unittest

SOURCE = Path(__file__).resolve().parents[2] / "chapters/pl/measure_theory/25-rozniczkowanie-calek-i-miar.tex"

class TestDifferentiationChapter25(unittest.TestCase):
    def test_atomic_derivative(self):
        for mu in product(range(3), repeat=3):
            for nu in product(range(3), repeat=3):
                for i in range(3):
                    if mu[i]:
                        for r in (Fraction(1,4), Fraction(1,2), Fraction(1)):
                            B = [j for j in range(3) if abs(i-j)<r]
                            self.assertEqual(Fraction(sum(nu[j] for j in B),sum(mu[j] for j in B)),Fraction(nu[i],mu[i]))

    def test_atomic_maximal(self):
        for mu in product(range(3), repeat=3):
            for nu in product(range(3), repeat=3):
                values = []
                for i in range(3):
                    ratios = [Fraction(0)]
                    for r in (1,2,3):
                        B = [j for j in range(3) if abs(j-i)<r]
                        mass = sum(mu[j] for j in B)
                        if mass:
                            ratios.append(Fraction(sum(nu[j] for j in B),mass))
                    values.append(max(ratios))
                for t in (Fraction(1,2), Fraction(1), Fraction(2), Fraction(3)):
                    self.assertLessEqual(t*sum(mu[i] for i in range(3) if values[i]>t),15*sum(nu))

    def test_step_cdf(self):
        for a,m in product(range(5),repeat=2):
            def F(x):
                return a*x+(m if x>=1 else 0)
            for x in (-1,0,2):
                for h in (Fraction(-1,4),Fraction(1,4)):
                    self.assertEqual((F(x+h)-F(x))/h,a)

    def test_open_balls_approach_boundary_from_below(self):
        # An atom on the sphere is excluded, not included.
        for weights in product(range(3), repeat=3):
            for r in (1,2,3):
                target = sum(weights[j] for j in range(3) if j<r)
                for n in range(1,9):
                    q = r-Fraction(1,2**n)
                    self.assertEqual(sum(weights[j] for j in range(3) if j<q),target)

    def test_signed_atomic_derivative(self):
        for mu in product(range(3), repeat=3):
            for nu in product(range(-2,3), repeat=3):
                for i in range(3):
                    if mu[i]:
                        # Singular atoms occur precisely at zero denominator atoms.
                        ac = [nu[j] if mu[j] else 0 for j in range(3)]
                        singular = [nu[j]-ac[j] for j in range(3)]
                        self.assertEqual(singular[i],0)
                        self.assertEqual(Fraction(nu[i],mu[i]),Fraction(ac[i],mu[i]))

    def test_non_doubling_example(self):
        for n in range(1,25):
            a,b = Fraction(1,2**(2*n)),Fraction(1,2**n)
            self.assertEqual((a+b)/a,1+2**n)

    def test_source(self):
        s = SOURCE.read_text(encoding="utf8")
        labels = re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for token in (r"cor:lebesgue-density-25",r"lem:relative-maximal-25",
                      r"thm:relative-lebesgue-25",r"thm:relative-radon-25",r"cor:relative-signed-25",
                      r"r_n\uparrow r",r"\mu(S^c)=0",r"\nu_s(K^c)<\varepsilon"):
            self.assertIn(token,s)
        stack = []
        for m in re.finditer(r"\\(begin|end)\{([^}]+)\}",s):
            if m[1]=="begin":
                stack.append(m[2])
            else:
                self.assertEqual(stack.pop(),m[2])
        self.assertFalse(stack)

if __name__ == "__main__":
    unittest.main()
