"""AA-54 independent integer polynomial checks of Molien rational identities."""
import unittest

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): c[i+j]+=v*w
    return c
def add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def prod(xs):
    p=[1]
    for x in xs: p=mul(p,x)
    return p
def factor(n): return [1]+[0]*(n-1)+[-1]
def equal(a,b): return all(x==0 for x in add(a,[-v for v in b]))

class AA54IntegerTests(unittest.TestCase):
    def test_molien(self):
        den=[[1,-2,1],[1,1],[1,1,1],[1,0,1],[1,1,1,1,1]]
        for N,c0,c1,c2,c5,d1,d2,d3 in [(24,6,8,0,0,3,4,6),(48,18,8,6,0,4,6,9),(120,30,20,0,12,6,10,15)]:
            nums=[[2,2],[c0],[2*c1,2*c1],[2*c2,2*c2],[c5*k for k in (4,6,6,4)]]
            numerator=[0]
            for i,num in enumerate(nums):
                numerator=add(numerator,mul(num,prod(den[:i]+den[i+1:])))
            left=mul(numerator,prod([factor(d1),factor(d2)]))
            right=[N*v for v in mul([1]+[0]*(d3-1)+[1],prod(den))]
            self.assertTrue(equal(left,right),N)
if __name__=="__main__": unittest.main()
