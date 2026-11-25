"""AM1-36: finite exact regressions for Stieltjes endpoint conventions."""
from fractions import Fraction as Q
import unittest


class StieltjesTests(unittest.TestCase):
    def test_am136_rs_common_jump(self):
        c = Q(1, 2)
        for n in range(3, 15):
            u, v = c-Q(1, 2**n), c+Q(1, 2**n)
            alpha = lambda t: int(t >= c)
            f = lambda t: int(t > c)
            self.assertEqual(f(u)*(alpha(v)-alpha(u)), 0)
            self.assertEqual(f(v)*(alpha(v)-alpha(u)), 1)

    def test_am136_ks_signed_endpoint_masses(self):
        # Values at a, a+, c-, c, c+, b-, b.
        g = [Q(0), Q(2), Q(2), Q(5), Q(1), Q(1), Q(4)]
        jumps = [g[1]-g[0], g[4]-g[2], g[6]-g[5]]
        self.assertEqual(jumps, [2, -1, 3])
        self.assertEqual(sum(jumps), g[-1]-g[0])
        variation = sum(abs(v-u) for u,v in zip(g,g[1:]))
        self.assertLessEqual(sum(map(abs, jumps)), variation)
        self.assertEqual(sum(Q(k)*m for k,m in zip([1,2,3],jumps)), 9)

    def test_am136_ks_common_jump_correction(self):
        fm, f0, fp = Q(1), Q(4), Q(2)
        gm, g0, gp = Q(-2), Q(5), Q(3)
        integrals = f0*(gp-gm)+g0*(fp-fm)
        correction = (f0-fm)*(g0-gm)-(fp-f0)*(gp-g0)
        self.assertEqual(integrals, fp*gp-fm*gm+correction)


if __name__ == '__main__':
    unittest.main()
