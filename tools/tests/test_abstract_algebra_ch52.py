"""AA-52: exact abstract lift orders and dicyclic normal forms."""
import itertools
import unittest
from math import lcm
from collections import Counter

def mul(a,b,n):
    k,e=a
    l,f=b
    return ((k+(-1)**e*l+n*(e*f))%(2*n),(e+f)%2)

def order(g,n):
    h=(0,0)
    for k in range(1,4*n+1):
        h=mul(h,g,n)
        if h==(0,0):
            return k
    raise AssertionError(g)

class AA52BinaryTests(unittest.TestCase):
    def test_dicyclic_normal_forms(self):
        for n in range(2,9):
            G=list(itertools.product(range(2*n),range(2)))
            for a,b,c in itertools.product(G,repeat=3):
                self.assertEqual(mul(mul(a,b,n),c,n),mul(a,mul(b,c,n),n))
            self.assertEqual([g for g in G if order(g,n)==2],[(n,0)])
            self.assertEqual(order((1,0),n),2*n)
            self.assertTrue(all(order((k,1),n)==4 for k in range(2*n)))
    def test_quotient_and_relations(self):
        for n in range(2,13):
            G=list(itertools.product(range(2*n),range(2)))
            for a,b in itertools.product(G,repeat=2):
                k,e=a
                l,f=b
                p,q=mul(a,b,n)
                self.assertEqual((p%n,q),((k+(-1)**e*l)%n,(e+f)%2))
            self.assertEqual(mul((0,1),(0,1),n),(n,0))
            self.assertEqual(mul(mul((0,1),(1,0),n),(n,1),n),(2*n-1,0))
    def test_binary_order_histograms(self):
        for d,expected in [
            ({1:1,2:3,3:8},{1:1,2:1,3:8,4:6,6:8}),
            ({1:1,2:9,3:8,4:6},{1:1,2:1,3:8,4:18,6:8,8:12}),
            ({1:1,2:15,3:20,5:24},{1:1,2:1,3:20,4:30,5:24,6:20,10:24})]:
            out=Counter()
            for m,c in d.items():
                if m%2: out[m]+=c; out[2*m]+=c
                else: out[2*m]+=2*c
            self.assertEqual(dict(out),expected)
    def test_a5_five_cycle_classes(self):
        def mul(p,q): return tuple(p[i] for i in q)
        def inv(p): return tuple(p.index(i) for i in range(5))
        def even(p): return sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2==0
        G=[p for p in itertools.permutations(range(5)) if even(p)]
        c=(1,2,3,4,0)
        c2=mul(c,c)
        cls=lambda g:{mul(mul(p,g),inv(p)) for p in G}
        A,B=cls(c),cls(c2)
        self.assertEqual((len(A),len(B)),(12,12))
        self.assertFalse(A&B)
        t=(1,0,2,3,4)
        self.assertEqual({mul(mul(t,p),t) for p in A},B)
if __name__=="__main__": unittest.main()
