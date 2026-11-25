"""Finite witnesses for the general locally compact Hausdorff Riesz proof."""
from fractions import Fraction as Q
import unittest


class RieszRepresentation13(unittest.TestCase):
    def test_partition_with_repeated_indices(self):
        f=Q(3,4)
        psi=[Q(1),Q(1,2),Q(1)]
        indices=[0,0,1]
        parts=[f*p/sum(psi) for p in psi]
        grouped=[sum(p for p,j in zip(parts,indices) if j==k) for k in (0,1)]
        self.assertEqual(sum(grouped),f)
        self.assertTrue(all(0<=g<=f for g in grouped))

    def test_open_separation_inequality(self):
        # Finite discrete model: every subset is open and compact.
        w=[Q(1),Q(0),Q(4),Q(2),Q(1,3)]
        mass=lambda a:sum(w[i] for i in a)
        E={0,2,4}
        U={0,1,2}
        W={0,1,2,4}
        H={0,2}
        V=H
        self.assertLessEqual(H,W&U)
        self.assertLessEqual(E-U,W-V)
        self.assertEqual(mass(V)+mass(W-V),mass(W))
        self.assertGreaterEqual(mass(W),mass(H)+mass(E-U))

    def test_threshold_bounds_and_local_cutoff(self):
        for n in (1,3,8):
            d=Q(2,n)
            for x in (Q(0),Q(1,5),d,Q(1),Q(2)):
                lower=d*sum(x>i*d for i in range(1,n+1))
                upper=d*sum(x>i*d for i in range(n))
                full=d*sum(x>=(i+1)*d for i in range(n))
                self.assertTrue(lower<=x<=upper)
                self.assertLessEqual(upper-lower,d)
                self.assertLessEqual(x,d+full)

    def test_local_error_budget(self):
        mass=Q(7,3)
        local_bound=Q(4)
        for N in (1,10,100):
            d=Q(2,N)
            self.assertEqual(d*(mass+local_bound),Q(38,3*N))

    def test_disjoint_open_superadditivity_finite_model(self):
        weights=[Q(1),Q(5),Q(2)]
        f=[Q(1),Q(0),Q(0)]
        g=[Q(0),Q(1,2),Q(1)]
        h=[a+b for a,b in zip(f,g)]
        I=lambda v:sum(w*x for w,x in zip(weights,v))
        self.assertTrue(all(0<=x<=1 for x in h))
        self.assertEqual(I(h),I(f)+I(g))

    def test_compact_support_zero_extension(self):
        psi=[Q(0),Q(2),Q(1),Q(0)]
        f=[Q(0),Q(3,4),Q(1),Q(0)]
        part=[v*p/p if p else 0 for v,p in zip(f,psi)]
        self.assertEqual(part,f)


if __name__=="__main__":
    unittest.main()
