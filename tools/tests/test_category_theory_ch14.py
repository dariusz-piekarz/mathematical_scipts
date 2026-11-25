"""CAT-14: finite adjunction models."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/14-sprzezenia-funktorow.tex"


def maps(n, m):
    return itertools.product(range(m), repeat=n)


def compose(g, f):
    return tuple(g[i] for i in f)


class CategoryTheoryCh14(unittest.TestCase):
    def test_CAT_14_001_image_quantifiers(self):
        for n, m in itertools.product(range(4), repeat=2):
            for f in maps(n, m):
                for a_mask, b_mask in itertools.product(range(1 << n), range(1 << m)):
                    a = {i for i in range(n) if a_mask >> i & 1}
                    b = {j for j in range(m) if b_mask >> j & 1}
                    ex = {f[i] for i in a}
                    pre = {i for i in range(n) if f[i] in b}
                    all_f = {j for j in range(m) if all(i in a for i in range(n) if f[i] == j)}
                    self.assertEqual(ex <= b, a <= pre)
                    self.assertEqual(pre <= a, b <= all_f)

    def test_CAT_14_002_diagonal_product_coproduct(self):
        for a, b, x in itertools.product(range(3), repeat=3):
            self.assertEqual({(h[:a], h[a:]) for h in maps(a+b, x)},
                             set(itertools.product(maps(a, x), maps(b, x))))
            self.assertEqual({(tuple(i//b for i in h), tuple(i%b for i in h))
                              for h in maps(x, a*b)},
                             set(itertools.product(maps(x, a), maps(x, b))))

    def test_CAT_14_003_poset_adjunction_triangles(self):
        for n, m in itertools.product(range(1, 4), repeat=2):
            for f, g in itertools.product(maps(n, m), maps(m, n)):
                if tuple(sorted(f)) != f or tuple(sorted(g)) != g:
                    continue
                if not all((f[i] <= j) == (i <= g[j])
                           for i in range(n) for j in range(m)):
                    continue
                self.assertTrue(all(i <= g[f[i]] for i in range(n)))
                self.assertTrue(all(f[g[j]] <= j for j in range(m)))
                self.assertTrue(all(f[g[f[i]]] == f[i] for i in range(n)))
                self.assertTrue(all(g[f[g[j]]] == g[j] for j in range(m)))
                full_f = all((f[i] <= f[k]) == (i <= k) for i in range(n) for k in range(n))
                full_g = all((g[j] <= g[k]) == (j <= k) for j in range(m) for k in range(m))
                self.assertEqual(full_f, all(g[f[i]] == i for i in range(n)))
                self.assertEqual(full_g, all(f[g[j]] == j for j in range(m)))
                # Every subset, including empty: join/meet preservation.
                for mask in range(1 << n):
                    a = [i for i in range(n) if mask >> i & 1]
                    self.assertEqual(f[max(a, default=0)], max((f[i] for i in a), default=0))
                for mask in range(1 << m):
                    b = [j for j in range(m) if mask >> j & 1]
                    self.assertEqual(g[min(b, default=m-1)], min((g[j] for j in b), default=n-1))

    def test_CAT_14_004_free_vector_bijection(self):
        for p in (2, 3):
            for n, m in itertools.product(range(3), repeat=2):
                vectors = tuple(maps(m, p))
                for images in itertools.product(vectors, repeat=n):
                    def lin(a):
                        return tuple(sum(a[j]*images[j][i] for j in range(n)) % p
                                     for i in range(m))
                    basis = [tuple(int(i == j) for i in range(n)) for j in range(n)]
                    self.assertEqual(tuple(lin(e) for e in basis), images)
                    for a, b in itertools.product(maps(n, p), repeat=2):
                        self.assertEqual(lin(tuple((u+v)%p for u,v in zip(a,b))),
                                         tuple((u+v)%p for u,v in zip(lin(a),lin(b))))

    def test_CAT_14_005_structure(self):
        s = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        self.assertEqual(len(labels), len(set(labels)))
        for name in ("sec:adjunctions", "def:adjunction", "def:unit-counit",
                     "tw:triangles", "tw:adjoints-preserve", "cat:prop:adj-full-faithful"):
            self.assertIn(name, labels)
        stack = []
        for cmd, env in re.findall(r"\\(begin|end)\{([^}]+)\}", s):
            if cmd == "begin":
                stack.append(env)
            else:
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
