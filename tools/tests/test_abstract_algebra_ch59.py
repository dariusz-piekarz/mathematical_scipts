import unittest
import sympy as s

def E(n,i,j):
    M=s.zeros(n)
    M[i,j]=1
    return M

def br(A,B):
    return A*B-B*A

class RootDecomposition(unittest.TestCase):
    def test_matrix_root_models(self):
        for n in range(2,7):
            hs=[E(n,k,k)-E(n,k+1,k+1) for k in range(n-1)]
            es={(i,j):E(n,i,j) for i in range(n) for j in range(n) if i!=j}
            weights={ij:tuple(H[ij[0],ij[0]]-H[ij[1],ij[1]] for H in hs) for ij in es}
            self.assertEqual(len(set(weights.values())),n*(n-1))
            self.assertEqual(s.Matrix(list(weights.values())).rank(),n-1)
            for (i,j),X in es.items():
                for H,w in zip(hs,weights[i,j]):
                    self.assertEqual(br(H,X),w*X)
                Y=es[j,i]
                H=E(n,i,i)-E(n,j,j)
                T=H/(2*n)
                self.assertEqual(T[i,i]-T[j,j],s.Rational(1,n))
                self.assertEqual(br(X,Y),H)
                self.assertEqual(br(H,X),2*X)
                self.assertEqual(br(H,Y),-2*Y)
                for (k,l),Z in es.items():
                    self.assertEqual(s.trace(X*Z),int(i==l and j==k))
                    B=br(X,Z)
                    for L,a,b in zip(hs,weights[i,j],weights[k,l]):
                        self.assertEqual(br(L,B),(a+b)*B)

    def test_jordan_components_adjoint(self):
        for n in range(3,7):
            S=s.diag(*([1,1]+[-2]+[0]*(n-3)))
            N=E(n,0,1)
            self.assertEqual(br(S,N),s.zeros(n))
            basis=[E(n,k,k)-E(n,k+1,k+1) for k in range(n-1)]
            basis += [E(n,i,j) for i in range(n) for j in range(n) if i!=j]
            for X in basis:
                self.assertEqual(br(N,br(N,br(N,X))),s.zeros(n))
                self.assertEqual(br(S,br(N,X)),br(N,br(S,X)))
                self.assertEqual(br(S+N,X),br(S,X)+br(N,X))

if __name__=='__main__':
    unittest.main()
