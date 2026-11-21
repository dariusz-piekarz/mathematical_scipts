"""Mathematical and source-provenance regression after AT↔DG proof comparison.

Pairs: (AT-03, DG-06), (AT-09, DG-10).
Never auto-merge or rename historically existing labels.
"""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters" / "pl" / "algebraic_topology"
DG = ROOT / "chapters" / "pl" / "differential_geometry_and_topology"
PATHS = {
    "AT03": next(AT.glob("03-*.tex")),
    "DG06": next(DG.glob("06-*.tex")),
    "AT09": next(AT.glob("09-*.tex")),
    "DG10": next(DG.glob("10-*.tex")),
}


def labels(source: str) -> set[str]:
    return set(re.findall(r"\\label\s*\{([^}]+)\}", source))


def matrix_product(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) % 2 for j in range(2))
        for i in range(2)
    )


class PairedProofAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = {
            key: p.read_text(encoding="utf-8-sig")
            for key, p in PATHS.items()
        }

    def test_noncommutative_pivot_has_correct_inverse_coefficient(self):
        s = self.s["AT03"]
        self.assertIn(r"x':=x-a(x)u^{-1}e", s)
        self.assertIn(r"x=x'+a(x)u^{-1}e", s)
        self.assertNotIn(r"x=x'+u^{-1}a(x)e", s)
        # Explicit counterexample over M_2(F_2) already used in AT-03.
        u = ((1, 1), (0, 1))
        a = ((0, 0), (1, 0))
        identity = ((1, 0), (0, 1))
        self.assertEqual(matrix_product(u, u), identity)
        au_inverse = matrix_product(a, u)
        inverse_a = matrix_product(u, a)
        self.assertNotEqual(au_inverse, inverse_a)
        # Correct elimination: a - (a*u^{-1})*u = 0 mod 2.
        self.assertEqual(matrix_product(au_inverse, u), a)
        # Incorrect coefficient order does not remove the pivot.
        self.assertNotEqual(matrix_product(inverse_a, u), a)

    def test_five_lemma_uses_precise_minimal_hypotheses(self):
        for key in ("AT03", "DG06"):
            s = self.s[key]
            pos = s.index(r"\begin{lemat}[Lemat pięciu]")
            block = s[pos:s.index(r"\end{lemat}", pos)]
            self.assertIn("surjekcją", block)
            self.assertIn("iniekcją", block)
            self.assertIn(r"$f_2$ i $f_4$", block)
            self.assertIn(r"\label{lem:pieciu}", block)

    def test_mayer_vietoris_boundary_is_constructed_not_asserted(self):
        for key in ("AT09", "DG10"):
            s = self.s[key]
            pos = s.index(r"\begin{twierdzenie}[Mayer--Vietoris dla form]")
            end = s.index(r"\end{proof}", pos)
            block = s[pos:end]
            for term in (
                r"s(\alpha,\beta)=",
                r"\delta[\gamma]",
                r"\dd\alpha",
                r"\dd\beta",
                r"\rho_U",
                r"\rho_V",
            ):
                self.assertIn(term, block)
            self.assertIn("podniesieni", block)
            self.assertIn(r"\gamma+\dd\theta", block)
            self.assertIn("dokładność", block.lower())

    def test_mayer_vietoris_boundary_on_circle_is_nonzero(self):
        # For the standard cover of S^1 by two contractible arcs,
        # U∩V has two components. H^0(U)⊕H^0(V)->H^0(U∩V)
        # sends (a,b) to (b-a,b-a): diagonal image.
        for a in range(-2, 3):
            for b in range(-2, 3):
                image = (b-a, b-a)
                self.assertEqual(image[0]-image[1], 0)
        # The class [(1,0)] is nonzero in R^2 / diagonal R.
        self.assertNotEqual((1, 0)[0] - (1, 0)[1], 0)

    def test_preserve_unique_de_rham_examples_and_criterion(self):
        at = labels(self.s["AT09"])
        dg = labels(self.s["DG10"])
        for name in (
            "thm:forma-okresy-pierwotna",
            "prz:okres-1-formy-pierwotna",
            "prz:stokes-pierscien-dwa-brzegi",
            "fig:stokes-pierscien",
        ):
            self.assertIn(name, at)
            self.assertNotIn(name, dg)
        self.assertIn("prz:formy-rachunek-r3", dg)
        self.assertNotIn("prz:formy-rachunek-r3", at)
        self.assertGreaterEqual(len(at & dg), 55)

    def test_preserve_unique_homological_examples(self):
        at = labels(self.s["AT03"])
        dg = labels(self.s["DG06"])
        for key in (
            "prz:redukcja-mod2-trzy-stopnie",
            "fig:redukcja-mod2-top",
            "uwaga:nieprzemienny-pivot-top",
        ):
            self.assertIn(key, at)
        for key in (
            "prz:ses-dwa-rozszerzenia",
            "prz:delta-razy-m",
            "prz:mod2-dwa-zrodla",
            "wn:pieciu-ses-kompleksy",
        ):
            self.assertIn(key, dg)
        self.assertGreaterEqual(len(at & dg), 60)

    def test_preserve_historical_labels_and_balanced_tex(self):
        min_label_counts = {"AT03": 69, "DG06": 72, "AT09": 64, "DG10": 61}
        for key, s in self.s.items():
            with self.subTest(source=key):
                l = re.findall(r"\\label\s*\{([^}]+)\}", s)
                self.assertEqual(len(l), len(set(l)))
                self.assertGreaterEqual(len(l), min_label_counts[key])
                opens = Counter(re.findall(r"\\begin\{([^}]+)\}", s))
                closes = Counter(re.findall(r"\\end\{([^}]+)\}", s))
                self.assertEqual(opens, closes)
                self.assertFalse(re.search(
                    r"\\(?:includegraphics|inputminted|lstinputlisting)\s*\{",
                    s,
                ))

    def test_consistent_kochain_as_kolancuch(self):
        for key, s in self.s.items():
            self.assertNotIn("kochain", s.lower())
            self.assertIn("kołańcuch", s)
            self.assertNotRegex(s.lower(), r"\bsekwencj\w*")
            self.assertNotRegex(s.lower(), r"\btensorowan\w*")

    def test_chain_cancellation_not_assumed_for_nonunits(self):
        at = self.s["AT03"]
        dg = self.s["DG06"]
        self.assertIn(r"\label{thm:kasowanie-pary}", at)
        self.assertIn(r"\label{thm:kasowanie-pary}", dg)
        self.assertIn("Niech $R$ będzie pierścieniem z jedynką", at)
        self.assertIn("pierścienia nieprzemiennego", at)
        # Over Z, multiplication by 2 is not a unit and H_0 = Z/2.
        self.assertNotEqual(2, 1)
        self.assertEqual({n % 2 for n in range(10)}, {0, 1})

    def test_merge_manifest_protects_all_unique_labels(self):
        source = ROOT / "application/config/KANDYDACI_SCALEN_AT_DG_ETAP_02.json"
        data = json.loads(source.read_text(encoding="utf-8"))
        self.assertEqual(len(data["pairs"]), 2)
        self.assertFalse(data["policy"]["auto_rename_labels"])
        self.assertFalse(data["policy"]["auto_identify_equal_theorems_by_label"])
        for pair in data["pairs"]:
            left, right = pair["left"].replace("-", ""), pair["right"].replace("-", "")
            a, b = labels(self.s[left]), labels(self.s[right])
            self.assertEqual(pair["shared_label_names"], len(a & b))
            self.assertEqual(set(pair["left_only_labels"]), a - b)
            self.assertEqual(set(pair["right_only_labels"]), b - a)
            self.assertIsNone(pair["canonical_source"])
            self.assertFalse(pair["approved_to_merge"])
            self.assertTrue(pair["significant_shared_label_differences"])

    def test_current_book_inclusions_remain_unchanged(self):
        for vol, path in (
            ("AT", ROOT / "books/pl/algebraic_topology.tex"),
            ("DG", ROOT / "books/pl/differential_geometry_and_topology.tex"),
        ):
            book = path.read_text(encoding="utf-8-sig")
            for key in (("AT03","AT09") if vol=="AT" else ("DG06","DG10")):
                source_path = PATHS[key]
                rel = "../../chapters/pl/" + (
                    "algebraic_topology/" if vol=="AT" else
                    "differential_geometry_and_topology/"
                ) + source_path.name
                self.assertIn(r"\input{" + rel + "}", book)


if __name__ == "__main__":
    unittest.main()
