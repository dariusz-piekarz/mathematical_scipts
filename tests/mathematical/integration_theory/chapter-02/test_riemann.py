"""IT-02: finite regression witnesses, not general proofs."""
from fractions import Fraction as F
import unittest

class RiemannRegression(unittest.TestCase):
    def test_unbounded_tag_difference(self):
        # f(0)=0, f(x)=1/x for x>0; first cell [0, 1/n].
        for n in (1, 2, 10, 100):
            for m in (3, 10, 100):
                width = F(1, n)
                tag = width / m
                self.assertEqual(width / tag, m)
                self.assertGreater(width / tag, 2)

    def test_l1_truncations_cauchy(self):
        def integral(n):
            return n*F(1, n*n) + 2*(1-F(1, n))
        for n in (1, 2, 3, 10, 100):
            self.assertEqual(integral(n), 2-F(1, n))
            for m in (n, n+1, 2*n):
                difference = integral(m)-integral(n)
                self.assertEqual(difference, F(1, n)-F(1, m))
                self.assertTrue(0 <= difference <= F(1, n))

    def test_null_bad_cells_and_endpoint_overlap(self):
        grid = [F(i, 8) for i in range(9)]
        cells = list(zip(grid, grid[1:]))
        for points in ([], [F(0)], [F(1, 2)], [F(1)], [F(1, 4), F(3, 4)]):
            bad = [(a,b) for a,b in cells if any(a <= x <= b for x in points)]
            self.assertLessEqual(len(bad), 2*len(points))
            self.assertLessEqual(sum((b-a for a,b in bad), F(0)), F(2*len(points),8))
