from fractions import Fraction as F
from math import (sin, cos, tan, exp, log, sqrt, asin, atan, sinh, cosh,
                  tanh, asinh, acosh, atanh)
from pathlib import Path
import unittest


class Chapter28(unittest.TestCase):
    def test_polynomial_normalization(self):
        coeff=(F(5),F(-4),F(3))
        primitive=(F(-2),)+tuple(c/(i+1) for i,c in enumerate(coeff))
        self.assertEqual(primitive,(F(-2),F(5),F(-2),F(1)))
        self.assertEqual(sum(primitive),2)
        self.assertEqual(tuple(i*c for i,c in enumerate(primitive) if i),coeff)

    def test_constant_difference_and_tangents(self):
        for x in (F(-2),F(0),F(1),F(3,2)):
            for c in (F(-1),F(0),F(2)):
                for h in (F(-1,10),F(1,10)):
                    self.assertEqual(((x+h)**2+c-(x*x+c))/h,2*x+h)
            self.assertEqual((x*x+2)-(x*x-1),3)

    def test_component_constants(self):
        g=lambda x:log(abs(x))+(1 if x>0 else 0)
        self.assertEqual(g(-1),0)
        self.assertEqual(g(1),1)
        for x in (-2.,-1.,1.,2.):
            self.assertAlmostEqual((g(x+1e-5)-g(x-1e-5))/2e-5,1/x,places=7)

    def test_linearity_coefficients(self):
        p=(F(1),F(2),F(3))
        q=(F(7),F(-1),F(5))
        for a,b in ((F(0),F(0)),(F(2),F(-3)),(F(0),F(1))):
            for c in (F(0),F(4)):
                P=tuple(a*u+b*v+(c if i==0 else 0)
                        for i,(u,v) in enumerate(zip(p,q)))
                self.assertEqual(tuple(i*P[i] for i in range(1,len(P))),
                                 tuple(a*i*p[i]+b*i*q[i] for i in range(1,len(P))))
                if a==b==0:
                    self.assertEqual(P,(c,0,0))

    def test_linearity_family_constant_recovery(self):
        for a,b in ((F(2),F(-3)),(F(0),F(2)),(F(-3),F(0))):
            for c in (F(-7,3),F(0),F(5)):
                c1,c2=(c/a,F(0)) if a else (F(0),c/b)
                self.assertEqual(a*c1+b*c2,c)
        self.assertNotEqual(F(0)*F(2)+F(0)*F(3),F(1))

    def test_affine_preimage_and_independent_normalization(self):
        for a,b in ((F(2),F(-1)),(F(-3),F(2))):
            lo,hi=sorted(((F(-2)-b)/a,(F(3)-b)/a))
            for x in (lo-1,lo,(lo+hi)/2,hi,hi+1):
                self.assertEqual(lo<x<hi,-2<a*x+b<3)
        for c_minus,c_plus in ((F(0),F(1)),(F(0),F(7)),(F(0),F(-3))):
            # log|-1|=log|1|=0; fixing the negative branch does not fix the positive branch.
            self.assertEqual(c_minus,0)
            self.assertNotEqual(c_minus,c_plus)

    def test_integer_power_primitive(self):
        for r in (-5,-3,-2,0,1,3,8):
            for x in (F(-2),F(-1,2),F(1,2),F(3)):
                self.assertEqual(F(1,r+1)*(r+1)*x**r,x**r)
            if r>=0:
                self.assertEqual(F(1,r+1)*(r+1)*F(0)**r,F(1) if r==0 else F(0))

    def test_elementary_primitive_table(self):
        # Numerical derivative witnesses only; the proof is in the text.
        rows=((exp,exp,(-1.,0.,1.)),
              (lambda x:3**x/log(3),lambda x:3**x,(-1.,0.,1.)),
              (sin,cos,(-1.,0.,1.)),(lambda x:-cos(x),sin,(-1.,0.,1.)),
              (tan,lambda x:1/cos(x)**2,(-.5,0.,.5)),
              (lambda x:-cos(x)/sin(x),lambda x:1/sin(x)**2,(-1.,.5,1.)),
              (atan,lambda x:1/(1+x*x),(-1.,0.,1.)),
              (asin,lambda x:1/sqrt(1-x*x),(-.5,0.,.5)))
        h=1e-5
        for primitive,f,points in rows:
            for x in points:
                self.assertAlmostEqual((primitive(x+h)-primitive(x-h))/(2*h),f(x),places=7)

    def test_hyperbolic_primitive_table(self):
        rows=((sinh,cosh,(-1.,0.,1.)),(cosh,sinh,(-1.,0.,1.)),
              (tanh,lambda x:1/cosh(x)**2,(-1.,0.,1.)),
              (lambda x:-cosh(x)/sinh(x),lambda x:1/sinh(x)**2,(-1.,.5,1.)),
              (asinh,lambda x:1/sqrt(1+x*x),(-1.,0.,1.)),
              (acosh,lambda x:1/sqrt(x*x-1),(1.5,2.,3.)),
              (lambda x:-acosh(-x),lambda x:1/sqrt(x*x-1),(-3.,-2.,-1.5)),
              (atanh,lambda x:1/(1-x*x),(-.5,0.,.5)),
              (lambda x:atanh(1/x),lambda x:1/(1-x*x),(-3.,-2.,2.,3.)))
        h=1e-5
        for primitive,f,points in rows:
            for x in points:
                self.assertAlmostEqual((primitive(x+h)-primitive(x-h))/(2*h),f(x),places=7)

    def test_affine_argument(self):
        for a,b in ((F(2),F(-1)),(F(-3),F(2))):
            for x in (F(-2),F(0),F(1)):
                # Derivative of (ax+b)^3/(3a) by the chain rule.
                self.assertEqual(3*(a*x+b)**2*a/(3*a),(a*x+b)**2)
        for x in (-1.,0.,1.):
            h=1e-5
            P=lambda t:sin(3*t-1)/3
            self.assertAlmostEqual((P(x+h)-P(x-h))/(2*h),cos(3*x-1),places=7)

    def test_step_omits_intermediate_value(self):
        f=lambda x:int(x>=0)
        self.assertEqual((f(-1),f(1)),(0,1))
        for x in (F(-2),F(-1,100),F(0),F(1,100),F(2)):
            self.assertNotEqual(f(x),F(1,2))

    def test_oscillating_derivative_and_primitive(self):
        from math import pi
        for n in (1,5,20,100):
            for x,v in ((1/(2*n*pi),-1),(1/((2*n+1)*pi),1)):
                self.assertAlmostEqual(2*x*sin(1/x)-cos(1/x),v,places=12)
                self.assertLessEqual(abs(x*sin(1/x)),abs(x))

    def test_figure_source(self):
        s=(Path(__file__).resolve().parents[4] /
           "chapters/pl/mathematical_analysis_i/28-funkcje-pierwotne.tex").read_text(encoding="utf8")
        for token in (r"plot (\x,{\x*\x})",r"plot (\x,{\x*\x+2})",
                      r"plot (\x,{\x*\x-1})","(1,1)","(1,3)","(1,0)"):
            self.assertIn(token,s)
        for c,y in ((0,1),(2,3),(-1,0)):
            self.assertEqual(1+c,y)
            self.assertEqual(F(17,10)+c-(F(3,10)+c),2*(F(135,100)-F(65,100)))


if __name__=="__main__":
    unittest.main()
