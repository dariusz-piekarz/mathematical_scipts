"""Independent finite-field regressions for geometric examples in ALG-00.

These small examples support, but do not replace, proofs for arbitrary fields.
"""
import unittest


def add(f, g, p):
    out = dict(f)
    for monomial, coefficient in g.items():
        out[monomial] = (out.get(monomial, 0) + coefficient) % p
    return {m: c % p for m, c in out.items() if c % p}


def multiply(f, g, p):
    out = {}
    for (i, j), a in f.items():
        for (r, s), b in g.items():
            k = (i + r, j + s)
            out[k] = (out.get(k, 0) + a * b) % p
    return {m: c for m, c in out.items() if c}


def substitute_parabola(f, p):
    """Formal substitution y=x^2, returning a univariate polynomial."""
    out = {}
    for (i, j), c in f.items():
        d = i + 2 * j
        out[d] = (out.get(d, 0) + c) % p
    return {i: c for i, c in out.items() if c}


def evaluate(f, x, y, p):
    return sum(c * pow(x, i, p) * pow(y, j, p)
               for (i, j), c in f.items()) % p


class ALG00GeometricExamples(unittest.TestCase):
    def test_parabola_quotient_relation_formally(self):
        for p in (2, 3, 5, 7):
            relation = {(0, 1): 1, (2, 0): -1}
            for a in range(4):
                for b in range(4):
                    g = {(a, b): 1, (1, 0): 2, (0, 0): 3}
                    f = multiply(relation, g, p)
                    self.assertEqual(substitute_parabola(f, p), {})
                    for t in range(p):
                        self.assertEqual(evaluate(f, t, t*t % p, p), 0)

    def test_f2_same_function_not_same_coordinate_ring_element(self):
        h = {(2, 0): 1, (1, 0): -1}
        self.assertTrue(all(evaluate(h, t, t*t, 2) == 0 for t in range(2)))
        self.assertNotEqual(substitute_parabola(h, 2), {})

    def test_axes_union_over_prime_fields(self):
        for p in (2, 3, 5, 7):
            for x in range(p):
                for y in range(p):
                    self.assertEqual((x*y % p == 0), (x == 0 or y == 0))

    def test_axes_intersect_at_origin_only(self):
        for p in (2, 3, 5, 7):
            horizontal = {(x, 0) for x in range(p)}
            vertical = {(0, y) for y in range(p)}
            self.assertEqual(horizontal & vertical, {(0, 0)})
            self.assertEqual(len(horizontal | vertical), 2*p-1)

    def test_double_point_has_nonzero_nilpotent(self):
        # k[t]/(t^2): a+bt, with (a+bt)(c+dt)=ac+(ad+bc)t.
        for p in (2, 3, 5, 7):
            t = (0, 1)
            product = ((t[0]*t[0]) % p,
                       (t[0]*t[1] + t[1]*t[0]) % p)
            self.assertNotEqual(t, (0, 0))
            self.assertEqual(product, (0, 0))

    def test_point_ideal_generators_vanish_at_point(self):
        for p in (2, 3, 5):
            for a in range(p):
                for b in range(p):
                    x_minus_a = {(1, 0): 1, (0, 0): -a}
                    y_minus_b = {(0, 1): 1, (0, 0): -b}
                    g = {(1, 1): 2, (2, 0): 1, (0, 0): 1}
                    h = {(0, 2): 1, (0, 1): 3}
                    f = add(multiply(x_minus_a, g, p),
                            multiply(y_minus_b, h, p), p)
                    self.assertEqual(evaluate(f, a, b, p), 0)


if __name__ == "__main__":
    unittest.main()
