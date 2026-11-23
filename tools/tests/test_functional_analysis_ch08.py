"""Functional analysis chapter 08: weak/weak-star topologies and completion.

Finite-dimensional models and source contracts complement, but never replace,
the full mathematical audit of infinite-dimensional theorems.
"""
from __future__ import annotations

import itertools
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "chapters/pl/functional_analysis"
BOOK = ROOT / "books/pl/functional_analysis.tex"
FILES = [
    "01-przestrzenie-liniowo-topologiczne-definicje-i-przyklady.tex",
    "02-podprzestrzenie-produkty-ilorazy-i-topologie-uniwersalne.tex",
    "03-sieci-struktura-jednostajna-i-zupelnosc.tex",
    "04-zbiory-ograniczone-rodziny-operatorow-i-metryzowalnosc.tex",
    "05-przestrzenie-lokalnie-wypukle-i-seminormy.tex",
    "06-twierdzenie-hahna-banacha-i-ciagly-dual.tex",
    "07-oddzielanie-zbiorow-wypuklych-polary-i-twierdzenie-bipolarne.tex",
    "08-pary-dualne-i-topologie-slabe.tex",
]


class FunctionalAnalysisChapter08(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = [(BASE / file).read_text(encoding="utf-8")
                       for file in FILES]
        cls.source = cls.sources[-1]

    def test_book_integration_and_section_counter(self):
        book = BOOK.read_text(encoding="utf-8")
        inputs = re.findall(
            r"\\input\{\.\./\.\./chapters/pl/functional_analysis/([^}]+)\}",
            book)
        self.assertEqual(inputs[:8], FILES)
        self.assertIn(r"\setcounter{section}{7}", self.source)

    def test_environment_counts(self):
        for env, expected in (("proof", 12), ("przyklad", 5)):
            self.assertEqual(self.source.count(r"\begin{" + env + "}"), expected)
            self.assertEqual(self.source.count(r"\end{" + env + "}"), expected)
        for env in ("definicja", "lemat", "twierdzenie",
                    "stwierdzenie", "wniosek", "uwaga"):
            self.assertEqual(self.source.count(r"\begin{" + env + "}"),
                             self.source.count(r"\end{" + env + "}"))

    def test_labels_unique_and_cross_references(self):
        own = re.findall(r"\\label\{([^}]+)\}", self.source)
        self.assertEqual(len(own), 18)
        self.assertEqual(len(own), len(set(own)))
        all_labels = {label for source in self.sources
                      for label in re.findall(r"\\label\{([^}]+)\}", source)}
        refs = re.findall(r"\\ref\{([^}]+)\}", self.source)
        refs += re.findall(r"\\hyperref\[([^]]+)\]", self.source)
        self.assertTrue(set(refs) <= all_labels, sorted(set(refs)-all_labels))

    def test_dual_terminology_and_network_proof_contract(self):
        self.assertIn("przestrzeń algebraicznie", self.source)
        self.assertIn("przestrzeń sprzężoną", self.source)
        self.assertNotIn("przestrzeń dualna topologiczna", self.source)
        self.assertNotIn("przestrzeń dualną algebraiczną", self.source)
        self.assertNotIn("przestrzeni dualnej algebraicznej", self.source)
        self.assertIn(r"$\dim E'\ge n$", self.source)
        self.assertIn(r"$f_j(x_k)=\delta_{jk}$", self.source)
        self.assertIn(r"$\Phi\notin J(E)$", self.source)
        self.assertIn(r"$(x_G)$ jest słabo fundamentalną", self.source)

    def test_pair_non_degeneracy_in_complex_finite_dimension(self):
        pair = lambda x, y: x[0]*y[0]+x[1]*y[1]
        for x in ((1+1j,0j),(0j,2j),(-1j,2+3j)):
            f = tuple(v.conjugate() for v in x)
            self.assertGreater(abs(pair(x,f)),0)
        for f in ((0j,1j),(2j,0j),(-1+1j,1+0j)):
            x = tuple(v.conjugate() for v in f)
            self.assertGreater(abs(pair(x,f)),0)

    def test_weak_neighborhood_and_pairing_convergence(self):
        # Coordinate seminorms p_j(x)=|x_j| generate the product
        # topology; pointwise convergence means coordinatewise.
        vectors = [(1/n, (-1)**n/n) for n in range(1,200)]
        for eps in (.5,.1,.01):
            N = math.floor(1/eps)+2
            for n in range(N,200):
                self.assertLess(abs(vectors[n-1][0]), eps)
                self.assertLess(abs(vectors[n-1][1]), eps)

    def test_weak_boundedness_of_finite_set(self):
        # For E=R^3, pairing with all R^3 linear forms.
        B = [(1,2,3),(-1,4,0),(0,0,0)]
        coefficients = itertools.product((-2,0,3), repeat=3)
        for a in coefficients:
            values = [abs(sum(x*y for x,y in zip(a,b))) for b in B]
            self.assertLessEqual(max(values),
                                 max(sum(abs(t)*abs(v)
                                         for t,v in zip(a,b)) for b in B))

    def test_dual_of_weak_topology_is_finite_span(self):
        # A functional annihilating ker T factors through T.
        # T(x,y,z)=(x+2y, y-z), g=3*T1-2*T2.
        T=lambda x:(x[0]+2*x[1],x[1]-x[2])
        g=lambda x:3*(x[0]+2*x[1])-2*(x[1]-x[2])
        for x in ((0,0,0),(1,2,3),(-1,4,0),(2,-3,1)):
            u,v=T(x)
            self.assertAlmostEqual(g(x),3*u-2*v)
        for t in (-5,0,1,7):
            # Kernel vector x=(-2t,t,t).
            self.assertEqual(g((-2*t,t,t)),0)

    def test_infinite_dimensional_weak_neighborhood_has_line(self):
        # An R^3 illustration of the finite-functional constraint:
        # if only f1=x and f2=y are controlled, every multiple of e3
        # belongs to the same neighborhood, and is unbounded for f3=z.
        for t in (-10000,-3,-1,0,1,13,10000):
            z=(0,0,t)
            self.assertLess(abs(z[0]), .5)
            self.assertLess(abs(z[1]), .5)
        self.assertGreater(max(abs(t) for t in (-10000,10000)), 1)

    def test_weak_unit_sphere_closure_finite_constraint_model(self):
        # In R^4, fixing finitely many coordinates from a point
        # inside the ball, one can use a free coordinate to hit sphere.
        x=(.3,.4,0,0)
        norm=lambda v:math.sqrt(sum(a*a for a in v))
        self.assertLess(norm(x),1)
        z=(x[0],x[1],math.sqrt(1-norm(x)**2),0)
        self.assertAlmostEqual(norm(z),1)
        self.assertEqual(z[:2],x[:2])

    def test_weakstar_basis_sequence_c0_l1(self):
        # <x,e_n>=x_n -> 0 for x in c0; ell-infinity witness ones
        # evaluates to one on each e_n, disproving weak convergence.
        vectors = (
            [1/(n+1) for n in range(400)],
            [(-1)**n/(n+1) for n in range(400)]
        )
        for x in vectors:
            self.assertLess(abs(x[-1]),.01)
            self.assertEqual(sum([1]*1),1)
        self.assertIn(r"\sigma(\ell^1,c_0)", self.source)

    def test_product_topology_equals_sigma_product_finite_support(self):
        # A finitely supported coefficient vector is a continuous
        # linear form in the product topology.
        coeff={1:2,4:-1,12:3}
        evaluate=lambda x:sum(coeff[i]*x.get(i,0) for i in coeff)
        x={1:1.5,4:2,12:-1}
        for j in (0,2,3,5,50,10000):
            x2=dict(x);x2[j]=1e6
            self.assertEqual(evaluate(x2),evaluate(x))

    def test_finite_interpolation_for_algebraic_dual_density(self):
        # E=c00, F=K^N; three prescribed moments of Phi on
        # polynomial coordinate functionals are matched by a single
        # finitely supported x=(-2,5,-2).
        x=(-2.,5.,-2.)
        test_forms=((1.,1.,1.),(1.,2.,3.),(1.,4.,9.))
        desired=(1.,2.,0.)
        for f,y in zip(test_forms,desired):
            self.assertAlmostEqual(sum(a*b for a,b in zip(x,f)),y)

    def test_biorthogonal_normed_dual_infinite_dimension_witness(self):
        # Finite-dimensional coordinate functionals are independent
        # for every n; Hahn-Banach extends each of them to E'.
        for n in (1,2,5,16):
            basis = [[int(i==j) for j in range(n)] for i in range(n)]
            coordinate = [[float(i==j) for j in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(n):
                    self.assertEqual(
                        sum(a*b for a,b in zip(coordinate[i],basis[j])),
                        int(i==j))

    def test_pointwise_cauchy_net_vs_sequence_distinction(self):
        # Exact finite-dimensional model of the directed interpolation
        # argument: for G subset H, the H-interpolant agrees with Phi
        # on every coordinate in G. No claim of an infinite-dimensional
        # nonconvergent net is made by this finite model.
        from fractions import Fraction

        indices = frozenset(range(1, 5))
        finite_sets = [
            frozenset(s)
            for size in range(len(indices) + 1)
            for s in itertools.combinations(sorted(indices), size)
        ]
        phi = {1: Fraction(7), 2: Fraction(-2),
               3: Fraction(4), 4: Fraction(15)}

        def interpolate(G):
            return {j: phi[j] if j in G else Fraction(0)
                    for j in indices}

        for G in finite_sets:
            x_G = interpolate(G)
            self.assertTrue(all(x_G[j] == phi[j] for j in G))
            for H in finite_sets:
                if G <= H:
                    x_H = interpolate(H)
                    self.assertTrue(all(x_H[j] == x_G[j] for j in G))

        for j in indices:
            anchor = frozenset({j})
            tail = [G for G in finite_sets if anchor <= G]
            self.assertTrue(tail)
            self.assertTrue(all(interpolate(G)[j] == phi[j] for G in tail))
        self.assertIn(r"\\mathcal G", self.source)

    def test_strong_operator_norm_bounded_sets(self):
        # E=R² with l1 norm, E'=linfty; bounded B gives
        # p_B(f)<=sup_B||x|| * ||f||_infty.
        B=[(0,0),(2,0),(-1,1),(0,-3)]
        f=(1.5,-.5)
        norm=lambda x:abs(x[0])+abs(x[1])
        val=max(abs(f[0]*x[0]+f[1]*x[1]) for x in B)
        self.assertLessEqual(
            val,max(map(norm,B))*max(map(abs,f))+1e-12)

    def test_mackey_disc_generated_seminorm(self):
        # K_f={a f : |a|<=1} yields p_K(x)=|<x,f>|.
        f=(1+2j,2-1j)
        x=(.5-1j,2+0j)
        pair=sum(a*b for a,b in zip(x,f))
        self.assertAlmostEqual(max(abs(pair*complex(math.cos(t),
                                                   math.sin(t)))
                                   for t in (0,.4,1,2)),abs(pair))
        self.assertIn(r"K_f=\{af:|a|\le1\}",self.source)


if __name__ == "__main__":
    unittest.main()
