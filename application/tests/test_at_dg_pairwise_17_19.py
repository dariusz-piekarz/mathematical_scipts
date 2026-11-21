"""Mathematical regressions: Pontriagin–Thom, bordism and DG handle calculus."""
from __future__ import annotations
from collections import Counter
from pathlib import Path
from itertools import product
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters/pl/algebraic_topology/17-konstrukcja-pontriagina-thoma-i-podstawy-teorii-kobordyzmow.tex"
DG = ROOT / "chapters/pl/differential_geometry_and_topology/19-kobordyzmy-i-rachunek-uchwytow.tex"
MANIFEST = ROOT / "application/config/KANDYDACI_SCALEN_AT_DG_ETAP_07.json"


def labels(s):
    return set(re.findall(r"\\label\{([^}]+)\}", s))


def mod2_poly_product(a, b, top=4):
    """Multiply multivariate polynomials in F_2[a,b]/(a^3,b^3)."""
    result = set()
    for (i, j), (k, h) in product(a, b):
        t = (i+k, j+h)
        if t[0] < 3 and t[1] < 3 and t[0] + t[1] <= top:
            if t in result:
                result.remove(t)
            else:
                result.add(t)
    return result


class BordismHandlesAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.at = AT.read_text(encoding="utf-8")
        cls.dg = DG.read_text(encoding="utf-8")
        cls.man = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_twisted_disc_bundle_boundary(self):
        # Fibre D2 has boundary S1. Monodromy z -> zbar restricts
        # to a reflection of S1 of degree -1, not +1.
        reflected_angles = [(-t) % 360 for t in range(0, 360, 30)]
        self.assertEqual(reflected_angles[:4], [0, 330, 300, 270])
        self.assertIn(r"r(z)=\overline z", self.at)
        self.assertIn(r"\partial V_-=(S^1\times[0,1])", self.at)
        self.assertIn(r"\deg h=-1", self.dg)
        self.assertIn(r"\label{fig:skrecony-uchwyt-klein-24}", self.dg)

    def test_klein_bottle_H1_has_order_two_torsion(self):
        # Abelianization of <a,b|bab^-1=a^-1> adds 2[a]=0.
        # Every class has unique normal form (a mod 2, b int).
        for a in range(-5, 6):
            for b in range(-5, 6):
                self.assertEqual(((a + 2) % 2, b), (a % 2, b))
        self.assertNotEqual((1 % 2, 0), (0, 0))
        self.assertIn(r"H_1(K;\Z)\cong\Z\oplus\Z/2\Z", self.at)
        self.assertIn(r"H_1(K;\Z)=\Z\oplus\Z/2\Z", self.dg)
        self.assertIn(r"bab^{-1}=a^{-1}", self.at)

    def test_torus_vs_klein_have_equal_euler_characteristic(self):
        # Mapping tori of circle homeomorphisms have chi = 0;
        # torus: one 0-cell, two 1-cells, one 2-cell.
        self.assertEqual(1 - 2 + 1, 0)
        self.assertIn(r"\chi(T^2)=\chi(K)=0", self.at)
        self.assertIn(r"[T^2]=[K]=0", self.at)

    def test_handle_chirurgy_boundary_dimensions(self):
        for m in range(2, 10):
            for k in range(1, m):
                attaching_sphere = k-1
                attaching_normal_disc = m-k
                belt_sphere = m-k-1
                new_belt_disc = k
                self.assertEqual(attaching_sphere+attaching_normal_disc, m-1)
                self.assertEqual(new_belt_disc+belt_sphere, m-1)
                self.assertEqual((k-1)+belt_sphere, m-2)
        self.assertIn(r"\label{thm:slad-chirurgii-18}", self.dg)
        self.assertIn(r"\label{thm:dualny-uchwyt-18}", self.dg)

    def test_relative_euler_characteristic_one_handle(self):
        # 3D cobordism from S2 to T2 or Klein, with one 1-handle:
        m, c0, c1 = 3, 0, 1
        relative_euler = c0-c1
        self.assertEqual(relative_euler, -1)
        self.assertEqual((1-(-1)**m)*relative_euler, -2)
        self.assertEqual((2-2), 0)  # Torus/Klein chi=0
        self.assertIn(r"\label{prop:euler-uchwyty-23}", self.dg)

    def test_handle_slide_is_invertible_chain_basis_change(self):
        # Slide basis e_p' = e_p + sigma e_q; D'_k = D_k T.
        for sigma in (-1, 1):
            T = ((1, 0), (sigma, 1))
            U = ((1, 0), (-sigma, 1))
            matrix = [[sum(T[i][l]*U[l][j] for l in range(2))
                       for j in range(2)] for i in range(2)]
            self.assertEqual(matrix, [[1, 0], [0, 1]])
        self.assertIn(r"D'_k=D_kT", self.dg)
        self.assertIn(r"D'_{k+1}=T^{-1}D_{k+1}", self.dg)
        self.assertIn(r"\label{prop:slide-18}", self.dg)

    def test_rp2_square_characteristic_numbers(self):
        # H*(RP2 x RP2; F2)=F2[a,b]/(a^3,b^3).
        w2 = {(2, 0), (1, 1), (0, 2)}
        w2_squared = mod2_poly_product(w2, w2)
        self.assertEqual(w2_squared, {(2, 2)})
        self.assertIn(r"\label{prz:bordism-rp2-product}", self.at)
        self.assertIn(r"\langle w_2(TX)^2,[X]_2\rangle=1", self.at)

    def test_rp4_different_bordism_characteristic(self):
        # (1+t)^5 modulo two = 1+t+t^4 mod t^5.
        coeff = [1, 5, 10, 10, 5]
        self.assertEqual([c % 2 for c in coeff], [1, 1, 0, 0, 1])
        self.assertIn(r"$w_2(TY)=0$", self.at)
        self.assertIn(r"\label{prz:bordism-rp4-versus-rp2-square}", self.at)

    def test_pt_normal_framing_and_whitney_condition_preserved(self):
        for token in (r"\label{thm:pt-framed-v9}", r"\label{thm:pt-MO-v9}",
                      r"\label{thm:sw-bdy-v9}", r"\label{lem:thom-transversal-v9-audyt}"):
            self.assertIn(token, self.at)
        for token in (r"\label{thm:zniesienie-18}",
                      r"\label{prop:whitney-do-zniesienia-18}",
                      r"\label{thm:kompleks-uchwytow-18}"):
            self.assertIn(token, self.dg)

    def test_labels_environments_provenance_and_canonical_inputs(self):
        left, right = labels(self.at), labels(self.dg)
        self.assertEqual(self.man["label_counts"]["AT17"], len(left))
        self.assertEqual(self.man["label_counts"]["DG19"], len(right))
        self.assertEqual(self.man["label_counts"]["shared"], len(left & right))
        self.assertEqual(left - right, set(self.man["labels_only_AT"]))
        self.assertEqual(right - left, set(self.man["labels_only_DG"]))
        self.assertFalse(self.man["policy"]["automatic_merge"])
        self.assertFalse(self.man["policy"]["approved_to_merge"])
        for txt, section, path in (
            (self.at, "algebraic_topology", AT),
            (self.dg, "differential_geometry_and_topology", DG),
        ):
            labels_all = re.findall(r"\\label\{([^}]+)\}", txt)
            self.assertEqual(len(labels_all), len(set(labels_all)))
            self.assertEqual(Counter(re.findall(r"\\begin\{([^}]+)\}", txt)),
                             Counter(re.findall(r"\\end\{([^}]+)\}", txt)))
            self.assertNotRegex(txt.lower(), r"\btensorowan\w*")
            self.assertNotRegex(txt.lower(), r"\bsekwencj\w*")
            book = (ROOT / "books/pl" / (section+".tex")).read_text(encoding="utf8")
            self.assertIn(r"\input{../../chapters/pl/" + section + "/" + path.name + "}", book)


if __name__ == "__main__":
    unittest.main()
