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
        self.assertTrue(all(math.isclose((1/n)*v, n, rel_tol=1e-12, abs_tol=1e-12)
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

    def test_chain_metric_on_finite_translation_group(self):
        # A finite model of the dyadic chain metric in the metrization proof.
        # X=Z/16Z, U_k=2^k Z/16Z (and U_0=X).
        size = 16

        def neighborhood(k):
            return {x for x in range(size) if x % (2**min(k, 4)) == 0}

        for n in range(4):
            v = neighborhood(n+1)
            u = neighborhood(n)
            self.assertTrue(all((a+b+c) % size in u
                                for a in v for b in v for c in v))

        def dyadic_weight(a, b):
            diff = (a-b) % size
            if diff == 0:
                return 0.0
            exponent = 0
            while diff % 2 == 0:
                exponent += 1
                diff //= 2
            return 2.0**(-min(exponent, 4))

        # Minimize the weights over all finite paths (Floyd-Warshall).
        metric = [[dyadic_weight(a, b) for b in range(size)]
                  for a in range(size)]
        for k in range(size):
            for i in range(size):
                for j in range(size):
                    metric[i][j] = min(
                        metric[i][j], metric[i][k] + metric[k][j])

        for a in range(size):
            for b in range(size):
                self.assertEqual(metric[a][b], dyadic_weight(a, b))
                self.assertEqual(metric[a][b], metric[b][a])
                self.assertEqual(metric[a][b], metric[(a+3)%size][(b+3)%size])
                if a != b:
                    self.assertGreater(metric[a][b], 0)
                for c in range(size):
                    self.assertLessEqual(metric[a][c],
                                         metric[a][b]+metric[b][c])
        for n in range(1, 5):
            self.assertTrue(all(metric[x][0] < 2.0**(-n)
                                for x in neighborhood(n+1)))
            self.assertTrue(all(x in neighborhood(n-1)
                                for x in range(size)
                                if metric[x][0] < 2.0**(-n)))

    def test_convex_combinations_of_disjoint_lp_spikes(self):
        # At p=1/2, construct actual finitely supported simple functions.
        # The p-mass of each spike equals 1, while the p-mass of the
        # average of n spikes equals sqrt(n) and grows unbounded.
        p = 0.5
        for n in (4, 9, 16, 25, 36):
            amplitude = n**(1/p)
            spikes = [[amplitude if i == j else 0.0
                       for i in range(n)] for j in range(n)]
            for f in spikes:
                integral_p = sum(abs(v)**p for v in f)/n
                self.assertAlmostEqual(integral_p, 1.0)
            average = [sum(spike[i] for spike in spikes)/n
                       for i in range(n)]
            self.assertAlmostEqual(
                sum(abs(v)**p for v in average)/n, math.sqrt(n))

    def test_product_metric_triangle_and_translation(self):
        def distance(x, y):
            return sum(
                (2.0**(-k))*min(1, abs(x.get(k, 0)-y.get(k, 0)))
                for k in range(1, 41)
            )
        vectors = [
            {}, {1: 1}, {1: -2, 3: 2},
            {2: 0.25, 7: -8}, {35: 1},
        ]
        shift = {1: 5, 3: -8, 7: 2}
        for x in vectors:
            for y in vectors:
                self.assertAlmostEqual(distance(x, y), distance(y, x))
                translated_x = {i: x.get(i, 0)+shift.get(i, 0)
                                for i in set(x) | set(shift)}
                translated_y = {i: y.get(i, 0)+shift.get(i, 0)
                                for i in set(y) | set(shift)}
                self.assertAlmostEqual(distance(x, y),
                                       distance(translated_x, translated_y))
                for z in vectors:
                    self.assertLessEqual(
                        distance(x, z), distance(x, y)+distance(y, z)+1e-14)
        # For any two points, the tail beyond coordinate N is < 2^-N.
        for n in (4, 8, 16, 32):
            from fractions import Fraction
            tail = sum((Fraction(1, 2**k) for k in range(n+1, 200)),
                       Fraction(0))
            self.assertLess(tail, Fraction(1, 2**n))

    def test_empty_operator_family_convention(self):
        self.assertIn(r"\sup_{T\in\mathcal T}\|T\|=0", self.chapter)
        self.assertIn(r"$\sup_{T\in\mathcal T}\|T\|=0$", self.chapter)

    def test_metricization_chain_induction_covers_empty_subchain(self):
        self.assertIn("Pusty podłańcuch", self.chapter)
        self.assertIn(r"U_n+U_n+U_n\subseteq U_{n-1}", self.chapter)


if __name__ == "__main__":
    unittest.main()
