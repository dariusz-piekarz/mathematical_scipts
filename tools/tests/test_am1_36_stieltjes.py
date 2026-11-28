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


    def test_am136_reverse_orientation(self):
        # Arbitrary discontinuous integrator values at tagged cells.
        points = [Q(0), Q(1, 3), Q(2, 3), Q(1)]
        tags = [Q(1, 6), Q(1, 2), Q(5, 6)]
        g = lambda t: t*t + 2*(t >= Q(1, 3))
        f = lambda t: 3*t-1
        direct = sum(f(t)*(g(v)-g(u))
                     for u,v,t in zip(points, points[1:], tags))
        phi = lambda s: 1-s
        rev_points = [phi(x) for x in reversed(points)]
        rev_tags = [phi(t) for t in reversed(tags)]
        reverse = sum(f(phi(t))*(g(phi(v))-g(phi(u)))
                      for u,v,t in zip(rev_points, rev_points[1:], rev_tags))
        self.assertEqual(reverse, -direct)

    def test_am136_cantor_moments(self):
        for n in range(1, 15):
            mean = sum(Q(1, 3**k) for k in range(1, n+1))
            variance = sum(Q(1, 9**k) for k in range(1, n+1))
            self.assertEqual(mean + Q(1, 2*3**n), Q(1, 2))
            self.assertEqual(variance + Q(1, 8*9**n) + Q(1, 4), Q(3, 8))


if __name__ == '__main__':
    unittest.main()
