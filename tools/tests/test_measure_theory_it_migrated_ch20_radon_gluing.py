"""Finite checks of local measure gluing and Radon examples."""
from fractions import Fraction as Q
import unittest


class RadonGluing13(unittest.TestCase):
    def test_consistent_local_restrictions(self):
        U=[{0},{0,1},{0,1,2}]
        local=[{0:Q(2),1:Q(9)}, {0:Q(2),1:Q(3),2:Q(8)},
               {0:Q(2),1:Q(3),2:Q(5)}]
        pieces=[U[0],U[1]-U[0],U[2]-U[1]]
        glued={x:local[n][x] for n,B in enumerate(pieces) for x in B}
        self.assertEqual(glued,{0:2,1:3,2:5})
        for m,region in enumerate(U):
            self.assertEqual(sum(glued[x] for x in region),
                             sum(local[m][x] for x in region))

    def test_gluing_countable_additivity_finite_model(self):
        pieces=[{0,2},{1},{3,4}]
        masses=[Q(1),Q(2),Q(3),Q(4),Q(5)]
        E=[{0,1},{2,4},{3}]
        def mu(A):
            return sum(sum(masses[x] for x in A & B) for B in pieces)
        self.assertEqual(mu(set.union(*E)),sum(mu(A) for A in E))

    def test_atomic_regular_sandwich_repeated_points(self):
        atoms=[(1,Q(2)),(1,Q(3)),(4,Q(7))]
        E={0,1,3}
        K={x for x,w in atoms if x in E}
        U=set(range(6))-{x for x,w in atoms if x not in E}
        mass=lambda A:sum(w for x,w in atoms if x in A)
        self.assertLessEqual(K,E)
        self.assertLessEqual(E,U)
        self.assertEqual(mass(K),mass(E))
        self.assertEqual(mass(E),mass(U))

    def test_density_atom_moments(self):
        for n in range(4):
            moment=Q(1,n+1)+(2 if n==0 else 0)
            self.assertEqual(moment,[Q(3),Q(1,2),Q(1,3),Q(1,4)][n])

    def test_circle_second_moment_symmetry(self):
        # Exact discrete quadrature for sin^2 and cos^2 at rational unit vectors.
        points=[(Q(1),Q(0)),(Q(3,5),Q(4,5)),(Q(0),Q(1)),(Q(4,5),Q(3,5))]
        self.assertTrue(all(x*x+y*y==1 for x,y in points))
        self.assertEqual(sum(x*x for x,y in points),Q(len(points),2))
        self.assertEqual(sum(y*y for x,y in points),Q(len(points),2))


if __name__=="__main__":
    unittest.main()
