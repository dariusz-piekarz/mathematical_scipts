from fractions import Fraction as F
from unittest import TestCase, main

class Chapter15(TestCase):
    def test_isolated_integer_points(self):
        for p in range(-10,11):
            self.assertEqual([x for x in range(-20,21) if abs(x-p)<F(1,2)],[p])

    def test_changed_value_at_zero(self):
        for n in range(1,101):
            x=F(1,n)
            self.assertEqual(abs((x+1)-7),6-x)
            self.assertEqual(abs((x+1)-1),x)

    def test_relative_open_interval(self):
        points=[F(n,20) for n in range(-20,41)]
        for x in points:
            self.assertEqual(0<=x<F(1,2),0<=x<=1 and -1<x<F(1,2))
            if 0<=x<F(1,2):
                r=F(1,2)-x
                self.assertTrue(all(0<=y<F(1,2) for y in points if 0<=y<=1 and abs(y-x)<r))

    def test_preimage_complement(self):
        A=set(range(-10,11)); Y=set(range(101)); V={0,1,4,9}
        f=lambda x:x*x
        self.assertEqual(A-{x for x in A if f(x) in V},{x for x in A if f(x) in Y-V})

    def test_closed_image_counterexample(self):
        for n in range(1,101):
            y=F(1,1+n*n)
            self.assertTrue(0<y<F(1,n))

    def test_local_nonzero_and_bounds(self):
        for b in [F(1),F(-1),F(1,8),F(-1,8)]:
            for n in range(3,20):
                for sign in [-1,1]:
                    g=b+sign*abs(b)/n
                    self.assertLess(abs(g-b),abs(b)/2)
                    self.assertGreater(abs(g),abs(b)/2)
                    self.assertGreater(g*b,0)
                    self.assertLess(abs(g),abs(b)+1)

    def test_extrema_counterexamples(self):
        for n in range(2,101):
            x=F(1,n); y=1-x
            self.assertTrue(0<x<1 and 0<y<1)
            self.assertEqual(1/x,n)
            self.assertEqual(1-y,x)
        def h(x): return x if x<1 else F(0)
        self.assertEqual(h(F(1)),0)
        for n in range(2,101):
            self.assertEqual(h(1-F(1,n)),1-F(1,n))

    def test_ivt_polynomial(self):
        P=lambda x:x*x*x+x-1
        self.assertEqual(P(F(0)),-1)
        self.assertEqual(P(F(1)),1)
        lo,hi=F(6823278,10**7),F(6823279,10**7)
        self.assertLess(P(lo),0)
        self.assertGreater(P(hi),0)
        vals=[F(n,10) for n in range(-20,21)]
        for x in vals:
            for y in vals:
                if x<y:
                    self.assertEqual(P(y)-P(x),(y-x)*(y*y+x*y+x*x+1))
                    self.assertGreater(P(y)-P(x),0)

    def test_supremum_proof_right_witness(self):
        for c in [F(0),F(1,3),F(9,10)]:
            for delta in [F(1,100),F(1,2),F(3)]:
                x=c+min(delta,1-c)/2
                self.assertTrue(c<x<=1)
                self.assertLess(x-c,delta)

    def test_discrete_inverse_counterexample(self):
        p=F(3)
        for n in range(1,101):
            x=p+F(1,n)
            self.assertEqual(abs(x-p),F(1,n))
            self.assertEqual(int(x!=p),1)

    def test_square_strict_increase(self):
        vals=[F(n,20) for n in range(21)]
        for x in vals:
            self.assertTrue(0<=x*x<=1)
            for y in vals:
                if x<y:
                    self.assertEqual(y*y-x*x,(y-x)*(y+x))
                    self.assertGreater(y*y-x*x,0)

if __name__ == "__main__": main()
