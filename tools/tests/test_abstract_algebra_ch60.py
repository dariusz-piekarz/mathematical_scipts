import unittest
import sympy as s

def module(m):
    H=s.diag(*[m-2*j for j in range(m+1)])
    E=s.zeros(m+1); F=s.zeros(m+1)
    for j in range(1,m+1):
        E[j-1,j]=j*(m-j+1)
        F[j,j-1]=1
    return H,E,F

class SL2(unittest.TestCase):
    def test_irreducibles(self):
        for m in range(13):
            H,E,F=module(m)
            I=s.eye(m+1)
            self.assertEqual(H*E-E*H,2*E)
            self.assertEqual(H*F-F*H,-2*F)
            self.assertEqual(E*F-F*E,H)
            self.assertEqual(H*H+2*H+4*F*E,m*(m+2)*I)
            self.assertEqual(F**(m+1),s.zeros(m+1))
            self.assertEqual(F**m*I[:,0],I[:,m])
            for j in range(1,m+2):
                self.assertEqual(E*F**j-F**j*E,j*F**(j-1)*(H-(j-1)*I))

    def test_multiplicity(self):
        ms=[0,1,1,2,4,4,7]
        H=s.diag(*[module(m)[0] for m in ms])
        a={j:list(H.diagonal()).count(j) for j in range(10)}
        for j in range(8):
            self.assertEqual(a[j]-a[j+2],ms.count(j))

    def test_cartan_realization_A(self):
        for n in range(2,8):
            roots=[s.Matrix([int(k==i)-int(k==j) for k in range(n)]) for i in range(n) for j in range(n) if i!=j]
            C=s.Matrix.hstack(*[s.eye(n)[:,i]-s.eye(n)[:,i+1] for i in range(n-1)])
            weights=[C.T*r for r in roots]
            B=sum((v*v.T for v in weights),s.zeros(n-1))
            inv=B.inv()
            rootset={tuple(v) for v in weights}
            for a in weights:
                self.assertTrue((a.T*inv*a)[0]>0)
                for b in weights:
                    k=2*(b.T*inv*a)[0]/(a.T*inv*a)[0]
                    self.assertTrue(k.is_Integer)
                    self.assertIn(tuple(b-k*a),rootset)

if __name__=='__main__':
    unittest.main()
