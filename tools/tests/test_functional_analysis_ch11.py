"""Regression contracts for functional analysis chapter 11 (standard library only)."""
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTERS = ROOT / "chapters/pl/functional_analysis"
SOURCE = CHAPTERS / "11-przestrzenie-frecheta-twierdzenia-o-odwzorowaniu-otwartym-i-wykresie-domknietym.tex"


class Chapter11Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")

    def test_source_and_core_theorems(self):
        self.assertIn(r"\label{thm:open-mapping11}", self.source)
        self.assertIn(r"\label{thm:closed-graph11}", self.source)
        self.assertIn(r"\label{thm:frechet-stability11}", self.source)
        self.assertIn(r"\label{cor:inverse-mapping11}", self.source)

    def test_environment_balancing(self):
        for environment in ("proof", "definicja", "twierdzenie", "stwierdzenie",
                            "wniosek", "lemat", "przyklad", "uwaga", "center",
                            "tikzpicture", "enumerate"):
            self.assertEqual(
                self.source.count(r"\begin{" + environment + "}"),
                self.source.count(r"\end{" + environment + "}"),
                environment,
            )
        self.assertEqual(self.source.count(r"\begin{proof}"), 10)
        self.assertEqual(self.source.count(r"\begin{przyklad}"), 6)
        self.assertEqual(self.source.count(r"\begin{tikzpicture}"), 1)

    def test_labels_and_references_in_actual_context(self):
        chapter_sources = [
            next(CHAPTERS.glob(f"{number:02d}-*.tex")).read_text(encoding="utf-8")
            for number in range(1, 12)
        ]
        labels = [
            label
            for source in chapter_sources
            for label in re.findall(r"\\label\{([^}]+)\}", source)
        ]
        self.assertEqual(len(labels), len(set(labels)))
        references = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", self.source)
        references += re.findall(r"\\hyperref\[([^\]]+)\]", self.source)
        self.assertEqual(len(references), 16)
        self.assertEqual([], sorted(set(references) - set(labels)))

    def test_convention_for_cauchy_sequences(self):
        self.assertNotRegex(self.source, r"\bsekwencj\w*|\bsekwencyjn\w*")
        self.assertIn("ciągów Cauchy'ego", self.source)
        self.assertIn("kanonicznej struktury jednostajnej", self.source)

    def test_complete_smooth_functions_uses_integral_identity(self):
        self.assertIn(r"g_j'=g_{j+1}", self.source)
        self.assertIn(r"g_0\in C^\infty([0,1])", self.source)
        self.assertIn(r"\int_{[0,t]}f_n^{(j+1)}", self.source)
        self.assertIn(r"p_m(f_n-g_0)\to0", self.source)

    def test_frechet_metric_is_finite(self):
        # Finite truncation of sum 2^-n min(1,p_n(x-y)) is bounded by 1.
        for x in ((0, 0, 0), (1, -2, 3), (-1, 0, 4)):
            for y in ((0, 0, 0), (1, -2, 3), (-1, 0, 4)):
                seminorms = [max(abs(x[k]-y[k]) for k in range(n)) for n in (1, 2, 3)]
                distance = sum(2**(-n) * min(1, p) for n, p in enumerate(seminorms, 1))
                self.assertGreaterEqual(distance, 0)
                self.assertLess(distance, 1)
                if x == y:
                    self.assertEqual(distance, 0)
                else:
                    self.assertGreater(distance, 0)

    def test_quotient_metric_example(self):
        # R^2 / ({0} x R), quotient metric of sup norm is |x_1 - y_1|.
        for a, b in ((2.0, -3.0), (-1.25, 2.75), (0.0, 0.0)):
            candidates = [max(abs(a-b), abs(t)) for t in (-100, -1, 0, 1, 100)]
            self.assertAlmostEqual(min(candidates), abs(a-b))
        self.assertIn(r"\bar d", self.source)

    def test_baire_open_mapping_construction(self):
        self.assertIn(r"U_n+U_n\subseteq U_{n-1}", self.source)
        self.assertIn(r"V_n\subseteq\overline{T(U_n)}", self.source)
        self.assertIn(r"\sum_{k=m}^N x_k\in U_{m-1}", self.source)
        self.assertIn(r"\overline{U_0}\subseteq U", self.source)

    def test_inverse_mapping_requires_surjectivity(self):
        self.assertRegex(self.source, r"ciągłym i surjektywnym")
        self.assertIn(r"\label{cor:inverse-mapping11}", self.source)
        self.assertIn(r"\label{cor:quotient-open11}", self.source)

    def test_closed_graph_full_domain(self):
        self.assertIn(r"T:E\to F", self.source)
        self.assertIn(r"G(T)\subseteq E\times F", self.source)
        self.assertIn(r"T=\pi_F\circ P^{-1}", self.source)
        self.assertIn(r"D(T)\ne E", self.source)

    def test_incomplete_codomain_counterexample(self):
        for n in (1, 4, 16, 64, 256):
            entries = [1/n] * n
            l1 = sum(abs(z) for z in entries)
            l2 = math.sqrt(sum(z*z for z in entries))
            self.assertAlmostEqual(l1, 1)
            self.assertAlmostEqual(l2, 1/math.sqrt(n))

    def test_dense_nonclosed_embedding(self):
        self.assertIn(r"(n^{-3/4})_{n\ge1}", self.source)
        # Squares are summable (p=3/2); absolute values are not (p=3/4).
        sum_p15 = sum(n**(-1.5) for n in range(1, 10001))
        sum_p075_small = sum(n**(-0.75) for n in range(1, 101))
        sum_p075_large = sum(n**(-0.75) for n in range(1, 10001))
        self.assertLess(sum_p15, 3)
        self.assertGreater(sum_p075_large, sum_p075_small)

    def test_differentiation_unbounded_in_sup_norm(self):
        for n in (10, 100, 1000):
            self.assertLessEqual(1/n, 0.1)
            # f_n(t) = sin(n t)/n, f'_n(t) = cos(n t)
            self.assertAlmostEqual(math.cos(n*0), 1.0)
        self.assertIn(r"f_n(t)=n^{-1}\sin(nt)", self.source)

    def test_continuous_derivative_on_smooth_frechet(self):
        self.assertIn(r"p_n(Df)\le p_{n+1}(f)", self.source)
        self.assertIn(r"p_n(Rg)\le 2p_n(g)", self.source)
        self.assertIn(r"C^\infty([0,1])/\K\cong C^\infty([0,1])", self.source)

    def test_figure_and_documentation(self):
        self.assertIn(r"\begin{tikzpicture}", self.source)
        self.assertIn("Schemat dowodu twierdzenia o wykresie domkniętym", self.source)
        self.assertNotRegex(self.source, r"\\(?:mathbf|mathbb)\s*\{?\s*1\s*\}?\s*_")
        self.assertNotIn("zwartościowanie", self.source)


if __name__ == "__main__":
    unittest.main()
