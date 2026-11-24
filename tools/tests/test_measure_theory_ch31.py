"""Chapter 31: finite models and source regressions, not proof certification."""
from fractions import Fraction as Q
from math import comb, factorial
from itertools import product
from pathlib import Path
import re
import unittest

SOURCE = Path(__file__).resolve().parents[2] / "chapters/pl/measure_theory/31-dzety-od-geometrii-rozniczkowej-do-teorii-miary.tex"

class Chapter31(unittest.TestCase):
    def test_mt31_001_monomial_count(self):
        for n in range(1,5):
            for k in range(6):
                self.assertEqual(sum(sum(a)<=k for a in product(range(k+1), repeat=n)),comb(n+k,k))

    def test_mt31_002_taylor_integral_coefficient(self):
        # Integral t^r(1-t)^k equals r!k!/(r+k+1)!.
        for k in range(7):
            for r in range(5):
                integral = sum(Q((-1)**j*comb(k,j),r+j+1) for j in range(k+1))
                self.assertEqual(integral,Q(factorial(r)*factorial(k),factorial(r+k+1)))
                if r == 0:
                    self.assertEqual((k+1)*integral,1)

    def test_mt31_003_second_jet_affine_change(self):
        # y=x+x^2, at 0: d/dy=d/dx, d²/dy²=d²/dx²-2d/dx.
        for p,a,b in product(range(-3,4),repeat=3):
            self.assertEqual((a-2*p)-(b-2*p),a-b)
        self.assertEqual(0-2*1,-2)

    def test_mt31_004_density_cone_intersection_bound(self):
        # Finite probability model: P(C ∩ A) >= P(C)-P(A^c).
        for c in range(1,9):
            for missing in range(9):
                for overlap in range(max(0,c+missing-8),min(c,missing)+1):
                    self.assertGreaterEqual(c-overlap,c-missing)

    def test_mt31_005_labels_and_source(self):
        s = SOURCE.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertEqual(len(labels),30)
        self.assertIn("thm:dzety-whitney-extension",labels)
        flat = " ".join(s.split())
        for step in ("przedstawicieli kiełków", "resztą całkową",
                     "czynnik niezróżniczkowany", "drugi aksjomat przeliczalności",
                     "Działanie jest wolne i przechodnie", "dopełnienia $A-x$"):
            self.assertIn(step,flat)
        self.assertNotRegex(s,r"\\(?:mathbf|mathbb)\{1\}_")

if __name__ == "__main__":
    unittest.main()
