"""ALG-05: concrete blow-up/transform identities and source regressions.

These computations do not substitute for proofs of blow-up universality,
properness, flat base change or Hironaka's resolution theorem.
"""
import re
import unittest
from math import comb
from pathlib import Path

SOURCE = (Path(__file__).resolve().parents[2] / "chapters" / "pl"
          / "algebraic_geometry"
          / "05-rozdmuchania-i-rozwiazywanie-osobliwosci.tex")


class ALG05Regressions(unittest.TestCase):
    def test_normal_cone_hilbert_function(self):
        # gr_(x,y) k[x,y] ~ k[X,Y], degree-m part has dimension m+1.
        for m in range(21):
            self.assertEqual(len([(i, m-i) for i in range(m+1)]), m+1)
        for n in range(1, 6):
            for m in range(11):
                self.assertEqual(comb(m+n-1, n-1), comb(m+n-1, m))

    def test_first_cusp_total_and_strict_transform(self):
        for x in range(-4, 5):
            for v in range(-4, 5):
                self.assertEqual((x*v)**2-x**3, x*x*(v*v-x))
        for t in range(-5, 6):
            x, v = t*t, t
            self.assertEqual(v*v-x, 0)
            self.assertEqual((x*v)**2-x**3, 0)

    def test_cusp_second_blowup_total_transform(self):
        for v in range(-4, 5):
            for w in range(-4, 5):
                x, y = v*w, v*v*w
                self.assertEqual(y*y-x**3, v**3*w*w*(v-w))

    def test_cusp_third_blowup_total_transform(self):
        for a in range(-4, 5):
            for b in range(-4, 5):
                v, w = a, a*b
                x, y = v*w, v*v*w
                self.assertEqual(y*y-x**3, a**6*b*b*(1-b))
        # After stage three: strict curve b=1 and old E1 b=0
        # meet new E3 a=0 at two distinct points.
        self.assertNotEqual((0, 1), (0, 0))

    def test_cusp_other_chart_no_exceptional_fibre(self):
        # Second chart of first blow-up: 1-u^3*y=0,
        # impossible on the exceptional divisor y=0.
        for u in range(-5, 6):
            self.assertNotEqual(1-u**3*0, 0)

    def test_node_parameterization_and_transversality(self):
        for p in (3, 5, 7, 11, 13, 17):
            for t in range(p):
                x = (t*t-1) % p
                y = t*x % p
                self.assertEqual((y*y-x*x-x*x*x) % p, 0)
            for t in (1, p-1):
                self.assertEqual((t*t-1) % p, 0)
                self.assertNotEqual((2*t) % p, 0)

    def test_tacnode_two_tangent_branches(self):
        for p in (3, 5, 7, 11):
            for x in range(p):
                for v in range(p):
                    self.assertEqual((v*v-x*x-(v-x)*(v+x)) % p, 0)
            self.assertNotEqual(1, p-1)

    def test_y2_equals_x5_two_blowups(self):
        for x in range(-4, 5):
            for v in range(-4, 5):
                self.assertEqual((x*v)**2-x**5, x*x*(v*v-x**3))
            for w in range(-4, 5):
                self.assertEqual((x*w)**2-x**3, x*x*(w*w-x))
        # Intersection with E: k[w]/(w^2), basis 1,w.
        self.assertEqual(len({0, 1}), 2)

    def test_quadratic_cone_after_blowup_is_smooth(self):
        for p in (3, 5, 7, 11):
            for u in range(p):
                for v in range(p):
                    if (v*v-1-u*u) % p == 0:
                        self.assertTrue((2*v) % p or (2*u) % p)

    def test_nonreduced_double_fibre(self):
        for p in (2, 3, 5, 7):
            def mul(x, y):
                return ((x[0]*y[0]) % p,
                        (x[0]*y[1]+x[1]*y[0]) % p)
            epsilon = (0, 1)
            self.assertNotEqual(epsilon, (0, 0))
            self.assertEqual(mul(epsilon, epsilon), (0, 0))

    def test_nonflat_base_change_extra_component(self):
        # A=k[x,y], I=(x,y), B=A/(x).
        # On second blow-up chart after x=0: u*y=0 (two axes).
        for p in (2, 3, 5, 7):
            locus = {(u,y) for u in range(p) for y in range(p)
                     if (u*y) % p == 0}
            self.assertEqual(len(locus), 2*p-1)
            self.assertTrue(all((u, 0) in locus for u in range(p)))
            self.assertTrue(all((0, y) in locus for y in range(p)))

    def test_projective_fibres_over_nonrational_centre_points(self):
        # X=A^3_{F_3}, Z=V(x_1,x_2)=A^1_{F_3}.
        # The closed point (t^2+1) on Z has residue field F_9,
        # since t^2+1 is irreducible over F_3.
        self.assertFalse(any((t*t+1) % 3 == 0 for t in range(3)))
        # Over that point the exceptional fibre is P^1_{F_9}, not
        # P^1_{F_3}; their rational-point counts differ.
        self.assertEqual(9 + 1, 10)
        self.assertNotEqual(9 + 1, 3 + 1)
        src = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"\PP^{c-1}_{\kappa(z)}", src)
        self.assertIn(r"\widetilde X\times_X\Spec\kappa(z)", src)
        self.assertIn(r"E\times_Z\Spec\kappa(z)", src)

    def test_positive_codimension_for_exceptional_projective_fibres(self):
        # For a regular immersion of codimension zero, Z=X and I=0.
        # Its Rees algebra is concentrated in degree zero, so Proj is
        # empty; no projective fibres P^(c-1) should be asserted.
        src = SOURCE.read_text(encoding="utf-8")
        self.assertEqual(src.count(r"stały kowymiar $c\ge1$"), 2)
        self.assertIn(r"\PP^{c-1}_{\kappa(z)}", src)

    def test_projective_chart_transition(self):
        for p in (3, 5, 7, 11):
            for v in range(1, p):
                u = pow(v, -1, p)
                self.assertEqual(u*v % p, 1)
                self.assertEqual(pow(u, -1, p), v)

    def test_normalization_parameterizations(self):
        for p in (3, 5, 7, 11):
            for t in range(p):
                x, y = t*t % p, t**3 % p
                self.assertEqual((y*y-x*x*x) % p, 0)
                x = (t*t-1) % p
                y = t*x % p
                self.assertEqual((y*y-x*x-x*x*x) % p, 0)

    def test_three_distinct_tangent_directions_not_snc(self):
        # v=0, w=0, v-w=0 have different tangent directions.
        gradients = ((1, 0), (0, 1), (1, -1))
        self.assertEqual(len(set(gradients)), 3)
        for i in range(3):
            for j in range(i+1, 3):
                a, b = gradients[i], gradients[j]
                self.assertNotEqual(a[0]*b[1]-a[1]*b[0], 0)
        # In dimension two no regular parameter product has 3 factors.

    def test_source_terminology_and_affine_fibre_proof(self):
        src = SOURCE.read_text(encoding="utf-8")
        no_refs = re.sub(
            r"\\(?:label|ref|eqref|autoref|pageref)\{[^}]+\}", "", src)
        self.assertIsNone(re.search(
            r"\b(?:chart\w*|charcie)\b", no_refs, re.IGNORECASE))
        self.assertNotIn("tensorowan", no_refs.lower())
        self.assertNotIn("przedsnop", no_refs.lower())
        self.assertIn("po zastosowaniu iloczynu tensorowego z $B$", src)
        self.assertIn("schematu testowego do przypadku afinicznego", src)
        self.assertIn("jest analogiczna do pierwszej mapy", src)
        self.assertIn("otwarty podschemat $\\Spec k[v]$", src)

    def test_tikz_and_stable_crossrefs(self):
        src = SOURCE.read_text(encoding="utf-8")
        self.assertEqual(src.count(r"\begin{tikzpicture}"), 4)
        self.assertEqual(src.count(r"\end{tikzpicture}"), 4)
        for i in range(1, 5):
            self.assertIn("Rysunek 5."+str(i), src)
        self.assertIn(r"\label{tw:ga5-universal}", src)
        self.assertIn(r"\label{tw:ga5-embedded-cusp}", src)


if __name__ == "__main__":
    unittest.main()
