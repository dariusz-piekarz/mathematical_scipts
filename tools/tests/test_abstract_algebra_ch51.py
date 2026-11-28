"""AA-51: finite orbit counts and permutation-group checks."""
import itertools as it
import unittest
from fractions import Fraction as Q
from collections import Counter
from math import lcm

def mul(p,q):
    return tuple(p[i] for i in q)

def order(p):
    seen=set()
    lengths=[]
    for i in range(len(p)):
        if i in seen:
            continue
        j=i
        n=0
        while j not in seen:
            seen.add(j)
            n+=1
            j=p[j]
        lengths.append(n)
    return lcm(*lengths)

def even(p):
    return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2==0

class AA51OrbitTests(unittest.TestCase):
    def test_signatures(self):
        for N in range(2,121):
            div=[i for i in range(2,N+1) if N%i==0]
            actual=set()
            for r in (2,3):
                for ms in it.combinations_with_replacement(div,r):
                    if sum(Q(1)-Q(1,m) for m in ms)==2-Q(2,N):
                        actual.add(ms)
            expected={(N,N)}
            if N%2==0 and N>=4:
                expected.add((2,2,N//2))
            extra={12:(2,3,3),24:(2,3,4),60:(2,3,5)}
            if N in extra:
                expected.add(extra[N])
            self.assertEqual(actual,expected,N)
    def test_a4_s4_a5_element_orders(self):
        for n,alt,expected in [(4,True,{1:1,2:3,3:8}),
             (4,False,{1:1,2:9,3:8,4:6}),
             (5,True,{1:1,2:15,3:20,5:24})]:
            G=[p for p in it.permutations(range(n)) if not alt or even(p)]
            self.assertEqual(dict(Counter(map(order,G))),expected)
    def test_a5_centralizers_and_klein(self):
        G=[p for p in it.permutations(range(5)) if even(p)]
        invol=[p for p in G if order(p)==2]
        V=set()
        for p in invol:
            C=frozenset(q for q in G if mul(p,q)==mul(q,p))
            self.assertEqual(len(C),4)
            self.assertEqual(sorted(map(order,C)),[1,2,2,2])
            V.add(C)
        self.assertEqual(len(V),5)
        self.assertEqual(sorted(sum(p in C for C in V) for p in invol),[1]*15)
    def test_minimal_orbits(self):
        for N,ms,want in [(12,(2,3,3),4),(24,(2,3,4),6),(60,(2,3,5),12)]:
            self.assertEqual(min(N//m for m in ms),want)
            self.assertEqual(sum(N//m*(m-1) for m in ms),2*(N-1))
if __name__=="__main__":
    unittest.main()
