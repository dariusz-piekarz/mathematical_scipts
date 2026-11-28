"""Independent finite CAL regressions retained after migration; not proofs."""
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


class TestKS(unittest.TestCase):
    def test_endpoint_split(self):
        # At c: left/right jumps 2,-1; at x: 3,-4.
        a,c,x,b = Q(0),Q(1,3),Q(2,3),Q(1)
        g = {a:0,c:2,x:4,b:0}
        f = lambda t: 1+t
        local = f(c)*(-1)+f(x)*3
        global_wrong = f(c)*(-1)+f(x)*(-1)
        self.assertEqual(local, Q(11,3))
        self.assertNotEqual(local, global_wrong)
        self.assertEqual(f(c)*2 + local + f(x)*(-4), f(c)*(2-1)+f(x)*(3-4))

    def test_weighted_partial_errors(self):
        # Unbounded multiplier levels, each partial error has its own budget.
        levels = [1,2,10,100,10000]
        e = [Q(1,2**(k+2)*k) for k in levels]
        weighted = sum(k*v for k,v in zip(levels,e))
        self.assertLess(weighted,Q(1,2))

    def test_joint_jumps(self):
        for fm,f0,fp in [(0,1,0),(0,2,3),(2,-1,4)]:
            for gm,g0,gp in [(0,1,0),(0,3,1),(3,-2,5)]:
                self.assertEqual(f0*(gp-gm)+g0*(fp-fm), fp*gp-fm*gm+(f0-fm)*(g0-gm)-(fp-f0)*(gp-g0))


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


class TestPerronCorrection(unittest.TestCase):
    def test_it05_two_sided_gap_envelope(self):
        # Piecewise linear residual on a gap, with two separated maxima.
        R = list(map(Q, [0, 3, 1, 4, 2, 0]))
        L = [max(R[:i+1]) for i in range(len(R))]
        B = [max(R[i:]) for i in range(len(R))]
        K = [l+B[0]-b for l, b in zip(L, B)]
        self.assertEqual(K[-1]-K[0], 2*max(R))
        self.assertTrue(all(a <= b for a,b in zip(K, K[1:])))
        for i,r in enumerate(R):
            self.assertGreaterEqual(K[i]-K[0], r)
            self.assertGreaterEqual(K[-1]-K[i], r)

    def test_it05_boundary_and_signed_secants(self):
        R = list(map(Q, [4, 1, 3, 0]))
        B = [max(R[i:]) for i in range(len(R))]
        K = [B[0]-b for b in B]
        for i,r in enumerate(R):
            self.assertGreaterEqual(K[-1]-K[i], r)
        # At an exceptional tag, |F increment| + |f(tag)| * length
        # is sufficient on either side, even for a negative value of f.
        for dy in (Q(-1,8), Q(1,8)):
            for dF in (Q(-3,5), Q(3,5)):
                for f in (Q(-17), Q(17)):
                    dH = (abs(dF)+abs(f)*abs(dy)) * (1 if dy>0 else -1)
                    self.assertGreaterEqual((dF+dH)/dy, f)
                    self.assertLessEqual((dF-dH)/dy, f)


def tagged_sum(points, tags, f, alpha):
    return sum((f(t) * (alpha(v) - alpha(u))
                for u, v, t in zip(points, points[1:], tags)), Q(0))


class TestRSSubstitution(unittest.TestCase):
    def test_it03_reparametrization_plateau_and_reverse(self):
        points = [Q(i, 8) for i in range(9)]
        tags = [(u + v) / 2 for u, v in zip(points, points[1:])]
        f = lambda x: x*x
        alpha = lambda x: x - 2*int(x >= Q(1, 2))
        phi = lambda t: max(Q(0), 2*t-1)
        image = [(phi(u), phi(v), phi(t))
                 for u,v,t in zip(points, points[1:], tags) if phi(u)!=phi(v)]
        expected = sum((f(t)*(alpha(v)-alpha(u)) for u,v,t in image), Q(0))
        self.assertEqual(tagged_sum(points, tags, lambda t:f(phi(t)),
                                    lambda t:alpha(phi(t))), expected)
        self.assertEqual(tagged_sum(points, tags, lambda t:f(1-t),
                                    lambda t:alpha(1-t)),
                         -tagged_sum(points, tags, f, alpha))

    def test_it03_signed_atom_and_error_bound(self):
        beta = lambda x: x - 2*int(x >= Q(1, 2))
        G = lambda x: x*x/2 - int(x >= Q(1, 2))
        expected = -Q(1, 6)
        for n in (15, 32, 63, 128):
            points = [Q(i, n) for i in range(n+1)]
            for tags in (points[:-1], points[1:],
                         [(u+v)/2 for u,v in zip(points, points[1:])]):
                left = tagged_sum(points, tags, lambda x:x, G)
                right = tagged_sum(points, tags, lambda x:x*x, beta)
                # Var(beta)=3, ||f||=1, omega_g(h)=h.
                self.assertLessEqual(abs(left-right), Q(3,n))
                self.assertLessEqual(abs(right-expected), Q(6,n))
                self.assertLessEqual(abs(left-expected), Q(9,n))

if __name__ == "__main__":
    unittest.main()
