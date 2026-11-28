import re
import unittest
from pathlib import Path
from fractions import Fraction

from distribution_migration_sources import source_for, reference_context

SOURCE = source_for(20)

def integral(poly, a, b):
    return sum(c * (Fraction(b)**(i+1) - Fraction(a)**(i+1)) / (i+1)
               for i, c in enumerate(poly))

def product(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] += a*b
    return r

def derivative(p):
    return [i*p[i] for i in range(1, len(p))] or [0]

class Chapter20(unittest.TestCase):
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
        context = reference_context(20)
        for label in re.findall(r"\\ref\{([^}]+)\}|\\hyperref\[([^\]]+)\]", s):
            self.assertIn(r"\label{" + (label[0] or label[1]) + "}", context)

    def test_FA20_derivative_and_restriction_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"D_\alpha(B)\subseteq tU",
            r"(-1)^{|\alpha|+|\beta|}",
            r"\partial^\alpha(e_U\varphi)=e_U(\partial^\alpha\varphi)",
            r"\langle T|_U,\partial^\alpha\varphi\rangle",
            r"Przedłużenie $F$ funkcji $\chi f$",
            r"\int_{\R^d}F\,\partial_j\Phi",
            r"\langle T_{\partial^\alpha f},\varphi\rangle",
            r"\ref{prop:regular-injective19}",
        ):
            self.assertIn(fragment, s)
        for a in range(12):
            for b in range(12):
                self.assertEqual((-1)**a * (-1)**b, (-1)**(a+b))

    def test_FA20_jump_sign_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"-f(a-\varepsilon)\varphi(a-\varepsilon)",
            r"f(a+\varepsilon)\varphi(a+\varepsilon)",
            r"2\varepsilon M p_1(\varphi)",
            r"(f(a+)-f(a-))\varphi(a)",
            r"\chi_{(-\infty,0)}",
            r"\chi_{(0,\infty)}",
            r"\langle\delta_0',\varphi\rangle=-1",
        ):
            self.assertIn(fragment, s)
        # Exact polynomial model on [-1,1]; vanishing endpoints suffice
        # for the finite-interval integration-by-parts identity.
        for phi in ([1,0,-1], [0,1,0,-1], [1,2,-1,-2]):
            for left,right in (([0],[1]), ([1,2],[2,-3]), ([3,-1,2],[-4,2,1])):
                lhs = -integral(product(left,derivative(phi)),-1,0) - integral(product(right,derivative(phi)),0,1)
                rhs = integral(product(derivative(left),phi),-1,0) + integral(product(derivative(right),phi),0,1) + (right[0]-left[0])*phi[0]
                self.assertEqual(lhs,rhs)


    def test_FA20_multivariate_leibniz_01(self):
        from itertools import product as cartesian_product
        from math import comb
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"gT=T\circ N_g",
            r"q_B(gT)=q_{N_g(B)}(T)",
            r"\binom\alpha{\nu-e_j}+\binom\alpha\nu=\binom\gamma\nu",
            r"\langle g(a)\delta_a'-g'(a)\delta_a,\varphi\rangle",
        ):
            self.assertIn(fragment, s)
        def multi_choose(a, b):
            if any(k < 0 or k > n for n,k in zip(a,b)):
                return 0
            from math import prod
            return prod(comb(n,k) for n,k in zip(a,b))
        for a in cartesian_product(range(4), repeat=3):
            for j in range(3):
                gamma = tuple(n + (i == j) for i,n in enumerate(a))
                for nu in cartesian_product(*(range(n+1) for n in gamma)):
                    prev = tuple(k - (i == j) for i,k in enumerate(nu))
                    self.assertEqual(multi_choose(a,prev)+multi_choose(a,nu),
                                     multi_choose(gamma,nu))

    def test_FA20_regularization_transpose_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\int_0^\infty\rho(t)\varphi(\varepsilon t)",
            r"q_B(T_{H\rho_\varepsilon}-c_\rho\delta_0)",
            r"otrzymujemy $c_\rho=0$",
            r"otrzymujemy $c_\rho=1$",
            r"D_\alpha N_{a_\alpha}",
            r"\langle T,P^{\mathrm t}\varphi\rangle",
            r"-a\varphi'+(b-a')\varphi",
            r"(c-\operatorname{div}b)\varphi",
        ):
            self.assertIn(fragment, s)
        # Exact finite-interval identity for a first-order operator
        # with variable coefficients and endpoint-vanishing test polynomials.
        for a in ([1],[0,1],[1,2,3]):
            for b in ([0],[2,-1]):
                for f in ([1],[1,2],[0,1,3]):
                    for phi in ([1,0,-1],[0,1,0,-1]):
                        lhs = integral(product(product(a,derivative(f)),phi),-1,1)
                        lhs += integral(product(product(b,f),phi),-1,1)
                        rhs = -integral(product(f,derivative(product(a,phi))),-1,1)
                        rhs += integral(product(product(b,f),phi),-1,1)
                        self.assertEqual(lhs,rhs)


    def test_FA20_primitive_and_gradient_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\supp\psi\subseteq[u,v]",
            r"\max\{1,\ell\}(1+\lambda_1(K)p_m(\eta))p_m(\varphi)",
            r"T=-S\circ R",
            r"R(\varphi')(x)=\int_{-\infty}^x",
            r"(e^AT)'=e^AT'+(e^A)'T",
            r"e^{-A}V+T_{ce^{-A}}",
            r"\partial_jT_Q=0",
            r"h_j=(\operatorname{Id}-P_j)\psi",
            r"\supp\theta_j\subseteq L_1\times\cdots\times L_d",
            r"\supp(T-T_c)=\varnothing",
            r"\langle S,\psi\rangle=\langle T,\eta\otimes\psi\rangle",
        ):
            self.assertIn(fragment, s)
        # Exact polynomial model of the zero-integral primitive on [-1,1].
        # eta=3/4(1-x^2) has integral one on this interval.
        eta = [Fraction(3,4),0,Fraction(-3,4)]
        self.assertEqual(integral(eta,-1,1),1)
        for phi in ([1,0,-1],[0,1,0,-1],[1,2,-1,-2]):
            mass = integral(phi,-1,1)
            h = [(phi[i] if i<len(phi) else 0) -
                 mass*(eta[i] if i<len(eta) else 0)
                 for i in range(max(len(phi),len(eta)))]
            self.assertEqual(integral(h,-1,1),0)
            primitive = [-integral(h,0,-1)] + [Fraction(c,i+1) for i,c in enumerate(h)]
            self.assertEqual(sum(c*(-1)**i for i,c in enumerate(primitive)),0)
            self.assertEqual(sum(primitive),0)
            self.assertEqual(derivative(primitive),h)


    def test_FA20_figure_and_product_domain_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"przyjmijmy $H(0)=0$",
            r"\draw[fill=blue!60!black,draw=blue!60!black,thick] (0,0) circle",
            r"\draw[fill=white,draw=blue!60!black,thick] (0,1.3) circle",
            r"h(t,y)=\varphi(t,y)-\eta(t)A\varphi(y)",
            r"\theta(t,y)=\int_{-\infty}^t h(s,y)",
            r"A(\eta\otimes\psi)=\psi",
            r"A(\partial_1\varphi)=0",
        ):
            self.assertIn(fragment, s)
        # Finite polynomial models of integration in the first coordinate.
        eta = [Fraction(3,4), 0, Fraction(-3,4)]
        for p in ([1,0,-1], [0,1,0,-1], [1,2,-1,-2]):
            self.assertEqual(integral(derivative(p),-1,1),0)
            for q in ([1], [2,-3,1]):
                mass = integral(p,-1,1)
                self.assertEqual([integral(eta,-1,1)*mass*c for c in q],
                                 [mass*c for c in q])

if __name__ == "__main__":
    unittest.main()
