"""AM1-36: finite atomic checks for KS order and truncation estimates."""
from fractions import Fraction as Q
import unittest


class KSOrderTests(unittest.TestCase):
    def test_nonnegative_truncations(self):
        masses = [Q(1, 3), Q(0), Q(2, 3), Q(1, 4)]
        values = [Q(7, 2), Q(100), Q(3, 2), Q(4)]
        integral = sum(m*v for m, v in zip(masses, values))
        truncations = [sum(m*min(v, n) for m, v in zip(masses, values))
                       for n in range(1, 6)]
        self.assertEqual(truncations, sorted(truncations))
        self.assertTrue(all(x <= integral for x in truncations))
        self.assertEqual(truncations[-1], integral)

    def test_two_sided_bounds_and_null_atom(self):
        masses = [Q(2), Q(0), Q(1, 2)]
        lower = [Q(-3), Q(-1000), Q(5)]
        upper = [Q(1), Q(1000), Q(8)]
        limit = [Q(-1), Q(42), Q(6)]
        integral = lambda v: sum(m*x for m, x in zip(masses, v))
        for n in range(1, 10):
            vals = [x+(y-x)/n for x,y in zip(limit,upper)]
            self.assertLessEqual(integral(lower), integral(vals))
            self.assertLessEqual(integral(vals), integral(upper))
            self.assertEqual(integral(vals)-integral(limit), Q(5, 1)/n)
        self.assertEqual(integral(limit), integral([limit[0], Q(-999), limit[2]]))


if __name__ == '__main__':
    unittest.main()
