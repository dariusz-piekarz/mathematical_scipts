import re
import unittest
from pathlib import Path
from fractions import Fraction
from math import factorial

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/functional_analysis"
SOURCE = next(DIR.glob("18-*.tex"))

class Chapter18(unittest.TestCase):
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
        context = "\n".join(p.read_text(encoding="utf-8") for p in DIR.glob("*.tex") if p.name[:2].isdigit() and int(p.name[:2]) <= 18)
        for label in re.findall(r"\\ref\{([^}]+)\}", s):
            self.assertIn(r"\label{" + label + "}", context)

    def test_FA18_stage_and_universal_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"p_{L,m}\le p_m",
            r"p_m=p_{K,m}",
            r"q\circ T\in\mathcal P",
            r"\mathcal D_K\to\mathcal D_{K_n}",
            r"C_K=\varepsilon^{-1}",
        ):
            self.assertIn(fragment, s)

    def test_FA18_variable_order_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\varepsilon^{n-k}\psi^{(k)}",
            r"\varepsilon^{n-m}",
            r"K=[n-1/4,n+1/4]",
            r"\psi^{(n)}(0)=n!",
        ):
            self.assertIn(fragment, s)
        for n in range(1, 9):
            for m in range(n):
                for eps in (Fraction(1,2), Fraction(1,4), Fraction(1,8)):
                    for k in range(m+1):
                        self.assertLessEqual(eps**(n-k), eps**(n-m))
                    self.assertGreater(factorial(n), 0)
                self.assertLess(Fraction(1,8)**(n-m), Fraction(1,4)**(n-m))

if __name__ == "__main__":
    unittest.main()
