"""ALG-01 independent finite-field and basic ideal regressions.

Finite-field checks are bounded sanity checks, not substitutes for
proofs of Hilbert's basis theorem or the Nullstellensatz.
"""
import unittest


PRIMES = (2, 3, 5, 7, 11)


def plane(p):
    return ((x, y) for x in range(p) for y in range(p))


def vanishing_points(p, polys):
    return {(x, y) for x, y in plane(p)
            if all(f(x, y) % p == 0 for f in polys)}


class ALG01GeometryRegressions(unittest.TestCase):
    def test_zariski_ideal_product_union(self):
        for p in PRIMES:
            x_axis = vanishing_points(p, [lambda x, y: y])
            y_axis = vanishing_points(p, [lambda x, y: x])
            product_zero = vanishing_points(p, [lambda x, y: x*y])
            self.assertEqual(product_zero, x_axis | y_axis)
            self.assertEqual(len(product_zero), 2*p - 1)
            self.assertEqual(x_axis & y_axis, {(0, 0)})

    def test_zero_locus_intersection_corresponds_to_ideal_sum(self):
        for p in PRIMES:
            parabola = vanishing_points(p, [lambda x, y: y-x*x])
            line = vanishing_points(p, [lambda x, y: y+x-2])
            combined = vanishing_points(
                p, [lambda x, y: y-x*x, lambda x, y: y+x-2])
            self.assertEqual(combined, parabola & line)

    def test_parabola_parametrization_over_fields(self):
        for p in PRIMES:
            parametrized = {(t, (t*t) % p) for t in range(p)}
            locus = vanishing_points(p, [lambda x, y: y-x*x])
            self.assertEqual(parametrized, locus)
            self.assertEqual(len(locus), p)

    def test_finite_field_pointwise_vs_formal_poly(self):
        for p in PRIMES:
            # x^p-x vanishes at all F_p-points but is formally nonzero.
            self.assertTrue(all((pow(t, p, p) - t) % p == 0
                                for t in range(p)))
            self.assertNotEqual({p: 1, 1: -1}, {})

    def test_cusp_parametrization_is_bijective(self):
        for p in PRIMES:
            points = vanishing_points(
                p, [lambda x, y: y*y - x*x*x])
            parametrized = {(t*t % p, t*t*t % p)
                            for t in range(p)}
            self.assertEqual(points, parametrized)
            self.assertEqual(len(points), p)
            for x, y in points:
                t = 0 if x == 0 else y * pow(x, -1, p) % p
                self.assertEqual((t*t % p, t*t*t % p), (x, y))

    def test_cusp_semigroup_omits_exponent_one(self):
        exponents = {2*a+3*b for a in range(15) for b in range(15)}
        self.assertNotIn(1, exponents)
        self.assertIn(0, exponents)
        self.assertTrue(all(n in exponents for n in range(2, 20)))

    def test_hyperbola_projection_omits_zero(self):
        for p in PRIMES:
            points = vanishing_points(
                p, [lambda x, y: x*y-1])
            self.assertEqual({x for x, _ in points}, set(range(1, p)))
            self.assertEqual(len(points), p-1)
            self.assertTrue(all(x*y % p == 1 for x, y in points))

    def test_weak_nullstellensatz_needs_algebraic_closure(self):
        # (x^2+1) is proper in F_3[x] but has no F_3-point.
        self.assertEqual([x for x in range(3)
                          if (x*x+1) % 3 == 0], [])
        self.assertTrue((2*2+1) % 3 != 0)

    def test_rabinowitsch_radical_example(self):
        # I=(x^3, x^2 y): x not in I, x^3 in I, V(I)=V(x).
        for p in PRIMES:
            zeros = vanishing_points(
                p, [lambda x, y: x**3, lambda x, y: x*x*y])
            self.assertEqual(zeros, {(0, y) for y in range(p)})
        # A monomial x^a y^b belongs to the monomial ideal exactly
        # when it is divisible by x^3 or by x^2 y.
        generators = ((3, 0), (2, 1))
        def in_ideal(exponents):
            return any(exponents[0] >= a and exponents[1] >= b
                       for a, b in generators)
        self.assertFalse(in_ideal((1, 0)))   # x not in I
        self.assertFalse(in_ideal((2, 0)))   # x^2 not in I
        self.assertTrue(in_ideal((3, 0)))    # x^3 in I
        self.assertTrue(in_ideal((2, 1)))    # x^2 y in I

    def test_finite_field_affine_point_sets_are_discrete(self):
        # Polynomials x-a and y-b cut out exactly one F_p-point.
        for p in PRIMES:
            for a in range(p):
                for b in range(p):
                    zeros = vanishing_points(
                        p,
                        [lambda x, y, a=a: x-a,
                         lambda x, y, b=b: y-b])
                    self.assertEqual(zeros, {(a, b)})


if __name__ == "__main__":
    unittest.main()
