"""Regression tests for the stable abstract-algebra chapter AA-01."""
from itertools import permutations
from math import gcd
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/abstract_algebra/01-grupy-podgrupy-i-grupy-cykliczne.tex"
BOOK = ROOT / "books/pl/abstract_algebra.tex"


class AbstractAlgebraChapter01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = CHAPTER.read_text(encoding="utf-8")

    def test_labels_and_proofs(self):
        labels = re.findall(r"\\label\{([^}]+)\}", self.text)
        self.assertEqual(len(labels), 24)
        self.assertEqual(len(set(labels)), 24)
        self.assertTrue(all(label.startswith("aa:") for label in labels))
        self.assertEqual(self.text.count(r"\begin{proof}"), 12)
        self.assertEqual(self.text.count(r"\end{proof}"), 12)

    def test_dependencies_and_book_import(self):
        self.assertNotRegex(self.text, r"\\(?:input|include|includegraphics|lstinputlisting)\b")
        self.assertIn(r"\input{../../chapters/pl/abstract_algebra/01-grupy-podgrupy-i-grupy-cykliczne.tex}",
                      BOOK.read_text(encoding="utf-8"))

    def test_sign_of_permutations(self):
        def mul(p, q):
            return tuple(p[q[i]] for i in range(len(p)))
        def sign(p):
            return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
        for n in range(1, 5):
            perms = list(permutations(range(n)))
            for sigma in perms:
                for tau in perms:
                    self.assertEqual(sign(mul(sigma, tau)), sign(sigma) * sign(tau))

    def test_cyclic_subgroups(self):
        for n in range(1, 31):
            for k in range(-n, n + 1):
                generated = {(j * k) % n for j in range(n)}
                self.assertEqual(len(generated), n // gcd(n, k))


if __name__ == "__main__":
    unittest.main()
