"""Chapter 01 structural and elementary-model regression tests.

These checks do not replace independent mathematical proof review or PDF inspection.
"""
from __future__ import annotations

from pathlib import Path
import math
import random
import re
import unittest


ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/functional_analysis/01-przestrzenie-liniowo-topologiczne-definicje-i-przyklady.tex"
BOOK = ROOT / "books/pl/functional_analysis.tex"


class FunctionalAnalysisChapter01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.chapter = CHAPTER.read_text(encoding="utf-8")
        cls.book = BOOK.read_text(encoding="utf-8")

    def test_integration_into_book(self) -> None:
        self.assertIn(
            r"\input{../../chapters/pl/functional_analysis/01-przestrzenie-liniowo-topologiczne-definicje-i-przyklady.tex}",
            self.book,
        )

    def test_proof_inventory_and_environments(self) -> None:
        text = self.chapter
        self.assertEqual(text.count(r"\begin{proof}"), 9)
        self.assertEqual(text.count(r"\end{proof}"), 9)
        self.assertEqual(text.count(r"\begin{przyklad}"), 7)
        self.assertEqual(text.count(r"\end{przyklad}"), 7)
        for name in ("twierdzenie", "stwierdzenie", "lemat", "wniosek", "definicja", "uwaga"):
            self.assertEqual(text.count(r"\begin{" + name + "}"), text.count(r"\end{" + name + "}"))

    def test_labels_and_refs(self) -> None:
        labels = re.findall(r"\\label\{([^}]+)\}", self.chapter)
        refs = re.findall(r"\\ref\{([^}]+)\}", self.chapter)
        self.assertEqual(len(labels), 15)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertEqual(len(refs), 4)
        self.assertTrue(set(refs).issubset(set(labels)))

    def test_indicator_convention(self) -> None:
        self.assertNotIn(r"\mathbf1", self.chapter)
        self.assertIn(r"\chi_A", self.chapter)
        self.assertIn(r"\chi_{A_i}", self.chapter)
        self.assertIn(r"f\chi_", self.chapter)

    def test_l_p_triangle_inequality_numeric(self) -> None:
        rng = random.Random(1142)
        for p in (0.2, 0.5, 0.8):
            for _ in range(1000):
                x, y, z = [rng.uniform(-3, 3) for _ in range(3)]
                self.assertLessEqual(
                    abs(x-z)**p,
                    abs(x-y)**p + abs(y-z)**p + 1e-12,
                )
            self.assertLess(1-1/p, 0)

    def test_balanced_nonconvex_example_witness(self) -> None:
        def in_a(x: float, y: float) -> bool:
            return (abs(x) <= 1 and abs(y) <= 1) or (
                abs(x) <= 2 and abs(y) <= .5
            )
        self.assertTrue(in_a(1, 1))
        self.assertTrue(in_a(2, .5))
        self.assertFalse(in_a(1.5, .75))
        for x, y in ((1, 1), (2, .5)):
            for scale in (-1, -.25, 0, .3, 1):
                self.assertTrue(in_a(scale*x, scale*y))

    def test_spike_l1_norm_formula(self) -> None:
        for n in (1, 2, 3, 10, 100):
            self.assertTrue(math.isclose(.5/n, 1/(2*n)))


if __name__ == "__main__":
    unittest.main()
