from fractions import Fraction as F
from pathlib import Path
import re
from unittest import TestCase, main

class Chapter21(TestCase):
    def test_fermat_signs(self):
        for h in [F(-3,7),F(-1,100),F(1,100),F(3,7)]:
            quotient=-h*h/h
            self.assertLessEqual(quotient,0) if h>0 else self.assertGreaterEqual(quotient,0)
            self.assertEqual((h*h)/h,-quotient)

    def test_stationary_not_extremum(self):
        for n in range(1,30):
            h=F(1,n)
            self.assertGreater(h**3,0)
            self.assertLess((-h)**3,0)
            self.assertEqual(h**3/h,h*h)

    def test_rolle_auxiliary(self):
        for a,b in [(F(-2),F(3)),(F(1,3),F(5,4))]:
            f=lambda x:(x-a)*(x-b)+2
            c=(a+b)/2
            self.assertEqual(f(a),f(b))
            self.assertTrue(a<c<b)
            self.assertEqual(2*c-a-b,0)

    def test_lagrange_auxiliary_endpoints(self):
        for a,b in [(F(-2),F(1)),(F(1,3),F(7,5))]:
            f=lambda x:x**2+3*x-1
            m=(f(b)-f(a))/(b-a)
            auxiliary=lambda x:f(x)-f(a)-m*(x-a)
            self.assertEqual(auxiliary(a),0)
            self.assertEqual(auxiliary(b),0)
            c=(a+b)/2
            self.assertEqual(2*c+3,m)

    def test_lagrange_multiple_witnesses_squared(self):
        # f(x)=x^3 on [-1,1], witness squares are exactly 1/3.
        slope=(F(1)**3-F(-1)**3)/2
        witness_squared=slope/3
        self.assertTrue(0<witness_squared<1)
        self.assertEqual(3*witness_squared,slope)

    def test_cauchy_auxiliary_endpoints(self):
        a,b=F(1),F(2)
        f=lambda x:x*x
        g=lambda x:x**3
        A=f(b)-f(a); B=g(b)-g(a)
        H=lambda x:B*(f(x)-f(a))-A*(g(x)-g(a))
        self.assertEqual(H(a),0)
        self.assertEqual(H(b),0)
        c=F(14,9)
        self.assertTrue(a<c<b)
        self.assertEqual(B*2*c-A*3*c*c,0)
        self.assertEqual(A/B,2/(3*c))

    def test_cauchy_degenerate_cross_product(self):
        A=F(2); B=F(0); c=F(0)
        fp=F(1); gp=2*c
        self.assertEqual(A*gp,B*fp)
        self.assertEqual(B,0)
        self.assertEqual(gp,0)

    def test_cubic_strict_monotonicity(self):
        points=[F(i,5) for i in range(-15,16)]
        for u in points:
            for v in points:
                if u<v:
                    self.assertEqual(v**3-u**3,(v-u)*(v*v+u*v+u*u))
                    self.assertGreater(v*v+u*v+u*u,0)
                    self.assertGreater(v**3-u**3,0)

    def test_increment_bounds(self):
        for u in [F(1),F(3,2),F(2)]:
            for v in [F(2),F(5,2),F(3)]:
                if u<v:
                    increment=v*v-u*u
                    self.assertLessEqual(2*(v-u),increment)
                    self.assertLessEqual(increment,6*(v-u))

    def test_inverse_lipschitz(self):
        for u in [F(-2),F(0),F(1,2)]:
            for v in [F(1),F(2),F(3)]:
                f=lambda x:x**3+2*x
                self.assertLessEqual(abs(v-u),abs(f(v)-f(u))/2)

    def test_logarithm_bound_order(self):
        # Exact order of the lower and upper bounds, not a numerical log proof.
        for x in [F(1,100),F(2,3),F(10)]:
            self.assertTrue(0<x/(1+x)<x)

    def test_endpoint_difference_sign(self):
        a,b=F(0),F(2)
        for h in [F(1,9),F(1,2)]:
            c=a+h/2
            d=b-h/2
            self.assertTrue(a<c<a+h)
            self.assertTrue(b-h<d<b)
            self.assertEqual(((a+h)**2-a*a)/h,2*c)
            self.assertEqual((b*b-(b-h)**2)/h,2*d)
            self.assertEqual(((b-h)**2-b*b)/(-h),2*d)

    def test_rolle_figure_coordinates(self):
        source=(Path(__file__).resolve().parents[4] /
                "chapters/pl/mathematical_analysis_i/21-twierdzenia-o-wartosci-sredniej.tex").read_text(encoding="utf-8")
        pictures=re.findall(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}",source,re.S)
        self.assertEqual(len(pictures),2)
        coords=re.findall(r"\\fill(?:\[[^\]]+\])? \(([\d.]+),([\d.]+)\) circle",pictures[0])
        points=[(F(x),F(y)) for x,y in coords]
        self.assertEqual(len(points),3)
        for x,y in points:
            self.assertEqual(y,F(145,100)-(x-1)**2)
        self.assertEqual(points[0][1],points[1][1])
        self.assertEqual(points[2][0],1)
        tangent=re.findall(r"\\draw\[green!40!black[^\]]*\] \(([\d.]+),([\d.]+)\)--\(([\d.]+),([\d.]+)\);",pictures[0])
        self.assertEqual(len(tangent),1)
        x1,y1,x2,y2=map(F,tangent[0])
        c,fc=points[2]
        self.assertTrue(x1<c<x2)
        self.assertEqual(y1,fc)
        self.assertEqual(y2,fc)

    def test_lagrange_figure_coordinates(self):
        source=(Path(__file__).resolve().parents[4] /
                "chapters/pl/mathematical_analysis_i/21-twierdzenia-o-wartosci-sredniej.tex").read_text(encoding="utf-8")
        picture=re.findall(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}",source,re.S)[1]
        coords=re.findall(r"\\fill(?:\[[^\]]+\])? \(([\d.]+),([\d.]+)\) circle",picture)
        points=[(F(x),F(y)) for x,y in coords]
        self.assertEqual(len(points),3)
        for x,y in points:
            self.assertEqual(y,F(7,10)*x*x+F(7,20))
        (a,fa),(b,fb),(c,fc)=points
        m=(fb-fa)/(b-a)
        self.assertEqual(m,F(14,10)*c)
        lines=re.findall(r"\\draw\[(orange!85!black|green!40!black)[^\]]*\] \(([\d.]+),([\d.]+)\)--\(([\d.]+),([\d.]+)\);",picture)
        self.assertEqual(len(lines),2)
        self.assertEqual({line[0] for line in lines},{'orange!85!black','green!40!black'})
        for color,x1,y1,x2,y2 in lines:
            x1,y1,x2,y2=map(F,(x1,y1,x2,y2))
            self.assertEqual((y2-y1)/(x2-x1),m)
            x,y=(a,fa) if color.startswith("orange") else (c,fc)
            self.assertEqual(y1-y,m*(x1-x))

if __name__ == "__main__": main()
