from fractions import Fraction as F
from itertools import product
import unittest

def conv(a,b,N):
    return [sum(a[j]*b[n-j] for j in range(n+1)) for n in range(N+1)]

def partial(a):
    s=F(0); v=[]
    for x in a:
        s+=x; v.append(s)
    return v

class Chapter11(unittest.TestCase):
    def test_finite_identities(self):
        a=[F((-1)**n,n+1) for n in range(15)]
        b=[F(1,2**n) for n in range(15)]
        A,B,C=partial(a),partial(b),partial(conv(a,b,14))
        for N in range(15):
            self.assertEqual(C[N],sum(a[j]*b[k] for j in range(N+1) for k in range(N+1-j)))
            self.assertEqual(C[N],sum(a[j]*B[N-j] for j in range(N+1)))
            self.assertEqual(A[N]*B[N],sum(a[j]*b[k] for j,k in product(range(N+1),repeat=2)))

    def test_absolute_tail_and_norm_bound(self):
        a=[F((-1)**n,2**n) for n in range(20)]
        b=[F(1,3**n) for n in range(20)]
        A,B,C=partial(a),partial(b),partial(conv(a,b,19))
        alpha,beta=F(2),F(3,2)
        for N in range(20):
            m=N//2
            self.assertLessEqual(abs(A[N]*B[N]-C[N]),beta*F(1,2**m)+alpha*F(1,2*3**m))
            self.assertLessEqual(sum(abs(x) for x in conv(a,b,N)),alpha*beta)

    def test_geometric_coefficients(self):
        for q in (F(0),F(1,2),F(-2,3)):
            a=[q**n for n in range(18)]
            self.assertEqual(conv(a,a,17),[(n+1)*q**n for n in range(18)])

    def test_mertens_identity_and_example(self):
        a=[F(1,2**n) for n in range(24)]
        b=[F((-1)**n,n+1) for n in range(24)]
        B=partial(b); A=partial(a)
        c=conv(a,b,23); C=partial(c)
        self.assertEqual(c[0],b[0])
        for n in range(1,24):
            self.assertEqual(c[n],b[n]+c[n-1]/2)
            self.assertLessEqual(abs(b[n]),abs(c[n])+abs(c[n-1])/2)
            J=n//2; z=B[-1]; M=max(abs(v-z) for v in B)
            self.assertEqual(C[n]-A[n]*z,sum(a[j]*(B[n-j]-z) for j in range(n+1)))
            self.assertLessEqual(abs(C[n]-A[n]*z),sum(abs(a[j])*abs(B[n-j]-z) for j in range(J+1))+M*sum(abs(a[j]) for j in range(J+1,n+1)))

    def test_divergent_example_exact_lower_bound(self):
        for n in range(50):
            for j in range(n+1):
                self.assertLessEqual((j+1)*(n-j+1),(n+1)**2)
            self.assertEqual(sum(F(1,n+1) for j in range(n+1)),1)

    def test_abel_finite_identity(self):
        a=[F((-1)**n,n+1) for n in range(22)]
        b=[F(n+1,2**n) for n in range(22)]
        A,B,C=partial(a),partial(b),partial(conv(a,b,21))
        for N in range(22):
            self.assertEqual(sum(C[:N+1]),sum(A[j]*B[N-j] for j in range(N+1)))
            for r,s in product(range(N+2),repeat=2):
                self.assertEqual(sum(r+s<=m for m in range(N+1)),sum(r<=j and s<=N-j for j in range(N+1)))

    def test_triangular_mean_endpoints(self):
        for J in range(1,10):
            for N in range(2*J,2*J+20):
                self.assertEqual(sum(not (J<=j<=N-J) for j in range(N+1)),2*J)

    def test_pair_enumeration_and_triple_product(self):
        for N in range(9):
            pairs=[(j,n-j) for n in range(N+1) for j in range(n+1)]
            self.assertEqual(len(pairs),len(set(pairs)))
            self.assertEqual(set(pairs),{(j,k) for j,k in product(range(N+1),repeat=2) if j+k<=N})
        a=[F(1,2**n) for n in range(10)]
        b=[F((-1)**n,n+1) for n in range(10)]
        c=[F(1,3**n) for n in range(10)]
        t=conv(conv(a,b,9),c,9)
        for n in range(10):
            self.assertEqual(t[n],sum(a[j]*b[k]*c[n-j-k] for j in range(n+1) for k in range(n-j+1)))

if __name__=="__main__": unittest.main()
