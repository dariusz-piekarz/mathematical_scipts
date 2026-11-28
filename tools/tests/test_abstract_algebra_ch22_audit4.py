"""AA-22 audyt IV: dodatkowa niezależna weryfikacja ciał skończonych i regresji.

Modele skończone nie zastępują ogólnych dowodów Artina i odpowiedniości.
"""
import itertools
import re
import unittest
from pathlib import Path

SOURCE=(Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/22-twierdzenie-artina-i-odpowiedniosc-galois.tex').read_text(encoding='utf8')

def add(a,b,p):
    return tuple((x+y)%p for x,y in zip(a,b))

def mul(a,b,p,f):
    n=len(f)-1
    t=[0]*(2*n-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):t[i+j]=(t[i+j]+x*y)%p
    for k in range(len(t)-1,n-1,-1):
        c=t[k]
        for j in range(n):t[k-n+j]=(t[k-n+j]-c*f[j])%p
    return tuple(t[:n])

def power(x,k,p,f):
    result=(1,)+(0,)*(len(f)-2)
    while k:
        if k%2:result=mul(result,x,p,f)
        x=mul(x,x,p,f)
        k//=2
    return result

def elements(p,n):
    return list(itertools.product(range(p),repeat=n))

class FiniteField27(unittest.TestCase):
    p=3;f=(1,2,0,1)  # x^3-x+1 over F3
    el=elements(3,3)
    def test_01_modulus_irreducible(self):
        self.assertTrue(all((x**3-x+1)%3!=0 for x in range(3)))
    def test_02_count(self):self.assertEqual(len(self.el),27)
    def test_03_fermat(self):
        self.assertTrue(all(power(x,27,self.p,self.f)==x for x in self.el))
    def test_04_frobenius_cube_identity(self):
        self.assertTrue(all(power(x,3**3,self.p,self.f)==x for x in self.el))
    def test_05_fixed_base(self):
        fixed=[x for x in self.el if power(x,3,self.p,self.f)==x]
        self.assertEqual(set(fixed),{(k,0,0) for k in range(3)})
    def test_06_orbits_under_frob(self):
        seen=set();sizes=[]
        for x in self.el:
            if x in seen:continue
            o={x,power(x,3,3,self.f),power(x,9,3,self.f)}
            self.assertEqual(len(o),1 if power(x,3,3,self.f)==x else 3)
            seen.update(o);sizes.append(len(o))
        self.assertEqual(sorted(sizes),[1]*3+[3]*8)
    def test_07_multiplicative_orders(self):
        unit=(1,0,0)
        orders=[]
        for x in self.el:
            if x==(0,0,0):continue
            z=unit
            for k in range(1,27):
                z=mul(z,x,3,self.f)
                if z==unit:orders.append(k);break
        self.assertEqual(max(orders),26)
        self.assertEqual(sum(o==26 for o in orders),12)
    def test_08_artin_fixed_degree(self):
        self.assertEqual(3,len([x for x in self.el if power(x,3,3,self.f)==x]))
        # The Frobenius has order three, which equals the extension degree.
        self.assertTrue(any(power(x,3,3,self.f)!=x for x in self.el))

class FiniteField8(unittest.TestCase):
    p=2;f=(1,1,0,1) # x^3+x+1
    el=elements(2,3)
    def test_09_modulus_irreducible(self):
        self.assertTrue(all((x**3+x+1)%2!=0 for x in range(2)))
    def test_10_frobenius_fixed(self):
        fixed={x for x in self.el if power(x,2,2,self.f)==x}
        self.assertEqual(fixed,{(0,0,0),(1,0,0)})
    def test_11_frobenius_order(self):
        self.assertTrue(all(power(x,8,2,self.f)==x for x in self.el))
        self.assertTrue(any(power(x,2,2,self.f)!=x for x in self.el))
        self.assertTrue(any(power(x,4,2,self.f)!=x for x in self.el))
    def test_12_multiplicative_cyclic(self):
        unit=(1,0,0);found=[]
        for x in self.el[1:]:
            if power(x,7,2,self.f)==unit and all(power(x,j,2,self.f)!=unit for j in range(1,7)):
                found.append(x)
        self.assertEqual(len(found),6)
    def test_13_frobenius_additive(self):
        for a in self.el:
            for b in self.el:
                self.assertEqual(power(add(a,b,2),2,2,self.f),add(power(a,2,2,self.f),power(b,2,2,self.f),2))

class SourceChecks(unittest.TestCase):
    def test_14_prior_corrections_present(self):
        self.assertIn(r'H_1,H_2\le\operatorname{Aut}(L)',SOURCE)
        self.assertIn(r'\alpha=(\omega\alpha)/\omega',SOURCE)
        self.assertIn('Niech $p$ będzie liczbą pierwszą',SOURCE)
        self.assertIn(r'\ref{aa:lem:extend-embedding-simple}',SOURCE)
    def test_15_finite_field_sentence_complete(self):
        self.assertIn('(przy czym $K$ utożsamiamy z pierwszym podciałem $L$).\nGrupa Galois rozszerzenia $L/K$',SOURCE)
    def test_16_source_proof_counts(self):
        self.assertEqual((SOURCE.count(r'\begin{proof}'),SOURCE.count(r'\end{proof}')),(5,5))
        self.assertEqual((SOURCE.count(r'\begin{przyklad}'),SOURCE.count(r'\end{przyklad}')),(4,4))
    def test_17_source_labels(self):
        labels=re.findall(r'\\label\{([^}]+)\}',SOURCE)
        self.assertEqual((len(labels),len(set(labels))),(12,12))
    def test_18_source_references(self):
        self.assertEqual(len(re.findall(r'\\(?:ref|eqref)\{[^}]+\}',SOURCE)),21)
    def test_19_assumptions_normal_and_galois(self):
        self.assertIn(r'$L/K$ będzie \emph{skończonym rozszerzeniem Galois}',SOURCE)
        self.assertIn(r'\sigma(E)=E',SOURCE)
    def test_20_consequential_terminology(self):
        self.assertNotRegex(SOURCE,r'(?i)\btensorowanie\b|\bsekwencyjn\w*\b|\bzwartościowanie\b')

if __name__=='__main__': unittest.main()
