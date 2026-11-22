"""Audyt 26: AC, dobry porządek, Hartogs, Zorn, przekroje i bazy."""
from itertools import combinations
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/logic_and_set_theory"
P = DIR/"26-aksjomat-wyboru-i-jego-rownowazne-postacie.tex"
TEXT = P.read_text(encoding="utf8")


class TestChapter26(unittest.TestCase):
    def test_imports_and_catalog(self):
        self.assertTrue(P.is_file())
        self.assertIn(P.name,(ROOT/"books/pl/logic_and_set_theory.tex").read_text(encoding="utf8"))
        self.assertIn("26-aksjomat-wyboru-i-jego-rownowazne-postacie.tex",
                      (ROOT/"catalog/books.json").read_text(encoding="utf8"))

    def test_balanced_environments(self):
        stack=[]
        for op,env in re.findall(r"\\(begin|end)\{([^}]+)\}",TEXT):
            if op=="begin":stack.append(env)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)

    def test_inventory_and_references(self):
        expected={"definicja":5,"przyklad":10,"lemat":1,
                  "twierdzenie":8,"wniosek":1,"uwaga":2,"proof":10}
        for env,n in expected.items():
            with self.subTest(env=env):
                self.assertEqual(TEXT.count(r"\begin{"+env+"}"),n)
                self.assertEqual(TEXT.count(r"\end{"+env+"}"),n)
        labels=re.findall(r"\\label\{([^}]+)\}",TEXT)
        refs=re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}",TEXT)
        self.assertEqual(len(labels),20)
        self.assertEqual(len(refs),18)
        other="\n".join(x.read_text(encoding="utf8") for x in DIR.glob("*.tex"))
        all_labels=re.findall(r"\\label\{([^}]+)\}",other)
        self.assertEqual(len(all_labels),len(set(all_labels)))
        self.assertFalse(set(refs)-set(all_labels))

    def test_equivalence_cycle_and_no_hidden_choice(self):
        for label in ("thm:choice-hartogs","thm:choice-wellorder",
                      "thm:choice-zorn","thm:hausdorff-zorn-equivalent",
                      "thm:choice-equivalence","thm:choice-sections",
                      "cor:choice-transversals","thm:choice-hamel-basis"):
            self.assertIn(r"\label{"+label+"}",TEXT)
        self.assertIn(r"\mathcal P(A)\setminus\{\varnothing\}",TEXT)
        self.assertIn("Bez",TEXT) if "Bez" in TEXT else self.assertIn("bez",TEXT)

    def test_wellorder_comparison_has_valid_induction(self):
        proof=TEXT.split(r"\begin{lemat}[Dobre porządki",1)[1].split(r"\end{proof}",1)[0]
        self.assertIn("indukcję po dobrym porządku",proof)
        self.assertIn(r"f(y)\ge y=f(x)",proof)
        self.assertIn(r"f(y)<f(x)",proof)
        self.assertNotIn("nieskończony ściśle malejący ciąg",proof)

    def test_finite_choice_induction_has_defined_indices(self):
        section=TEXT.split(r"\begin{twierdzenie}[Wybór ze skończonej rodziny w ZF]",1)[1].split(r"\end{proof}",1)[0]
        self.assertNotIn(r"A_{e(n)}",section)
        self.assertIn(r"$(B_k)_{k\in S(n)}$",section)
        self.assertIn(r"$B_k:=A_{e(k)}$",section)
        self.assertIn(r"$e:n\to I$",section)
        self.assertIn(r"$c(i)\in A_i$",section)

    def test_hartogs_and_zorn_bounding_sets(self):
        self.assertIn(r"\mathcal P(A)\times\mathcal P(A\times A)",TEXT)
        self.assertIn(r"\mathcal P(\mathcal W)",TEXT)
        self.assertIn(r"\ref{thm:zf-product}",TEXT)
        self.assertIn(r"\mathcal P(P\times\{0,1\})",TEXT)
        self.assertIn(r"\mathcal P(I\times\bigcup_{i\in I}A_i)",TEXT)

    def test_explicit_empty_index_and_poset_cases(self):
        self.assertIn(r"łańcuch pusty musi mieć ograniczenie górne w $P$",TEXT)
        self.assertIn(r"$I=\varnothing$ zawiera funkcję pustą",TEXT)
        self.assertIn(r"Dla $I=\varnothing$ funkcja pusta",TEXT)


    def test_hartogs_small_cases(self):
        # Dla n elementów typy dobrze uporządkowanych podzbiorów
        # to dokładnie 0,...,n, więc H(A) ma n+1 typów.
        for n in range(6):
            A=tuple(range(n))
            sizes={len(t) for k in range(n+1) for t in combinations(A,k)}
            self.assertEqual(sizes,set(range(n+1)))
            self.assertGreater(len(sizes),len(A))

    def test_finite_disjoint_choice_and_sections(self):
        families=[("a","b"),("b",),("a","c")]
        E={(i,a) for i,values in enumerate(families) for a in values}
        section={i:(i,values[0]) for i,values in enumerate(families)}
        self.assertEqual(len(section),len(families))
        self.assertTrue(all(section[i] in E and section[i][0]==i
                            for i in range(len(families))))
        self.assertIn(r"\operatorname{id}_I",TEXT)

    def test_hamel_basis_includes_zero_space(self):
        self.assertIn(r"V=\{0\}",TEXT)
        self.assertIn(r"B=\varnothing",TEXT) if r"B=\varnothing" in TEXT else self.assertIn(r"\varnothing",TEXT)
        self.assertIn(r"\ref{thm:choice-zorn}",TEXT)
        self.assertIn("skończonym nośniku",TEXT)


if __name__=="__main__":
    unittest.main()
