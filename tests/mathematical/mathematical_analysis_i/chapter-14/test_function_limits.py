from fractions import Fraction as F
from unittest import TestCase, main

class Chapter14(TestCase):
    def test_accumulation_witnesses(self):
        for n in range(1,101):
            x=F(1,n+1)
            self.assertTrue(0<x<F(1,n))
            self.assertTrue(0<1-(1-x)<F(1,n))

    def test_point_value_irrelevant(self):
        def f(x): return x+1 if x else F(7)
        self.assertEqual(f(F(0)),7)
        for n in range(1,101):
            for x in [F(1,n+1),-F(1,n+1)]:
                self.assertEqual(abs(f(x)-1),abs(x))
                self.assertLess(abs(f(x)-1),F(1,n))

    def test_two_directions(self):
        def f(x,y): return x*x/(x*x+y*y)
        for n in range(1,101):
            x=F(1,n)
            self.assertEqual(f(x,0),1)
            self.assertEqual(f(0,x),0)

    def test_composition_exception(self):
        def f(x): return 0
        def g(y): return 0 if y else 1
        for n in range(1,101):
            x=F(1,n)
            self.assertEqual(f(x),0)
            self.assertEqual(g(x),0)
            self.assertEqual(g(f(x)),1)

    def test_incomplete_target_cauchy_witness(self):
        for n in range(1,30):
            delta=F(1,n)
            x,z=delta/2,delta/3
            self.assertTrue(0<x<1 and 0<z<1)
            self.assertLess(abs(x-z),delta)

    def test_denominator_nonzero(self):
        for b in [F(1), F(-1), F(1,8), F(-1,8)]:
            for n in range(3,20):
                for sign in [-1,1]:
                    g=b+sign*abs(b)/n
                    self.assertLess(abs(g-b),abs(b)/2)
                    self.assertGreater(abs(g),abs(b)/2)

    def test_cancelled_rational_function(self):
        for n in range(1,101):
            for x in [2+F(1,n),2-F(1,n)]:
                self.assertNotEqual(x,2)
                self.assertEqual((x*x-4)/(x-2),x+2)

    def test_squeeze(self):
        for n in range(1,30):
            for x in [F(1,n),-F(1,n)]:
                for u in [F(-1),F(-1,3),F(0),F(1,3),F(1)]:
                    self.assertLessEqual(-abs(x),x*u)
                    self.assertLessEqual(x*u,abs(x))

    def test_one_sided_sign(self):
        for n in range(1,101):
            for x,expected in [(F(1,n),1),(-F(1,n),-1)]:
                self.assertEqual((x>0)-(x<0),expected)

    def test_reciprocal_infinite_limits(self):
        for M in [F(1,3),F(1),F(10),F(100)]:
            x=1/(2*M)
            self.assertGreater(1/x,M)
            self.assertLess(1/(-x),-M)
        for eps in [F(1,3),F(1,10),F(1,100)]:
            for x in [2/eps,-2/eps]:
                self.assertLess(abs(1/x),eps)
        for k in range(1,30):
            M=F(k*k); x=F(1,2*k)
            self.assertGreater(1/(x*x),M)

if __name__ == "__main__": main()
