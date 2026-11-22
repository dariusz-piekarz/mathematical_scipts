"""Audyt 25: aksjomaty ZF, liczby von Neumanna, rekursja i arytmetyka."""
from itertools import product
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/logic_and_set_theory"
P = DIR / "25-aksjomaty-zf-zfc-i-konstrukcje-zbiorowe.tex"
TEXT = P.read_text(encoding="utf-8")


class TestChapter25(unittest.TestCase):
    def test_imports_and_catalog(self):
        self.assertTrue(P.is_file())
        self.assertIn(P.name, (ROOT/"books/pl/logic_and_set_theory.tex").read_text(encoding="utf8"))
        self.assertIn(P.as_posix().split("chapters/",1)[-1],
                      (ROOT/"catalog/books.json").read_text(encoding="utf8"))

    def test_balanced_environments(self):
        stack = []
        for op,name in re.findall(r"\\(begin|end)\{([^}]+)\}",TEXT):
            if op=="begin": stack.append(name)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),name)
        self.assertFalse(stack)

    def test_inventory_and_structure(self):
        expected = {"definicja":16,"przyklad":14,"lemat":6,"twierdzenie":11,
                    "wniosek":2,"uwaga":5,"proof":19,"figure":1}
        for env,count in expected.items():
            with self.subTest(env=env):
                self.assertEqual(TEXT.count(r"\begin{"+env+"}"),count)
                self.assertEqual(TEXT.count(r"\end{"+env+"}"),count)
        self.assertEqual(len(re.findall(r"\\label\{([^}]+)\}",TEXT)),46)
        self.assertEqual(len(re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}",TEXT)),23)

    def test_labels_resolved_with_all_chapters(self):
        all_text = "\n".join(p.read_text(encoding="utf8") for p in sorted(DIR.glob("*.tex")))
        labels = re.findall(r"\\label\{([^}]+)\}",all_text)
        self.assertEqual(len(labels),len(set(labels)))
        refs = re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}",TEXT)
        self.assertFalse(set(refs)-set(labels))

    def test_zf_axiom_family_and_no_ac_in_arithmetic(self):
        for label in ("def:zf-extensionality","def:zf-pairing","def:zf-union",
                      "def:zf-power","def:zf-separation","def:zf-replacement",
                      "def:zf-infinity","def:zf-foundation",
                      "thm:zf-cantor","thm:zf-omega","thm:zf-omega-recursion"):
            self.assertIn(r"\label{"+label+"}",TEXT)
        assert r"\ref{ch:axiom-choice}" in TEXT
        self.assertIn("bez aksjomatu wyboru",TEXT)

    def test_arithmetic_dependency_order(self):
        labels = ["thm:zf-omega", "lem:zf-vn-successor",
                  "thm:zf-omega-recursion","def:zf-addition",
                  "thm:zf-add-assoc-comm","def:zf-multiplication",
                  "thm:zf-distributivity","thm:zf-mult-assoc-comm",
                  "def:zf-natural-order","thm:zf-wellordered-omega",
                  "thm:zf-division"]
        offsets=[TEXT.index(r"\label{"+x+"}") for x in labels]
        self.assertEqual(offsets,sorted(offsets))

    def test_successor_iteration_matches_von_neumann(self):
        n=frozenset()
        omega=[]
        for i in range(7):
            omega.append(n)
            self.assertEqual(len(n),i)
            n=n|frozenset({n})
        self.assertEqual(len(set(omega)),7)
        for i in range(7):
            self.assertFalse(omega[i] in omega[i])

    def test_recursive_arithmetic_on_small_range(self):
        # Potwierdza zgodność definicji rekurencyjnych z działaniami na N.
        def add(a,b):
            z=a
            for _ in range(b): z+=1
            return z
        def mul(a,b):
            z=0
            for _ in range(b): z=add(z,a)
            return z
        for a,b,c in product(range(5),repeat=3):
            self.assertEqual(add(add(a,b),c),add(a,add(b,c)))
            self.assertEqual(mul(a,add(b,c)),add(mul(a,b),mul(a,c)))
        for a in range(20):
            for b in range(1,8):
                sols=[(q,r) for q in range(22) for r in range(b)
                      if a==b*q+r]
                self.assertEqual(len(sols),1)


if __name__ == "__main__":
    unittest.main()
