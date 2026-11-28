"""CAT-12: finite models of slice and comma categories."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/12-obiekty-nad-ustalona-baza-i-kategorie-przecinkowe.tex"


def maps(n, m):
    return itertools.product(range(m), repeat=n)


def comp(g, f):
    return tuple(g[i] for i in f)


class CategoryTheoryCh12(unittest.TestCase):
    def test_CAT_12_001_slice_composition(self):
        for b, x, y, z in itertools.product(range(3), repeat=4):
            for r, v, u in itertools.product(maps(z, b), maps(y, z), maps(x, y)):
                q, p = comp(r, v), comp(comp(r, v), u)
                self.assertEqual(comp(r, comp(v, u)), p)
                self.assertEqual(comp(q, tuple(range(y))), q)

    def test_CAT_12_002_initial_terminal(self):
        for b, x in itertools.product(range(3), repeat=2):
            for p in maps(x, b):
                self.assertEqual([u for u in maps(x, b) if comp(tuple(range(b)), u) == p], [p])
                self.assertEqual([u for u in maps(0, x) if comp(p, u) == ()], [()])

    def test_CAT_12_003_fiber_reconstruction(self):
        for b, x, y in itertools.product(range(3), repeat=3):
            for p, q in itertools.product(maps(x, b), maps(y, b)):
                fibers = [tuple(i for i in range(x) if p[i] == j) for j in range(b)]
                targets = [tuple(i for i in range(y) if q[i] == j) for j in range(b)]
                families = itertools.product(*(itertools.product(t, repeat=len(f))
                                                for f, t in zip(fibers, targets)))
                reconstructed = set()
                for family in families:
                    pairs = {i: k for f, values in zip(fibers, family)
                             for i, k in zip(f, values)}
                    reconstructed.add(tuple(pairs[i] for i in range(x)))
                self.assertEqual(reconstructed, {u for u in maps(x, y) if comp(q, u) == p})

    def test_CAT_12_004_pullback_universal(self):
        for b, x, y, z in itertools.product(range(3), repeat=4):
            for p, q in itertools.product(maps(x, b), maps(y, b)):
                pairs = [(i, j) for i in range(x) for j in range(y) if p[i] == q[j]]
                px, py = (tuple(t[k] for t in pairs) for k in (0, 1))
                for u, v in itertools.product(maps(z, x), maps(z, y)):
                    lifts = [h for h in maps(z, len(pairs)) if comp(px, h) == u and comp(py, h) == v]
                    self.assertEqual(len(lifts), int(comp(p, u) == comp(q, v)))
                    if lifts:
                        self.assertEqual(comp(comp(p, px), lifts[0]), comp(p, u))

    def test_CAT_12_005_comma_composition(self):
        # F=G=Id: arrow category of finite sets.
        for x, y, z, a, b, c in itertools.product(range(3), repeat=6):
            for u, v, w, f, g, h, k in itertools.product(
                    maps(x, a), maps(y, b), maps(z, c),
                    maps(x, y), maps(a, b), maps(y, z), maps(b, c)):
                if comp(g, u) == comp(v, f) and comp(k, v) == comp(w, h):
                    self.assertEqual(comp(comp(k, g), u), comp(w, comp(h, f)))

    def test_CAT_12_006_structure(self):
        s = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        self.assertEqual(len(labels), len(set(labels)))
        for name in ("sec:slice", "def:slice", "cat:prop:slice-initial-terminal",
                     "cat:prop:slice-product", "cat:def:comma"):
            self.assertIn(name, labels)
        stack = []
        for cmd, env in re.findall(r"\\(begin|end)\{([^}]+)\}", s):
            if cmd == "begin":
                stack.append(env)
            else:
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
