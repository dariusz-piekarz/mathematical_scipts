"""AA-55 independent exact character calculation for exceptional groups."""
import unittest
from fractions import Fraction as F

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def scale(a,c): return (a[0]*c,a[1]*c)
def mul(a,b,D): return (a[0]*b[0]+D*a[1]*b[1],a[0]*b[1]+a[1]*b[0])

class IndependentMcKayTests(unittest.TestCase):
    def test_character_recurrence(self):
        for D,N,zero,one,extra,p,q,r in [
            (2,24,6,8,[],6,8,12),
            (2,48,18,8,[((0,1),6)],8,12,18),
            (5,120,30,20,[((F(1,2),F(1,2)),12),((F(-1,2),F(1,2)),12)],12,20,30)]:
            hist=[((0,0),zero),((2,0),1),((-2,0),1),((1,0),one),((-1,0),one)]
            for t,c in extra: hist.extend([(t,c),(scale(t,-1),c)])
            total=[(0,0) for _ in range(121)]
            for t,m in hist:
                a,b=(1,0),t
                total[0]=add(total[0],scale(a,m))
                total[1]=add(total[1],scale(b,m))
                for k in range(2,121):
                    a,b=b,sub(mul(t,b,D),a)
                    total[k]=add(total[k],scale(b,m))
            for k,v in enumerate(total):
                expected=sum((k-e*r-i*p)%q==0 for e in (0,1)
                    for i in range(max(0,(k-e*r)//p+1)))
                self.assertEqual(v,(N*expected,0))

if __name__=="__main__": unittest.main()
