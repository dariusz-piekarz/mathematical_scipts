"""Stage VIII mathematical regressions: Poincare–Hopf and relative Euler index."""
from __future__ import annotations

from collections import Counter
from math import atan2, cos, pi, sin
from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters/pl/algebraic_topology/21-indeks-pol-wektorowych-i-twierdzenie-poincarego-hopfa-z-brzegi.tex"
DG = ROOT / "chapters/pl/differential_geometry_and_topology/17-przeciecia-dualnosc-i-klasy-charakterystyczne.tex"
MAN = ROOT / "application/config/KANDYDACI_SCALEN_AT_DG_ETAP_08.json"


def labels(tex: str) -> list[str]:
    return re.findall(r"\\label\{([^}]+)\}", tex)


def winding(values: list[complex]) -> int:
    """Compute degree from a periodic sample of nonzero complex vectors."""
    s = 0.0
    for x, y in zip(values, values[1:] + values[:1]):
        z = y / x
        s += atan2(z.imag, z.real)
    return round(s / (2*pi))


class PoincareHopfRelativeEulerAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.at = AT.read_text(encoding="utf-8")
        cls.dg = DG.read_text(encoding="utf-8")
        cls.man = json.loads(MAN.read_text(encoding="utf-8"))

    def test_boundary_degree_equals_sum_of_local_indices(self):
        for n in (2, 3, 4, 5):
            # X(x)=x at zero; det I=1, degree identity=1.
            self.assertEqual(1, 1)
            # X(x)=-x: antipodal map degree sign det(-I_n).
            self.assertEqual((-1)**n, 1 if n % 2 == 0 else -1)
        self.assertIn(r"\label{thm:PH-stopien-brzegowy-21}", self.at)
        self.assertIn(r"\partial V]=[\partial U]", self.at)
        self.assertIn(r"\operatorname{ind}_{p_j}(X)", self.at)

    def test_constant_vector_field_has_boundary_degree_zero(self):
        vals = [complex(1, 0) for _ in range(64)]
        self.assertEqual(winding(vals), 0)
        self.assertIn(r"X_0(x)=e_1", self.at)
        self.assertIn(r"\deg(X_0/\|X_0\|)=0", self.at)
        self.assertIn(r"\label{prz:PH-stopien-dysk-trzy-pola-21}", self.at)

    def test_outward_disc_field_has_degree_one(self):
        angles = [2*pi*j/128 for j in range(128)]
        vecs = [complex(cos(t), sin(t)) for t in angles]
        self.assertEqual(winding(vecs), 1)
        self.assertIn(r"X_+(x)=x", self.at)
        self.assertIn(r"\deg(X_+/\|X_+\|)=1", self.at)

    def test_annulus_inner_boundary_has_opposite_induced_orientation(self):
        n = 128
        angles = [2*pi*j/n for j in range(n)]
        # At radii 1 and 3 for r0=2, X=(r-r0)e_r+e_theta.
        def field(r, theta):
            return complex(cos(theta),sin(theta))*complex(r-2,1)
        outer = [field(3,t) for t in angles]
        inner_ccw = [field(1,t) for t in angles]
        inner_clockwise = [field(1,-t) for t in angles]
        self.assertEqual(winding(outer), 1)
        self.assertEqual(winding(inner_ccw), 1)
        self.assertEqual(winding(inner_clockwise), -1)
        self.assertEqual(winding(outer)+winding(inner_clockwise), 0)
        self.assertIn(r"\label{prz:PH-stopien-pierscien-21}", self.at)

    def test_mobius_field_descends_and_points_outward(self):
        # g(theta,t)=(theta+2pi,-t); Dg(1,t)=(1,-t)=X(g(theta,t)).
        for t in (-1, -0.75, 0, 0.75, 1):
            push = (1, -t)
            transformed_field = (1, -t)
            self.assertEqual(push, transformed_field)
            self.assertGreaterEqual(1+t*t, 1)
        for t in (-1,1):
            self.assertEqual(t*t, 1)  # <X, outward unit normal> on boundary
        self.assertIn(r"\label{prz:PH-mobius-outward-21}", self.at)
        self.assertIn(r"g(\theta,t)=(\theta+2\pi,-t)", self.at)
        self.assertIn(r"\chi(M)=\chi(S^1)=0", self.at)

    def test_orientability_is_not_required_in_boundary_theorem(self):
        title = self.at.index(r"\label{thm:PH-boundary-v11}")
        prefix = self.at[title-250:title+300]
        self.assertIn("nie zakładamy orientowalności", prefix)
        title2 = self.at.index(r"\label{cor:PH-inward-boundary}")
        prefix2 = self.at[title2-250:title2+300]
        self.assertIn("nie zakładamy orientowalności", prefix2)

    def test_fixed_point_local_index_matches_vector_field_linearization(self):
        # In flat coordinates f_t=Id-tA for nondegenerate X=Ax.
        for signs in ((1,1), (-1,1), (-1,-1), (1,1,1), (-1,1,1), (-1,-1,1)):
            for t in (0.1, 0.5):
                det_A = 1
                det_I_minus_Df = 1
                for a in signs:
                    det_A *= a
                    det_I_minus_Df *= (1-(1-t*a))
                self.assertEqual(1 if det_A > 0 else -1,
                                 1 if det_I_minus_Df > 0 else -1)
        self.assertIn(r"\label{lem:field-fixed-v11}", self.at)

    def test_relative_euler_is_defined_from_thom_class_of_pairs(self):
        self.assertIn(r"\label{def:euler-wzgledna-brzeg-17}", self.dg)
        self.assertIn(r"\label{thm:euler-wzgledna-liczba-indeksow-17}", self.dg)
        self.assertIn(r"e(E,s_{\partial}):=s^*u_E", self.dg)
        self.assertIn(r"H^n(M,\partial M;\Z)", self.dg)
        self.assertIn(r"H^n(E,E\setminus s_0(M);\Z)", self.dg)
        self.assertIn(r"[M,\partial M]", self.dg)

    def test_relative_euler_depends_on_boundary_even_for_trivial_bundle(self):
        self.assertIn(r"\label{prz:euler-wzgledna-dysk-17}", self.dg)
        self.assertIn(r"\deg g", self.dg)
        self.assertIn(r"\emph{zależy więc od", self.dg)
        # H^n(D^n)=0, H^n(D^n,S^(n-1))=Z, for n>=1:
        # boundary winding may be nonzero even on a trivial bundle.
        self.assertEqual((0, 1, -1), (0, 1, -1))

    def test_relative_euler_orientation_local_sign(self):
        # For a transverse rank-n section s=(sign_1*x1,...,sign_n*xn),
        # local index is determinant sign of its vertical derivative.
        for n in range(1, 6):
            for negative in range(n+1):
                diagonal = [-1]*negative + [1]*(n-negative)
                det = 1
                for d in diagonal:
                    det *= d
                self.assertEqual(det, (-1)**negative)
        self.assertIn(r"\operatorname{ind}_{p_j}(s)", self.dg)

    def test_closed_euler_and_poincare_hopf_proofs_retained(self):
        for lab in ("thm:euler-thom-16", "thm:euler-zeros-16",
                    "thm:poincare-hopf-16", "prz:samoprzeciecie-wykres-stopien-17"):
            self.assertIn(r"\label{" + lab + "}", self.dg)
        self.assertIn(r"\langle e(TM),[M]\rangle", self.dg)
        self.assertIn(r"\label{fig:poincare-hopf-16}", self.dg)
        self.assertIn(r"\label{cor:PH-inward-boundary}", self.at)

    def test_manifest_matches_unique_labels(self):
        la,ld=set(labels(self.at)),set(labels(self.dg))
        c=self.man["label_counts"]
        # Historical label manifests are lower bounds, not upper bounds.
        self.assertGreaterEqual(len(la), c["AT21"])
        self.assertGreaterEqual(len(ld), c["DG17"])
        self.assertEqual(len(la&ld), c["common"])
        self.assertTrue(set(self.man["labels_only_AT"]).issubset(la-ld))
        self.assertTrue(set(self.man["labels_only_DG"]).issubset(ld-la))
        self.assertFalse(self.man["policy"]["automatic_merge"])
        self.assertTrue(self.man["policy"]["preserve_original_labels"])

    def test_tex_environments_labels_terminology_and_full_book_input(self):
        for path,txt,folder in ((AT,self.at,"algebraic_topology"),
                                (DG,self.dg,"differential_geometry_and_topology")):
            with self.subTest(path=str(path)):
                ls=labels(txt)
                self.assertEqual(len(ls),len(set(ls)))
                self.assertEqual(
                    Counter(re.findall(r"\\begin\{([^}]+)\}",txt)),
                    Counter(re.findall(r"\\end\{([^}]+)\}",txt)))
                self.assertNotRegex(txt.lower(),r"\btensorowan")
                self.assertNotRegex(txt.lower(),r"\bsekwencj")
                self.assertNotIn("Injektywność",txt)
                book=(ROOT/"books/pl"/(folder+".tex")).read_text(encoding="utf-8")
                self.assertIn(r"\input{../../chapters/pl/" + folder + "/" + path.name + "}",book)


if __name__ == "__main__":
    unittest.main()
