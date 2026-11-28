"""Finite regression witnesses for Jordan, Stieltjes and Hausdorff formulas."""
from fractions import Fraction as Q
import unittest


class MeasuresChapter10(unittest.TestCase):
    def test_half_open_stieltjes_telescoping(self):
        # Right-continuous step function, with atoms at -1, 0, 1.
        alpha=lambda x: sum(w for c,w in ((-1,2),(0,3),(1,5)) if c<=x)
        xs=[Q(-2),Q(-1),Q(0),Q(1),Q(2)]
        masses=[alpha(v)-alpha(u) for u,v in zip(xs,xs[1:])]
        self.assertEqual(masses,[2,3,5,0])
        self.assertEqual(sum(masses),alpha(xs[-1])-alpha(xs[0]))
        # In particular (a,b] excludes a, but includes b.
        self.assertEqual(alpha(1)-alpha(0),5)

    def test_initial_atom_vs_right_continuous_replacement(self):
        a,b=Q(0),Q(1)
        g=lambda x:int(x>a)
        h=lambda x:1
        f=lambda x:7-2*x
        self.assertEqual(f(a)*(g(b)-g(a)),7)
        self.assertEqual(h(b)-h(a),0)
        self.assertEqual(f(b),5)

    def test_density_and_atomic_signed_integral(self):
        values=[Q(-2),Q(3),Q(-1)]
        weights=[Q(1,2),Q(1,4),Q(1,4)]
        signed=sum(v*w for v,w in zip(values,weights))
        absolute=sum(abs(v)*w for v,w in zip(values,weights))
        positive=sum(max(v,0)*w for v,w in zip(values,weights))
        negative=sum(max(-v,0)*w for v,w in zip(values,weights))
        self.assertEqual(signed,positive-negative)
        self.assertEqual(absolute,positive+negative)
        self.assertLessEqual(abs(signed),absolute)

    def test_cantor_moments(self):
        # Truncated random ternary series with independent digits 0,2.
        for n in range(1,9):
            xs=[Q(0)]
            for k in range(1,n+1):
                xs=[x+Q(b,3**k) for x in xs for b in (0,2)]
            mean=sum(xs)/len(xs)
            second=sum(x*x for x in xs)/len(xs)
            self.assertEqual(mean,(1-Q(1,3**n))/2)
            self.assertEqual(second-mean**2,(1-Q(1,9**n))/8)
            self.assertLess(second,Q(3,8))

    def test_cantor_cylinder_mass_and_separation(self):
        intervals=[(Q(0),Q(1))]
        for n in range(1,9):
            intervals=[pair for u,v in intervals
                       for pair in ((u,u+(v-u)/3),(v-(v-u)/3,v))]
            ell=Q(1,3**n)
            self.assertEqual(len(intervals),2**n)
            self.assertTrue(all(v-u==ell for u,v in intervals))
            self.assertTrue(all(s-v>=ell for (_,v),(s,_) in zip(intervals,intervals[1:])))
            self.assertEqual(sum(v-u for u,v in intervals),Q(2,3)**n)
            self.assertEqual(len(intervals)*Q(1,2**n),1)

    def test_hausdorff_open_interval_budget(self):
        # Diameter-zero pieces may still be covered with positive radii.
        diameters=[Q(0),Q(1,4),Q(0),Q(1,7)]
        eps=Q(1,100)
        lengths=[d+eps/Q(2**j) for j,d in enumerate(diameters,1)]
        self.assertTrue(all(l>d for l,d in zip(lengths,diameters)))
        self.assertLess(sum(lengths),sum(diameters)+eps)

    def test_jordan_elementary_length_and_boundary(self):
        # Finite interval approximations to [0,1], with one point omitted.
        for n in range(2,20):
            E=Q(1,2)-Q(1,2*n)+Q(1,2)-Q(1,2*n)
            H=Q(1)
            self.assertEqual(H-E,Q(1,n))
            self.assertGreaterEqual(E,0)


# Preserve the independent historical IT-10 exact arithmetic regressions.
class TestIntegrationMeasures(unittest.TestCase):
    def test_stieltjes_atom_and_telescoping(self):
        # Right-continuous alpha(x)=x+2*chi_[1/2,infty)(x).
        alpha = lambda x: x + 2 * (x >= Q(1, 2))
        points = [Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)]
        masses = [alpha(v)-alpha(u) for u,v in zip(points,points[1:])]
        self.assertEqual(sum(masses), 3)
        self.assertEqual(masses[1], Q(9, 4))
        for n in range(2, 20):
            self.assertEqual(alpha(Q(1,2))-alpha(Q(1,2)-Q(1,2**n)), 2+Q(1,2**n))

    def test_cantor_cylinder_mass(self):
        for n in range(1, 10):
            self.assertEqual(2**n * Q(1,2**n), 1)
            self.assertEqual(Q(1,2**n), 2 * Q(1,2**(n+1)))

    def test_cantor_moments(self):
        # Independent digits, finite partial sums and exact limiting tails.
        for n in range(1, 10):
            mean = sum(Q(1,3**k) for k in range(1,n+1))
            variance = sum(Q(1,9**k) for k in range(1,n+1))
            self.assertEqual(mean + Q(1,2*3**n), Q(1,2))
            self.assertEqual(variance + Q(1,8*9**n), Q(1,8))
            self.assertEqual((mean + Q(1,2*3**n))**2 + variance + Q(1,8*9**n), Q(3,8))

if __name__=="__main__":
    unittest.main()
