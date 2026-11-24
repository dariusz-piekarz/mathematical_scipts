from fractions import Fraction as F
import itertools
import unittest

class Chapter08(unittest.TestCase):
    def test_oscillating_tail_extrema(self):
        # For this specific infinite sequence each tail extremum is
        # attained at its first positive or negative term.
        a=lambda n: (1+F(1,(n+1)//2))*(1 if n%2 else -1)
        for N in range(1,51):
            k=(N+1)//2
            lo=-1-F(1,k)
            hi=1+F(1,k+(N%2==0))
            self.assertEqual(min(a(N),a(N+1)),lo)
            self.assertEqual(max(a(N),a(N+1)),hi)
            self.assertTrue(all(lo<=a(n)<=hi for n in range(N,N+100)))

    def test_tail_extrema_order(self):
        for a in itertools.product(range(-2,3),repeat=4):
            lo=[min(a[n:]) for n in range(4)]
            hi=[max(a[n:]) for n in range(4)]
            self.assertEqual(lo,sorted(lo))
            self.assertEqual(hi,sorted(hi,reverse=True))
            for n,m in itertools.product(range(4),repeat=2):
                self.assertLessEqual(lo[n],hi[m])
            self.assertEqual(min(-v for v in a),-max(a))

    def test_periodic_sum_bounds(self):
        # Infinite periodic sequences: each tail contains every value
        # in a period. The finite computation is exact for these examples.
        periods=list(itertools.product(range(-2,3),repeat=3))
        for a,b in itertools.product(periods,repeat=2):
            la,La,lb,Lb=min(a),max(a),min(b),max(b)
            c=[x+y for x,y in zip(a,b)]
            self.assertLessEqual(la+lb,min(c))
            self.assertLessEqual(min(c),min(la+Lb,La+lb))
            self.assertLessEqual(max(La+lb,la+Lb),max(c))
            self.assertLessEqual(max(c),La+Lb)

    def test_scaling_sign(self):
        for a in itertools.product(range(-2,3),repeat=3):
            for c in range(-3,4):
                v=[c*x for x in a]
                self.assertEqual(min(v),c*(min(a) if c>=0 else max(a)))
                self.assertEqual(max(v),c*(max(a) if c>=0 else min(a)))

    def test_nonnegative_product_bounds(self):
        p=list(itertools.product(range(3),repeat=3))
        for a,b in itertools.product(p,repeat=2):
            c=[x*y for x,y in zip(a,b)]
            self.assertLessEqual(min(a)*min(b),min(c))
            self.assertLessEqual(max(c),max(a)*max(b))

    def test_counterexamples_to_equality_and_sign(self):
        a=(0,2); b=(2,0)
        self.assertEqual(tuple(x+y for x,y in zip(a,b)),(2,2))
        self.assertEqual(tuple(x*y for x,y in zip(a,b)),(0,0))
        self.assertEqual(max(x*y for x,y in zip((-1,-1),(-1,1))),1)
        self.assertEqual(max((-1,-1))*max((-1,1)),-1)

    def test_subsequence_witnesses(self):
        for k in range(1,100):
            self.assertLess(abs(1+F(1,k+1)-1),F(1,k))
            self.assertLess(abs(-1-F(1,k+1)+1),F(1,k))
            self.assertGreater(2*(k+1),2*k)
            self.assertGreater(k+1,k)

if __name__=="__main__": unittest.main()
