"""AA-X17: Burnside orbit counts = traces of Reynolds projectors, exactly."""
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]

def comp(g, h):
    return tuple(g[h[i]] for i in range(len(g)))

def group_generated(n, generators):
    identity = tuple(range(n))
    group = {identity}
    while True:
        augmented = group | {comp(g, h) for g in group for h in generators}
        if len(augmented) == len(group):
            return sorted(group)
        group = augmented

def permute_colors(g, colors):
    result = [None] * len(g)
    for i, color in enumerate(colors):
        result[g[i]] = color
    return tuple(result)

def orbits(group, points, action):
    remaining = set(points)
    result = []
    while remaining:
        x = next(iter(remaining))
        orbit = {action(g, x) for g in group}
        assert orbit <= set(points)
        result.append(orbit)
        remaining -= orbit
    return result

def fixed_counts(group, points, action):
    return [sum(action(g, x) == x for x in points) for g in group]

def reynolds(group, points, action):
    """Exact matrix on formal permutation basis, entry (i,j) = fixed sum / |G|."""
    ix = {p: i for i, p in enumerate(points)}
    n = len(points)
    counts = [[0] * n for _ in range(n)]
    for g in group:
        for j, p in enumerate(points):
            counts[ix[action(g, p)]][j] += 1
    return [[Fraction(v, len(group)) for v in row] for row in counts]

def squared(m):
    n = len(m)
    return [[sum((m[i][k] * m[k][j] for k in range(n)), Fraction()) for j in range(n)] for i in range(n)]

def matrix_of(g, points, action):
    ix = {p: i for i, p in enumerate(points)}
    n = len(points)
    out = [[0] * n for _ in range(n)]
    for j, p in enumerate(points):
        out[ix[action(g, p)]][j] = 1
    return out

def matmul(a, b):
    n = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(n)), Fraction()) for j in range(n)] for i in range(n)]

S3 = sorted(permutations(range(3)))
R4 = (1, 2, 3, 0)
F4 = (0, 3, 2, 1)
D4 = group_generated(4, (R4, F4))
C4 = group_generated(4, (R4,))

def kind_s3(g):
    if g == (0, 1, 2):
        return "e"
    return "t" if sum(g[i] > g[j] for i in range(3) for j in range(i + 1, 3)) % 2 else "c"

