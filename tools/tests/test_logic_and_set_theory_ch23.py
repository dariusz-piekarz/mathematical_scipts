"""Rozdział 23: regresja konstrukcji domknięcia Skolema i dolnego L-S.
Testy skończone są pomocnicze; nie zastępują dowodu dla dowolnych mocy.
"""
import re
import unittest
from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/logic_and_set_theory"
PATH = DIR / "23-dolne-twierdzenie-lowenheima-skolema-i-domkniecia-skolema.tex"
SOURCE = PATH.read_text(encoding="utf-8")


class TestLogicChapter23(unittest.TestCase):
    def test_imported_and_catalogued(self):
        self.assertTrue(PATH.is_file())
        self.assertIn(PATH.name, (ROOT/"books/pl/logic_and_set_theory.tex").read_text(encoding="utf-8"))
        self.assertIn(str(PATH.relative_to(ROOT)).replace("\\", "/"),
                      (ROOT/"catalog/books.json").read_text(encoding="utf-8"))

    def test_balanced_environments(self):
        stack = []
        for op, env in re.findall(r"\\(begin|end)\{([^}]+)\}", SOURCE):
            if op == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack, env)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)

    def test_inventory(self):
        inv = {"definicja": 3, "uwaga": 3, "lemat": 2, "proof": 4,
               "twierdzenie": 1, "wniosek": 1, "przyklad": 2}
        for env, n in inv.items():
            with self.subTest(env=env):
                self.assertEqual(SOURCE.count(r"\begin{" + env + "}"), n)
                self.assertEqual(SOURCE.count(r"\end{" + env + "}"), n)

    def test_labels_and_references(self):
        all_labels = []
        for f in DIR.glob("*.tex"):
            all_labels.extend(re.findall(r"\\label\{([^}]+)\}", f.read_text(encoding="utf8")))
        refs = re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", SOURCE)
        own = re.findall(r"\\label\{([^}]+)\}", SOURCE)
        self.assertEqual(len(own), 12)
        self.assertEqual(len(refs), 9)
        self.assertEqual(len(all_labels), len(set(all_labels)))
        self.assertFalse(set(refs) - set(all_labels))

    def test_skolem_choice_and_total_function(self):
        self.assertIn(r"F_\theta:M^k\to M", SOURCE)
        self.assertIn("najmniejszy w tym porządku", SOURCE)
        self.assertIn(r"m_*\in M", SOURCE)
        self.assertIn("Nie dodajemy ich symboli", SOURCE)

    def test_hull_has_induction_and_tarski_vaught(self):
        self.assertIn(r"X_{n+1}", SOURCE)
        self.assertIn(r"\bigcup_{n\in\N}X_n", SOURCE)
        self.assertIn(r"\ref{thm:model-tarski-vaught}", SOURCE)
        self.assertIn(r"f^{\mathcal M}(\vec a)\in N", SOURCE)

    def test_cardinal_estimates_have_choice_qualification(self):
        for snippet in (r"\aleph_0\cdot\kappa=\kappa",
                        r"\kappa\cdot\kappa=\kappa",
                        r"|X_{n+1}|\le\kappa+\kappa=\kappa",
                        r"\kappa\le\lambda\le |M|"):
            self.assertIn(snippet, SOURCE)
        self.assertIn("aksjomatu wyboru", SOURCE)

    def test_q_has_no_sqrt_two_in_small_rational_sample(self):
        vals = [Fraction(p,q) for p in range(-20,21)
                for q in range(1,21)]
        self.assertFalse(any(x*x == 2 for x in vals))
        self.assertIn(r"\mathcal Q", SOURCE)
        self.assertIn(r"\mathcal K\preccurlyeq\mathcal R", SOURCE)

    def test_limitation_non_effectivity(self):
        self.assertIn("nie jest algorytmem", SOURCE)
        self.assertIn("nie musimy umieć rozstrzygać", SOURCE)


if __name__ == "__main__":
    unittest.main()
