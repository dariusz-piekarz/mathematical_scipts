"""AM1-36: exact finite checks for first crossings and multiplier sums."""
from fractions import Fraction as Q
import unittest


class TestOrderAndMultiplier(unittest.TestCase):
    def test_first_downward_crossing(self):
        # Piecewise affine F on vertices 0,1,2,3,4.
        values = [Q(4), Q(5), Q(1), Q(3), Q(0)]
        for level in [Q(k, 4) for k in range(1, 16)]:
            i = next(i for i in range(4)
                     if values[i] > level >= values[i+1])
            slope = values[i+1]-values[i]
            x = Q(i)+(level-values[i])/slope
            self.assertLess(slope, 0)
            self.assertEqual(values[i]+slope*(x-i), level)
            self.assertTrue(all(v > level for v in values[:i+1]))

    def test_tagged_multiplier_error_and_summation(self):
        xs = [Q(0), Q(1, 3), Q(2, 3), Q(1)]
        tags = [Q(1, 6), Q(1, 2), Q(5, 6)]
        F = lambda x: x*x
        g = lambda x: 2*x-3*(x >= Q(1, 2))
        dF = [F(v)-F(u) for u,v in zip(xs,xs[1:])]
        tagged = sum(g(t)*d for t,d in zip(tags,dF))
        left = sum(g(u)*d for u,d in zip(xs,dF))
        variation_bound = Q(5)
        modulus_bound = Q(2, 3)
        self.assertLessEqual(abs(tagged-left), modulus_bound*variation_bound)
        right = sum(F(v)*(g(v)-g(u)) for u,v in zip(xs,xs[1:]))
        self.assertEqual(left+right, F(1)*g(1)-F(0)*g(0))


if __name__ == '__main__':
    unittest.main()
