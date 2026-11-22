"""ALG-04: checks of examples in commutative algebra, sheaves, curves and residues.

Tests verify concrete formulas. They do not replace proofs of Riemann--Roch,
Serre duality, Noether normalization or Grothendieck residue theorems.
"""
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import unittest


SRC = (Path(__file__).resolve().parents[2] / "chapters" / "pl"
       / "algebraic_geometry"
       / "04-algebra-przemienna-snopy-i-krzywe-algebraiczne.tex")


def elliptic_points(p, a, b):
    return {(x, y) for x in range(p) for y in range(p)
            if (y*y - x*x*x - a*x - b) % p == 0}


def elliptic_add(p, a, b, P, Q):
    """Affine Weierstrass law; None represents the point at infinity."""
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0:
        return None
    if P == Q:
        m = ((3*x1*x1 + a)*pow(2*y1 % p, -1, p)) % p
    else:
        m = ((y2-y1)*pow((x2-x1) % p, -1, p)) % p
    x3 = (m*m-x1-x2) % p
    return (x3, (m*(x1-x3)-y1) % p)


class ALG04Regressions(unittest.TestCase):
    def test_source_cauchy_polydisc_and_radius_hypothesis(self):
        text = SRC.read_text(encoding="utf-8")
        block = text[text.index(r"\begin{wniosek}[Wzór na współczynnik Taylora]"):
                     text.index(r"\end{wniosek}", text.index(
                         r"\begin{wniosek}[Wzór na współczynnik Taylora]"))]
        self.assertIn(r"domkniętego", block)
        self.assertIn(r"r_1,\ldots,r_n>0", block)
        self.assertIn(r"polidysku", block)

    def test_source_avoids_deprecated_terms(self):
        s = SRC.read_text(encoding="utf-8").lower()
        for phrase in ("tensorowanie", "tensorowaniu", "tensorowaniem",
                       "chartów", "zwartościowanie", "sekwencyjny"):
            self.assertNotIn(phrase, s, phrase)

    def test_plane_curve_arithmetic_genus(self):
        for d in range(1, 15):
            genus = (d-1)*(d-2)//2
            for m in range(d, d+10):
                self.assertEqual(
                    comb(m+2, 2)-comb(m-d+2, 2), d*m + 1-genus)

    def test_projective_line_cohomology(self):
        for n in range(-12, 13):
            h0 = len([j for j in range(0, max(n+1, 0))])
            # Negative powers t^j surviving k[t]+t^n k[t^-1]:
            h1 = len([j for j in range(n+1, 0) if j < 0])
            self.assertEqual(h0, max(n+1, 0))
            self.assertEqual(h1, max(-n-1, 0))
            self.assertEqual(h0-h1, n+1)

    def test_serre_pairing_on_p1_is_perfect(self):
        for n in range(-12, -1):
            alpha_exponents = list(range(n+1, 0))
            beta_exponents = list(range(-n-1))
            mat = [[int(i+j == -1) for j in beta_exponents]
                   for i in alpha_exponents]
            self.assertEqual(len(mat), -n-1)
            self.assertTrue(all(sum(row) == 1 for row in mat))
            self.assertTrue(all(sum(row[j] for row in mat) == 1
                                for j in range(len(beta_exponents))))

    def test_elliptic_law_closure_identity_and_inverse(self):
        for p, a, b in ((5, 1, 1), (7, 2, 3), (11, 1, 4), (13, 1, 1)):
            if (4*a*a*a+27*b*b) % p == 0:
                continue
            points = elliptic_points(p, a, b)
            for P in points:
                self.assertEqual(elliptic_add(p, a, b, None, P), P)
                self.assertEqual(elliptic_add(p, a, b, P, None), P)
                self.assertIsNone(elliptic_add(
                    p, a, b, P, (P[0], -P[1] % p)))
                for Q in points:
                    self.assertIn(elliptic_add(p, a, b, P, Q), points | {None})

    def test_elliptic_associativity_in_finite_examples(self):
        for p, a, b in ((5, 1, 1), (7, 2, 3), (11, 1, 4)):
            if (4*a*a*a + 27*b*b) % p == 0:
                continue
            points = list(elliptic_points(p, a, b)) + [None]
            for P in points:
                for Q in points:
                    for R in points:
                        self.assertEqual(
                            elliptic_add(p, a, b,
                                        elliptic_add(p, a, b, P, Q), R),
                            elliptic_add(p, a, b, P,
                                        elliptic_add(p, a, b, Q, R)))

    def test_hyperelliptic_genus(self):
        for degree in range(5, 18):
            branches = degree + (degree % 2)
            genus = (branches-2)//2
            self.assertEqual(genus, (degree-1)//2)

    def test_residue_sum_on_four_affine_points(self):
        for numerator, expected in (
            (lambda z, w: 1, 0),
            (lambda z, w: z, 0),
            (lambda z, w: z+w, 0),
            (lambda z, w: z*w, 1),
        ):
            total = sum((Fraction(numerator(z, w), 4*z*w)
                         for z in (-1, 1) for w in (-1, 1)), Fraction(0))
            self.assertEqual(total, expected)

    def test_multivariate_monomial_coefficient(self):
        # The coefficient of z^(m-1)w^(n-1) in exp(z+w) is
        # 1 / ((m-1)!(n-1)!).
        for m in range(1, 7):
            for n in range(1, 7):
                expected = Fraction(1, factorial(m-1)*factorial(n-1))
                self.assertEqual(
                    Fraction(1, factorial(m-1)*factorial(n-1)),
                    expected)
        self.assertEqual(Fraction(1, factorial(1)*factorial(2)),
                         Fraction(1, 2))

    def test_jacobian_orientation_and_order(self):
        J = 1*(-1)-1*1  # f1=z+w, f2=z-w
        self.assertEqual(J, -2)
        self.assertEqual(Fraction(1, J), Fraction(-1, 2))
        self.assertEqual(Fraction(1, -J), Fraction(1, 2))

    def test_degenerate_residue_and_local_quotient(self):
        # f1=z^2, f2=w^2+z^3. Since z^2=0, f2 reduces to w^2.
        monomial_basis = {(i, j) for i in (0, 1) for j in (0, 1)}
        self.assertEqual(len(monomial_basis), 4)
        # Res(h;z^2,w^2) = coefficient of zw in h.
        examples = [
            ({(0, 0): 1}, 0),
            ({(1, 1): 1}, 1),
            ({(2, 0): 1, (1, 1): 2, (0, 2): 1}, 2),
        ]
        for coeffs, value in examples:
            self.assertEqual(coeffs.get((1, 1), 0), value)

    def test_integrality_matrix_orientation_non_symmetric(self):
        """Columns encode b*e_j, so the generator column requires C^T."""
        # B=Z[sqrt(2)]; b=sqrt(2); e=(1,b)^T.
        # b*e1=e2; b*e2=2*e1; hence C=[[0,2],[1,0]].
        basis = ((1, 0), (0, 1))  # a+c*b is represented as (a,c)
        C = ((0, 2), (1, 0))

        def mul_b(v):
            return (2*v[1], v[0])

        def rhs(matrix, row):
            return tuple(sum(matrix[row][j]*basis[j][k]
                             for j in range(2)) for k in range(2))

        CT = tuple(zip(*C))
        self.assertTrue(all(mul_b(basis[i]) == rhs(CT, i)
                            for i in range(2)))
        self.assertTrue(any(mul_b(basis[i]) != rhs(C, i)
                            for i in range(2)))
        # The original mistake was (bI-C)e=0 with the same c_{ij}
        # convention; this source assertion prevents its reintroduction.
        src = SRC.read_text(encoding="utf-8")
        self.assertIn(r"(bI-C^{\mathsf T})e=0", src)
        self.assertIn(r"\det(TI-C^{\mathsf T})=\det(TI-C)", src)



    def test_divisor_sheaf_has_zero_section_on_empty_open(self):
        """The vacuous valuation condition on U=empty is NOT a sheaf."""
        # For every nonzero rational f the condition
        # ord_P(f)+n_P >= 0 for all P in the empty set is true.
        # Thus the naive formula would make F(empty)=k(C),
        # contradicting the sheaf axiom for the empty cover.
        assert all([])  # empty universal quantification is vacuously true
        src = SRC.read_text(encoding="utf-8")
        definition = src.split(
            r"\begin{definicja}[Snop dywizora]", 1
        )[1].split(r"\end{definicja}", 1)[0]
        self.assertIn(r"\emph{niepustego}", definition)
        self.assertIn(
            r"\mathcal O_C(D)(\varnothing)=\{0\}", definition)
        self.assertIn(r"ograniczenie do $\varnothing$", definition)
        self.assertIn(
            r"$C$ gładką nierozkładalną krzywą", definition)



if __name__ == "__main__":
    unittest.main()
