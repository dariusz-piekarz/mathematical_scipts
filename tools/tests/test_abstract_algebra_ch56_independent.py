"""AA-56 independent integer-coordinate F4 and G2 root checks."""
import unittest
from itertools import product,combinations
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def roots_f4():
    roots=set(product((-1,1),repeat=4))
    for i in range(4):
        for t in (-2,2):
            a=[0]*4;a[i]=t;roots.add(tuple(a))
    for i,j in combinations(range(4),2):
        for x,y in product((-2,2),repeat=2):
            a=[0]*4;a[i]=x;a[j]=y;roots.add(tuple(a))
    return roots
def roots_g2():
    roots=set()
    for i,j in product(range(3),repeat=2):
        if i!=j:
            a=[0]*3;a[i]=1;a[j]=-1;roots.add(tuple(a))
    for i in range(3):
        a=[-1]*3;a[i]=2
        roots.add(tuple(a));roots.add(tuple(-v for v in a))
    return roots
class RootsTests(unittest.TestCase):
    def check(self,R,n):
        self.assertEqual(len(R),n)
        for a in R:
            self.assertIn(tuple(-x for x in a),R)
            for b in R:
                num=2*dot(a,b);den=dot(a,a)
                self.assertEqual(num%den,0)
                self.assertIn(tuple(y-num//den*x for x,y in zip(a,b)),R)
    def test_f4(self): self.check(roots_f4(),48)
    def test_g2(self): self.check(roots_g2(),12)
if __name__=="__main__": unittest.main()
