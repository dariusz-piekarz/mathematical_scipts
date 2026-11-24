"""Source regressions and exact finite-dimensional models for chapter 28."""
from fractions import Fraction as Q
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/pl/measure_theory/28-wzor-na-pole-powierzchni-krotnosci-i-koobszar.tex"

def transpose(a):
    return list(map(list, zip(*a)))

def mul(a, b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def det(a):
    if not a:
        return Q(1)
    return sum((-1)**j * a[0][j] * det([row[:j]+row[j+1:] for row in a[1:]]) for j in range(len(a)))

def inverse(a):
    n = len(a)
    d = det(a)
    return [[Q((-1)**(i+j)*det([row[:i]+row[i+1:] for k,row in enumerate(a) if k!=j]), d) for j in range(n)] for i in range(n)]

EXPECTED_LABELS = ["ch:area-coarea-28","def:k-jacobian-28","def:multiplicity-28","lem:graph-hausdorff-28","thm:graph-area-28","thm:immersion-area-28","eq:area-immersion-28","def:normal-jacobian-28","lem:linear-coarea-28","thm:coarea-submersion-28","eq:coarea-smooth-28","cor:coarea-level-28","thm:pushforward-coarea-28","sec:rademacher-28","def:frechet-rademacher-28","lem:rademacher-line-28","lem:rademacher-direction-28","thm:rademacher-28","lem:whitney-c1-28","eq:whitney-condition-28","lem:lusin-whitney-28","lem:critical-area-null-28","lem:null-fibres-lipschitz-28","lem:critical-coarea-null-28","thm:lipschitz-area-coarea-28","lem:c1-general-area-28","thm:coarea-manifolds-28","eq:coarea-manifolds-28","cor:riemann-hausdorff-28"]

class Chapter28(unittest.TestCase):
    def test_stable_labels(self):
        labels = re.findall(r"\\label\{([^}]+)\}", SOURCE.read_text(encoding="utf-8"))
        self.assertEqual(labels, EXPECTED_LABELS)

    def test_gram_reparametrization(self):
        a = [[1,2],[2,1],[0,3]]
        p = [[2,1],[1,3]]
        ap = mul(a,p)
        self.assertEqual(det(mul(transpose(ap),ap)), det(mul(transpose(a),a))*det(p)**2)

    def test_normal_jacobian_schur(self):
        # Positive definite, non-block-diagonal metric with a two-dimensional fibre.
        a = [[2,1,0,1],[0,2,1,0],[0,0,3,1],[0,0,0,2]]
        b = mul(transpose(a),a)
        h = [[5,1],[1,3]]
        l = [[1,0,0,0],[0,1,0,0]]
        c = [row[2:] for row in b[2:]]
        adj = mul(mul(inverse(b),transpose(l)),h)
        self.assertEqual(det(mul(l,adj))*det(b),det(h)*det(c))

    def test_equal_dimension_empty_fibre_block(self):
        b = [[4,1],[1,3]]
        h = [[2,1],[1,5]]
        self.assertEqual(det(mul(inverse(b),h))*det(b),det(h)*det([]))

    def test_rank_deficient_gram(self):
        a = [[1,2],[2,4],[3,6]]
        self.assertEqual(det(mul(transpose(a),a)),0)

    def test_critical_fibre_scaling(self):
        # Number of cubes times fibre cost times target volume bound.
        for n in range(1,7):
            for m in range(1,n+1):
                r, eta = Q(1,16),Q(1,9)
                self.assertEqual(r**(-n)*r**(n-m)*eta*r**m,eta)

    def test_whitney_dyadic_intervals(self):
        # Exact one-dimensional model of the maximal-cube construction
        # for K={0}; use rational arithmetic, including grid boundaries.
        def dist(a, b):
            return Q(0) if a <= 0 <= b else min(abs(a), abs(b))

        def containing(x, side):
            k = x // side
            return k * side, (k + 1) * side

        cubes = set()
        for x in (Q(1,128), Q(-1,128), Q(1,3), Q(-3,2), Q(16), Q(-32)):
            side = Q(1, 2**18)
            a, b = containing(x, side)
            self.assertGreaterEqual(dist(a,b), 20*side)
            while True:
                aa, bb = containing(x, 2*side)
                if dist(aa,bb) < 40*side:
                    break
                a,b = aa,bb
                side *= 2
            self.assertTrue(a <= x <= b)
            self.assertLess(dist(a,b),42*side)
            centre = (a+b)/2
            left, right = centre-Q(9,16)*side, centre+Q(9,16)*side
            self.assertGreaterEqual(dist(left,right),19*side)
            self.assertLessEqual(max(abs(left),abs(right)),44*side)
            cubes.add((a,b))
        for a,b in cubes:
            for c,d in cubes:
                if (a,b) != (c,d):
                    self.assertGreaterEqual(max(a,c),min(b,d))

    def test_whitney_affine_reproduction(self):
        # Exact affine data at distinct anchors, arbitrary partition
        # values and derivatives satisfying the two partition identities.
        a, slope = Q(7,3), Q(-5,4)
        x = Q(2,7)
        anchors = [Q(-3), Q(1,2), Q(4)]
        weights = [Q(1,5), Q(3,10), Q(1,2)]
        derivatives = [Q(2,3), Q(-1,4), Q(-5,12)]
        self.assertEqual(sum(weights),1)
        self.assertEqual(sum(derivatives),0)
        p = [a+slope*t+slope*(x-t) for t in anchors]
        self.assertEqual(sum(w*v for w,v in zip(weights,p)),a+slope*x)
        self.assertEqual(sum(weights)*slope+sum(w*v for w,v in zip(derivatives,p)),slope)

    def test_linear_coarea_nonorthogonal_fibres(self):
        # A=[2,1], G=[[1/2,-1/2],[0,1]], so AG=[1,0].
        a = [[Q(2),Q(1)]]
        g = [[Q(1,2),Q(-1,2)],[Q(0),Q(1)]]
        self.assertEqual(mul(a,g),[[1,0]])
        z = [[row[1]] for row in g]
        self.assertEqual(det(mul(a,transpose(a)))*det(g)**2,
                         det(mul(transpose(z),z)))

    def test_required_measure_theoretic_steps(self):
        source = SOURCE.read_text(encoding="utf-8")
        for term in ("zewnętrzną miarę zero", "Nie wymaga ono", "zupełność miary Lebesgue'a", "Nie zakładamy istnienia krzywej minimalizującej", "borelowską funkcją"):
            self.assertIn(term,source)

if __name__ == "__main__":
    unittest.main()
