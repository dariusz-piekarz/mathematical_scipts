"""CAT-37: finite operad models and structural regression checks."""
import itertools
import json
import re
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/37-operady-i-algebry-nad-operadami.tex"


def inverse(sigma):
    return tuple(sigma.index(i) for i in range(len(sigma)))


def permute(t, sigma):
    return tuple(t[i] for i in inverse(sigma))


def flatten(blocks):
    return tuple(x for block in blocks for x in block)


def compose_affine(e, f):
    a, b = e
    c, d = f
    return a + b*c, b*d


def substitute_intervals(outer, inner):
    return tuple(compose_affine(e, f)
                 for e, block in zip(outer, inner) for f in block)


class CategoryTheoryCh37(unittest.TestCase):
    def test_CAT_37_001_balanced_block_permutations(self):
        for k in range(5):
            for sigma in itertools.permutations(range(k)):
                for lengths in itertools.product(range(3), repeat=k):
                    blocks = tuple(tuple((i, j) for j in range(n))
                                   for i, n in enumerate(lengths))
                    source = flatten(blocks)
                    target = flatten(permute(blocks, sigma))
                    # D maps an index in the reordered list to its
                    # original index; D^{-1} acts on the original tensor.
                    D = tuple(source.index(x) for x in target)
                    self.assertEqual(permute(source, inverse(D)), target)
                    # Verify the right-action composition convention.
                    for tau in itertools.permutations(range(k)):
                        composite = tuple(sigma[tau[i]] for i in range(k))
                        self.assertEqual(permute(permute(blocks, tau), sigma),
                                         permute(blocks, composite))

    def test_CAT_37_002_little_intervals_homotopy(self):
        p = ((Fraction(0), Fraction(1, 2)),
             (Fraction(1, 2), Fraction(1, 2)))
        identity = ((Fraction(0), Fraction(1)),)
        left = substitute_intervals(p, (p, identity))
        right = substitute_intervals(p, (identity, p))
        self.assertNotEqual(left, right)
        for t in (Fraction(i, 20) for i in range(21)):
            u, v = (1+t)/4, (2+t)/4
            path = ((Fraction(0), u), (u, v-u), (v, 1-v))
            self.assertTrue(all(b > 0 and a >= 0 and a+b <= 1
                                for a, b in path))
            self.assertTrue(all(a+b <= c
                                for (a, b), (c, _) in zip(path, path[1:])))
            if t == 0:
                self.assertEqual(path, left)
            if t == 1:
                self.assertEqual(path, right)

    def test_CAT_37_003_barratt_eccles_freeness(self):
        for n in range(4):
            orders = tuple(itertools.permutations(range(n)))
            for m in range(3):
                for vertices in itertools.product(orders, repeat=m+1):
                    for sigma in orders:
                        moved = tuple(tuple(sigma[i] for i in o)
                                      for o in vertices)
                        self.assertEqual(moved == vertices,
                                         sigma == tuple(range(n)))

    def test_CAT_37_004_structure(self):
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
            self.assertTrue(s[match.end():].lstrip().startswith(r"\begin{proof}"),
                            match.group(1))
        chapter_path = CHAPTER.relative_to(ROOT).as_posix()
        self.assertIn(chapter_path, (ROOT / "books/pl/category_theory.tex").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
        self.assertIn(chapter_path, next(book for book in catalog["books"]
                                        if book["id"] == "category_theory")["chapters"])


if __name__ == "__main__":
    unittest.main()
