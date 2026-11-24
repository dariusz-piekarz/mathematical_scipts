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


    def test_mt31_006_whitney_intervals(self):
        # K={0}, dyadic intervals on the positive half-line.
        # Scaling and reflection reduce the check to integer indices.
        for m in range(8,16):
            for j in range(-4,5):
                ell = Q(2)**j
                lo,hi = m*ell,(m+1)*ell
                parent_lo = 2*(m//2)*ell
                self.assertGreaterEqual(lo,8*ell)
                self.assertLess(parent_lo,16*ell)
                self.assertLess(lo,18*ell)
                self.assertGreaterEqual(lo-ell/8,7*ell)
                self.assertLessEqual(hi+ell/8,20*ell)

    def test_mt31_007_whitney_polynomial_recenter(self):
        # Exact scalar polynomials with coefficients of x^i.
        def deriv(c,b,r):
            return sum(c[i]*factorial(i)//factorial(i-r)*b**(i-r)
                       for i in range(r,len(c)))
        for c in product(range(-2,3),repeat=4):
            for b in (-2,0,3):
                for z in (-1,1,4):
                    for r in range(4):
                        actual = deriv(c,z,r)
                        recentered = sum(Q(deriv(c,b,r+j),factorial(j))*(z-b)**j
                                         for j in range(4-r))
                        self.assertEqual(actual,recentered)

    def test_mt31_008_whitney_derivative_bounds_and_gluing(self):
        s = " ".join(SOURCE.read_text(encoding="utf-8").split())
        for term in ("parami rozłącznych wnętrzach, których suma",
                     "pokrycie powiększeniami jest lokalnie skończone",
                     "Traktując $a$ jako ustalony punkt podczas różniczkowania",
                     "dla dowolnego kierunku zbliżania",
                     "Wektor $(H_"):
            self.assertIn(term,s)
        for expr in (r"7\sqrt n\,\ell(Q)",r"20\sqrt n\,\ell(Q)",
                     r"D^\alpha(S^{-1})",r"z\in\overline{Q^*}",
                     r"r^{k-|\beta|+|\gamma|}"):
            self.assertIn(expr,s)

if __name__ == "__main__":
    unittest.main()
