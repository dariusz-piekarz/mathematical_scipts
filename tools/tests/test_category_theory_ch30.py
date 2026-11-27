"""CAT-30: finite topos models and structural regression checks."""
import itertools
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/30-toposy-elementarne-i-toposy-grothendiecka.tex"


def subobjects(n, m, r):
    # A presheaf on V -> U is a function r: F(U) -> F(V).
    return [(frozenset(i for i in range(n) if a & (1 << i)),
             frozenset(j for j in range(m) if b & (1 << j)))
            for a in range(1 << n) for b in range(1 << m)
            if all(not (a & (1 << i)) or b & (1 << j)
                   for i, j in enumerate(r))]


def le(a, b):
    return a[0] <= b[0] and a[1] <= b[1]


def meet(a, b):
    return a[0] & b[0], a[1] & b[1]


def implication(a, b, n, m, r):
    v = (frozenset(range(m)) - a[1]) | b[1]
    u = frozenset(i for i in range(n)
                  if (i not in a[0] or i in b[0]) and r[i] in v)
    return u, v


def lift(a):
    # Omega(U) = empty, proper, maximal; Omega(V) = empty, maximal.
    return (frozenset(3*i+j for i in a[0] for j in range(3)),
            frozenset(2*i+j for i in a[1] for j in range(2)))


def forall_omega(a, n, m, r):
    v = frozenset(i for i in range(m)
                  if all(2*i+j in a[1] for j in range(2)))
    u = frozenset(i for i in range(n) if r[i] in v
                  and all(3*i+j in a[0] for j in range(3)))
    return u, v


class CategoryTheoryCh30(unittest.TestCase):
    def test_CAT_30_001_heyting_quantified_constructions(self):
        for n, m in itertools.product(range(3), repeat=2):
            for r in itertools.product(range(m), repeat=n):
                subs = subobjects(n, m, r)
                product_r = tuple(2*i+j for i in r for j in (0, 1, 1))
                q = (frozenset(3*i+2 for i in range(n)),
                     frozenset(2*i+1 for i in range(m)))
                self.assertEqual(forall_omega(q, n, m, r),
                                 (frozenset(), frozenset()))
                for a, b in itertools.product(subs, repeat=2):
                    d = implication(a, b, n, m, r)
                    left = implication(lift(a), q, 3*n, 2*m, product_r)
                    right = implication(lift(b), q, 3*n, 2*m, product_r)
                    rel = implication(meet(left, right), q, 3*n, 2*m, product_r)
                    join = forall_omega(rel, n, m, r)
                    self.assertEqual(join, (a[0] | b[0], a[1] | b[1]))
                    for c in subs:
                        self.assertEqual(le(c, d), le(meet(c, a), b))
                        self.assertEqual(le(c, join), le(lift(c), rel))

    def test_CAT_30_002_structure(self):
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
        for match in re.finditer(r"\\end\{(twierdzenie|stwierdzenie|lemat|wniosek)\}", s):
            self.assertTrue(s[match.end():].lstrip().startswith(r"\begin{proof}"))
        chapter_path = CHAPTER.relative_to(ROOT).as_posix()
        self.assertIn(chapter_path, (ROOT / "books/pl/category_theory.tex").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
        self.assertIn(chapter_path, next(book for book in catalog["books"]
                                        if book["id"] == "category_theory")["chapters"])


if __name__ == "__main__":
    unittest.main()
