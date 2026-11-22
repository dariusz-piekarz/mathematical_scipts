"""ALG-03 regressions: singular points, normalization, blowups and genus.

Finite-field examples independently check formulas, not general theorems.
"""
from itertools import product
from math import comb
import unittest

PRIMES = (2, 3, 5, 7, 11, 13)


def order(coefficients, p):
    """Least total degree with a nonzero coefficient; zero has no order."""
    degrees = [a + b for (a, b), c in coefficients.items() if c % p]
    return min(degrees) if degrees else None


class ALG03Regressions(unittest.TestCase):
    def test_order_zero_and_multiplication_by_unit(self):
        for p in PRIMES:
            self.assertEqual(order({(0, 0): 1, (1, 0): 1}, p), 0)
            self.assertEqual(order({(0, 2): 1, (3, 0): -1}, p), 2)
            # (1+x)(y^2-x^3), including positive characteristic.
            prod = {(0, 2): 1, (1, 2): 1, (3, 0): -1, (4, 0): -1}
            self.assertEqual(order(prod, p), 2)

    def test_cusp_normalization_and_tangent(self):
        for p in PRIMES:
            values = [(t*t % p, t*t*t % p) for t in range(p)]
            self.assertEqual(len(set(values)), p)
            self.assertTrue(all((y*y - x*x*x) % p == 0
                                for x, y in values))
            # Initial form y^2 has only one geometric tangent y=0.
            self.assertEqual({(x, y) for x, y in product(range(p), repeat=2)
                              if y*y % p == 0}, {(x, 0) for x in range(p)})

    def test_node_normalization_two_branches(self):
        for p in PRIMES:
            if p == 2:
                continue
            fibers = {}
            for t in range(p):
                x = (t*t - 1) % p
                y = (t*x) % p
                self.assertEqual((y*y-x*x*(x+1)) % p, 0)
                fibers.setdefault((x, y), []).append(t)
            self.assertEqual(sorted(fibers[(0, 0)]), [1, p-1])
            self.assertTrue(all(len(params) == 1
                                for point, params in fibers.items()
                                if point != (0, 0)))

    def test_tangent_cone_of_node(self):
        for p in PRIMES:
            if p == 2:
                continue
            points = {(x, y) for x, y in product(range(p), repeat=2)
                      if (y*y-x*x) % p == 0}
            expected = {(x, (eps*x) % p)
                        for x in range(p) for eps in (-1, 1)}
            self.assertEqual(points, expected)

    def test_blowup_cusp_transform_and_smoothness(self):
        for p in PRIMES:
            for u, v in product(range(p), repeat=2):
                self.assertEqual(
                    ((u*v)**2-u**3) % p, (u*u*(v*v-u)) % p)
            self.assertEqual({(u, v) for u, v in product(range(p), repeat=2)
                              if u == 0 and (v*v-u) % p == 0}, {(0, 0)})
            self.assertNotEqual((-1) % p, 0)

    def test_blowup_node_separated_transverse_points(self):
        for p in PRIMES:
            if p == 2:
                continue
            points = {(0, v) for v in range(p) if (v*v-1) % p == 0}
            self.assertEqual(points, {(0, 1), (0, p-1)})
            self.assertTrue(all(2*v % p for _, v in points))
            for u, v in product(range(p), repeat=2):
                self.assertEqual(
                    ((u*v)**2-u*u*(u+1)) % p,
                    (u*u*(v*v-u-1)) % p)

    def test_plane_curve_arithmetic_genus(self):
        for degree in range(1, 9):
            genus = (degree-1)*(degree-2)//2
            for m in range(degree, degree+8):
                self.assertEqual(
                    comb(m+2, 2) - comb(m-degree+2, 2),
                    degree*m+1-genus)
        self.assertEqual((1-1)*(1-2)//2, 0)
        self.assertEqual((3-1)*(3-2)//2, 1)

    def test_local_cusp_intersection_orders(self):
        # Restrict y^2-x^3 to tangent y=0 -> -x^3 (order 3).
        # Restrict to x=0 -> y^2 (order 2).
        for p in PRIMES:
            self.assertEqual(order({(3, 0): -1}, p), 3)
            self.assertEqual(order({(0, 2): 1}, p), 2)


if __name__ == "__main__":
    unittest.main()
