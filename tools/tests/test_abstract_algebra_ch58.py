"""AA-58 exact Killing forms in classical matrix models."""
import unittest
import sympy as s
def E(n,i,j):
    a=s.zeros(n);a[i,j]=1;return a
def br(a,b):return a*b-b*a
def basis(t,n):
    if t=="gl":return [E(n,i,j) for i in range(n) for j in range(n)]
    if t=="sl":return [E(n,i,j) for i in range(n) for j in range(n) if i!=j]+[E(n,i,i)-E(n,i+1,i+1) for i in range(n-1)]
    if t=="so":return [E(n,i,j)-E(n,j,i) for i in range(n) for j in range(i+1,n)]
    m=2*n
    B=[E(m,i,j)-E(m,n+j,n+i) for i in range(n) for j in range(n)]
    for i in range(n):
        for j in range(i,n):
            q=E(m,i,n+j);r=E(m,n+i,j)
            if i!=j:q+=E(m,j,n+i);r+=E(m,n+j,i)
            B.extend([q,r])
    return B
class KillingTests(unittest.TestCase):
    def test_classical(self):
        for t,ns in [("gl",range(1,5)),("sl",range(2,5)),("so",range(2,6)),("sp",range(1,4))]:
            for n in ns:
                B=basis(t,n);d=len(B);m=B[0].rows
                M=s.Matrix.hstack(*(a.reshape(m*m,1) for a in B))
                pivots=M.T.rref()[1]
                L=M[list(pivots),:].inv()
                A=[L*s.Matrix.hstack(*(br(x,y).reshape(m*m,1) for y in B))[list(pivots),:] for x in B]
                for i,x in enumerate(B):
                    for j,y in enumerate(B):
                        expected={"gl":2*n,"sl":2*n,"so":n-2,"sp":2*n+2}[t]*s.trace(x*y)
                        if t=="gl":expected-=2*s.trace(x)*s.trace(y)
                        self.assertEqual(s.trace(A[i]*A[j]),expected,(t,n,i,j))
    def test_sl2(self):
        B=[s.diag(1,-1),E(2,0,1),E(2,1,0)]
        K=s.Matrix([[4*s.trace(x*y) for y in B] for x in B])
        self.assertEqual(K.det(),-128)
if __name__=="__main__":unittest.main()
