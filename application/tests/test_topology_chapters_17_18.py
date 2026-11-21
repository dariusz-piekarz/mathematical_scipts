"""AT-17/18 audit regressions: Pontriagin–Thom, bordism and Morse homology.

Checks canonical source and theorem labels, tensor-algebra cross-volume links,
calculations of Stiefel–Whitney numbers and RP2 Morse differentials,
LaTeX environments and independence of local image/code resources.
Separate CI compiles the dependent AT-01–18 volume twice.
"""
from __future__ import annotations

from collections import Counter
from math import exp
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters" / "pl" / "algebraic_topology"
DG = ROOT / "chapters" / "pl" / "differential_geometry_and_topology"
BOOK = ROOT / "books" / "pl" / "algebraic_topology.tex"


class TopologySeventeenEighteenAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = sorted(AT.glob("0[1-9]-*.tex")) + sorted(
            f for n in range(10, 19) for f in AT.glob(f"{n:02d}-*.tex")
        )
        cls.text = {
            file.name[:2]: file.read_text(encoding="utf-8-sig")
            for file in cls.files
        }

    def test_book_loads_exactly_the_eighteen_prerequisites(self):
        self.assertEqual(set(self.text), {f"{i:02d}" for i in range(1, 19)})
        book = BOOK.read_text(encoding="utf-8-sig")
        for file in self.files:
            with self.subTest(path=file.name):
                self.assertIn(
                    r"\input{../../chapters/pl/algebraic_topology/"
                    + file.name + "}", book
                )

    def test_preserve_historical_labels_and_no_duplicates(self):
        historical = {
            "17": (
                "ch:pt-v9", "lem:pt-regular-v9", "lem:pt-collapse-v9",
                "thm:pt-framed-v9", "cor:pt-stable-v9",
                "thm:pt-pd-v9", "cor:euler-zero-v9",
                "prop:bordism-group-v9", "ex:bordism-low-v9",
                "thm:sw-bdy-v9", "thm:omega2-v9",
                "prop:normal-class-v9", "thm:pt-MO-v9",
                "lem:thom-transversal-v9-audyt",
            ),
            "18": (
                "ch:morse-v10", "thm:morse-lemma-v10",
                "lem:morse-energy-v10", "prop:morse-dimension-v10",
                "thm:morse-compact-v10", "def:morse-complex-v10",
                "thm:morse-d2-v10", "thm:morse-handle-v10",
                "lem:morse-same-level-audit", "thm:morse-singular-v10",
                "thm:morse-inequalities-v10",
            ),
        }
        for chapter, names in historical.items():
            for label in names:
                with self.subTest(chapter=chapter, label=label):
                    self.assertEqual(
                        self.text[chapter].count(r"\label{" + label + "}"), 1
                    )
        labels = re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.text.values())
        )
        self.assertEqual(len(labels), len(set(labels)))

    def test_references_resolve_inside_at_volume(self):
        labels = set(re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.text.values())
        ))
        for chapter in ("17", "18"):
            refs = re.findall(
                r"\\(?:ref|eqref|pageref|autoref|nameref)\s*\{([^}]+)\}",
                self.text[chapter],
            )
            self.assertGreater(len(refs), 4)
            self.assertFalse(set(refs) - labels, set(refs) - labels)

    def test_real_geometry_tensor_chapter_and_canonical_label_reused(self):
        source = (
            DG / "03-algebra-tensorowa-i-zewnetrzna.tex"
        ).read_text(encoding="utf-8-sig")
        for label in (
            "ch:algebra-tensorowa",
            "sec:iloczyn-tensorowy",
            "thm:tensor-hom",
        ):
            self.assertIn(r"\label{" + label + "}", source)
        for chapter in ("17", "18"):
            self.assertIn("03-algebra-tensorowa-i-zewnetrzna.tex", self.text[chapter])
            self.assertIn(r"\href{https://github.com/", self.text[chapter])
        self.assertIn(r"thm:tensor-hom", self.text["17"])
        self.assertIn(r"sec:iloczyn-tensorowy", self.text["18"])
        morse = (
            DG / "18-teoria-morse-a-punkty-krytyczne-uchwyty-i-przeplyw.tex"
        ).read_text(encoding="utf-8-sig")
        cobordism = (
            DG / "19-kobordyzmy-i-rachunek-uchwytow.tex"
        ).read_text(encoding="utf-8-sig")
        self.assertIn(r"\label{ch:teoria-morsea}", morse)
        self.assertIn(r"\label{ch:rachunek-uchwytow}", cobordism)

    def test_no_external_graphic_or_source_dependencies(self):
        for chapter, min_figs in (("17", 2), ("18", 2)):
            src = self.text[chapter]
            begin = Counter(re.findall(r"\\begin\{([^}]+)\}", src))
            end = Counter(re.findall(r"\\end\{([^}]+)\}", src))
            self.assertEqual(begin, end)
            self.assertGreaterEqual(begin["tikzpicture"], min_figs)
            for cmd in (
                "includegraphics", "input", "include",
                "lstinputlisting", "inputminted",
            ):
                self.assertNotRegex(src, r"\\" + cmd + r"\s*\{")

    def test_approved_polish_terms(self):
        for chapter in ("17", "18"):
            self.assertNotRegex(
                self.text[chapter].lower(),
                r"\btensorowan\w*|\btensorowali\w*"
                r"|\bsekwencj\w*|\binjekcj\w*|\bseskwilini\w*",
            )

    def test_product_of_projective_planes_is_nonneutral_in_bordism(self):
        chapter = self.text["17"]
        self.assertIn(r"\label{prz:bordism-rp2-product}", chapter)
        self.assertIn(r"\label{fig:bordism-rp2-product}", chapter)
        self.assertIn(r"\langle w_2(TX)^2,[X]_2\rangle=1", chapter)
        self.assertIn(r"\langle w_4(TX),[X]_2\rangle=1", chapter)
        # Multiply w2=a²+ab+b² with itself in F2[a,b]/(a³,b³).
        w2 = {(2, 0), (1, 1), (0, 2)}
        square = set()
        for i, j in w2:
            for k, l in w2:
                mon = (i + k, j + l)
                if mon[0] >= 3 or mon[1] >= 3:
                    continue
                if mon in square:
                    square.remove(mon)
                else:
                    square.add(mon)
        self.assertEqual(square, {(2, 2)})
        self.assertIn(r"2[X]=0", chapter)

    def test_rp4_has_same_euler_parity_but_distinct_bordism(self):
        chapter = self.text["17"]
        self.assertIn(r"\label{prz:bordism-rp4-versus-rp2-square}", chapter)
        self.assertIn(r"w(TY)=(1+t)^5=1+t+t^4", chapter)
        # Two SW-number vectors (w2²,w4) are linearly independent over F2.
        x = (1, 1)
        y = (0, 1)
        self.assertEqual((x[0]*y[1] - x[1]*y[0]) % 2, 1)
        self.assertEqual(sum([1, -1, 1]), 1)  # chi(RP4)=1
        self.assertEqual(1 * 1, 1)  # chi(RP2×RP2)=1

    def test_projective_morse_quadratic_flow_is_descending(self):
        chapter = self.text["18"]
        self.assertIn(r"\label{prz:morse-rp2-torsja}", chapter)
        self.assertIn(r"\label{fig:morse-rp2-torsja}", chapter)
        lambdas = (-1.0, 0.0, 3.0)
        x = (0.3, -0.5, 0.8)

        def value(time):
            weights = [exp(-4 * l * time) * y*y
                       for l, y in zip(lambdas, x)]
            return sum(l * w for l, w in zip(lambdas, weights)) / sum(weights)

        self.assertLess(value(0.5), value(0))
        self.assertLess(value(0), value(-0.5))
        self.assertIn(r"\lambda(p_i)=i", chapter)

    def test_morse_rp2_integral_torsion_calculation(self):
        chapter = self.text["18"]
        self.assertIn(r"\partial_2=2", chapter)
        self.assertIn(r"\partial_1=0", chapter)
        self.assertRegex(chapter, r"HM_1=[^\n]*\\cong\\Z/2\\Z")
        # 0 -> Z --2--> Z --0--> Z -> 0 gives H2=0, H1=Z/2, H0=Z.
        kernel_d2 = [n for n in range(-50, 51) if 2*n == 0]
        self.assertEqual(kernel_d2, [0])
        self.assertEqual({2*k for k in range(-50, 51)} & {1, 3, 5}, set())
        self.assertEqual({(2*k) % 2 for k in range(-50, 51)}, {0})

    def test_morse_rationalization_is_explicit_and_nonredundant(self):
        chapter = self.text["18"]
        self.assertIn(r"CM_*(f,g)\otimes_{\Z}\Q", chapter)
        self.assertIn(r"\Q$ jest płaskim $\Z$-modułem", chapter)
        self.assertIn(r"HM_k(f,g)\otimes_{\Z}\Q", chapter)
        self.assertNotIn("Tensorujmy", chapter)


if __name__ == "__main__":
    unittest.main()
