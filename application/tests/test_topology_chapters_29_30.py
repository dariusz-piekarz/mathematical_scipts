"""AT-29/30 mathematical audit: lim^1, tubular neighborhoods and transversality.

All computations use only the Python standard library. No figure, data,
program, or package external to the source tree is required.
"""
from __future__ import annotations

from collections import Counter
from math import cos, hypot, isclose, sin, sqrt
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters" / "pl" / "algebraic_topology"
DG = ROOT / "chapters" / "pl" / "differential_geometry_and_topology"
SHARED = ROOT / "shared" / "pl"
BOOK = ROOT / "books" / "pl" / "algebraic_topology.tex"


class AlgebraicTopologyTwentyNineThirtyAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.paths = [
            next(AT.glob(f"{n:02d}-*.tex")) for n in range(1, 31)
        ]
        cls.texts = {
            p.name[:2]: p.read_text(encoding="utf-8-sig")
            for p in cls.paths
        }
        cls.shared = [
            p.read_text(encoding="utf-8-sig")
            for p in (
                SHARED / "slabe_twierdzenie_lefschetza.tex",
                SHARED / "rozdmuchanie_punktu_normalna.tex",
                SHARED / "rozdmuchanie_punktu_kohomologia.tex",
            )
        ]

    def test_canonical_book_includes_all_thirty(self):
        self.assertEqual(
            set(self.texts), {f"{n:02d}" for n in range(1, 31)}
        )
        book = BOOK.read_text(encoding="utf-8-sig")
        for path in self.paths:
            self.assertIn(
                r"\input{../../chapters/pl/algebraic_topology/"
                + path.name + "}", book
            )
        self.assertIn(r"\appendix", self.texts["29"])
        self.assertNotIn(r"\appendix", self.texts["30"])
        self.assertLess(
            book.index("29-dalsze-narzedzia"),
            book.index("30-minimalne-przypomnienie"),
        )

    def test_labels_are_unique_and_forward_references_resolve(self):
        text = "\n".join([*self.texts.values(), *self.shared])
        labels = re.findall(r"\\label\s*\{([^}]+)\}", text)
        self.assertEqual(len(labels), len(set(labels)))
        known = set(labels)
        for n in ("29", "30"):
            refs = set(re.findall(
                r"\\(?:ref|eqref|pageref|autoref|nameref)\s*\{([^}]+)\}",
                self.texts[n],
            ))
            self.assertFalse(refs - known, sorted(refs - known))
        for label, n in (
            ("ch:xviii-domkniecie", "29"),
            ("thm:xviii-milnor", "29"),
            ("prz:xviii-lim1-2adic-audit", "29"),
            ("fig:xviii-lim1-2adic-audit", "29"),
            ("ch:dodatek-geometria", "30"),
            ("prz:at30-okrag-regularny", "30"),
            ("prz:at30-transwersalnosc-prostych", "30"),
            ("fig:at30-stycznosc-transwersalnosc", "30"),
        ):
            self.assertIn(r"\label{" + label + "}", self.texts[n])

    def test_environments_tikz_and_source_independence(self):
        for n in ("29", "30"):
            with self.subTest(chapter=n):
                src = self.texts[n]
                begin = Counter(re.findall(r"\\begin\{([^}]+)\}", src))
                end = Counter(re.findall(r"\\end\{([^}]+)\}", src))
                self.assertEqual(begin, end)
                self.assertGreaterEqual(begin["figure"], 1)
                self.assertGreaterEqual(begin["tikzpicture"], 1)
                for cmd in (
                    "input", "include", "includegraphics",
                    "lstinputlisting", "inputminted",
                ):
                    self.assertNotRegex(
                        src, r"\\" + cmd + r"\s*(?:\[[^]]*])?\s*\{"
                    )
                self.assertNotIn(r"\\mathcal", src)
                self.assertNotIn(r"\\to", src)
                self.assertNotRegex(
                    src.lower(),
                    r"\btensorowan\w*|\bsekwencj\w*|\bseskwilini\w*",
                )

    def test_mittag_leffler_counterexample_is_explicit(self):
        src = self.texts["29"]
        self.assertIn(r"\label{prz:xviii-lim1-2adic-audit}", src)
        self.assertIn(r"\varprojlim{}^1(\Z,\times2)", src)
        # Sum of even powers of 2 equals -1/3 in Z_2.
        for n in range(1, 21):
            r = sum(2 ** (2 * j) for j in range((n + 1) // 2))
            self.assertEqual((3 * r + 1) % (2**n), 0)
        # No integer q can satisfy 3q=-1.
        self.assertNotEqual(-1 % 3, 0)

    def test_each_finite_difference_system_can_be_solved(self):
        b = lambda j: 1 if j % 2 == 0 else 0
        for N in range(1, 28):
            a = [0] * (N + 1)
            for j in range(N - 1, -1, -1):
                a[j] = b(j) + 2 * a[j + 1]
            self.assertTrue(all(
                a[j] - 2 * a[j + 1] == b(j) for j in range(N)
            ))

    def test_morse_linearization_uses_covariant_derivative(self):
        src = self.texts["29"]
        self.assertIn(r"\nabla_s\xi", src)
        self.assertIn("trywializacji równoległej", src)
        self.assertIn(r"\label{lem:xviii-uniform-right-inverse}", src)
        self.assertIn("nie przedstawiamy jako udowodnionego", src)

    def test_derivations_and_smooth_framings_are_qualified(self):
        src = self.texts["30"]
        self.assertIn(r"D(fg)=f(p)D(g)+g(p)D(f)", src)
        self.assertIn("gładkich", src)
        self.assertIn("gładkiej", src)
        for ch, label in (
            ("01", "ch:rozmaitosci"),
            ("03", "ch:algebra-tensorowa"),
            ("15", "ch:sard-transwersalnosc"),
            ("16", "ch:wlozenia-otoczenia"),
        ):
            text = next(DG.glob(f"{ch}-*.tex")).read_text(encoding="utf-8-sig")
            self.assertIn(r"\label{" + label + "}", text)
            self.assertIn(r"\texttt{" + label + "}", src)

    def test_circle_regular_value_normal_and_tubular_inverse(self):
        src = self.texts["30"]
        self.assertIn(r"\label{prz:at30-okrag-regularny}", src)
        self.assertIn(r"\Phi^{-1}(X,Y,Z)", src)
        for theta in (0.0, 0.4, 1.7, 3.1, 4.8):
            x, y = cos(theta), sin(theta)
            self.assertTrue(isclose(x * x + y * y, 1, abs_tol=1e-12))
            # Rank DF=2 on F^{-1}(0); radial and vertical rows independent.
            self.assertTrue(abs(x) > 1e-4 or abs(y) > 1e-4)
            tang = (-y, x, 0)
            self.assertTrue(isclose(x * tang[0] + y * tang[1], 0,
                                    abs_tol=1e-12))
            for a, b in ((0, 0), (-0.18, 0.09), (0.21, -0.13)):
                X, Y, Z = (1 + a) * x, (1 + a) * y, b
                rho = hypot(X, Y)
                xx, yy, aa, bb = X / rho, Y / rho, rho - 1, Z
                for actual, expected in (
                    (xx, x), (yy, y), (aa, a), (bb, b)
                ):
                    self.assertTrue(isclose(
                        actual, expected, rel_tol=1e-12, abs_tol=1e-12
                    ))

    def test_tangent_line_and_transverse_perturbation(self):
        src = self.texts["30"]
        self.assertIn(
            r"\label{prz:at30-transwersalnosc-prostych}", src
        )
        # At y=1, x=0 and both tangent lines are horizontal.
        x0, y0 = 0, 1
        det_at_tangency = (-y0) * 0 - x0 * 1
        self.assertEqual(det_at_tangency, 0)
        for eps in (0.1, 0.3, 0.5):
            x = sqrt(2 * eps - eps * eps)
            y = 1 - eps
            for sign in (-1, 1):
                xx = sign * x
                self.assertTrue(isclose(xx * xx + y * y, 1))
                # det((-y,xx),(1,0))=-xx !=0.
                self.assertNotEqual(-xx, 0)


if __name__ == "__main__":
    unittest.main()
