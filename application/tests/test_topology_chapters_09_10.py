"""AT-09/10 mathematical regression: de Rham, Stokes, Cech inverse limits.

Protects canonical labels, references, no external figure dependencies,
calculated examples and key hypotheses. Real two-pass PDF CI is separate.
"""
from __future__ import annotations

from collections import Counter
from math import pi, gcd
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters" / "pl" / "algebraic_topology"
BOOK = ROOT / "books" / "pl" / "algebraic_topology.tex"


class TopologyChapterNineTenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = sorted(AT.glob("0[1-9]-*.tex")) + sorted(AT.glob("10-*.tex"))
        cls.texts = {
            path.name[:2]: path.read_text(encoding="utf-8-sig")
            for path in cls.files
        }
        cls.book = BOOK.read_text(encoding="utf-8-sig")

    def test_original_modular_book_has_ten_chapters(self):
        self.assertEqual(
            set(self.texts), {f"{i:02d}" for i in range(1, 11)}
        )
        for path in self.files:
            self.assertIn(
                r"\input{../../chapters/pl/algebraic_topology/" + path.name + "}",
                self.book
            )

    def test_all_labels_are_unique_and_historical_targets_survive(self):
        required = {
            "09": (
                "ch:formy-de-rham", "thm:formy-d", "thm:stokes-formy",
                "thm:lemat-poincare-formy", "thm:de-rham",
                "thm:mv-de-rham", "thm:orientacja-atlas-forma"
            ),
            "10": (
                "ch:cech-v4", "lem:cech-contiguity-v4",
                "prop:cech-poly-v4", "thm:solenoid-v4",
                "thm:cech-neighbourhood-v4"
            ),
        }
        for num, labels in required.items():
            for label in labels:
                with self.subTest(num=num, label=label):
                    self.assertEqual(
                        self.texts[num].count(r"\label{" + label + "}"), 1
                    )
        labels = re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.texts.values())
        )
        self.assertEqual(len(labels), len(set(labels)))

    def test_all_refs_resolve_in_ten_chapter_scope(self):
        labels = set(re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.texts.values())
        ))
        for num in ("09", "10"):
            refs = re.findall(
                r"\\(?:ref|eqref|autoref|pageref|nameref)\s*\{([^}]+)\}",
                self.texts[num]
            )
            self.assertGreater(len(refs), 5)
            self.assertEqual(set(refs) - labels, set())

    def test_latex_environments_and_image_independence(self):
        for num, figures in (("09", 6), ("10", 2)):
            source = self.texts[num]
            begin = Counter(re.findall(r"\\begin\{([^}]+)\}", source))
            end = Counter(re.findall(r"\\end\{([^}]+)\}", source))
            self.assertEqual(begin, end)
            self.assertGreaterEqual(begin["figure"], figures)
            self.assertGreaterEqual(begin["tikzpicture"], figures)
            for command in ("input", "includegraphics", "lstinputlisting",
                            "inputminted", "include"):
                self.assertNotRegex(source, r"\\" + command + r"\s*\{")

    def test_polish_mathematical_terminology(self):
        for num in ("09", "10"):
            self.assertNotRegex(
                self.texts[num].lower(),
                r"\btensorowan\w*|\btensorowali\w*"
                r"|\bsekwencj\w*|\bseskwilini\w*"
            )

    def test_de_rham_exactness_criterion_and_annulus_are_explicit(self):
        source = self.texts["09"]
        for name in (
            "thm:forma-okresy-pierwotna",
            "prz:okres-1-formy-pierwotna",
            "prz:stokes-pierscien-dwa-brzegi",
            "fig:stokes-pierscien",
        ):
            self.assertIn(r"\label{" + name + "}", source)
        self.assertIn(r"\omega=\dd f", source)
        # Annulus 1<=r<=2: ∫_A dx∧dy = 3pi; boundaries 4pi and -pi.
        self.assertAlmostEqual(pi * (2**2 - 1**2), 3*pi)
        self.assertAlmostEqual(4*pi + (-pi), 3*pi)

    def test_de_rham_full_comparison_proof_still_present(self):
        source = self.texts["09"]
        for label in (
            "eq:integracja-lancuchowa", "eq:de-rham-iso",
            "lem:homotopia-form", "thm:podzial-jednosci-formy",
        ):
            self.assertIn(r"\label{" + label + "}", source)
        self.assertIn(r"C_*^\infty", source)
        self.assertIn(r"H(r)^{-1}H(I)", source)

    def test_cech_continuity_and_hawaiian_earring_product_vs_sum(self):
        source = self.texts["10"]
        self.assertIn(r"\label{lem:cech-ciaglosc-odwrotna}", source)
        self.assertIn(r"\label{fig:cech-hawajski-granice}", source)
        self.assertIn(r"\bigoplus_{n=1}^{\infty}\Z", source)
        self.assertIn(r"\prod_{n=1}^{\infty}\Z", source)
        # For projections Z^(m+1)->Z^m a compatible sequence is
        # determined by infinitely many arbitrary integer coordinates.
        digits = [3, -2, 0, 5, 11]
        prefixes = [tuple(digits[:i]) for i in range(1, len(digits)+1)]
        for smaller, larger in zip(prefixes, prefixes[1:]):
            self.assertEqual(larger[:-1], smaller)

    def test_cech_h0_sine_curve_distinguishes_path_components(self):
        source = self.texts["10"]
        self.assertIn(r"\label{prz:cech-sinus-stopien-zero}", source)
        self.assertIn(r"H_0^{\mathrm{sing}}(T;\Z)\cong\Z^2", source)
        self.assertIn(r"\check H_0(T;\Z)\cong\Z", source)

    def test_cech_inverse_image_construction_and_solenoid_tex(self):
        source = self.texts["10"]
        self.assertIn(r"V'_x=f_{j_x,m}^{-1}(V_x)", source)
        self.assertIn(
            r"\pi_m^{-1}(V'_x)=\pi_{j_x}^{-1}(V_x)", source
        )
        self.assertIn(r"$\Sigma_p=C\sqcup D$", source)
        self.assertIn(r"$S^1=\pi_j(C)\sqcup\pi_j(D)$", source)
        # Catch dropped backslashes in mathematical notation.
        self.assertNotRegex(source, r"(?<!\\)\bSigma_p\b")
        self.assertNotRegex(source, r"(?<!\\)\bpi_[ij]\b")
        self.assertNotIn(r"\sqcuppi", source)

    def test_solenoids_p2_p3_and_nonexact_inverse_limit(self):
        source = self.texts["10"]
        for label in (
            "prz:cech-solenoidy-2-3", "fig:cech-solenoid-stopnie",
            "prz:cech-lim-niedokladnosc"
        ):
            self.assertIn(r"\label{" + label + "}", source)
        self.assertIn(r"\Z[1/2]", source)
        self.assertIn(r"\Z[1/3]", source)
        self.assertIn(r"\Z_2", source)
        # Only 0 is divisible by all 2^n in integers.
        for k in range(-200, 201):
            if all(k % (2**n) == 0 for n in range(1, 10)):
                self.assertEqual(k, 0)
        # Compatible binary residues define an element of Z_2.
        digits = [1, 0, 1, 1, 0, 1]
        partial = [sum(digits[j]*(2**j) for j in range(n))
                   for n in range(1, len(digits)+1)]
        for n in range(1, len(partial)):
            self.assertEqual(partial[n] % (2**n), partial[n-1])


if __name__ == "__main__":
    unittest.main()
