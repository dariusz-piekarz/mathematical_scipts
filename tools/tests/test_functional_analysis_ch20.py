import re
import unittest
from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/functional_analysis"
SOURCE = next(DIR.glob("20-*.tex"))

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
        context = "\n".join(p.read_text(encoding="utf-8") for p in DIR.glob("*.tex") if p.name[:2].isdigit() and int(p.name[:2]) <= 20)
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

if __name__ == "__main__":
    unittest.main()
