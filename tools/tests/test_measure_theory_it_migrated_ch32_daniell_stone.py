"""Finite regression witnesses for Daniell--Stone constructions with and without a unit."""
from fractions import Fraction as Q
import unittest


class DaniellStone12(unittest.TestCase):
    def test_cover_residual(self):
        u=Q(1)
        h=[Q(1,2**k) for k in range(1,13)]
        residual=[max(u-sum(h[:n]),0) for n in range(1,13)]
        self.assertEqual(residual,[Q(1,2**n) for n in range(1,13)])
        self.assertTrue(all(a>b for a,b in zip(residual,residual[1:])))

    def test_lattice_cutoff_split(self):
        xs=[Q(-1),Q(0),Q(1,3),Q(1),Q(2)]
        h=[Q(2),Q(5),Q(1),Q(3),Q(7)]
        v=[min(1,max(x,0)) for x in xs]
        b=[min(y,7*z) for y,z in zip(h,v)]
        a=[y-z for y,z in zip(h,b)]
        self.assertTrue(all(x>=0 for x in a+b))
        self.assertEqual([x+y for x,y in zip(a,b)],h)
        self.assertEqual(b[:2],[0,0])
        self.assertEqual(a[-2:],[0,0])

    def test_level_ramp_telescoping(self):
        for x in (Q(-1),Q(0),Q(1,7),Q(2)):
            vals=[min(1,n*max(x,0)) for n in range(1,15)]
            diffs=[vals[0]]+[b-a for a,b in zip(vals,vals[1:])]
            self.assertTrue(all(d>=0 for d in diffs))
            self.assertEqual(sum(diffs),int(x>0))

    def test_threshold_bounds_and_exact_ramp_identity(self):
        d=Q(1,4)
        m=8
        for x in [Q(j,24) for j in range(49)]:
            lower=d*sum(x>k*d for k in range(1,m+1))
            upper=d*sum(x>k*d for k in range(m))
            ramps=d*sum(min(1,max(x-k*d,0)/d) for k in range(m))
            self.assertTrue(lower<=x<=upper)
            self.assertLessEqual(upper-lower,d)
            self.assertEqual(ramps,x)

    def test_weighted_representation_squeeze(self):
        xs=[Q(0),Q(1,3),Q(1),Q(5,3)]
        w=[Q(2),Q(1,2),Q(0),Q(4)]
        d=Q(1,5)
        m=10
        integral=lambda f:sum(a*b for a,b in zip(w,f))
        L=[d*sum(x>k*d for k in range(1,m+1)) for x in xs]
        U=[d*sum(x>k*d for k in range(m)) for x in xs]
        self.assertTrue(integral(L)<=integral(xs)<=integral(U))
        self.assertLessEqual(integral(U)-integral(L),d*sum(w))

    def test_dyadic_layers_gap(self):
        for k in range(12):
            self.assertGreater(Q(1,2**(k+1))-Q(1,2**(k+2)),0)

    def test_atomic_weights_no_mass_at_limit(self):
        for n in (1,3,10):
            weights={Q(1,k):Q(1,2**k) for k in range(1,n+1)}
            self.assertEqual(weights.get(Q(0),0),0)
            self.assertEqual(sum(weights.values()),1-Q(1,2**n))

    def test_boundary_evaluation_lacks_order_continuity(self):
        for t in (Q(1),Q(1,5),Q(1,10)):
            seq=[max(1-n*t,0) for n in range(1,15)]
            self.assertEqual(seq[-1],0)
            self.assertEqual(seq,sorted(seq,reverse=True))
        self.assertTrue(all(max(1-n*0,0)==1 for n in range(1,15)))


    def test_split_first_increment_without_unit(self):
        # The zero-level set may have infinite mass in the general proof.
        for delta in (Q(1,3), Q(1,7)):
            m=12
            for j in range(3*m+1):
                x=j*delta/3
                lower=delta*sum(x>k*delta for k in range(1,m+1))
                first=min(x,delta)
                rest=delta*sum(min(1,max(x-k*delta,0)/delta)
                               for k in range(1,m))
                self.assertEqual(first+rest,x)
                self.assertLessEqual(rest,lower)
                self.assertLessEqual(lower,x)

    def test_cover_truncation_l1_error(self):
        w=[Q(2),Q(3),Q(1),Q(4)]
        indicator=[Q(1),Q(0),Q(1),Q(0)]
        hs=[[Q(1,3),Q(1,100),Q(1,2),Q(0)],
            [Q(2,3),Q(0),Q(1,2),Q(1,200)]]
        integral=lambda f:sum(a*b for a,b in zip(w,f))
        total=[sum(row) for row in zip(*hs)]
        v=[min(1,x) for x in total]
        self.assertTrue(all(a<=b<=c for a,b,c in zip(indicator,v,total)))
        error=integral([abs(a-b) for a,b in zip(v,indicator)])
        budget=sum(integral(h) for h in hs)-integral(indicator)
        self.assertLessEqual(error,budget)
        partial=[min(1,x) for x in hs[0]]
        self.assertLessEqual(
            integral([abs(a-b) for a,b in zip(partial,indicator)]),
            integral([a-b for a,b in zip(v,partial)])+error)

    def test_positive_threshold_cover(self):
        h=[Q(0),Q(1,4),Q(2),Q(3)]
        w=[Q(3),Q(1),Q(5),Q(2)]
        ih=sum(a*b for a,b in zip(h,w))
        for t in (Q(1,4),Q(1),Q(2),Q(4)):
            mass=sum(a for a,x in zip(w,h) if x>t)
            self.assertLessEqual(t*mass,ih)


if __name__=="__main__":
    unittest.main()