class BurnsideReynoldsInterface(unittest.TestCase):
    def test_group_laws_and_actions(self):
        self.assertEqual((len(S3), len(D4), len(C4)), (6, 8, 4))
        for G in (S3, D4, C4):
            e = tuple(range(len(G[0])))
            self.assertIn(e, G)
            for g in G:
                for h in G:
                    self.assertIn(comp(g, h), G)
                    for i in range(len(e)):
                        self.assertEqual(comp(g, h)[i], g[h[i]])
    def test_burnside_by_direct_orbit_enumeration(self):
        cases = [
            (S3, list(range(3)), lambda g, x: g[x], 1),
            (D4, list(range(4)), lambda g, x: g[x], 1),
            (D4, list(product(range(2), repeat=4)), permute_colors, 6),
            (D4, list(product(range(3), repeat=4)), permute_colors, 21),
            (C4, list(product(range(3), repeat=4)), permute_colors, 24),
        ]
        for G, X, act, expected in cases:
            with self.subTest(group=len(G), points=len(X)):
                counts = fixed_counts(G, X, act)
                self.assertEqual(sum(counts), expected * len(G))
                self.assertEqual(len(orbits(G, X, act)), expected)
    def test_reynolds_trace_idempotence_and_orbit_image(self):
        cases = [
            (S3, list(range(3)), lambda g, x: g[x], 1),
            (D4, list(range(4)), lambda g, x: g[x], 1),
            (D4, list(product(range(2), repeat=4)), permute_colors, 6),
            (S3, [(a, i) for a in (0, 1) for i in range(3)],
             lambda g, x: (x[0], g[x[1]]), 2),
        ]
        for G, X, act, expected in cases:
            with self.subTest(group=len(G), points=len(X)):
                P = reynolds(G, X, act)
                self.assertEqual(P, squared(P))
                self.assertEqual(sum(P[i][i] for i in range(len(X))), expected)
                self.assertEqual(len(orbits(G, X, act)), expected)
                self.assertTrue(all(sum(row) == 1 for row in P))
    def test_reynolds_intertwines_group(self):
        for G, X, act in (
            (S3, list(range(3)), lambda g, x: g[x]),
            (D4, list(product(range(2), repeat=4)), permute_colors),
        ):
            P = reynolds(G, X, act)
            for g in G:
                A = matrix_of(g, X, act)
                self.assertEqual(matmul(P, A), P)
                self.assertEqual(matmul(A, P), P)
    def test_s3_character_and_trivial_isotypic_multiplicity(self):
        irreps = {"trivial": {"e": 1, "t": 1, "c": 1},
                  "sign": {"e": 1, "t": -1, "c": 1},
                  "standard": {"e": 2, "t": 0, "c": -1}}
        permutation_char = {g: sum(g[i] == i for i in range(3)) for g in S3}
        expected = {"trivial": 1, "sign": 0, "standard": 1}
        for name, chi in irreps.items():
            scalar = Fraction(sum(permutation_char[g] * chi[kind_s3(g)] for g in S3), len(S3))
            self.assertEqual(scalar, expected[name])
        self.assertEqual(sum(permutation_char.values()), len(S3))
        self.assertEqual(sum(permutation_char[g] for g in S3), 6)
    def test_empty_trivial_and_modular_edge_cases(self):
        G = C4
        self.assertEqual(len(orbits(G, [], lambda g, x: x)), 0)
        self.assertEqual(reynolds(G, [], lambda g, x: x), [])
        X = list(range(5))
        P = reynolds(G, X, lambda g, x: x)
        self.assertEqual(P, [[int(i == j) for j in range(5)] for i in range(5)])
        self.assertEqual(len(orbits(G, X, lambda g, x: x)), 5)
        # Burnside counts remain integers in characteristic 2; the Reynolds
        # average 1/|C2| cannot be formed in F2 when |C2|=2=0.
        C2 = [(0, 1), (1, 0)]
        self.assertEqual(sum(fixed_counts(C2, [0, 1], lambda g, x: g[x])), 2)
        self.assertEqual(len(orbits(C2, [0, 1], lambda g, x: g[x])), 1)
        self.assertEqual(2 % 2, 0)
    def test_source_hypotheses_labels_and_references(self):
        files = {
            1: "01-grupy-podgrupy-i-grupy-cykliczne.tex",
            2: "02-warstwy-lagrange-euler-i-grupy-ilorazowe.tex",
            3: "03-dzialania-grup-orbity-i-rownanie-klas.tex",
            41: "41-reprezentacje-grup-i-twierdzenie-maschkego.tex",
            42: "42-lemat-schura-charaktery-i-ortogonalnosc.tex",
        }
        src = {n: (ROOT / "chapters/pl/abstract_algebra" / f).read_text(encoding="utf-8")
               for n, f in files.items()}
        labels = [t for content in src.values() for t in re.findall(r"\\label\{([^{}]+)\}", content)]
        self.assertEqual(len(labels), len(set(labels)))
        target = set(labels)
        for n in (3, 41, 42):
            refs = set(re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^{}]+)\}", src[n]))
            self.assertFalse(refs - target, f"AA-{n} missing targets: {refs - target}")
        for req in ("aa:tw:burnside", "aa:prop:reynolds-vectors", "aa:def:character",
                    "aa:prop:character-basics", "aa:prop:isotypic-projector"):
            self.assertIn(req, target)

if __name__ == "__main__":
    unittest.main()
