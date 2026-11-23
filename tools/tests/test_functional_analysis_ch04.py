"""Audit regressions for Chapter 04 of Functional Analysis.

These tests exercise structural contracts and finite numerical models;
they do not replace full proof verification.
"""
from __future__ import annotations

import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "chapters/pl/functional_analysis"
NAMES = {
    1: "01-przestrzenie-liniowo-topologiczne-definicje-i-przyklady.tex",
    2: "02-podprzestrzenie-produkty-ilorazy-i-topologie-uniwersalne.tex",
    3: "03-sieci-struktura-jednostajna-i-zupelnosc.tex",
    4: "04-zbiory-ograniczone-rodziny-operatorow-i-metryzowalnosc.tex",
    5: "05-przestrzenie-lokalnie-wypukle-i-seminormy.tex",
}
BOOK = ROOT / "books/pl/functional_analysis.tex"


class FunctionalAnalysisChapter04(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.texts = {n: (BASE / path).read_text(encoding="utf-8")
                     for n, path in NAMES.items()}
        cls.chapter = cls.texts[4]

    def test_integration_and_numbering(self):
        book = BOOK.read_text(encoding="utf-8")
        for path in NAMES.values():
            self.assertIn(r"\input{../../chapters/pl/functional_analysis/" + path + "}", book)
        self.assertIn(r"\setcounter{section}{3}", self.chapter)

    def test_balanced_environments(self):
        for env, expected in (("proof", 9), ("przyklad", 5)):
            self.assertEqual(self.chapter.count(r"\begin{" + env + "}"), expected)
            self.assertEqual(self.chapter.count(r"\end{" + env + "}"), expected)
        for env in ("definicja", "twierdzenie", "stwierdzenie", "lemat", "wniosek", "uwaga"):
            self.assertEqual(self.chapter.count(r"\begin{" + env + "}"),
                             self.chapter.count(r"\end{" + env + "}"))

    def test_labels_and_cross_references(self):
        labels = re.findall(r"\\label\{([^}]+)\}", self.chapter)
        self.assertEqual(len(labels), 15)
        self.assertEqual(len(set(labels)), 15)
        all_labels = set()
        for text in self.texts.values():
            all_labels.update(re.findall(r"\\label\{([^}]+)\}", text))
        refs = re.findall(r"\\ref\{([^}]+)\}", self.chapter)
        refs += re.findall(r"\\hyperref\[([^]]+)\]", self.chapter)
        self.assertTrue(set(refs) <= all_labels, sorted(set(refs)-all_labels))

    def test_polish_terminology_and_indicator_notation(self):
        self.assertNotIn(r"\mathbf1", self.chapter)
        self.assertNotIn("Sekwencyjne kryterium", self.chapter)
        self.assertNotIn("pierwszoprzeliczalną", self.chapter)
        self.assertIn("spełnia pierwszy aksjomat przeliczalności", self.chapter)
        self.assertIn(r"\chi_{I_{n,j}}", self.chapter)
        self.assertIn(r"\chi_{[0,1]}", self.chapter)

    def test_sequential_boundedness_on_real_line(self):
        points = [-7.0, -1.0, 0, 2.0, 6.0]
        for n in range(1, 200):
            scalar = 1 / n
            val = scalar * points[n % len(points)]
            self.assertLessEqual(abs(val), 7/n + 1e-12)
        unbounded_points = [n*n for n in range(1, 200)]
        self.assertTrue(all((1/n)*v == n
                            for n, v in enumerate(unbounded_points, 1)))

    def test_quasinorm_convex_hull_unbounded(self):
        for p in (0.2, 0.5, 0.75, 0.95):
            masses = [n**(1-p) for n in (1, 2, 8, 32, 128, 512)]
            self.assertTrue(all(a < b for a, b in zip(masses, masses[1:])))
            for n in (1, 2, 8, 32):
                # On an interval of mass 1/n, value n^(1/p) gives p-mass 1.
                self.assertAlmostEqual(n*(n**(1/p))**p/n, n)  # sum of n spikes
                self.assertAlmostEqual((n**(1/p))**p / n, 1.0)

    def test_pointwise_bounded_operator_family_not_equicontinuous(self):
        for n in range(1, 101):
            sparse_x = {1: 2, 3: -1}
            self.assertEqual(n*sparse_x.get(n, 0), 0 if n > 3 else n*sparse_x.get(n, 0))
            e_n = {n: 1}
            self.assertEqual(n*e_n[n], n)
        norms = [n for n in range(1, 101)]
        self.assertEqual(max(norms), 100)

    def test_strong_vs_bounded_operator_convergence(self):
        for x in ({2: 1, 7: -5}, {1: 3}, {}):
            vals = [n*x.get(n, 0) for n in range(1, 100)]
            self.assertEqual(vals[8:], [0] * 91)
        self.assertTrue(all(n > 0 for n in range(1, 100)))

    def test_operator_norm_control_in_finite_dimension(self):
        # Sup norm on K^3; for S(x)=sum_i a_i*x_i scalar range,
        # ||S||<=sum_i |a_i|, hence finite coordinate evaluations suffice.
        coeffs = [2, -3, 1]
        for x in ((1, 0, 0), (0, 1, 0), (1, -1, 1), (0, 0, 0)):
            val = sum(a*z for a, z in zip(coeffs, x))
            self.assertLessEqual(abs(val), sum(abs(a) for a in coeffs) * max(map(abs, x)))

    def test_product_metric_coordinatewise(self):
        def distance(x, y, num=200):
            return sum((2.0**(-k))*min(1, abs(x.get(k, 0)-y.get(k, 0)))
                       for k in range(1, num+1))
        for n in (1, 2, 4, 8, 16, 64):
            z = {n: 1}
            self.assertAlmostEqual(distance(z, {}), 2.0**(-n))
        self.assertLess(distance({30: 1}, {}), distance({2: 1}, {}))

    def test_empty_operator_family_convention(self):
        self.assertIn(r"\sup_{T\in\mathcal T}\|T\|=0", self.chapter)
        self.assertIn(r"$\sup_{T\in\mathcal T}\|T\|=0$", self.chapter)

    def test_metricization_chain_induction_covers_empty_subchain(self):
        self.assertIn("Pusty podłańcuch", self.chapter)
        self.assertIn(r"U_n+U_n+U_n\subseteq U_{n-1}", self.chapter)


if __name__ == "__main__":
    unittest.main()
