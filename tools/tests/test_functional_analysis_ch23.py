import re
import unittest
from pathlib import Path
from fractions import Fraction as F
from itertools import product

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/functional_analysis"
SOURCE = next(DIR.glob("23-*.tex"))

class Chapter23(unittest.TestCase):
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
                            if p.name[:2].isdigit() and int(p.name[:2]) <= 23)
        for a,b in re.findall(r"\\ref\{([^}]+)\}|\\hyperref\[([^\]]+)\]", s):
            self.assertIn(r"\label{" + (a or b) + "}", context)

    def test_FA23_montel_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\ref{lem:montel-schwartz22}",
            r"\ref{lem:exhaustion17}",
            r"|x-y|<\delta_j",
            r"M_{j+1,m+1}\sum_{i=1}^d|x_i-y_i|",
            r"\ref{thm:D-Montel18}",
            r"Funkcjonał Minkowskiego $p_U$",
            r"\{f:p_U(f)<1\}\subseteq U",
            r"\{u_n-u:n\ge1\}",
            r"\sup_{x\in B}|(u_n-u)(x)|\le2\varepsilon/3",
        ):
            self.assertIn(fragment,s)

    def test_FA23_nuclear_banach_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\sum_j\|\ell_j(x)y_j\|\le\|x\|\sum_j\|\ell_j\|\|y_j\|",
            r"\|T-T_N\|\le\sum_{j>N}\|\ell_j\|\|y_j\|",
            r"\|T-T_N\|<\varepsilon/2",
            r"\|T\|\le\|T\|_{\mathcal N}",
            r"\|BTA\|_{\mathcal N}\le\|B\|\|T\|_{\mathcal N}\|A\|",
            r"(\ell_j\circ A)(x)By_j",
            r"\|D-D_N\|=1/(N+1)",
            r"\sum_{n=1}^N|\ell_j(e_n)|^2\le\|\ell_j\|^2",
        ):
            self.assertIn(fragment,s)
        # Exact finite diagonal truncation models (not a proof of compactness).
        for N in range(1,33):
            for extra in range(1,9):
                tail = [F(1,n) for n in range(N+1,N+extra+1)]
                self.assertEqual(max(tail),F(1,N+1))
                self.assertGreaterEqual(sum(tail),F(1,N+1))
        # Harmonic sum dyadic blocks have a uniform lower bound.
        for k in range(10):
            self.assertGreaterEqual(sum(F(1,n) for n in range(2**k+1,2**(k+1)+1)),F(1,2))

    def test_FA23_ideal_composition_01(self):
        # Exact finite rank-one composition models on Q^2:
        # (B(y ell)A) x == By (ell A)x.
        def mv(A,x):
            return tuple(sum(a*b for a,b in zip(row,x)) for row in A)
        matrices = [((1,0),(0,1)),((1,2),(-1,3)),((0,-2),(1,0))]
        vectors = [(1,0),(0,1),(2,-3)]
        for A,B,y,ell,x in product(matrices,matrices,vectors,vectors,vectors):
            T = tuple(tuple(v*c for c in ell) for v in y)
            lhs = mv(B,mv(T,mv(A,x)))
            eA = tuple(sum(ell[i]*A[i][j] for i in range(2)) for j in range(2))
            By = mv(B,y)
            rhs = tuple(v*sum(c*t for c,t in zip(eA,x)) for v in By)
            self.assertEqual(lhs,rhs)

    def test_FA23_nuclear_completions_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"j_{r,p}=j_{q,p}j_{r,q}",
            r"q=Cq_0",
            r"\ref{lem:nuclear-cofinal23}",
            r"c_{0,m}(I)",
            r"p_{m+1}(a)/(1+|\nu|)",
            r"\binom{r+d-1}{d-1}",
            r"k-m+d-1<-1",
            r"\frac{M_{k+1}}{1+R}",
            r"2M_{k+1}/(1+R)",
        ):
            self.assertIn(fragment,s)
        from math import comb
        # Count multiindices by total degree independently of binomial formula.
        counts = [1]+[0]*12
        for d in range(1,7):
            counts = [sum(counts[:r+1]) for r in range(13)]
            for r in range(13):
                self.assertEqual(counts[r],comb(r+d-1,d-1))
        for k,m,R,r in product(range(4),range(1,5),range(5),range(1,9)):
            if r>R:
                self.assertLessEqual(F(1,(1+r)**m),F(1,(1+R)**m))

    def test_FA23_nuclear_fourier_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"L=\supp\chi\Subset\Omega",
            r"(2R)^{-d}\lambda_d",
            r"(1+\pi^2|n|^2/R^2)^r c_n(f)",
            r"v_n=[\chi e_n]_{p_{K,m}}",
            r"2r>m+d",
            r"(2s+1)^d-(2s-1)^d",
            r"[f]_{p_{K,m}}=\sum_{n\in\mathbb Z^d}c_n(f)v_n",
            r"p_{K,m}\le p_{L,2r}",
            r"\operatorname{Re}c_n(f)\operatorname{Re}v_n",
        ):
            self.assertIn(fragment,s)
        # Fourier multipliers on finite trigonometric polynomial models.
        for n1,n2,r in product(range(-4,5),range(-4,5),range(5)):
            multiplier=1
            for _ in range(r):
                multiplier += (n1*n1+n2*n2)*multiplier
            self.assertEqual(multiplier,(1+n1*n1+n2*n2)**r)
        # Realification, exact small integer coefficients.
        for a,b,c,d in product(range(-2,3),repeat=4):
            self.assertEqual(((a+1j*b)*(c+1j*d)).real,a*c-b*d)

    def test_FA23_hilbert_factorization_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"h(x)^2=b(x,x)",
            r"\|J^*\|_{\mathrm{HS}}=\|J\|_{\mathrm{HS}}",
            r"h(x)\le Aq(x)",
            r"r=0",
            r"x\in\ker r",
            r"\Big\|\sum_j z_jVe_j\Big\|",
            r"VU([x]_r)=\sum_j a_j\ell_j([x]_q)y_j=[x]_h",
            r"\|VU\|_{\mathrm{HS}}^2\le\|V\|_{\mathrm{HS}}^2",
        ):
            self.assertIn(fragment,s)
        # Exact rational models with A=1, weights 9/25,16/25.
        vectors=[(1,0),(0,1),(F(1,2),F(-1,2))]
        for l1,l2,y1,y2,x,sign in product(vectors,vectors,vectors,vectors,
                                         [(1,0),(0,1),(2,-3)],[-1,1]):
            z1=sum(a*b for a,b in zip(l1,x))
            z2=sum(a*b for a,b in zip(l2,x))
            u=(F(3,5)*z1,F(4,5)*z2)
            v1=tuple(F(3,5)*a for a in y1)
            v2=tuple(sign*F(4,5)*a for a in y2)
            lhs=tuple(u[0]*a+u[1]*b for a,b in zip(v1,v2))
            rhs=tuple(F(9,25)*z1*a+sign*F(16,25)*z2*b
                      for a,b in zip(y1,y2))
            self.assertEqual(lhs,rhs)
            self.assertLessEqual(sum(v*v for v in lhs),sum(v*v for v in u))
            self.assertLessEqual(sum(v*v for v in v1+v2),1)

    def test_FA23_nuclear_permanence_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"P_{L^\perp}J|_{N^\perp}",
            r"p_F(x)\le p_E(x)",
            r"[x]_{t|_F}\mapsto[x]_t",
            r"\operatorname{dist}([x]_t,N_t)",
            r"\|P_{N_t^\perp}[x]_t\|",
            r"[\pi x]_{\bar t}\mapsto [x]_t+N_t",
            r"p_Q(\pi(x+m))=p_Q(\pi x)",
            r"\ker q=\bigoplus_n\ker q_n",
            r"z rzutem współrzędnym normy co najwyżej",
            r"\sum_{n\ge1}2^{-n}<\infty",
            r"K=\varnothing",
            r"\ref{thm:D-stage18}",
        ):
            self.assertIn(fragment,s)
        # Coordinate restrictions and compressions of finite matrices:
        # squared Hilbert-Schmidt norm cannot increase.
        matrices=[((1,2,3),(0,-1,4),(2,0,-2)),
                  ((0,0,0),(1,0,0),(0,0,2)),
                  ((1,0,0),(0,1,0),(0,0,1))]
        masks=range(8)
        for J,rows,cols in product(matrices,masks,masks):
            full=sum(v*v for row in J for v in row)
            compressed=sum(J[i][j]**2 for i in range(3) for j in range(3)
                           if rows&(1<<i) and cols&(1<<j))
            self.assertLessEqual(compressed,full)
        # Finite models of rescaling a nuclear representation.
        for n,cost in product(range(1,13),[F(0),F(1,3),F(2),F(7)]):
            c=1+2**n*cost
            self.assertLess(cost/c,F(1,2**n))

    def test_FA23_kernel_localization_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\chi_j\in\mathcal D(V_j)",
            r"\supp\chi_j\subset V_j",
            r"eliminuje inne kopie okresowe",
            r"(2R_j)^{d_2}",
            r"p_{K_i\times L_j^*,m+2t}(\Phi_{ij})",
            r"2t>r+d_2",
            r"\operatorname{Re}f_{ijn}\otimes\operatorname{Re}g_{jn}",
            r"f_{ijn}=(\eta_i f)c_{jn}(\theta_j g)",
            r"g_{jn}$ nie zależy od $\Phi$",
            r"p_{M,m_{ij}+2t_{ij}}(\Phi)",
            r"b(\eta_i f,\theta_j g)",
            r"p_{K_x\times K_y,q}(f\otimes g)",
            r"\ref{thm:D-bounded18}",
            r"\lambda_d(\operatorname{pr}_1 M)p_{M,0}(\Phi)",
        ):
            self.assertIn(fragment,s)
        # Finite rational model of localized bilinear pairing, with
        # partition weights summing to one on each coordinate.
        def pair(f,g,K):
            return sum(f[i]*K[i][j]*g[j] for i in range(2) for j in range(2))
        vectors=[(1,0),(0,1),(2,-3)]
        kernels=[((1,0),(0,1)),((1,2),(-1,3)),((0,-2),(1,0))]
        weights=[(F(0),F(1)),(F(1,3),F(2,3)),(F(1),F(0))]
        for f,g,K,w,z in product(vectors,vectors,kernels,weights,weights):
            fx=[tuple(f[i]*w[i] for i in range(2)),
                tuple(f[i]*(1-w[i]) for i in range(2))]
            gy=[tuple(g[j]*z[j] for j in range(2)),
                tuple(g[j]*(1-z[j]) for j in range(2))]
            self.assertEqual(sum(pair(u,v,K) for u in fx for v in gy),pair(f,g,K))

    def test_FA23_kernel_periodic_copy_01(self):
        # Piecewise polynomial surrogate, not a smooth test function:
        # localization must suppress all noncentral periodic copies.
        def bump(y):
            return (1-y*y)**2 if abs(y)<1 else F(0)
        def periodic(y,R):
            t=(y+R)%(2*R)-R
            return bump(t)
        def cutoff(y,R):
            if abs(y)<=1: return F(1)
            if abs(y)>=R: return F(0)
            return (R-abs(y))/(R-1)
        for R in [F(3,2),F(2),F(3)]:
            for j in range(-48,49):
                y=F(j,4)
                self.assertEqual(cutoff(y,R)*periodic(y,R),bump(y))
            self.assertGreater(periodic(2*R,R),0)
            self.assertEqual(cutoff(2*R,R),0)

    def test_FA23_hermite_basis_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"P_{n+1}=2xP_n-P_n'",
            r"2^n n!\sqrt\pi",
            r"|g(x)|e^{R|x|}",
            r"\ref{thm:fourier-auto-tempered22}",
            r"Przeliczalność rodziny $n$",
            r"P_n'=2nP_{n-1}",
            r"L=\sum_j a_j^*a_j+dI",
            r"(2(|\nu|+l+1))^{l/2}",
            r"2r\ge N+m+s",
            r"\ref{thm:plancherel22}",
            r"p_k(H(f))\le\|(1+L)^k f\|_2",
            r"p_{r+t}(c)^2",
            r"H(u)_\nu=c_\nu",
            r"Q_{N,m}(H^{-1}c)\le C p_{r+t}(c)",
            r"q=q'\circ H",
        ):
            self.assertIn(fragment,s)
        from math import factorial
        def trim(p):
            while len(p)>1 and p[-1]==0: p.pop()
            return p
        def add(p,q):
            return trim([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0)
                         for i in range(max(len(p),len(q)))])
        def scale(p,a): return trim([a*c for c in p])
        def X(p): return [0]+p
        def D(p): return [i*p[i] for i in range(1,len(p))] or [0]
        P=[[1]]
        for n in range(12):
            P.append(add(scale(X(P[-1]),2),scale(D(P[-1]),-1)))
        def moment(k):
            if k%2: return F(0)
            v=F(1)
            for j in range(1,k,2): v*=F(j,2)
            return v
        for n,m in product(range(13),repeat=2):
            integral=sum(a*b*moment(i+j) for i,a in enumerate(P[n])
                         for j,b in enumerate(P[m]))
            self.assertEqual(integral,2**n*factorial(n) if n==m else 0)
        for n in range(12):
            self.assertEqual(D(P[n]),scale(P[n-1],2*n) if n else [0])
            self.assertEqual(add(scale(X(P[n]),2),scale(D(P[n]),-1)),P[n+1])
            self.assertEqual(add(scale(D(D(P[n])),-1),
                                 add(scale(X(D(P[n])),2),P[n])),
                             scale(P[n],2*n+1))

if __name__ == "__main__":
    unittest.main()
