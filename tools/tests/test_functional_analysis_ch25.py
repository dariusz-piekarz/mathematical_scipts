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

    def test_FA25_dual_compact_extension_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"p\circ j",
            r"= \sup_{y\in j(B)}",
            r"(j\circ i)'=i'\circ j'",
            r"T=F|_{\mathcal D(\Omega)}",
            r"\ref{lem:distribution-local19}",
            r"L=\supp\chi",
            r"C_L 2^m p_{L,m}(\chi)p_{L,m}(f)",
            r"\sum_{\gamma\le\alpha}\binom{\alpha}{\gamma}=2^{|\alpha|}",
            r"(\chi_1-\chi_2)f",
            r"\ref{lem:compact-action21}",
        ):
            self.assertIn(fragment,s)
        from math import comb
        # Finite jets: Leibniz product and cutoffs equal to 1 near support.
        V=list(product(range(-1,2),repeat=4))
        for a,b in product(V,repeat=2):
            for m in range(4):
                val=sum(comb(m,k)*a[k]*b[m-k] for k in range(m+1))
                self.assertLessEqual(abs(val),2**m*max(map(abs,a))*max(map(abs,b)))
            chi=(1,0,0,0)
            self.assertEqual(tuple(sum(comb(m,k)*chi[k]*a[m-k]
                                       for k in range(m+1)) for m in range(4)),a)
        # Transposition of composition with rectangular matrices.
        def mm(A,B):
            return tuple(tuple(sum(a*b for a,b in zip(row,col))
                               for col in zip(*B)) for row in A)
        J=((1,2),(-1,0),(0,3))
        I=((1,0,1),(0,1,-1))
        for t in product(range(-2,3),repeat=3):
            self.assertEqual(mm((t,),mm(J,I)),mm(mm((t,),J),I))

    def test_FA25_tempered_extension_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\widetilde T\in\mathcal S'",
            r"\ref{thm:tempered-estimate22}",
            r"\delta f/(2p_{j,j}(f))",
            r"C p_{N,m}(\varphi_j-\varphi_k)",
            r"\widetilde T(f)=\lim_jT(\varphi_j)",
            r"C p_{N,m}(\varphi_j-\psi_j)",
            r"|\widetilde T(f)|\le C p_{N,m}(f)",
            r"\widetilde T|_{\mathcal D}=T",
            r"\ref{prop:schwartz-embeddings22}",
            r"e^{-n/2}(n+2)^N p_{0,m}(\psi)",
            r"e^{n/2}\int_\R e^y\psi(y)",
            r"\ref{ex:non-tempered22}",
        ):
            self.assertIn(fragment,s)
        from math import factorial
        # Finite model of the Cauchy estimate for a dominated functional.
        # c_k=(-1)^k(1+k)^N/2^(k+1), weighted dual sum <= 1.
        for N,r,s,a,b in product(range(5),(F(1,2),F(-1,3),F(0)),
                                 (F(1,4),F(-2,3)),range(-2,3),range(-2,3)):
            f=[a*r**k+b*s**k for k in range(12)]
            c=[F((-1)**k*(1+k)**N,2**(k+1)) for k in range(12)]
            for n in range(1,12):
                for m in (n+1,12):
                    v=sum(c[k]*f[k] for k in range(n,m))
                    p=max((1+k)**N*abs(f[k]) for k in range(n,m))
                    self.assertLessEqual(abs(v),p)
                    self.assertLessEqual(abs(v),p*sum(F(1,2**(k+1)) for k in range(n,m)))
        # Exact rational upper-bound certificate for (n+2)^N exp(-n/2).
        for N,n in product(range(9),range(1,61)):
            term=F(n,2)**(N+1)/factorial(N+1)
            lower=sum(F(n,2)**k/factorial(k) for k in range(N+2))
            self.assertTrue(lower>=term>0)
            self.assertLessEqual(F((n+2)**N,1)/term,
                                 F(3**N*2**(N+1)*factorial(N+1),n))

if __name__ == "__main__":
    unittest.main()
