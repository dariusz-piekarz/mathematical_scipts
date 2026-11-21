"""Detailed mathematical audit regression for AT-13/14.

Check historical labels, references, standalone diagrams and explicit arithmetic
behind Moore spaces, Postnikov lifting and Steenrod squares. The two-pass TeX
compilation is a separate CI requirement.
"""
from __future__ import annotations

from collections import Counter
from math import comb
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters" / "pl" / "algebraic_topology"
BOOK = ROOT / "books" / "pl" / "algebraic_topology.tex"


class TopologyChapterThirteenFourteenAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = sorted(AT.glob("0[1-9]-*.tex")) + sorted(
            file for number in range(10, 15)
            for file in AT.glob(f"{number:02d}-*.tex")
        )
        cls.texts = {
            path.name[:2]: path.read_text(encoding="utf-8-sig")
            for path in cls.files
        }

    def test_canonical_modular_book_contains_all_fourteen_chapters(self):
        self.assertEqual(set(self.texts), {f"{n:02d}" for n in range(1, 15)})
        book = BOOK.read_text(encoding="utf-8-sig")
        for file in self.files:
            with self.subTest(chapter=file.name[:2]):
                self.assertIn(
                    r"\input{../../chapters/pl/algebraic_topology/"
                    + file.name + "}", book
                )

    def test_historical_labels_are_preserved_and_unique(self):
        original = {
            "13": (
                "ch:klasyfikacja-v6",
                "thm:KGn-existence-v6",
                "thm:rep-coho-v6",
                "thm:bar-BG-v6",
                "thm:BG-general-v6",
                "thm:obstruction-section-v6",
                "sec:audyt-VI-VII",
            ),
            "14": (
                "ch:postnikow-v7",
                "thm:postnikow-istence-v7",
                "lem:hofib-K-v7",
                "thm:postnikov-k-v7",
                "thm:s2-k-v7",
                "thm:whitehead-product-v7",
                "thm:whitehead-square-v7",
                "thm:postnikov-lift-v7",
                "lem:cup-i-v7",
                "thm:steenrod-basic-v7",
                "thm:steenrod-cartan-v7",
            ),
        }
        for chapter, labels in original.items():
            for label in labels:
                with self.subTest(chapter=chapter, label=label):
                    self.assertEqual(
                        self.texts[chapter].count(r"\label{" + label + "}"), 1
                    )
        all_labels = re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.texts.values())
        )
        self.assertEqual(len(all_labels), len(set(all_labels)))

    def test_references_resolve_in_fourteen_chapter_scope(self):
        declared = set(re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.texts.values())
        ))
        for chapter in ("13", "14"):
            references = re.findall(
                r"\\(?:ref|eqref|autoref|pageref|nameref)\s*\{([^}]+)\}",
                self.texts[chapter],
            )
            self.assertGreater(len(references), 0)
            self.assertEqual(set(references) - declared, set())

    def test_balanced_environments_and_no_external_assets(self):
        for chapter, minimum_figures in (("13", 1), ("14", 1)):
            source = self.texts[chapter]
            self.assertEqual(
                Counter(re.findall(r"\\begin\{([^}]+)\}", source)),
                Counter(re.findall(r"\\end\{([^}]+)\}", source)),
            )
            self.assertGreaterEqual(
                len(re.findall(r"\\begin\{tikzpicture\}", source)),
                minimum_figures + 1,
            )
            for command in (
                "includegraphics", "input", "include", "lstinputlisting",
                "inputminted", "verbatiminput",
            ):
                self.assertNotRegex(source, r"\\" + command + r"\s*\{")

    def test_polish_terminology(self):
        for chapter in ("13", "14"):
            self.assertNotRegex(
                self.texts[chapter].lower(),
                r"\btensorowan\w*|\btensorowali\w*"
                r"|\bsekwencj\w*|\binjekc\w*|\bekwawariant\w*",
            )

    def test_moore_cohomology_exposes_hom_and_ext(self):
        chapter = self.texts["13"]
        self.assertIn(
            r"\label{prz:moore-cohomology-Hom-Ext-v6}", chapter
        )
        self.assertIn(
            r"\label{fig:moore-kernel-cokernel-v6}", chapter
        )
        self.assertIn(r"H^n(M;A)=A[m]", chapter)
        self.assertIn(r"H^{n+1}(M;A)=A/mA", chapter)
        m, modulus = 6, 4
        annihilator = [a for a in range(modulus)
                       if (m * a) % modulus == 0]
        image = {(m * a) % modulus for a in range(modulus)}
        self.assertEqual(annihilator, [0, 2])
        self.assertEqual(image, {0, 2})
        self.assertEqual(modulus // len(image), 2)
        self.assertRegex(chapter, r"\\operatorname\{Ext\}\^1_(?:\\Z|\{\\Z\})")

    def test_obstruction_cp2_nontrivial_square(self):
        chapter = self.texts["14"]
        self.assertIn(r"\label{prz:postnikow-cp2-nie-ma-liftu}", chapter)
        self.assertIn(r"\ref{thm:postnikov-lift-v7}", chapter)
        self.assertIn(r"h^2\ne0", chapter)
        self.assertIn(r"\eta\in\pi_3(S^2)", chapter)

    def test_whitehead_fold_does_not_extend(self):
        chapter = self.texts["14"]
        self.assertIn(r"\label{prz:whitehead-fold-product-v7}", chapter)
        self.assertIn(r"\label{fig:whitehead-product-obstruction-v7}", chapter)
        self.assertIn(r"[\iota_2,\iota_2]=\pm2\eta", chapter)
        # Product of two degree-two generators: x²=y²=0, xy is
        # an integral top generator, so (x+y)²=2xy is nonzero.
        x_square = y_square = 0
        x_y = 1
        self.assertEqual(x_square + 2*x_y + y_square, 2)

    def test_steenrod_square_formula_and_adem_example(self):
        chapter = self.texts["14"]
        self.assertIn(r"\label{prz:steenrod-rp5-obliczenia-v7}", chapter)
        self.assertEqual(comb(3, 1) % 2, 1)
        self.assertEqual(comb(3, 2) % 2, 1)
        for degree in range(100):
            with self.subTest(degree=degree):
                self.assertEqual(
                    (comb(degree, 1) * comb(degree + 1, 1)) % 2,
                    0,
                )
        self.assertIn("nie zastępuje ogólnego dowodu relacji Adema", chapter)

    def test_cartan_and_adem_proofs_not_overclaimed(self):
        chapter = self.texts["14"]
        self.assertIn("nie deklarujemy pełnego dowodu Cartana ani", chapter)
        self.assertIn("Adema", chapter)


if __name__ == "__main__":
    unittest.main()
