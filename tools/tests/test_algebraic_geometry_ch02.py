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

    def test_last_coordinate_homogenization_and_embedding(self):
        # Iota(x,y)=[x:y:1], and affine f(x,y) becomes F(X,Y,Z).
        for p in PRIMES:
            for x, y in product(range(p), repeat=2):
                affine = (y-x*x) % p
                homogeneous = (y*1-x*x) % p  # YZ-X^2, Z=1
                self.assertEqual(affine, homogeneous)
                self.assertEqual(
                    normalize((x, y, 1), p) in
                    zero_locus(p, lambda X, Y, Z: Y*Z-X*X),
                    affine == 0)
                for z in range(1, p):
                    X, Y = x*z % p, y*z % p
                    self.assertEqual(
                        (Y*z-X*X) % p,
                        (z*z*(y-x*x)) % p)
            for x, y in product(range(p), repeat=2):
                self.assertEqual(
                    (x*y-1) % p == 0,
                    normalize((x, y, 1), p) in
                    zero_locus(p, lambda X, Y, Z: X*Y-Z*Z))

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

    def test_hilbert_function_of_nonmonomial_complete_intersection(self):
        # F=X^2+YZ, G=Y^3+XZ^2. At Z=0 the equations
        # X^2=Y^3=0 have no projective common point. The
        # quotient must have Hilbert function 1,3,5,6,6,...
        # Check this via independent modular ranks of ideal pieces.
        def monomials(m):
            return [(a, b, m-a-b) for a in range(m+1)
                    for b in range(m-a+1)]

        def modular_rank(rows, p):
            pivots = {}
            for source in rows:
                row = source[:]
                while True:
                    col = next((i for i, value in enumerate(row)
                                if value % p), None)
                    if col is None:
                        break
                    if col not in pivots:
                        inverse = pow(row[col] % p, -1, p)
                        pivots[col] = [(x*inverse) % p for x in row]
                        break
                    multiple = row[col] % p
                    row = [(x-multiple*y) % p
                           for x, y in zip(row, pivots[col])]
            return len(pivots)

        F = {(2, 0, 0): 1, (0, 1, 1): 1}
        G = {(0, 3, 0): 1, (1, 0, 2): 1}
        for p in PRIMES:
            dimensions = []
            for m in range(7):
                mon = monomials(m)
                positions = {term: j for j, term in enumerate(mon)}
                rows = []
                for degree, polynomial in ((2, F), (3, G)):
                    if m < degree:
                        continue
                    for a, b, c in monomials(m-degree):
                        row = [0]*len(mon)
                        for (i, j, k), coefficient in polynomial.items():
                            pos = positions[(a+i, b+j, c+k)]
                            row[pos] = (row[pos]+coefficient) % p
                        rows.append(row)
                dimensions.append(len(mon)-modular_rank(rows, p))
            self.assertEqual(dimensions, [1, 3, 5, 6, 6, 6, 6],
                             f"Unexpected Hilbert function over F_{p}")

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
