"""AA-X25: degree-four constructibility versus generic S_n and radicals.

Exact modular arithmetic and exhaustive S4 operations; these finite
regressions complement, but do not replace, the general field-theory proof.
"""
from itertools import combinations, permutations
from math import gcd, factorial
from pathlib import Path
import re
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
X = sp.Symbol("X")
F = X**4 - X - 1
IDENTITY = (0, 1, 2, 3)
S4 = tuple(permutations(range(4)))


def mul(a, b):
    """Composition a after b."""
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a):
    return tuple(a.index(i) for i in range(len(a)))


def parity(a):
    return (-1) ** sum(a[i] > a[j] for i in range(len(a))
                        for j in range(i + 1, len(a)))


def cycle_type(a):
    seen = set()
    lengths = []
    for i in range(len(a)):
        if i in seen:
            continue
        j, length = i, 0
        while j not in seen:
            seen.add(j)
            j = a[j]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths))


def generated(generators):
    """Exact closure in S4 with right-multiplication by generators."""
    elements = {IDENTITY}
    pending = [IDENTITY]
    while pending:
        a = pending.pop()
        for g in generators:
            b = mul(a, g)
            if b not in elements:
                elements.add(b)
                pending.append(b)
    return frozenset(elements)


def derived(elements):
    commutators = [
        mul(mul(mul(a, b), inverse(a)), inverse(b))
        for a in elements for b in elements
    ]
    return generated(commutators)


def is_two_power(n):
    return n > 0 and (n & (n - 1)) == 0


def phi_by_coprime_count(n):
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))


