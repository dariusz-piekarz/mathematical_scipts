"""IT-08/09: exact finite regressions; not a proof of infinite statements."""
from fractions import Fraction as Q
import unittest


def cantor_intervals(n):
    intervals = [(Q(0), Q(1))]
    for _ in range(n):
        intervals = [(u, u+(v-u)/3) for u,v in intervals] + [(v-(v-u)/3,v) for u,v in intervals]
    return sorted(intervals)


class TestDenjoy(unittest.TestCase):
    def test_it09_local_cantor_oscillation(self):
        for r in range(5):
            for n in range(r+1, 9):
                for a,b in cantor_intervals(r):
                    gaps = [(u+(v-u)/3,v-(v-u)/3) for u,v in cantor_intervals(n-1) if a<=u<v<=b]
                    self.assertEqual(len(gaps), 2**(n-r-1))
                    self.assertEqual(sum(v-u for u,v in gaps), Q(2**(n-r-1),3**n))
                    self.assertEqual(len(gaps)*Q(1,2**n),Q(1,2**(r+1)))
                    self.assertTrue(all(v<=w for (u,v),(w,z) in zip(gaps,gaps[1:])))

    def test_it09_level_variation(self):
        for n in range(1,15):
            amplitude=Q(1,2**n)
            self.assertEqual(2**(n-1)*2*amplitude,1)

    def test_it08_product_oscillation(self):
        F=[Q(-3,2),Q(5,3),Q(1,7)]
        G=[Q(4,3),Q(-1,5),Q(7,2)]
        osc=lambda s:max(s)-min(s)
        self.assertLessEqual(osc([x*y for x,y in zip(F,G)]),max(map(abs,F))*osc(G)+max(map(abs,G))*osc(F))


if __name__ == '__main__':
    unittest.main()
