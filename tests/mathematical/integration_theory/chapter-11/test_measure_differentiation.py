"""Finite regression witnesses for differentiation estimates."""
from fractions import Fraction as Q
import unittest


class MeasureDifferentiation11(unittest.TestCase):
    def test_five_radius_bound(self):
        for r in (Q(1),Q(2),Q(7,3)):
            s=r/2+Q(1,100)
            self.assertLess(2*r+s,5*s)

    def test_ball_boundary_annulus(self):
        for d in (1,2,3,5):
            r=Q(2)
            volumes=[(r+Q(1,n))**d-(r-Q(1,n))**d for n in (2,10,100)]
            self.assertGreater(volumes[0],volumes[1])
            self.assertGreater(volumes[1],volumes[2])

    def test_one_sided_oscillation_bound(self):
        # f(t)=t, x=0; exact average absolute deviations.
        for h in (Q(1,2),Q(1,10),Q(1,100)):
            one=h*h/2/h
            symmetric=h*h/(2*h)
            self.assertLessEqual(one,2*symmetric)
            self.assertEqual(one,symmetric)

    def test_symmetric_mean_not_lebesgue_point(self):
        # sign function on symmetric intervals, value zero at origin.
        for r in (Q(1),Q(1,3),Q(1,100)):
            self.assertEqual((r-r)/(2*r),0)
            self.assertEqual((r+r)/(2*r),1)

    def test_signed_cdf_increment_orientation(self):
        # Absolutely continuous component F(x)=x**2 on [0,1].
        x=Q(1,2)
        for h in (Q(1,100),-Q(1,100),Q(1,1000)):
            q=((x+h)**2-x*x)/h
            self.assertEqual(q,2*x+h)

    def test_jordan_variation_decomposition(self):
        values=[Q(0),Q(3),Q(-2),Q(1)]
        V=[Q(0)]
        for a,b in zip(values,values[1:]):
            V.append(V[-1]+abs(b-a))
        p=[(v+f-values[0])/2 for v,f in zip(V,values)]
        q=[(v-f+values[0])/2 for v,f in zip(V,values)]
        self.assertEqual(p,sorted(p))
        self.assertEqual(q,sorted(q))
        self.assertEqual([a-b for a,b in zip(p,q)],values)


if __name__=="__main__":
    unittest.main()
