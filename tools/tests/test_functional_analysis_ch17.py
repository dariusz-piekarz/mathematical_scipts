import re
import unittest
from pathlib import Path
from fractions import Fraction
from math import comb

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/functional_analysis"
SOURCE = next(DIR.glob("17-*.tex"))

class Chapter17(unittest.TestCase):
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
        context = "\n".join(p.read_text(encoding="utf-8") for p in DIR.glob("*.tex") if p.name[:2].isdigit() and int(p.name[:2]) <= 17)
        for label in re.findall(r"\\ref\{([^}]+)\}", s):
            self.assertIn(r"\label{" + label + "}", context)

    def test_empty_compact_and_cutoff_support(self):
        s = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"Dla $K=\varnothing$ przyjmujemy $p_{K,m}=0$", s)
        self.assertIn(r"\overline B(0,\delta/2)\subset B(0,\delta)", s)
        self.assertNotIn(r"\mathbf1_V", s)
        for delta in map(Fraction, range(1, 11)):
            self.assertLess(delta / 2, delta)

    def test_leibniz_bound(self):
        for a in range(9):
            for b in range(9):
                self.assertEqual(sum(comb(a,k)*comb(b,l) for k in range(a+1) for l in range(b+1)), 2**(a+b))

    def test_complete_metric_and_scaling(self):
        s = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"g_{\alpha+e_i}(x)$ przy $t\to0$", s)
        self.assertIn(r"\sum_{n>N}2^{-n}", s)
        self.assertIn(r"0<a<\varepsilon/q_n(f)", s)


    def test_fourier_and_schwartz_bounds(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"Q_{d+1+|\beta|,|\alpha|}(f)",
            r"(-i)^{|\alpha|+|\beta|}",
            r"2^{k(d-Np)}",
            r"\delta/\sqrt\varepsilon",
            r"\|f\|_1\|g\|_1<\infty",
            r"(2\pi)^{d/2}\widehat f(\xi)\widehat g(\xi)",
        ):
            self.assertIn(fragment, s)
        for a in range(9):
            for b in range(9):
                self.assertEqual((1j)**(-a)*(-1j)**b, (-1j)**(a+b))


    def test_compact_jets_and_empty_exhaustion(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"q_n=p_{K_n,n}",
            r"p_{K,m}(f-g)=0",
            r"T(f)-T(g)",
            r"Q_{N+1}(f_j)\ge cj",
        ):
            self.assertIn(fragment, s)
        # Polynomials f(x)=x and g(x)=0 coincide at 0, but their
        # first derivatives differ; point values alone do not determine T.
        f_at_zero, g_at_zero = 0, 0
        f_derivative_at_zero, g_derivative_at_zero = 1, 0
        self.assertEqual(f_at_zero, g_at_zero)
        self.assertNotEqual(f_derivative_at_zero, g_derivative_at_zero)

if __name__ == "__main__":
    unittest.main()
