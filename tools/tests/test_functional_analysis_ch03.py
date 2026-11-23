"""Functional analysis chapter 03: net/filter/completion regression tests.

These checks are auxiliary; proofs and topology are audited independently.
"""
from __future__ import annotations

import math
import re
import unittest
from itertools import product
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


class FunctionalAnalysisChapter03(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.texts = {n: (BASE / name).read_text(encoding="utf-8")
                     for n, name in NAMES.items()}
        cls.chapter = cls.texts[3]

    def test_book_integration(self):
        book = BOOK.read_text(encoding="utf-8")
        for n, name in NAMES.items():
            self.assertIn(r"\input{../../chapters/pl/functional_analysis/" + name + "}", book)
        self.assertIn(r"\setcounter{section}{2}", self.chapter)

    def test_proofs_examples_and_environments(self):
        text = self.chapter
        for env, count in (("proof", 9), ("przyklad", 3)):
            self.assertEqual(text.count(r"\begin{" + env + "}"), count)
            self.assertEqual(text.count(r"\end{" + env + "}"), count)
        for env in ("definicja", "twierdzenie", "stwierdzenie", "lemat", "wniosek", "uwaga"):
            self.assertEqual(text.count(r"\begin{" + env + "}"),
                             text.count(r"\end{" + env + "}"))

    def test_labels_references(self):
        labels = re.findall(r"\\label\{([^}]+)\}", self.chapter)
        self.assertEqual(len(labels), 15)
        self.assertEqual(len(set(labels)), len(labels))
        all_labels = set().union(*[
            set(re.findall(r"\\label\{([^}]+)\}", text))
            for text in self.texts.values()
        ])
        refs = re.findall(r"\\ref\{([^}]+)\}", self.chapter)
        refs += re.findall(r"\\hyperref\[([^]]+)\]", self.chapter)
        self.assertTrue(set(refs).issubset(all_labels), sorted(set(refs)-all_labels))
        for label in ("thm:filter-cauchy", "thm:tvs-completion",
                      "prop:completion-criterion", "ex:sigma-net"):
            self.assertIn(label, labels)

    def test_terminology_and_corrected_notation(self):
        self.assertNotRegex(self.chapter, r"\b[Ss]ekwencyjn")
        self.assertIn("Przestrzeń ciągowo zupełna, ale niezupełna", self.chapter)
        self.assertIn(r"$y_e+W_0\subseteq V$", self.chapter)
        self.assertNotIn(r"$y_e+W_e\subseteq V$", self.chapter)

    def test_finite_set_directed_system(self):
        # All subsets of {0,...,m-1}, directed by inclusion.
        for m in range(1, 7):
            sets = [frozenset(i for i in range(m) if mask & (1 << i))
                    for mask in range(1 << m)]
            for a in sets:
                for b in sets:
                    upper = a | b
                    self.assertIn(upper, sets)
                    self.assertTrue(a <= upper and b <= upper)

    def test_filter_tail_construction(self):
        # Fréchet filter on finite directed tails has the filter property.
        for n in range(2, 24):
            tails = [set(range(k, n)) for k in range(n)]
            for a in tails:
                for b in tails:
                    self.assertIn(a & b, tails)
                    self.assertTrue(a & b)

    def test_entourage_inverse_and_composition(self):
        points = range(-6, 7)
        eps = 3
        E = {(x, y) for x, y in product(points, repeat=2) if abs(x-y) < eps}
        self.assertTrue(all((x,x) in E for x in points))
        self.assertEqual({(y,x) for x,y in E}, E)
        V = {(x, y) for x, y in product(points, repeat=2) if abs(x-y) < eps/2}
        for (x,y) in V:
            for (a,z) in V:
                if y == a:
                    self.assertIn((x,z), E)

    def test_moving_finite_support_converges_coordinatewise(self):
        # e_n -> 0 in the product topology but not in the l1 norm.
        for n in range(1, 150):
            x = {n: 1}
            for coordinate in range(1, n):
                self.assertEqual(x.get(coordinate, 0), 0)
            self.assertEqual(sum(abs(v) for v in x.values()), 1)

    def test_ell_two_finite_truncation_approximates(self):
        # x_n=2^-n is in l2 and truncations in c00 converge.
        errors = []
        for N in range(1, 30):
            error = math.sqrt(sum(4.0 ** (-n) for n in range(N + 1, 300)))
            errors.append(error)
        self.assertTrue(all(errors[i+1] < errors[i] for i in range(len(errors)-1)))
        self.assertLess(errors[-1], 1e-8)

    def test_completion_open_neighborhood_representatives(self):
        # Equivalent sequences 1 +/- 1/n have the same limit.
        # Only 1-1/n is eventually inside (-1,1), but neither
        # admits a fixed-radius margin to the boundary.
        for n in range(2, 500):
            self.assertLess(1 - 1/n, 1)
            self.assertGreater(1 + 1/n, 1)
        for eps in (0.1, 0.01, 0.001):
            n = math.ceil(2/eps)
            self.assertGreater(1 - 1/n + eps, 1)
        self.assertEqual(len({1.0, float(1)}), 1)


if __name__ == "__main__":
    unittest.main()
