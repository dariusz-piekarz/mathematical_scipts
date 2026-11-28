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


    def test_jordan_positive_part_weighted_atoms(self):
        weights=[Q(3),Q(-2),Q(0),Q(5,2)]
        f=[Q(1,2),Q(1),Q(2),Q(3,4)]
        T=lambda g:sum(a*b for a,b in zip(weights,g))
        from itertools import product
        admissible=product(*[(Q(0), x/2, x) for x in f])
        self.assertEqual(max(T(g) for g in admissible),
                         sum(max(w,0)*x for w,x in zip(weights,f)))

    def test_complex_phase_and_modulus_measure(self):
        weights=[3+4j,-2j,0j,-5+0j]
        g=[0.5,1.0,2.0,0.25]
        h=[x*w.conjugate()/abs(w) if w else 0j
           for w,x in zip(weights,g)]
        T=lambda z:sum(w*v for w,v in zip(weights,z))
        expected=sum(abs(w)*x for w,x in zip(weights,g))
        self.assertAlmostEqual(T(h).real, expected)
        self.assertAlmostEqual(T(h).imag, 0)
        self.assertTrue(all(abs(v)<=x+1e-12 for v,x in zip(h,g)))
        self.assertAlmostEqual(sum(abs(w) for w in weights),12)

    def test_radial_projection_does_not_increase_error(self):
        for z in (0j,0.5+0.5j,3+4j,-2j,-2+1j):
            p=z/max(1,abs(z))
            for w in (0j,1j,-1j,1+0j,-1+0j,0.3+0.4j):
                self.assertLessEqual(abs(p-w),abs(z-w)+1e-12)


if __name__=="__main__":
    unittest.main()
