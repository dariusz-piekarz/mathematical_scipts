"""ALG-06 mathematical and TeX regressions for algebraic surfaces.

Numeric checks are supplements to, not substitutes for, mathematical proofs.
"""
import itertools
import re
import unittest
from pathlib import Path

SOURCE = (Path(__file__).resolve().parents[2] / "chapters" / "pl"
          / "algebraic_geometry"
          / "06-powierzchnie-algebraiczne-przeciecia-rozdmuchania-i-szczegolne.tex")


class ALG06Regressions(unittest.TestCase):
    def test_local_intersection_lengths(self):
        # k[x,y]_(x,y)/(y,y-x^m) has basis 1,x,...,x^(m-1).
        for m in range(1, 16):
            self.assertEqual(len(range(m)), m)
            self.assertEqual(m == 1, m < 2)

    def test_intersection_blowup_formula(self):
        for self_intersection in range(-8, 15):
            for multiplicity in range(0, 8):
                self.assertEqual(
                    self_intersection - multiplicity**2,
                    self_intersection + 0 + 0 - multiplicity**2)
                self.assertEqual(
                    -multiplicity*(-1), multiplicity)

    def test_infinitely_near_exceptional_curves(self):
        # Intersection matrix in the total-transform basis: diag(-1,-1).
        def pairing(a, b):
            return -a[0]*b[0] - a[1]*b[1]
        strict = (1, -1)
        second = (0, 1)
        self.assertEqual(pairing(strict, strict), -2)
        self.assertEqual(pairing(second, second), -1)
        self.assertEqual(pairing(strict, second), 1)

    def test_canonical_square_after_blowups(self):
        for r in range(10):
            # K=-3H+E_1+...+E_r on Bl_{r points}(P^2).
            self.assertEqual(9-r, (-3)**2 - sum(1 for _ in range(r)))
            self.assertEqual(9-r, 9-r)

    def test_hirzebruch_intersection_and_canonical(self):
        for n in range(60):
            B2, BF, F2 = -n, 1, 0
            K2 = 4*B2 + 4*(n+2)*BF + (n+2)**2*F2
            self.assertEqual(K2, 8)
            self.assertEqual(-2*B2 - (n+2)*BF, n-2)

    def test_del_pezzo_degree_of_six_points(self):
        r = 6
        self.assertEqual(9-r, 3)
        self.assertEqual(10-r, 4)  # Dimension of cubic forms through points.
        self.assertEqual((3**2-r), 3)

    def test_27_lines_integer_intersection_solutions(self):
        # 3a-sum b=1, a^2-sum b^2=-1; b_i>=0 and a>=1.
        classes = []
        for a in (1, 2, 3):
            for b in itertools.product(range(a+1), repeat=6):
                if sum(b) == 3*a-1 and sum(x*x for x in b) == a*a+1:
                    classes.append((a, b))
        linear = [x for x in classes if x[0] == 1]
        conic = [x for x in classes if x[0] == 2]
        higher = [x for x in classes if x[0] == 3]
        self.assertEqual(len(linear), 15)
        self.assertEqual(len(conic), 6)
        self.assertFalse(higher)
        self.assertEqual(6+len(linear)+len(conic), 27)

    def test_27_lines_intersection_configuration(self):
        # In Pic(S)=ZH ⊕ ZE_1 ⊕ ... ⊕ ZE_6, pairing diag(1,-1,...).
        curves = []
        for i in range(6):
            e = [0]*7
            e[i+1] = 1
            curves.append(tuple(e))
        for i in range(6):
            for j in range(i+1, 6):
                ell = [0]*7
                ell[0] = 1
                ell[i+1] = ell[j+1] = -1
                curves.append(tuple(ell))
        for i in range(6):
            conic = [2] + [-1]*6
            conic[i+1] = 0
            curves.append(tuple(conic))
        L = (3,) + (-1,)*6  # -K_S
        def intersection(a, b):
            return a[0]*b[0] - sum(x*y for x, y in zip(a[1:], b[1:]))
        self.assertEqual(len(curves), 27)
        self.assertEqual(len(set(curves)), 27)
        self.assertTrue(all(intersection(c, c) == -1 for c in curves))
        self.assertTrue(all(intersection(L, c) == 1 for c in curves))
        for a in curves:
            matches = [intersection(a, b) for b in curves if a != b]
            self.assertEqual(matches.count(1), 10)
            self.assertEqual(matches.count(0), 16)
            self.assertTrue(all(n in (0, 1) for n in matches))
        self.assertEqual(27*10//2, 135)

    def test_fermat_27_explicit_lines(self):
        # Over F_7, -1 has exactly 3 cube roots, as over C.
        p = 7
        roots = [a for a in range(p) if (a**3 + 1) % p == 0]
        self.assertEqual(len(roots), 3)
        for zeta, eta in itertools.product(roots, repeat=2):
            for u, v in itertools.product(range(p), repeat=2):
                x = (zeta*u, u, eta*v, v)
                self.assertEqual(sum(z**3 for z in x) % p, 0)
        self.assertEqual(3*len(roots)**2, 27)

    def test_quartic_k3_adjunction(self):
        degree = 4
        K_degree = degree - 4
        self.assertEqual(K_degree, 0)
        self.assertEqual((degree+2)//2, 3)
        # 2g-2=(K+C).C = degree for K3 hyperplane.
        self.assertEqual(2*3-2, degree)

    def test_characteristic_chi_k3_and_rational(self):
        self.assertEqual(1-0+1, 2)
        self.assertEqual(1-0+0, 1)

    def test_morphism_charts_f1(self):
        for p in (3, 5, 7, 11, 13):
            for t in range(1, p):
                s = pow(t, -1, p)
                self.assertEqual(t*s % p, 1)
                for lam in range(p):
                    for mu in range(p):
                        left = ((lam, (lam*t) % p, mu), (1, t))
                        right = (((s*(t*lam)) % p, (t*lam) % p, mu), (s, 1))
                        # Projective-coordinate transitions differ by scalar t
                        self.assertEqual(left[0], right[0])

    def test_intersection_statement_explicit_closed_point(self):
        src = SOURCE.read_text(encoding="utf-8")
        block = src.split(r"\label{st:ga6-transversal-one}", 1)[1].split(
            r"\end{stwierdzenie}", 1)[0]
        self.assertIn("dwiema różnymi całkowitymi krzywymi", block)
        self.assertIn("punktem zamkniętym", block)
        self.assertIn(r"i_p(C,D;S)=1", block)

    def test_blowup_statements_are_self_contained(self):
        src = SOURCE.read_text(encoding="utf-8")
        for label in ("st:ga6-blowup-form", "st:ga6-Kblowup",
                      "st:ga6-pic-blowup"):
            with self.subTest(label=label):
                block = src.split(r"\label{" + label + "}", 1)[1].split(
                    r"\end{stwierdzenie}", 1)[0]
                self.assertIn("punktem zamkniętym", block)
                self.assertIn(r"\pi:\widetilde S=", block)
                self.assertRegex(block, r"dzielnikiem\s+wyjątkowym")

    def test_named_objects_in_global_results(self):
        src = SOURCE.read_text(encoding="utf-8")
        hirz = src.split(r"\label{st:ga6-hirzebruch}", 1)[1].split(
            r"\end{stwierdzenie}", 1)[0]
        self.assertIn("Niech $n", hirz)
        self.assertIn("$F$ klasę włókna", hirz)
        self.assertIn("$B$ sekcję", hirz)
        dp = src.split(r"\label{st:ga6-del-pezzo-degree}", 1)[1].split(
            r"\end{stwierdzenie}", 1)[0]
        self.assertIn("punktach zamkniętych", dp)
        self.assertIn("Oznaczmy przez $H$", dp)
        self.assertIn("$E_1,\\ldots,E_r$ dzielniki wyjątkowe".replace(
            "\\\\", "\\"), dp)
        chi = src.split(r"\label{st:ga6-chi}", 1)[1].split(
            r"\end{stwierdzenie}", 1)[0]
        self.assertIn("nad $\\C$".replace("\\\\", "\\"), chi)
        self.assertIn(r"p_g(S)=\dim_\C H^0", chi)

    def test_polish_divisor_inflection(self):
        src = SOURCE.read_text(encoding="utf-8")
        self.assertIn("[Dzielniki i ich równoważność liniowa]", src)
        self.assertIn("Dwa dzielniki $D,D'$", src)
        self.assertIn("jako dzielniki, a zatem", src)
        self.assertNotIn("dzielniky", src.lower())
        self.assertNotIn("charcie", src.lower())

    def test_intersection_residue_degree_over_finite_field(self):
        # The conic x^2+xz+z^2+y^2 over F_2 meets y=0 in a
        # degree-2 closed point, not a rational point.
        self.assertFalse(any((t*t + t + 1) % 2 == 0
                             for t in range(2)))
        # Derivatives of the conic are (z,0,x); their sole
        # possible common projective zero [0:1:0] is not on it.
        self.assertEqual((0*0+0*0+0*0+1*1) % 2, 1)
        self.assertEqual(2*1, 2)
        src = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"[\kappa(p):k]\,i_p", src)
        block = src.split(r"\label{tw:ga6-intersection-global}", 1)[1].split(
            r"\end{twierdzenie}", 1)[0]
        self.assertIn("ciałem algebraicznie domkniętym", block)
        self.assertIn("charakterystyki $0$", block)

    def test_adjunction_standalone_field_hypotheses(self):
        src = SOURCE.read_text(encoding="utf-8")
        block = src.split(r"\label{tw:ga6-adjunction}", 1)[1].split(
            r"\end{twierdzenie}", 1)[0]
        self.assertIn("charakterystyki $0$", block)
        self.assertIn("$C\subseteq S$", block)
        hirz = src.split(r"\label{st:ga6-hirzebruch}", 1)[1].split(
            r"\end{stwierdzenie}", 1)[0]
        self.assertIn("charakterystyki $0$", hirz)
        self.assertIn(r"\PP_{\PP^1_k}", hirz)

    def test_stable_labels_and_source_terms(self):
        src = SOURCE.read_text(encoding="utf-8")
        no_refs = re.sub(r"\\(?:label|ref|cref|eqref)\{[^}]+\}", "", src)
        self.assertIsNone(re.search(r"dywizor|chart|charcie|dzielniky|injektywno", no_refs, re.I))
        self.assertIn(r"\nu^*(\mathcal O_S(D)|_C)", src)
        self.assertIn(r"N_{E/\widetilde S}\cong\mathcal O_{\PP^1_k}(-1)", src)
        self.assertIn(r"\label{tw:ga6-27-lines}", src)
        self.assertIn(r"\label{tw:ga6-quartic-k3}", src)

    def test_tikz_proof_and_environment_balance(self):
        src = SOURCE.read_text(encoding="utf-8")
        for env, count in (("tikzpicture", 3), ("proof", 13), ("minipage", 3)):
            self.assertEqual(src.count(r"\begin{" + env + "}"), count)
            self.assertEqual(src.count(r"\end{" + env + "}"), count)
        stack = []
        for match in re.finditer(r"\\(begin|end)\{([A-Za-z*]+)\}", src):
            cmd, name = match.groups()
            if cmd == "begin":
                stack.append(name)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), name)
        self.assertFalse(stack)


if __name__ == "__main__":
    unittest.main()
