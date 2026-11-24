import re
import unittest
from pathlib import Path
from fractions import Fraction as F
from itertools import product

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/functional_analysis"
SOURCE = next(DIR.glob("25-*.tex"))

class Chapter25(unittest.TestCase):
    def test_structure_and_references(self):
        s = SOURCE.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        self.assertEqual(len(labels), len(set(labels)))
        stack = []
        for op, env in re.findall(r"\\(begin|end)\{([^}]+)\}", s):
            if op == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        context = "\n".join(p.read_text(encoding="utf-8") for p in DIR.glob("*.tex")
                            if p.name[:2].isdigit() and int(p.name[:2]) <= 25)
        for a,b in re.findall(r"\\ref\{([^}]+)\}|\\hyperref\[([^\]]+)\]", s):
            self.assertIn(r"\label{" + (a or b) + "}", context)

    def test_FA25_embeddings_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"K_j\subseteq\operatorname{int}K_{j+1}",
            r"\bigcup_jK_j=\Omega",
            r"\ref{prop:D-independence18}",
            r"p_{N,m}((1-\chi_R)f)",
            r"\frac{C_{\chi,m}}{1+R}p_{N+1,m}(f)",
            r"p_{0,0}(f_n)=p_{0,0}(\psi)>0",
            r"e^{-n^2}(1+n+A)^N",
            r"\ref{thm:D-sequences18}",
            r"\supp h_j\subseteq\Omega\setminus K_j",
            r"L\subseteq\operatorname{int}K_J",
            r"\ref{thm:D-nonmetric18}",
            r"\ref{thm:nuclear-D23}",
        ):
            self.assertIn(fragment,s)

    def test_FA25_cutoff_weight_and_support_01(self):
        # Model radial weights on rational radii; no smoothness assumption.
        for R,k,N in product(range(1,13),range(25),range(7)):
            x=F(R)+F(k,4)
            self.assertLessEqual((1+x)**N, (1+x)**(N+1)/(1+R))
        # Exhaustion of (0,1): K_j=[1/(j+2),1-1/(j+2)].
        # Nonempty compact supports H_j lie below K_j.
        for j in range(1,41):
            a,b=F(1,4*(j+2)),F(1,2*(j+2))
            self.assertTrue(0<a<b<F(1,j+2))
            for i in range(1,j+1):
                self.assertLess(b,F(1,i+2))
        # Translated supports of radius A, weighted estimate.
        for n,A,k,N in product(range(1,11),range(1,5),range(-4,5),range(6)):
            x=F(n)+F(A*k,4)
            self.assertLessEqual((1+abs(x))**N,(1+n+A)**N)

if __name__ == "__main__":
    unittest.main()
