"""AM1-36: exact checks for one-sided jumps and the variation defect."""
import itertools
import unittest
from fractions import Fraction as Q


class VariationDefectTests(unittest.TestCase):
    def test_all_small_signed_jumps(self):
        for left, value, right in itertools.product(range(-3, 4), repeat=3):
            p, q = value-left, right-value
            defect = abs(p)+abs(q)-abs(p+q)
            self.assertGreaterEqual(defect, 0)
            self.assertEqual(defect == 0, min(left, right) <= value <= max(left, right))
            self.assertEqual(defect, 2*min(abs(p), abs(q)) if p*q < 0 else 0)

    def test_piecewise_affine_with_point_values(self):
        # a, a+, c-, c, c+, d-, d, d+, b-, b.
        vals = list(map(Q, [0, 2, 4, 8, 3, 1, -2, 2, 5, 3]))
        total = sum(abs(v-u) for u, v in zip(vals, vals[1:]))
        measure_variation = sum(abs(vals[j]-vals[i]) for i,j in
                                [(0,1),(1,2),(2,4),(4,5),(5,7),(7,8),(8,9)])
        defect = sum(abs(vals[k]-vals[k-1])+abs(vals[k+1]-vals[k])
                     -abs(vals[k+1]-vals[k-1]) for k in [3,6])
        self.assertEqual(total, measure_variation+defect)
        self.assertEqual(defect, 14)


if __name__ == '__main__':
    unittest.main()
