"""Detailed mathematical audit regression for AT-13/14.

Check historical labels, references, standalone diagrams and explicit arithmetic
behind Moore spaces, Postnikov lifting and Steenrod squares. The two-pass TeX
compilation is a separate CI requirement.
"""
from __future__ import annotations

from collections import Counter
from math import comb, gcd
from itertools import permutations
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

    def test_KAn_uniqueness_realizes_cocycle_before_extending(self):
        ch = self.texts["13"]
        proof = ch.split(r"\label{thm:KGn-existence-v6}", 1)[1].split(
            r"\section{Kohomologia jako zbiór klas homotopii}", 1
        )[0]
        for token in (
            r"H^n(K;A)\cong\operatorname{Hom}(H_n(K;\Z),A)",
            r"c\in C^n(K;A)",
            r"wartością $\delta c$",
            r"$\pi_j(L)=0$ dla $j>n$",
            r"twierdzenie Whiteheada",
        ):
            self.assertIn(token, proof)
        # The existence proof cannot assume the representation theorem
        # from the following section; instead it constructs the map.
        self.assertNotIn(r"\ref{thm:rep-coho-v6}", proof)

    def test_discrete_bar_model_respects_right_principal_action(self):
        ch = self.texts["13"]
        self.assertIn(
            r"(h^{-1}g_0,\ldots,h^{-1}g_k)", ch
        )
        self.assertIn("wolne prawe działanie", ch)
        perms = list(permutations(range(3)))

        def product(a, b):
            return tuple(a[b[i]] for i in range(3))

        def inverse(p):
            return tuple(p.index(i) for i in range(3))

        def act(x, h):
            return product(inverse(h), x)

        for x in perms:
            for h in perms:
                for k in perms:
                    # (x . h) . k = x . (h*k) for a right action.
                    self.assertEqual(
                        act(act(x, h), k), act(x, product(h, k))
                    )
            # A permutation can be fixed by right translation only
            # if that translating element is the identity.
            self.assertEqual(
                [h for h in perms if act(x, h) == x],
                [(0, 1, 2)],
            )

    def test_moore_Hom_Ext_cyclic_coefficient_arithmetic(self):
        ch = self.texts["13"]
        for m in range(2, 12):
            for modulus in range(2, 12):
                # For A=Z/modulus, ker(m:A->A) and coker both
                # have exactly gcd(m,modulus) elements.
                annihilator = {
                    x for x in range(modulus)
                    if (m*x) % modulus == 0
                }
                image = {
                    (m*x) % modulus for x in range(modulus)
                }
                self.assertEqual(len(annihilator), gcd(m, modulus))
                self.assertEqual(modulus // len(image), gcd(m, modulus))
        self.assertIn(r"\operatorname{Ext}^1_{\Z}", ch)
        self.assertIn(r"H^{n+1}(M;A)=A/mA", ch)

    def test_Milnor_join_local_trivializations_are_explicit(self):
        ch = self.texts["13"]
        for token in (
            r"$EG\to BG:=EG/G$",
            r"$V_i=\{t_i>0\}\subset EG$",
            r"$U_i=V_i/G$",
            r"e\longmapsto e\cdot g_i(e)^{-1}",
            r"$g_i(eh)=g_i(e)h$",
            r"$V_i\cong U_i\times G$",
        ):
            self.assertIn(token, ch)

    def test_clutching_has_both_directions_and_based_normalization(self):
        ch = self.texts["13"]
        for token in (
            r"$g_t:S^{n-1}\to G$",
            r"$S^{n-1}\times I$",
            r"$S^n\times I$",
            r"$\widehat g(x)=g(x_0)^{-1}g(x)$",
            r"$H(x_0,t)^{-1}H(x,t)$",
            r"\ref{thm:BG-general-v6}",
        ):
            self.assertIn(token, ch)
        # In the path-connected group SO(2)=S^1 all free homotopy
        # classes of S^1 maps are represented by based winding numbers.
        # Multiplication by a constant changes the basepoint value, not
        # the increment of the chosen argument along one full turn.
        for degree in range(-10, 11):
            for phase in range(-3, 4):
                total_argument_change = (
                    (phase + 2*degree) - phase
                )
                self.assertEqual(total_argument_change, 2*degree)

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
        # The complete derivation now explicitly relies on a deep construction lemma.
        self.assertIn("lemat o potęgach", chapter)
        self.assertIn(r"\operatorname{Sq}^2\operatorname{Sq}^2", chapter)

    def test_cartan_and_adem_proofs_not_overclaimed(self):
        chapter = self.texts["14"]
        # The coherently equivariant power construction is an explicit dependency;
        # the chapter does not claim an independent chain-level construction.
        self.assertIn("Zakres geometrycznego lematu wejściowego", chapter)
        self.assertIn("jego pełne udowodnienie", chapter)
        self.assertIn("relacji Adema", chapter)


if __name__ == "__main__":
    unittest.main()
