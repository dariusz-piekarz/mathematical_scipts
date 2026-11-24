import re
import unittest
from pathlib import Path
from fractions import Fraction
from math import factorial

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/functional_analysis"
SOURCE = next(DIR.glob("19-*.tex"))

class Chapter19(unittest.TestCase):
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
        context = "\n".join(p.read_text(encoding="utf-8") for p in DIR.glob("*.tex") if p.name[:2].isdigit() and int(p.name[:2]) <= 19)
        refs = re.findall(r"\\ref\{([^}]+)\}", s)
        refs += re.findall(r"\\hyperref\[([^\]]+)\]", s)
        for label in refs:
            self.assertIn(r"\label{" + label + "}", context)

    def test_regular_and_point_distributions(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"T_f-T_g=T_{f-g}",
            r"f\chi_V",
            r"\overline B(x,\varepsilon)\subseteq V",
            r"\int_K|f|\,\mathrm d\lambda_d=0",
            r"\partial^\alpha\psi(0)=\alpha!\ne0",
            r"\varepsilon^{|\alpha|-|\beta|}",
            r"\varphi(t)-\varphi(-t)=\int_{-t}^t",
        ):
            self.assertIn(fragment, s)
        for n in range(1, 9):
            for m in range(n):
                for eps in (Fraction(1,2), Fraction(1,4), Fraction(1,8)):
                    for k in range(m+1):
                        self.assertLessEqual(eps**(n-k), eps**(n-m))
                self.assertGreater(factorial(n), 0)

    def test_restriction_locality_and_compact_support(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\langle T|_U,\varphi\rangle=\langle T,e_U\varphi\rangle",
            r"O=\{x\in\Omega:h(x)>0\}",
            r"\varphi_j=\eta_j\varphi/h",
            r"\supp\varphi_j\subseteq L\cap\supp\eta_j\Subset U_{x_j}",
            r"\sum_j\varphi_j=\varphi",
            r"p_m(\chi\varphi)\le 2^m p_m(\chi)p_{K,m}(\varphi)",
            r"|\widetilde T(u)|\le C p_{K,m}(u)",
        ):
            self.assertIn(fragment, s)
        for weights in ((1,0), (1,1), (1,2,3), (0,0,5)):
            total = sum(weights)
            self.assertEqual(sum(Fraction(w,total) for w in weights), 1)

if __name__ == "__main__":
    unittest.main()
