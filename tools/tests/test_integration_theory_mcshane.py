"""Finite checks for IT-07 McShane free tags and common refinement."""
from fractions import Fraction as Q
import unittest


def refine(P, R):
    for a, b, t in P:
        for c, d, s in R:
            length = min(b, d) - max(a, c)
            if length > 0:
                yield length, t, s


class TestMcShane(unittest.TestCase):
    def test_it07_absolute_refinement(self):
        P = [(Q(0), Q(1, 3), Q(3, 4)), (Q(1, 3), Q(1), Q(0))]
        R = [(Q(0), Q(1, 2), Q(1)), (Q(1, 2), Q(1), Q(1, 4))]
        f = lambda t: 4*t-2
        cells = list(refine(P, R))
        hi = sum(length*max(f(t), f(s)) for length,t,s in cells)
        lo = sum(length*min(f(t), f(s)) for length,t,s in cells)
        abs_P = sum((b-a)*abs(f(t)) for a,b,t in P)
        abs_R = sum((b-a)*abs(f(t)) for a,b,t in R)
        self.assertEqual(sum(length for length,t,s in cells), 1)
        self.assertEqual(hi-lo, sum(length*abs(f(t)-f(s)) for length,t,s in cells))
        self.assertLessEqual(abs(abs_P-abs_R), hi-lo)

    def test_it07_indicator_sandwich(self):
        # K=[1/4,3/4], O=(1/8,7/8), E=[1/5,4/5].
        E = lambda t: Q(1,5) <= t <= Q(4,5)
        P = [(Q(0),Q(1,5),Q(0)), (Q(1,5),Q(4,5),Q(1,2)),
             (Q(4,5),Q(1),Q(1))]
        for a,b,t in P:
            if E(t):
                self.assertTrue(Q(1,8)<a<=b<Q(7,8))
            else:
                self.assertTrue(b<Q(1,4) or a>Q(3,4))
        S = sum(b-a for a,b,t in P if E(t))
        self.assertTrue(Q(1,2)<=S<=Q(3,4))
        self.assertEqual(S,Q(3,5))


if __name__ == '__main__':
    unittest.main()
