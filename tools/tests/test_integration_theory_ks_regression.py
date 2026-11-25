from fractions import Fraction as Q
import unittest

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

if __name__ == '__main__':
    unittest.main()
