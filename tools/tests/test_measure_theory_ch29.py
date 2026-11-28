"""Chapter 29: exact model and source regressions, not proof certification."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/pl/measure_theory/29-zbiory-prostowalne-funkcje-bv-i-zbiory-o-skonczonym-obwodzie.tex"
EXPECTED_LABELS = ["ch:geometric-measure-29","def:rectifiable-29","ex:lip-graph-29","lem:rectifiable-union-29","thm:rectifiable-decomposition-29","def:BV-variation-29","lem:BV-smooth-29","thm:BV-measure-29","thm:BV-banach-29","def:finite-perimeter-29","thm:smooth-perimeter-29","ex:cube-perimeter-29","lem:perimeter-complement-29","thm:perimeter-lsc-29","lem:BV-translation-29","thm:perimeter-compact-29","def:normal-BV-29","def:measure-boundary-29","lem:essential-boundary-null-29","def:reduced-boundary-29","lem:reduced-boundary-measurable-29","thm:gauss-green-BV-29","eq:gauss-green-BV-29","lem:dg-relative-isoperimetric","lem:dg-ball-cut","lem:dg-density","lem:dg-blowup","lem:dg-rectifiability","lem:dg-density-identification","thm:de-giorgi-structure-29","lem:BV-level-meas-auditVI","thm:BV-layercake-29","lem:BV-strict-approx","lem:BV-smooth-levels","thm:BV-coarea-full-29","eq:BV-coarea-full-29","cor:BV-coarea-weighted-29","def:current-29","lem:current-boundary-square-29"]
EXPECTED_EXTERNAL = ["ch:area-coarea-28","ch:covering-24","ch:hausdorff-26","ch:miary-ze-znakiem","ch:riesz-markov-21","ch:vector-measures-30","rem:hausdorff-convention-26","thm:graph-area-28","thm:hausdorff-lipschitz-26","thm:lebesgue-diff-25","thm:lipschitz-area-coarea-28","thm:rademacher-28","thm:relative-lebesgue-25","thm:relative-radon-25"]


def integrate_step(knots, values, a, b):
    return sum((max(Q(0), min(b, y)-max(a, x))*v
                for x, y, v in zip(knots, knots[1:], values)), Q(0))


def jumps(knots, values):
    padded = [Q(0), *values, Q(0)]
    return {x: b-a for x, a, b in zip(knots, padded, padded[1:]) if b != a}


class Chapter29(unittest.TestCase):
    def test_labels_and_external_dependencies(self):
        source = SOURCE.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", source)
        refs = set(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", source))
        self.assertEqual(labels, EXPECTED_LABELS)
        self.assertEqual(sorted(refs-set(labels)), EXPECTED_EXTERNAL)

    def test_step_derivative_and_current_boundary_sign(self):
        knots = [Q(-2), Q(-1), Q(1), Q(4)]
        values = [Q(1), Q(0), Q(1)]
        atoms = jumps(knots, values)
        self.assertEqual(atoms, {Q(-2):1, Q(-1):-1, Q(1):1, Q(4):-1})
        for degree in range(1, 6):
            integral = sum(v*(b**degree-a**degree)
                           for a,b,v in zip(knots,knots[1:],values))
            self.assertEqual(integral, -sum(c*x**degree for x,c in atoms.items()))
        self.assertEqual(sum(map(abs, atoms.values())), 4)

    def test_exact_step_coarea_including_negative_levels(self):
        knots = [Q(-2), Q(-1), Q(1), Q(4)]
        for vals in product(range(-2, 3), repeat=3):
            variation = sum(map(abs, jumps(knots, list(vals)).values()))
            levels = sorted(set([0, *vals]))
            integral = Q(0)
            for a,b in zip(levels,levels[1:]):
                t = Q(a+b,2)
                # Outside support, u=0. Subtract the constant superlevel value.
                superlevel = [int(v>t)-int(0>t) for v in vals]
                integral += (b-a)*sum(map(abs,jumps(knots,superlevel).values()))
            self.assertEqual(integral, variation)

    def test_weighted_coarea_at_every_jump(self):
        vals = [-3, 2, -1, 4, 0]
        weights = [Q(1,3), Q(7,2), Q(0), Q(5)]
        expected = sum(w*abs(b-a) for a,b,w in zip(vals,vals[1:],weights))
        levels = sorted(set(vals))
        got = Q(0)
        for a,b in zip(levels,levels[1:]):
            t = Q(a+b,2)
            got += (b-a)*sum(w*abs(int(v>t)-int(u>t))
                             for u,v,w in zip(vals,vals[1:],weights))
        self.assertEqual(got, expected)

    def test_translation_bound_for_step_functions(self):
        knots = list(map(Q, [-3,-1,2,5]))
        vals = list(map(Q, [2,-1,3]))
        variation = sum(map(abs,jumps(knots,vals).values()))
        for h in [Q(-7), Q(-1,3), Q(0), Q(2,5), Q(4)]:
            breaks = sorted(set(knots+[k-h for k in knots]))
            difference = sum(abs(integrate_step(knots,vals,a+h,b+h)
                                 -integrate_step(knots,vals,a,b))
                             for a,b in zip(breaks,breaks[1:]))
            self.assertLessEqual(difference, abs(h)*variation)

    def test_cube_averages_and_projection_contraction(self):
        knots = [Q(-1),Q(1,3),Q(7,4),Q(2)]
        vals = [Q(0),Q(1),Q(0)]
        for m in range(1,7):
            side = Q(3,2**m)
            edges = [Q(-1)+side*i for i in range(2**m+1)]
            error = Q(0)
            for a,b in zip(edges,edges[1:]):
                mass = integrate_step(knots,vals,a,b)
                mean = mass/side
                self.assertTrue(0<=mean<=1)
                error += mass*(1-mean)+(side-mass)*mean
            self.assertLessEqual(error, 2*side*2)

    def test_partition_gradient_cancellation(self):
        u = Q(5,3)
        psi = [Q(1,6), Q(1,3), Q(1,2)]
        grad = [Q(-4,7), Q(3,7), Q(1,7)]
        self.assertEqual(sum(psi),1)
        self.assertEqual(sum(u*d for d in grad),0)
        self.assertEqual(sum(p*Q(7,5) for p in psi),Q(7,5))

    def test_cone_separation_constants(self):
        alpha = Q(1,8)
        for n in range(2,9):
            r = Q(3,7)
            rho = alpha*r/16
            # Volumes divided by omega_n.
            delta = (alpha/16)**n/8
            volume = rho**n
            self.assertEqual(delta*r**n,volume/8)
            self.assertLessEqual(delta*(rho/2)**n,volume/8)
            self.assertGreater(volume/2-delta*(rho/2)**n,delta*r**n)
            self.assertGreater(7*alpha*r/8,rho)

    def test_scaled_hyperplane_density(self):
        for n in range(1,9):
            for r in (Q(1,10),Q(3,7),Q(2)):
                self.assertEqual(r**(1-n)*r**(n-1),1)

    def test_polar_variation_of_vector_atoms(self):
        vectors = [(3,4),(-5,12),(0,-2)]
        lengths = [5,13,2]
        normals = [tuple(Q(c,l) for c in v) for v,l in zip(vectors,lengths)]
        self.assertEqual(sum(lengths),20)
        for v,l,p in zip(vectors,lengths,normals):
            self.assertEqual(sum(c*c for c in p),1)
            self.assertEqual(tuple(l*c for c in p),v)
        self.assertNotEqual(sum(lengths)**2,sum(sum(v[i] for v in vectors)**2 for i in range(2)))

    def test_local_exhaustion_and_exceptional_level_convention(self):
        # Finite model of monotone exhaustion and zero extension on exceptional levels.
        atoms = [{1:Q(2),2:Q(1)}, {}, {2:Q(3),3:Q(4)}]
        for A in ({1},{1,2},{1,2,3}):
            lhs = sum(sum(m.get(x,0) for x in A) for m in atoms)
            rhs = sum(sum(m.get(x,0) for m in atoms) for x in A)
            self.assertEqual(lhs,rhs)
        self.assertEqual(sum(sum(m.values()) for m in atoms),10)

    def test_required_proof_steps(self):
        text = SOURCE.read_text(encoding="utf-8")
        for term in ("wspólnym zbiorze", "twierdzenia Sarda",
                     "układ Dynkina", "klas funkcji",
                     "zbieżnością ścisłą", "rozmaitościach",
                     "przeliczalnej sumie pełnych wykresów"):
            # Source prose can wrap across lines.
            self.assertIn(term, " ".join(text.split()))
        self.assertNotRegex(text, r"\\(?:mathbf|mathbb)\{1\}_")
        self.assertNotIn("mollifikator",text)


if __name__ == "__main__":
    unittest.main()
