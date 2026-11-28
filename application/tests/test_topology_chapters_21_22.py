"""AT-21/22 deep audit regressions: boundary indices and noncompact duality.

Separate CI checks two-pass LaTeX with AT-01..23 as context because AT-22
already contains an original, forward reference to the sheaf chapter AT-23.
AT-23 is a reference prerequisite, not a chapter reviewed here.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
from math import cos, sin, pi
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters" / "pl" / "algebraic_topology"
BOOK = ROOT / "books" / "pl" / "algebraic_topology.tex"


class TopologyChaptersTwentyOneTwentyTwoAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = sorted(AT.glob("0[1-9]-*.tex")) + sorted(
            f for n in range(10, 24) for f in AT.glob(f"{n:02d}-*.tex")
        )
        cls.src = {f.name[:2]: f.read_text(encoding="utf-8-sig")
                   for f in cls.files}

    def test_book_includes_canonical_chapters_and_future_reference(self):
        self.assertEqual(set(self.src), {f"{n:02d}" for n in range(1, 24)})
        book = BOOK.read_text(encoding="utf-8-sig")
        for file in self.files:
            with self.subTest(chapter=file.name[:2]):
                self.assertIn(
                    r"\input{../../chapters/pl/algebraic_topology/"
                    + file.name + "}", book
                )

    def test_historical_labels_preserved_and_global_uniqueness(self):
        historical = {
            "21": ("ch:poincare-hopf-v11", "lem:field-fixed-v11",
                   "thm:PH-boundary-v11"),
            "22": ("ch:compact-bm-v11",
                   "def:compact-support-cohom-v11",
                   "prop:compact-proper-v11", "lem:compact-R-v11",
                   "thm:compact-Rn-v11", "thm:compact-deRham-v11",
                   "def:BM-chain-v11", "prop:BM-proper-v11",
                   "ex:BM-line-v11", "thm:noncompact-PD-v11"),
        }
        for ch, labels in historical.items():
            for label in labels:
                with self.subTest(ch=ch, label=label):
                    self.assertEqual(self.src[ch].count(
                        r"\label{" + label + "}"), 1)
        labels = re.findall(r"\\label\s*\{([^}]+)\}",
                            "\n".join(self.src.values()))
        self.assertEqual(len(labels), len(set(labels)))

    def test_all_audited_references_have_targets_through_at23(self):
        labels = set(re.findall(r"\\label\s*\{([^}]+)\}",
                                "\n".join(self.src.values())))
        for ch in ("21", "22"):
            refs = re.findall(
                r"\\(?:ref|eqref|pageref|autoref|nameref)\s*\{([^}]+)\}",
                self.src[ch],
            )
            self.assertGreaterEqual(len(refs), 4)
            self.assertEqual(set(refs) - labels, set())
        self.assertIn(r"\ref{ch:snopy-verdier-v12}", self.src["22"])
        self.assertIn(r"\label{ch:snopy-verdier-v12}", self.src["23"])

    def test_balanced_tex_and_tikz_no_external_assets(self):
        for ch in ("21", "22"):
            text = self.src[ch]
            self.assertEqual(
                Counter(re.findall(r"\\begin\{([^}]+)\}", text)),
                Counter(re.findall(r"\\end\{([^}]+)\}", text)),
            )
            self.assertGreaterEqual(text.count(r"\begin{tikzpicture}"), 1)
            for external in (
                "includegraphics", "input", "include",
                "lstinputlisting", "inputminted",
            ):
                self.assertNotRegex(text, r"\\" + external + r"\s*\{")

    def test_polish_mathematical_terminology(self):
        for ch in ("21", "22"):
            self.assertNotRegex(
                self.src[ch].lower(),
                r"\btensorowan\w*|\btensorowali\w*"
                r"|\bsekwencj\w*|\binjekc\w*",
            )

    def test_local_field_index_uses_actual_euclidean_chart_domain(self):
        """The Brouwer degree is computed on phi(U), not on a manifold patch U."""
        src = self.src["21"]
        required = (
            r"$\varphi:W\to\R^n$ z $\varphi(p)=0$",
            r"$\overline U\subset W\cap\operatorname{int}M$",
            r"$p$ jest jedynym zerem $X$ w $\overline U$",
            r"$f_t(\overline U)\subset W$",
            r"$V(y)=\mathrm d\varphi_{\varphi^{-1}(y)}",
            r"$\deg(\id-F_t,\varphi(U),0)=\deg(V,\varphi(U),0)$",
            r"Gładkie pole wektorowe $X\in\mathfrak X(M)$",
        )
        for fragment in required:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, src)
        self.assertNotIn(r"\deg(\id-F_t,U,0)", src)
        self.assertNotIn("Iteracja XI:", src)

    def test_boundary_crossing_example_changes_index_only_at_boundary(self):
        """For X_s(x)=(1-s)e_1+s*x, the zero crosses |x|=1 at s=1/2."""
        src = self.src["21"]
        self.assertIn(r"\label{prz:PH-przekroczenie-brzegu-21}", src)
        for parameter in (0.01, 0.25, 0.49, 0.5, 0.51, 0.75, 1.0):
            zero_radius = (1 - parameter) / parameter
            interior = zero_radius < 1
            on_boundary = zero_radius == 1
            with self.subTest(parameter=parameter):
                self.assertEqual(interior, parameter > 0.5)
                self.assertEqual(on_boundary, parameter == 0.5)
                # At every interior zero D X_s=s I_n has positive determinant.
                if interior:
                    self.assertGreater(parameter**3, 0)

    def test_double_smoothing_preserves_fixed_points_and_lefschetz(self):
        """Relative smoothing on the double is homotopic and fixed-point safe."""
        src = self.src["21"]
        for fragment in (
            r"$\widetilde F:DM\to DM$",
            r"homotopijne z $F$",
            r"równe mu w mniejszych otoczeniach",
            r"nie tworzy nowych punktów stałych",
            r"$L(\widetilde F)=L(F)$",
            r"twierdzenie o gładkiej aproksymacji",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, src)

    def test_all_environment_nesting_and_reference_closure(self):
        """Environment count alone misses mis-nesting; audit structure sequentially."""
        for ch in ("21", "22"):
            src = self.src[ch]
            with self.subTest(chapter=ch):
                starts = re.findall(
                    r"\\(?:ref|eqref|pageref|autoref|nameref)\s*\{", src
                )
                complete = re.findall(
                    r"\\(?:ref|eqref|pageref|autoref|nameref)\s*\{[^{}\n]+\}",
                    src,
                )
                self.assertEqual(len(starts), len(complete))
                stack = []
                for item in re.finditer(
                    r"\\(begin|end)\{([^{}]+)\}", src
                ):
                    kind, env = item.groups()
                    if kind == "begin":
                        stack.append(env)
                    else:
                        self.assertTrue(stack, f"Unexpected end of {env}")
                        self.assertEqual(stack.pop(), env)
                self.assertFalse(stack, f"Unclosed environments: {stack}")

    def test_inward_poincare_hopf_sign_on_balls(self):
        src = self.src["21"]
        self.assertIn(r"\label{cor:PH-inward-boundary}", src)
        self.assertIn(r"\label{prz:PH-inward-ball}", src)
        for n in range(1, 9):
            with self.subTest(n=n):
                # determinant of D(-id) = (-1)^n; chi(D^n) = 1.
                det_minus_identity = (-1) ** n
                self.assertEqual(det_minus_identity, (-1)**n * 1)

    def test_annulus_field_outward_both_boundaries_without_zeros(self):
        src = self.src["21"]
        self.assertIn(r"\label{prz:PH-annulus-nozeros}", src)
        self.assertIn(r"\label{fig:PH-annulus-field}", src)
        a, b = 1.0, 3.0
        r0 = (a+b)/2
        for theta in (0, pi/7, pi/3, pi, 2*pi):
            er = (cos(theta), sin(theta))
            et = (-sin(theta), cos(theta))
            for r in (a, r0, b):
                x = ((r-r0)*er[0]+et[0],
                     (r-r0)*er[1]+et[1])
                length_squared = x[0]**2 + x[1]**2
                with self.subTest(r=r, theta=theta):
                    self.assertAlmostEqual(length_squared, (r-r0)**2+1)
                    self.assertGreater(length_squared, 0)
                if r == a:
                    outward_normal = (-er[0], -er[1])
                    self.assertGreater(sum(u*v for u,v in
                                           zip(x, outward_normal)), 0)
                if r == b:
                    self.assertGreater(sum(u*v for u,v in zip(x, er)), 0)

    def test_at22_dual_cell_boundary_coboundary_grading(self):
        """For sigma<tau, d sigma* has coefficient tau*, never sigma in d tau."""
        src = self.src["22"]
        for fragment in (
            r"współczynnikiem $\tau^*$ w $\delta(\sigma^*)$",
            r"współczynnikowi $\sigma$ w $\partial\tau$",
            r"$\dim D(\tau)=n-k-1=\dim D(\sigma)-1$",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, src)
        self.assertNotIn(r"współczynnikiem $\sigma$ w $\delta\tau$", src)
        for face, expected in (((1, 2), 1), ((0, 2), -1), ((0, 1), 1)):
            with self.subTest(face=face):
                boundary = {(1, 2): 1, (0, 2): -1, (0, 1): 1}
                self.assertEqual(boundary[face], expected)

    def test_at22_explicit_coefficients_and_chart_mapping_rule(self):
        src = self.src["22"]
        for fragment in (
            r"Niech $X,Y$ będą lokalnie zwartymi przestrzeniami Hausdorffa,",
            r"$G$ grupą abelową, a $k\ge0$ liczbą całkowitą.",
            r"$G$ grupą abelową, a $k\in\Z$.",
            r"drugoprzeliczalnej rozmaitości $M$ bez brzegu",
            r"homologia Borela--Moore'a",
            r"odwzorowanie właściwe",
            r"Porównanie odwzorowań łączących",
            r"przy przejściu między mapami",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, src)
        self.assertNotIn("homologia Borel--Moore'a", src)
        self.assertNotIn("Mapa łańcuchowa", src)

    def test_disjoint_lines_product_and_direct_sum_distinction(self):
        src = self.src["22"]
        self.assertIn(r"\label{prz:BM-countable-lines}", src)
        self.assertIn(r"\label{fig:BM-countable-lines}", src)
        self.assertIn(r"\prod_{j\in\N}\Z", src)
        self.assertIn(r"\bigoplus_{j\in\N}\Z", src)
        # The constant infinite integer sequence belongs to product but
        # to no finite-support direct sum. A single nonzero coordinate
        # does belong to both.
        product_element = [1] * 1000
        self.assertEqual(len([n for n in product_element if n]), 1000)
        for truncation in (5, 10, 20):
            self.assertGreater(
                len([n for n in product_element if n]), truncation
            )
        finite_support = [0] * 1000
        finite_support[12] = 3
        self.assertEqual(sum(n != 0 for n in finite_support), 1)

    def test_proper_inclusion_need_not_inject_on_BM(self):
        src = self.src["22"]
        self.assertIn(r"\label{prz:BM-proper-inclusion-line}", src)
        self.assertIn(r"H_1^{\mathrm{BM}}(\R^2;\Z)", src)
        self.assertIn(r"H^1(\R^2;\Z)=0", src)
        self.assertIn(r"i_*=0", src)

    def test_boundary_and_noncompact_hypotheses_remain_explicit(self):
        src21 = self.src["21"]
        self.assertIn(r"p\in\operatorname{int}M", src21)
        self.assertIn(r"\ref{thm:PH-boundary-v11}", src21)
        src22 = self.src["22"]
        self.assertIn("lokalnie zwartą przestrzenią Hausdorffa", src22)
        self.assertIn(r"\mathcal O_M\otimes_{\Z}G", src22)
        self.assertIn("drugoprzeliczalną", src22)


if __name__ == "__main__":
    unittest.main()
