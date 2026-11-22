"""Logic chapter 29: weaker choice principles, Baire, BPI and Tychonoff."""
from pathlib import Path
from itertools import product, combinations
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/logic_and_set_theory"
FILE = DIR / "29-slabsze-zasady-wyboru-i-ich-ograniczenia.tex"
TEXT = FILE.read_text(encoding="utf8")


class TestChapter29(unittest.TestCase):
    def test_book_and_catalog(self):
        self.assertIn(FILE.name, (ROOT/"books/pl/logic_and_set_theory.tex").read_text("utf8"))
        self.assertIn(FILE.name, (ROOT/"catalog/books.json").read_text("utf8"))
        self.assertIn(r"\label{ch:weak-choice}",TEXT)

    def test_inventory_and_balanced_environments(self):
        expected={"definicja":6,"twierdzenie":7,"proof":8,"lemat":1,
                  "przyklad":5,"uwaga":7}
        for env,count in expected.items():
            with self.subTest(env=env):
                self.assertEqual(TEXT.count(r"\begin{"+env+"}"),count)
                self.assertEqual(TEXT.count(r"\end{"+env+"}"),count)
        stack=[]
        for kind,env in re.findall(r"\\(begin|end)\{([^}]+)\}",TEXT):
            if kind=="begin":
                stack.append(env)
            else:
                self.assertTrue(stack,env)
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)
        labels=re.findall(r"\\label\{([^}]+)\}",TEXT)
        self.assertEqual(len(labels),24)
        self.assertEqual(len(labels),len(set(labels)))

    def test_all_references_resolve(self):
        labels=set()
        for f in DIR.glob("*.tex"):
            labels.update(re.findall(r"\\label\{([^}]+)\}",f.read_text("utf8")))
        refs=re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}",TEXT)
        self.assertEqual(len(refs),11)
        self.assertFalse(set(refs)-labels)

    def test_all_full_book_sections_retained(self):
        for label in (
            "thm:choice-chain","thm:countable-union-cc",
            "thm:weak-choice-baire-dc","ex:weak-choice-baire-noncomplete",
            "rem:weak-choice-baire-dc","def:bpi-boolean-filter",
            "lem:bpi-ultrafilter-criterion","thm:bpi-ultrafilter-equivalence",
            "thm:bpi-tychonoff-hausdorff","thm:ac-full-tychonoff",
            "thm:tukey-equivalent-ac","rem:bpi-vs-ac"):
            with self.subTest(label=label):
                self.assertIn(r"\label{"+label+"}",TEXT)
        self.assertIn("Twierdzenie Baire'a z DC",TEXT)

    def test_baire_uses_closed_ball_containment(self):
        self.assertIn(r"\overline B(z_0,r_0)\subseteq U\cap D_0",TEXT)
        self.assertIn(r"\overline B(z_{i+1},r_{i+1})",TEXT)
        self.assertIn(r"\overline B(z_m,r_m)",TEXT)
        self.assertIn(r"\subseteq B(z_{m-1},r_{m-1})\cap D_m",TEXT)
        self.assertIn("kula jest domknięta",TEXT)
        self.assertIn(r"x\in U\cap\bigcap_{i\in\omega}D_i",TEXT)
        self.assertIn(r"X\setminus\overline{F_n}",TEXT)

    def test_boolean_filter_and_ultrafilter_finite_cases(self):
        S=frozenset(range(3))
        subsets={frozenset(k for k in S if mask&(1<<k)) for mask in range(2**len(S))}
        def proper_filter(F):
            return (S in F and frozenset() not in F
                    and all(a & b in F for a in F for b in F)
                    and all(b in F for a in F for b in subsets if a<=b))
        proper=[]
        items=list(subsets)
        for mask in range(2**len(items)):
            F={items[k] for k in range(len(items)) if (mask>>k)&1}
            if proper_filter(F):
                proper.append(F)
        for F in proper:
            maximal=not any(F < G for G in proper)
            decides=all((b in F) != ((S-b) in F) for b in subsets)
            self.assertEqual(maximal,decides)
        self.assertEqual(len([F for F in proper if all((b in F) != ((S-b) in F) for b in subsets)]),3)

    def test_prime_ideals_are_ultrafilter_complements(self):
        S=frozenset(range(3))
        all_subsets=[frozenset(x for x in S if mask&(1<<x))
                     for mask in range(1<<len(S))]
        for mask in range(1<<len(all_subsets)):
            I={a for j,a in enumerate(all_subsets) if (mask>>j)&1}
            ideal=(frozenset() in I and S not in I
                   and all(a|b in I for a in I for b in I)
                   and all(b in I for a in I for b in all_subsets if b<=a))
            prime=ideal and all((a in I or b in I)
                                for a in all_subsets for b in all_subsets
                                if a&b in I)
            U=set(all_subsets)-I
            ultra=(S in U and frozenset() not in U
                   and all((a in U) != ((S-a) in U) for a in all_subsets))
            self.assertEqual(prime,ultra)
        self.assertIn("Ideałem właściwym",TEXT)
        self.assertIn("pierwszy",TEXT)
        self.assertIn("dopełnieniem",TEXT)

    def test_dc_finite_prefixes_form_a_coherent_graph(self):
        A=[set([0,1]),set([2,3]),set([4,5])]
        prefixes={()}
        for values in A:
            next_prefixes={s+(v,) for s in prefixes for v in values}
            self.assertEqual(len(next_prefixes),len(prefixes)*2)
            for s in prefixes:
                self.assertEqual(len([t for t in next_prefixes if t[:-1]==s]),2)
            prefixes=next_prefixes
        self.assertEqual(len(prefixes),8)
        self.assertTrue(all(p[k] in A[k] for p in prefixes for k in range(3)))

    def test_tychonoff_uses_canonical_tagged_points(self):
        self.assertIn(r"\widehat A_i:=A_i\times\{0\}",TEXT)
        self.assertIn(r"\infty_i:=(i,1)",TEXT)
        self.assertIn(r"\ref{thm:choice-finite-family}",TEXT)
        self.assertIn(r"\pi_i",TEXT)
        self.assertIn(r"i\mapsto a_i",TEXT)
        self.assertIn("przez zastępowanie",TEXT)

    def test_tukey_finite_character_on_partial_choice(self):
        E={(i,v) for i in range(3) for v in (0,1)}
        elements=list(E)
        def is_partial_function(F):
            return len({i for i,v in F})==len(F)
        for mask in range(1<<len(elements)):
            F={elements[i] for i in range(len(elements)) if mask & (1<<i)}
            all_finite=all(is_partial_function(G) for k in range(len(F)+1)
                           for G in map(set,combinations(F,k)))
            self.assertEqual(is_partial_function(F),all_finite)

    def test_hausdorff_vs_nonhausdorff_compact_example(self):
        # Tau={empty,A,{infinity},A union {infinity}}
        A=frozenset(range(3))
        inf="infinity"
        X=A|frozenset({inf})
        topology={frozenset(),A,frozenset({inf}),X}
        self.assertTrue(all(any(any(x in U for U in cover) for x in X)
                            for cover in [topology]))
        # Dwa punkty z A nie mają rozłącznych otoczeń.
        for a,b in combinations(A,2):
            self.assertFalse(any(U.isdisjoint(V) for U in topology for V in topology
                                 if a in U and b in V))
        self.assertIn(A,topology)
        self.assertIn(frozenset({inf}),topology)

    def test_tychonoff_and_choice_not_conflated(self):
        self.assertIn("Hausdorffa",TEXT)
        self.assertIn(r"\mathrm{BPI}",TEXT)
        self.assertIn(r"\mathrm{AC}_{\omega}",TEXT)
        self.assertIn(r"\mathrm{DC}",TEXT)
        self.assertIn(r"\mathrm{AC}\Rightarrow\mathrm{DC}",TEXT)
        self.assertIn("niehausdorffowskie",TEXT)
        self.assertIn("skończony charakter",TEXT)


if __name__ == "__main__":
    unittest.main()
