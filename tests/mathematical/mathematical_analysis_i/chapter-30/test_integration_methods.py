from fractions import Fraction as F
from math import (sin, cos, tan, exp, log, sqrt, asin, atan, asinh, acosh, pi)
from pathlib import Path
import unittest


class Chapter30(unittest.TestCase):
    def test_parts_polynomial_identity(self):
        for x in map(F,(-3,-1,0,1,4)):
            # u=x^2, v=x^3, H=2*x^5/5.
            self.assertEqual(5*x**4-2*x**4,3*x**4)
            self.assertEqual(x**5-F(2,5)*x**5,F(3,5)*x**5)

    def test_parts_log(self):
        for x in (.2,.7,1.,3.):
            h=1e-5
            G=lambda t:t*log(t)-t
            self.assertAlmostEqual((G(x+h)-G(x-h))/(2*h),log(x),places=7)
        self.assertAlmostEqual(exp(1)*log(exp(1))-exp(1)-(log(1)-1),1)

    def test_parts_exp_trig_normalization(self):
        for x in (-2.,0.,1.,2.):
            I=(exp(x)*(cos(x)+sin(x))-1)/2
            J=(exp(x)*(sin(x)-cos(x))+1)/2
            self.assertAlmostEqual(I,exp(x)*cos(x)-1+J)
            self.assertAlmostEqual(J,exp(x)*sin(x)-I)
        self.assertEqual((exp(0)*(cos(0)+sin(0))-1)/2,0)

    def test_nonmonotone_substitution(self):
        H=lambda x:log(1+x*x)
        self.assertAlmostEqual(H(1)-H(0),log(2))
        self.assertEqual(H(1)-H(-1),0)
        self.assertAlmostEqual(H(0)-H(1),-log(2))
        for x in (-2.,-1.,0.,1.,2.):
            h=1e-5
            self.assertAlmostEqual((H(x+h)-H(x-h))/(2*h),2*x/(1+x*x),places=7)

    def test_partial_fraction_identity(self):
        A,B,C=F(-1,4),F(5,2),F(1,4)
        self.assertEqual((A+C,B-2*C,-A+B+C),(0,2,3))
        for x in map(F,(-4,-2,0,2,3)):
            self.assertEqual((2*x+3)/((x-1)**2*(x+1)),A/(x-1)+B/(x-1)**2+C/(x+1))

    def test_repeated_quadratic_numerator_split(self):
        for b,c,B,C in ((F(2),F(3),F(4),F(-1)),(F(-3),F(5),F(-2),F(7))):
            d2=c-b*b/4
            self.assertGreater(d2,0)
            for x in map(F,(-3,-1,0,2,4)):
                q=x*x+b*x+c
                self.assertEqual(q,(x+b/2)**2+d2)
                self.assertEqual(B*x+C,B*(2*x+b)/2+C-B*b/2)

    def test_quadratic_reduction_exact(self):
        for k in range(2,9):
            for t in map(F,(-2,-1,0,1,3)):
                for d2 in (F(1,4),F(1),F(7)):
                    q=t*t+d2
                    derivative=((3-2*k)*t*t+d2)/q**k
                    self.assertEqual(derivative,(3-2*k)/q**(k-1)+2*(k-1)*d2/q**k)
                    self.assertEqual((derivative+(2*k-3)/q**(k-1))/(2*(k-1)*d2),1/q**k)

    def test_trigonometric_power(self):
        for x in (-2.,-1.,0.,.7,2.):
            self.assertAlmostEqual(sin(x)*(cos(x)**2-cos(x)**4),sin(x)**3*cos(x)**2)
            self.assertAlmostEqual((1-cos(2*x))/2,sin(x)**2)

    def test_weierstrass_all_branches(self):
        for k in (-2,-1,0,1,2):
            for t in (-3.,-1.,0.,1.,3.):
                x=2*atan(t)+2*k*pi
                self.assertAlmostEqual(tan(x/2),t)
                self.assertAlmostEqual(sin(x),2*t/(1+t*t))
                self.assertAlmostEqual(cos(x),(1-t*t)/(1+t*t))
                self.assertAlmostEqual(2/(1+t*t)/(2+cos(x)),2/(3+t*t))

    def test_weierstrass_primitive(self):
        G=lambda x:2/sqrt(3)*atan(tan(x/2)/sqrt(3))
        for x in (-2.,-1.,0.,1.,2.):
            h=1e-5
            self.assertAlmostEqual((G(x+h)-G(x-h))/(2*h),1/(2+cos(x)),places=7)

    def test_trig_root(self):
        for a in (1.,2.,5.):
            for x in (-.8*a,-.2*a,0.,.5*a):
                r=sqrt(a*a-x*x)
                self.assertAlmostEqual(r/2-x*x/(2*r)+a*a/(2*r),r)
                t=asin(x/a)
                self.assertAlmostEqual(a*sin(t),x)
                self.assertAlmostEqual(a*cos(t),r)
            G=lambda x:x*sqrt(max(0.,a*a-x*x))/2+a*a*asin(x/a)/2
            self.assertAlmostEqual(G(a)-G(-a),pi*a*a/2)

    def test_hyperbolic_root_branches(self):
        for a in (1.,2.,4.):
            for x in (-3*a,-2*a,0.,2*a,3*a):
                self.assertAlmostEqual((1/a)/sqrt(1+(x/a)**2),1/sqrt(a*a+x*x))
                if abs(x)>a:
                    H=lambda t:acosh(t/a) if t>a else -acosh(-t/a)
                    h=1e-5
                    self.assertAlmostEqual((H(x+h)-H(x-h))/(2*h),1/sqrt(x*x-a*a),places=7)

    def test_sine_reduction(self):
        for n in range(2,11):
            for x in (-1.,0.,.4,1.,2.):
                s,c=sin(x),cos(x)
                derivative=(n-1)*s**(n-2)*c*c-s**n
                self.assertAlmostEqual(derivative,(n-1)*s**(n-2)-n*s**n)
                self.assertAlmostEqual(-derivative/n+(n-1)*s**(n-2)/n,s**n)
        G=lambda x:-sin(x)**3*cos(x)/4-3*sin(x)*cos(x)/8+3*x/8
        self.assertAlmostEqual(G(pi/2)-G(0),3*pi/16)

    def test_triangle_source(self):
        s=(Path(__file__).resolve().parents[4] /
           "chapters/pl/mathematical_analysis_i/30-metody-calkowania.tex").read_text(encoding="utf8")
        for token in (r"\coordinate (A) at (3,0)",r"\coordinate (B) at (3,1.8)",
                      r"\sqrt{a^2-x^2}",r"x=a\sin t"):
            self.assertIn(token,s)
        self.assertEqual(F(3)**2+F(9,5)**2,F(306,25))


if __name__=="__main__":
    unittest.main()
