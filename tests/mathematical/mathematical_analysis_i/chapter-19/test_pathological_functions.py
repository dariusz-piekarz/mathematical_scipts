from fractions import Fraction as F
from math import gcd
from unittest import TestCase, main

def cantor_intervals(n):
    intervals=[(F(0),F(1))]
    for _ in range(n):
        intervals=[part for a,b in intervals
                   for part in [(a,a+(b-a)/3),(b-(b-a)/3,b)]]
    return intervals

def cantor_approx(x,n):
    intervals=cantor_intervals(n)
    for k,(a,b) in enumerate(intervals):
        if x<a:
            return F(k,2**n)
        if x<=b:
            return (k+(x-a)/(b-a))/2**n
    return F(1)

class Chapter19(TestCase):
    def test_thomae_reduced_fraction(self):
        for p in range(-15,16):
            for q in range(1,12):
                x=F(p,q)
                self.assertEqual(gcd(abs(x.numerator),x.denominator),1)
                self.assertEqual(F(1,x.denominator),F(gcd(abs(p),q),q))

    def test_thomae_finite_exception_set(self):
        a=F(2,3)
        for N in range(1,10):
            E={F(p,q) for q in range(1,N+1)
                for p in range(-2*q,3*q+1)
                if a-1<=F(p,q)<=a+1}
            delta=min([F(1)]+[abs(x-a) for x in E if x!=a])
            self.assertGreater(delta,0)
            for q in range(1,2*N+3):
                for p in range(-q,2*q+1):
                    x=F(p,q)
                    if 0<abs(x-a)<delta:
                        self.assertGreater(x.denominator,N)
                        self.assertLess(F(1,x.denominator),F(1,N))

    def test_oscillation_argument_order(self):
        # u_n and v_n are 1/pi times the rational coefficients below.
        for n in range(1,50):
            u=1/(F(1,2)+2*n)
            v=1/(F(3,2)+2*n)
            unext=1/(F(1,2)+2*(n+1))
            self.assertTrue(0<unext<v<u)
            self.assertLess(u,F(1,n))

    def test_cantor_interval_counts(self):
        for n in range(8):
            I=cantor_intervals(n)
            self.assertEqual(len(I),2**n)
            self.assertTrue(all(b-a==F(1,3**n) for a,b in I))
            self.assertEqual(sum(b-a for a,b in I),F(2,3)**n)
            self.assertTrue(all(I[k][1]<I[k+1][0] for k in range(len(I)-1)))

    def test_cantor_endpoints_persist(self):
        for n in range(5):
            ends={x for pair in cantor_intervals(n) for x in pair}
            later={x for pair in cantor_intervals(n+3) for x in pair}
            self.assertTrue(ends<=later)

    def test_cantor_binary_paths(self):
        for n in range(1,7):
            I=cantor_intervals(n)
            for k,(a,b) in enumerate(I):
                bits=[(k>>(n-i))&1 for i in range(1,n+1)]
                self.assertEqual(a,sum(F(2*bit,3**i) for i,bit in enumerate(bits,1)))
                self.assertEqual(b,a+F(1,3**n))

    def test_cantor_approx_endpoints_and_gaps(self):
        for n in range(5):
            I=cantor_intervals(n)
            for k,(a,b) in enumerate(I):
                self.assertEqual(cantor_approx(a,n),F(k,2**n))
                self.assertEqual(cantor_approx(b,n),F(k+1,2**n))
                if k+1<len(I):
                    mid=(b+I[k+1][0])/2
                    self.assertEqual(cantor_approx(mid,n),F(k+1,2**n))
                    self.assertEqual(cantor_approx(mid,n+2),cantor_approx(mid,n))

    def test_cantor_uniform_increment(self):
        for n in range(5):
            for a,b in cantor_intervals(n):
                u=a+(b-a)/3
                v=b-(b-a)/3
                self.assertEqual(cantor_approx(u,n+1)-cantor_approx(u,n),F(1,6*2**n))
                self.assertEqual(cantor_approx(v,n+1)-cantor_approx(v,n),-F(1,6*2**n))
            for i in range(81):
                x=F(i,80)
                self.assertLessEqual(abs(cantor_approx(x,n+1)-cantor_approx(x,n)),F(1,6*2**n))
                self.assertLessEqual(abs(cantor_approx(x,n+3)-cantor_approx(x,n)),F(1,3*2**n))

    def test_cantor_monotonicity(self):
        for n in range(5):
            values=[cantor_approx(F(i,100),n) for i in range(101)]
            self.assertEqual(values,sorted(values))
            self.assertEqual((values[0],values[-1]),(0,1))

    def test_oscillation_ball_inclusion(self):
        p=F(2,3); r=F(1,2)
        for i in range(-5,6):
            q=p+r*F(i,12)
            for j in range(-5,6):
                x=q+r*F(j,12)
                self.assertLess(abs(q-p),r/2)
                self.assertLess(abs(x-q),r/2)
                self.assertLess(abs(x-p),r)

    def test_nested_interval_witness(self):
        a,b=F(0),F(1)
        for n in range(1,20):
            c,d=a+(b-a)/4,a+(b-a)/2
            self.assertTrue(a<c<d<b)
            self.assertLessEqual(d-c,F(1,n))
            a,b=c,d

if __name__ == "__main__": main()
