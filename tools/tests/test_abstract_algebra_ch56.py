"""AA-56 finite Cartan classification and root realizations."""
import unittest
import sympy as s

def path(n): return [(i,i+1,1,1) for i in range(n-1)]
def cartan(n,edges):
    a=2*s.eye(n)
    for i,j,p,q in edges: a[i,j]=-p; a[j,i]=-q
    return a
def star(arms):
    edges=[]; k=0
    for length in arms:
        p=0
        for _ in range(length):
            k+=1; edges.append((p,k,1,1)); p=k
    return cartan(k+1,edges)
class CartanTests(unittest.TestCase):
    def check(self,a,det):
        self.assertEqual(a.det(),det)
        for i in range(1,a.rows+1):
            self.assertGreater(a[:i,:i].det(),0)
    def test_families(self):
        for n in range(1,13):
            self.check(cartan(n,path(n)),n+1)
            if n>=2:
                self.check(cartan(n,path(n)[:-1]+[(n-2,n-1,1,2)]),2)
                self.check(cartan(n,path(n)[:-1]+[(n-2,n-1,2,1)]),2)
            if n>=4: self.check(star((1,1,n-3)),4)
        for n in (6,7,8): self.check(star((1,2,n-4)),9-n)
        self.check(cartan(4,[(0,1,1,1),(1,2,1,2),(2,3,1,1)]),1)
        self.check(cartan(2,[(0,1,1,3)]),1)
    def test_schur_inequalities(self):
        for a in range(1,13):
            for b in range(1,13):
                self.assertEqual(2*a*b<(a+1)*(b+1), min(a,b)==1 or (a,b)==(2,2))
        for a in range(2,20):
            for b in range(a,20):
                for c in range(b,20):
                    self.assertEqual(b*c+a*c+a*b>a*b*c,
                        (a,b)==(2,2) or (a,b)==(2,3) and c in (3,4,5))
if __name__=="__main__": unittest.main()
