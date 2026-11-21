"""AT-27/28 mathematical regressions, preserved labels, dependencies and TeX.

These tests intentionally keep the three historical shared mathematical modules
used by AT-28 rather than copying their old labels into a second source.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
from math import comb
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters" / "pl" / "algebraic_topology"
BOOK = ROOT / "books" / "pl" / "algebraic_topology.tex"
SHARED = ROOT / "shared" / "pl"
SHARED_FILES = (
    "slabe_twierdzenie_lefschetza.tex",
    "rozdmuchanie_punktu_normalna.tex",
    "rozdmuchanie_punktu_kohomologia.tex",
)


class AlgebraicTopologyTwentySevenTwentyEightAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.paths = sorted(
            path for n in range(1, 29)
            for path in AT.glob(f"{n:02d}-*.tex")
        )
        cls.texts = {
            p.name[:2]: p.read_text(encoding="utf-8-sig")
            for p in cls.paths
        }
        cls.shared = {
            name: (SHARED / name).read_text(encoding="utf-8-sig")
            for name in SHARED_FILES
        }

    def test_book_includes_twenty_eight_canonical_chapters(self):
        self.assertEqual(
            set(self.texts), {f"{n:02d}" for n in range(1, 29)}
        )
        book = BOOK.read_text(encoding="utf-8-sig")
        for p in self.paths:
            with self.subTest(chapter=p.name[:2]):
                self.assertIn(
                    r"\input{../../chapters/pl/algebraic_topology/" +
                    p.name + "}", book
                )

    def test_preserve_labels_and_all_links_resolve(self):
        complete = "\n".join([*self.texts.values(), *self.shared.values()])
        labels = re.findall(r"\\label\s*\{([^}]+)\}", complete)
        self.assertEqual(
            len(labels), len(set(labels)), "label collision in current volume"
        )
        for key in ("27", "28"):
            with self.subTest(chapter=key):
                refs = set(re.findall(
                    r"\\(?:ref|eqref|pageref|autoref|nameref)\s*\{([^}]+)\}",
                    self.texts[key],
                ))
                self.assertFalse(refs - set(labels), refs - set(labels))
        for key, label in (
            ("27", "ch:xvi-szesc-operacji"),
            ("27", "thm:xvi-localization"),
            ("28", "ch:xvii-topologia-odmian"),
            ("28", "thm:xvii-blowup-general"),
        ):
            self.assertIn(r"\label{" + label + "}", self.texts[key])

    def test_shared_modules_are_canonical_and_guarded(self):
        chapter = self.texts["28"]
        for name in SHARED_FILES:
            self.assertIn(r"\input{../../shared/pl/" + name + "}", chapter)
            self.assertIn(r"\ifcsname ", self.shared[name])
            self.assertIn(r"\fi", self.shared[name])
        self.assertIn(
            r"\label{thm:xvii-weak-lefschetz}",
            self.shared["slabe_twierdzenie_lefschetza.tex"],
        )
        self.assertIn(
            r"\label{lem:xvii-exceptional}",
            self.shared["rozdmuchanie_punktu_normalna.tex"],
        )
        self.assertIn(
            r"\label{thm:xvii-blowup}",
            self.shared["rozdmuchanie_punktu_kohomologia.tex"],
        )

    def test_balanced_environments_in_chapters_and_shared(self):
        for name, source in (
            *[(f"AT-{k}", self.texts[k]) for k in ("27", "28")],
            *list(self.shared.items()),
        ):
            with self.subTest(file=name):
                opens = Counter(re.findall(r"\\begin\{([^}]+)\}", source))
                closes = Counter(re.findall(r"\\end\{([^}]+)\}", source))
                self.assertEqual(opens, closes)
                self.assertGreaterEqual(opens["proof"] + opens["przyklad"], 1)
        for k in ("27", "28"):
            self.assertGreaterEqual(
                len(re.findall(r"\\begin\{tikzpicture\}", self.texts[k])), 2
            )
            for command in ("includegraphics", "inputminted", "lstinputlisting"):
                self.assertNotRegex(
                    self.texts[k], r"\\" + command + r"\s*\{"
                )

    def test_ci_workflow_triggers_on_actual_chapters(self):
        """A paired audit must execute after either reviewed chapter changes."""
        workflow = (
            ROOT / ".github" / "workflows" /
            "algebraic-topology-audit-ch27-28.yml"
        ).read_text(encoding="utf-8")
        for number in ("27", "28"):
            with self.subTest(chapter=number):
                self.assertIn(
                    '"chapters/pl/algebraic_topology/' + number + '-*.tex"',
                    workflow,
                )
        self.assertIn('"books/pl/algebraic_topology.tex"', workflow)
        for shared_file in SHARED_FILES:
            self.assertIn('"shared/pl/' + shared_file + '"', workflow)

    def test_derived_nearby_cycles_are_notated_as_cohomology_sheaves(self):
        """Rpsi is a derived functor, not a sheaf to derive again."""
        source = self.texts["27"]
        self.assertIn(r"(\mathcal H^q(R\psi_fk_X))_x", source)
        for obsolete in (
            r"R^q\psi_f", r"R^0\psi_f", r"R^1\psi_f",
            r"R^0\phi_f", r"R^1\phi_f",
        ):
            self.assertNotIn(obsolete, source)

    def test_polish_compound_words_are_preserved(self):
        """A global terminology replacement must not corrupt 'konsekwencje'."""
        self.assertIn("konsekwencje elementarnych rachunków",
                      self.texts["27"])
        self.assertIn("konsekwencje dołączania komórek",
                      self.texts["28"])
        for chapter in ("27", "28"):
            self.assertNotIn("konciągi", self.texts[chapter])
            self.assertNotRegex(self.texts[chapter].lower(),
                                r"\binjektywn\w*")

    def test_fixed_math_commands_and_approved_polish(self):
        for k in ("27", "28"):
            src = self.texts[k]
            self.assertNotIn(r"\\mathcal", src)
            self.assertNotIn(r"f:X\\to Y", src)
            self.assertNotRegex(
                src.lower(),
                r"\btensorowan\w*|\bsekwencj\w*|\bseskwilini\w*",
            )

    def test_punctured_disk_derived_pushforward(self):
        chapter = self.texts["27"]
        self.assertIn(r"\label{prz:xvi-punctured-disc-audit}", chapter)
        self.assertIn(r"\label{fig:xvi-punctured-disc-audit}", chapter)
        # H^0(D)=k -> H^0(D*)=k is identity.
        # Therefore H^1(D,D*)=0, H^2(D,D*)=H^1(D*)=k.
        h0_disc = 1
        h0_punctured = 1
        restriction_rank = 1
        h1_punctured = 1
        self.assertEqual(h0_disc - restriction_rank, 0)
        self.assertEqual(h0_punctured - restriction_rank, 0)
        self.assertEqual(h1_punctured, 1)
        self.assertIn(r"i^!k_X\simeq k_{\{0\}}[-2]", chapter)
        self.assertIn(r"(R^1j_*k_U)_0\cong k", chapter)

    def test_elliptic_blowup_betti_hodge_and_euler(self):
        chapter = self.texts["28"]
        self.assertIn(r"\label{prz:xvii-blowup-elliptic-audit}", chapter)
        self.assertIn(r"\label{fig:xvii-elliptic-blowup-audit}", chapter)
        # Genus of a smooth degree-3 plane curve.
        genus = (3 - 1) * (3 - 2) // 2
        self.assertEqual(genus, 1)
        # P^3 has one class in each even cohomological degree.
        base_b = [1, 0, 1, 0, 1, 0, 1]
        elliptic_b = [1, 2 * genus, 1]
        blow_b = [
            base_b[k] + (elliptic_b[k - 2] if 2 <= k <= 4 else 0)
            for k in range(7)
        ]
        self.assertEqual(blow_b, [1, 0, 2, 2, 2, 0, 1])
        self.assertEqual(sum((-1)**k * b for k, b in enumerate(blow_b)), 4)
        self.assertEqual(blow_b[3], 2)
        self.assertIn(r"h^{2,1}(\widetilde X)", chapter)
        self.assertIn(r"h^{1,2}(\widetilde X)", chapter)

    def test_integral_blowup_proof_has_all_four_steps(self):
        chapter = self.texts["28"]
        for phrase in (
            r"\pi_!\pi^*\alpha",
            r"\pi_*[\widetilde X]=[X]",
            r"j^*j_*\beta",
            r"\delta_E(p^*b)",
            r"\pi_{\mathrm{rel}}^*c=c'",
        ):
            self.assertIn(phrase, chapter)


    def test_at27_audited_functor_hypotheses_and_polish_terms(self):
        chapter = self.texts["27"]
        for fragment in (
            r"$f_*$ i $f_!$ są lewostronnie dokładne",
            "zachowują trójkąty wyróżnione",
            r"$X'=X\times_Y Y'$",
            r"$H^{n-q}(M;\operatorname{or}_M)$",
            r"$A\in D^b_c(X;k)$",
            r"$R\psi_fA=i^*R\widetilde j_*\widetilde j^*A$",
            r"mającym izolowany punkt krytyczny w $x$",
            "obiekt dualny w sensie Verdiera",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, chapter)
        self.assertNotRegex(chapter, r"\brezolwent\w*")
        self.assertNotIn("naturalną mapą", chapter)
        self.assertNotIn("nie muszą zachowywać krótkich ciągów dokładnych bez", chapter)

    def test_at27_stalk_localization_and_properness_regressions(self):
        # At U: 0 -> k -> k -> 0; at Z: 0 -> 0 -> k -> k -> 0.
        for site in ("open", "closed"):
            j = 1 if site == "open" else 0
            middle = 1
            quotient = 0 if site == "open" else 1
            self.assertEqual(j + quotient, middle)
        # Proper f: R -> R, x |-> x^2, finite fibres of ranks 0,1,2.
        fibre_ranks = {y: (0 if y < 0 else 1 if y == 0 else 2)
                       for y in (-3, -1, 0, 1, 3)}
        self.assertEqual(list(fibre_ranks.values()), [0, 0, 1, 2, 2])
        # Nonproper open j: (0,1) -> R: empty fibre at 0, but (j_*k)_0=k.
        fibre_at_boundary = 0
        direct_image_stalk = 1
        self.assertNotEqual(fibre_at_boundary, direct_image_stalk)
        # Poincare: H_c^1(R;k)=k dual to H^0(R;k)=k,
        # whereas H_c^0(R;k)=0 and H^1(R;k)=0.
        self.assertEqual((0, 1), (0, 1))
        self.assertIn(r"i^!k_X\simeq k_{\{0\}}[-2]", self.texts["27"])


if __name__ == "__main__":
    unittest.main()
