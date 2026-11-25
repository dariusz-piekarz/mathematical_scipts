from fractions import Fraction as F
from math import comb
from pathlib import Path
import re
from unittest import TestCase, main

class Chapter20(TestCase):
    def test_quadratic_difference(self):
        for a in [F(-2),F(0),F(3,2)]:
            for h in [F(-1,7),F(1,11)]:
                self.assertEqual(((a+h)**2-a*a)/h,2*a+h)
                self.assertEqual((a+h)**2-a*a-2*a*h,h*h)

    def test_absolute_value_one_sided(self):
        for n in range(1,20):
            h=F(1,n)
            self.assertEqual(abs(h)/h,1)
            self.assertEqual(abs(-h)/(-h),-1)

    def test_cube_root_vertical_tangent(self):
        for n in range(1,20):
            for t in [F(1,n),F(-1,n)]:
                h=t**3
                self.assertEqual(t/h,n*n)

    def test_damped_oscillation_exponents(self):
        for n in range(1,20):
            h=F(1,n)
            self.assertEqual(h*h/h,h)
            self.assertEqual(h/h,1)
            self.assertEqual(h/(h*h),n)

    def test_product_difference_identity(self):
        for f0 in [F(0),F(-1),F(3,2)]:
            for g0 in [F(0),F(2)]:
                for h in [F(-1,5),F(1,7)]:
                    f1=f0+2*h+h*h
                    g1=g0-3*h
                    self.assertEqual((f1*g1-f0*g0)/h,
                                     (f1-f0)/h*g1+f0*(g1-g0)/h)

    def test_reciprocal_difference_identity(self):
        for a in [F(-2),F(1,2)]:
            for h in [F(-1,9),F(1,11)]:
                b=a+h
                self.assertEqual((1/b-1/a)/h,-(b-a)/(h*b*a))

    def test_integer_power_difference(self):
        for a in [F(-2),F(0),F(3,2)]:
            for h in [F(-1,5),F(1,11)]:
                for n in range(1,10):
                    self.assertEqual(((a+h)**n-a**n)/h,
                        sum(comb(n,k)*a**(n-k)*h**(k-1) for k in range(1,n+1)))

    def test_negative_integer_power(self):
        for a in [F(-2),F(3,2)]:
            for h in [F(-1,7),F(1,9)]:
                for n in range(1,7):
                    self.assertEqual(((a+h)**(-n)-a**(-n))/h,
                        -((a+h)**n-a**n)/(h*(a+h)**n*a**n))

    def test_chain_rule_zero_inner_increment(self):
        # g(b+k)=g(b)+2*b*k+k*k, including k=0.
        for b in [F(0),F(2)]:
            for h in [F(1,5),F(-1,7)]:
                for k in [F(0),h,h*h]:
                    self.assertEqual(((b+k)**2-b*b)/h,(2*b+k)*k/h)

    def test_inverse_difference_identity(self):
        for a in [F(1),F(2)]:
            for h in [F(1,9),F(-1,11)]:
                x=a+h
                self.assertEqual((x-a)/(x*x-a*a),1/(x+a))

    def test_trig_quotient_numerators(self):
        for t in [F(0),F(1,3),F(2)]:
            c=(1-t*t)/(1+t*t)
            s=2*t/(1+t*t)
            self.assertEqual(c*c+s*s,1)
            if c:
                self.assertEqual((c*c+s*s)/(c*c),1+(s/c)**2)
            if s:
                self.assertEqual((-s*s-c*c)/(s*s),-1/(s*s))

    def test_hyperbolic_quotient_numerators(self):
        for t in [F(1,3),F(1),F(2)]:
            c=(t+1/t)/2; s=(t-1/t)/2
            self.assertEqual(c*c-s*s,1)
            self.assertEqual(1-(s/c)**2,1/(c*c))
            if s:
                self.assertEqual(1-(c/s)**2,-1/(s*s))

    def test_logarithmic_composition_algebra(self):
        for x in [F(-2),F(0),F(3,2)]:
            self.assertGreater(1+x*x,0)
            for h in [F(1,9),F(-1,11)]:
                self.assertEqual(((1+(x+h)**2)-(1+x*x))/h,2*x+h)

    def test_secant_tangent_coordinates(self):
        a=F(1); h=F(3,5)
        f=lambda x:x*x/2+F(7,20)
        self.assertEqual(f(a),F(85,100))
        self.assertEqual(f(a+h),F(163,100))
        slope=(f(a+h)-f(a))/h
        self.assertEqual(slope,F(13,10))
        for x,y in [(F(45,100),F(135,1000)),(F(235,100),F(2605,1000))]:
            self.assertEqual(y,f(a)+slope*(x-a))
        for x,y in [(F(25,100),F(10,100)),(F(24,10),F(225,100))]:
            self.assertEqual(y,f(a)+a*(x-a))

    def test_differential_vs_finite_increment(self):
        for a in [F(-2),F(0),F(1)]:
            for h in [F(0),F(-1,7),F(3,5)]:
                dx=h
                dy=a*dx
                delta_y=((a+h)**2-a*a)/2
                self.assertEqual(delta_y-dy,h*h/2)
                if h:
                    self.assertEqual((delta_y-dy)/h,h/2)
        self.assertEqual(F(85,100)+F(3,5),F(145,100))
        self.assertEqual(F(163,100)-F(145,100),F(18,100))

    def test_differential_linearity_and_zero_derivative(self):
        for a in (F(-2),F(0),F(3,2)):
            h,k,lam,mu=F(-1,7),F(1,4),F(2),F(-3)
            df=lambda v:a*v
            self.assertEqual(df(lam*h+mu*k),lam*df(h)+mu*df(k))
            self.assertEqual(df(1),a)
        for h in (F(-1,10),F(1,100)):
            self.assertEqual(abs(h*h)/abs(h),abs(h))

    def test_differential_table_exact(self):
        for h,dy,delta_y,r,ratio in (
            (F(3,5),F(3,5),F(78,100),F(18,100),F(3,10)),
            (F(1,10),F(1,10),F(105,1000),F(5,1000),F(5,100)),
            (F(1,100),F(1,100),F(1005,100000),F(5,100000),F(5,1000)),
            (F(-1,10),F(-1,10),F(-95,1000),F(5,1000),F(5,100)),
        ):
            self.assertEqual(dy,h)
            self.assertEqual(delta_y,((1+h)**2-1)/2)
            self.assertEqual(r,delta_y-dy)
            self.assertEqual(r/abs(h),ratio)

    def test_differential_position(self):
        source=(Path(__file__).resolve().parents[4] /
                "chapters/pl/mathematical_analysis_i/20-pochodna.tex").read_text(encoding="utf-8")
        self.assertEqual(source.count(r"\label{ma1:def:differential}"),1)
        self.assertLess(source.index(r"\label{ma1:def:derivative}"),
                        source.index(r"\label{ma1:def:differential}"))
        self.assertLess(source.index(r"\label{ma1:def:differential}"),
                        source.index(r"\begin{tikzpicture}"))
        self.assertLess(source.index(r"\label{ma1:def:differential}"),
                        source.index(r"\section{Przybliżenie liniowe i ciągłość}"))

    def test_differential_diagram_source(self):
        source=(Path(__file__).resolve().parents[4] /
                "chapters/pl/mathematical_analysis_i/20-pochodna.tex").read_text(encoding="utf-8")
        figure=source.split(r"\begin{tikzpicture}",1)[1].split(r"\end{tikzpicture}",1)[0]
        self.assertIn(r"$\Delta x=dx=h$",figure)
        self.assertIn(r"$\Delta y$",figure)
        self.assertIn(r"$dy$",figure)
        self.assertIn(r"$r(h)$",figure)
        self.assertIn(r"(P)--(T)",figure)
        self.assertIn(r"(T)--(B)",figure)
        self.assertIn(r"(A)--(P)",figure)
        coords={name:(F(x),F(y)) for name,x,y in
                re.findall(r"\\coordinate \(([ABTP])\) at \(([\d.]+),([\d.]+)\);",figure)}
        self.assertEqual(set(coords),{"A","B","T","P"})
        a,fa=coords["A"]
        b,fb=coords["B"]
        t,ft=coords["T"]
        self.assertEqual(coords["P"],(b,fa))
        self.assertEqual(b,t)
        self.assertEqual(fa,a*a/2+F(7,20))
        self.assertEqual(fb,b*b/2+F(7,20))
        self.assertEqual(ft,fa+a*(b-a))
        self.assertEqual(fb-ft,(b-a)**2/2)

if __name__ == "__main__": main()
