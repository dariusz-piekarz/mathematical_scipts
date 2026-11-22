"""Audyt 28: ordynały, supremum, indukcja, rekurencja i kardynały."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/logic_and_set_theory"
SRC = DIR / "28-liczby-porzadkowe-i-rekurencja-pozaskonczona.tex"
TEXT = SRC.read_text(encoding="utf8")


class TestChapter28(unittest.TestCase):
    def test_registered(self):
        self.assertIn(SRC.name, (ROOT/"books/pl/logic_and_set_theory.tex").read_text("utf8"))
        self.assertIn(SRC.name, (ROOT/"catalog/books.json").read_text("utf8"))
        self.assertIn(r"\label{ch:ordinals}", TEXT)

    def test_balanced_environments(self):
        stack=[]
        for op,env in re.findall(r"\\(begin|end)\{([^}]+)\}",TEXT):
            if op=="begin":
                stack.append(env)
            else:
                self.assertTrue(stack,env)
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)

    def test_complete_original_inventory(self):
        counts={"definicja":4,"przyklad":5,"lemat":2,
                "twierdzenie":5,"wniosek":1,"uwaga":3,"proof":8}
        for env,count in counts.items():
            with self.subTest(env=env):
                self.assertEqual(TEXT.count(r"\begin{"+env+"}"),count)
                self.assertEqual(TEXT.count(r"\end{"+env+"}"),count)
        labels=re.findall(r"\\label\{([^}]+)\}",TEXT)
        self.assertEqual(len(labels),17)
        self.assertEqual(len(labels),len(set(labels)))

    def test_required_material(self):
        for label in ("lem:ordinal-segments","thm:ordinal-trichotomy",
                      "cor:ordinal-sup","lem:ordinal-limit-union",
                      "thm:ordinal-induction","thm:ordinal-recursion",
                      "ex:ordinal-addition","ex:ordinal-vn-hierarchy",
                      "def:ordinal-multiplication","ex:ordinal-mul-noncommutative",
                      "thm:initial-exists","thm:burali-forti"):
            with self.subTest(label=label):
                self.assertIn(r"\label{"+label+"}",TEXT)

    def test_all_cross_references_resolve(self):
        files=list(DIR.glob("*.tex"))
        labels=set()
        for file in files:
            labels.update(re.findall(r"\\label\{([^}]+)\}",file.read_text("utf8")))
        refs=re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}",TEXT)
        self.assertEqual(len(refs),18)
        self.assertFalse(set(refs)-labels)

    def test_ordinal_successors_and_unions_on_finite_models(self):
        # 0,...,6 jako zbiory przechodnie von Neumanna.
        n=frozenset()
        numbers=[]
        for i in range(7):
            numbers.append(n)
            n=n|frozenset({n})
        for i in range(6):
            self.assertEqual(numbers[i]|frozenset({numbers[i]}),numbers[i+1])
        for i in range(7):
            self.assertEqual(frozenset().union(*numbers[:i]),numbers[max(i-1,0)])
        for i in range(1,7):
            self.assertEqual(frozenset().union(*numbers[:i+1]),numbers[i])
        for i in range(7):
            self.assertFalse(numbers[i] in numbers[i])

    def test_successor_and_limit_case_distinguished(self):
        self.assertIn(r"\bigcup_{\beta<\lambda}\beta",TEXT)
        self.assertIn("niezerowym ordynałem granicznym",TEXT)
        self.assertIn("następnikiem",TEXT)
        self.assertIn("przechodniość",TEXT)

    def test_recursion_uses_replacement_not_class_set(self):
        self.assertIn(r"schemat zastępowania daje zbiór",TEXT)
        self.assertIn(r"\mathcal G=\{g_\delta:\delta<\beta\}",TEXT)
        self.assertIn(r"\ref{lem:ordinal-limit-union}",TEXT)
        self.assertIn(r"\gamma+1<\beta",TEXT)
        self.assertIn("Nie zakładamy istnienia wspólnego",TEXT)

    def test_wellorder_representation_no_hidden_choice(self):
        self.assertIn("To jedyne miejsce w konstrukcji",TEXT)
        self.assertIn(r"\mathcal F_w:=\{f_v:v\prec w\}",TEXT)
        self.assertIn(r"f_w:=u\cup\{(w,u[W_{<w}])\}",TEXT)
        self.assertIn(r"r[W]",TEXT)
        self.assertIn("wbrew aksjomatowi ufundowania",TEXT)
        self.assertIn(r"r(u)\in r(v)",TEXT)

    def test_small_ordinal_arithmetic(self):
        # Operacje na ordynałach skończonych pokrywają się z N.
        def oadd(alpha,beta):
            z=alpha
            for _ in range(beta):
                z+=1
            return z
        def omul(alpha,beta):
            z=0
            for _ in range(beta):
                z=oadd(z,alpha)
            return z
        for a in range(8):
            for b in range(8):
                self.assertEqual(oadd(a,b),a+b)
                self.assertEqual(omul(a,b),a*b)
        self.assertIn(r"2\cdot\omega",TEXT)
        self.assertIn(r"\omega\cdot2",TEXT)
        self.assertIn(r"\aleph_0",TEXT)

    def test_burali_forti_non_set(self):
        self.assertIn(r"\gamma\in\gamma",TEXT)
        self.assertIn(r"\bigcup O",TEXT)
        self.assertIn("nie jest zbiorem",TEXT)


if __name__=="__main__":
    unittest.main()
