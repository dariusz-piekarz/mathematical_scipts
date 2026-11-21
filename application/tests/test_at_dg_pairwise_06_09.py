"""Mathematical and preservation regression: AT-06 versus DG-09.

Tests do not infer equality of theorems from matching historical labels.
"""
from __future__ import annotations

from collections import Counter
from math import gcd
from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters/pl/algebraic_topology"
DG = ROOT / "chapters/pl/differential_geometry_and_topology"
PATHS = {
    "AT06": next(AT.glob("06-*.tex")),
    "DG09": next(DG.glob("09-*.tex")),
}


def labels(source: str) -> set[str]:
    return set(re.findall(r"\\label\{([^}]+)\}", source))


def theorem_block(source: str, label: str) -> str:
    k = source.index(r"\label{" + label + "}")
    # All targeted statements have a proof immediately following.
    stop = source.index(r"\end{proof}", k)
    return source[k:stop]


class HurewiczComparisonAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = {
            key: path.read_text(encoding="utf-8-sig")
            for key, path in PATHS.items()
        }
        cls.manifest = json.loads(
            (ROOT / "application/config/KANDYDACI_SCALEN_AT_DG_ETAP_04.json")
            .read_text(encoding="utf-8")
        )

    def test_two_cell_attachment_homology_general_integer_coefficients(self):
        for a in range(-8, 9):
            for b in range(-8, 9):
                if a == b == 0:
                    continue
                d = gcd(abs(a), abs(b))
                u, v = b // d, -(a // d)
                self.assertEqual(a * u + b * v, 0)
                self.assertEqual(gcd(abs(u), abs(v)), 1)
                for x in range(-3, 4):
                    for y in range(-3, 4):
                        if a*x+b*y == 0:
                            # This is exactly rank-one kernel Z*(u,v).
                            if u:
                                self.assertEqual(y*u, x*v)
                                self.assertEqual(x % abs(u), 0)
                            else:
                                self.assertEqual(x, 0)
                                self.assertEqual(y % abs(v), 0)
                # gcd is the generator of the image.
                self.assertEqual(a % d, 0)
                self.assertEqual(b % d, 0)

    def test_attachment_examples_include_hurewicz_connectivity_warning(self):
        s = self.source["DG09"]
        for token in (
            r"\label{prz:dwiekrotne-dolaczenie-stopnie-dg09}",
            r"\pi_2(X_{4,6})\cong\Z/2\Z",
            r"X_{a,b}\simeq S^3",
            r"\gcd(|a|,|b|)",
            r"H_3(X_{a,b};\Z)",
            "2$-spójności",
        ):
            self.assertIn(token, s)
        # For (4, 6), the generator of H3 is (3,-2), while pi2=Z/2.
        self.assertEqual(4*3 + 6*(-2), 0)
        self.assertEqual(gcd(4, 6), 2)
        # For (2, 3), pi2=0 and H3=Z.
        self.assertEqual(gcd(2, 3), 1)

    def test_singular_triangle_gives_correct_hurewicz_h1_signs(self):
        s = theorem_block(self.source["AT06"], "thm:hurewicz-h1")
        self.assertIn("t_1/2+t_2", s)
        self.assertIn(r"\partial T_{\alpha,\beta}", s)
        self.assertIn(r"\beta-(\alpha*\beta)+\alpha", s)
        self.assertIn("naturalność", s)
        # Affine interpolation at the three vertices gives 0, 1/2, 1.
        vertices = ((1,0,0), (0,1,0), (0,0,1))
        self.assertEqual([v[1]/2+v[2] for v in vertices], [0, 0.5, 1])

    def test_relative_hurewicz_does_not_apply_five_lemma_to_pi2(self):
        s = theorem_block(self.source["AT06"], "thm:hurewicz-wzgledny")
        self.assertIn(r"\pi_1(X,x_0)=0", s)
        self.assertIn(r"\pi_2(Z,A)\cong", s)
        self.assertIn(r"\pi_2(X,A)\cong", s)
        self.assertIn(r"\operatorname{im}", s)
        self.assertIn("pi_2" if False else "stopniu $2$", s)
        self.assertIn("wyróżnioną", s)
        self.assertIn("grup", s)
        self.assertIn("lemat pięciu", s)

    def test_preserve_two_distinct_klein_and_syzygy_examples(self):
        at, dg = labels(self.source["AT06"]), labels(self.source["DG09"])
        for key in (
            "prz:pi1-klein-hurewicz",
            "prz:pi-2-3-komorki",
            "fig:pi-2-3-komorki",
        ):
            self.assertIn(key, at)
            self.assertNotIn(key, dg)
        self.assertIn("prz:dwiekrotne-dolaczenie-stopnie-dg09", dg)
        self.assertNotIn("prz:dwiekrotne-dolaczenie-stopnie-dg09", at)

    def test_exact_label_provenance_manifest(self):
        meta = self.manifest
        self.assertFalse(meta["approved_to_merge"])
        self.assertTrue(meta["policy"]["preserve_original_labels"])
        self.assertTrue(meta["policy"]["do_not_rename_source_labels"])
        pair = meta["pair"]
        a, b = labels(self.source["AT06"]), labels(self.source["DG09"])
        self.assertEqual(pair["shared_label_names"], len(a & b))
        self.assertEqual(set(pair["left_only_labels"]), a - b)
        self.assertEqual(set(pair["right_only_labels"]), b - a)
        self.assertTrue(pair["mathematical_findings"])

    def test_tex_environments_labels_and_no_unaudited_dependencies(self):
        for key, s in self.source.items():
            with self.subTest(chapter=key):
                ll = re.findall(r"\\label\{([^}]+)\}", s)
                self.assertEqual(len(ll), len(set(ll)))
                self.assertEqual(
                    Counter(re.findall(r"\\begin\{([^}]+)\}", s)),
                    Counter(re.findall(r"\\end\{([^}]+)\}", s)),
                )
                self.assertNotRegex(s.lower(), r"\bsekwencj\w*")
                self.assertNotRegex(s.lower(), r"\btensorowan\w*")

    def test_canonical_books_keep_both_unchanged_inputs(self):
        for key, path in PATHS.items():
            volume = "algebraic_topology" if key.startswith("AT") else (
                "differential_geometry_and_topology"
            )
            book = (ROOT / "books/pl" / (volume + ".tex")).read_text(encoding="utf8")
            self.assertIn(r"\input{../../chapters/pl/" + volume + "/" +
                          path.name + "}", book)


if __name__ == "__main__":
    unittest.main()