class ConstructibilityGenericGaloisInterface(unittest.TestCase):
    def test_exact_mod2_irreducibility_and_mod7_three_cycle(self):
        f2 = sp.Poly(F, X, modulus=2)
        self.assertEqual(f2, sp.Poly(X**4 + X + 1, X, modulus=2))
        self.assertTrue(all(f2.eval(t) % 2 != 0 for t in (0, 1)))
        # The only monic irreducible quadratic over F2 is X^2+X+1.
        q = sp.Poly(X**2 + X + 1, X, modulus=2)
        self.assertEqual(f2.rem(q), sp.Poly(1, X, modulus=2))
        self.assertTrue(sp.Poly(F, X, domain=sp.QQ).is_irreducible)

        f7 = sp.Poly(F, X, modulus=7)
        cub = sp.Poly(X**3 + 3*X**2 + 2*X - 2, X, modulus=7)
        self.assertEqual(f7, sp.Poly(X - 3, X, modulus=7) * cub)
        self.assertTrue(all(cub.eval(t) % 7 != 0 for t in range(7)))
        self.assertEqual(cub.degree(), 3)
        self.assertEqual(int(sp.discriminant(F, X)), -283)
        self.assertNotEqual(-283 % 2, 0)
        self.assertNotEqual(-283 % 7, 0)
        # Good Frobenius types are a 4-cycle and (1,3).
        self.assertEqual(tuple(sorted(
            g.degree() for g, exponent
            in sp.factor_list(f2)[1] for _ in range(exponent))), (4,))
        self.assertEqual(tuple(sorted(
            g.degree() for g, exponent
            in sp.factor_list(f7)[1] for _ in range(exponent))), (1, 3))

    def test_all_four_cycles_and_three_cycles_generate_s4(self):
        cycles4 = [g for g in S4 if cycle_type(g) == (4,)]
        cycles3 = [g for g in S4 if cycle_type(g) == (1, 3)]
        self.assertEqual(len(cycles4), 6)
        self.assertEqual(len(cycles3), 8)
        for a in cycles4:
            for b in cycles3:
                with self.subTest(a=a, b=b):
                    self.assertEqual(len(generated((a, b))), 24)
        # Direct calculation is a separate check from using the
        # classification of transitive quartic Galois subgroups.

    def test_s4_is_solvable_but_is_not_a_two_group(self):
        s = frozenset(S4)
        a4 = frozenset(g for g in S4 if parity(g) == 1)
        klein = frozenset(g for g in S4
                          if cycle_type(g) in ((1, 1, 1, 1), (2, 2)))
        self.assertEqual((len(s), len(a4), len(klein)), (24, 12, 4))
        self.assertEqual(derived(s), a4)
        self.assertEqual(derived(a4), klein)
        self.assertEqual(derived(klein), frozenset((IDENTITY,)))
        self.assertFalse(is_two_power(len(s)))
        self.assertTrue(all(is_two_power(n) for n in (1, 2, 4, 8)))
        # A solvable Galois group only yields radicals, not necessarily
        # a tower of quadratic extensions.

    def test_d4_two_group_model_and_quadratic_tower(self):
        rotation = (1, 2, 3, 0)
        reflection = (0, 3, 2, 1)
        d4 = generated((rotation, reflection))
        rotations = generated((rotation,))
        square = mul(rotation, rotation)
        half_turn = generated((square,))
        self.assertEqual([len(g) for g in
                          (d4, rotations, half_turn,
                           frozenset((IDENTITY,)))], [8, 4, 2, 1])
        self.assertTrue(rotations.issubset(d4))
        self.assertTrue(half_turn.issubset(rotations))
        self.assertEqual(mul(mul(reflection, rotation), reflection),
                         inverse(rotation))
        self.assertEqual(len(d4), 8)
        self.assertEqual(sp.discriminant(X**4 - 2, X), -2048)
        self.assertTrue(sp.Poly(X**4-2, X, domain=sp.QQ).is_irreducible)
        # Q -> Q(sqrt(2)) -> Q(sqrt(sqrt(2))) is quadratic at
        # both steps, while the quartic is irreducible.
        y = sp.sqrt(sp.sqrt(2))
        self.assertEqual(sp.simplify(y**4), 2)
        self.assertEqual(sp.simplify((y**2)**2), 2)

    def test_quartic_degree_not_sufficient_for_constructibility(self):
        self.assertTrue(sp.Poly(F, X, domain=sp.QQ).is_irreducible)
        self.assertEqual(sp.Poly(F, X).degree(), 4)
        self.assertTrue(is_two_power(4))
        self.assertEqual(sp.Poly(F, X).count_roots(-sp.oo, sp.oo), 2)
        # For either real root, its normal closure is the same S4
        # splitting field. 24 cannot be the order of a 2-group.
        self.assertFalse(is_two_power(factorial(4)))
        self.assertTrue(is_two_power(8))
        # This does not contradict quartics being solvable by radicals.
        self.assertEqual(len(derived(S4)), 12)

    def test_polygon_criterion_matches_fermats_primes(self):
        # For n<=100, all odd Fermat primes relevant to Gauss-Wantzel
        # are 3,5,17. The test uses direct gcd-count rather than
        # trusting the library's totient implementation.
        fprimes = (3, 5, 17)
        for n in range(3, 101):
            with self.subTest(n=n):
                totient = phi_by_coprime_count(n)
                self.assertEqual(totient, int(sp.totient(n)))
                m = n
                while m % 2 == 0:
                    m //= 2
                for p in fprimes:
                    if m % p == 0:
                        m //= p
                fermat_form = m == 1
                self.assertEqual(is_two_power(totient), fermat_form)
        for n, want in ((5, True), (7, False), (9, False),
                        (15, True), (17, True), (33, False),
                        (51, False), (85, True),
                        (257, True), (65537, True)):
            self.assertEqual(is_two_power(int(sp.totient(n))), want)

    def test_generic_symmetry_and_specialization_warning(self):
        # This checks elementary symmetric invariance, not the generic
        # Galois theorem (which needs formal independent variables).
        xx = sp.symbols("x0:4")
        elementary = [
            sp.expand(sum(sp.prod(xx[i] for i in ids)
                          for ids in combinations(range(4), k)))
            for k in range(1, 5)
        ]
        self.assertEqual(len(S4), 24)
        for p in S4:
            sub = dict(zip(xx, (xx[j] for j in p)))
            for poly in elementary:
                self.assertEqual(sp.expand(poly.xreplace(sub)-poly), 0)
        # Specializations to rational coefficients can have smaller
        # Galois groups than the generic polynomial with group S4.
        self.assertEqual(sp.factor(X**4-1),
                         (X-1)*(X+1)*(X**2+1))
        self.assertTrue(sp.Poly(F, X, domain=sp.QQ).is_irreducible)

    def test_source_references_hypotheses_and_chapter_count(self):
        folder = ROOT / "chapters/pl/abstract_algebra"
        paths = sorted(folder.glob("[0-9][0-9]-*.tex"))
        self.assertEqual(len(paths), 50)
        sources = {p.name: p.read_text(encoding="utf8") for p in paths}
        labels = [a for text in sources.values()
                  for a in re.findall(r"\\label\{([^{}]+)\}", text)]
        self.assertEqual(len(labels), len(set(labels)))
        focus = (
            "30-konstrukcje-cyrklem-i-linijka-oraz-wielokaty-foremne.tex",
            "36-wielomian-ogolny-i-grupy-symetryczne.tex",
        )
        self.assertEqual(sum(len(re.findall(r"\\label\{", sources[n]))
                             for n in focus), 24)
        refs = [r for n in focus for r in re.findall(
            r"\\(?:ref|eqref|pageref|autoref)\{([^{}]+)\}", sources[n])]
        self.assertEqual(len(refs), 20)
        self.assertEqual(set(refs) - set(labels), set())
        for required in (
            "aa:lem:quadratic-tower-normal-closure",
            "aa:tw:constructibility-tower",
            "aa:cor:constructibility-degree",
            "aa:tw:regular-polygon",
            "aa:tw:generic-sn",
            "aa:wn:generic-abel",
        ):
            self.assertIn(required, labels)


if __name__ == "__main__":
    unittest.main()
