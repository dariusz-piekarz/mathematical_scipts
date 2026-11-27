"""CAT-38: finite descent and noncommutative cocycle regressions."""
import itertools
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/38-teoria-zstepowania-i-stosy.tex"


def mul(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def inv(p):
    return tuple(p.index(i) for i in range(len(p)))


class CategoryTheoryCh38(unittest.TestCase):
    def test_CAT_38_001_set_descent(self):
        # Surjection V -> U, including empty sets in the fibers.
        for n in range(4):
            for m in range(3):
                for u in itertools.product(range(m), repeat=n):
                    if set(u) != set(range(m)):
                        continue
                    for sizes in itertools.product(range(3), repeat=m):
                        options = [tuple(itertools.permutations(range(sizes[t])))
                                   for t in u]
                        for gauges in itertools.product(*options):
                            # theta_vw = gauge_v gauge_w^{-1}.
                            points = [(v, a) for v, t in enumerate(u)
                                      for a in range(sizes[t])]
                            def theta(v, w, a):
                                return mul(gauges[v], inv(gauges[w]))[a]
                            classes = {
                                (v, a): frozenset((w, b) for w, b in points
                                                 if u[v] == u[w]
                                                 and a == theta(v, w, b))
                                for v, a in points
                            }
                            for t in range(m):
                                quotient = {classes[v, a] for v, a in points
                                            if u[v] == t}
                                self.assertEqual(len(quotient), sizes[t])
                                for v in range(n):
                                    if u[v] == t:
                                        self.assertEqual(
                                            {classes[v, a] for a in range(sizes[t])},
                                            quotient)
                            for v, a in points:
                                for w, b in classes[v, a]:
                                    self.assertEqual(classes[v, a], classes[w, b])

    def test_CAT_38_002_noncommutative_cocycle(self):
        group = tuple(itertools.permutations(range(3)))
        identity = tuple(range(3))
        for gauges in itertools.product(group, repeat=3):
            trans = {(i, j): mul(gauges[i], inv(gauges[j]))
                     for i, j in itertools.product(range(3), repeat=2)}
            for i, j, k in itertools.product(range(3), repeat=3):
                self.assertEqual(mul(trans[i, j], trans[j, k]), trans[i, k])
                self.assertEqual(trans[i, i], identity)
                self.assertEqual(inv(trans[i, j]), trans[j, i])
            # Change local trivializations by a noncommuting family.
            for change in itertools.product(group, repeat=3):
                updated = {(i, j): mul(mul(change[i], trans[i, j]), inv(change[j]))
                           for i, j in trans}
                for i, j in trans:
                    self.assertEqual(mul(change[i], trans[i, j]),
                                     mul(updated[i, j], change[j]))
                for i, j, k in itertools.product(range(3), repeat=3):
                    self.assertEqual(mul(updated[i, j], updated[j, k]),
                                     updated[i, k])

    def test_CAT_38_003_action_groupoid(self):
        group = tuple(itertools.permutations(range(3)))
        for y, a, b, h in itertools.product(range(3), group, group, group):
            yp = a[y]
            ypp = b[yp]
            self.assertEqual(inv(mul(a, h))[yp], inv(h)[y])
            self.assertEqual(inv(mul(b, mul(a, h)))[ypp], inv(h)[y])
            self.assertEqual(mul(b, a)[y], ypp)
        for y in range(3):
            self.assertEqual(sum(a[y] == y for a in group), 2)

    def test_CAT_38_004_structure(self):
        s = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        self.assertEqual(len(labels), len(set(labels)))
        all_labels = [label for f in CHAPTER.parent.glob("*.tex")
                      for label in re.findall(r"\\label\{([^}]+)\}",
                                              f.read_text(encoding="utf-8"))]
        for label in labels + re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", s):
            self.assertEqual(all_labels.count(label), 1, label)
        stack = []
        for cmd, env in re.findall(r"\\(begin|end)\{([^}]+)\}", s):
            if cmd == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack, env)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        for match in re.finditer(r"\\begin\{(twierdzenie|stwierdzenie|lemat|wniosek)\}(.*?)\\end\{\1\}",
                                 s, re.S):
            if "wynik zewnętrzny" in match.group(2).splitlines()[0]:
                continue
            self.assertTrue(s[match.end():].lstrip().startswith(r"\begin{proof}"),
                            match.group(2)[:100])
        chapter_path = CHAPTER.relative_to(ROOT).as_posix()
        self.assertIn(chapter_path, (ROOT / "books/pl/category_theory.tex").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
        self.assertIn(chapter_path, next(book for book in catalog["books"]
                                        if book["id"] == "category_theory")["chapters"])


if __name__ == "__main__":
    unittest.main()
