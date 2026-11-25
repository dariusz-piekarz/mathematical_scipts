"""CAT-15: finite models of monads and their algebras."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/15-monady-jak-opisac-konstrukcje-swobodna-na-jednym-poziomie.tex"


def lists(xs, maxlen=2):
    return [w for n in range(maxlen+1) for w in itertools.product(xs, repeat=n)]


def flat(xs):
    return tuple(x for w in xs for x in w)


def subsets(xs):
    xs = tuple(xs)
    return [frozenset(xs[i] for i in range(len(xs)) if mask >> i & 1)
            for mask in range(1 << len(xs))]


class CategoryTheoryCh15(unittest.TestCase):
    def test_CAT_15_001_list_laws(self):
        words = lists((0, 1))
        for w in words:
            self.assertEqual(flat((w,)), w)
            self.assertEqual(flat(tuple((x,) for x in w)), w)
        blocks = lists(words)
        for w in lists(blocks):
            self.assertEqual(flat(tuple(flat(b) for b in w)), flat(flat(w)))

    def test_CAT_15_002_powerset_laws(self):
        for n in range(3):
            ps = subsets(range(n))
            pps = subsets(ps)
            def union(xs):
                return frozenset(x for a in xs for x in a)
            for a in ps:
                self.assertEqual(union((a,)), a)
                self.assertEqual(union(frozenset((x,)) for x in a), a)
            for a in subsets(pps):
                self.assertEqual(union(union(a)), union(union(b) for b in a))

    def test_CAT_15_003_kleisli_list(self):
        words = lists((0, 1), 1)
        funcs = list(itertools.product(words, repeat=2))
        identity = ((0,), (1,))
        def star(g, f):
            return tuple(flat(tuple(g[i] for i in w)) for w in f)
        for f in funcs:
            self.assertEqual(star(identity, f), f)
            self.assertEqual(star(f, identity), f)
        for f, g, h in itertools.product(funcs, repeat=3):
            self.assertEqual(star(h, star(g, f)), star(star(h, g), f))

    def test_CAT_15_004_list_algebra_noncommutative(self):
        # S3, with composition in the order written.
        group = tuple(itertools.permutations(range(3)))
        identity = tuple(range(3))
        def mul(g, f):
            return tuple(g[i] for i in f)
        def alg(word):
            r = identity
            for g in word:
                r = mul(r, g)
            return r
        for g in group:
            self.assertEqual(alg((g,)), g)
        blocks = lists(group)
        for pair in itertools.product(blocks, repeat=2):
            self.assertEqual(alg(flat(pair)), alg(tuple(alg(w) for w in pair)))
        self.assertNotEqual(mul((1,0,2), (0,2,1)), mul((0,2,1), (1,0,2)))

    def test_CAT_15_005_structure(self):
        s = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        self.assertEqual(len(labels), len(set(labels)))
        for name in ("sec:monads", "def:monad", "przyklad:list-monad",
                     "przyklad:powerset-monad", "cat:thm:adjunction-monad",
                     "cat:def:kleisli", "cat:prop:kleisli-adj",
                     "cat:def:em-algebra", "cat:prop:em-adj", "cat:ex:list-algebras"):
            self.assertIn(name, labels)
        stack = []
        for cmd, env in re.findall(r"\\(begin|end)\{([^}]+)\}", s):
            if cmd == "begin":
                stack.append(env)
            else:
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
