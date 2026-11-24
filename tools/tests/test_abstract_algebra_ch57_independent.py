"""AA-57 independent integer matrix checks of Engel and positive characteristic."""
import unittest
def zero(n):return [[0]*n for _ in range(n)]
def unit(n,i,j):
    a=zero(n);a[i][j]=1;return a
def mul(a,b):
    return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def br(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(mul(a,b),mul(b,a))]
class IndependentLieTests(unittest.TestCase):
    def test_ad_nilpotence(self):
        for n in range(1,9):
            x=zero(n)
            for i in range(n-1):x[i][i+1]=1
            for i in range(n):
                for j in range(n):
                    a=unit(n,i,j)
                    for _ in range(2*n-1):a=br(x,a)
                    self.assertEqual(a,zero(n))
    def test_characteristic_p(self):
        for p in (2,3,5,7,11,13):
            x=zero(p);y=zero(p)
            for i in range(p-1):x[i+1][i]=1;y[i][i+1]=i+1
            self.assertEqual([[v%p for v in r] for r in br(y,x)],[[int(i==j) for j in range(p)] for i in range(p)])
if __name__=="__main__":unittest.main()
