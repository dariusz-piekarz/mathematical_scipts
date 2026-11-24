import re
import unittest
from fractions import Fraction as F
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/functional_analysis"
SOURCE = next(DIR.glob("26-*.tex"))


class Chapter26(unittest.TestCase):
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
                            if p.name[:2].isdigit() and int(p.name[:2]) <= 26)
        for a, b in re.findall(r"\\ref\{([^}]+)\}|\\hyperref\[([^\]]+)\]", s):
            self.assertIn(r"\label{" + (a or b) + "}", context)

    def test_FA26_canonical_goldstine_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"|f(x)|\le\|f\|\|x\|",
            r"\ref{cor:norming}",
            r"|(J_Xx)(f)|=|f(x)|",
            r"J_X(B_X)\subseteq B_{X''}",
            r"\Phi\in B_{X''}\setminus\overline{J_X(B_X)}^{\,w^\ast}",
            r"|f_j(x)-\Phi(f_j)|<\eta",
            r"\ref{cor:point-closed-convex}",
            r"\ref{lem:realification}",
            r"\sup_{x\in B_X}\operatorname{Re}f(x)=\|f\|",
            r"\operatorname{Re}\Phi(f)\le|\Phi(f)|",
            r"\ref{cor:weak-convex-closure}",
            r"J_X(B_X)=B_{X''}",
            r"J_X(\|\Phi\|x)=\Phi",
            r"|f(x)|\le\|G\|\|x\|",
            r"\ref{thm:point-closed-subspace}",
        ):
            self.assertIn(fragment, s)

    def test_FA26_complex_norming_model_01(self):
        # Exact finite-dimensional models on C^3 with the l1 norm.
        # Complex numbers are pairs of rationals, avoiding floating point.
        def mul(z, w):
            a, b = z
            c, d = w
            return (a*c-b*d, a*d+b*c)

        def pairing(a, x):
            terms = [mul(z, w) for z, w in zip(a, x)]
            return tuple(sum(t[k] for t in terms) for k in range(2))

        coeffs = [((0, 0), 0), ((1, 0), 1), ((0, -2), 2),
                  ((3, 4), 5), ((-4, 3), 5)]
        for entries in product(coeffs, repeat=3):
            a = [z for z, m in entries]
            M = max(m for z, m in entries)
            j = next(i for i, (z, m) in enumerate(entries) if m == M)
            x = [(F(0), F(0)) for _ in range(3)]
            if M:
                x[j] = (F(a[j][0], M), F(-a[j][1], M))
            self.assertEqual(pairing(a, x), (M, 0))
            # Check the dual-norm bound on independent l1-unit vectors.
            for i, (u, v) in product(range(3), ((1, 0), (0, 1),
                                                (F(3, 5), F(-4, 5)))):
                y = [(F(0), F(0)) for _ in range(3)]
                y[i] = (u, v)
                re, im = pairing(a, y)
                self.assertLessEqual(re*re+im*im, M*M)
        # Reconstruction of the complex-linear functional from its
        # real part L: f(z)=L(z)-i L(iz).
        for a, z in product(product(((-1, 0), (0, 1), (1, -1)), repeat=3),
                            product(((-1, 0), (0, 1), (1, -1)), repeat=3)):
            iz = [(-v, u) for u, v in z]
            self.assertEqual(pairing(a, z),
                             (pairing(a, z)[0], -pairing(a, iz)[0]))


    def test_FA26_eberlein_smulian_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"F=\{0\}",
            r"\|\Theta-\Psi_j\|\|f_{\Psi_j}\|",
            r"F=\{f_{\Psi_1},\ldots,f_{\Psi_r}\}",
            r"\|y\|-2\|y-y_j\|>\|y\|/3",
            r"0\le d(u,v)-d_N(u,v)\le2^{-N}",
            r"\ref{cor:uniform-boundedness}",
            r"n>|f(x)|+1",
            r"|f(x_n)-\Phi(f)|<1/n",
            r"\|G-\Psi\|<\eta",
            r"\|\Psi\|\le3\|\Psi-G\|<3\eta",
            r"C=\overline{J_X(A)}^{\,w^\ast}",
            r"J_X(\overline A^{\,w})=C",
        ):
            self.assertIn(fragment, s)
        # Exact finite models of the metric and finite norming cover.
        V = list(product((-1, 0, 1), repeat=2))

        def term(u, v, j):
            return F(1, 2**j)*min(1, abs(u[j-1]-v[j-1]))

        def metric(u, v):
            return sum(term(u, v, j) for j in (1, 2))

        for u, v, w in product(V, repeat=3):
            self.assertLessEqual(metric(u, w), metric(u, v)+metric(v, w))
        for u, v in product(V, repeat=2):
            self.assertEqual(metric(u, v)==0, u==v)
            for N in range(3):
                tail = metric(u, v)-sum(term(u, v, j) for j in range(1, N+1))
                self.assertTrue(0 <= tail <= F(1, 2**N))

        S = [(F(a, 16), F(b, 16)) for a, b in
             product(range(-16, 17), repeat=2) if max(abs(a), abs(b))==16]
        for p, q in product(S, repeat=2):
            d = max(abs(a-b) for a, b in zip(p, q))
            if d >= F(1, 4):
                continue
            j = next(i for i in range(2) if abs(p[i])==1)
            self.assertTrue(abs(q[j]) >= abs(p[j])-d > F(1, 2))

    def test_FA26_schur_blocks_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"|x(j)|\le\|x\|_1",
            r"m_0=n_0=0",
            r"n_k>n_{k-1}",
            r"m_k>m_{k-1}",
            r"\sum_{j\notin I_k}|y_k(j)|<\varepsilon/4",
            r"m_k\ge k",
            r"a_jy_k(j)=|y_k(j)|",
            r"\sum_j|a_jx(j)|\le\|x\|_1",
            r"f(y_k)\to0",
            r"\ref{thm:schur-l1-26}",
            r"\ref{thm:orth-decomposition13}",
            r"\sum_{n\ge1}|\langle e_n,x\rangle|^2\le\|x\|^2",
            r"\ref{thm:riesz-hilbert13}",
        ):
            self.assertIn(fragment, s)
        # Three disjoint singleton blocks, with small leakage.
        # A single complex-linear functional must work for all rows.
        phases = [(F(1), F(0)), (F(0), F(1)),
                  (F(-1), F(0)), (F(3, 5), F(4, 5))]
        for core in product(phases, repeat=3):
            a = [(u, -v) for u, v in core]
            for scale in (F(0), F(1, 32), F(1, 16)):
                for k in range(3):
                    y = [core[j] if j == k else
                         (scale*core[j][0], -scale*core[j][1])
                         for j in range(3)]
                    norm = 1+2*scale
                    re = sum(u*p-v*q for (u,v),(p,q) in zip(a,y))
                    im = sum(u*q+v*p for (u,v),(p,q) in zip(a,y))
                    self.assertGreaterEqual(re, 1-2*scale)
                    self.assertGreater(re, F(1, 2))
                    self.assertLessEqual(re*re+im*im, norm*norm)
        # Bessel inequality for a rational orthonormal basis of R^3.
        E = [(F(3,5),F(4,5),F(0)), (F(-4,5),F(3,5),F(0)),
             (F(0),F(0),F(1))]
        for x in product(range(-2,3),repeat=3):
            coeff = [sum(a*b for a,b in zip(e,x)) for e in E]
            norm2 = sum(a*a for a in x)
            for n in range(1,4):
                self.assertLessEqual(sum(c*c for c in coeff[:n]), norm2)
            self.assertEqual(sum(c*c for c in coeff), norm2)

    def test_FA26_uniform_convexity_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\delta_X(\varepsilon)",
            r"\ref{prop:parallelogram13}",
            r"\|(x+y)/2\|^2=1-\|x-y\|^2/4",
            r"\delta_H(\varepsilon)=1-\sqrt{1-\varepsilon^2/4}>0",
            r"\Phi/\|\Phi\|",
            r"\operatorname{Re}\Phi(f)>1-\delta/2",
            r"|f(x_\alpha)-\Phi(f)|<\delta/2",
            r"1-\delta<\|x_\alpha\|\le1",
            r"\|u_\alpha-u_\beta\|<\varepsilon/2",
            r"\|x_\alpha-x_\beta\|<\varepsilon/2+2\delta<\varepsilon",
            r"\|x_\alpha-x_{\alpha_n}\|<2^{-n}",
            r"\Phi=J_Xx",
            r"f(u_n)=f(x_n)/\|x_n\|",
            r"\liminf_k\|(u_{n_k}+u)/2\|",
            r"\|x_n-x\|\le\|x_n\|\|u_n-u\|",
        ):
            self.assertIn(fragment, s)
        # Rational unit circle models; squared norms avoid roundoff.
        def sq(v):
            return sum(x*x for x in v)
        def add(u, v):
            return tuple(a+b for a,b in zip(u,v))
        def sub(u, v):
            return tuple(a-b for a,b in zip(u,v))
        def scale(t, u):
            return tuple(t*a for a in u)
        V = [((1-t*t)/(1+t*t), 2*t/(1+t*t))
             for t in (F(k,8) for k in range(-16,17))]
        V.append((F(-1), F(0)))
        for u,v in product(V, repeat=2):
            self.assertEqual(sq(scale(F(1,2),add(u,v))), 1-sq(sub(u,v))/4)
        for u in V:
            x,y = u,(u[0],-u[1])
            self.assertTrue(sq(x)==sq(y)==1 and sq(sub(x,y))==4*u[1]**2
                            and sq(scale(F(1,2),add(x,y)))==u[0]**2)
        for eps in (F(1,2),F(1),F(3,2),F(2)):
            delta = eps*eps/64
            rs = (1,1-delta/2,1-delta/4)
            for u,v,r,s in product(V,V,rs,rs):
                x,y = scale(r,u),scale(s,v)
                if x[0]<=1-delta or y[0]<=1-delta:
                    continue
                self.assertLess(sq(sub(u,v)),(eps/2)**2)
                self.assertLess(sq(sub(x,y)),eps**2)

    def test_FA26_weak_sphere_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\ref{thm:sfera-slaba}",
            r"\overline{S_X}^{\,w}\subseteq B_X",
            r"v\in\bigcap_{j=1}^m\ker f_j",
            r"\|x+tv\|\ge t\|v\|-\|x\|",
            r"x+t_0v\in U\cap S_X",
            r"względną słabą zwartość",
            r"A=(0,1)\subseteq\R",
            r"\Phi=J_Xy",
            r"A=\overline A^{\,w}",
            r"\|e_n-e_m\|^2=2",
            r"\|(u+v)/2\|_\infty=1",
        ):
            self.assertIn(fragment, s)
        # Exact finite-dimensional slice model: two independent
        # linear constraints on the real l-infinity unit cube.
        V = list(product(range(-1,2), repeat=3))
        X = list(product((F(-1,2),F(0),F(1,2)), repeat=3))
        def dot(a,b):
            return sum(x*y for x,y in zip(a,b))
        def norm(x):
            return max(map(abs,x))
        for f,g in product(V,repeat=2):
            v = (f[1]*g[2]-f[2]*g[1], f[2]*g[0]-f[0]*g[2],
                 f[0]*g[1]-f[1]*g[0])
            if not any(v):
                continue
            self.assertTrue(dot(f,v)==dot(g,v)==0)
            for x in X:
                t = min((F(1 if a>0 else -1)-b)/a
                        for a,b in zip(v,x) if a)
                y = tuple(b+t*a for a,b in zip(v,x))
                self.assertTrue(t>0 and norm(y)==1)
                self.assertTrue(dot(f,y)==dot(f,x) and dot(g,y)==dot(g,x))

if __name__ == "__main__":
    unittest.main()
