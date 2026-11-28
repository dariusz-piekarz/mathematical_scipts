"""Finite-model regression checks for Chapter 07 (functions and mappings).

These tests detect regressions in boundary cases; they do not prove
statements for arbitrary infinite sets.
"""
import unittest
from itertools import product


class TestLogicAndSetTheoryChapter07(unittest.TestCase):
    def test_finite_functions_and_inverses(self):
        tested = 0
        for n in range(5):
            for m in range(5):
                functions = list(product(range(m), repeat=n))
                expected = m**n if n else 1  # 0^0 = 1 for functions
                self.assertEqual(len(functions), expected, (n, m))
                reverse_maps = list(product(range(n), repeat=m))
                for f in functions:
                    tested += 1
                    fibres = [[a for a in range(n) if f[a] == b]
                              for b in range(m)]
                    injective = len(set(f)) == n
                    surjective = set(f) == set(range(m))
                    self.assertEqual(injective,
                                     all(len(fibre) <= 1 for fibre in fibres))
                    self.assertEqual(surjective,
                                     all(bool(fibre) for fibre in fibres))
                    self.assertEqual(sum(map(len, fibres)), n)
                    self.assertEqual(
                        {a for fibre in fibres for a in fibre},
                        set(range(n)))
                    left = any(all(g[f[a]] == a for a in range(n))
                               for g in reverse_maps)
                    right = any(all(f[g[b]] == b for b in range(m))
                                for g in reverse_maps)
                    both = any(
                        all(g[f[a]] == a for a in range(n))
                        and all(f[g[b]] == b for b in range(m))
                        for g in reverse_maps
                    )
                    self.assertEqual(left, injective and (n > 0 or m == 0))
                    self.assertEqual(right, surjective)
                    self.assertEqual(both, injective and surjective)
        self.assertEqual(tested, 499)

    def test_characteristic_functions(self):
        for n in range(5):
            characteristics = {
                tuple(1 if mask & (1 << a) else 0 for a in range(n))
                for mask in range(1 << n)
            }
            self.assertEqual(characteristics,
                             set(product((0, 1), repeat=n)))


if __name__ == "__main__":
    unittest.main()
