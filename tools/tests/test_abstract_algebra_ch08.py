"""AA-08 regression: structural controls and finite algebraic models."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import math
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
TEXT = (ROOT / "chapters/pl/abstract_algebra/08-grupy-abelowe-torsja-i-iloczyn-tensorowy.tex").read_text("utf8")

class Chapter08(unittest.TestCase):
    def test_structure_and_labels(self):
        labels = re.findall(r"\\label\{([^}]+)\}", TEXT)
        self.assertEqual((len(labels), len(set(labels))), (31, 31))
        self.assertEqual(TEXT.count(r"\begin{proof}"), 12)
        self.assertEqual(TEXT.count(r"\end{proof}"), 12)

    def test_internal_references(self):
        labels = set(re.findall(r"\\label\{([^}]+)\}", TEXT))
        refs = set(re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}", TEXT))
        self.assertTrue(refs <= labels, refs - labels)

    def test_universal_naturality(self):
        self.assertIn("Izomorfizm jest naturalny", TEXT)
        self.assertIn(r"\mathrm{id}_{C_m}\otimes f", TEXT)
        self.assertIn(r"\label{aa:tw:abelian-tensor-universal}", TEXT)

    def test_prufer_identification(self):
        self.assertIn(r"(\mathbb Q/\mathbb Z)[p^\infty]=C_{p^\infty}", TEXT)
        self.assertIn(r"C_{p^\infty}=\bigcup_{k\ge1}H_k", TEXT)
        self.assertIn(r"\label{aa:tw:torsion-primary}", TEXT)

    def check_crt(self, n):
        remaining=n; factors=[]
        for p in range(2, n+1):
            if remaining%p: continue
            q=1
            while remaining%p==0: q*=p; remaining//=p
            factors.append(q)
        self.assertEqual(math.prod(factors), n)
        es=[(n//q)*pow(n//q,-1,q)%n for q in factors]
        self.assertEqual(sum(es)%n, 1%n)
        for x in range(n):
            self.assertEqual(sum((e*x)%n for e in es)%n,x)

    def check_primary(self, p, exponents):
        mods=tuple(p**e for e in exponents)
        for k in range(1,5):
            actual=sum(all((p**k*a)%q==0 for a,q in zip(v,mods))
                       for v in product(*(range(q) for q in mods)))
            self.assertEqual(actual,p**sum(min(k,e) for e in exponents))

    def check_tensor(self, m):
        for n in range(1,22):
            g=math.gcd(m,n)
            for k in range(1,14):
                count=sum((m*a)%k==(n*a)%k==0 for a in range(k))
                hom=sum((g*a)%k==0 for a in range(k))
                self.assertEqual(count,hom)

    def check_prufer(self, p):
        for k in range(1,6):
            h={Fraction(a,p**k)%1 for a in range(p**k)}
            hnext={Fraction(a,p**(k+1))%1 for a in range(p**(k+1))}
            self.assertTrue(h<hnext)
            for n in range(1,12):
                s=0;u=n
                while u%p==0: s+=1;u//=p
                for a in range(min(p**k,30)):
                    z=(a*pow(u,-1,p**(k+s)))%(p**(k+s))
                    self.assertEqual((n*z)%(p**(k+s)),(a*p**s)%(p**(k+s)))

    def check_natural(self,m):
        for n,k in product(range(1,17), repeat=2):
            g=math.gcd(m,n);h=math.gcd(m,k)
            for t in range(k):
                if (n*t)%k: continue
                for a in range(n):
                    self.assertEqual((a%g)*t%h, (a*t)%h)

for n in (6,10,12,18,30,60,120,360):
    def run(self, n=n): self.check_crt(n)
    setattr(Chapter08, f"test_crt_{n:03d}", run)
for p,es in ((2,()),(2,(1,2)),(2,(2,3)),(2,(1,2,4)),
             (3,(1,)),(3,(1,2)),(3,(1,1,2)),(5,(1,2))):
    def run(self, p=p, es=es): self.check_primary(p,es)
    setattr(Chapter08, f"test_primary_{p}_{'_'.join(map(str,es)) or 'empty'}", run)
for m in (2,3,4,5,6,8,10,12):
    def run(self, m=m): self.check_tensor(m)
    setattr(Chapter08, f"test_cyclic_tensor_{m}", run)
for p in (2,3,5,7):
    def run(self, p=p): self.check_prufer(p)
    setattr(Chapter08, f"test_prufer_{p}", run)
for m in (2,3,4,6,8,12):
    def run(self, m=m): self.check_natural(m)
    setattr(Chapter08, f"test_naturality_{m}", run)

if __name__ == "__main__":
    unittest.main()
