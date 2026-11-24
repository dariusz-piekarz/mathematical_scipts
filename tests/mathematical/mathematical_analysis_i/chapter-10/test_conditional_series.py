from fractions import Fraction as F
from itertools import permutations
import unittest

def a(n):
    return F(1 if n%2 else -1,n)

def partial(n):
    return sum((a(j) for j in range(1,n+1)),F(0))

class Chapter10(unittest.TestCase):
    def test_leibniz_brackets(self):
        for k in range(20):
            self.assertLessEqual(partial(2*k),partial(2*k+2))
            self.assertGreaterEqual(partial(2*k+1),partial(2*k+3))
            self.assertEqual(partial(2*k+1)-partial(2*k),F(1,2*k+1))
            self.assertEqual(partial(2*k+1)-partial(2*k+2),F(1,2*k+2))

    def test_figure_values(self):
        # Decimal coordinates in the TikZ figure are rounded to six digits.
        points=["0","1",".5",".833333",".583333",".783333",".616667",".759524",".634524",".745635",".645635"]
        for n,s in enumerate(points):
            self.assertLessEqual(abs(F(s)-partial(n)),F(1,1000000))
        self.assertEqual(partial(9)-partial(10),F(1,10))

    def test_positive_negative_parts(self):
        for n in range(1,30):
            terms=[a(j) for j in range(1,n+1)]
            p=sum(max(x,0) for x in terms)
            q=sum(max(-x,0) for x in terms)
            self.assertEqual(p-q,partial(n))
            self.assertEqual(p+q,sum(abs(x) for x in terms))

    def test_grouping_counterexample_and_identity(self):
        terms=[1,-1]*10
        self.assertEqual([sum(terms[i:i+2]) for i in range(0,20,2)],[0]*10)
        self.assertEqual(sum(terms[:1]),1)
        for ends in [(1,4,7,12),(2,6,12),(12,)]:
            start=0
            blocks=[]
            for end in ends:
                blocks.append(sum(a(n) for n in range(start+1,end+1)))
                start=end
            self.assertEqual(sum(blocks),partial(12))

    def test_absolute_rearrangement_finite_bound(self):
        terms=[F((-1)**n,2**n) for n in range(1,7)]
        S=sum(terms)
        for p in permutations(range(6)):
            used=set()
            t=F(0)
            for i in p:
                used.add(i)
                t+=terms[i]
                if {0,1,2}<=used:
                    self.assertLessEqual(abs(t-S),sum(abs(x) for x in terms[3:]))

    def test_riemann_finite_target_crossings(self):
        # Finite prefixes of the proof's greedy construction, not a convergence proof.
        for target in (F(-1,2),F(0),F(2,3)):
            p=q=0
            s=F(0)
            used=[]
            while s>target:
                q+=1; used.append(2*q); s-=F(1,2*q)
            for k in range(12):
                while True:
                    p+=1; used.append(2*p-1); s+=F(1,2*p-1)
                    if s>target: break
                self.assertTrue(0<s-target<=F(1,2*p-1))
                while True:
                    q+=1; used.append(2*q); s-=F(1,2*q)
                    if s<target: break
                self.assertTrue(0<target-s<=F(1,2*q))
            self.assertEqual(len(used),len(set(used)))
            self.assertEqual(set(used),set(range(1,2*p,2))|set(range(2,2*q+1,2)))

    def test_two_positive_one_negative(self):
        used=[]
        t=F(0)
        for m in range(1,41):
            block=[4*m-3,4*m-1,2*m]
            used.extend(block)
            t+=sum(a(n) for n in block)
            self.assertEqual(t,partial(4*m)+F(1,2)*partial(2*m))
            self.assertEqual(len(set(used)),3*m)

if __name__=="__main__": unittest.main()
