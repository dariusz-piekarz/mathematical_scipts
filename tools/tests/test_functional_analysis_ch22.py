import re
import unittest
from pathlib import Path
from math import comb, factorial as _factorial
from fractions import Fraction as F
from itertools import product

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/functional_analysis"
SOURCE = next(DIR.glob("22-*.tex"))

class Chapter22(unittest.TestCase):
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
                            if p.name[:2].isdigit() and int(p.name[:2]) <= 22)
        for a,b in re.findall(r"\\ref\{([^}]+)\}|\\hyperref\[([^\]]+)\]", s):
            self.assertIn(r"\label{" + (a or b) + "}", context)

    def test_FA22_tempered_embeddings_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"(1+\max_{x\in K}|x|)^N p_m(\varphi)",
            r"T|_{\mathcal D}=T\circ j",
            r"2^{k(d+M-N)}",
            r"\mathrm d|\mu|(x)",
            r"Q_{N,m}(g-\chi(\cdot/R)g)",
            r"R^d\lambda_d(B(0,1))",
            r"P_B(T_f)\le C_d\|f\|_2",
            r"\overline f$ w $L^2$",
            r"P_B(T|_{\mathcal D})=P_{j(B)}(T)",
            r"\ref{lem:compact-action21}",
        ):
            self.assertIn(fragment, s)
        # Exact dyadic tail ratios for all integer exponent models.
        for d,M,extra in product(range(1,7),range(6),range(1,5)):
            N = d+M+extra
            ratio = F(2)**(d+M-N)
            self.assertTrue(0 < ratio < 1)
            self.assertEqual(sum(ratio**k for k in range(8)),
                             (1-ratio**8)/(1-ratio))

    def test_FA22_multiplier_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"M_m=\max_{|\gamma|\le m}M_\gamma",
            r"\binom\beta\gamma C_\gamma",
            r"Q_{N,m}(a\varphi)\le C_m Q_{N+M_m,m}(\varphi)",
            r"P_B(A^{\mathrm t}T)=P_{A(B)}(T)",
            r"A\varphi=(-1)^{|\alpha|}",
        ):
            self.assertIn(fragment,s)
        # Polynomial jets at a point: derivative of a product.
        def jet(p,k,x):
            return sum(v*comb(i,k)*x**(i-k) for i,v in enumerate(p) if i>=k)
        polys = [[1], [1,-2,3], [0,1,0,-3,1]]
        for a,b,x,k in product(polys,polys,[-2,0,3],range(7)):
            ab = [0]*(len(a)+len(b)-1)
            for i,u in enumerate(a):
                for j,v in enumerate(b):
                    ab[i+j] += u*v
            self.assertEqual(jet(ab,k,x),
                             sum(jet(a,j,x)*jet(b,k-j,x) for j in range(k+1)))

    def test_FA22_montel_and_topologies_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\|x-y\|_1\sup_{\psi\in B}Q_{0,m+1}(\psi)",
            r"Q_{N+1,m}(\varphi_{n_k})",
            r"w domknięciu $B$ wybieramy $f_n\in B$",
            r"\sup_n|\langle T_n-T,v\rangle|",
            r"e^{-n^2}(2+3n)^N Q_{0,m}(\psi)",
            r"\mathcal S/M",
            r"T(\psi_n)=1",
        ):
            self.assertIn(fragment,s)
        self.assertNotIn("równoodległościowość",s)
        self.assertNotIn("sekwencyjna",s)

    def test_FA22_fourier_plancherel_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"T\circ\mathcal F",
            r"\langle T,\mathcal F^{-1}\varphi\rangle",
            r"\mathcal F(-i\xi_j\varphi)",
            r"\mathcal F(-i\partial_{\xi_j}\varphi)",
            r"\mathcal F^4T=T",
            r"T_{e^{-ia\cdot\xi}}",
            r"T_{(i\xi)^\alpha}",
            r"\|f\|_1\|\varphi\|_1",
            r"\mathcal F(\overline{\widehat g})(x)",
            r"\|\widehat f_n-\widehat g_n\|_2",
            r"P_B(T_{f_n}-T_f)",
            r"\lim_nT_{\widehat f_n}=T_{\widehat f}",
        ):
            self.assertIn(fragment,s)
        # Polynomial times exp(-x^2/2): exact Gaussian-integer
        # coefficient arithmetic (small integers, exactly representable).
        def trim(p):
            while len(p)>1 and p[-1]==0:
                p.pop()
            return p
        def add(p,q):
            return trim([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0)
                         for i in range(max(len(p),len(q)))])
        def scale(p,c):
            return trim([c*v for v in p])
        def deriv(p):
            return trim(add([i*p[i] for i in range(1,len(p))] or [0],
                            scale([0]+p,-1)))
        basis=[[1]]
        for n in range(8):
            basis.append(scale(deriv(basis[-1]),1j))
        def fourier(p):
            out=[0]
            for n,c in enumerate(p):
                out=add(out,scale(basis[n],c))
            return out
        def moment2(k):
            # Integral x^k exp(-x^2) / sqrt(pi), scaled by 2^8.
            if k%2: return 0
            v=2**(8-k//2)
            for j in range(1,k,2): v*=j
            return v
        def inner(p,q):
            return sum(a*complex(b).conjugate()*moment2(i+j)
                       for i,a in enumerate(p) for j,b in enumerate(q))
        models=[[0]*n+[1] for n in range(7)]+[[1,2j,-3],[2-1j,0,1,0,-2j]]
        for p in models:
            fp=fourier(p)
            self.assertEqual(fourier(deriv(p)),scale([0]+fp,1j))
            self.assertEqual(fourier([0]+p),scale(deriv(fp),1j))
            self.assertEqual(fourier(fp),[(-1)**n*c for n,c in enumerate(p)])
            self.assertEqual(fourier(fourier(fourier(fp))),p)
        for p,q in product(models,repeat=2):
            self.assertEqual(inner(fourier(p),fourier(q)),inner(p,q))

    def test_FA22_schwartz_convolution_compact_fourier_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"Q_{N,m}(\rho(h-\cdot))\le(1+|h|)^N",
            r"|t|(2+|x|)^N Q_{N,m+2}(\rho)",
            r"C(1+|x|)^N Q_{N,m+|\alpha|}(\rho)",
            r"Q_{N,m}(G_x)\le",
            r"Q_{N,m}(G_x-G_{x'})",
            r"Q_{N,m}(I_{R''}-I_{R'})",
            r"\langle T_u,\psi\rangle=\langle T,\check\rho*\psi\rangle",
            r"\ref{thm:smoothing21}",
            r"\rho(z)(\mathcal F\psi)(y+z)",
            r"c_d\|\rho\|_1\|\psi\|_1",
            r"C,m,L$",
            r"\partial_x^\gamma((-ix)^\beta)",
            r"p_q(J_R-\chi\mathcal F\varphi)",
            r"\langle T,\chi\mathcal F\varphi\rangle",
            r"\mathcal FT=T_{F_T}",
        ):
            self.assertIn(fragment, s)
        # Gaussian smoothing of point jets: exp(-x^2/2) times
        # polynomial. Derivatives in the distribution variable
        # have the opposite sign to derivatives in x.
        def deriv(p):
            q = [0]*(len(p)+1)
            for i,c in enumerate(p):
                if i:
                    q[i-1] += i*c
                q[i+1] -= c
            while len(q)>1 and q[-1]==0:
                q.pop()
            return q
        def val(p,x):
            return sum(c*x**i for i,c in enumerate(p))
        polys = [[1]]
        for _ in range(8):
            polys.append(deriv(polys[-1]))
        for n,m,a,x in product(range(5),range(5),[-2,0,1],[-3,0,2]):
            ypoly=[1]
            for _ in range(n):
                ypoly=[-c for c in deriv(ypoly)]
            for _ in range(m):
                ypoly=deriv(ypoly)
            self.assertEqual(val(polys[n+m],x-a),(-1)**n*val(ypoly,x-a))
            # Independent Leibniz computation of the derivative
            # of the smoothing polynomial times the Gaussian.
            expected = sum(comb(m,k)*sum(c*comb(i,k) *
                           _factorial(k)*(x-a)**(i-k)
                           for i,c in enumerate(polys[n]) if i>=k)
                           *val(polys[m-k],x-a) for k in range(m+1))
            self.assertEqual(val(polys[n+m],x-a),expected)

        # Fourier of a shifted point derivative, after dividing by
        # the common normalization and phase: (i*xi)^n.
        # Differentiation in xi acts on both the monomial and phase.
        def phase_deriv(p,a):
            q=[-1j*a*c for c in p]
            for i in range(1,len(p)):
                q[i-1]+=i*p[i]
            return q
        for n,k,a,xi in product(range(5),range(5),[-2,0,3],[-3,1,2]):
            p=[0]*n+[1j**n]
            for _ in range(k):
                p=phase_deriv(p,a)
            expected=sum(comb(k,j)*1j**n*comb(n,j)*_factorial(j)
                         *xi**(n-j)*(-1j*a)**(k-j)
                         for j in range(min(k,n)+1))
            self.assertEqual(val(p,xi),expected)

if __name__ == "__main__":
    unittest.main()
