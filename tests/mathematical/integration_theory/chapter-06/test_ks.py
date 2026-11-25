"""Finite regression witnesses for KS formulas; not general proofs."""
from fractions import Fraction as Q
import unittest


class KSChapter06(unittest.TestCase):
    def test_jordan_and_canonical_mass_bound(self):
        # Triples at interior nodes: left limit, point value, right limit.
        g=list(map(Q,[2,5,1,4,0,7,3,-2,6]))
        V=[Q(0)]
        for x,y in zip(g,g[1:]):
            V.append(V[-1]+abs(y-x))
        p=[(v+x-g[0])/2 for x,v in zip(g,V)]
        q=[(v-x+g[0])/2 for x,v in zip(g,V)]
        self.assertTrue(all(x<=y for x,y in zip(p,p[1:])))
        self.assertTrue(all(x<=y for x,y in zip(q,q[1:])))
        self.assertEqual(p[-1]+q[-1],V[-1])
        # Right-continuous cumulative values eliminate point impulses.
        G=[g[i]-g[0] for i in (1,4,7,8)]
        masses=[G[0]]+[y-x for x,y in zip(G,G[1:])]
        self.assertLessEqual(sum(map(abs,masses)),V[-1])
        self.assertEqual(sum(masses),g[-1]-g[0])

    def test_interval_endpoint_conventions(self):
        # u=a, v=b with initial and final jumps and one interior atom.
        ga,gap,gbm,gb=map(Q,[2,5,9,7])
        open_mass=gbm-gap
        left=gap-ga
        right=gb-gbm
        self.assertEqual(open_mass+left+right,gb-ga)
        self.assertEqual(open_mass+left,gbm-ga)
        self.assertEqual(open_mass+right,gb-gap)

    def test_point_impulse_cancellation(self):
        for tag_value in map(Q,[-17,0,5]):
            self.assertEqual(tag_value*(1-0)+tag_value*(0-1),0)

    def test_integration_by_parts_signed_jumps(self):
        for f0 in map(Q,[-3,0,4]):
            fm,fp=Q(2),Q(-5)
            for g0 in map(Q,[-8,1,7]):
                gm,gp=Q(3),Q(6)
                left=f0*(gp-gm)+g0*(fp-fm)
                right=fp*gp-fm*gm+(f0-fm)*(g0-gm)-(fp-f0)*(gp-g0)
                self.assertEqual(left,right)

    def test_chain_error_budget_unbounded_multiplier(self):
        eps=Q(1,10)
        budget=sum(2*k*eps/Q(k*2**(k+2)) for k in range(1,25))
        self.assertLess(budget,eps/2)

    def test_signed_atoms_and_tail(self):
        self.assertEqual(Q(1,3)+3*Q(1,3)**2-2*Q(2,3)**2,-Q(2,9))
        for n in (1,3,10):
            partial=sum(Q(1,2**k)*(1-Q(1,2**k)) for k in range(1,n+1))
            self.assertTrue(0<=Q(2,3)-partial<=Q(1,2**n))


if __name__=="__main__":
    unittest.main()
