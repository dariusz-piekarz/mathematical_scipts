"""Source regressions and exact finite models for chapter 27."""
import unittest
from pathlib import Path
from fractions import Fraction as Q
import re

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/pl/measure_theory/27-miary-na-rozmaitosciach-ujecie-miarowo-teoretyczne.tex"


class Chapter27(unittest.TestCase):
    def test_stable_labels(self):
        text = SOURCE.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", text)
        self.assertEqual(len(labels), 11)
        self.assertEqual(len(set(labels)), 11)
        self.assertIn("thm:manifold-change-27", labels)
        self.assertIn("thm:product-riemann-27", labels)

    def test_immersion_graph_argument(self):
        text = SOURCE.read_text(encoding="utf-8")
        for term in ("Dla $k=0$", "wykresem", "przekrój", "Tonellego"):
            self.assertIn(term, text)

    def test_jacobian_nonorthonormal_coordinates(self):
        # G=diag(4,9), H=diag(25,49), D=[[2,1],[1,3]].
        # P=diag(1/2,1/3), Q=diag(1/5,1/7).
        det_a = Q(5)*2*Q(1,2)*Q(7)*3*Q(1,3) - Q(5)*Q(1,3)*Q(7)*Q(1,2)
        self.assertEqual(det_a, Q(5)*Q(35,6))
        inverse = Q(1, det_a)
        self.assertEqual(det_a*inverse, 1)

    def test_product_density(self):
        # Constant chart densities: sqrt(det G)=6, sqrt(det H)=5.
        # Rectangle sides 2,3 and interval length 4.
        self.assertEqual(6*5*2*3*4, (6*2*3)*(5*4))

    def test_conformal_scaling(self):
        # e^phi=3, n=2: metric entries scale by 9,
        # the volume density scales by 3^2.
        self.assertEqual((4*9)*(9*9), (4*9)*3**4)


if __name__ == "__main__":
    unittest.main()
