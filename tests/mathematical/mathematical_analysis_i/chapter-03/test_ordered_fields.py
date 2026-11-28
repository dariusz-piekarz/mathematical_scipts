from fractions import Fraction as F
import itertools
import unittest

class Chapter03(unittest.TestCase):
    def test_floor_and_density(self):
        vals=[F(i,j) for i in range(-8,9) for j in range(1,6)]
        for x in vals:
            m=x.numerator//x.denominator
            self.assertTrue(m<=x<m+1)
            for n in range(1,9):
                r=F((n*x).numerator//(n*x).denominator,n)
                self.assertTrue(r<=x<r+F(1,n))
        for x,y in itertools.product(vals,repeat=2):
            if x>=y: continue
            n=(1/(y-x)).numerator//(1/(y-x)).denominator+1
            nx=n*x
            m=nx.numerator//nx.denominator
            self.assertTrue(x<F(m+1,n)<y)

    def test_power_bound(self):
        vals=[F(i,4) for i in range(9)]
        for x,y,n in itertools.product(vals,vals,range(1,7)):
            if x>y: continue
            delta=y**n-x**n
            self.assertEqual(delta,(y-x)*sum(y**(n-1-k)*x**k for k in range(n)))
            self.assertTrue(0<=delta<=n*F(2)**(n-1)*(y-x))
            if x<y: self.assertGreater(delta,0)

    def test_root_perturbations(self):
        for s,a,n in itertools.product([F(i,3) for i in range(1,10)], [F(i,2) for i in range(1,13)], range(1,6)):
            M=1+a
            if s>M or s**n==a: continue
            C=n*(M+1)**(n-1)
            if s**n<a:
                h=min(F(1),(a-s**n)/C)/2
                self.assertTrue(s+h<=M+1 and (s+h)**n<a)
            else:
                h=min(s,(s**n-a)/C)/2
                self.assertTrue(0<s-h and (s-h)**n>a)

    def test_sup_product_estimate(self):
        for s,t in itertools.product(map(F,range(4)),repeat=2):
            eps=F(1,7)
            M=1+s+t
            e=max(F(0),s-eps/(2*M))
            g=max(F(0),t-eps/(2*M))
            self.assertTrue(0<=s*t-e*g<eps)

    def test_positive_product_cut_witness(self):
        for x,y in itertools.product([F(i,3) for i in range(1,7)],repeat=2):
            for r in (F(0),x*y/2,x*y*F(99,100)):
                p=(r/y+x)/2
                q=(r/p+y)/2
                self.assertTrue(0<p<x and 0<q<y and r<p*q)

    def test_signed_supremum_counterexample(self):
        E=G={F(-2),F(-1)}
        self.assertEqual(max(E)*max(G),1)
        self.assertEqual(max(e*g for e in E for g in G),4)

    def test_rational_embedding_representatives(self):
        for a,b,c,d in itertools.product(range(-3,4),range(1,5),range(-3,4),range(1,5)):
            x,y=F(a,b),F(c,d)
            self.assertEqual(F(2*a,2*b),x)
            self.assertEqual(F(a*d+b*c,b*d),x+y)
            self.assertEqual(F(a*c,b*d),x*y)
            self.assertEqual(a*d<c*b,x<y)

if __name__=="__main__": unittest.main()
