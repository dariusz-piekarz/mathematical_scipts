"""CAT-40 regression checks. Finite models supplement, not replace, proofs."""
import itertools
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/40-kategorie-dostepne-i-lokalnie-prezentowalne.tex"


def classes(nodes, relations):
    """Equivalence classes of a finite presentation."""
    parent = {x: x for x in nodes}

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for a, b in relations:
        parent[find(a)] = find(b)
    result = {}
    for x in parent:
        result.setdefault(find(x), set()).add(x)
    return {frozenset(c) for c in result.values()}


def functions(n, m):
    return itertools.product(range(m), repeat=n)


class CategoryTheoryCh40(unittest.TestCase):
    def test_CAT_40_001_filtered_equalizer(self):
        # A chain of two stages, with a possibly noninjective transition.
        # Compare colimit of equalizers with equalizer of colimits.
        for n, m in itertools.product(range(4), repeat=2):
            for transition in functions(n, m):
                for f, g in itertools.product(functions(2, n), repeat=2):
                    early = {i for i in range(2) if f[i] == g[i]}
                    late = {i for i in range(2)
                            if transition[f[i]] == transition[g[i]]}
                    nodes = {(0, i) for i in early} | {(1, i) for i in late}
                    quotient = classes(nodes, [((0, i), (1, i)) for i in early])
                    self.assertEqual({i for c in quotient for stage, i in c if stage == 1}, late)
                    self.assertTrue(all(sum(stage == 1 for stage, _ in c) == 1
                                        for c in quotient))

    def test_CAT_40_002_presheaf_elements(self):
        # Base category 0 -> 1. A presheaf is a function F(1) -> F(0).
        # At 0, the representable colimit identifies each tagged F(1)
        # element with its restriction in F(0); at 1 it is discrete.
        for a, b in itertools.product(range(5), repeat=2):
            for restriction in functions(b, a):
                nodes = {(0, x) for x in range(a)} | {(1, y) for y in range(b)}
                q0 = classes(nodes, [((1, y), (0, x))
                                     for y, x in enumerate(restriction)])
                expected = {frozenset({(0, x)} | {(1, y)
                            for y in range(b) if restriction[y] == x})
                            for x in range(a)}
                self.assertEqual(q0, expected)
                q1 = classes([(1, y) for y in range(b)], [])
                self.assertEqual(q1, {frozenset({(1, y)}) for y in range(b)})
                self.assertTrue(all(any(c1 <= c0 for c0 in q0) for c1 in q1))

    def test_CAT_40_003_orthogonality_reflector(self):
        # Orthogonality to the fold 2 -> 1 and universal factorization.
        for n in range(6):
            diagonal = {(x, x) for x in range(n)}
            self.assertEqual(diagonal == set(functions(2, n)), n <= 1)
            r = int(n > 0)
            eta = (0,) * n
            for m in (0, 1):
                extensions = list(functions(r, m))
                for f in functions(n, m):
                    self.assertEqual(sum(tuple(h[x] for x in eta) == f
                                         for h in extensions), 1)
                self.assertEqual({tuple(h[x] for x in eta) for h in extensions},
                                 set(functions(n, m)))

    def test_CAT_40_004_structure(self):
        s = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        refs = re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", s)
        catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
        book = next(b for b in catalog["books"] if b["id"] == "category_theory")
        entry = (ROOT / book["entrypoint"]).read_text(encoding="utf-8")
        path = CHAPTER.relative_to(ROOT).as_posix()
        self.assertIn(path, book["chapters"])
        self.assertIn(path, entry)
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
        self.assertGreaterEqual(len(statements), 24)
        for match in statements:
            self.assertTrue(s[match.end():].lstrip().startswith(r"\begin{proof}"),
                            match.group(0)[:120])


if __name__ == "__main__":
    unittest.main()
