"""AA-X23: exact S4/V4 resolvent action and Frobenius cycle signatures.

Checks AA-32 discriminants, AA-34 cubic resolvents, AA-35 good reductions.
All arithmetic uses exact integers or finite-field polynomials.
"""
from itertools import permutations
from pathlib import Path
import re
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
X, Y = sp.symbols("X Y")
PAIRS = (
    ((0, 1), (2, 3)),
    ((0, 2), (1, 3)),
    ((0, 3), (1, 2)),
)
PAIR_KEYS = tuple(frozenset(frozenset(p) for p in pairing)
                  for pairing in PAIRS)
EXAMPLES = {
    "C4": X**4 + X**3 + X**2 + X + 1,
    "D4": X**4 - 2,
    "V4": X**4 - 10*X**2 + 1,
    "S4": X**4 - X - 1,
    "reducible": (X-1)*(X-2)*(X-3)*(X-4),
}
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)


def compose(a, b):
    """Permutation composition a after b."""
    return tuple(a[b[i]] for i in range(len(a)))


def induced(p):
    """Action on the three unordered partitions of {0,1,2,3}."""
    out = []
    for pairs in PAIRS:
        new_pairing = frozenset(frozenset(p[v] for v in pair)
                                for pair in pairs)
        out.append(PAIR_KEYS.index(new_pairing))
    return tuple(out)


def cycle_type(p):
    visited = set()
    lengths = []
    for i in range(len(p)):
        if i in visited:
            continue
        j, length = i, 0
        while j not in visited:
            visited.add(j)
            j = p[j]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths))


def parity(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p))
                     for j in range(i+1, len(p))) % 2 else 1


def resolvent(f):
    poly = sp.Poly(f, X, domain=sp.ZZ)
    assert poly.degree() == 4 and poly.LC() == 1
    _, a, b, c, d = poly.all_coeffs()
    return sp.expand(Y**3-b*Y**2+(a*c-4*d)*Y
                     -(a*a*d+c*c-4*b*d))


def modular_factor_type(poly, symbol, p):
    factors = sp.factor_list(sp.Poly(poly, symbol, modulus=p))[1]
    return tuple(sorted(f.degree() for f, multiplicity in factors
                        for _ in range(multiplicity)))


def squarefree(poly, symbol, p):
    f = sp.Poly(poly, symbol, modulus=p)
    return f.gcd(f.diff()).degree() == 0


