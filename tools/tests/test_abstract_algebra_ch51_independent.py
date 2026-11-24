"""AA-51: exact geometric checks independent of orbit enumeration."""
import unittest
import itertools as it
import sympy as s

def key(M):
    return tuple(s.simplify(e) for e in M)

def signed_perms(cyclic=False):
    for p in it.permutations(range(3)):
        if cyclic and p not in [(0,1,2),(1,2,0),(2,0,1)]:
            continue
        for signs in it.product((-1,1),repeat=3):
            M=s.zeros(3)
            for i,j in enumerate(p):
                M[i,j]=signs[i]
            if M.det()==1:
                yield M

class AA51GeometryTests(unittest.TestCase):
    def test_tetrahedron(self):
        X={v for v in it.product((-1,1),repeat=3) if s.prod(v)==1}
        G=list(signed_perms(True))
        self.assertEqual(len(G),12)
        for M in G:
            self.assertEqual({key(M*s.Matrix(v)) for v in X},X)
        for subset in it.combinations(X,3):
            self.assertNotEqual(s.Matrix.hstack(*(s.Matrix(v) for v in subset)).det(),0)
    def test_cube(self):
        G=list(signed_perms())
        self.assertEqual(len(G),24)
        X=list(v for v in it.product((-1,1),repeat=3) if s.prod(v)==1)
        def line(v):
            return tuple(z*v[0] for z in v)
        actions={tuple(line(key(M*s.Matrix(v))) for v in X) for M in G}
        self.assertEqual(len(actions),24)
    def test_icosahedron(self):
        # Work over the quadratic number field using exact algebraic entries.
        phi=(1+s.sqrt(5))/2
        v=s.Matrix([0,1,phi])
        ring=[s.Matrix(a) for a in [(0,-1,phi),(phi,0,1),(1,phi,0),
                                  (-1,phi,0),(-phi,0,1)]]
        X=[v,-v]+ring+[-a for a in ring]
        for i,a in enumerate(ring):
            self.assertEqual(s.simplify(v.dot(a)-phi),0)
            for j,b in enumerate(ring):
                if i!=j:
                    expected=phi if (i-j)%5 in (1,4) else -phi
                    self.assertEqual(s.simplify(a.dot(b)-expected),0)
        B=s.Matrix.hstack(v,ring[0],ring[1])
        C=s.Matrix.hstack(v,ring[1],ring[2])
        R=(C*B.inv()).applyfunc(s.simplify)
        self.assertEqual((R.T*R-s.eye(3)).applyfunc(s.simplify),s.zeros(3))
        self.assertEqual(s.simplify(R.det()),1)
        self.assertEqual({key(R*a) for a in X},{key(a) for a in X})
        self.assertEqual((R**5-s.eye(3)).applyfunc(s.simplify),s.zeros(3))
        self.assertNotEqual(R,s.eye(3))
        self.assertEqual(len({key(M*v) for M in signed_perms(True)}),12)
if __name__=="__main__":
    unittest.main()
