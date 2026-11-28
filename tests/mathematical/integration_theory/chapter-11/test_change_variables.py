"""Finite checks of algebra and estimates used in change of variables."""
from fractions import Fraction as Q
import math
import unittest


class ChangeVariables11(unittest.TestCase):
    def test_elementary_determinants(self):
        def det(a):
            return a[0][0]*a[1][1]-a[0][1]*a[1][0]
        A=[[Q(2),Q(3)],[Q(5),Q(7)]]
        B=[A[0], [v+3*u for u,v in zip(*A)]]
        self.assertEqual(det(A),det(B))
        self.assertEqual(det(A[::-1]),-det(A))

    def test_cube_contraction_budget(self):
        r,d=Q(3,2),Q(1,5)
        for y in (-(1-d)*r,Q(0),(1-d)*r):
            for z in (-r,Q(0),r):
                self.assertLessEqual(abs(y-d*z),r)
        self.assertEqual((1-d)*r,Q(6,5))

    def test_dyadic_disjointification(self):
        cubes=[set(range(0,4)),set(range(2,4)),set(range(4,6))]
        covered=set()
        pieces=[]
        for cube in cubes:
            pieces.append(cube-covered)
            covered |= cube
        self.assertEqual(sum(map(len,pieces)),len(covered))
        self.assertTrue(all(not (a&b) for i,a in enumerate(pieces) for b in pieces[i+1:]))

    def test_polar_sector(self):
        r,dr,theta=Q(2),Q(1,10),Q(1,4)
        area=((r+dr)**2-r*r)*theta/2
        self.assertEqual(area,(r*dr+dr*dr/2)*theta)
        self.assertEqual(area/(dr*theta),r+dr/2)

    def test_spherical_orthonormal_frame(self):
        for t,p in ((0.2,0.7),(1.5,2.1),(2.8,5.5)):
            a=(math.sin(t)*math.cos(p),math.sin(t)*math.sin(p),math.cos(t))
            b=(math.cos(t)*math.cos(p),math.cos(t)*math.sin(p),-math.sin(t))
            c=(-math.sin(p),math.cos(p),0)
            dot=lambda u,v:sum(x*y for x,y in zip(u,v))
            for v in (a,b,c):
                self.assertAlmostEqual(dot(v,v),1)
            for u,v in ((a,b),(a,c),(b,c)):
                self.assertAlmostEqual(dot(u,v),0)

    def test_square_map_multiplicity(self):
        self.assertEqual(Q(1)**2-(-Q(1))**2,0)
        self.assertEqual(2*(Q(1)**2-Q(0)**2),2)

    def test_singular_probability_mixture_weights(self):
        for N in (1,4,15):
            w=sum(Q(1,2**k) for k in range(1,N+1))
            self.assertEqual(w,1-Q(1,2**N))
            self.assertGreater(Q(1,2**N),0)


if __name__=="__main__":
    unittest.main()
