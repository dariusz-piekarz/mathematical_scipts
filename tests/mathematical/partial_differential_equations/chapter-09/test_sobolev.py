"""Exact finite checks of selected chapter 09 formulas, not proofs of density or traces."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import re
import unittest


class SobolevChecks(unittest.TestCase):
    def test_PDE_09_025_multiindex_pascal(self):
        def c(alpha, beta):
            if any(b < 0 or b > a for a, b in zip(alpha, beta)):
                return 0
            return comb(alpha[0], beta[0]) * comb(alpha[1], beta[1])
        for a in range(5):
            for b in range(5):
                for j in (0, 1):
                    alpha = (a, b)
                    upper = tuple(v + (i == j) for i, v in enumerate(alpha))
                    for m in range(a + 2):
                        for n in range(b + 2):
                            gamma = (m, n)
                            lower = tuple(v - (i == j) for i, v in enumerate(gamma))
                            self.assertEqual(c(alpha, lower) + c(alpha, gamma), c(upper, gamma))

    def test_PDE_09_028_mollifier_diagram_clearance(self):
        # Check actual source coordinates rather than a duplicate drawing.
        root = Path(__file__).resolve().parents[4]
        source = (root / "chapters/pl/partial_differential_equations/"
                  "09-przestrzenie-sobolewa.tex").read_text(encoding="utf-8")
        diagram = source.split(r"\begin{tikzpicture}", 1)[1].split(
            r"\end{tikzpicture}", 1)[0]
        num = r"([-+]?(?:\d+(?:\.\d*)?|\.\d+))"
        point = r"\(" + num + "," + num + r"\)"
        def bounds(color):
            m = re.search(r"fill=" + color + r"[^\]]*\]\s*" + point
                          + r"\s+rectangle\s+" + point, diagram)
            self.assertIsNotNone(m)
            return tuple(map(F, m.groups()))
        ux0, uy0, ux1, uy1 = bounds("green")
        kx0, ky0, kx1, ky1 = bounds("orange")
        m = re.search(r"\\coordinate \(x\) at " + point, diagram)
        self.assertIsNotNone(m)
        x, y = map(F, m.groups())
        m = re.search(r"\(x\) circle \(" + num + r"\)", diagram)
        self.assertIsNotNone(m)
        radius = F(m.group(1))
        self.assertGreater(radius, 0)
        self.assertTrue(kx0 < x < kx1 and ky0 < y < ky1)
        # K + closed ball lies in the central strip of U; reserve a
        # conservative 0.4 coordinate units for its 10pt rounded corners.
        self.assertGreater(min(kx0-ux0, ux1-kx1), radius + F(2, 5))
        self.assertGreater(min(ky0-uy0, uy1-ky1), radius)

    def test_PDE_09_066_reflection_moments(self):
        # Lagrange basis at 1 with nodes -1,...,-k.
        for k in range(1, 9):
            nodes = list(range(-1, -k - 1, -1))
            weights = []
            for x in nodes:
                w = F(1)
                for y in nodes:
                    if x != y:
                        w *= F(1 - y, x - y)
                weights.append(w)
            for m in range(k):
                self.assertEqual(sum(w * x**m for w, x in zip(weights, nodes)), 1)
            self.assertNotEqual(sum(w * x**k for w, x in zip(weights, nodes)), 1)

    def test_PDE_09_076_green_kernel(self):
        for y in (F(1, 7), F(1, 2), F(5, 6)):
            left = lambda x: x * (1 - y)
            right = lambda x: y * (1 - x)
            self.assertEqual(left(0), 0)
            self.assertEqual(right(1), 0)
            self.assertEqual(left(y), right(y))
            self.assertEqual(-y - (1 - y), -1)
        # Integral of G(x,y) over y, for f=1.
        for x in (F(0), F(1, 5), F(1, 2), F(1)):
            integral = (1 - x) * x*x/2 + x * (F(1, 2) - x + x*x/2)
            self.assertEqual(integral, x*(1-x)/2)

    def test_PDE_09_079_080_scaling(self):
        for d in range(2, 9):
            for p in range(1, d):
                critical = F(d*p, d-p)
                self.assertEqual(d/critical - F(d,p) + 1, 0)
                self.assertLess(d/(critical + 1) - F(d,p) + 1, 0)
                self.assertLess(1 - F(d,p), 0)  # q=infinity


if __name__ == "__main__":
    unittest.main()
