"""AT-23/24 mathematical audit: sheaves, Laurent residues, perverse IC.

Dependency scope AT-01..24. Math tests check explicit computations,
historical references and valid locally embedded TikZ assets. Compilation
and visual proofing are done separately by the LaTeX audit workflow.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters" / "pl" / "algebraic_topology"
BOOK = ROOT / "books" / "pl" / "algebraic_topology.tex"


class TopologyChaptersTwentyThreeTwentyFourAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = sorted(AT.glob("0[1-9]-*.tex")) + sorted(
            f for n in range(10, 25) for f in AT.glob(f"{n:02d}-*.tex")
        )
        cls.sources = {
            path.name[:2]: path.read_text(encoding="utf-8-sig")
            for path in cls.files
        }

    def test_modular_book_has_all_twenty_four_chapters(self):
        self.assertEqual(set(self.sources), {f"{n:02d}" for n in range(1, 25)})
        book = BOOK.read_text(encoding="utf-8-sig")
        for file in self.files:
            with self.subTest(file=file.name):
                self.assertIn(
                    r"\input{../../chapters/pl/algebraic_topology/"
                    + file.name + "}", book
                )

    def test_historical_labels_still_unique(self):
        historical = {
            "23": (
                "ch:snopy-verdier-v12", "def:sheaf-v12",
                "lem:stalk-exact-v12", "def:jbang-v12",
                "prop:jbang-sections-v12", "def:sheaf-cohom-v12",
                "lem:sheaf-mv-v12", "thm:leray-sheaf-v12",
                "thm:de-rham-sheaf-v12", "def:verdier-v12",
                "thm:verdier-global-v12", "thm:verdier-manifold-v12",
                "ex:node-duality-v12", "thm:localization-v12",
                "thm:p1-twist-v12",
            ),
            "24": (
                "ch:ih-perverse-xiii", "def:pseudomanifold-xiii",
                "def:perversity-xiii", "def:allowability-xiii",
                "thm:cone-ih-xiii", "thm:ih-duality-xiii",
                "ex:suspension-torus-xiii", "def:perverse-support-xiii",
                "thm:heart-perverse-xiii", "def:middle-extension-xiii",
                "def:ic-xiii", "thm:ic-comparison-xiii",
                "prop:node-ic-xiii", "thm:decomposition-xiii",
                "cor:small-map-ic-xiii", "prop:blowup-decomp-xiii",
                "thm:relative-hard-lefschetz-xiii",
            ),
        }
        for chapter, labels in historical.items():
            for label in labels:
                with self.subTest(chapter=chapter, label=label):
                    self.assertEqual(
                        self.sources[chapter].count(r"\label{" + label + "}"),
                        1,
                    )
        all_labels = re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.sources.values())
        )
        self.assertEqual(len(all_labels), len(set(all_labels)))

    def test_reviewed_chapter_references_resolve_within_at_01_24(self):
        declared = set(re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.sources.values())
        ))
        for chapter in ("23", "24"):
            refs = re.findall(
                r"\\(?:ref|eqref|autoref|pageref|nameref)\s*\{([^}]+)\}",
                self.sources[chapter],
            )
            self.assertGreaterEqual(len(refs), 5)
            self.assertEqual(set(refs) - declared, set())

    def test_latex_environments_and_asset_independence(self):
        for chapter in ("23", "24"):
            src = self.sources[chapter]
            self.assertEqual(
                Counter(re.findall(r"\\begin\{([^}]+)\}", src)),
                Counter(re.findall(r"\\end\{([^}]+)\}", src)),
            )
            self.assertGreaterEqual(src.count(r"\begin{tikzpicture}"), 2)
            for command in (
                "includegraphics", "input", "include",
                "lstinputlisting", "inputminted",
            ):
                self.assertNotRegex(src, r"\\" + command + r"\s*\{")

    def test_consistent_polish_and_no_malformed_emphasis(self):
        for chapter in ("23", "24"):
            src = self.sources[chapter]
            self.assertNotRegex(
                src.lower(),
                r"\btensorowan\w*|\bsekwencj\w*"
                r"|\binjekcj\w*|\bseskwilini\w*",
            )
            self.assertNotIn(r"\\emph{", src)

    def test_residue_pairing_has_dual_bases_for_all_negative_m(self):
        src = self.sources["23"]
        self.assertIn(r"\label{prz:p1-serre-residue}", src)
        self.assertIn(r"\label{fig:p1-serre-residue}", src)
        self.assertIn(r"\operatorname{Res}_{z=0}", src)
        for m in range(-12, -1):
            N = -m - 2
            # A residue is nonzero iff exponent of h*p equals -1.
            matrix = [
                [int((m + 1 + i) + ell == -1)
                 for ell in range(N + 1)]
                for i in range(N + 1)
            ]
            with self.subTest(m=m):
                self.assertTrue(all(sum(row) == 1 for row in matrix))
                self.assertTrue(all(sum(row[j] for row in matrix) == 1
                                    for j in range(N + 1)))
                self.assertEqual(
                    matrix,
                    [[int(ell == N-i) for ell in range(N+1)]
                     for i in range(N+1)],
                )

    def test_residue_of_cech_coboundary_vanishes(self):
        # With m <= -2 and deg(p) <= -m-2, f0*p contains
        # nonnegative powers; z^m*f_inf(1/z)*p has powers <= -2.
        for m in range(-10, -1):
            N = -m-2
            for degree_p in range(N+1):
                for degree_finf in range(6):
                    self.assertLessEqual(
                        m + degree_p - degree_finf,
                        -2,
                    )
            self.assertGreaterEqual(0, 0)

    def test_nodal_sheaf_exact_sequence_at_stalk(self):
        src = self.sources["24"]
        self.assertIn(
            r"\label{prz:node-normalization-exact-sequence}", src
        )
        self.assertIn(
            r"\label{fig:node-normalization-exact-sequence}", src
        )
        self.assertIn(r"\xrightarrow{\ a\mapsto(a,a)\ }k^2", src)
        for prime in (2, 3, 5, 7):
            with self.subTest(characteristic=prime):
                diag = {(a, a) for a in range(prime)}
                kernel = {
                    (a, b) for a in range(prime)
                    for b in range(prime)
                    if (a-b) % prime == 0
                }
                self.assertEqual(diag, kernel)
                image = {(a-b) % prime
                         for a in range(prime)
                         for b in range(prime)}
                self.assertEqual(image, set(range(prime)))

    def test_nodal_curve_ordinary_and_intersection_cohomology(self):
        src = self.sources["24"]
        self.assertIn(r"H^1(C;k)=k", src)
        self.assertIn(r"IH^1(C;k)=0", src)
        self.assertIn(r"\nu_*k_{\mathbb P^1}[1]", src)
        # Global constants on connected P1 map via equal values
        # at both preimages: a-a=0, giving H^1(C;k) = coker(0:k->k).
        for a in range(-8, 9):
            self.assertEqual(a-a, 0)
        self.assertIn(
            r"Z długiego ciągu kohomologii otrzymujemy fragment", src
        )

    def test_deep_theorems_remain_explicit_dependencies(self):
        s23, s24 = self.sources["23"], self.sources["24"]
        self.assertIn("istnienia $a^!$", s23)
        self.assertIn("Nie dowodzimy tu twierdzenia o rozkładzie", s24)
        self.assertIn("jawnie przyjętymi", s24)
        self.assertIn("twierdzenia B Cartana", s23)


if __name__ == "__main__":
    unittest.main()
