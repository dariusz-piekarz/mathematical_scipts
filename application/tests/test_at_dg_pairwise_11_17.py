"""Mathematical regression checks for AT-11 / DG-17 duality and intersection audits."""
from __future__ import annotations

from collections import Counter
from itertools import permutations
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT_PATH = ROOT / "chapters/pl/algebraic_topology/11-przeciecia-dualnosc-i-klasy-charakterystyczne.tex"
DG_PATH = ROOT / "chapters/pl/differential_geometry_and_topology/17-przeciecia-dualnosc-i-klasy-charakterystyczne.tex"
MANIFEST = ROOT / "application/config/KANDYDACI_SCALEN_AT_DG_ETAP_05.json"


def labels(text: str) -> set[str]:
    return set(re.findall(r"\\label\s*\{([^}]+)\}", text))


def determinant(a):
    """Leibniz formula, exact integers; adequate for 2x2 and 4x4 examples."""
    n = len(a)
    total = 0
    for perm in permutations(range(n)):
        inv = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        product = 1
        for i, j in enumerate(perm):
            product *= a[i][j]
        total += (-1)**inv * product
    return total


class ATDG11_17Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.at = AT_PATH.read_text(encoding="utf8")
        cls.dg = DG_PATH.read_text(encoding="utf8")
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf8"))

    def test_graph_of_degree_d_has_even_self_intersection(self):
        # Q_{S2 x S2} is the hyperbolic intersection form.
        Q = ((0, 1), (1, 0))
        for d in range(-12, 13):
            v = (1, d)
            self.assertEqual(sum(v[i]*Q[i][j]*v[j] for i in range(2) for j in range(2)), 2*d)
        self.assertIn(r"\label{prz:samoprzeciecie-wykres-stopien-17}", self.dg)
        self.assertIn(r"I(\Gamma_f,\Gamma_f)", self.dg)
        self.assertIn(r"f^*(TS^2)", self.dg)

    def test_graph_normal_bundle_orientation_jacobian(self):
        # Graph tangent columns (I,Df), normal representative columns (0,I).
        for x, y, z, w in ((1, 2, 3, 4), (0, 0, 0, 0), (-3, 1, -5, 2)):
            mat = [[1,0,0,0], [0,1,0,0], [x,y,1,0], [z,w,0,1]]
            self.assertEqual(determinant(mat), 1)
        self.assertEqual(determinant([[-1,0],[0,-1]]), 1)
        self.assertEqual(determinant([[1,0],[0,1]]), 1)
        self.assertIn(r"\D_NX=-\id", self.dg)
        self.assertIn(r"\D_SX=\id", self.dg)

    def test_signed_intersection_pairings_and_parity(self):
        hyperbolic = ((0, 1), (1, 0))
        odd = ((1, 0), (0, -1))
        self.assertEqual(determinant(hyperbolic), -1)
        self.assertEqual(determinant(odd), -1)
        self.assertTrue(all((
            hyperbolic[0][0]*a*a + (hyperbolic[0][1]+hyperbolic[1][0])*a*b
            + hyperbolic[1][1]*b*b
        ) % 2 == 0 for a in range(-5, 6) for b in range(-5, 6)))
        self.assertEqual(odd[0][0], 1)
        self.assertIn(r"\label{prz:formy-przeciecia-cp2-s2}", self.at)
        self.assertIn(r"\det Q=\pm1", self.at)

    def test_alternating_unimodular_matrices_even_rank(self):
        # Any skew-symmetric matrix in odd rank has zero determinant.
        for a, b, c in ((0, 0, 0), (1, 2, 3), (-5, 7, -9)):
            Q = ((0, a, b), (-a, 0, c), (-b, -c, 0))
            self.assertEqual(determinant(Q), 0)
        self.assertEqual(determinant([[0, 1], [-1, 0]]), 1)
        self.assertIn(r"$Q^{\mathsf T}=-Q$", self.at)
        self.assertIn(r"\det Q=\pm1", self.at)

    def test_mod2_odd_cup_square_need_not_vanish(self):
        # H*(RP2;F2)=F2[x]/(x^3), x in degree 1 and x^2 != 0.
        square = [0, 0, 1]
        self.assertEqual(square[2], 1)
        self.assertIn(r"$x^2\ne0$", self.at)
        self.assertIn(r"\label{prop:kubek-graded-16}", self.at)

    def test_chain_contraction_sign_proof_is_explicit(self):
        for term in (
            r"K(a\otimes b)=h(a)\otimes b",
            r"\partial K+K\partial",
            r"(\id-P)\otimes\id+P\otimes(\id-P)",
            r"H(\sigma)=Kz",
        ):
            self.assertIn(term, self.at)
        self.assertEqual(self.at.count(r"H(\sigma)=Kz"), 1)

    def test_projective_bundle_skeleton_proof_has_all_hypotheses(self):
        for term in (
            r"\Phi^q_{B,A}",
            r"H^{q-d}(\R P^{r-1};\mathbb F_2)",
            r"\Phi^q_{M^{(d)},M^{(d-1)}}",
            "lemat o pięciu",
        ):
            self.assertIn(term, self.at)
        self.assertIn(r"\label{thm:wi-klasy-16}", self.dg)

    def test_historical_unique_content_and_labels_preserved(self):
        manifest = self.manifest
        la, ld = labels(self.at), labels(self.dg)
        # Stage V is a historical provenance snapshot. Subsequent verified
        # audits may ADD labels to DG-17 (or AT-11), but must not silently
        # remove labels that were historically unique or common.
        historic_common = set(manifest["historical_common_labels"])
        self.assertEqual(len(historic_common), manifest["common_label_names"])
        self.assertTrue(historic_common.issubset(la & ld))
        self.assertTrue(set(manifest["at_only_labels"]).issubset(la-ld))
        self.assertTrue(set(manifest["dg_only_labels"]).issubset(ld-la))
        self.assertEqual(manifest["common_label_names"], 42)
        self.assertFalse(manifest["policy"]["automatic_merge"])
        self.assertFalse(manifest["policy"]["merge_approved"])
        for key in (
            "thm:pl-v4", "thm:alexander-v4",
            "prz:formy-przeciecia-cp2-s2",
            "fig:formy-przeciecia-parzystosc",
        ):
            self.assertIn(key, la)
        for key in (
            "prz:pd-rp2-21", "prz:sw-sfera-stabilna-21",
            "prz:samoprzeciecie-wykres-stopien-17",
        ):
            self.assertIn(key, ld)

    def test_no_duplicates_unbalanced_environments_or_unwanted_terms(self):
        for source in (self.at, self.dg):
            found = re.findall(r"\\label\s*\{([^}]+)\}", source)
            self.assertEqual(len(found), len(set(found)))
            self.assertEqual(
                Counter(re.findall(r"\\begin\{([^}]+)\}", source)),
                Counter(re.findall(r"\\end\{([^}]+)\}", source)),
            )
            self.assertNotRegex(source.lower(), r"\bkochain\w*")
            self.assertNotRegex(source.lower(), r"\btensorowan\w*")
            self.assertNotRegex(source.lower(), r"\bsekwencj\w*")

    def test_canonical_books_keep_the_sources(self):
        for name, file_path, section in (
            ("AT", AT_PATH, "algebraic_topology"),
            ("DG", DG_PATH, "differential_geometry_and_topology"),
        ):
            source = (ROOT / "books/pl" / (section + ".tex")).read_text(encoding="utf8")
            self.assertIn(
                r"\input{../../chapters/pl/" + section + "/" + file_path.name + "}",
                source, name,
            )


if __name__ == "__main__":
    unittest.main()
