"""Rozdział 24: diagramy, zwartość, elementarne łańcuchy, paradoks Skolema."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT/"chapters/pl/logic_and_set_theory"
PATH = DIR/"24-gorne-twierdzenie-lowenheima-skolema-i-paradoks-skolema.tex"
SOURCE = PATH.read_text(encoding="utf-8")


class TestLogicChapter24(unittest.TestCase):
    def test_imported_and_catalogued(self):
        self.assertTrue(PATH.is_file())
        self.assertIn(PATH.name, (ROOT/"books/pl/logic_and_set_theory.tex").read_text(encoding="utf-8"))
        self.assertIn(str(PATH.relative_to(ROOT)).replace("\\", "/"),
                      (ROOT/"catalog/books.json").read_text(encoding="utf-8"))

    def test_balanced_environments(self):
        stack = []
        for op, env in re.findall(r"\\(begin|end)\{([^}]+)\}", SOURCE):
            if op=="begin": stack.append(env)
            else:
                self.assertTrue(stack, env)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)

    def test_inventory(self):
        inv = {"definicja": 2, "uwaga": 6, "lemat": 2, "proof": 7,
               "twierdzenie": 4, "wniosek": 1, "przyklad": 2}
        for env,n in inv.items():
            with self.subTest(env=env):
                self.assertEqual(SOURCE.count(r"\begin{"+env+"}"),n)
                self.assertEqual(SOURCE.count(r"\end{"+env+"}"),n)

    def test_labels_and_references(self):
        labels=[]
        for p in DIR.glob("*.tex"):
            labels += re.findall(r"\\label\{([^}]+)\}",p.read_text(encoding="utf8"))
        own=re.findall(r"\\label\{([^}]+)\}",SOURCE)
        refs=re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}",SOURCE)
        self.assertEqual(len(own),18)
        self.assertEqual(len(refs),11)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertFalse(set(refs)-set(labels))

    def test_elementary_diagram_is_full(self):
        self.assertIn(r"\operatorname{ED}(\mathcal M)",SOURCE)
        self.assertIn("negacjami", SOURCE)
        self.assertIn("kwantyfikatorami", SOURCE)
        self.assertIn(r"j(a):=c_a^{\mathcal B}",SOURCE)

    def test_upper_model_has_all_four_steps(self):
        proof = SOURCE.split(r"\begin{twierdzenie}[Górne twierdzenie",1)[1].split(r"\end{proof}",1)[0]
        for n in range(1,5):
            self.assertIn(f"Etap {n}",proof)
        self.assertIn(r"\operatorname{ED}(\mathcal M)",proof)
        self.assertIn(r"\ref{thm:compactness}",proof)
        self.assertIn(r"\ref{thm:downward-ls}",proof)
        self.assertIn(r"\mathcal M\preccurlyeq\mathcal N",proof)
        self.assertIn(r"|N|=|C|=\lambda",proof)

    def test_finite_fragment_of_new_constants(self):
        # Każdy skończony podzbiór indeksów da się obsadzić
        # różnymi elementami dowolnego nieskończonego modelu.
        for n in range(13):
            representatives=list(range(n))
            self.assertEqual(len(set(representatives)),n)
        self.assertIn("skończony",SOURCE)
        self.assertIn("parami różne",SOURCE)

    def test_chain_uses_finite_stage_and_quantifier_argument(self):
        section = SOURCE.split(r"\begin{lemat}[Suma rosnącego ciągu",1)[1].split(r"\end{proof}",1)[0]
        self.assertIn("największy", section) if "największy" in section else self.assertIn("maksimum", section)
        self.assertIn(r"\exists y\,\theta(y,\vec a)", section)
        self.assertIn("Przechodniość elementarności", section)

    def test_true_arithmetic_nonstandard_c(self):
        p=SOURCE.split(r"\begin{twierdzenie}[Przeliczalny niestandardowy model",1)[1].split(r"\end{proof}",1)[0]
        self.assertIn(r"\operatorname{Th}(\mathfrak N)",p)
        self.assertIn(r"\overline n<c",p)
        self.assertIn(r"\ref{thm:compactness}",p)
        self.assertIn(r"\ref{cor:downward-countable}",p)

    def test_internal_vs_external_and_second_order(self):
        for z in ("E_r", "Zewnętrzne wyliczenie", "wewnętrznym",
                  r"\ref{sec:second-order-introduction}",
                  r"\ref{cor:downward-countable}",
                  "semantyce Henkina"):
            self.assertIn(z, SOURCE)
        self.assertIn(r"E:=\{e(n):n\in\N\}",SOURCE)


if __name__=="__main__":
    unittest.main()
