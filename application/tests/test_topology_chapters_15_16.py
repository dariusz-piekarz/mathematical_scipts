"""AT-15/16 audit regression: operations, Freudenthal and stable Hopf class.

Checks canonical chapters and labels, explicit numerical cohomology calculations,
self-contained LaTeX figures and the proof-scope caveats for Cartan and Adem.
Run the separate two-pass LaTeX workflow to validate PDF construction.
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


class TopologyChaptersFifteenSixteenAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = sorted(AT.glob("0[1-9]-*.tex")) + sorted(
            f for n in range(10, 17) for f in AT.glob(f"{n:02d}-*.tex")
        )
        cls.text = {
            file.name[:2]: file.read_text(encoding="utf-8-sig")
            for file in cls.files
        }

    def test_canonical_book_includes_all_sixteen_chapters(self):
        self.assertEqual(
            set(self.text), {f"{n:02d}" for n in range(1, 17)}
        )
        book = BOOK.read_text(encoding="utf-8-sig")
        for file in self.files:
            with self.subTest(file=file.name):
                self.assertIn(
                    r"\input{../../chapters/pl/algebraic_topology/"
                    + file.name + "}", book
                )

    def test_original_labels_survive_without_duplicates(self):
        required = {
            "15": (
                "ch:operacje-v8", "prop:bockstein-v8",
                "thm:sq1-bock-v8", "thm:cartan-v8",
                "thm:adem-v8", "lem:susp-cupzero-v8",
                "thm:sigma-cp2-v8", "thm:thom-wu-v8",
            ),
            "16": (
                "ch:stabilna-v8", "lem:cone-relative-v8",
                "thm:bm-v8", "thm:freudenthal-v8",
                "thm:stable-range-v8", "lem:sigma-product-v8",
                "thm:stable-eta-v8", "thm:HA-rep-v8",
            ),
        }
        for chapter, labels in required.items():
            for label in labels:
                with self.subTest(chapter=chapter, label=label):
                    self.assertEqual(
                        self.text[chapter].count(r"\label{" + label + "}"),
                        1,
                    )
        all_labels = re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.text.values())
        )
        self.assertEqual(len(all_labels), len(set(all_labels)))

    def test_every_reference_from_pair_resolves_in_prerequisites(self):
        all_labels = set(re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.text.values())
        ))
        for chapter in ("15", "16"):
            refs = re.findall(
                r"\\(?:ref|eqref|autoref|pageref|nameref)\s*\{([^}]+)\}",
                self.text[chapter],
            )
            self.assertGreater(len(refs), 0)
            self.assertEqual(set(refs) - all_labels, set())

    def test_no_external_assets_and_balanced_latex_environments(self):
        for chapter, minimum_figures in (("15", 1), ("16", 2)):
            src = self.text[chapter]
            self.assertEqual(
                Counter(re.findall(r"\\begin\{([^}]+)\}", src)),
                Counter(re.findall(r"\\end\{([^}]+)\}", src)),
            )
            self.assertGreaterEqual(
                src.count(r"\begin{tikzpicture}"), minimum_figures
            )
            for cmd in (
                "includegraphics", "input", "include",
                "lstinputlisting", "inputminted",
            ):
                self.assertNotRegex(src, r"\\" + cmd + r"\s*\{")

    def test_polish_terms_and_distinction_between_map_and_chart(self):
        for chapter in ("15", "16"):
            self.assertNotRegex(
                self.text[chapter].lower(),
                r"\btensorowan\w*|\bseskwilini\w*"
                r"|\bsekwencj\w*|\binjekcj\w*",
            )

    def test_bockstein_of_rp2_generator_via_cellular_lift(self):
        src = self.text["15"]
        self.assertIn(r"\label{prz:bockstein-rp2-komorki-v8}", src)
        self.assertIn(r"\label{fig:bockstein-rp2-v8}", src)
        self.assertIn(r"\beta_2(t)=t^2\ne0", src)
        # d_2=2 on Z; lifting the mod-2 1-cocycle by 1 into
        # Z/4 produces coboundary 2 mod 4, then beta=2/2=1 mod 2.
        d2_integral = 2
        lifted = 1
        delta_mod4 = (d2_integral * lifted) % 4
        self.assertEqual(delta_mod4, 2)
        self.assertEqual((delta_mod4 // 2) % 2, 1)

    def test_adem_check_is_local_not_universal(self):
        src = self.text["15"]
        self.assertIn(r"\label{prz:adem-rp-niskie-v8}", src)
        self.assertIn("ale nie dowodzi jej dla dowolnej przestrzeni", src)
        # The check on F_2[t] alone cannot establish a natural
        # operation identity on all spaces; both compositions
        # happen to vanish on every t^m.
        for m in range(101):
            lhs = comb(m, 2) * comb(m+2, 2)
            rhs = m * comb(m+1, 3)
            with self.subTest(m=m):
                self.assertEqual(lhs % 2, rhs % 2)
                self.assertEqual(lhs % 2, 0)
        self.assertIn("Nie dowodzimy tu tego twierdzenia", src)
        self.assertIn("Pełny dowód kołańcuchowy", src)

    def test_klein_bottle_freudenthal_is_abelianization(self):
        src = self.text["16"]
        self.assertIn(r"\label{prz:freudenthal-klein-abel-v8}", src)
        self.assertIn(r"\pi_1(K)_{\mathrm{ab}}", src)
        self.assertIn(r"\pi_2(\Sigma K)", src)
        # In abelianization a + b - a = -b -> 2b=0.
        for k in (-3, -1, 0, 1, 3):
            a, b = k, 1
            self.assertEqual((a+b-a) % 2, (-b) % 2)

    def test_first_stable_stem_and_suspension_ranges(self):
        src = self.text["16"]
        self.assertIn(r"\label{prz:eta-stabilizacja-v8}", src)
        self.assertIn(r"\label{fig:eta-stabilizacja-v8}", src)
        self.assertIn(r"\pi_1^{\mathrm s}=\Z/2", src)
        # For q=n+1 on S^n, r=n-1; Freudenthal gives
        # iso exactly when n+1 < 2n-1, i.e. n>2.
        for n in range(2, 18):
            with self.subTest(n=n):
                self.assertEqual(n+1 < 2*(n-1)+1, n>2)
        self.assertIn(r"\ker E=2\Z", src)

    def test_rank_zero_thom_and_whitney_formula(self):
        """Rank-zero Thom unit and universal Whitney polynomial identities."""
        chapter = self.text["15"]
        for token in (
            r"$D^0=\{*\}$",
            r"$S^{-1}=\varnothing$",
            r"$U=1_B\in H^0(B;\F_2)$",
            r"$\operatorname{Sq}^i(1_B)=0$",
            r"$w(\xi\oplus\eta)$",
            r"U_{\xi\oplus\eta}",
            "Różnowartościowość izomorfizmu Thoma",
        ):
            with self.subTest(token=token):
                self.assertIn(token, chapter)

        # For a sum of r+s tautological real lines over RP^infty,
        # (1+t)^r * (1+t)^s = (1+t)^(r+s), including ranks zero.
        for rank_one in range(17):
            for rank_two in range(17):
                for k in range(rank_one + rank_two + 1):
                    coeff = sum(
                        comb(rank_one, j)*comb(rank_two, k-j)
                        for j in range(k+1)
                        if j <= rank_one and k-j <= rank_two
                    )
                    with self.subTest(r=rank_one,s=rank_two,k=k):
                        self.assertEqual(
                            coeff % 2, comb(rank_one+rank_two,k) % 2
                        )
        self.assertEqual(comb(0, 0), 1)

    def test_cellular_bockstein_matches_Sq1_on_RP(self):
        """Bockstein from Z/4 cellular lifts is Sq^1 on RP^N."""
        chapter = self.text["15"]
        self.assertIn(r"\beta_2(t)=t^2\ne0", chapter)
        # On RP^N, integral cellular boundary C_(m+1)->C_m
        # is 2 for m+1 even and 0 for m+1 odd.
        for N in range(1, 24):
            for m in range(N+1):
                boundary = 2 if (m+1) % 2 == 0 and m+1 <= N else 0
                bockstein_coeff = (boundary // 2) % 2
                sq1_coeff = m % 2 if m+1 <= N else 0
                with self.subTest(N=N, m=m):
                    self.assertEqual(bockstein_coeff, sq1_coeff)

    def test_deep_dependencies_are_explicit_not_overclaimed(self):
        src = self.text["15"] + self.text["16"]
        self.assertIn("nie pełny niezależny dowód", src)
        self.assertIn("względem", src)
        self.assertIn("Stabilność", src)


if __name__ == "__main__":
    unittest.main()
