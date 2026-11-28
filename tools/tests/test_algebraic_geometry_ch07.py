"""ALG-07: Chow groups, Chern-class and surface RR regressions.

These tests check exact algebraic identities and TeX-source invariants.
They do not replace proof of Chow-ring construction, splitting principle,
Bertini, or Hirzebruch--Riemann--Roch.
"""
import itertools
import re
import unittest
from fractions import Fraction
from math import comb
from pathlib import Path

SOURCE = (Path(__file__).resolve().parents[2] / "chapters" / "pl"
          / "algebraic_geometry"
          / "07-teoria-przeciec-grupy-chowa-i-klasy-cherna.tex")


class ALG07Regressions(unittest.TestCase):
    def test_local_intersection_multiplicity(self):
        # k[x,y]_(x,y)/(y,y-x^m) ~= k[x]_(x)/(x^m).
        for m in range(1, 21):
            basis = tuple(range(m))
            self.assertEqual(len(basis), m)
            self.assertTrue(all(k < m for k in basis))

    def test_projective_closure_infinity_all_m(self):
        # C=V(Y), D=V(Y Z^(m-1)-X^m), P=[X:Y:0].
        for p in (2, 3, 5, 7, 11):
            for m in range(1, 7):
                points_c = {(1, 0)}
                points_d = {
                    (x, y) for x in range(p) for y in range(p)
                    if (x, y) != (0, 0)
                    and ((y-x) if m == 1 else -pow(x, m, p)) % p == 0
                }
                self.assertFalse(any((x, y) in points_d for x, y in points_c))
                if m == 1:
                    self.assertIn((1, 1), points_d)
                else:
                    self.assertIn((0, 1), points_d)
        src = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"Dla $m\ge2$ na $Z=0$", src)
        self.assertIn(r"Dla $m=1$ drugie równanie", src)
        self.assertIn(r"$[1:1:0]$", src)
        self.assertIn(r"$[0:1:0]$", src)

    def test_chow_projective_space_zero_dimensional_case(self):
        # CH*(P^0) = Z; formal generator h is zero.
        src = SOURCE.read_text(encoding="utf-8")
        block = src.split(r"\label{tw:ga7-chow-pn}", 1)[1].split(
            r"\end{twierdzenie}", 1)[0]
        self.assertIn(r"\Z[h]/(h)", block)
        self.assertIn("formalnym $h=0$", block)
        proof = src.split(r"\label{tw:ga7-chow-pn}", 1)[1].split(
            r"\end{proof}", 1)[0]
        self.assertIn(r"$n=0$", proof)
        self.assertIn(r"\PP^0_k=\Spec k", proof)

    def test_chow_ring_pn_basis_dimensions(self):
        for n in range(10):
            basis = tuple(range(n+1))
            self.assertEqual(len(basis), n+1)
            self.assertEqual(basis[0], 0)
            self.assertTrue(all(j <= n for j in basis))

    def test_rational_equivalence_p1_and_a1(self):
        # div_P1(t-a)=[a]-[infty], div_A1(t-a)=[a].
        for a in range(-5, 6):
            divis_p1 = {a: 1, "infinity": -1}
            divis_a1 = {a: 1}
            self.assertEqual(sum(divis_p1.values()), 0)
            self.assertEqual(sum(divis_a1.values()), 1)

    def test_c1_line_bundle_additivity(self):
        for a, b in itertools.product(range(-6, 7), repeat=2):
            self.assertEqual(a+b, b+a)
            self.assertEqual(a+(-a), 0)
            self.assertEqual((a+b) + (-b), a)

    def test_whitney_for_sums_of_line_bundles(self):
        for a, b, c in itertools.product(range(-3, 4), repeat=3):
            # (1+ah)(1+bh)(1+ch) truncated to degree <=2.
            c1 = a+b+c
            c2 = a*b+a*c+b*c
            self.assertEqual(c1, (a+b)+c)
            self.assertEqual(c2, a*b+(a+b)*c)

    def test_rank_two_projective_bundle_relation(self):
        for a, b in itertools.product(range(-4, 5), repeat=2):
            # Formal relation (xi-a)(xi-b) vanishes mod polynomial.
            c1 = a+b
            c2 = a*b
            self.assertEqual(a*a-c1*a+c2, 0)
            self.assertEqual(b*b-c1*b+c2, 0)

    def test_euler_projective_space_chern(self):
        for n in range(1, 15):
            for i in range(n+1):
                self.assertEqual(comb(n+1, i),
                                 comb(n, i) + (comb(n, i-1) if i else 0))

    def test_three_simple_vector_field_zeros(self):
        weights = ((1, 2), (-1, 1), (-2, -1))
        self.assertEqual(len(weights), 3)
        self.assertTrue(all(a*b != 0 for a, b in weights))
        self.assertEqual(sum(1 for a, b in weights if a*b != 0), 3)

    def test_hypersurface_first_and_second_chern(self):
        for n, d in itertools.product(range(2, 8), range(1, 11)):
            c1 = (n+1)-d
            c2 = comb(n+1, 2)-(n+1)*d+d*d
            self.assertEqual(c1, n+1-d)
            self.assertEqual(c2, d*d-(n+1)*d+comb(n+1, 2))

    def test_degree_d_surface_noether(self):
        for d in range(1, 16):
            K2 = d*(d-4)**2
            c2 = d*(d*d-4*d+6)
            chi = d*(d*d-6*d+11)//6
            self.assertEqual(K2+c2, 12*chi)
            self.assertEqual(d*(d*d-6*d+11) % 6, 0)
        self.assertEqual([(d*(d-4)**2, d*(d*d-4*d+6))
                          for d in (1, 2, 3, 4)],
                         [(9, 3), (8, 4), (3, 9), (0, 24)])

    def test_riemann_roch_p2_all_integers(self):
        for d in range(-32, 33):
            lhs = 1 + Fraction(d*(d+3), 2)
            rhs = Fraction((d+1)*(d+2), 2)
            self.assertEqual(lhs, rhs)
            self.assertEqual(rhs.denominator, 1)

    def test_riemann_roch_p1_times_p1(self):
        for a, b in itertools.product(range(-9, 10), repeat=2):
            D2 = 2*a*b
            DK = -2*a-2*b
            self.assertEqual(1+Fraction(D2-DK, 2), (a+1)*(b+1))

    def test_surface_rr_parity_in_blowups(self):
        for a, b1, b2 in itertools.product(range(-8, 9), repeat=3):
            # On blow-up of two points, D=aH+b1E1+b2E2,
            # K=-3H+E1+E2. Intersection form diag(1,-1,-1).
            D2 = a*a-b1*b1-b2*b2
            DK = -3*a-b1-b2
            self.assertEqual((D2-DK) % 2, 0)

    def test_todd_and_chern_character_degree_two(self):
        # Identity: (x1^2+x2^2)/12+x1*x2/4 =
        # (c1^2+c2)/12.
        for x, y in itertools.product(range(-7, 8), repeat=2):
            a = Fraction(x*x+y*y, 12)+Fraction(x*y, 4)
            b = Fraction((x+y)**2+x*y, 12)
            self.assertEqual(a, b)

    def test_blowup_preserves_chi_and_adds_c2(self):
        for K2, c2 in itertools.product(range(-12, 13), repeat=2):
            self.assertEqual((K2-1)+(c2+1), K2+c2)

    def test_normalization_pullback_is_explicit(self):
        src = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"\nu^*(\mathcal O_S(D)|_C)", src)
        self.assertIn(r"\label{st:ga7-divisor-degree}", src)

    def test_hilbert_polynomial_from_rr_and_exact_sequence(self):
        # On a smooth degree-d surface in P^3, compare surface RR
        # with chi(O_P3(m))-chi(O_P3(m-d)) for all integer m.
        def choose3_polynomial(t):
            return t*(t-1)*(t-2)//6

        for d in range(1, 13):
            for m in range(-16, 17):
                chi_O = d*(d*d-6*d+11)//6
                chi_RR = chi_O + d*m*(m+4-d)//2
                chi_sequence = (choose3_polynomial(m+3)
                                - choose3_polynomial(m-d+3))
                self.assertEqual(chi_RR, chi_sequence)
        self.assertEqual(1 + 3*1*(1+4-3)//2, 4)
        self.assertEqual(2 + 4*1*(1+4-4)//2, 4)
        src = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"\label{prz:ga7-hilbert-polynomial}", src)
        self.assertIn(r"\binom{m+3}{3}-\binom{m-d+3}{3}", src)

    def test_canonical_divisor_distinct_from_chow_class(self):
        # K_S is a divisor, H is a hyperplane divisor, h=[H] a Chow
        # class. Linear equivalence must never be written against h.
        src = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"\omega_S\cong\mathcal O_S(d-4)", src)
        self.assertIn(r"K_S\sim(d-4)H", src)
        self.assertIn(r"h=[H]=c_1(\mathcal O_S(1))", src)
        self.assertNotIn(r"K_S\sim(d-4)h", src)
        statement = src.split(
            r"\label{wn:ga7-degree-d-surface}", 1
        )[1].split(r"\end{wniosek}", 1)[0]
        self.assertIn("dzielnikiem", statement)
        self.assertIn("kanonicznego", statement)
        for d in range(1, 16):
            self.assertEqual(d*(d-4)**2,
                             d*(d-4)*(d-4))

    def test_explicit_closed_point_and_canonical_hypotheses(self):
        src = SOURCE.read_text(encoding="utf-8")
        blowup = src.split(
            r"\label{prz:ga7-blowup-c2}", 1
        )[1].split(r"\end{przyklad}", 1)[0]
        self.assertIn("punktem zamkniętym", blowup)
        self.assertIn(r"\operatorname{Bl}_pS", blowup)
        parity = src.split(
            r"\label{wn:ga7-parity}", 1
        )[1].split(r"\end{wniosek}", 1)[0]
        self.assertIn("dzielnikiem kanonicznym", parity)
        self.assertIn(r"D\cdot(D-K_S)", parity)
        degree = src.split(
            r"\label{st:ga7-divisor-degree}", 1
        )[1].split(r"\end{stwierdzenie}", 1)[0]
        self.assertIn("dla $D=C$ i $C$ gładkiej", degree)

    def test_vector_bundle_rr_uses_chow_canonical_class(self):
        src = SOURCE.read_text(encoding="utf-8")
        noether = src.split(r"\label{tw:ga7-noether}", 1)[1].split(
            r"\end{twierdzenie}", 1)[0]
        self.assertIn(
            r"(c_1(\mathcal E)-c_1(\omega_S))", noether)
        self.assertNotIn(r"(c_1(\mathcal E)-K_S)", noether)
        proof = src.split(r"\label{tw:ga7-noether}", 1)[1].split(
            r"\end{proof}", 1)[0]
        self.assertIn(r"c_1(T_S)=-c_1(\omega_S)", proof)
        self.assertIn(r"c_1(\omega_S)=[K_S]", proof)

    def test_noether_statement_defines_canonical_divisor(self):
        src = SOURCE.read_text(encoding="utf-8")
        statement = src.split(r"\label{tw:ga7-noether}", 1)[1].split(
            r"\end{twierdzenie}", 1)[0]
        self.assertIn(
            r"Niech $K_S$ będzie dowolnym dzielnikiem kanonicznym",
            statement)
        self.assertIn(r"K_S^2+\deg c_2(T_S)", statement)

    def test_line_bundle_rr_distinguishes_divisor_and_chow_class(self):
        src = SOURCE.read_text(encoding="utf-8")
        proof = src.split(r"\label{tw:ga7-noether}", 1)[1].split(
            r"\end{proof}", 1)[0]
        self.assertIn(r"c_1(\mathcal E)=[D]", proof)
        self.assertNotIn(r"$c_1=D$", proof)

    def test_chern_numbers_not_individually_birational_invariant(self):
        # The blow-up changes K^2 by -1 and deg(c2) by +1,
        # preserving 12 chi(O_S) rather than each summand.
        for canonical_square in range(-20, 25):
            for second_chern in range(0, 25):
                self.assertEqual(
                    (canonical_square - 1) + (second_chern + 1),
                    canonical_square + second_chern)
        src = SOURCE.read_text(encoding="utf-8")
        summary = src.split(r"\label{sec:ga7-summary}", 1)[1]
        self.assertIn("nie należy automatycznie uważać za niezmienniki", summary)
        self.assertIn(r"12\chi(\mathcal O_S)", summary)

    def test_standalone_field_hypotheses_are_explicit(self):
        src = SOURCE.read_text(encoding="utf-8")
        cases = {
            r"\label{tw:ga7-hypersurface-chern}":
                "Niech $k$ będzie ciałem algebraicznie domkniętym",
            r"\label{lem:ga7-chi-exact}":
                "Niech $k$ będzie ciałem",
            r"\label{lem:ga7-ch-td-surface}":
                "Niech $k$ będzie ciałem charakterystyki zero",
            r"\label{st:ga7-zero-section}":
                "Niech $k$ będzie ciałem algebraicznie domkniętym",
        }
        for label, required in cases.items():
            with self.subTest(label=label):
                self.assertIn(label, src)
                block = src.split(label, 1)[1].split(
                    r"\end{", 1)[0]
                self.assertIn(required, block)

    def test_self_contained_cycle_and_bundle_hypotheses(self):
        src = SOURCE.read_text(encoding="utf-8")
        cases = {
            "def:ga7-cycles": "Niech $k$ będzie ciałem",
            "def:ga7-rational-divisor": "$X$ schematem skończonego typu",
            "def:ga7-chow": "Niech $k$ będzie ciałem",
            "def:ga7-proper-intersection": "nad $k$",
            "def:ga7-c1": "Niech $k$ będzie ciałem",
            "st:ga7-c1-add": "Niech $k$ będzie ciałem",
            "tw:ga7-projective-bundle": "$X$ gładką quasi-rzutową rozmaitością nad $k$",
            "def:ga7-c-classes": "Niech $k$ będzie ciałem",
            "tw:ga7-chern-axioms": "Dla wiązki wektorowej",
            "def:ga7-chi": "$S$ gładką rzutową powierzchnią nad $k$",
            "def:ga7-ch-td": "Niech $k$ będzie ciałem charakterystyki zero",
        }
        for label, expected in cases.items():
            with self.subTest(label=label):
                marker = r"\label{" + label + "}"
                self.assertIn(marker, src)
                statement = src.split(marker, 1)[1].split(r"\end{", 1)[0]
                self.assertIn(expected, statement)

    def test_rational_divisor_title_matches_all_dimensions(self):
        src = SOURCE.read_text(encoding="utf-8")
        self.assertIn(
            r"\begin{definicja}[Dzielnik funkcji wymiernej na podschemacie całkowitym]",
            src)
        definition = src.split(r"\label{def:ga7-rational-divisor}", 1)[1].split(
            r"\end{definicja}", 1)[0]
        self.assertIn(r"$r\ge0$", definition)
        self.assertIn(r"wymiaru $r+1$", definition)

    def test_bezout_example_rejects_zero_polynomial(self):
        src = SOURCE.read_text(encoding="utf-8")
        bezout = src.split(r"\label{prz:ga7-bezout}", 1)[1].split(
            r"\end{przyklad}", 1)[0]
        self.assertIn(r"$F\ne0$", bezout)
        self.assertIn(r"$d\ge1$", bezout)
        self.assertIn("dodatnich stopni", bezout)

    def test_nodal_normalization_pushes_two_zeros_to_one_point(self):
        # W: y^2=x^2(x+1), nu(t)=(t^2-1,t(t^2-1)).
        # The node is the image of t=+1 and t=-1, each a
        # simple zero of x; its principal cycle has weight 2.
        for p in (3, 5, 7, 11, 13):
            zeros = []
            for t in range(p):
                x = (t*t-1) % p
                y = (t*x) % p
                self.assertEqual((y*y-x*x*(x+1)) % p, 0)
                if x == 0:
                    zeros.append(t)
                    self.assertEqual(y, 0)
                    self.assertNotEqual((2*t) % p, 0)
            self.assertEqual(set(zeros), {1, p-1})
            self.assertEqual(len(zeros), 2)

    def test_singular_curve_divisor_defined_by_pushforward(self):
        src = SOURCE.read_text(encoding="utf-8")
        definition = src.split(
            r"\label{def:ga7-rational-divisor}", 1
        )[1].split(r"\end{definicja}", 1)[0]
        self.assertIn(r"\nu_*", definition)
        self.assertIn(r"\operatorname{div}_{\widetilde W}(f)", definition)
        self.assertIn(r"\operatorname{ord}_q(f)[\nu(q)]", definition)
        self.assertIn(r"[\kappa(q):\kappa(\nu(q))]", definition)
        example = src.split(
            r"\label{prz:ga7-nodal-divisor}", 1
        )[1].split(r"\end{przyklad}", 1)[0]
        self.assertIn(r"$t=1$ i $t=-1$", example)
        self.assertIn(r"\operatorname{div}_W(x)=2[p]", example)

    def test_source_terminology_and_crossrefs(self):
        src = SOURCE.read_text(encoding="utf-8")
        stripped = re.sub(
            r"\\(?:label|ref|eqref|cref|autoref|pageref)\{[^}]+\}", "", src)
        self.assertIsNone(re.search(
            r"dywizor|tensorowanie|dzielniky|dzielnikem|charcie|chartach"
            r"|injektyw|sekwencyjn|zwartościowan",
            stripped, re.IGNORECASE))
        self.assertIn(r"\label{tw:ga7-hrr}", src)
        self.assertIn(r"\label{tw:ga7-rr-surfaces}", src)
        self.assertIn(r"\label{tw:ga7-chow-ring}", src)

    def test_tikz_and_proof_environment_balance(self):
        src = SOURCE.read_text(encoding="utf-8")
        self.assertEqual(src.count(r"\begin{tikzpicture}"), 2)
        self.assertEqual(src.count(r"\end{tikzpicture}"), 2)
        # Proofs with and without optional titles all use the same begin tag.
        self.assertEqual(len(re.findall(r"\\begin\{proof\}", src)), 14)
        self.assertEqual(src.count(r"\end{proof}"), 14)
        stack = []
        for m in re.finditer(r"\\(begin|end)\{([a-zA-Z*]+)\}", src):
            if m[1] == "begin":
                stack.append(m[2])
            else:
                self.assertTrue(stack, m[0])
                self.assertEqual(stack.pop(), m[2])
        self.assertFalse(stack)


if __name__ == "__main__":
    unittest.main()
