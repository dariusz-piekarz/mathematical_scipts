import re
import unittest
from pathlib import Path
from fractions import Fraction as F
from itertools import product

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/functional_analysis"
SOURCE = next(DIR.glob("24-*.tex"))

class Chapter24(unittest.TestCase):
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
                            if p.name[:2].isdigit() and int(p.name[:2]) <= 24)
        for a,b in re.findall(r"\\ref\{([^}]+)\}|\\hyperref\[([^\]]+)\]", s):
            self.assertIn(r"\label{" + (a or b) + "}", context)

    def test_FA24_algebraic_and_projective_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"V/N",
            r"iloraz jest zerowy",
            r"e_i'\otimes I_{F_0}",
            r"P\otimes Q",
            r"\sum_i g_i(y)f_i=0",
            r"h(i,j)=\delta_{ij}",
            r"\pi_{p,q}(x\otimes y)=p(x)q(y)",
            r"p(x-x_0)q(y-y_0)",
            r"s(b(x,y))\le p(x)q(y)",
            r"s(\widetilde b(u))\le\pi_{p,q}(u)",
        ):
            self.assertIn(fragment,s)

    def test_FA24_injective_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\ell\in E',\ m\in F'",
            r"wartość sumy jest niezależna",
            r"\varepsilon_{p,q}\le\pi_{p,q}",
            r"\varepsilon_{p,q}(u)\ge|(\ell\otimes m)(u)|>0",
            r"\varepsilon_{X,Y}(u)\le",
            r"\|e_i'\|\varepsilon(u)",
            r"\varepsilon(u)\le\pi(u)\le\sum_{i=1}^n\|e_i\|\|y_i\|",
            r"\varepsilon(v_N)=1/N\to0",
            r"\pi(v_N)=1",
        ):
            self.assertIn(fragment,s)

    def test_FA24_finite_l1_models_01(self):
        # On l1^2 x l1^2, epsilon is the maximum over sign vectors.
        # Pi equals the entrywise l1 norm, as certified by a sign matrix.
        signs = list(product((-1,1),repeat=2))
        for a,b,c,d in product(range(-2,3),repeat=4):
            M=((a,b),(c,d))
            eps=max(abs(sum(u[i]*M[i][j]*v[j] for i in range(2) for j in range(2)))
                    for u,v in product(signs,repeat=2))
            pi=sum(abs(x) for row in M for x in row)
            S=tuple(tuple((x>0)-(x<0) for x in row) for row in M)
            self.assertEqual(sum(S[i][j]*M[i][j] for i in range(2) for j in range(2)),pi)
            self.assertLessEqual(eps,pi)
            self.assertGreaterEqual(eps,max(abs(x) for row in M for x in row))
        # Elementary tensors and coordinate projections.
        vectors=list(product(range(-2,3),repeat=2))
        for x,y in product(vectors,repeat=2):
            M=tuple(tuple(a*b for b in y) for a in x)
            eps=max(abs(sum(u[i]*M[i][j]*v[j] for i in range(2) for j in range(2)))
                    for u,v in product(signs,repeat=2))
            self.assertEqual(eps,sum(map(abs,x))*sum(map(abs,y)))
            for i in range(2):
                self.assertLessEqual(sum(map(abs,M[i])),eps)

    def test_FA24_seminorm_completion_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\pi_{p,q}(u)=\|u_{p,q}\|_\pi",
            r"\varepsilon_{p,q}(u)=\|u_{p,q}\|_\varepsilon",
            r"|\ell(v)|\le\pi_{p,q}(v)",
            r"x\in\ker p",
            r"\|x_n-x_m\|\,\|y_n\|",
            r"\bar b:E_p\times F_q",
            r"nie zakłada dziedziczności normy rzutowej",
            r"\pi_{p,r}(u)=\|u_{p,r}\|_\pi",
            r"C\varepsilon_{q,r}(u)",
            r"j_{q,P}=\sum_{\alpha\in J}",
            r"j_{q,p}=j_{P,p}j_{q,P}",
        ):
            self.assertIn(fragment,s)
        self.assertNotRegex(s,r"\\textup\{23\.\d+\}")
        # Noncoordinate quotient p(x)=|x0+x2|+|x1-x2|.
        # Both factors use this quotient. Kernel perturbations leave
        # the quotient tensor and its norm certificates unchanged.
        P=((1,0,1),(0,1,-1))
        k=(-1,1,1)
        def tr(A): return tuple(zip(*A))
        def mm(A,B):
            return tuple(tuple(sum(a*b for a,b in zip(row,col))
                               for col in zip(*B)) for row in A)
        def outer(x,y): return tuple(tuple(a*b for b in y) for a in x)
        def add(A,B): return tuple(tuple(a+b for a,b in zip(x,y)) for x,y in zip(A,B))
        vectors=list(product(range(-1,2),repeat=3))
        signs=list(product((-1,1),repeat=2))
        for x,y in product(vectors,repeat=2):
            U=outer(x,y)
            M=mm(mm(P,U),tr(P))
            V=add(add(U,outer(k,y)),outer(x,k))
            self.assertEqual(mm(mm(P,V),tr(P)),M)
            pi=sum(abs(a) for row in M for a in row)
            S=tuple(tuple((a>0)-(a<0) for a in row) for row in M)
            self.assertEqual(sum(a*b for row,srow in zip(M,S) for a,b in zip(row,srow)),pi)
            eps=max(abs(sum(u[i]*M[i][j]*v[j] for i in range(2) for j in range(2)))
                    for u,v in product(signs,repeat=2))
            self.assertLessEqual(eps,pi)
            self.assertEqual(eps,pi) # rank-one quotient tensor

    def test_FA24_functional_tensor_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\|Ju_N-Ju\|_{\ell^1(F)}\le\pi(u_N-u)",
            r"\pi_{p\circ A,q\circ B}(u)",
            r"w(i,j)\le(1+|i|)(1+|j|)",
            r"P_m(Ju)\le\pi_{p_m,p_m}(u)",
            r"M>2m+d_1+d_2",
            r"a^{[N]}\otimes b^{[N]}",
            r"R\widehat J=I",
            r"\operatorname{int}K_{n+1}\setminus K_{n-2}",
            r"\chi_i\in\mathcal D(V_i)",
            r"K\cap\supp\chi_i\ne\varnothing",
            r"L\cap\supp\psi_j\ne\varnothing",
            r"2a>r+d_1",
            r"2b>s+d_2",
            r"\widehat J_{\mathcal E}T_{ij}(\Phi)=\Phi_{ij}",
            r"T_{ij}(fg)=(\eta_i f)\otimes(\theta_j g)",
            r"T\widehat J_{\mathcal E}=I",
        ):
            self.assertIn(fragment,s)
        # Weighted coordinate models, exact integer arithmetic.
        for i,j,m in product(range(13),range(13),range(7)):
            self.assertLessEqual((1+i+j)**m,(1+i)**m*(1+j)**m)
            self.assertLessEqual((1+i)**m*(1+j)**m,(1+i+j)**(2*m))
        # Real trigonometric basis on a four-point periodic grid,
        # unnormalized; rational orthogonal coefficients.
        B=[(1,1,1,1),(1,0,-1,0),(0,1,0,-1),(1,-1,1,-1)]
        norms=[sum(t*t for t in b) for b in B]
        def coeff(x,k):
            return F(sum(a*b for a,b in zip(x,B[k])),norms[k])
        V=[(1,0,0,0),(0,1,0,0),(1,-2,3,-1),(0,0,1,2),(1,1,1,1)]
        for x,y in product(V,repeat=2):
            M=tuple(tuple(a*b for b in y) for a in x)
            C=tuple(tuple(F(sum(M[i][j]*B[k][i]*B[l][j]
                                for i,j in product(range(4),repeat=2)),
                            norms[k]*norms[l])
                          for l in range(4)) for k in range(4))
            for k,l in product(range(4),repeat=2):
                self.assertEqual(C[k][l],coeff(x,k)*coeff(y,l))
            for i,j in product(range(4),repeat=2):
                self.assertEqual(sum(C[k][l]*B[k][i]*B[l][j]
                                     for k,l in product(range(4),repeat=2)),M[i][j])

    def test_FA24_inductive_tensor_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"h(x\otimes\cdot)",
            r"h_s=s\circ\widetilde b",
            r"\widetilde b:E\otimes_i F\to G",
            r"2t_{ij}>r_{ij}+d_2",
            r"p_{M,m_{ij}+2t_{ij}}(\Phi)",
            r"\lambda(B(\Phi))=\langle K_\lambda,\Phi\rangle",
            r"B(f\otimes g)=b(f,g)",
            r"\ref{thm:D-complete18}",
            r"JB=I",
            r"BJ=I",
            r"\varepsilon=\pi\le i",
            r"f_N^{(m)}(0)=N^m",
            r"N^{m-r}\le C Q(g_m) C_{\chi,r}",
        ):
            self.assertIn(fragment,s)
        from math import comb
        # Derivatives at zero for cos(N*x-m*pi/2), via the
        # two-dimensional differentiation recurrence.
        for m,r,N in product(range(1,9),range(8),range(1,13)):
            if r>=m: continue
            a,b=[(1,0),(0,1),(-1,0),(0,-1)][m%4]
            for _ in range(m):
                a,b=N*b,-N*a
            self.assertEqual(a,N**m)
            # Leibniz upper bounds, using model bounds for cutoff jets.
            for k in range(r+1):
                bound=sum(comb(k,j)*(k-j+1)*N**j for j in range(k+1))
                self.assertLessEqual(bound,N**r*sum(comb(k,j)*(k-j+1) for j in range(k+1)))
        # Signed point-jet pairing, finite model.
        for f,g in product(product(range(-1,2),repeat=4),repeat=2):
            v=sum((-1)**(m+1)*f[m]*g[m] for m in range(4))
            w=sum(f[m]*g[m] if (m+1)%2==0 else -f[m]*g[m] for m in range(4))
            self.assertEqual(v,w)

    def test_FA24_kernel_correspondence_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"A:\mathcal D(\Omega)\to\mathcal D'(\Lambda)_\beta",
            r"\ref{thm:schwartz-kernel23}",
            r"\{g\}",
            r"izomorfizm algebraiczny",
            r"\ref{ex:diagonal-kernel23}",
            r"\supp\delta_\Delta=\Delta",
            r"p(f)\le\lambda_d(K)^{1/2}p_{K,0}(f)",
            r"|b(f,g)|\le p(f)p(g)",
            r"Osobliwość jądra nie oznacza braku łącznej",
        ):
            self.assertIn(fragment,s)
        # Polynomial models on [-1,1]; not compactly supported tests.
        V=list(product(range(-1,2),repeat=3))
        def moment(k): return F(0) if k%2 else F(2,k+1)
        def integ(a,b):
            return sum(x*y*moment(i+j) for i,x in enumerate(a) for j,y in enumerate(b))
        for a,b in product(V,repeat=2):
            c=[0]*5
            for i,j in product(range(3),repeat=2): c[i+j]+=a[i]*b[j]
            v=sum(t*moment(k) for k,t in enumerate(c))
            self.assertEqual(v,integ(a,b))
            self.assertLessEqual(v*v,integ(a,a)*integ(b,b))
        # Gaussian integer coordinate models of the complex bilinear
        # diagonal pairing. Values are exactly representable.
        W=[(1,0),(1j,0),(1+1j,2-1j),(0,1j),(-1,2j)]
        for a,b in product(W,repeat=2):
            v=sum(x*y for x,y in zip(a,b))
            self.assertEqual(v,sum(a[i]*b[j]*int(i==j) for i,j in product(range(2),repeat=2)))
            self.assertLessEqual(v.real**2+v.imag**2,
                sum(x.real**2+x.imag**2 for x in map(complex,a))*
                sum(x.real**2+x.imag**2 for x in map(complex,b)))
            self.assertEqual(sum((1j*x)*y for x,y in zip(a,b)),1j*v)
            self.assertEqual(sum(x*(1j*y) for x,y in zip(a,b)),1j*v)

if __name__ == "__main__":
    unittest.main()
