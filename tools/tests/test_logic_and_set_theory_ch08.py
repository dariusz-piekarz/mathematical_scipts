"""Finite regression checks for Chapter 08 (images, preimages and mappings).

Small-model tests provide counterexample searches, not proofs of infinite
or ZF statements. In particular, finite choice tests do not establish AC.
"""
import unittest
from itertools import product


def maps(n, m):
    return list(product(range(m), repeat=n))


def powerset(n):
    return [frozenset(k for k in range(n) if mask & (1 << k))
            for mask in range(1 << n)]


def image(f, s):
    return frozenset(f[x] for x in s)


def inverse(f, t):
    return frozenset(x for x in range(len(f)) if f[x] in t)


def injective(f):
    return len(f) == len(set(f))


def surjective(f, m):
    return set(f) == set(range(m))


class TestLogicAndSetTheoryChapter08(unittest.TestCase):
    def test_images_and_preimages(self):
        count = 0
        for n in range(4):
            for m in range(4):
                for f in maps(n, m):
                    for s in powerset(n):
                        for u in powerset(n):
                            count += 1
                            self.assertEqual(image(f, s | u),
                                             image(f, s) | image(f, u))
                            self.assertLessEqual(image(f, s & u),
                                                 image(f, s) & image(f, u))
                            if injective(f):
                                self.assertEqual(image(f, s & u),
                                                 image(f, s) & image(f, u))
                                self.assertEqual(image(f, s - u),
                                                 image(f, s) - image(f, u))
                            fibres = [
                                frozenset(a for a in range(n) if f[a] == b)
                                for b in range(m)
                            ]
                            fibre_condition = all(
                                not (fibre & s and fibre & u)
                                or bool(fibre & s & u)
                                for fibre in fibres
                            )
                            self.assertEqual(
                                image(f, s & u) == image(f, s) & image(f, u),
                                fibre_condition)
                        for t in powerset(m):
                            self.assertEqual(
                                image(f, s) <= t, s <= inverse(f, t))
                            self.assertEqual(
                                inverse(f, image(f, s)),
                                frozenset(x for x in range(n)
                                          if any(f[x] == f[z] for z in s)))
                            self.assertEqual(
                                image(f, inverse(f, t)),
                                t & image(f, range(n)))
                    for t in powerset(m):
                        for v in powerset(m):
                            self.assertEqual(inverse(f, t | v),
                                             inverse(f, t) | inverse(f, v))
                            self.assertEqual(inverse(f, t & v),
                                             inverse(f, t) & inverse(f, v))
                            self.assertEqual(inverse(f, set(range(m)) - t),
                                             set(range(n)) - inverse(f, t))
        self.assertEqual(count, 2556)

    def test_empty_and_nonempty_intersection_families(self):
        checked = 0
        for n in range(4):
            for m in range(4):
                for f in maps(n, m):
                    subsets = powerset(n)
                    families = [()]
                    families.extend((s,) for s in subsets)
                    families.extend((s, u) for s in subsets for u in subsets)
                    families.extend((s, u, v)
                                    for s in subsets for u in subsets
                                    for v in subsets)
                    for fam in families:
                        checked += 1
                        common = (set(range(n)) if not fam
                                  else set.intersection(*map(set, fam)))
                        image_common = (
                            set(range(m)) if not fam else
                            set.intersection(*(set(image(f, s))
                                               for s in fam)))
                        self.assertLessEqual(image(f, common),
                                             image_common)
                        if fam and injective(f):
                            self.assertEqual(image(f, common),
                                             image_common)
                        if not fam:
                            self.assertEqual(image(f, common)
                                             == image_common,
                                             surjective(f, m))
        self.assertEqual(checked, 22356)

    def test_composition(self):
        checked = 0
        for n in range(4):
            for m in range(4):
                for k in range(4):
                    for f in maps(n, m):
                        for g in maps(m, k):
                            checked += 1
                            composed = tuple(g[b] for b in f)
                            for s in powerset(n):
                                self.assertEqual(image(composed, s),
                                                 image(g, image(f, s)))
                            for t in powerset(k):
                                self.assertEqual(inverse(composed, t),
                                                 inverse(f, inverse(g, t)))
                            if injective(f) and injective(g):
                                self.assertTrue(injective(composed))
                            if surjective(f, m) and surjective(g, k):
                                self.assertTrue(surjective(composed, k))
                            if injective(composed):
                                self.assertTrue(injective(f))
                            if surjective(composed, k):
                                self.assertTrue(surjective(g, k))
        self.assertEqual(checked, 1678)

    def test_product_with_empty_factors(self):
        checked = 0
        for n in range(3):
            for m in range(3):
                for p in range(3):
                    for q in range(3):
                        for f in maps(n, m):
                            for g in maps(p, q):
                                checked += 1
                                pairs = {(f[a], g[c])
                                         for a in range(n) for c in range(p)}
                                injprod = len(pairs) == n * p
                                surjprod = len(pairs) == m * q
                                if injective(f) and injective(g):
                                    self.assertTrue(injprod)
                                if surjective(f, m) and surjective(g, q):
                                    self.assertTrue(surjprod)
                                if n > 0 and p > 0 and injprod:
                                    self.assertTrue(injective(f))
                                    self.assertTrue(injective(g))
                                if m > 0 and q > 0 and surjprod:
                                    self.assertTrue(surjective(f, m))
                                    self.assertTrue(surjective(g, q))
        self.assertEqual(checked, 121)

    def test_gluing_and_quotients(self):
        partial = []
        for s in powerset(3):
            domain = sorted(s)
            for values in maps(len(domain), 2):
                partial.append(dict(zip(domain, values)))
        self.assertEqual(len(partial), 27)
        for f in partial:
            for g in partial:
                compatible = all(f[x] == g[x] for x in f.keys() & g.keys())
                joined = {**f, **g}
                valid = all(joined[x] == v for x, v in f.items())
                valid &= all(joined[x] == v for x, v in g.items())
                self.assertEqual(compatible, valid)
        for n in range(4):
            for m in range(4):
                for f in maps(n, m):
                    classes = {
                        b: frozenset(a for a in range(n) if f[a] == b)
                        for b in set(f)
                    }
                    self.assertEqual(
                        frozenset(classes.values()).__len__(),
                        len(set(f)))
                    self.assertEqual(
                        set().union(*classes.values()), set(range(n)))


if __name__ == "__main__":
    unittest.main()
