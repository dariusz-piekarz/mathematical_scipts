"""Finite regression models for CAT-42; not substitutes for proofs."""
import itertools
import unittest


def functions(n, m):
    return itertools.product(range(m), repeat=n)


def kernel(f):
    return {(x, y) for x in range(len(f)) for y in range(len(f)) if f[x] == f[y]}


class CategoryTheoryCh42(unittest.TestCase):
    def test_regular_image_and_pullback(self):
        for n, m, k in itertools.product(range(4), repeat=3):
            for f in functions(n, m):
                for g in functions(k, m):
                    pullback = {(i, j) for i in range(n) for j in range(k) if f[i] == g[j]}
                    self.assertEqual({j for i, j in pullback},
                                     {j for j in range(k) if g[j] in set(f)})

    def test_effective_equivalence_relations(self):
        for n in range(4):
            pairs = list(itertools.product(range(n), repeat=2))
            for mask in range(1 << len(pairs)):
                r = {p for i, p in enumerate(pairs) if mask & (1 << i)}
                if not all((i, i) in r for i in range(n)):
                    continue
                if not all((j, i) in r for i, j in r):
                    continue
                if not all((i, k) in r for i, j in r for h, k in r if j == h):
                    continue
                q = tuple(min(j for j in range(n) if (i, j) in r) for i in range(n))
                self.assertEqual(kernel(q), r)

    def test_descent_through_surjection(self):
        for n, m, k in itertools.product(range(4), repeat=3):
            for a in functions(n, m):
                if set(a) != set(range(m)):
                    continue
                for b in functions(n, k):
                    if not kernel(a) <= kernel(b):
                        continue
                    candidates = [g for g in functions(m, k)
                                  if tuple(g[a[i]] for i in range(n)) == b]
                    self.assertEqual(len(candidates), 1)

    def test_local_lift_independence_on_quotients(self):
        # Two lifts can differ in representatives, but not in target classes.
        for n, m in itertools.product(range(4), repeat=2):
            for q in functions(m, m):
                lifts = list(functions(n, m))
                for b, c in itertools.product(lifts, repeat=2):
                    if all((x, y) in kernel(q) for x, y in zip(b, c)):
                        self.assertEqual(tuple(q[x] for x in b), tuple(q[y] for y in c))

    def test_baer_sum_cyclic_extensions(self):
        # Extensions of Z/n by Z/m with relation n*b = t*a.
        # Representatives t modulo m, modulo changes t -> t+n*s.
        from math import gcd
        for m, n in itertools.product(range(1, 9), repeat=2):
            d = gcd(m, n)
            classes = lambda t: {(t + n*s) % m for s in range(m)}
            for t, u in itertools.product(range(m), repeat=2):
                self.assertEqual({(x+y) % m for x in classes(t) for y in classes(u)},
                                 classes(t+u))
                self.assertEqual(classes(t) == classes(u), (t-u) % d == 0)
                self.assertEqual(classes(t+(-t)), classes(0))


if __name__ == "__main__":
    unittest.main()
