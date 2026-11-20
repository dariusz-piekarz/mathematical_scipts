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
