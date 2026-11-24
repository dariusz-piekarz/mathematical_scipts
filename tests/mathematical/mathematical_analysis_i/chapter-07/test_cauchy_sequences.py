from fractions import Fraction as F
from math import isqrt
import itertools
import unittest

class Chapter07(unittest.TestCase):
    def test_cluster_extraction_indices(self):
        # Alternating sequence with even entries 1/k and odd entries k.
        old=0
        for k in range(1,31):
            n=2*(k+1)
            self.assertGreater(n,old)
            self.assertLess(F(1,n//2),F(1,k))
            old=n

    def test_harmonic_counterexample(self):
        for n in range(1,101):
            self.assertGreaterEqual(sum(F(1,j) for j in range(n+1,2*n+1)),F(1,2))
            self.assertEqual(sum(F(1,j) for j in range(1,n+2))-sum(F(1,j) for j in range(1,n+1)),F(1,n+1))

    def test_rational_sqrt2_bracket(self):
        for n in range(1,101):
            k=isqrt(2*n*n)
            self.assertLess(k*k,2*n*n)
            self.assertGreater((k+1)**2,2*n*n)
            for m in (n,n+1,2*n):
                l=isqrt(2*m*m)
                self.assertLess(abs(F(k,n)-F(l,m)),max(F(1,n),F(1,m)))

    def test_cauchy_with_subsequence_estimate(self):
        vals=[F(i,8) for i in range(-8,9)]
        eps=F(1,2)
        for x,y,a in itertools.product(vals,repeat=3):
            if abs(x-y)<eps/2 and abs(y-a)<eps/2:
                self.assertLess(abs(x-a),eps)

    def test_product_embedding_distance(self):
        for x,y,p,q in itertools.product(range(-2,3),repeat=4):
            a=(p,x,q); b=(p,y,q)
            self.assertEqual(max(abs(u-v) for u,v in zip(a,b)),abs(x-y))
            self.assertEqual(sum(abs(u-v) for u,v in zip(a,b)),abs(x-y))

    def test_bounded_function_uniform_witness(self):
        S=[F(i,10) for i in range(11)]
        eps=F(1,7)
        n=15
        f=lambda t: t*t
        fn=lambda t: t*t+t/n
        self.assertLess(max(abs(fn(t)-f(t)) for t in S),eps/2)
        self.assertLessEqual(max(abs(f(t)) for t in S),max(abs(fn(t)) for t in S)+1)

if __name__=="__main__": unittest.main()
