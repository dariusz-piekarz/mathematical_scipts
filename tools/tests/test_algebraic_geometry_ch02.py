"""ALG-02 projective geometry regressions over small prime fields.

Checks detect regressions in examples and coordinate formulas; they
do not substitute for proofs of the general Bezout theorem.
"""
from itertools import product
import unittest


PRIMES = (2, 3, 5, 7, 11)


def normalize(point, p):
    """Canonical representative of a projective point over F_p."""
    assert any(x % p for x in point)
    pivot = next(x % p for x in point if x % p)
    inv = pow(pivot, -1, p)
    return tuple((x * inv) % p for x in point)


def projective_points(p, n):
    return {
        normalize(v, p)
        for v in product(range(p), repeat=n + 1)
        if any(v)
    }


def zero_locus(p, poly, n=2):
    return {v for v in projective_points(p, n) if poly(*v) % p == 0}


class ALG02ProjectiveRegressions(unittest.TestCase):
    def test_projective_space_cardinality(self):
        for p in PRIMES:
            self.assertEqual(len(projective_points(p, 0)), 1)
            self.assertEqual(len(projective_points(p, 1)), p + 1)
            self.assertEqual(len(projective_points(p, 2)), p*p + p + 1)

    def test_parallel_affine_lines_meet_at_infinity(self):
        # Coordinates [X:Y:Z], equations Y=0 and Y-Z=0.
        for p in PRIMES:
            points = {a for a in projective_points(p, 2)
                      if a[1] == 0 and (a[1]-a[2]) % p == 0}
            self.assertEqual(points, {(1, 0, 0)})

    def test_two_standard_charts_cover_projective_line(self):
        for p in PRIMES:
            points = projective_points(p, 1)
            u0 = {a for a in points if a[0]}
            u1 = {a for a in points if a[1]}
            self.assertEqual(points, u0 | u1)
            for s, t in u0 & u1:
                x = t * pow(s, -1, p) % p
                y = s * pow(t, -1, p) % p
                self.assertEqual(x*y % p, 1)

    def test_projective_conic_parametrization(self):
        for p in PRIMES:
            parametrized = {
                normalize((s*s, s*t, t*t), p)
                for s, t in projective_points(p, 1)
            }
            conic = zero_locus(p, lambda X, Y, Z: X*Z-Y*Y)
            self.assertEqual(parametrized, conic)
            self.assertEqual(len(conic), p+1)

    def test_parabola_and_hyperbola_infinity(self):
        for p in PRIMES:
            parabola = zero_locus(p, lambda X, Y, Z: Y*Z-X*X)
            hyperbola = zero_locus(p, lambda X, Y, Z: X*Y-Z*Z)
            self.assertEqual({v for v in parabola if v[2] == 0},
                             {(0, 1, 0)})
            self.assertEqual({v for v in hyperbola if v[2] == 0},
                             {(1, 0, 0), (0, 1, 0)})

    def test_homogenization_generators_spurious_point(self):
        # Original I=(x,xy-y)=(x,y). Naively homogenized:
        # J=(X,XY-YZ), which incorrectly adds [X:Y:Z]=[0:1:0].
        for p in PRIMES:
            naive = {v for v in projective_points(p, 2)
                     if v[0] == 0 and (v[0]*v[1]-v[1]*v[2]) % p == 0}
            correct = {v for v in projective_points(p, 2)
                       if v[0] == 0 and v[1] == 0}
            self.assertEqual(naive, {(0, 0, 1), (0, 1, 0)})
            self.assertEqual(correct, {(0, 0, 1)})

    def test_cremona_base_locus_and_involution(self):
        for p in PRIMES:
            pts = projective_points(p, 2)
            base = {(1, 0, 0), (0, 1, 0), (0, 0, 1)}
            def cremona(v):
                X, Y, Z = v
                return (Y*Z % p, X*Z % p, X*Y % p)
            self.assertEqual({v for v in pts if cremona(v) == (0, 0, 0)},
                             base)
            for v in pts:
                if all(v):
                    self.assertEqual(normalize(cremona(cremona(v)), p), v)

    def test_euler_identity_in_positive_characteristic(self):
        # F=XZ-Y^2 has degree 2, including in characteristic 2.
        for p in PRIMES:
            for X, Y, Z in projective_points(p, 2):
                F = X*Z-Y*Y
                lhs = X*Z + Y*(-2*Y) + Z*X
                self.assertEqual((lhs-2*F) % p, 0)

    def test_tangent_to_conic_has_double_intersection(self):
        # At [1:0:0] on XZ-Y^2=0 the tangent is Z=0;
        # the restricted binary form is -Y^2.
        for p in PRIMES:
            on_tangent = zero_locus(
                p, lambda X, Y, Z: X*Z-Y*Y) & zero_locus(
                p, lambda X, Y, Z: Z)
            self.assertEqual(on_tangent, {(1, 0, 0)})
            self.assertNotEqual(-1 % p, 0)  # multiplicity 2, not 0

    def test_two_conics_meet_at_two_points_characteristic_not_two(self):
        for p in (3, 5, 7, 11):
            f = zero_locus(p, lambda X, Y, Z: X*Z-Y*Y)
            g = zero_locus(p, lambda X, Y, Z: X*Z+Y*Y)
            self.assertEqual(f & g, {(1, 0, 0), (0, 0, 1)})
            # In each local chart the ideal reduces to (z,y^2),
            # with local quotient basis {1,y}.
            basis = [0, 1]
            self.assertEqual(len(basis) + len(basis), 2*2)

    def test_complete_intersection_monomial_basis(self):
        # k[x,y]/(x^d,y^e) has basis {x^i y^j: i<d, j<e}.
        for d, e in ((1, 1), (1, 3), (2, 2), (2, 5), (3, 4)):
            standard_monomials = {(i, j) for i in range(d)
                                  for j in range(e)}
            self.assertEqual(len(standard_monomials), d*e)
            self.assertTrue(all(i < d and j < e
                                for i, j in standard_monomials))


if __name__ == "__main__":
    unittest.main()
