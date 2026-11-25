from fractions import Fraction as F
from math import exp, factorial, log, log1p
from pathlib import Path
import unittest


def spike(n, x):
    return max(F(0), min(n*n*x, 2*n-n*n*x))


class Chapter32(unittest.TestCase):
    def test_uniform_approximation_integral_bound(self):
        for n in (2, 5, 10, 100):
            # f_n=x^2+x/n on [0,1], f=x^2.
            error=F(1,2*n)
            self.assertLessEqual(error,F(1,n))
            self.assertEqual(F(1,3)+error-F(1,3),error)

    def test_darboux_perturbation(self):
        for n in (2, 5, 10):
            # Nondecreasing f=x^2, g=f+x/n, partition into n equal pieces.
            p=[F(i,n) for i in range(n+1)]
            def gap(f):
                return sum((f(b)-f(a))*(b-a) for a,b in zip(p,p[1:]))
            a=gap(lambda x:x*x)
            b=gap(lambda x:x*x+x/n)
            self.assertLessEqual(abs(a-b),F(2,n))

    def test_moving_spike_exact_area_and_pointwise(self):
        for n in (2,4,6,20):
            p=[F(0),F(1,n),F(2,n),F(1)]
            area=sum((spike(n,a)+spike(n,b))*(b-a)/2 for a,b in zip(p,p[1:]))
            self.assertEqual(area,1)
            self.assertEqual(spike(n,F(1,n)),n)
            self.assertEqual(spike(n,F(0)),0)
        for x in (F(1,100),F(1,3),F(1)):
            n=int(2/x)+1
            self.assertEqual(spike(n,x),0)

    def test_joint_continuity_witness(self):
        for n in (2,5,10):
            for x in (F(0),F(1,3),F(1)):
                # f(x,t)=x*t^2, t0=1.
                t=1+F(1,n)
                self.assertLessEqual(abs(x*t*t-x),abs(t*t-1))

    def test_uniform_difference_quotient(self):
        for h in (F(-1,10),F(1,10),F(1,100)):
            for x in (F(0),F(1,3),F(1)):
                t=F(2)
                q=x*((t+h)**2-t*t)/h
                self.assertEqual(q-2*x*t,x*h)
                self.assertLessEqual(abs(q-2*x*t),abs(h))

    def test_higher_derivatives_polynomial(self):
        for t in (F(-2),F(0),F(3)):
            # Integral of x*t^3 over [0,1] equals t^3/2.
            for j in range(4):
                coefficient=F(factorial(3),factorial(3-j))
                self.assertEqual(coefficient*t**(3-j)/2,
                                 F(1,2)*coefficient*t**(3-j))

    def test_logarithm_parameter_integrand(self):
        for t in (-.8,-.2,0.,.5,2.):
            for x in (0.,.1,.5,1.):
                def f(s):
                    return s if x==0 else log1p(s*x)/x
                h=1e-5
                self.assertAlmostEqual((f(t+h)-f(t-h))/(2*h),1/(1+t*x),places=7)
        self.assertAlmostEqual(log1p(1e-8)/1e-8,1,places=7)

    def test_leibniz_oriented_and_equal_endpoints(self):
        for t in (F(-3,4),F(-1,4),F(0),F(1,2)):
            H=lambda x:x**3/3+t*x*x/2
            self.assertEqual(H(t)-H(F(0)),5*t**3/6)
            self.assertEqual(t*t+t*t+t*t/2,5*t*t/2)
            for h in (F(-1,100),F(1,100)):
                q=F(5,6)*((t+h)**3-t**3)/h
                self.assertEqual(q-5*t*t/2,F(5,6)*(3*t*h+h*h))

    def test_leibniz_both_moving_bounds(self):
        # f(x,t)=x+t, alpha=-t, beta=t^2.
        for t in (F(-1,2),F(0),F(1,2)):
            endpoint=(t*t+t)*2*t+(-t+t)
            interior=t*t+t
            derivative=2*t**3+3*t*t+t
            self.assertEqual(endpoint+interior,derivative)

    def test_uniform_cauchy_tails(self):
        for u,v in ((1.,2.),(5.,10.),(10.,30.)):
            for t in (.5,1.,2.,5.):
                tail=(exp(-t*u)-exp(-t*v))/t
                self.assertTrue(0<=tail<=2*exp(-u/2))

    def test_majorant_derivative(self):
        for x in (0.,.5,2.,10.):
            for t in (.5,1.,2.,4.):
                self.assertLessEqual(exp(-t*x),exp(-x/2))
                self.assertLessEqual(x*exp(-t*x),x*exp(-x/2))

    def test_exponential_moments_recurrence(self):
        for t in (F(1,2),F(1),F(3)):
            prev=1/t
            for n in range(1,8):
                moment=F(factorial(n))/t**(n+1)
                self.assertEqual(moment,n*prev/t)
                prev=moment

    def test_nonuniform_tail_at_boundary(self):
        for R in (1.,10.,100.,1000.):
            t=1/(R*R)
            self.assertAlmostEqual(exp(-t*R),exp(-1/R))
            self.assertGreater(exp(-t*R),.3)
        self.assertGreater(exp(-1/1000),.99)

    def test_nondifferentiability_despite_pointwise_integrals(self):
        for h in (F(-1,10),F(-1,100),F(1,100),F(1,10)):
            self.assertEqual(abs(h)/h,1 if h>0 else -1)
            # Integral of the partial derivative, t!=0.
            sign=1 if h>0 else -1
            self.assertEqual(2*h/abs(h)-h*h*sign/abs(h)**2,sign)
            for x in (0.,1.,5.):
                self.assertLessEqual(abs(float(h)*exp(-abs(float(h))*x)),abs(float(h)))

    def test_figure_source(self):
        s=(Path(__file__).resolve().parents[4] /
           "chapters/pl/mathematical_analysis_i/32-calki-zalezne-od-parametru.tex").read_text(encoding="utf8")
        for token in (r"(0,0)--(.5,2)--(1,0)",r"(0,0)--(.25,4)--(.5,0)",
                      r"(0,0)--({1/6},6)--({1/3},0)"):
            self.assertIn(token,s)
        for n in (2,4,6):
            self.assertEqual(F(2,n)*n/2,1)


if __name__=="__main__":
    unittest.main()
