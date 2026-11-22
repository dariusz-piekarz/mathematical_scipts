"""Chapter 30: infinite games, AD, PD and Wadge reductions."""
from pathlib import Path
import itertools
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/logic_and_set_theory"
FILE = DIR / "30-gry-nieskonczone-i-aksjomat-determinacji.tex"
TEXT = FILE.read_text(encoding="utf8")


class TestChapter30(unittest.TestCase):
    def test_registered(self):
        self.assertIn(FILE.name,(ROOT/"books/pl/logic_and_set_theory.tex").read_text("utf8"))
        self.assertIn(FILE.name,(ROOT/"catalog/books.json").read_text("utf8"))
        self.assertIn(r"\label{ch:determinacy}",TEXT)

    def test_environment_inventory_and_balance(self):
        expected={"definicja":12,"przyklad":7,"twierdzenie":15,
                  "lemat":9,"wniosek":4,"uwaga":15,"proof":26,
                  "figure":1,"tikzpicture":1}
        for env,count in expected.items():
            with self.subTest(env=env):
                self.assertEqual(TEXT.count(r"\begin{"+env+"}"),count)
                self.assertEqual(TEXT.count(r"\end{"+env+"}"),count)
        stack=[]
        for op,env in re.findall(r"\\(begin|end)\{([^}]+)\}",TEXT):
            if op=="begin":
                stack.append(env)
            else:
                self.assertTrue(stack,env)
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)
        labels=re.findall(r"\\label\{([^}]+)\}",TEXT)
        self.assertEqual(len(labels),57)
        self.assertEqual(len(set(labels)),len(labels))

    def test_all_references_resolve_in_existing_chapters(self):
        labels=set()
        for path in DIR.glob("*.tex"):
            labels.update(re.findall(r"\\label\{([^}]+)\}",path.read_text("utf8")))
        refs=re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}",TEXT)
        self.assertEqual(len(refs),49)
        self.assertEqual(set(refs)-labels,set())

    def test_original_pdf_full_material(self):
        for label in (
            "def:game-a","def:strategy-ad","def:baire-cylinders",
            "thm:open-determinacy","ex:ad-two-step-quantifiers",
            "fig:ad-two-moves","cor:closed-determinacy",
            "thm:ac-not-ad","lem:ad-countable-choice-reals",
            "lem:ad-meager-countable-union","lem:ad-baire-category",
            "lem:ad-banach-mazur-category","thm:ad-baire-property",
            "thm:ad-perfect-set","thm:ad-no-wellorder-reals",
            "lem:ad-covering-game","thm:ad-measurability",
            "thm:pd-regularity","thm:martin-steel-projective",
            "thm:martin-steel-woodin-lr","thm:pd-projective-wadge",
            "thm:wadge-open-complete","thm:wadge-closed-complete",
            "thm:wadge-strategy-continuity",
            "thm:wadge-clopen-selfdual"):
            with self.subTest(label=label):
                self.assertIn(r"\label{"+label+"}",TEXT)

    def test_open_and_closed_determinacy_are_zf(self):
        self.assertIn("Już w ZF, bez aksjomatu wyboru",TEXT)
        self.assertIn(r"\label{cor:closed-determinacy}"+"\nW ZF",TEXT)
        self.assertIn(r"\ref{thm:choice-hartogs}",TEXT)
        self.assertIn(r"\ref{thm:ordinal-recursion}",TEXT)
        self.assertIn("najmniejszego",TEXT)
        self.assertIn("ściśle malejący",TEXT)

    def test_two_step_game_minimax(self):
        # A: pierwszy gracz gra 0, drugi gracz ma zagrać niezerowo.
        choices=range(3)
        A=lambda u,v: u==0 and v!=0
        for u in choices:
            self.assertFalse(A(u,0))
        self.assertFalse(any(all(A(u,v) for v in choices) for u in choices))
        self.assertTrue(all(any(not A(u,v) for v in choices) for u in choices))

    def test_ad_perfect_set_game_strategy_construction(self):
        self.assertIn(r"\label{thm:ad-perfect-set}",TEXT)
        self.assertIn(r"\theta:\omega^\omega\to D\subseteq2^\omega",TEXT)
        self.assertIn(r"0^{n_0}1",TEXT)
        self.assertIn(r"f[2^\omega]",TEXT)
        self.assertIn(r"przestrzeń $2^\omega$ jest zwarta",TEXT.lower())
        # Przy dowolnym binarnym prefiksie u znajdują się dwa różne przedłużenia.
        for length in range(6):
            for prefix in itertools.product((0,1),repeat=length):
                a=prefix+(0,)*3
                b=prefix+(1,)*3
                self.assertNotEqual(a,b)
                self.assertEqual(a[:length],b[:length])

    def test_countable_union_meager_has_real_codes(self):
        self.assertIn(r"\label{lem:ad-meager-countable-union}",TEXT)
        self.assertIn(r"\label{lem:ad-countable-choice-reals}",TEXT)
        self.assertIn(r"T_F:=\{s\in T:[s]\cap F\ne\varnothing\}",TEXT)
        self.assertIn(r"c_n\in C_n",TEXT)
        self.assertIn(r"\omega^2",TEXT)

    def test_canonical_baire_in_reals_no_dc(self):
        self.assertIn(r"\overline{I_{n+1}}",TEXT)
        self.assertIn(r"\operatorname{diam}(I_n)",TEXT)
        self.assertIn("pierwszą",TEXT)
        self.assertIn(r"\ref{lem:ad-meager-countable-union}",TEXT)

    def test_baire_and_regularity_dependencies(self):
        self.assertIn(r"\ref{lem:ad-meager-countable-union}",TEXT)
        self.assertIn(r"\ref{thm:ad-perfect-set}",TEXT)
        self.assertIn(r"\ref{thm:ad-measurability}",TEXT)
        self.assertIn(r"\ref{lem:ad-covering-game}",TEXT)
        self.assertIn(r"\label{lem:projective-same-reals}",TEXT)

    def test_wadge_continuity_and_semi_linearity(self):
        self.assertIn(r"\label{thm:pd-projective-wadge}",TEXT)
        self.assertIn(r"A\leq_{\mathrm W}B",TEXT)
        self.assertIn(r"B\leq_{\mathrm W}",TEXT)
        self.assertIn(r"\label{thm:wadge-open-complete}",TEXT)
        self.assertIn(r"\label{thm:wadge-closed-complete}",TEXT)
        self.assertIn("gracz II ma strategię wygrywającą",TEXT)
        # Zbiór U: istnieje niezerowa współrzędna.
        def U(x):return any(z!=0 for z in x)
        for n in range(1,8):
            self.assertFalse(U((0,)*n))
            self.assertTrue(U((0,)*(n-1)+(1,)))

    def test_open_wadge_completeness_is_justified(self):
        self.assertIn(r"\label{thm:wadge-open-complete}",TEXT)
        self.assertIn(r"\label{thm:wadge-open-nonselfdual}",TEXT)
        self.assertIn(r"U_0=f^{-1}[U]",TEXT)
        self.assertIn(r"(f\circ g)^{-1}[U]",TEXT)
        self.assertIn("który nie jest domknięty",TEXT)
        self.assertIn(r"U_0=f^{-1}[V]",TEXT)
        self.assertIn("Już w ZF zachodzą następujące fakty",TEXT)

    def test_lebesgue_measurability_assumptions_and_proof_scope(self):
        # The classical AD conclusion is stronger than the AD+DC proof
        # supplied here; the headings and explanatory notes must agree.
        self.assertIn(
            r"\section{Mierzalność w sensie Lebesgue'a przy AD i DC}", TEXT
        )
        self.assertIn(
            r"\begin{twierdzenie}[Mierzalność zbiorów liczb rzeczywistych przy AD i DC]", TEXT
        )
        self.assertIn(
            r"$\mathrm{ZF}+\mathrm{DC}+\mathrm{AD}$", TEXT
        )
        self.assertIn("Nie jest samodzielnym dowodem tego wyniku", TEXT)
        self.assertIn("nie jest tutaj przedstawiany jako udowodniony", TEXT)
        self.assertIn(r"\label{rem:ad-analytic-input}", TEXT)

    def test_global_choice_not_conflated_with_ad(self):
        self.assertIn(r"\mathrm{AD}",TEXT)
        self.assertIn("sprzeczny z AC",TEXT)
        self.assertIn(r"L(\R)\models\mathrm{AD}",TEXT)
        self.assertIn("bez aksjomatu wyboru",TEXT)


if __name__=="__main__":
    unittest.main()
