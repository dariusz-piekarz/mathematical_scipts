from fractions import Fraction as F
from unittest import TestCase, main

class Chapter16(TestCase):
    def test_square_witness(self):
        for n in range(1,101):
            x,y=F(n),F(n)+F(1,n)
            self.assertEqual(y-x,F(1,n))
            self.assertEqual(y*y-x*x,2+F(1,n*n))

    def test_square_bounded_lipschitz(self):
        for R in [F(1,3),F(1),F(4)]:
            points=[R*F(i,10) for i in range(-10,11)]
            for x in points:
                for y in points:
                    self.assertLessEqual(abs(x*x-y*y),2*R*abs(x-y))

    def test_reciprocal_witness(self):
        for n in range(1,101):
            x,y=F(1,n),F(1,n+1)
            self.assertEqual(x-y,F(1,n*(n+1)))
            self.assertEqual(abs(1/x-1/y),1)

    def test_sqrt_holder(self):
        points=[F(i,7) for i in range(21)]
        for a in points:
            for b in points:
                self.assertLessEqual((a-b)**2,abs(a*a-b*b))
        for n in range(1,101):
            self.assertEqual(F(1,n)/F(1,n*n),n)

    def test_no_holder_rational_witness(self):
        for m in range(1,9):
            for n in range(m,15):
                x=F(1,2**(n*n))
                self.assertLessEqual(x,F(1,2**n)**m)
                self.assertGreaterEqual(F(2**n,n),F(n-1,2))

    def test_power_root_bound(self):
        for m in range(1,15):
            for u in [F(0),F(1,3),F(2)]:
                t=(1+u)**m
                self.assertLessEqual(1+u,1+(t-1)/m)

    def test_power_ratio_bound(self):
        for m in range(1,7):
            for j in range(m+1):
                for a,b in [(F(1,3),F(2,3)),(F(1,2),F(3,2)),(F(2),F(5))]:
                    s,t=a**m,b**m
                    self.assertLessEqual(a**j,b**j)
                    self.assertLessEqual(b**j,t/s*a**j)

    def test_discrete_modulus(self):
        for n in range(1,101):
            self.assertEqual(int(n+1!=1),1)
            self.assertEqual(abs(n+1-1),n)

    def test_product_estimate(self):
        M=F(2)
        points=[F(i,2) for i in range(-4,5)]
        for a,b in zip(points, reversed(points)):
            for c,d in zip(points[1:],points[:-1]):
                self.assertLessEqual(abs(a*b-c*d),M*abs(a-c)+M*abs(b-d))

    def test_reciprocal_estimate(self):
        m=F(1,3)
        points=[F(i,3) for i in range(-9,10) if i!=0]
        for a in points:
            for b in points:
                self.assertLessEqual(abs(1/a-1/b),abs(a-b)/(m*m))

    def test_extension_triangle_budget(self):
        for delta in [F(1,100),F(1),F(7,2)]:
            p,q=F(0),delta/4
            for n in range(4,15):
                x,y=p-delta/n,q+delta/n
                self.assertLess(abs(x-p),delta/3)
                self.assertLess(abs(y-q),delta/3)
                self.assertLess(abs(x-y),delta)

    def test_incomplete_extension_witness(self):
        for n in range(1,101):
            x=F(1,n+1)
            self.assertTrue(0<x<1)
            self.assertLess(x,F(1,n))

    def test_power_positive_bounds(self):
        for n in range(1,10):
            for m in range(n+1):
                for a in [F(1,3),F(1),F(2)]:
                    t=a**n
                    self.assertLessEqual(min(t,1),a**m)
                    self.assertLessEqual(a**m,max(t,1))
                    self.assertGreater(a**m,0)
                    self.assertEqual(a**m*(1/a)**m,1)

    def test_extension_holder_distant_pairs(self):
        # f(x)=sqrt(x); exact square-root values at rational squares.
        for p,q in [(F(0),F(4)),(F(1),F(7)),(F(2),F(20))]:
            for n in range(1,21):
                a,b=p+F(1,n),q+F(1,2*n)
                self.assertLessEqual((a-b)**2,abs(a*a-b*b))
            self.assertLessEqual((p-q)**2,abs(p*p-q*q))

if __name__ == "__main__": main()
