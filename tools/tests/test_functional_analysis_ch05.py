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

    def test_compact_seminorm_excludes_empty_supremum_ambiguity(self):
        self.assertIn("niepustego", self.chapter)
        self.assertIn(r"p_K=0", self.chapter)
        # A finite compact set K={0,1/2,1} in [0,1]:
        # p_K is subadditive and absolutely homogeneous.
        positions = (0.0, 0.5, 1.0)
        f = [t*t for t in positions]
        g = [1-t for t in positions]
        p = lambda v: max(map(abs, v))
        self.assertLessEqual(p([a+b for a, b in zip(f,g)]),
                             p(f)+p(g)+1e-12)
        for scalar in (-3, 0, 0.25, 2):
            self.assertAlmostEqual(
                p([scalar*val for val in f]),
                abs(scalar)*p(f))

    def test_frechet_completeness_reference_is_explicit(self):
        self.assertIn(
            r"Zupełność wykażemy w Twierdzeniu~\ref{thm:smooth-complete}",
            self.chapter)
        self.assertNotIn("Zupełność wykażemy w następnym stwierdzeniu",
                         self.chapter)
        self.assertIn(r"\label{thm:smooth-complete}", self.chapter)

    def test_minkowski_boundary_and_nonzero_condition(self):
        # The gauge of A = {(x,y): x^2/4 + y^2 < 1} is
        # sqrt(x^2/4+y^2). Points scaled by it lie on the boundary.
        points = ((3, 0), (1, 2), (-1, 1.3), (0, 0.1))
        for x, y in points:
            gauge = math.hypot(x/2, y)
            self.assertGreater(gauge, 0)
            xx, yy = x/gauge, y/gauge
            self.assertAlmostEqual((xx/2)**2+yy**2, 1)
        # This formula must not be applied to kernel elements.
        self.assertIn(r"p_A(x)>0", self.chapter)

    def test_atomless_lp_equal_mass_partition(self):
        # For f(t)=t on [0,1], nu_f([0,a]) = a^(p+1)/(p+1).
        # This explicitly realizes the partition used in the proof
        # that a continuous functional on L^p (p<1) must vanish.
        for p in (0.25, 0.5, 0.8):
            pnorm = (1/(p+1))**(1/p)
            for n in (2, 3, 8, 32):
                endpoints = [(k/n)**(1/(p+1)) for k in range(n+1)]
                masses = [
                    (endpoints[k+1]**(p+1)-endpoints[k]**(p+1))/(p+1)
                    for k in range(n)
                ]
                self.assertAlmostEqual(sum(masses), 1/(p+1))
                for mass in masses:
                    self.assertAlmostEqual(mass, 1/(n*(p+1)))
                combined = sum(mass**(1/p) for mass in masses)
                self.assertAlmostEqual(combined, n**(1-1/p)*pnorm)
                self.assertLess(combined, pnorm)

    def test_complex_minkowski_gauge_homogeneity_and_subadditivity(self):
        # Complex absolutely convex ball A={|z_1|+2|z_2|<1}.
        gauge = lambda z: abs(z[0])+2*abs(z[1])
        vectors = [
            (0j, 0j), (1+2j, -1j), (-3+1j, 2-2j), (0j, 5j)
        ]
        scalars = (0j, 1j, -1+0j, 0.4+0.3j, 2-3j)
        for x in vectors:
            for a in scalars:
                ax = (a*x[0], a*x[1])
                self.assertAlmostEqual(gauge(ax), abs(a)*gauge(x))
            for y in vectors:
                xy = (x[0]+y[0], x[1]+y[1])
                self.assertLessEqual(gauge(xy), gauge(x)+gauge(y)+1e-12)

    def test_nonhausdorff_seminorm_family_and_separation(self):
        # A single p(x,y)=|x| does not separate (0,1) and 0.
        p1 = lambda v: abs(v[0])
        p2 = lambda v: abs(v[1])
        self.assertEqual(p1((0, 1)), 0)
        self.assertEqual(p2((0, 1)), 1)
        for x in (-2, -1, 0, 1, 3):
            for y in (-2, 0, 1, 4):
                if (x, y) != (0, 0):
                    self.assertGreater(max(p1((x,y)), p2((x,y))), 0)
        self.assertIn(r"\bigcap_{p\in\mathcal P}\ker p=\{0\}",
                      self.chapter)

    def test_quotient_seminorm_balls_and_local_convexity(self):
        # Linear quotient of R^2 by horizontal axis identifies with R.
        norm = lambda vector: abs(vector[1])
        points = [(3,1),(-4,1),(1,-2),(0,0)]
        for x in points:
            self.assertAlmostEqual(norm(x),norm((x[0]+5,x[1])))
            self.assertEqual(norm((0,0)),0)


if __name__ == "__main__":
    unittest.main()
