"""AA-57 exact matrix Lie algebra regression tests."""
import unittest
import sympy as s

def E(n,i,j):
    a=s.zeros(n);a[i,j]=1;return a
def br(a,b):return a*b-b*a
def span(mats,n):
    if not mats:return []
    return [v.reshape(n,n) for v in s.Matrix.hstack(*(a.reshape(n*n,1) for a in mats)).columnspace()]
def comm(A,B,n):return span([br(a,b) for a in A for b in B],n)
class LieTests(unittest.TestCase):
    def test_triangular_series(self):
        for n in range(1,6):
            N=[E(n,i,j) for i in range(n) for j in range(i+1,n)]
            B=[E(n,i,j) for i in range(n) for j in range(i,n)]
            self.assertEqual(len(comm(B,B,n)),len(N))
            C=N
            for r in range(1,n+1):
                self.assertEqual(len(C),max(0,(n-r)*(n-r+1)//2))
                C=comm(N,C,n)
    def test_sl2(self):
        h=s.diag(1,-1);e=E(2,0,1);f=E(2,1,0)
        self.assertEqual(br(h,e),2*e)
        self.assertEqual(br(h,f),-2*f)
        self.assertEqual(br(e,f),h)
        self.assertEqual(len(comm([h,e,f],[h,e,f],2)),3)
    def test_sp(self):
        for n in range(1,4):
            m=2*n;I=s.eye(n);Z=s.zeros(n)
            J=Z.row_join(I).col_join((-I).row_join(Z))
            B=[E(m,i,j)-E(m,n+j,n+i) for i in range(n) for j in range(n)]
            for i in range(n):
                for j in range(i,n):
                    q=E(m,i,n+j);r=E(m,n+i,j)
                    if i!=j:q+=E(m,j,n+i);r+=E(m,n+j,i)
                    B.extend([q,r])
            self.assertEqual(len(span(B,m)),n*(2*n+1))
            for a in B:
                for b in B:
                    c=br(a,b);self.assertEqual(c.T*J+J*c,s.zeros(m))
if __name__=="__main__":unittest.main()
