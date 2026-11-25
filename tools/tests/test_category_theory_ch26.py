"""CAT-26: finite poset models and source structure, not formal proofs."""
import itertools
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/26-rozszerzenia-kana.tex"


class CategoryTheoryCh26(unittest.TestCase):
    def test_CAT_26_001_pointwise_poset_adjunction(self):
        # A finite chain, B finite chain, C a four-element chain.
        # Nat is pointwise order. Empty supremum = 0, infimum = 3.
        A = range(3)
        B = range(4)
        C = range(4)
        monotone = lambda n, values: list(
            itertools.combinations_with_replacement(values, n))
        maps = monotone(len(A), C)
        targets = monotone(len(B), C)
        le = lambda f, g: all(x <= y for x, y in zip(f, g))
        for K in monotone(len(A), B):
            for F in maps:
                L = tuple(max((F[a] for a in A if K[a] <= b), default=0)
                          for b in B)
                R = tuple(min((F[a] for a in A if b <= K[a]), default=3)
                          for b in B)
                self.assertIn(L, targets)
                self.assertIn(R, targets)
                self.assertTrue(le(F, tuple(L[K[a]] for a in A)))
                self.assertTrue(le(tuple(R[K[a]] for a in A), F))
                for H in targets:
                    HK = tuple(H[K[a]] for a in A)
                    self.assertEqual(le(L, H), le(F, HK))
                    self.assertEqual(le(H, R), le(HK, F))

    def test_CAT_26_002_structure(self):
        source = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", source)
        self.assertEqual(len(labels), len(set(labels)))
        all_labels = []
        for p in CHAPTER.parent.glob("*.tex"):
            all_labels.extend(re.findall(r"\\label\{([^}]+)\}",
                                         p.read_text(encoding="utf-8")))
        for ref in re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", source):
            self.assertEqual(all_labels.count(ref), 1, ref)
        stack = []
        for kind, env in re.findall(r"\\(begin|end)\{([^}]+)\}", source):
            if kind == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack, env)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        for m in re.finditer(r"\\end\{(twierdzenie|stwierdzenie|lemat|wniosek)\}",
                             source):
            self.assertTrue(source[m.end():].lstrip().startswith(r"\begin{proof}"))
        book = (ROOT / "books/pl/category_theory.tex").read_text(encoding="utf-8")
        self.assertIn(CHAPTER.relative_to(ROOT).as_posix(), book)


if __name__ == "__main__":
    unittest.main()
