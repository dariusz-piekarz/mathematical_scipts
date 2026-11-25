"""CAT-11: finite exponential objects and transposition."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/11-obiekty-wykladnicze-i-przestrzenie-odwzorowan.tex"


def maps(n, m):
    return itertools.product(range(m), repeat=n)


def compose(g, f):
    return tuple(g[i] for i in f)


def curry(f, x, a):
    return tuple(tuple(f[i*a+j] for j in range(a)) for i in range(x))


class CategoryTheoryCh11(unittest.TestCase):
    def test_CAT_11_001_curry_bijection(self):
        for x, a, b in itertools.product(range(4), repeat=3):
            fs = list(maps(x*a, b))
            got = {curry(f, x, a) for f in fs}
            expected = set(itertools.product(tuple(maps(a, b)), repeat=x))
            self.assertEqual(got, expected)
            self.assertEqual(len(got), len(fs))
            for f in fs:
                self.assertEqual(tuple(v for row in curry(f, x, a) for v in row), f)

    def test_CAT_11_002_naturality_x(self):
        for x, y, a, b in itertools.product(range(3), repeat=4):
            for r, f in itertools.product(maps(y, x), maps(x*a, b)):
                pre = tuple(f[r[i]*a+j] for i in range(y) for j in range(a))
                self.assertEqual(curry(pre, y, a), compose(curry(f, x, a), r))

    def test_CAT_11_003_change_arguments(self):
        for a, ap, b, c in itertools.product(range(3), repeat=4):
            for r, g, h in itertools.product(maps(ap, a), maps(b, c), maps(a, b)):
                self.assertEqual(compose(g, compose(h, r)), compose(compose(g, h), r))

    def test_CAT_11_004_boolean_poset(self):
        universe = set(range(4))
        subsets = [set(i for i in universe if mask & (1 << i)) for mask in range(16)]
        for a, b, x in itertools.product(subsets, repeat=3):
            self.assertEqual(x & a <= b, x <= (universe-a) | b)

    def test_CAT_11_005_zero_object_obstruction(self):
        for p in (2, 3, 5, 7):
            endos = [tuple(c*x % p for x in range(p)) for c in range(p)]
            self.assertGreater(len(set(endos)), 1)
            self.assertEqual(len(list(maps(0, p))), 1)

    def test_CAT_11_006_exponential_laws(self):
        for a, b, c, d in itertools.product(range(4), repeat=4):
            self.assertEqual((b*c)**a, b**a * c**a)
            self.assertEqual((b**a)**d, b**(a*d))
            self.assertEqual(b**1, b)
            self.assertEqual(1**a, 1)

    def test_CAT_11_007_finite_discrete_topology(self):
        for a, b in itertools.product(range(4), repeat=2):
            functions = list(maps(a, b))
            for f in functions:
                intersection = set(functions)
                for i, value in enumerate(f):
                    intersection &= {h for h in functions if h[i] == value}
                self.assertEqual(intersection, {f})
            for f, i in itertools.product(functions, range(a)):
                self.assertIn(f[i], range(b))

    def test_CAT_11_008_structure(self):
        s = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        self.assertEqual(len(labels), len(set(labels)))
        for name in ("sec:exponentials", "def:exponential", "przyklad:exponential-set",
                     "cat:thm:exp-unique", "cat:thm:exp-naturality", "cat:prop:exp-argument",
                     "cat:ex:exp-zero", "cat:thm:exp-top", "cat:prop:exp-laws"):
            self.assertIn(name, labels)
        stack = []
        for cmd, env in re.findall(r"\\(begin|end)\{([^}]+)\}", s):
            if cmd == "begin":
                stack.append(env)
            else:
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
