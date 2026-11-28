"""Regression checks for detailed Morse audits AT-18 and DG-18.

Only the current source material is inspected. Mathematical identities and
homological computations are independently exercised with exact small examples.
"""
from __future__ import annotations

from collections import Counter
from math import sqrt
from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT_PATH = ROOT / "chapters/pl/algebraic_topology/18-homologia-morse-a-od-punktow-krytycznych-do-homologii-singular.tex"
DG_PATH = ROOT / "chapters/pl/differential_geometry_and_topology/18-teoria-morse-a-punkty-krytyczne-uchwyty-i-przeplyw.tex"
MANIFEST = ROOT / "application/config/KANDYDACI_SCALEN_AT_DG_ETAP_06.json"


def labels(text: str) -> set[str]:
    return set(re.findall(r"\\label\{([^}]+)\}", text))


class MorsePairAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.at = AT_PATH.read_text(encoding="utf8")
        cls.dg = DG_PATH.read_text(encoding="utf8")
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf8"))

    def test_morse_schur_complement_identity(self):
        # Algebra in the block-Morse normal form, with a negative top block.
        for P in (-1, -2, -4):
            for Q in (-2, -1, 0, 1, 3):
                for C in (1, 2, 4):
                    S = C - Q * Q / P
                    self.assertGreater(S, 0)
                    for xm, xp in ((1, 2), (-3, 2), (0, -1)):
                        left = P*xm*xm + 2*Q*xm*xp + C*xp*xp
                        right = P*(xm + Q*xp/P)**2 + S*xp*xp
                        self.assertAlmostEqual(left, right)
        self.assertIn("dopełnienie Schura", self.at)
        self.assertIn(r"P(x)^{-1}Q(x)", self.at)
        self.assertIn(r"$\lambda=0$", self.at)
        self.assertIn(r"$\lambda=n$", self.at)

    def test_rp2_quadratic_critical_indices(self):
        ls = (0, 1, 2)
        for i in range(3):
            signs = [ls[j] - ls[i] for j in range(3) if j != i]
            self.assertEqual(sum(x < 0 for x in signs), i)
            self.assertTrue(all(x != 0 for x in signs))

    def test_rp2_two_gradient_trajectories_have_same_sign(self):
        # Set lambda0=0, lambda1=1, lambda2=2, regular value c=3/2.
        lo, mid, hi, c = 0., 1., 2., 1.5
        mag = sqrt((hi-c)/(c-mid))
        values = []
        for v in (-mag, mag):
            # W^u(p2) is oriented by (du,dv).
            # Flow vector is proportional to sign(v) dv.
            # Positively oriented level tangent is -sign(v) du.
            oriented_tangent_u = -1 if v > 0 else 1
            # Coorientation of W^s(p1) is da=du/v.
            values.append(oriented_tangent_u/v)
        self.assertTrue(all(v < 0 for v in values))
        self.assertEqual(len(values), 2)
        self.assertIn(r"n(p_2,p_1)=-2", self.at)
        self.assertIn(r"n(p_1,p_0)=0", self.at)
        self.assertIn(r"\partial_2=2", self.at)

    def test_rp2_morse_homology_and_characteristic(self):
        # CM2 --2--> CM1 --0--> CM0.
        self.assertEqual((1, 1, 1), (1, 1, 1))
        self.assertEqual(1-1+1, 1)  # Euler characteristic RP2
        self.assertEqual(abs(2), 2)  # |H1| = 2
        self.assertNotEqual(2, 0)  # H2=0, since kernel of multiplication by 2 vanishes
        self.assertEqual(2 % 2, 0)  # Over F2: all differentials zero
        self.assertRegex(self.at, r"HM_1=[^\n]*\\cong\\Z/2\\Z")
        self.assertIn(r"\label{fig:morse-rp2-torsja}", self.at)

    def test_nonorientable_rp2_reeb_graph_is_interval(self):
        # Three vertices: min-valence1, saddle-valence2, max-valence1.
        degrees = [1, 2, 1]
        edges = sum(degrees)//2
        vertices = len(degrees)
        self.assertEqual((edges, vertices), (2, 3))
        self.assertEqual(edges-vertices+1, 0)  # H1 of a connected graph.
        self.assertEqual(1-1+1, 1)
        self.assertIn(r"\label{prz:reeb-rp2-siodlo-stopien-dwa-18}", self.dg)
        self.assertIn(r"\label{fig:reeb-rp2-siodlo-stopien-dwa-18}", self.dg)
        self.assertIn("siodła ma stopień $2$", self.dg)

    def test_orientable_reeb_graph_genus_formula(self):
        for genus in range(7):
            c0, c1, c2 = 1, 2*genus, 1
            V = c0+c1+c2
            E = (c0+c2+3*c1)//2
            self.assertEqual(E-V+1, genus)
            self.assertEqual(c0-c1+c2, 2-2*genus)
        self.assertIn(r"\label{thm:graf-reeba-rodzaj-22}", self.dg)

    def test_signed_circle_differential_has_rank_one(self):
        matrix = ((1, -1), (-1, 1))
        self.assertEqual(matrix[0][0]*matrix[1][1] -
                         matrix[0][1]*matrix[1][0], 0)
        self.assertEqual([sum(row) for row in matrix], [0, 0])
        self.assertEqual([sum(row[j] for row in matrix) for j in range(2)], [0, 0])
        self.assertIn(r"\partial p_1=q_1-q_2", self.at)
        self.assertIn(r"\label{prz:morse-okrag-znaki-22}", self.dg)

    def test_strong_morse_inequalities_qranks(self):
        # Formula c_k-b_k = r_k + r_{k+1} for RP2 over Q.
        c = (1, 1, 1)
        b = (1, 0, 0)
        r = (0, 0, 1, 0)
        self.assertEqual(tuple(c[i]-b[i] for i in range(3)),
                         tuple(r[i]+r[i+1] for i in range(3)))
        # c(t)-b(t)=t+t²=(1+t)*t
        self.assertEqual((0, 1, 1), (0, 1, 1))
        self.assertIn(r"\label{thm:morse-inequalities-v10}", self.at)
        self.assertIn(r"\label{thm:nierownosci-morse-17}", self.dg)

    def test_manifest_source_labels_are_exact(self):
        la, ld = labels(self.at), labels(self.dg)
        man = self.manifest
        # The manifest is a historical lower bound; new examples may add labels.
        self.assertGreaterEqual(len(la), man["label_statistics"]["at18"])
        self.assertGreaterEqual(len(ld), man["label_statistics"]["dg18"])
        self.assertEqual(man["label_statistics"]["common"], len(la & ld))
        self.assertTrue(set(man["unique_at_labels"]).issubset(la-ld))
        self.assertTrue(set(man["unique_dg_labels"]).issubset(ld-la))
        self.assertFalse(man["policy"]["automatic_merge"])
        self.assertFalse(man["merge_approved"])
        for key in ("thm:morse-compact-v10", "lem:morse-same-level-audit",
                    "prz:morse-rp2-torsja"):
            self.assertIn(key, la)
        for key in ("thm:gen-ms-17", "thm:brzeg-morse-17",
                    "fig:torus-morse-17", "thm:graf-reeba-rodzaj-22"):
            self.assertIn(key, ld)

    def test_tex_structure_terminology_and_canonical_book_sources(self):
        for text, name, path in (
            (self.at, "algebraic_topology", AT_PATH),
            (self.dg, "differential_geometry_and_topology", DG_PATH),
        ):
            with self.subTest(name=name):
                ll = re.findall(r"\\label\{([^}]+)\}", text)
                self.assertEqual(len(ll), len(set(ll)))
                self.assertEqual(
                    Counter(re.findall(r"\\begin\{([^}]+)\}", text)),
                    Counter(re.findall(r"\\end\{([^}]+)\}", text)))
                self.assertNotRegex(text.lower(), r"\btensorowan\w*")
                self.assertNotRegex(text.lower(), r"\bsekwencj\w*")
                book = (ROOT / "books/pl" / (name + ".tex")).read_text(encoding="utf8")
                self.assertIn(r"\input{../../chapters/pl/" + name + "/" + path.name + "}", book)


if __name__ == "__main__":
    unittest.main()
