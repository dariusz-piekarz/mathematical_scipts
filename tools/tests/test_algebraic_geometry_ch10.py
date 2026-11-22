"""ALG-10 regressions: algebraic cycles, topology, Lefschetz and Hodge.

Checks explicit formulas and TeX invariants. Does not prove external
Poincare duality, weak/hard Lefschetz or Chern-Gauss-Bonnet.
"""
import re
import unittest
from math import comb
from pathlib import Path

SOURCE = (Path(__file__).resolve().parents[2] / "chapters" / "pl"
          / "algebraic_geometry"
          / "10-geometria-algebraiczna-a-topologia-od-cykli-do-twierdzen-lefsc.tex")


class ALG10Regressions(unittest.TestCase):
    def test_degree_d_euler_and_canonical_square(self):
        known = {1: (3, 9), 2: (4, 8), 3: (9, 3),
                 4: (24, 0), 5: (55, 5)}
        for d in range(1, 121):
            euler = d*(d*d-4*d+6)
            ksq = d*(d-4)**2
            self.assertGreater(euler, 0)
            if d in known:
                self.assertEqual((euler, ksq), known[d])

    def test_surface_betti_numbers(self):
        for d in range(1, 121):
            b0, b1, b3, b4 = 1, 0, 0, 1
            b2 = d*(d*d-4*d+6)-2
            self.assertGreaterEqual(b2, 0)
            self.assertEqual(b0-b1+b2-b3+b4,
                             d*(d*d-4*d+6))

    def test_hodge_surface_numbers(self):
        for d in range(1, 121):
            pg = 0 if d <= 3 else comb(d-1, 3)
            b2 = d*(d*d-4*d+6)-2
            h11 = b2-2*pg
            self.assertGreaterEqual(h11, 1)
            self.assertEqual(2*pg+h11, b2)
            if d == 4:
                self.assertEqual((pg,b2,h11), (1,22,20))

    def test_noether_hypersurface_identity(self):
        for d in range(1, 121):
            pg = 0 if d<=3 else comb(d-1,3)
            self.assertEqual(
                12*(1+pg),
                d*(d-4)**2+d*(d*d-4*d+6))

    def test_blowup_euler_and_intersections(self):
        for n in range(0, 61):
            self.assertEqual((3+n)-3, n)
            self.assertEqual((9-n)+(3+n), 12)
            self.assertEqual((1+n)-1, n)

    def test_simple_node_has_two_branches(self):
        for p in (3,5,7,11,13):
            solutions = []
            for t in range(p):
                x=(t*t-1)%p
                y=(t*x)%p
                self.assertEqual((y*y-x*x*(x+1))%p,0)
                if x==0:
                    solutions.append(t)
            self.assertEqual(set(solutions),{1,p-1})

    def test_node_smoothing_annulus_discriminant(self):
        for eps2 in (4,9,16,25):
            for t in range(1,eps2//2):
                delta=eps2**2-4*t*t
                self.assertGreater(delta,0)
                self.assertGreater(eps2,2*t)

    def test_plane_curve_genus_and_euler(self):
        for d in range(1, 121):
            g=(d-1)*(d-2)//2
            self.assertEqual(2*g-2,d*(d-3))
            self.assertEqual(2-2*g, 2-d*(d-3)-2)

    def test_hodge_diamond_k3(self):
        self.assertEqual(1+20+1,22)
        self.assertEqual(2*1+20,22)
        self.assertEqual(1-0+1,2)

    def test_source_canonical_divisor_and_sheaf_types(self):
        s=SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"\omega_S\cong\mathcal O_S(d-4)",s)
        self.assertIn(r"p_g=h^0(S,\omega_S)",s)
        self.assertNotIn(r"$K_S\cong\mathcal O_S(d-4)$",s)
        self.assertNotIn(r"$K_S\simeq\mathcal O_S(d-4)$",s)

    def test_canonical_quantifiers(self):
        s=SOURCE.read_text(encoding="utf-8")
        block=s.split(r"\label{tw:ga10-surface-euler}",1)[1].split(
            r"\end{twierdzenie}",1)[0]
        self.assertIn("dowolnym dzielnikiem kanonicznym",block)
        noether=s.split("[Kontrola wzoru Noethera]",1)[1].split(
            r"\end{stwierdzenie}",1)[0]
        self.assertIn("dowolnego dzielnika kanonicznego",noether)

    def test_fundamental_class_requires_compactness(self):
        s=SOURCE.read_text(encoding="utf-8")
        note=s.split("[W przypadku osobliwym]",1)[1].split(
            r"\end{uwaga}",1)[0]
        self.assertIn("domkniętej pododmiany",note)
        self.assertIn("zwartej rozmaitości",note)

    def test_source_terminology(self):
        s=SOURCE.read_text(encoding="utf-8")
        self.assertIsNone(re.search(
            r"dywizor|chart|injektyw|tensorowanie|zwartościowan",
            s,re.IGNORECASE))
        self.assertIn("iniektywności",s)

    def test_unique_labels_and_proofs(self):
        s=SOURCE.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertGreaterEqual(len(labels),23)
        self.assertGreaterEqual(s.count(r"\begin{proof}"),8)

    def test_tikz_and_environment_balance(self):
        s=SOURCE.read_text(encoding="utf-8")
        self.assertEqual(s.count(r"\begin{tikzpicture}"),4)
        self.assertEqual(s.count(r"\end{tikzpicture}"),4)
        stack=[]
        for m in re.finditer(r"\\(begin|end)\{([a-zA-Z*]+)\}",s):
            if m[1]=="begin":
                stack.append(m[2])
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),m[2])
        self.assertFalse(stack)


if __name__=="__main__":
    unittest.main()
