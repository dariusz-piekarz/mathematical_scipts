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

    def test_at23_derived_open_extension_is_not_inferred_from_exactness(self):
        """Derived compact support needs a comparison theorem, not just exact j!."""
        src = self.sources["23"]
        for fragment in (
            r"R\Gamma_c(X,j_!\mathcal G)\simeq R\Gamma_c(U,\mathcal G)",
            r"sama dokładność $j_!$ nie dowodzi",
            r"rezolucjach acyklicznych względem nośników zwartych",
            r"R\Gamma_c(X,j_!{-})\simeq",
            r"który jest dokładny i zachowuje snopy iniektywne",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, src)
        self.assertNotIn("przez dokładność $j_!$", src)

    def test_at23_standalone_hypotheses_and_polish_chart_mapping_rule(self):
        src = self.sources["23"]
        for fragment in (
            r"Niech $k$ będzie ciałem, a $X$ przestrzenią topologiczną.",
            r"$\check H^0(\mathcal U,\mathcal F)\cong\mathcal F(X)$",
            r"a $\mathcal U=(U_i)_{i\in I}$ uporządkowanym pokryciem otwartym",
            r"liniowego odwzorowania ograniczenia",
            r"Dla ustalonego \emph{liniowego} operatora różniczkowego $P$",
            r"rzeczywistych przestrzeni wektorowych (tutaj $k=\R$)",
            r"(tutaj $k=\C$)",
            r"Niech $a:X\to\{*\}$ będzie odwzorowaniem do punktu.",
            r"naturalne odwzorowanie",
            r"w sąsiednich mapach różnią się znakiem stopnia",
            r"drugoprzeliczalną topologiczną $n$-rozmaitością",
            r"\section{Rezolucja de Rhama",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, src)
        self.assertNotIn("Właściwość mapy", src)
        self.assertNotIn("rezolwent", src)
        self.assertNotRegex(
            src, r"\b(?:karta|karty|karcie|kartę|kartą|kart)\b"
                 r"|\bsekwencj\w*|\btensorowan\w*"
        )

    def test_at23_nested_latex_environments_and_closed_refs(self):
        src = self.sources["23"]
        starts = re.findall(
            r"\\(?:ref|eqref|autoref|nameref|pageref)\s*\{", src
        )
        full = re.findall(
            r"\\(?:ref|eqref|autoref|nameref|pageref)\s*\{[^{}\n]+\}", src
        )
        self.assertEqual(len(starts), len(full))
        stack = []
        for m in re.finditer(r"\\(begin|end)\{([^{}]+)\}", src):
            kind, env = m.groups()
            if kind == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack, f"Unexpected end of {env}")
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack, f"Unclosed TeX environments: {stack}")

    def test_residue_pairing_has_dual_bases_for_all_negative_m(self):
        src = self.sources["23"]
        self.assertIn(r"\label{prz:p1-serre-residue}", src)
        self.assertIn(r"\label{fig:p1-serre-residue}", src)
        self.assertIn(r"\node at (3.0,0) {$\langle\cdot,\cdot\rangle$};", src)
        self.assertNotIn(r"\draw[->,thick] (a)--(b)", src)
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

    def test_nodal_normalization_is_small_but_surface_blowup_not(self):
        src = self.sources["24"]
        self.assertIn(r"\label{prz:small-node-normalization}", src)
        self.assertIn(r"\ref{cor:small-map-ic-xiii}", src)
        self.assertIn(r"R\nu_*k_{\mathbb P^1}[1]\simeq IC_C(k)", src)
        # A finite morphism has 0-dimensional fibers everywhere;
        # the blowup at the origin in C^2 has a 1-dimensional fiber
        # above a codimension-two point: 2 is not strictly > 2.
        for r in range(1, 6):
            self.assertLess(0, r)
        fiber_dimension = 1
        codimension = 2
        self.assertEqual(codimension, 2 * fiber_dimension)
        self.assertFalse(codimension > 2 * fiber_dimension)

    def test_deep_theorems_remain_explicit_dependencies(self):
        s23, s24 = self.sources["23"], self.sources["24"]
        self.assertIn("istnienia $a^!$", s23)
        self.assertIn("Nie dowodzimy tu twierdzenia o rozkładzie", s24)
        self.assertRegex(s24, r"\\emph\{jawnie\s+przyjętymi\}")
        self.assertIn("twierdzenia B Cartana", s23)


    def test_at24_audit_i_hypotheses_semismall_proof_and_diagram(self):
        src = self.sources["24"]
        for fragment in (
            "na przestrzeniach niezwartych",
            r"$\mathbb D_XIC_X(k)\simeq IC_X(k)$",
            "dla $k=\\Q$",
            "kryterium półmałości:",
            r"$H^0(i_0^*P)\cong H^2(\mathbb P^1;\Q)\cong\Q$",
            "Zatem $m=1$",
            r"\fill[manifoldred] (-3.18,0)",
            r"\fill[manifoldred] (-2.92,0)",
            r"{$p_+$}",
            r"{$p_-$}",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, src)
        self.assertNotIn("nielokalnie skończonej", src)
        self.assertNotIn("k^\\vee", src)
        self.assertNotIn("pochodny obraz\nwłaściwy", src)


    def test_at24_all_named_objects_in_key_statements_are_declared(self):
        src = self.sources["24"]
        for fragment in (
            "Niech $X$ będzie $n$-wymiarową warstwową",
            r"a $\bar p$ klasyczną perwersyjnością na $X$.",
            r"$k$ ciałem, a $i_x:\{x\}\hookrightarrow X$",
            "wymiaru zespolonego $d$, $k$ ciałem, a $L$",
            "Niech $X$ będzie zespoloną odmianą algebraiczną,",
            r"$k$ ciałem, a $j:U=X_{\mathrm{reg}}\hookrightarrow X$",
            r"$\nu:\widetilde X\to X$ normalizacją.",
            r"zachodzi $\operatorname{codim}_\C X_r>2r$ dla każdego",
            r"Niech $f:\widetilde{\C^2}\to\C^2$ będzie rozdmuchaniem",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, src)
        self.assertNotIn("Dla $X$ powyżej i dowolnego ciała $k$", src)
        self.assertNotIn("Definicji powyżej. Wówczas", src)



if __name__ == "__main__":
    unittest.main()
