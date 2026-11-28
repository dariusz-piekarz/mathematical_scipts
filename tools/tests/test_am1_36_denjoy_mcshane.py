"""AM1-36: finite exact regression checks, not proofs of limit theorems."""
from fractions import Fraction as Q
import unittest


class DenjoyMcShaneTests(unittest.TestCase):
    def test_cantor_gap_oscillation_and_variation(self):
        for r in range(6):
            for n in range(r + 1, 12):
                count = 2**(n-r-1)
                amplitude = Q(1, 2**n)
                self.assertEqual(count * amplitude, Q(1, 2**(r+1)))
                self.assertEqual(2**(n-1) * 2 * amplitude, 1)
                self.assertLess(count * Q(1, 3**n), Q(1, 3**r))

    def test_free_tag_common_refinement(self):
        p = [(Q(0), Q(1,3), Q(3,4)), (Q(1,3), Q(1), Q(0))]
        q = [(Q(0), Q(1,2), Q(1)), (Q(1,2), Q(1), Q(1,4))]
        f = lambda t: 4*t-2
        cells = [(min(v,z)-max(u,w), f(t), f(s))
                 for u,v,t in p for w,z,s in q if min(v,z)>max(u,w)]
        hi = sum(h*max(x,y) for h,x,y in cells)
        lo = sum(h*min(x,y) for h,x,y in cells)
        self.assertEqual(hi-lo, sum(h*abs(x-y) for h,x,y in cells))
        self.assertEqual(sum(h for h,x,y in cells), 1)
        self.assertLessEqual(abs(sum((v-u)*abs(f(t)) for u,v,t in p)
                                 -sum((v-u)*abs(f(t)) for u,v,t in q)), hi-lo)

    def test_product_oscillation_bound(self):
        f = [Q(-3,2), Q(5,3), Q(1,7)]
        g = [Q(4,3), Q(-1,5), Q(7,2)]
        osc = lambda x: max(x)-min(x)
        self.assertLessEqual(osc([x*y for x,y in zip(f,g)]),
                             max(map(abs,f))*osc(g)+max(map(abs,g))*osc(f))


if __name__ == '__main__':
    unittest.main()
