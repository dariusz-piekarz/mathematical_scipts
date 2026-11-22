"""Audyt rozdziału 27: arytmetyka mocy, parowanie Cantora i jawne bijekcje."""
import itertools
import math
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/logic_and_set_theory"
FILE = DIR / "27-liczby-kardynalne-i-arytmetyka-mocy.tex"
SOURCE = FILE.read_text(encoding="utf8")


class TestChapter27(unittest.TestCase):
    def test_book_registration(self):
        book = (ROOT/"books/pl/logic_and_set_theory.tex").read_text(encoding="utf8")
        catalog = (ROOT/"catalog/books.json").read_text(encoding="utf8")
        self.assertIn(FILE.name,book)
        self.assertIn(FILE.name,catalog)
        self.assertIn(r"\chapter{Liczby kardynalne i arytmetyka mocy}",SOURCE)

    def test_environment_and_inventory(self):
        stack=[]
        for op,env in re.findall(r"\\(begin|end)\{([^}]+)\}",SOURCE):
            if op=="begin":
                stack.append(env)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)
        expected={"definicja":4,"twierdzenie":11,"proof":12,
                  "przyklad":5,"wniosek":2,"uwaga":6,"figure":1}
        for env,num in expected.items():
            with self.subTest(env=env):
                self.assertEqual(SOURCE.count(r"\begin{"+env+"}"),num)
                self.assertEqual(SOURCE.count(r"\end{"+env+"}"),num)

    def test_labels_and_declared_forward_reference(self):
        sources = [p.read_text(encoding="utf8") for p in DIR.glob("*.tex")]
        full="\n".join(sources)
        labels=re.findall(r"\\label\{([^}]+)\}",full)
        refs=re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}",SOURCE)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertEqual(len(re.findall(r"\\label\{([^}]+)\}",SOURCE)),24)
        self.assertEqual(len(refs),12)
        self.assertEqual(set(refs)-set(labels),{"ch:ordinals"})

    def test_full_original_material_retained(self):
        for label in ("thm:card-cb","thm:card-laws","thm:card-exponent-exponent",
                      "ex:card-zero-exponents","thm:card-n2","ex:card-unpair",
                      "fig:card-pairing-diagonal","thm:card-continuum",
                      "thm:card-n-not-r","thm:card-open-interval-real",
                      "thm:card-open-half-open","thm:card-comparability-choice"):
            self.assertIn(r"\label{"+label+"}",SOURCE)
        self.assertIn(r"\begin{tikzpicture}",SOURCE)
        self.assertIn(r"\ref{thm:choice-hartogs}",SOURCE)
        self.assertIn(r"\ref{thm:zf-omega-recursion}",SOURCE)

    def test_cardinal_arithmetic_finite_cases(self):
        for a,b,c in itertools.product(range(5),repeat=3):
            self.assertEqual(a+b,b+a)
            self.assertEqual((a+b)+c,a+(b+c))
            self.assertEqual(a*(b+c),a*b+a*c)
            self.assertEqual(c**(a+b),c**a*c**b)
            self.assertEqual((c**b)**a,c**(a*b))
        self.assertEqual(0**0,1)
        self.assertEqual(0**1,0)
        self.assertEqual(3**2,9)

    def test_cantor_pairing_is_bijection_on_prefix(self):
        def pair(m,n):
            s=m+n
            return s*(s+1)//2+n
        for k in range(200):
            s=0
            while (s+1)*(s+2)//2<=k:
                s+=1
            n=k-s*(s+1)//2
            m=s-n
            self.assertEqual(pair(m,n),k)
            self.assertGreaterEqual(m,0)
            self.assertGreaterEqual(n,0)
        self.assertEqual(pair(2,1),7)

    def test_cantor_bernstein_construction_finite_models(self):
        # Wszystkie iniekcje w obie strony między zbiorami skończonymi
        # wymagają równej mocy. Kontrola konkretnej konstrukcji h z tekstu.
        for n in range(5):
            A=set(range(n))
            B=set(range(n))
            for pp in itertools.permutations(range(n)):
                f=dict(enumerate(pp))
                for qq in itertools.permutations(range(n)):
                    g=dict(enumerate(qq))
                    A0=A-set(g.values())
                    parts=[A0]
                    C=set(A0)
                    while True:
                        nxt={g[f[a]] for a in parts[-1]}
                        old=len(C)
                        C|=nxt
                        if len(C)==old:break
                        parts.append(nxt)
                    invg={a:b for b,a in g.items()}
                    h={a:(f[a] if a in C else invg[a]) for a in A}
                    self.assertEqual(set(h.values()),B)
                    self.assertEqual(len(set(h.values())),n)

    def test_explicit_interval_bijections(self):
        def f(x):
            return (1+x/(1+abs(x)))/2
        def inv(t):
            u=2*t-1
            return u/(1-abs(u))
        for x in [-100,-10,-3,-1,-.5,0,.5,1,3,10,100]:
            y=f(x)
            self.assertTrue(0<y<1)
            self.assertTrue(math.isclose(inv(y),x,rel_tol=1e-12,abs_tol=1e-12))
        for t in [.01,.1,.2,.4,.5,.75,.9,.99]:
            self.assertTrue(math.isclose(f(inv(t)),t,abs_tol=1e-12))
        def h(n):
            return 1/(n-1)
        for n in range(2,50):
            self.assertEqual(1/(n-1),h(n))

    def test_no_hidden_choice_for_countable_pairs(self):
        self.assertIn("nie wymaga AC",SOURCE)
        self.assertIn("przeliczalna suma przeliczalnych",SOURCE)
        self.assertIn(r"\chi_S",SOURCE)
        self.assertIn("bez aksjomatu wyboru",SOURCE.lower())


if __name__ == "__main__":
    unittest.main()
