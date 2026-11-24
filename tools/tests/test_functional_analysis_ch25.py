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

    def test_FA25_weak_strong_sequences_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"K=\overline B^{\,X}",
            r"K\subseteq\bigcup_{j=1}^k(x_j+U)",
            r"\le2\varepsilon/3<\varepsilon",
            r"\ref{cor:montel-dual-seq23}",
            r"\label{rem:sequence-net25}",
            r"T_{F,n}|_{\operatorname{lin}F}=0",
            r"\sup_{v\in B_0}|T_{F,n}(v)|\ge n",
            r"C_B=\sup_{\varphi\in B}p_{2,0}(\varphi)",
            r"r(x)^{-2k}P_k(x,r(x))",
            r"P_{k+1}=z^2\partial_x P_k+xz\partial_z P_k",
            r"-2kxP_k-\tfrac12 xzP_k",
            r"\ge e^{(n-1)/2}",
            r"a_j\in\Omega\setminus K_j",
            r"\langle\delta_{a_j},1\rangle=1",
        ):
            self.assertIn(fragment,s)
        from math import factorial
        # Compare the polynomial derivative recurrence against the
        # independent Taylor series of sqrt(1+(x+h)^2) and exp.
        def recurrence(P,k):
            Q={}
            def add(i,j,c): Q[i,j]=Q.get((i,j),F(0))+c
            for (i,j),c in P.items():
                if i: add(i-1,j+2,i*c)
                if j: add(i+1,j,j*c)
                add(i+1,j,-2*k*c)
                add(i+1,j+1,-c/2)
            return {ij:c for ij,c in Q.items() if c}
        K=10
        P=[{(0,0):F(1)}]
        for k in range(K): P.append(recurrence(P[-1],k))
        for t in [F(j,13) for j in range(-12,13)]:
            x=2*t/(1-t*t)
            r=(1+t*t)/(1-t*t)
            R=[r]
            for n in range(1,K+1):
                target=2*x if n==1 else F(1) if n==2 else F(0)
                R.append((target-sum(R[j]*R[n-j] for j in range(1,n)))/(2*r))
            E=[F(1)]
            for n in range(1,K+1):
                E.append(-sum(j*R[j]*E[n-j] for j in range(1,n+1))/(2*n))
            for k in range(K+1):
                actual=sum(c*x**i*r**j for (i,j),c in P[k].items())/r**(2*k)
                self.assertEqual(actual,factorial(k)*E[k])
        # Escaping points on the bounded open interval (0,1).
        for j,J in product(range(1,61),repeat=2):
            if j<J: continue
            a=F(1,2*(j+2)); lo=F(1,J+2); hi=1-lo
            self.assertTrue(0<a<lo<=hi<1)

    def test_FA25_natural_operators_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"p_{K,m}(\partial^\alpha f)\le p_{K,m+|\alpha|}(f)",
            r"p_{N,m}(\partial^\alpha f)\le p_{N,m+|\alpha|}(f)",
            r"p_{N,m}(af)\le 2^m A_m p_{N+M_m,m}(f)",
            r"P_B(A'T)=P_{A(B)}(T)",
            r"(-1)^{|\alpha|}\langle T,\partial^\alpha f\rangle",
            r"\langle aT,f\rangle=\langle T,af\rangle",
            r"aT_1=T_a",
            r"\ref{thm:fourier-auto-tempered22}",
            r"\partial_y^\beta A_T f(y)",
            r"p_{N,k}(A_Tf)\le C(1+R)^N p_{N,k+m}(f)",
            r"\langle T*S,f\rangle=\langle S,A_Tf\rangle",
        ):
            self.assertIn(fragment,s)
        # Exact translated polynomial jets for convolution with
        # a finite linear combination of point derivatives.
        from math import factorial
        def jet(c,x,k):
            return sum(a*F(factorial(j),factorial(j-k))*x**(j-k)
                       for j,a in enumerate(c) if j>=k)
        atoms=[(F(-1,2),0,F(2)),(F(1,3),1,F(-3,2)),(F(1),2,F(1,4))]
        for c,y,k in product(product(range(-1,2),repeat=4),
                             (F(-2),F(-1,3),F(0),F(3,2)),range(4)):
            # Expand the translated polynomial before differentiating.
            from math import comb
            q=[sum(w*(-1)**m*a*F(factorial(j),factorial(j-m))*
                   comb(j-m,l)*x**(j-m-l)
                   for x,m,w in atoms for j,a in enumerate(c) if j>=m+l)
               for l in range(4)]
            direct=sum(w*(-1)**m*jet(c,x+y,k+m) for x,m,w in atoms)
            self.assertEqual(jet(q,y,k),direct)
        for x,y,N in product((F(k,3) for k in range(-9,10)),
                             (F(k,4) for k in range(-12,13)),range(7)):
            self.assertLessEqual((1+abs(y))**N,
                                 (1+abs(x))**N*(1+abs(x+y))**N)

if __name__ == "__main__":
    unittest.main()
