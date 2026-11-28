"""Finite regression witnesses for Alexiewicz and endpoint criteria."""
from fractions import Fraction as Q
import math
import unittest


class HKComparisons11(unittest.TestCase):
    def test_piecewise_linear_primitive(self):
        xs=[Q(0),Q(1,3),Q(3,4),Q(1)]
        ys=[Q(0),Q(2),Q(-1),Q(3)]
        slopes=[(v-u)/(b-a) for a,b,u,v in zip(xs,xs[1:],ys,ys[1:])]
        for k in range(1,len(xs)):
            self.assertEqual(sum(s*(b-a) for s,a,b in zip(slopes[:k],xs[:k],xs[1:k+1])),ys[k])

    def test_interpolation_uniform_budget(self):
        u,v,x=Q(2),Q(3),Q(5,2)
        for theta in (Q(0),Q(1,3),Q(1)):
            self.assertLessEqual(abs((1-theta)*u+theta*v-x),
                                 (1-theta)*abs(u-x)+theta*abs(v-x))

    def test_alexiewicz_bounded_by_l1(self):
        increments=[Q(1),Q(-2),Q(3),Q(-1,2)]
        partial=[sum(increments[:k]) for k in range(len(increments)+1)]
        self.assertLessEqual(max(map(abs,partial)),sum(map(abs,increments)))

    def test_monotone_truncation_mass(self):
        for n in (1,2,10,100):
            self.assertAlmostEqual(1+math.log(n),n*(1/n)+math.log(n))

    def test_oscillatory_obstruction_at_threshold(self):
        for k in (1,10,100):
            a=2*k*math.pi+math.pi/6
            b=2*k*math.pi+5*math.pi/6
            self.assertAlmostEqual((b-a)/2,math.pi/3)
            self.assertGreaterEqual(a,1)

    def test_removed_interval_budget(self):
        for n in (1,3,10):
            removed=sum(Q(1,2**(j+2)) for j in range(1,n+1))
            self.assertLess(removed,Q(1,4))
            self.assertGreater(1-removed,Q(3,4))


if __name__=="__main__":
    unittest.main()
