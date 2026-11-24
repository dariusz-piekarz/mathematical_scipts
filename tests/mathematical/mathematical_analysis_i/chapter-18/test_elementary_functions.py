from fractions import Fraction as F
from math import factorial
from unittest import TestCase, main

def E(x,N):
    return sum((x**n/factorial(n) for n in range(N+1)),F(0))

def C(x,N):
    return sum(((-1)**n*x**(2*n)/factorial(2*n) for n in range(N+1)),F(0))

def S(x,N):
    return sum(((-1)**n*x**(2*n+1)/factorial(2*n+1) for n in range(N+1)),F(0))

class Chapter18(TestCase):
    def test_exponential_majorant(self):
        for R in [F(1,2),F(2),F(7,3)]:
            for n in range(1,20):
                if n+1>=2*R:
                    self.assertLessEqual((R**(n+1)/factorial(n+1))/(R**n/factorial(n)),F(1,2))

    def test_cauchy_coefficients(self):
        for n in range(15):
            for x,y in [(F(1,3),F(-2,5)),(F(-3),F(2))]:
                self.assertEqual(sum(x**k*y**(n-k)/factorial(k)/factorial(n-k) for k in range(n+1)),(x+y)**n/factorial(n))

    def test_local_power_difference(self):
        for n in range(1,12):
            for x,y in [(F(-1),F(2)),(F(1,3),F(-2,3))]:
                R=max(abs(x),abs(y))
                self.assertLessEqual(abs(x**n-y**n),n*R**(n-1)*abs(x-y))

    def test_positive_exp_lower_bound(self):
        for n in range(1,10):
            for x in [F(1,5),F(1),F(3)]:
                self.assertGreaterEqual(E(x,n),1+x)

    def test_rational_power_consistency(self):
        for t in [F(2,3),F(2),F(5)]:
            for m in range(-4,5):
                for n in range(1,5):
                    a=t**n
                    self.assertEqual((t**m)**n,a**m)

    def test_trig_series_coefficients(self):
        for n in range(16):
            # exp(it) exp(-it): coefficient of t^n must vanish for n>0.
            coef=sum(F((-1)**(n-k),factorial(k)*factorial(n-k)) for k in range(n+1))
            self.assertEqual(coef,int(n==0))
            if n%2==0:
                # Parity decomposition of exp(it).
                self.assertEqual(C(F(0),n),1)
                self.assertEqual(S(F(0),n),0)

    def test_pi_sign_witnesses(self):
        self.assertEqual(C(F(2),2),F(-1,3))
        for k in range(1,21):
            x=F(k,10)
            self.assertGreater(x-x**3/6,0)
            for n in range(5):
                self.assertLess(x*x/F((2*n+2)*(2*n+3)),1)
        for n in range(1,10):
            self.assertLess(F(4,(2*n+1)*(2*n+2)),1)

    def test_hyperbolic_identity_and_tanh_inverse(self):
        for t in [F(1,7),F(1),F(3),F(9,2)]:
            c=(t+1/t)/2; s=(t-1/t)/2
            self.assertEqual(c*c-s*s,1)
            y=s/c
            self.assertTrue(-1<y<1)
            self.assertEqual((1+y)/(1-y),t*t)
            if s:
                v=c/s
                self.assertGreater(abs(v),1)
                self.assertEqual((v+1)/(v-1),t*t)

    def test_hyperbolic_quadratic_equations(self):
        for t in [F(1,3),F(1),F(7,2)]:
            s=(t-1/t)/2; c=(t+1/t)/2
            self.assertEqual(t*t-2*s*t-1,0)
            self.assertEqual(t*t-2*c*t+1,0)

    def test_small_argument_estimates(self):
        for x in [F(1,2),F(-1,3),F(1,100)]:
            for N in range(2,10):
                self.assertLessEqual(abs((E(x,N)-1)/x-1),abs(x)*sum(F(1,factorial(n)) for n in range(2,N+1)))
                self.assertLessEqual(abs(S(x,N)/x-1),x*x*sum(F(1,factorial(2*n+1)) for n in range(1,N+1)))

    def test_argument_residue_classes(self):
        for n in range(1,15):
            for m in range(-30,31):
                k=m%n
                self.assertTrue(0<=k<n)
                self.assertEqual((m-k)%n,0)
            for j in range(n):
                for k in range(n):
                    self.assertEqual((j-k)%n==0,j==k)

    def test_trig_addition_coefficients(self):
        # Homogeneous coefficients after substituting arguments x*t and y*t.
        for x,y in [(F(1,3),F(-2,5)),(F(-3),F(2))]:
            for n in range(15):
                cc=ss=sc=cs=F(0)
                for k in range(n+1):
                    j=n-k
                    a=x**k/factorial(k)
                    b=y**j/factorial(j)
                    if k%2==0 and j%2==0:
                        cc+=(-1)**(k//2+j//2)*a*b
                    elif k%2==1 and j%2==1:
                        ss+=(-1)**(k//2+j//2)*a*b
                    elif k%2==1:
                        sc+=(-1)**(k//2+j//2)*a*b
                    else:
                        cs+=(-1)**(k//2+j//2)*a*b
                expected=(-1)**(n//2)*(x+y)**n/factorial(n)
                self.assertEqual(cc-ss,expected if n%2==0 else 0)
                self.assertEqual(sc+cs,expected if n%2==1 else 0)

    def test_rational_power_root_witness(self):
        for root in [F(2,3),F(1),F(5,2)]:
            for n in range(1,7):
                a=root**n
                for m in range(-5,6):
                    candidate=root**m
                    self.assertGreater(candidate,0)
                    self.assertEqual(candidate**n,a**m)

if __name__ == "__main__": main()
