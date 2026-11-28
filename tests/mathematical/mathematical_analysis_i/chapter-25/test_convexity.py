from fractions import Fraction as F
from math import exp, log
from pathlib import Path
import unittest

class Chapter25(unittest.TestCase):
    def test_quadratic_chord_gap(self):
        for x,y in ((F(-1),F(2)),(F(0),F(0)),(F(2),F(-3))):
            for t in (F(0),F(1,3),F(1)):
                z=(1-t)*x+t*y
                gap=(1-t)*x*x+t*y*y-z*z
                self.assertEqual(gap,t*(1-t)*(x-y)**2)
                self.assertEqual(gap>0,x!=y and 0<t<1)

    def test_secant_interpolation(self):
        for u,v,w in ((F(-3),F(-1),F(2)),(F(0),F(1,3),F(2))):
            s=lambda x,y:(y*y-x*x)/(y-x)
            self.assertLess(s(u,v),s(u,w))
            self.assertLess(s(u,w),s(v,w))
            self.assertEqual(s(u,w),((v-u)*s(u,v)+(w-v)*s(v,w))/(w-u))

    def test_endpoint_counterexample(self):
        f=lambda x:int(x==0)
        for x,y in ((F(0),F(1)),(F(0),F(0)),(F(1,3),F(0))):
            for t in (F(0),F(1,2),F(1)):
                self.assertLessEqual(f((1-t)*x+t*y),(1-t)*f(x)+t*f(y))

    def test_lipschitz_secant_bounds(self):
        u,a,b,v=map(F,(-3,-2,2,3))
        s=lambda x,y:x+y
        for x,y in ((a,b),(a,F(0)),(F(-1),b),(F(1,3),F(2,3))):
            self.assertLessEqual(s(u,a),s(x,y))
            self.assertLessEqual(s(x,y),s(b,v))
            self.assertLessEqual(abs(y*y-x*x),5*abs(y-x))

    def test_one_sided_abs(self):
        for h in (F(1,10),F(1,4)):
            self.assertEqual(abs(-h)/(-h),-1)
            self.assertEqual(abs(h)/h,1)
            for p in (F(-1),F(0),F(1)):
                self.assertGreaterEqual(abs(h),p*h)
                self.assertGreaterEqual(abs(-h),-p*h)

    def test_support_abs_outside_interval(self):
        for h in (F(1,10),F(2,3)):
            for p in (F(-2),F(-3,2),F(3,2),F(2)):
                x=h if p>0 else -h
                self.assertLess(abs(x),p*x)
    
    def test_jensen_induction_normalization(self):
        for ws in ((F(1,6),F(1,3),F(1,2)),(F(1,7),F(2,7),F(4,7))):
            for xs in ((F(-3),F(2),F(5)),(F(2),F(2),F(2))):
                s=1-ws[-1]
                z=sum(w*x/s for w,x in zip(ws[:-1],xs[:-1]))
                self.assertEqual(sum(ws[:-1])/s,1)
                mu=sum(w*x for w,x in zip(ws,xs))
                self.assertEqual(s*z+ws[-1]*xs[-1],mu)
                first=s*z*z+ws[-1]*xs[-1]**2-mu**2
                second=sum(w*x*x for w,x in zip(ws[:-1],xs[:-1]))-s*z*z
                self.assertGreaterEqual(first,0)
                self.assertGreaterEqual(second,0)
                self.assertEqual(first+second,sum(w*x*x for w,x in zip(ws,xs))-mu**2)
                self.assertEqual(first+second==0,len(set(xs))==1)

    def test_support_quadratic(self):
        for a in (F(-2),F(0),F(3,2)):
            for x in (F(-3),a,F(4)):
                self.assertEqual(x*x-a*a-2*a*(x-a),(x-a)**2)

    def test_strict_convexity_without_positive_second(self):
        for u,v in ((F(-2),F(-1)),(F(-1),F(0)),(F(-1),F(1)),(F(0),F(1,2))):
            self.assertEqual(v**3-u**3,(v-u)*(u*u+u*v+v*v))
            self.assertGreater(4*v**3-4*u**3,0)
        self.assertEqual(12*0**2,0)

    def test_jensen_quadratic_with_zero_weights(self):
        for weights in ((F(1,3),F(0),F(2,3)),(F(1),F(0),F(0)),(F(1,2),F(1,2),F(0))):
            for xs in ((F(2),F(-1),F(2)),(F(-2),F(1),F(3))):
                mu=sum(w*x for w,x in zip(weights,xs))
                gap=sum(w*x*x for w,x in zip(weights,xs))-mu*mu
                self.assertEqual(gap,sum(w*(x-mu)**2 for w,x in zip(weights,xs)))
                self.assertEqual(gap==0,len({x for w,x in zip(weights,xs) if w>0})==1)

    def test_amgm(self):
        for xs,ws in (((1.,4.),(.5,.5)),((1.,2.,8.),(.25,.25,.5)),((2.,9.,2.),(.5,0.,.5))):
            arithmetic=sum(x*w for x,w in zip(xs,ws))
            geometric=exp(sum(w*log(x) for x,w in zip(xs,ws)))
            self.assertGreaterEqual(arithmetic+1e-14,geometric)

    def test_dyadic_midpoints(self):
        for m in range(1,8):
            for j in range(2**(m-1)):
                t=F(2*j+1,2**m)
                l,r=F(j,2**(m-1)),F(j+1,2**(m-1))
                self.assertEqual(t,(l+r)/2)
                self.assertLessEqual(t*t,(l*l+r*r)/2)

    def test_inflection_counterexamples(self):
        for h in (F(1,10),F(1,3)):
            self.assertLess(6*(-h),0)
            self.assertGreater(6*h,0)
            self.assertEqual(12*(-h)**2,12*h*h)
            self.assertEqual(2*abs(h)/h,2)
            self.assertEqual(2*abs(-h)/(-h),-2)

    def test_bernoulli_real(self):
        # Positive rational square bases give exact half-integer powers.
        for t in (F(1,4),F(1,2),F(1),F(3,2),F(3)):
            x=t*t-1
            for k in (-4,-2,-1,0,1,2,3,4):
                r=F(k,2)
                gap=t**k-(1+r*x)
                if 0<r<1:
                    self.assertLessEqual(gap,0)
                else:
                    self.assertGreaterEqual(gap,0)
                self.assertEqual(gap==0,x==0 or r in (0,1))
        for r in (F(1,2),F(1),F(2)):
            self.assertEqual((0-(1-r))==0,r==1)

    def test_young(self):
        # p=3, q=3/2: b=t^2, so b^q=t^3 exactly.
        for a in (F(0),F(1,2),F(1),F(2)):
            for t in (F(0),F(1,2),F(1),F(3)):
                b=t*t
                gap=a**3/3+2*t**3/3-a*b
                self.assertGreaterEqual(gap,0)
                self.assertEqual(gap==0,a**3==t**3)
                self.assertEqual(gap,(a-t)**2*(a+2*t)/3)
        for a,b in ((F(0),F(0)),(F(0),F(2)),(F(2),F(2)),(F(1),F(3))):
            self.assertEqual((a*a+b*b)/2-a*b,(a-b)**2/2)

    def test_figure_source(self):
        s=(Path(__file__).resolve().parents[4] /
           "chapters/pl/mathematical_analysis_i/25-wypuklosc-i-wkleslosc.tex").read_text(encoding="utf8")
        for token in ("(-1,.8)","(2,2.3)","(.5,.425)","(.5,1.55)",
                      r"plot (\x,{\x*\x*\x})",r"plot (\x,{\x*\x*\x*\x})"):
            self.assertIn(token,s)
        f=lambda x:x*x/2+F(3,10)
        self.assertEqual(f(F(-1)),F(8,10))
        self.assertEqual(f(F(2)),F(23,10))
        self.assertEqual(f(F(1,2)),F(425,1000))
        self.assertEqual((f(F(-1))+f(F(2)))/2,F(155,100))

if __name__=="__main__":
    unittest.main()
