"""CAT-29: finite site models and structural regression checks."""
import itertools
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/29-presnopy-snopy-i-topologie-grothendiecka.tex"


def below(u, opens=range(4)):
    return tuple(v for v in opens if v & u == v)


def covers(u, space=range(4)):
    """Covering sieves on a finite topology, including the empty sieve."""
    opens = below(u, space)
    for bits in itertools.product((False, True), repeat=len(opens)):
        r = frozenset(v for v, bit in zip(opens, bits) if bit)
        union = 0
        for v in r:
            union |= v
        if union == u and all(set(below(v, space)) <= r for v in r):
            yield r


def families(values, restrict, r):
    opens = sorted(r)
    for items in itertools.product(*(values[v] for v in opens)):
        x = dict(zip(opens, items))
        if all(restrict(v, w, x[v]) == x[w] for v in r for w in below(v, values)):
            yield tuple(zip(opens, items))


def plus(values, restrict):
    representatives = {
        u: tuple((r, x) for r in covers(u, values) for x in families(values, restrict, r))
        for u in values
    }

    def equivalent(u, p, q):
        r, x = p
        s, y = q
        return any(t <= r & s and all(dict(x)[v] == dict(y)[v] for v in t)
                   for t in covers(u, values))

    classes = {
        u: frozenset(frozenset(q for q in representatives[u] if equivalent(u, p, q))
                     for p in representatives[u])
        for u in values
    }

    def locate(u, p):
        return next(c for c in classes[u] if p in c)

    def restriction(u, v, c):
        r, x = next(iter(c))
        rr = r & frozenset(below(v, values))
        return locate(v, (rr, tuple((w, s) for w, s in x if w in rr)))

    def unit(u, s):
        r = frozenset(below(u, values))
        return locate(u, (r, tuple((v, restrict(u, v, s)) for v in sorted(r))))

    return classes, restriction, unit


def sheaf_condition(values, restrict, injective_only=False):
    for u in values:
        for r in covers(u, values):
            images = [tuple((v, restrict(u, v, s)) for v in sorted(r))
                      for s in values[u]]
            if len(set(images)) != len(images):
                return False
            if not injective_only and set(images) != set(families(values, restrict, r)):
                return False
    return True


class CategoryTheoryCh29(unittest.TestCase):
    def test_CAT_29_001_site_axioms(self):
        for u in range(4):
            self.assertIn(frozenset(below(u)), set(covers(u)))
            for r in covers(u):
                for v in below(u):
                    self.assertIn(r & frozenset(below(v)), set(covers(v)))
                for s in covers(u):
                    self.assertIn(r & s, set(covers(u)))
        self.assertIn(frozenset(), set(covers(0)))

    def test_CAT_29_002_constant_presheaf_plus(self):
        values = {0: (0,), 1: (0, 1), 2: (0, 1), 3: (0, 1)}
        restrict = lambda u, v, s: s if v else 0
        self.assertTrue(sheaf_condition(values, restrict, True))
        self.assertFalse(sheaf_condition(values, restrict))
        p, rp, unit = plus(values, restrict)
        self.assertTrue(sheaf_condition(p, rp))
        self.assertEqual([len(p[u]) for u in range(4)], [1, 2, 2, 4])
        self.assertNotEqual(unit(3, 0), unit(3, 1))

    def test_CAT_29_003_nonseparated_presheaf_plus(self):
        values = {0: (0,), 1: (0,), 2: (0,), 3: (0, 1)}
        restrict = lambda u, v, s: s if u == v else 0
        self.assertFalse(sheaf_condition(values, restrict, True))
        p, rp, unit = plus(values, restrict)
        self.assertEqual(unit(3, 0), unit(3, 1))
        self.assertTrue(sheaf_condition(p, rp, True))
        pp, rpp, _ = plus(p, rp)
        self.assertTrue(sheaf_condition(pp, rpp))

    def test_CAT_29_004_representables_on_discrete_space(self):
        for a in range(4):
            values = {u: (0,) if u & a == u else () for u in range(4)}
            self.assertTrue(sheaf_condition(values, lambda u, v, s: s))

    def test_CAT_29_006_two_plus_steps_really_needed(self):
        # Opens of the four-point example: c=4, d=8, A=13, B=14.
        values = {0: (0,), 4: (0,), 8: (0,), 12: (0, 1),
                  13: (0,), 14: (0,), 15: ()}

        def restrict(u, v, s):
            if u == v:
                return s
            if u == 14 and v == 12:
                return 1
            return 0

        for u in values:
            for v in below(u, values):
                for w in below(v, values):
                    for x in values[u]:
                        self.assertEqual(restrict(v, w, restrict(u, v, x)),
                                         restrict(u, w, x))
        p, rp, _ = plus(values, restrict)
        self.assertEqual([len(p[u]) for u in (12, 13, 14, 15)], [1, 1, 1, 0])
        self.assertTrue(sheaf_condition(p, rp, True))
        self.assertFalse(sheaf_condition(p, rp))
        pp, rpp, _ = plus(p, rp)
        self.assertEqual(len(pp[15]), 1)
        self.assertTrue(sheaf_condition(pp, rpp))

    def test_CAT_29_005_structure(self):
        s = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        self.assertEqual(len(labels), len(set(labels)))
        all_labels = [label for f in CHAPTER.parent.glob("*.tex")
                      for label in re.findall(r"\\label\{([^}]+)\}",
                                              f.read_text(encoding="utf-8"))]
        for ref in re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", s):
            self.assertEqual(all_labels.count(ref), 1, ref)
        stack = []
        for cmd, env in re.findall(r"\\(begin|end)\{([^}]+)\}", s):
            if cmd == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack, env)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        for m in re.finditer(r"\\end\{(twierdzenie|stwierdzenie|lemat|wniosek)\}", s):
            self.assertTrue(s[m.end():].lstrip().startswith(r"\begin{proof}"))
        self.assertNotIn(r"\begin{CD}", s)
        chapter_path = CHAPTER.relative_to(ROOT).as_posix()
        self.assertIn(chapter_path, (ROOT/"books/pl/category_theory.tex").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT/"catalog/books.json").read_text(encoding="utf-8"))
        self.assertIn(chapter_path, next(b for b in catalog["books"]
                                        if b["id"] == "category_theory")["chapters"])


if __name__ == "__main__":
    unittest.main()
