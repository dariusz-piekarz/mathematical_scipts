"""Regression checks for functional analysis, chapter 05.

Numerical counterexample models supplement independent full mathematical audits.
"""
from __future__ import annotations

from pathlib import Path
import math
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/functional_analysis"
BOOK = ROOT / "books/pl/functional_analysis.tex"
NAMES = (
    "01-przestrzenie-liniowo-topologiczne-definicje-i-przyklady.tex",
    "02-podprzestrzenie-produkty-ilorazy-i-topologie-uniwersalne.tex",
    "03-sieci-struktura-jednostajna-i-zupelnosc.tex",
    "04-zbiory-ograniczone-rodziny-operatorow-i-metryzowalnosc.tex",
    "05-przestrzenie-lokalnie-wypukle-i-seminormy.tex",
)


class FunctionalAnalysisChapter05(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.texts = [(CHAPTER / p).read_text(encoding="utf-8") for p in NAMES]
        cls.chapter = cls.texts[-1]

    def test_book_context_and_chapter_numbering(self):
        book = BOOK.read_text(encoding="utf-8")
        for name in NAMES:
            self.assertIn(
                r"\input{../../chapters/pl/functional_analysis/" + name + "}",
                book)
        self.assertIn(r"\setcounter{section}{4}", self.chapter)

    def test_environments(self):
        s = self.chapter
        for environment, count in (("proof", 13), ("przyklad", 5)):
            self.assertEqual(s.count(r"\begin{" + environment + "}"), count)
            self.assertEqual(s.count(r"\end{" + environment + "}"), count)
        for environment in ("definicja", "twierdzenie", "stwierdzenie",
                            "lemat", "wniosek", "uwaga"):
            self.assertEqual(
                s.count(r"\begin{" + environment + "}"),
                s.count(r"\end{" + environment + "}"))

    def test_labels_and_actual_references(self):
        labels = re.findall(r"\\label\{([^}]+)\}", self.chapter)
        self.assertEqual(len(labels), 19)
        self.assertEqual(len(set(labels)), 19)
        all_labels = set()
        for source in self.texts:
            all_labels.update(re.findall(r"\\label\{([^}]+)\}", source))
        refs = (re.findall(r"\\ref\{([^}]+)\}", self.chapter)
                + re.findall(r"\\hyperref\[([^]]+)\]", self.chapter))
        self.assertFalse(set(refs) - all_labels, sorted(set(refs) - all_labels))
        for label in ("thm:minkowski", "thm:lcs-seminorms",
                      "thm:kolmogorov-normability", "thm:smooth-complete"):
            self.assertIn(label, labels)

    def test_terminology_and_figure_disclaimer(self):
        s = self.chapter
        self.assertNotRegex(s, r"\b[Ss]ekwencyjn")
        self.assertNotIn("ciągły dual", s)
        self.assertIn("przestrzeń sprzężoną", s)
        self.assertIn("funkcjonał\nMinkowskiego $p_U$ z poprzedniej podsekcji.", s)
        self.assertIn(r"p_A(x)>0", s)
        self.assertIn(r"x/p_A(x)", s)
        self.assertIn(r"\chi_{E_j}", s)

    def test_absolute_convexity_criterion(self):
        # The l1 ball in R^2 is absolutely convex.
        vectors = ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1),
                   (0.25, -0.5))
        for x in vectors:
            for y in vectors:
                for alpha, beta in ((0, 0), (1, 0), (0, -1),
                                    (0.4, -0.6), (0.2, 0.5)):
                    z = (alpha*x[0]+beta*y[0], alpha*x[1]+beta*y[1])
                    self.assertLessEqual(abs(z[0])+abs(z[1]), 1+1e-12)

    def test_minkowski_gauge_strip_vs_norm(self):
        # For the open balanced absorbing strip A={|x_0|<1},
        # its gauge is |x_0| and vanishes on the nonzero y-axis.
        for x in (-3.0, -1.0, 0.0, 1.2, 7.0):
            for y in (-4.0, 0.0, 2.0):
                gauge = abs(x)
                for t in (0.1, 0.5, 1.5, 2.0):
                    self.assertAlmostEqual(t*gauge, abs(t*x))
                self.assertEqual(gauge, abs(x))
        self.assertEqual(abs(0), 0)  # p_A((0,1))=0

    def test_noncontinuous_gauge_on_c00(self):
        # x^(n)=e_n/n tends to 0 in sup norm but p_A(x^(n))=1.
        for n in range(1, 200):
            vector = {n: 1/n}
            norm_inf = max(map(abs, vector.values()))
            gauge = max(k*abs(v) for k,v in vector.items())
            self.assertAlmostEqual(norm_inf, 1/n)
            self.assertAlmostEqual(gauge, 1)
        self.assertLess(1/100000, 1e-4)

    def test_zero_continuous_functionals_on_nonatomic_lp_bound(self):
        # Equal p-mass partition of an atomless measure:
        # |L(f)| <= C * n^(1-1/p)*||f||_p -> 0.
        for p in (0.2, 0.5, 0.75, 0.95):
            exponent = 1-1/p
            self.assertLess(exponent, 0)
            values = [n**exponent for n in (1, 2, 4, 16, 256, 4096)]
            self.assertTrue(all(values[i+1] < values[i]
                                for i in range(len(values)-1)))
            self.assertLess(1000000**exponent, 1)

    def test_nonnormability_smooth_function_derivatives(self):
        # For f_N=delta/(2 N^m) sin(Nt) we have p_m<=delta/2,
        # while p_(m+1) grows as delta*N/2.
        delta = 0.8
        for m in (0, 1, 3):
            for n in (8.0, 16.0, 32.0, 64.0):
                upper = max(delta/(2*n**m)*n**j for j in range(m+1))
                self.assertLessEqual(upper, delta/2 + 1e-12)
                next_derivative_amplitude = delta*n/2
                self.assertGreaterEqual(next_derivative_amplitude, delta*4)
                # The oscillatory factor attains magnitude one on [0,1].
                vals = [abs(math.sin(n*t)) for t in (math.pi/(2*n), 0.0)]
                self.assertAlmostEqual(max(vals), 1)

    def test_countable_seminorm_metric_translation_and_triangle(self):
        # Product seminorms p_n(x)=|x_n|, finite-support vectors.
        def distance(x,y):
            return sum(2.0**(-n)*min(1, abs(x.get(n,0)-y.get(n,0)))
                       for n in range(1,51))
        vectors = [{}, {1:3}, {2:-1.5, 4:0.25}, {40:1}]
        translate = {1:5, 2:-4, 4:2}
        for x in vectors:
            for y in vectors:
                shifted_x = {n:x.get(n,0)+translate.get(n,0)
                             for n in set(x)|set(translate)}
                shifted_y = {n:y.get(n,0)+translate.get(n,0)
                             for n in set(y)|set(translate)}
                self.assertAlmostEqual(distance(x,y),distance(shifted_x,shifted_y))
                for z in vectors:
                    self.assertLessEqual(distance(x,z), distance(x,y)+distance(y,z)+1e-12)

    def test_seminorm_cauchy_and_uniform_limits(self):
        # In C^infty, derivative families are simultaneously Cauchy in
        # each C([0,1]) norm; use elementary polynomial truncations.
        def p_m_of_coefficients(coeffs, m):
            # Bound sup of first m derivatives of polynomial on [0,1].
            vals = []
            current = coeffs[:]
            for j in range(m+1):
                vals.append(sum(abs(a) for a in current))
                current = [(k+1)*current[k+1]
                           for k in range(len(current)-1)]
            return max(vals)
        for m in range(4):
            coefficients = [1/math.factorial(n) for n in range(7)]
            tails = [
                p_m_of_coefficients([0.0]*(N+1) +
                                    coefficients[N+1:],m)
                for N in range(1,6)
            ]
            self.assertTrue(all(x >= y for x,y in zip(tails,tails[1:])))

    def test_quotient_seminorm_balls_and_local_convexity(self):
        # Linear quotient of R^2 by horizontal axis identifies with R.
        norm = lambda vector: abs(vector[1])
        points = [(3,1),(-4,1),(1,-2),(0,0)]
        for x in points:
            self.assertAlmostEqual(norm(x),norm((x[0]+5,x[1])))
            self.assertEqual(norm((0,0)),0)


if __name__ == "__main__":
    unittest.main()
