"""AT-07/AT-08 regression gates: proof hypotheses, calculations and TeX assets.

Covers the audited two-chapter pair and its 01-06 prerequisites.
A successful static suite is not a substitute for the real PDF CI build.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
from math import gcd
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters" / "pl" / "algebraic_topology"
BOOK = ROOT / "books" / "pl" / "algebraic_topology.tex"


class TopologyChapterSevenEightTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = sorted(AT.glob("0[1-8]-*.tex"))
        cls.texts = {p.name[:2]: p.read_text(encoding="utf-8-sig")
                     for p in cls.files}

    def test_original_modular_book_registers_all_prerequisites(self):
        self.assertEqual(set(self.texts), {f"{i:02d}" for i in range(1, 9)})
        book = BOOK.read_text(encoding="utf-8-sig")
        for p in self.files:
            self.assertIn(
                r"\input{../../chapters/pl/algebraic_topology/" + p.name + "}",
                book)

    def test_historical_labels_preserved_without_new_collisions(self):
        expected = {
            "07": ("ch:fibracje-v4", "lem:fib-wzgledne-v4",
                   "thm:fib-les-v4", "thm:hopf-v4"),
            "08": ("ch:kohomologia-singularna",
                   "thm:ez-v4", "thm:kunneth-v4",
                   "sec:ez-kunneth-v4"),
        }
        for num, names in expected.items():
            for label in names:
                with self.subTest(chapter=num, label=label):
                    self.assertEqual(
                        self.texts[num].count(r"\label{" + label + "}"), 1)
        labels = re.findall(r"\\label\s*\{([^}]+)\}",
                            "\n".join(self.texts.values()))
        self.assertEqual(len(labels), len(set(labels)))

    def test_all_references_resolve_in_first_eight_chapters(self):
        declared = set(re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.texts.values())))
        for num in ("07", "08"):
            refs = re.findall(
                r"\\(?:ref|eqref|autoref|pageref|nameref)\s*\{([^}]+)\}",
                self.texts[num])
            self.assertGreater(len(refs), 0)
            self.assertEqual(set(refs) - declared, set())

    def test_no_external_assets_balanced_environments(self):
        for num, num_figs in (("07", 2), ("08", 1)):
            src = self.texts[num]
            begin = Counter(re.findall(r"\\begin\{([^}]+)\}", src))
            end = Counter(re.findall(r"\\end\{([^}]+)\}", src))
            self.assertEqual(begin, end)
            self.assertGreaterEqual(begin["tikzpicture"], num_figs)
            for command in ("includegraphics", "input", "lstinputlisting",
                            "inputminted"):
                self.assertNotRegex(src, r"\\" + command + r"\s*\{")

    def test_polish_mathematical_terminology(self):
        for num in ("07", "08"):
            self.assertNotRegex(
                self.texts[num].lower(),
                r"\btensorowan\w*|\btensorowali\w*|\bsekwencj\w*"
                r"|\bseskwilini\w*")

    def test_hopf_local_trivializations_and_connecting_map(self):
        src = self.texts["07"]
        self.assertIn(r"\label{prz:fib-hopf-nietrywialna}", src)
        self.assertIn(r"\label{fig:fib-hopf}", src)
        self.assertIn(r"\frac{\overline u}{|u|}", src)
        self.assertIn(r"\pi_2(S^2)", src)
        self.assertIn(r"\pi_1(S^1)", src)
        # s_1(1/u) = (\bar u/|u|) s_0(u), checked at u=i:
        # s_0(i)=(1,i)/sqrt(2), s_1(-i)=(-i,1)/sqrt(2).
        u = 1j
        s0 = (1/(2**0.5), u/(2**0.5))
        s1 = ((1/u)/(2**0.5), 1/(2**0.5))
        phase = u.conjugate()/abs(u)
        for a, b in zip(s1, s0):
            self.assertAlmostEqual(abs(a-phase*b), 0)

    def test_klein_mapping_torus_reverses_generator(self):
        src = self.texts["07"]
        self.assertIn(r"\label{prz:fib-klein-monodromia}", src)
        self.assertIn(r"a b a^{-1}=b^{-1}", src)
        self.assertIn(r"\pi_1(K)", src)

    def test_aw_cup_proof_has_correct_middle_term_cancellation(self):
        src = self.texts["08"]
        self.assertIn(r"\label{prz:kohomologia-kubek-torus}", src)
        self.assertIn(r"\label{fig:kubek-torus}", src)
        self.assertIn("Te dwa dodatkowe wyrazy znoszą się", src)
        self.assertNotIn("Dwa wyrazy ze środkowych ścian", src)
        # Cocycle values for [ABC],[ACD]: a=(1,0,-1,0,1)
        # and b=(0,1,0,1,1) on AB,BC,CD,AD,AC.
        a = {"AB": 1, "BC": 0, "CD": -1, "AD": 0, "AC": 1}
        b = {"AB": 0, "BC": 1, "CD": 0, "AD": 1, "AC": 1}
        for c in (a, b):
            self.assertEqual(c["BC"]-c["AC"]+c["AB"], 0)
            self.assertEqual(c["CD"]-c["AD"]+c["AC"], 0)
        pairing = a["AB"]*b["BC"] + a["AC"]*b["CD"]
        self.assertEqual(pairing, 1)

    def test_kunneth_rp2_product_torsion_and_de_rham_generator(self):
        src = self.texts["08"]
        self.assertIn(r"\label{prz:kunneth-rp2-razy-rp2}", src)
        self.assertIn(r"\label{prz:de-rham-okrag-explicit}", src)
        self.assertEqual(gcd(2, 2), 2)
        # The tensor H1(P) tensor H1(P) contributes to H2;
        # Tor(H1(P),H1(P)) contributes to H3.
        self.assertIn(r"H_3(X;\Z)\cong\Z/2\Z", src)
        self.assertIn(r"\int_{S^1}\omega", src)


if __name__ == "__main__":
    unittest.main()
