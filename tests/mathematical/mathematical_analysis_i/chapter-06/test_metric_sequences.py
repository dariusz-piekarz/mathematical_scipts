from fractions import Fraction as F
import itertools
import unittest

V=list(itertools.product(range(-1,2),repeat=3))
def d1(x,y): return sum(abs(a-b) for a,b in zip(x,y))
def dinf(x,y): return max(abs(a-b) for a,b in zip(x,y))

class Chapter06(unittest.TestCase):
    def test_metrics_and_comparison(self):
        for x,y in itertools.product(V,repeat=2):
            for d in (d1,dinf):
                self.assertGreaterEqual(d(x,y),0)
                self.assertEqual(d(x,y)==0,x==y)
                self.assertEqual(d(x,y),d(y,x))
            self.assertTrue(dinf(x,y)<=d1(x,y)<=3*dinf(x,y))
        for x,y,z in itertools.product(V,repeat=3):
            for d in (d1,dinf):
                self.assertLessEqual(d(x,z),d(x,y)+d(y,z))

    def test_distance_estimate(self):
        vals=range(-4,5)
        for x,y,u,v in itertools.product(vals,repeat=4):
            self.assertLessEqual(abs(abs(x-u)-abs(y-v)),abs(x-y)+abs(u-v))

    def test_epsilon_witness(self):
        for e in (F(i,j) for i in range(1,12) for j in range(1,30)):
            r=1/e
            N=r.numerator//r.denominator+1
            for n in range(N,N+10):
                self.assertLess(F(1,n),e)

    def test_coordinate_counterexample(self):
        for n in range(1,15):
            en=tuple(int(j==n) for j in range(1,16))
            self.assertEqual(dinf(en,(0,)*15),1)
            for j in range(1,n):
                self.assertEqual(en[j-1],0)

    def test_bernoulli_and_geometric_bound(self):
        for r in (F(i,j) for i in range(1,5) for j in range(1,8)):
            q=1/(1+r)
            for n in range(1,21):
                self.assertGreaterEqual((1+r)**n,1+n*r)
                self.assertLessEqual(q**n,1/(1+n*r))

    def test_product_estimate(self):
        vals=[F(i,3) for i in range(-3,4)]
        for xn,yn,x,y in itertools.product(vals,repeat=4):
            M=max(F(1),abs(xn),abs(y))
            self.assertLessEqual(abs(xn*yn-x*y),M*(abs(yn-y)+abs(xn-x)))

    def test_reciprocal_estimate(self):
        vals=[F(i,8) for i in range(-16,17)]
        for yn,y in itertools.product(vals,repeat=2):
            if not y or abs(yn-y)>=abs(y)/2: continue
            self.assertGreater(abs(yn),abs(y)/2)
            self.assertLessEqual(abs(1/yn-1/y),2*abs(yn-y)/abs(y)**2)

    def test_squeeze_example(self):
        for n in range(1,51):
            self.assertTrue(-F(1,n)<=F((-1)**n,n)<=F(1,n))

    def test_euclidean_metric_exact(self):
        # Square all nonnegative quantities; no floating-point square roots.
        def sq(u): return sum(a*a for a in u)
        for u,v in itertools.product(V,repeat=2):
            dot=sum(a*b for a,b in zip(u,v))
            self.assertEqual(sq(u)*sq(v)-dot*dot,
                sum((u[j]*v[k]-u[k]*v[j])**2 for j in range(3) for k in range(j+1,3)))
            self.assertGreaterEqual(sq(u)*sq(v)-dot*dot,0)
            w=tuple(a+b for a,b in zip(u,v))
            delta=sq(w)-sq(u)-sq(v)
            self.assertTrue(delta<=0 or delta*delta<=4*sq(u)*sq(v))
        for x,y in itertools.product(V,repeat=2):
            q=sq(tuple(a-b for a,b in zip(x,y)))
            self.assertTrue(dinf(x,y)**2<=q<=3*dinf(x,y)**2)

    def test_zero_denominator_limit_examples(self):
        for n in range(1,51):
            a,b=F(1,n),F(1,n*n)
            self.assertEqual(a/a,1)
            self.assertEqual(b/a,a)
            self.assertEqual(a/b,n)

if __name__=="__main__": unittest.main()
