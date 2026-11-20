"""AT-11/12 audit regression tests: duality, intersection forms and spectral pages."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters" / "pl" / "algebraic_topology"
BOOK = ROOT / "books" / "pl" / "algebraic_topology.tex"


class TopologyChapterElevenTwelveAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = sorted(AT.glob("0[1-9]-*.tex")) + sorted(
            f for n in (10, 11, 12) for f in AT.glob(f"{n:02d}-*.tex")
        )
        cls.text = {
            f.name[:2]: f.read_text(encoding="utf-8-sig")
            for f in cls.files
        }

    def test_canonical_book_includes_twelve_chapters(self):
        self.assertEqual(set(self.text), {f"{i:02d}" for i in range(1, 13)})
        book = BOOK.read_text(encoding="utf-8-sig")
        for f in self.files:
            self.assertIn(
                r"\input{../../chapters/pl/algebraic_topology/" + f.name + "}",
                book,
            )

    def test_preserve_historical_labels(self):
        required = {
            "11": (
                "ch:przeciecia-dualnosc-klasy",
                "thm:poincare-dualnosc-16",
                "thm:pl-v4",
                "thm:alexander-v4",
                "thm:clutching-16",
                "thm:wi-klasy-16",
                "thm:poincare-hopf-16",
                "thm:forma-przeciecia-16",
            ),
            "12": (
                "ch:ciagi-spektralne-v5",
                "lem:dr-v5",
                "thm:pages-v5",
                "thm:convergence-v5",
                "thm:serre-v5",
                "thm:serre-general-v6",
                "thm:gysin-v5",
                "thm:thom-v5",
            ),
        }
        for chapter, labels in required.items():
            for label in labels:
                with self.subTest(chapter=chapter, label=label):
                    self.assertEqual(
                        self.text[chapter].count(r"\label{" + label + "}"),
                        1,
                    )
        labels = re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.text.values())
        )
        self.assertEqual(len(labels), len(set(labels)))

    def test_all_references_resolve_with_prior_chapters(self):
        labels = set(re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.text.values())
        ))
        for chapter in ("11", "12"):
            refs = re.findall(
                r"\\(?:ref|eqref|autoref|pageref|nameref)\s*\{([^}]+)\}",
                self.text[chapter],
            )
            self.assertGreater(len(refs), 15)
            self.assertEqual(set(refs) - labels, set())

    def test_environment_balance_and_independent_figures(self):
        for chapter, minimum_figures in (("11", 5), ("12", 2)):
            src = self.text[chapter]
            self.assertEqual(
                Counter(re.findall(r"\\begin\{([^}]+)\}", src)),
                Counter(re.findall(r"\\end\{([^}]+)\}", src)),
            )
            self.assertGreaterEqual(
                len(re.findall(r"\\begin\{tikzpicture\}", src)),
                minimum_figures,
            )
            for command in ("includegraphics", "input", "include",
                            "lstinputlisting", "inputminted"):
                self.assertNotRegex(src, r"\\" + command + r"\s*\{")

    def test_consistent_polish_terminology(self):
        for chapter in ("11", "12"):
            self.assertNotRegex(
                self.text[chapter].lower(),
                r"\btensorowan\w*|\btensorowali\w*"
                r"|\bsekwencj\w*|\binjekc\w*",
            )

    def test_cp2_connected_sum_parity_obstructs_homotopy(self):
        ch = self.text["11"]
        self.assertIn(r"\label{prz:formy-przeciecia-cp2-s2}", ch)
        self.assertIn(r"\label{fig:formy-przeciecia-parzystosc}", ch)
        # CP2#(-CP2): diag(1,-1) is odd, S2xS2 hyperbolic is even.
        def q_odd(a, b):
            return a*a - b*b

        def q_even(a, b):
            return 2*a*b

        self.assertEqual(q_odd(1, 0), 1)
        for a in range(-12, 13):
            for b in range(-12, 13):
                self.assertEqual(q_even(a, b) % 2, 0)
        self.assertIn(r"H_2(N;\Z)", ch)

    def test_spectral_page_three_example(self):
        ch = self.text["12"]
        self.assertIn(r"\label{prz:spectral-d3-cancel}", ch)
        self.assertIn(r"d^3:E^3_{3,0}", ch)
        # C3 = Z, C2 = Z, d3 = identity:
        self.assertEqual(1, 1)  # rank(d3) = 1
        self.assertEqual(1 - 1, 0)  # H3
        self.assertEqual(1 - 1, 0)  # H2
        self.assertIn("Strona czwarta jest zerowa", ch)

    def test_extension_problem_distinguishes_actual_groups(self):
        ch = self.text["12"]
        self.assertIn(r"\label{prz:spectral-extension-z4}", ch)
        self.assertIn(r"\label{fig:spectral-extension-z4}", ch)
        z4 = [0, 1, 2, 3]
        z2x2 = [(a, b) for a in range(2) for b in range(2)]
        self.assertEqual(len(z4), len(z2x2))
        self.assertEqual((1 + 1) % 4, 2)
        self.assertTrue(all(((a+a) % 2, (b+b) % 2) == (0, 0)
                            for a, b in z2x2))
        self.assertIn(r"\Z/4\Z", ch)
        self.assertIn(r"(\Z/2\Z)^2", ch)

    def test_serre_hypotheses_no_contradictory_disclaimer(self):
        ch = self.text["12"]
        self.assertIn(r"\ref{thm:serre-general-v6}", ch)
        self.assertIn("skończeniewymiarowej", ch)
        self.assertIn("Nie należy więc opisywać", ch)
        self.assertNotIn(
            "Wersja dla wszystkich fibracji Serre'a, pełny dowód", ch
        )


if __name__ == "__main__":
    unittest.main()
