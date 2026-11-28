from fractions import Fraction as F
from math import exp, sqrt
from pathlib import Path
import re
import unittest

def sums(f,a,b,n):
    h=(b-a)/n
    l=h*sum(f(a+j*h) for j in range(n))
    r=h*sum(f(a+j*h) for j in range(1,n+1))
    m=h*sum(f(a+(j+F(1,2))*h) for j in range(n))
    return l,r,m,(l+r)/2

def simpson(f,a,b,n):
    h=(b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if j%2 else 2)*f(a+j*h) for j in range(1,n)))

class Chapter35(unittest.TestCase):
    def test_rectangle_linear(self):
        for n in (1,2,4,10):
            l,r,m,t=sums(lambda x:x,F(0),F(1),n)
            self.assertEqual(F(1,2)-l,F(1,2*n))
            self.assertEqual(r-F(1,2),F(1,2*n))
            self.assertEqual(m,F(1,2))
    def test_quadratic(self):
        for n in (1,2,4,10):
            _,_,m,t=sums(lambda x:x*x,F(0),F(1),n)
            self.assertEqual(F(1,3)-m,F(1,12*n*n))
            self.assertEqual(t-F(1,3),F(1,6*n*n))
            _,_,m,t=sums(lambda x:-x*x,F(0),F(1),n)
            self.assertGreaterEqual(m,F(-1,3))
            self.assertLessEqual(t,F(-1,3))
    def test_simpson_exactness(self):
        for n in (2,4,8):
            for k in range(4):
                self.assertEqual(simpson(lambda x:x**k,F(-1),F(2),n),(F(2)**(k+1)-F(-1)**(k+1))/(k+1))
    def test_simpson_quartic(self):
        for n in (2,4,8,12):
            self.assertEqual(simpson(lambda x:x**4,F(0),F(1),n)-F(1,5),F(24,180*n**4))
    def test_simpson_kernel(self):
        for h in (F(1),F(2),F(1,3)):
            c=[h**4/72,0,-h*h/12,h/9,F(-1,24)]
            def d(t,k):
                p=c[:]
                for _ in range(k):
                    p=[j*p[j] for j in range(1,len(p))]
                return sum(v*t**j for j,v in enumerate(p))
            for k in (0,1,2):
                self.assertEqual(d(h,k),0)
            self.assertEqual(d(0,3),2*h/3)
            self.assertEqual(d(h,3),-h/3)
            self.assertEqual(d(0,4),-1)
            self.assertEqual(2*sum(v*h**(j+1)/(j+1) for j,v in enumerate(c)),h**5/90)
    def test_simpson_kernel_even_extension(self):
        for h in (F(1),F(3,2),F(2)):
            for j in range(11):
                t=h*j/10
                right=(h-t)**3*(h+3*t)/72
                left=(h+(-t))**3*(h-3*(-t))/72
                self.assertEqual(right,left)
                self.assertGreaterEqual(right,0)
                self.assertEqual(right,h**4/72-h*h*t*t/12+h*t**3/9-t**4/24)
    def test_trapezoid_identity(self):
        for n in (1,2,5):
            f=lambda x:x**5-2*x+3
            t=sums(f,F(-1),F(2),n)[3]
            t2=sums(f,F(-1),F(2),2*n)[3]
            self.assertEqual(simpson(f,F(-1),F(2),2*n),(4*t2-t)/3)
    def test_exp_bound(self):
        for n in (2,4,8,12,16):
            q=simpson(exp,F(0),F(1),n)
            self.assertLessEqual(abs(q-(exp(1)-1)),exp(1)/(180*n**4))
        self.assertLess(F(3,180*12**4),F(1,10**6))
    def test_gauss_moments(self):
        for k in range(4):
            self.assertEqual(0 if k%2 else 2*F(1,3)**(k//2),0 if k%2 else F(2,k+1))
        self.assertEqual(F(2,5)-F(2,9),F(24,135))
    def test_gauss_kernel(self):
        self.assertEqual((F(2,5)-F(4,9)+F(2,9))/24,F(1,135))
    def test_gauss_affine(self):
        for a,b in ((0.,1.),(-2.,3.),(2.,4.)):
            m=(a+b)/2
            h=(b-a)/2
            q=h*((m-h/sqrt(3))**4+(m+h/sqrt(3))**4)
            self.assertAlmostEqual((b**5-a**5)/5-q,h**5*24/135,places=10)
    def test_richardson(self):
        for n in (2,4,8):
            q=simpson(lambda x:x**4,F(0),F(1),n)
            q2=simpson(lambda x:x**4,F(0),F(1),2*n)
            self.assertEqual(F(1,5)-q2,(q2-q)/15)
    def test_false_zero_refinement_estimator(self):
        from math import prod
        p=lambda x:prod((x-F(j,4))**2 for j in range(5))
        self.assertEqual(simpson(p,F(0),F(1),2),0)
        self.assertEqual(simpson(p,F(0),F(1),4),0)
        self.assertGreater(p(F(1,8)),0)
        # Integrate the expanded polynomial in rational arithmetic.
        c=[F(1)]
        for j in range(5):
            for _ in range(2):
                d=[F(0)]*(len(c)+1)
                for k,a in enumerate(c):
                    d[k]-=F(j,4)*a
                    d[k+1]+=a
                c=d
        self.assertGreater(sum(a/F(k+1) for k,a in enumerate(c)),0)
    def test_positive_weights(self):
        for n in (2,4,8):
            f=lambda x:x*x
            g=lambda x:f(x)+F(1,100)*(-1)**int(n*x)
            self.assertLessEqual(abs(simpson(f,F(0),F(1),n)-simpson(g,F(0),F(1),n)),F(1,100))
    def test_listing(self):
        src=(Path(__file__).resolve().parents[4]/"chapters/pl/mathematical_analysis_i/35-kwadratury-numeryczne.tex").read_text(encoding="utf8")
        code=re.search(r"\\begin\{lstlisting\}\[style=python\](.*?)\\end\{lstlisting\}",src,re.S).group(1)
        ns={}
        exec(code.split("for n in (4, 8, 16, 32):")[0],ns)
        self.assertAlmostEqual(ns["simpson"](lambda x:x**3,0,1,4),.25)
        for n in (0,1,3,-2,2.5):
            with self.assertRaises(ValueError):
                ns["simpson"](lambda x:x,0,1,n)

if __name__=="__main__":
    unittest.main()
