"""CAT-18: glossary and synthesis coverage."""
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/18-slownik-oznaczen-i-krotkie-podsumowanie.tex"


class CategoryTheoryCh18(unittest.TestCase):
    def test_CAT_18_001_glossary_coverage(self):
        s = CHAPTER.read_text(encoding="utf-8")
        for token in (r"\Hom_{\mathcal C}", r"\mathcal C^{\op}",
                      r"\Nat(F,G)", r"h^A=\Hom(A,-)", r"h_A=\Hom(-,A)",
                      r"\mathcal P_+", r"\int F", r"B^A", r"(F\downarrow G)",
                      r"F\dashv G", r"(T,\eta,\mu)", r"\mathcal C_T",
                      r"\mathcal C^T", r"\Ker f", r"\pi_0(X)"):
            self.assertIn(token, s)

    def test_CAT_18_002_local_references(self):
        s = CHAPTER.read_text(encoding="utf-8")
        labels = {}
        for path in CHAPTER.parent.glob("*.tex"):
            for label in re.findall(r"\\label\{([^}]+)\}", path.read_text(encoding="utf-8")):
                labels.setdefault(label, []).append(path.name)
        refs = re.findall(r"\\ref\{([^}]+)\}", s)
        self.assertGreaterEqual(len(set(refs)), 20)
        for label in refs:
            self.assertEqual(len(labels.get(label, [])), 1, label)

    def test_CAT_18_003_structure(self):
        s = CHAPTER.read_text(encoding="utf-8")
        stack = []
        for cmd, env in re.findall(r"\\(begin|end)\{([^}]+)\}", s):
            if cmd == "begin":
                stack.append(env)
            else:
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertIn("sec:slownik", labels)
        self.assertEqual(s.count(r"\begin{tabular}"), 6)