class QuarticResolventFrobeniusInterface(unittest.TestCase):
    def test_s4_pairing_action_kernel_and_parity(self):
        all_perms = list(permutations(range(4)))
        image = {p: induced(p) for p in all_perms}
        self.assertEqual(len(set(image.values())), 6)
        kernel = [p for p in all_perms if image[p] == (0, 1, 2)]
        self.assertEqual(set(kernel), {
            (0, 1, 2, 3), (1, 0, 3, 2),
            (2, 3, 0, 1), (3, 2, 1, 0),
        })
        signatures = {
            (1, 1, 1, 1): (1, 1, 1),
            (1, 1, 2): (1, 2),
            (2, 2): (1, 1, 1),
            (1, 3): (3,),
            (4,): (1, 2),
        }
        for p in all_perms:
            with self.subTest(perm=p):
                self.assertEqual(cycle_type(image[p]),
                                 signatures[cycle_type(p)])
                self.assertEqual(parity(p), parity(image[p]))
                for q in all_perms:
                    self.assertEqual(induced(compose(p, q)),
                                     compose(image[p], image[q]))

    def test_resolvent_discriminant_identity_and_exact_models(self):
        predicted = {
            "C4": (Y-2)*(Y**2+Y-1),
            "D4": Y*(Y**2+8),
            "V4": (Y+10)*(Y-2)*(Y+2),
            "S4": Y**3+4*Y-1,
        }
        discriminants = {"C4": 125, "D4": -2048,
                         "V4": 147456, "S4": -283,
                         "reducible": 144}
        for name, f in EXAMPLES.items():
            with self.subTest(name=name):
                r = resolvent(f)
                self.assertEqual(sp.discriminant(f, X),
                                 sp.discriminant(r, Y))
                self.assertEqual(sp.discriminant(f, X),
                                 discriminants[name])
                if name in predicted:
                    self.assertEqual(sp.expand(r-predicted[name]), 0)
                    self.assertTrue(sp.Poly(f, X, domain=sp.QQ).is_irreducible)
        repeated = (X-1)**2*(X+2)*(X-3)
        self.assertEqual(sp.discriminant(repeated, X), 0)
        self.assertEqual(sp.discriminant(resolvent(repeated), Y), 0)

    def test_good_prime_factor_types_functorial_under_resolvent(self):
        induced_types = {
            (1, 1, 1, 1): (1, 1, 1),
            (1, 1, 2): (1, 2),
            (2, 2): (1, 1, 1),
            (1, 3): (3,),
            (4,): (1, 2),
        }
        checked = 0
        for name, f in EXAMPLES.items():
            r, D = resolvent(f), int(sp.discriminant(f, X))
            for p in PRIMES:
                if D % p == 0:
                    continue
                with self.subTest(name=name, p=p):
                    self.assertTrue(squarefree(f, X, p))
                    self.assertTrue(squarefree(r, Y, p))
                    typ_f = modular_factor_type(f, X, p)
                    typ_r = modular_factor_type(r, Y, p)
                    self.assertEqual(typ_r, induced_types[typ_f])
                    checked += 1
        self.assertGreaterEqual(checked, 35)

    def test_nonfaithfulness_and_group_classification_examples(self):
        # An image of cycle type (1,2) has two distinct lifts in S4:
        # a 4-cycle and a 2-cycle with two fixed points.
        p4 = (1, 2, 3, 0)
        p2 = (1, 0, 2, 3)
        self.assertEqual(cycle_type(induced(p4)), (1, 2))
        self.assertEqual(cycle_type(induced(p2)), (1, 2))
        self.assertNotEqual(cycle_type(p4), cycle_type(p2))
        # Image of any product of two disjoint transpositions is identity.
        p22 = (1, 0, 3, 2)
        self.assertEqual(induced(p22), (0, 1, 2))
        # The resolvent's factor degrees distinguish the three regimes
        # but NOT C4 versus D4 when its type is (1,2).
        shapes = {
            "C4": (1, 2), "D4": (1, 2),
            "V4": (1, 1, 1), "S4": (3,),
        }
        for name, factors in shapes.items():
            r = resolvent(EXAMPLES[name])
            self.assertEqual(tuple(sorted(sp.degree(g, Y)
                                          for g, exp in sp.factor_list(r)[1]
                                          for _ in range(exp))), factors)

    def test_good_and_bad_primes_and_legendre_sign(self):
        for name, f in EXAMPLES.items():
            r, D = resolvent(f), int(sp.discriminant(f, X))
            for p in PRIMES:
                with self.subTest(name=name,p=p):
                    good = D % p != 0
                    self.assertEqual(squarefree(f,X,p), good)
                    self.assertEqual(squarefree(r,Y,p), good)
                    if good and p % 2:
                        typ = modular_factor_type(f,X,p)
                        sign = (-1)**(4-len(typ))
                        legendre = pow(D%p, (p-1)//2, p)
                        self.assertEqual(legendre,
                                         1 if sign==1 else p-1)
        # Ramification of a number field is not inferred for arbitrary orders.
        self.assertEqual(sp.discriminant(EXAMPLES["C4"], X) % 5, 0)
        self.assertEqual(sp.discriminant(EXAMPLES["D4"], X) % 2, 0)

    def test_source_labels_references_and_assumptions(self):
        folder = ROOT / "chapters/pl/abstract_algebra"
        files = sorted(folder.glob("[0-9][0-9]-*.tex"))
        self.assertEqual(len(files), 50)
        sources = {p.name:p.read_text(encoding="utf-8") for p in files}
        labels = [z for content in sources.values()
                  for z in re.findall(r"\\label\{([^{}]+)\}", content)]
        self.assertEqual(len(labels), len(set(labels)))
        focus = [
          "32-wyroznik-i-grupa-galois.tex",
          "34-rezolwenta-szescienna-i-grupy-galois-stopnia-czwartego.tex",
          "35-redukcja-modulo-p-i-cykle-frobeniusa.tex",
        ]
        self.assertEqual(sum(len(re.findall(r"\\label\{", sources[f]))
                             for f in focus), 35)
        refs = [z for f in focus
                for z in re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^{}]+)\}",
                                    sources[f])]
        self.assertEqual(len(refs), 33)
        self.assertEqual(set(refs) - set(labels), set())
        for label in (
            "aa:tw:quartic-resolvent-formula",
            "aa:tw:s4-v4",
            "aa:wn:quartic-resolvent-disc",
            "aa:tw:quartic-classification",
            "aa:tw:dedekind-cycle",
            "aa:tw:disc-alternating",
        ):
            self.assertIn(label, labels)
        self.assertIn("charakterystyki różnej od $2$", sources[focus[1]])


if __name__ == "__main__":
    unittest.main()
