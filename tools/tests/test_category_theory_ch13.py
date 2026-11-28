"""CAT-13: finite models for equivalences and quasi-inverses."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/13-rownowaznosci-kategorii.tex"


class CategoryTheoryCh13(unittest.TestCase):
    def test_CAT_13_001_corrected_fullness(self):
        # One-object group category Z/n, F=G=Id. The two natural
        # isomorphisms are independent and need not coincide.
        for n in range(2, 8):
            for alpha, beta, u in itertools.product(range(n), repeat=3):
                c = (alpha - beta) % n
                up = (-c + u + c) % n
                f = (alpha + up - alpha) % n
                self.assertEqual(f, u)

    def test_CAT_13_002_quasi_inverse_conjugation(self):
        # A groupoid with multiple objects; each Hom is Z/n.
        # Composition adds labels, and F sends the sole object to 0.
        for n in range(2, 5):
            for eps in itertools.product(range(n), repeat=3):
                def lift(y, z, u):
                    return (-eps[z] + u + eps[y]) % n
                for y, z, w in itertools.product(range(3), repeat=3):
                    self.assertEqual(lift(y, y, 0), 0)
                    for u, v in itertools.product(range(n), repeat=2):
                        self.assertEqual(lift(y, w, (u+v) % n),
                                         (lift(y, z, u)+lift(z, w, v)) % n)
                        self.assertEqual((eps[z]+lift(y, z, u)) % n,
                                         (u+eps[y]) % n)
                eta, theta = (-eps[0]) % n, eps[0]
                self.assertEqual((eta+theta) % n, 0)
                self.assertEqual((theta+eta) % n, 0)

    def test_CAT_13_003_skeleton_representatives(self):
        # Equivalence relation represented by a partition of finite objects.
        for classes in itertools.product(range(3), repeat=4):
            reps = {c: classes.index(c) for c in set(classes)}
            self.assertEqual(len(reps), len(set(classes)))
            self.assertTrue(all(classes[reps[c]] == c for c in classes))
            for a, b in itertools.product(range(4), repeat=2):
                self.assertEqual(classes[a] == classes[b],
                                 reps[classes[a]] == reps[classes[b]])

    def test_CAT_13_004_matrix_coordinates(self):
        for p in (2, 3):
            for n, m in itertools.product(range(3), repeat=2):
                basis = [tuple(int(i == j) for i in range(n)) for j in range(n)]
                for entries in itertools.product(range(p), repeat=n*m):
                    def apply(v):
                        return tuple(sum(entries[i*n+j]*v[j] for j in range(n)) % p
                                     for i in range(m))
                    columns = [apply(e) for e in basis]
                    recovered = tuple(columns[j][i] for i in range(m) for j in range(n))
                    self.assertEqual(recovered, entries)

    def test_CAT_13_006_noncommutative_quasi_inverse(self):
        # Three-object groupoid with Hom sets labelled by S_3.
        # Multiplication is composition, not commutative addition.
        group = tuple(itertools.permutations(range(3)))
        identity = tuple(range(3))

        def mul(g, f):
            return tuple(g[i] for i in f)

        def inv(g):
            return tuple(g.index(i) for i in range(3))

        self.assertNotEqual(mul((1, 0, 2), (0, 2, 1)),
                            mul((0, 2, 1), (1, 0, 2)))
        for eps in itertools.product(group, repeat=3):
            def lift(y, z, u):
                return mul(inv(eps[z]), mul(u, eps[y]))

            for y, z, w in itertools.product(range(3), repeat=3):
                self.assertEqual(lift(y, y, identity), identity)
                for u, v in itertools.product(group, repeat=2):
                    self.assertEqual(lift(y, w, mul(v, u)),
                                     mul(lift(z, w, v), lift(y, z, u)))
                    self.assertEqual(mul(eps[z], lift(y, z, u)),
                                     mul(u, eps[y]))
            eta, theta = inv(eps[0]), eps[0]
            self.assertEqual(mul(theta, eta), identity)
            self.assertEqual(mul(eta, theta), identity)
            for f in group:
                self.assertEqual(mul(lift(0, 0, f), eta), mul(eta, f))

    def test_CAT_13_005_structure(self):
        s = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        self.assertEqual(len(labels), len(set(labels)))
        for name in ("sec:equivalence", "def:equivalence", "tw:equivalence",
                     "przyklad:mat-equivalence", "cat:prop:skeleton"):
            self.assertIn(name, labels)
        stack = []
        for cmd, env in re.findall(r"\\(begin|end)\{([^}]+)\}", s):
            if cmd == "begin":
                stack.append(env)
            else:
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
