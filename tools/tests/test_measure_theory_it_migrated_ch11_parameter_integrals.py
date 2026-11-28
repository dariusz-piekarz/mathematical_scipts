"""Finite regression witnesses for parameter integrals; not general proofs."""
from fractions import Fraction as Q
import math
import unittest


class ParameterIntegrals11(unittest.TestCase):
    def test_escape_of_mass_on_fixed_interval(self):
        for n in (2,10,100):
            t=Q(1,n)
            self.assertEqual(t*(1/t),1)
            self.assertEqual(t*min(Q(2),1/t),Q(2,n))

    def test_smooth_parameter_counterexample(self):
        for t in (0.5,-0.5,0.1,-0.1):
            x=3.0
            self.assertLessEqual(abs(t*math.exp(-t*t*x)),abs(t))
            self.assertAlmostEqual(t*t/(t*t),1.0)

    def test_complex_mean_value_projection(self):
        z=complex(3,4)
        u=z/abs(z)
        self.assertAlmostEqual((u.conjugate()*z).real,abs(z))
        self.assertLessEqual(abs(z.real),abs(z))

    def test_uniform_error_bound(self):
        weights=[Q(1,2),Q(3),Q(2)]
        h=[Q(1,3),Q(1,5),Q(1,7)]
        for t in (-1,0,1):
            err=[t*h[0],-t*h[1],h[2]]
            self.assertLessEqual(abs(sum(w*e for w,e in zip(weights,err))),
                                 sum(w*v for w,v in zip(weights,h)))

    def test_signed_tail_cancellation(self):
        for n in (1,5,100):
            t=Q(1,n+1)
            left=1/t
            self.assertGreater(left,n)
            self.assertEqual((left+1-left)-(left+2-(left+1)),0)
            self.assertEqual((left+1-left)+(left+2-(left+1)),2)

    def test_exponential_polynomial_majorant(self):
        for k in range(1,8):
            a=2.0
            C=(2*k/a)**k*math.exp(-k)
            for x in (0,0.1,1,2,5,10,30):
                self.assertLessEqual(x**k*math.exp(-a*x/2),C*(1+1e-12))

    def test_laplace_complex_difference_quotient(self):
        import cmath
        z=2+1j
        x=0.7
        for w in (1e-4,1e-4j,-1e-4+1e-4j):
            q=(cmath.exp(-(z+w)*x)-cmath.exp(-z*x))/w
            self.assertLess(abs(q+x*cmath.exp(-z*x)),1e-4)

    def test_gamma_recurrence_boundary(self):
        for s in (0.5,1,3,5):
            self.assertAlmostEqual(math.gamma(s+1),s*math.gamma(s))
            self.assertLess(1e-12**s,1e-5)
            self.assertLess(100**s*math.exp(-100),1e-25)


if __name__=="__main__":
    unittest.main()
