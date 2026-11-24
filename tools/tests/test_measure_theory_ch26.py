"""Exact finite checks of the Hausdorff and Frostman constructions."""
from fractions import Fraction
from pathlib import Path
from itertools import product
import re
import unittest

SOURCE = Path(__file__).resolve().parents[2] / "chapters/pl/measure_theory/26-miara-hausdorffa-i-wymiar-hausdorffa.tex"

class TestHausdorffChapter26(unittest.TestCase):
    def test_fat_cantor(self):
        length = Fraction(1)
        for n in range(1,31):
            gap = Fraction(1,4**n)
            self.assertGreater(length,gap)
            length = (length-gap)/2
            self.assertEqual(length,Fraction(1,2**(n+1))*(1+Fraction(1,2**n)))
            self.assertEqual(2**n*length,(1+Fraction(1,2**n))/2)

    def test_tree_capacities(self):
        # dyadic intervals, s=1/2 model with rational capacity per level
        for mask in range(1,256):
            leaves = [Fraction(bool(mask & (1<<i)),4) for i in range(8)]
            levels = [leaves]
            for cap in (Fraction(1,2),Fraction(3,4),Fraction(1)):
                prev = levels[-1]
                levels.append([min(cap,prev[i]+prev[i+1]) for i in range(0,len(prev),2)])
            mass = levels[-1]
            for caps in reversed(levels[:-1]):
                nxt = []
                for i,m in enumerate(mass):
                    a = min(m,caps[2*i])
                    b = m-a
                    self.assertLessEqual(b,caps[2*i+1])
                    self.assertGreaterEqual(b,0)
                    nxt.extend([a,b])
                self.assertEqual(sum(nxt),sum(mass))
                mass = nxt
            self.assertGreater(sum(mass),0)

    def test_atomic_bound_requires_tail(self):
        # A fixed approximant with a positive atom cannot obey C*r^s for every r.
        for m,C in product((Fraction(1,8),Fraction(1,2),Fraction(1)),(1,2,4)):
            r = m/(2*C)
            self.assertGreater(m,C*r)

    def test_source(self):
        s=SOURCE.read_text(encoding="utf8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for token in (r"n\ge j(r)",r"miary $\mu_n$ są atomowe",r"\lambda_1(F)=1/2",
                      r"c_dd^{d/2}",r"s<t<a",r"\mu(\{x\})=0"):
            self.assertIn(token,s)
        stack=[]
        for m in re.finditer(r"\\(begin|end)\{([^}]+)\}",s):
            if m[1]=="begin":
                stack.append(m[2])
            else:
                self.assertEqual(stack.pop(),m[2])
        self.assertFalse(stack)

if __name__=="__main__":
    unittest.main()
