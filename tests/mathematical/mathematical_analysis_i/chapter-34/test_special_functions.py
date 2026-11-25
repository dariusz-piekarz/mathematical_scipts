from fractions import Fraction as F
from math import exp, log, sin, cos, atan, sqrt, pi, factorial, gamma, erf, erfc
from pathlib import Path
import unittest


def simpson(fun, a, b, n=4000):
    h=(b-a)/n
    return h/3*(fun(a)+fun(b)+sum((4 if j%2 else 2)*fun(a+j*h)
                                  for j in range(1,n)))


class Chapter34(unittest.TestCase):
    def test_gamma_recurrence(self):
        for s in (.25,.5,1.,1.5,3.7):
            self.assertAlmostEqual(gamma(s+1),s*gamma(s),places=11)
        for n in range(8):
            self.assertAlmostEqual(gamma(n+1),factorial(n))

    def test_gamma_log_majorants(self):
        for c,d in ((.25,2.),(1.,3.)):
            for x in (.001,.1,.9,1.,2.,8.):
                for s in (c,(c+d)/2,d):
                    for k in range(4):
                        val=x**(s-1)*abs(log(x))**k*exp(-x)
                        bound=x**(c-1)*abs(log(x))**k if x<=1 else x**(d+k-1)*exp(-x)
                        self.assertLessEqual(val,bound+1e-14)

    def test_gamma_log_moment(self):
        for c in (.5,1.,2.):
            for k in range(4):
                expected=factorial(k)/c**(k+1)
                self.assertAlmostEqual(simpson(lambda u:u**k*exp(-c*u),0,100,20000),
                                       expected,places=6)

    def test_beta_recurrence_polynomial(self):
        def beta_int(p,q):
            return sum(F((-1)**j*factorial(q-1),factorial(j)*factorial(q-1-j)*(p+j))
                       for j in range(q))
        for p in range(1,6):
            for q in range(1,6):
                val=beta_int(p,q)
                self.assertEqual(val,beta_int(q,p))
                self.assertEqual(beta_int(p,q+1),F(q,p+q)*val)
                self.assertEqual(val,beta_int(p+1,q)+beta_int(p,q+1))
                self.assertEqual(val,F(factorial(p-1)*factorial(q-1),factorial(p+q-1)))

    def test_beta_scaling_majorant(self):
        for q in (.2,1.,3.):
            for n in (4,20,100):
                for u in (.1,1.,n/2,n*.99):
                    self.assertLessEqual((1-u/n)**(q+n-1),exp(-u/2))
                    if u<n/2:
                        self.assertLessEqual(abs(log(1-u/n)+u/n),(u/n)**2+1e-15)

    def test_euler_limit_integer(self):
        for p in (1,2,3,5):
            for n in (10,100,1000):
                val=F(n**p*factorial(n),factorial(n+p))*factorial(p-1)
                exact=F(factorial(p-1))
                self.assertLess(val,exact)
                self.assertLessEqual(exact-val,exact*F(p*(p+1),2*n))

    def test_beta_gamma_ratio_products(self):
        for p,q in ((F(1,2),F(1,3)),(F(3,2),F(2))):
            for n in (2,5,12):
                product=F(1)
                for j in range(n):
                    product*= (q+j)/(p+q+j)
                longer=product*(q+n)/(p+q+n)
                self.assertEqual(longer/product,(q+n)/(p+q+n))

    def test_beta_trigonometric(self):
        for p,q in ((1,1),(2,3),(3,2),(.5,.5)):
            fun=lambda t:2*sin(t)**(2*p-1)*cos(t)**(2*q-1)
            self.assertAlmostEqual(simpson(fun,0,pi/2),gamma(p)*gamma(q)/gamma(p+q),places=9)

    def test_wallis_bounds(self):
        w=F(1)
        for n in range(1,501):
            w*=F(4*n*n,4*n*n-1)
            self.assertLess(float(w),pi/2)
            self.assertLessEqual(pi/2,float(w)*((2*n+1)/(2*n))+1e-14)

    def test_gaussian_integral(self):
        for a in (.25,1.,3.):
            self.assertAlmostEqual(simpson(lambda x:exp(-a*x*x),-20,20,10000),
                                   sqrt(pi/a),places=9)
        for n in range(7):
            self.assertAlmostEqual(gamma(n+.5),sqrt(pi)*factorial(2*n)/(4**n*factorial(n)),places=9)

    def test_erf_series(self):
        for x in (-2.,-1.,0.,.5,1.,2.):
            value=2/sqrt(pi)*sum((-1)**n*x**(2*n+1)/(factorial(n)*(2*n+1)) for n in range(40))
            self.assertAlmostEqual(value,erf(x),places=10)

    def test_erfc_tail(self):
        for x in (.5,1.,2.,4.,8.):
            leading=exp(-x*x)/(x*sqrt(pi))
            ratio=erfc(x)/leading
            self.assertLessEqual(ratio,1)
            self.assertGreaterEqual(ratio,1-1/(2*x*x))

    def test_damped_fresnel(self):
        for a,b in ((1.,.5),(1.,-2.),(.5,1.)):
            phase=atan(b/a)/2
            scale=sqrt(pi)/2*(a*a+b*b)**(-.25)
            for trig,expected in ((cos,scale*cos(phase)),(sin,scale*sin(phase))):
                self.assertAlmostEqual(simpson(lambda x:exp(-a*x*x)*trig(b*x*x),0,12,12000),
                                       expected,places=8)

    def test_fresnel_tail_bound(self):
        L=sqrt(pi/8)
        for x in (2.,3.,5.):
            c=simpson(lambda t:cos(t*t),0,x)
            s=simpson(lambda t:sin(t*t),0,x)
            self.assertLessEqual(abs(c-L-sin(x*x)/(2*x)),1/(2*x**3))
            self.assertLessEqual(abs(s-L+cos(x*x)/(2*x)),1/(2*x**3))

    def test_damped_sine_integral(self):
        for a,b in ((.5,1.),(1.,-2.),(2.,0.)):
            fun=lambda t: b if t==0 else exp(-a*t)*sin(b*t)/t
            self.assertAlmostEqual(simpson(fun,0,80,16000),atan(b/a),places=8)

    def test_sine_integral_tail(self):
        for x in (2.,5.,10.,20.):
            val=simpson(lambda t:1 if t==0 else sin(t)/t,0,x)
            self.assertLessEqual(abs(val-pi/2+cos(x)/x),2/x**2)

    def test_ci_origin_remainder(self):
        # Ci(x)-log(x)-c0 equals the integral of (cos t-1)/t.
        for x in (.01,.1,.5,1.):
            val=simpson(lambda t:0 if t==0 else -2*sin(t/2)**2/t,0,x)
            self.assertTrue(-x*x/4<=val<=0)

    def test_erf_figure_samples(self):
        import re
        src=(Path(__file__).resolve().parents[4] /
             "chapters/pl/mathematical_analysis_i/34-funkcje-specjalne.tex").read_text(encoding="utf8")
        points=re.search(r"plot coordinates \{([^}]+)\}",src)
        self.assertIsNotNone(points)
        pairs=re.findall(r"\(([-.\d]+),([-.\d]+)\)",points.group(1))
        self.assertGreaterEqual(len(pairs),15)
        for x,y in pairs:
            self.assertLessEqual(abs(float(y)-erf(float(x))),.0000051)


if __name__=="__main__":
    unittest.main()
