from fractions import Fraction as F
from math import factorial
from pathlib import Path
import unittest

class Chapter26(unittest.TestCase):
    def test_landau_with_zeros(self):
        for x in (F(-1,10),F(0),F(1,10)):
            g=x*x
            f=x*g
            self.assertLessEqual(abs(f),F(1,10)*abs(g))
            if g==0:
                self.assertEqual(f,0)

    def test_equivalence_relative_error(self):
        for x in (F(-1,10),F(1,10)):
            g=x*x
            f=g*(1+x)
            self.assertEqual((f-g)/g,f/g-1)
            self.assertLessEqual(abs(g),2*abs(f))

    def test_same_sign_sum(self):
        for g,v in ((F(1),F(2)),(F(-3),F(-1))):
            for r,s in ((F(1,10),F(-1,5)),(F(0),F(1,7))):
                f,u=g*(1+r),v*(1+s)
                self.assertLessEqual(abs((f+u)/(g+v)-1),max(abs(r),abs(s)))

    def test_cancellation(self):
        for x in (F(1,10),F(1,100),F(1,1000)):
            f,g=x+x*x,x
            u,v=-x+2*x*x,-x+x*x
            self.assertEqual(f/g-1,x)
            self.assertEqual(u/v-1,x*x/v)
            self.assertEqual((f+u)/(g+v),3)

    def test_product_error_identity(self):
        for r,s in ((F(1,10),F(-1,5)),(F(0),F(1,7))):
            self.assertEqual((1+r)*(1+s)-1,r+s+r*s)

    def test_growth_power_bound(self):
        for x in (F(1),F(10),F(100)):
            for m in (3,4,5):
                p=2
                c=F(2)
                lower=(c*x)**m/factorial(m)
                self.assertEqual(x**p/lower,F(factorial(m),1)/c**m*x**(p-m))

    def test_factorial_ratios(self):
        for c in (F(1,2),F(2),F(3)):
            for n in range(6,13):
                a=c**n/factorial(n)
                b=c**(n+1)/factorial(n+1)
                self.assertEqual(b/a,c/(n+1))
                self.assertLessEqual(b,a/2)

    def test_geometric_exact_remainder(self):
        for x in (F(-1,3),F(1,3),F(1,10)):
            for n in range(7):
                remainder=1/(1-x)-sum(x**j for j in range(n+1))
                self.assertEqual(remainder,x**(n+1)/(1-x))
                self.assertLessEqual(abs(remainder),2*abs(x)**(n+1))

    def test_geometric_infinity(self):
        for t in (F(3),F(10),F(100)):
            for n in range(5):
                remainder=1/(t-1)-sum(t**(-j) for j in range(1,n+2))
                self.assertEqual(remainder,t**(-n-2)/(1-1/t))

    def test_asymptotic_coefficient_recovery(self):
        coeffs=(F(2),F(-3),F(5),F(7))
        for x in (F(-1,10),F(1,100)):
            f=sum(c*x**j for j,c in enumerate(coeffs))
            for k in range(len(coeffs)):
                quotient=(f-sum(coeffs[j]*x**j for j in range(k)))/x**k
                self.assertEqual(quotient,coeffs[k]+sum(coeffs[j]*x**(j-k) for j in range(k+1,len(coeffs))))

    def test_taylor_cancellation_coefficient(self):
        for x in (F(1,10),F(-1,10)):
            sin_poly=x-x**3/6
            cos_poly=1-x*x/2
            self.assertEqual((sin_poly-x*cos_poly)/x**3,F(1,3))

    def test_reciprocal_identity(self):
        for eta in (F(0),F(-1,3),F(1,10)):
            self.assertEqual(1/(1+eta),1-eta+eta*eta/(1+eta))
            self.assertLessEqual(abs(eta*eta/(1+eta)),2*eta*eta)

    def test_figure_source(self):
        s=(Path(__file__).resolve().parents[4] /
           "chapters/pl/mathematical_analysis_i/26-asymptotyka.tex").read_text(encoding="utf8")
        for token in (r"plot (\x,{ln(\x)})",r"plot (\x,{\x})",r"plot (\x,{exp(\x/6)})"):
            self.assertIn(token,s)

if __name__=="__main__":
    unittest.main()
