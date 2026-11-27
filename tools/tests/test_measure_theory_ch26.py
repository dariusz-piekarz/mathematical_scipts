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
        # binary tree with illustrative rational capacities per level
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

    def test_normalized_frostman_approximants(self):
        # Finite models: separate convergence of positive total mass
        # and of probability measures before reconstructing the measure.
        for weights in product(range(4), repeat=4):
            mass = sum(weights)
            if not mass:
                continue
            prob = [Fraction(w, mass) for w in weights]
            self.assertEqual(sum(prob), 1)
            for mask in range(16):
                p = sum(prob[i] for i in range(4) if mask & (1 << i))
                raw = sum(weights[i] for i in range(4) if mask & (1 << i))
                self.assertEqual(mass*p, raw)
                for n in (1, 2, 8, 32):
                    bn = mass + Fraction(1, n)
                    self.assertLessEqual(abs(bn*p - raw), Fraction(1, n))

    def test_capacity_against_exhaustive_covers(self):
        # Binary depth-three tree with rational example costs (in quarters).
        # Independently enumerate all subfamilies of the 15 nodes.
        nodes = [(255,4)]
        for depth,cap in ((1,3),(2,2),(3,1)):
            width = 8//(2**depth)
            nodes.extend((((1<<width)-1) << (i*width),cap)
                         for i in range(2**depth))
        best = [100]*256
        for subset in range(1<<len(nodes)):
            covered = cost = 0
            for i,(bits,cap) in enumerate(nodes):
                if subset & (1<<i):
                    covered |= bits
                    cost += cap
            best[covered] = min(best[covered],cost)
        for mask in range(256):
            leaves = [(mask>>i)&1 for i in range(8)]
            for cap in (2,3,4):
                leaves = [min(cap,leaves[i]+leaves[i+1])
                          for i in range(0,len(leaves),2)]
            self.assertEqual(leaves[0],min(best[m] for m in range(256) if m&mask==mask))

    def test_cantor_cylinder_masses(self):
        for m in range(1,9):
            points = [sum(2*((word>>j)&1)*3**(m-1-j)
                          for j in range(m)) for word in range(2**m)]
            for n in range(m+1):
                for prefix in range(2**n):
                    start = sum(2*((prefix>>j)&1)*3**(m-1-j) for j in range(n))
                    end = start+3**(m-n)
                    count = sum(start<=x<=end for x in points)
                    self.assertEqual(Fraction(count,2**m),Fraction(1,2**n))

    def test_source(self):
        s=SOURCE.read_text(encoding="utf8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for token in (r"n\ge j(r)",r"miary $\mu_n$ są atomowe",r"\lambda_1(F)=1/2",
                      r"c_dd^{d/2}",r"s<t<a",r"\mu(\{x\})=0",r"\mu_n(Q)=m_n(Q)",r"cor:energy-dimension-26",r"\mu(I\cap C)=2^{-n}"):
            self.assertIn(token,s)
        stack=[]
        for m in re.finditer(r"\\(begin|end)\{([^}]+)\}",s):
            if m[1]=="begin":
                stack.append(m[2])
            else:
                self.assertEqual(stack.pop(),m[2])
        self.assertFalse(stack)
        known = set(labels)
        for path in SOURCE.parent.glob("[0-9][0-9]-*.tex"):
            known.update(re.findall(r"\\label\{([^}]+)\}", path.read_text(encoding="utf-8")))
        refs = set(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", s))
        self.assertFalse(refs - known, f"Missing references: {sorted(refs - known)}")
        self.assertNotIn(r"\atlasref{CAL-", s)
        self.assertIn(r"\ref{lem:compact-prob-22}", s)
        self.assertIn(r"\eta_n=\mu_n/b_n", s)


if __name__=="__main__":
    unittest.main()
