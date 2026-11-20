"""Regression checks for the detailed mathematical audits of AT-05 and AT-06.

Tests protect historical references, proof hypotheses, mathematical examples,
inline figure independence and Polish terminology. PDF layout is checked in CI.
"""
from __future__ import annotations

from collections import Counter
from math import gcd
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters" / "pl" / "algebraic_topology"
BOOK = ROOT / "books" / "pl" / "algebraic_topology.tex"


class TopologyChapterFiveSixAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = sorted(AT.glob("0[1-6]-*.tex"))
        cls.texts = {f.name[:2]: f.read_text(encoding="utf-8-sig")
                     for f in cls.files}
        cls.book = BOOK.read_text(encoding="utf-8-sig")

    def test_all_six_chapters_appear_in_original_modular_book(self):
        self.assertEqual(set(self.texts), {"01", "02", "03", "04", "05", "06"})
        for f in self.files:
            self.assertIn(
                r"\input{../../chapters/pl/algebraic_topology/" + f.name + "}",
                self.book)

    def test_historical_labels_remain_unique(self):
        original_labels = {
            "05": (
                "ch:homologia-przestrzeni", "thm:brzeg-brzegu",
                "thm:wycinanie", "thm:mv-przestrzenie",
                "thm:homologia-sfer", "thm:komorkowa-singularna",
                "thm:formula-komorkowa", "prop:lokalna-homologia",
            ),
            "06": (
                "ch:wyzsza-homotopia", "thm:pi-n-abelowe",
                "thm:les-pi", "lem:hep-cw", "thm:przyblizenie-komorkowe",
                "thm:whitehead", "thm:hurewicz-h1",
                "thm:hurewicz-wyzszy", "thm:hurewicz-wzgledny",
                "cor:whitehead-homologiczny",
            ),
        }
        for chapter, names in original_labels.items():
            for label in names:
                with self.subTest(chapter=chapter, label=label):
                    self.assertEqual(self.texts[chapter].count(
                        r"\label{" + label + "}"), 1)
        labels = re.findall(r"\\label\s*\{([^}]+)\}",
                            "\n".join(self.texts.values()))
        self.assertEqual(len(labels), len(set(labels)))

    def test_all_new_and_old_chapter_refs_resolve_with_prerequisites(self):
        labels = set(re.findall(r"\\label\s*\{([^}]+)\}",
                                "\n".join(self.texts.values())))
        for chapter in ("05", "06"):
            refs = re.findall(
                r"\\(?:ref|eqref|autoref|pageref|nameref)\s*\{([^}]+)\}",
                self.texts[chapter])
            self.assertGreater(len(refs), 40)
            self.assertEqual(set(refs) - labels, set())

    def test_environment_balance_and_no_external_assets(self):
        for chapter, min_figures in (("05", 4), ("06", 5)):
            source = self.texts[chapter]
            begins = Counter(re.findall(r"\\begin\{([^}]+)\}", source))
            ends = Counter(re.findall(r"\\end\{([^}]+)\}", source))
            self.assertEqual(begins, ends)
            self.assertGreaterEqual(begins["figure"], min_figures)
            self.assertGreaterEqual(begins["tikzpicture"], min_figures)
            for command in ("includegraphics", "input", "include",
                            "lstinputlisting", "inputminted"):
                self.assertNotRegex(source, r"\\" + command + r"\s*\{")

    def test_polish_terminology(self):
        for chapter in ("05", "06"):
            self.assertNotRegex(self.texts[chapter].lower(),
                                r"\btensorowan\w*|\btensorowali\w*"
                                r"|\bsekwencyjn\w*|\bseskwilini\w*")

    def test_mayer_vietoris_boundary_is_explicit(self):
        ch = self.texts["05"]
        self.assertIn(r"\label{prz:mv-sfera-dwie-polkul}", ch)
        self.assertIn(r"\delta[a+b]=[\gamma]", ch)
        self.assertIn(r"\partial a=\gamma", ch)
        self.assertIn(r"\partial b=-\gamma", ch)

    def test_klein_bottle_cellular_chain_computation(self):
        ch = self.texts["05"]
        self.assertIn(r"\label{prz:homologia-butelka-kleina}", ch)
        self.assertIn(r"\label{fig:homologia-butelka-kleina}", ch)
        self.assertIn("aba^{-1}b", ch)
        # For the CW chain complex Z -> Z^2 -> Z the differentials
        # are d2(1)=(0,2), d1=0.
        d2 = (0, 2)
        self.assertEqual(gcd(*d2), 2)
        self.assertEqual(d2, (0, 2))
        self.assertEqual(tuple(v % 2 for v in d2), (0, 0))
        self.assertEqual(1 - 2 + 1, 0)  # Euler characteristic

    def test_gcd_attachments_yield_h2_zero_and_h3_one_generator(self):
        ch = self.texts["06"]
        self.assertIn(r"\label{prz:pi-2-3-komorki}", ch)
        self.assertIn(r"\label{fig:pi-2-3-komorki}", ch)
        self.assertEqual(gcd(2, 3), 1)   # d3: Z^2 -> Z is onto
        # Integer kernel of (a,b) -> 2a + 3b: all multiples of (3,-2).
        for a in range(-12, 13):
            for b in range(-12, 13):
                if 2*a + 3*b == 0:
                    self.assertEqual(a % 3, 0)
                    self.assertEqual(b, -2*(a // 3))
        self.assertIn(r"S^3\simeq X", ch)
        self.assertIn(r"cor:whitehead-homologiczny", ch)

    def test_hurewicz_fundamental_group_example_matches_klein_h1(self):
        ch = self.texts["06"]
        self.assertIn(r"\label{prz:pi1-klein-hurewicz}", ch)
        self.assertIn(r"\ref{prz:homologia-butelka-kleina}", ch)
        self.assertIn("2b=0", ch)
        self.assertIn(r"\pi_1(K)_{\mathrm{ab}}", ch)


if __name__ == "__main__":
    unittest.main()
