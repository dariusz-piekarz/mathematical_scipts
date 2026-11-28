"""CAT-41 finite regression models; these do not replace mathematical proofs."""
import itertools
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/41-teorie-algebraiczne-lawverea.tex"


def words(n, length=3):
    return [w for k in range(length + 1)
            for w in itertools.product(range(n), repeat=k)]


def substitute(word, values):
    return tuple(x for i in word for x in values[i])


class CategoryTheoryCh41(unittest.TestCase):
    def test_CAT_41_001_list_substitution(self):
        for n in range(3):
            for m in range(3):
                for s in itertools.product(words(n, 2), repeat=m):
                    for t in words(m, 2):
                        for r in itertools.product(words(2, 1), repeat=n):
                            self.assertEqual(substitute(substitute(t, s), r),
                                             substitute(t, tuple(substitute(x, r) for x in s)))
                projections = tuple((i,) for i in range(n))
                for w in words(n):
                    self.assertEqual(substitute(w, projections), w)

    def test_CAT_41_002_list_to_finite_powerset(self):
        # The support map is a monad morphism: substitution becomes union.
        for n, m in itertools.product(range(3), repeat=2):
            for s in itertools.product(words(n, 2), repeat=m):
                for t in words(m):
                    self.assertEqual(set(substitute(t, s)),
                                     set().union(*(set(s[i]) for i in set(t))))
        for i in range(4):
            self.assertEqual(set((i,)), {i})

    def test_CAT_41_003_empty_context(self):
        # Variable-only theory, including the empty model and empty product.
        for n, m in itertools.product(range(5), repeat=2):
            self.assertEqual(len(list(itertools.product(range(n), repeat=m))), n ** m)
        self.assertEqual(words(0), [()])  # list monad has a nullary unit
        self.assertEqual(list(itertools.product(range(0), repeat=1)), [])

    def test_CAT_41_004_retract_coequalizer(self):
        # For finite sets, a split idempotent's image coequalizes id and e.
        for n in range(5):
            for e in itertools.product(range(n), repeat=n):
                if any(e[e[i]] != e[i] for i in range(n)):
                    continue
                image = sorted(set(e))
                for h in itertools.product(range(2), repeat=n):
                    if any(h[e[i]] != h[i] for i in range(n)):
                        continue
                    extensions = [k for k in itertools.product(range(2), repeat=len(image))
                                  if all(k[image.index(e[i])] == h[i] for i in range(n))]
                    self.assertEqual(extensions, [tuple(h[x] for x in image)])

    def test_CAT_41_006_finite_powerset_merging(self):
        # Finite direct images need not be injective. For a two-stage
        # filtered diagram, equivalence is detected at the common stage.
        def subsets(n):
            return [frozenset(i for i in range(n) if mask & (1 << i))
                    for mask in range(1 << n)]

        for n, m in itertools.product(range(4), repeat=2):
            for f in itertools.product(range(m), repeat=n):
                early, late = subsets(n), subsets(m)
                def image(a):
                    return frozenset(f[i] for i in a)

                classes = {b: {(1, b)} for b in late}
                for a in early:
                    classes[image(a)].add((0, a))
                self.assertEqual(set(classes), set(late))
                for a, b in itertools.product(early, repeat=2):
                    self.assertEqual(any((0, a) in q and (0, b) in q
                                         for q in classes.values()),
                                     image(a) == image(b))
                self.assertTrue(all(sum(stage == 1 for stage, _ in q) == 1
                                    for q in classes.values()))

    def test_CAT_41_005_structure(self):
        s = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        refs = re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", s)
        catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
        book = next(b for b in catalog["books"] if b["id"] == "category_theory")
        path = CHAPTER.relative_to(ROOT).as_posix()
        self.assertIn(path, book["chapters"])
        self.assertIn(path, (ROOT / book["entrypoint"]).read_text(encoding="utf-8"))
        all_labels = Counter(label for p in book["chapters"]
                             for label in re.findall(r"\\label\{([^}]+)\}",
                                                     (ROOT / p).read_text(encoding="utf-8")))
        for label in labels + refs:
            self.assertEqual(all_labels[label], 1, label)
        stack = []
        for cmd, env in re.findall(r"\\(begin|end)\{([^}]+)\}", s):
            if cmd == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack, env)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        statements = list(re.finditer(
            r"\\begin\{(twierdzenie|stwierdzenie|lemat|wniosek)\}.*?\\end\{\1\}", s, re.S))
        self.assertGreaterEqual(len(statements), 12)
        for match in statements:
            self.assertTrue(s[match.end():].lstrip().startswith(r"\begin{proof}"),
                            match.group(0)[:120])


if __name__ == "__main__":
    unittest.main()
