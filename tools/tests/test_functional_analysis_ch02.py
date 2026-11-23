"""Regression tests for Functional Analysis, chapter 02.

Numerical examples supplement, but do not replace, mathematical proof audits.
"""
from __future__ import annotations

from itertools import combinations
from pathlib import Path
import math
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "chapters/pl/functional_analysis"
FILES = {
    "01": BASE / "01-przestrzenie-liniowo-topologiczne-definicje-i-przyklady.tex",
    "02": BASE / "02-podprzestrzenie-produkty-ilorazy-i-topologie-uniwersalne.tex",
    "05": BASE / "05-przestrzenie-lokalnie-wypukle-i-seminormy.tex",
}
BOOK = ROOT / "books/pl/functional_analysis.tex"


class Chapter02Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.texts = {key: value.read_text(encoding="utf-8") for key, value in FILES.items()}
        cls.text = cls.texts["02"]

    def test_import_and_chapter_context(self):
        book = BOOK.read_text(encoding="utf-8")
        for key in ("01", "02", "05"):
            self.assertIn(r"\input{../../" + str(FILES[key].relative_to(ROOT)) + "}", book)
        self.assertIn(r"\setcounter{section}{1}", self.text)

    def test_environments(self):
        for env, expected in (("proof", 14), ("przyklad", 7)):
            self.assertEqual(self.text.count(r"\begin{" + env + "}"), expected)
            self.assertEqual(self.text.count(r"\end{" + env + "}"), expected)
        for env in ("definicja", "twierdzenie", "stwierdzenie", "lemat", "wniosek", "uwaga"):
            self.assertEqual(self.text.count(r"\begin{" + env + "}"),
                             self.text.count(r"\end{" + env + "}"))

    def test_labels_and_references(self):
        labels = re.findall(r"\\label\{([^}]+)\}", self.text)
        self.assertEqual(len(labels), 15)
        self.assertEqual(len(set(labels)), len(labels))
        all_labels = set()
        for source in self.texts.values():
            all_labels.update(re.findall(r"\\label\{([^}]+)\}", source))
        refs = (re.findall(r"\\ref\{([^}]+)\}", self.text)
                + re.findall(r"\\hyperref\[([^]]+)\]", self.text))
        for ref in refs:
            self.assertIn(ref, all_labels)
        for label in ("sec:tvs", "sec:lokalnie-wypukle", "thm:final-tvs",
                      "thm:quotient-norm", "thm:hausdorffization"):
            self.assertIn(label, all_labels)

    def test_terminology(self):
        prose = re.sub(r"\\(?:label|ref)\{[^}]+\}", "", self.text)
        prose = re.sub(r"\\hyperref\[[^]]+\]", "", prose)
        self.assertIsNone(re.search(r"(?<![\w-])dual(?:u)?(?![\w-])", prose))
        self.assertIsNone(re.search(r"\brodziny map\b", prose))
        self.assertNotIn(r"\mathbf1", prose)

    def test_product_weak_versus_uniform_convergence(self):
        for n in range(2, 110):
            center, radius = 1/n, 1/(n*n)
            self.assertGreater(center-radius, 0)
            self.assertLess(center+radius, 1)
            self.assertEqual(max(0, 1-n*n*abs(center-1/n)), 1)
        for t in (0.0, 0.1, 0.25, 0.75, 1.0):
            vals = [max(0, 1-n*n*abs(t-1/n)) for n in range(300, 400)]
            self.assertEqual(vals, [0]*len(vals))

    def test_product_bounded_finite_coordinates(self):
        for dim in range(1, 7):
            points = [tuple(k/(i+1) for i in range(dim)) for k in range(-4, 5)]
            projected = [max(abs(x[i]) for x in points) for i in range(dim)]
            self.assertTrue(all(math.isfinite(v) for v in projected))
            self.assertEqual(max(max(abs(x[i]) for i in range(dim)) for x in points),
                             max(projected))

    def test_quotient_norm_r2_by_horizontal_axis(self):
        # Euclidean X=R^2, M=R x {0}: distance of (a,b) to M is |b|.
        for a in (-4, 0, 2, 6):
            for b in (-3, -1, 0, 5):
                candidate = math.sqrt((a-a)**2+b*b)
                for m in (-5, -1, 0, 2, 7):
                    self.assertLessEqual(candidate, math.hypot(a-m, b)+1e-12)
                self.assertEqual(candidate, abs(b))

    def test_final_set_topology_cross_is_not_vector(self):
        # Final topology for the two axis embeddings on R^2:
        # singleton (1,1) has empty inverse images, singleton (0,0) does not.
        def preimages(point):
            x, y = point
            on_first = x if y == 0 else None
            on_second = y if x == 0 else None
            return on_first, on_second
        self.assertEqual(preimages((1, 1)), (None, None))
        self.assertEqual(preimages((0, 0)), (0, 0))

    def test_diagonal_quotient_norm_and_triangle(self):
        # For M=span((1,1)) in Euclidean R^2, dist((a,b), M)=|a-b|/sqrt(2).
        from itertools import product
        for a, b in product(range(-3, 4), repeat=2):
            quotient_norm = abs(a-b) / math.sqrt(2)
            closest = (a+b)/2
            self.assertTrue(math.isclose(
                math.hypot(a-closest, b-closest), quotient_norm,
                rel_tol=1e-12, abs_tol=1e-12,
            ))
            for t in (-7, -1, 0, 0.5, 2, 8):
                self.assertLessEqual(
                    quotient_norm, math.hypot(a-t, b-t)+1e-12
                )
        for a, b, c, d in product(range(-2, 3), repeat=4):
            left = abs((a+c)-(b+d))
            right = abs(a-b) + abs(c-d)
            self.assertLessEqual(left, right)

    def test_nonclosed_subspace_has_nonseparating_quotient_seminorm(self):
        # x=(2^-n)_{n>=1} belongs to l2 but not c00.
        # Its distance to c00 is zero, because finite truncations converge.
        tail_norms = [
            math.sqrt((4.0**(-(n+1)))/(1-0.25))
            for n in range(1, 40)
        ]
        self.assertTrue(all(v > 0 for v in tail_norms))
        self.assertTrue(all(x > y for x, y in zip(tail_norms, tail_norms[1:])))
        self.assertLess(tail_norms[-1], 1e-10)

    def test_product_functional_requires_finitely_many_coordinates(self):
        indices = tuple(range(5))
        for number in range(len(indices)):
            for restricted in combinations(indices, number):
                j = next(i for i in indices if i not in restricted)
                # No coordinate constraint on j can control L(x)=3*x_j.
                for scale in (1.0, 10.0, 100.0):
                    vector = {j: scale}
                    self.assertTrue(all(vector.get(i, 0) == 0
                                        for i in restricted))
                    self.assertGreater(abs(3*vector[j]), 1)

    def test_direct_sum_topologies_e_n(self):
        # In product topology e_n converges coordinatewise to 0,
        # whereas the seminorm p_(1,1,...) has value 1.
        for n in range(1, 200):
            e_n = {n: 1}
            for j in range(1, n):
                self.assertEqual(e_n.get(j, 0), 0)
            self.assertEqual(sum(abs(v) for v in e_n.values()), 1)


if __name__ == "__main__":
    unittest.main()
