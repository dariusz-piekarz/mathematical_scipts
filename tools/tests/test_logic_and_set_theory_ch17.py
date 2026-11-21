"""Chapter 17 audit regressions: finite falsification checks, not general proofs."""
from itertools import product
from pathlib import Path
from math import isqrt, factorial, prod
import re
import unittest

CHAPTER=(Path(__file__).resolve().parents[2]
 / 'chapters/pl/logic_and_set_theory/17-arytmetyka-formalna-i-kodowanie-skladni.tex')
if not CHAPTER.exists():
    CHAPTER=Path('/mnt/data/logika_rozdzial_17_audyt_III.tex')


def first_primes(n):
    result=[]; p=2
    while len(result)<n:
        if all(p%d for d in range(2,isqrt(p)+1)):
            result.append(p)
        p+=1
    return result


def encode(a):
    return prod(p**(x+1) for p,x in zip(first_primes(len(a)),a))


def decode(n):
    if n<=0: return None
    if n==1: return []
    res=[]
    q=n
    for p in first_primes(n.bit_length()+1):
        if q%p:
            return res if q==1 else None
        k=0
        while q%p==0: q//=p; k+=1
        res.append(k-1)
    return None


def S(x): return x+1 if isinstance(x,int) else x

def plus(x,y):
    if isinstance(y,str):return y
    return x if isinstance(x,str) else x+y

def times(x,y):
    if isinstance(y,str):return x if isinstance(x,str) else y
    if isinstance(x,str):return 0 if y==0 else x
    return x*y


class TestChapter17(unittest.TestCase):
    def test_source_inventory_and_new_zero_arity_definition(self):
        s=CHAPTER.read_text(encoding='utf8')
        self.assertIn(r'$\N^0$ jest zbiorem jednoelementowym',s)
        self.assertIn(r'dla wszystkich arności $k\ge0$',s)
        self.assertIn(r'$\operatorname{pd}(0)=Z^0=0$',s)
        self.assertIn(r'$\operatorname{pd}(S(y))=P_1^2(y,\operatorname{pd}(y))=y$',s)
        self.assertNotIn('wszystkich dodatnich arności',s)
        self.assertEqual(s.count(r'\begin{lemat}'),5)
        self.assertEqual(s.count(r'\begin{proof}'),5)
        self.assertEqual(s.count(r'\begin{definicja}'),10)
        labels=re.findall(r'\\label\{([^}]+)\}',s)
        self.assertEqual(len(labels),34)
        self.assertEqual(len(labels),len(set(labels)))
        stack=[]
        for mode,env in re.findall(r'\\(begin|end)\{([^{}]+)\}',s):
            if mode=='begin':stack.append(env)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)

    def test_induction_scheme_parameters(self):
        s=CHAPTER.read_text(encoding='utf8')
        self.assertIn(r'\forall\vec y\,\Bigl[\bigl(\varphi(0,\vec y)\land\forall x\,(\varphi(x,\vec y)\to\varphi(S(x),\vec y))\bigr)\to\forall x\,\varphi(x,\vec y)\Bigr]',s)
        self.assertNotIn(r'\varphi(0,\overline y)',s)

    def test_concrete_countermodel_of_Q(self):
        els=list(range(32))+['a','b']
        for x in els:
            self.assertNotEqual(S(x),0)
            self.assertEqual(plus(x,0),x)
            self.assertEqual(times(x,0),0)
            self.assertTrue(x==0 or x in ('a','b') or S(x-1)==x)
            for y in els:
                self.assertEqual(S(x)==S(y),x==y)
                self.assertEqual(plus(x,S(y)),S(plus(x,y)))
                self.assertEqual(times(x,S(y)),plus(times(x,y),x))
        self.assertEqual(plus('a','b'),'b')
        self.assertEqual(plus('b','a'),'a')
        self.assertNotEqual(plus('a','b'),plus('b','a'))

    def test_Q_finite_initial_segments(self):
        for n in range(23):
            for x in range(32):
                self.assertEqual(any(z+x+1==n for z in range(50)),x<n)
                self.assertTrue(x<n or x==n or n<x)

    def test_zero_ary_recursion_predecessor(self):
        for n in range(150):
            y=0
            for i in range(n):y=i
            self.assertEqual(y,max(0,n-1))

    def test_primitive_recursive_bounded_minimization(self):
        for n in range(8):
            for bits in product((0,1),repeat=n+1):
                formula=sum(prod(1-bits[i] for i in range(j+1)) for j in range(n+1))
                expected=next((i for i,b in enumerate(bits) if b),n+1)
                self.assertEqual(formula,expected)

    def test_prime_code_roundtrips(self):
        total=0
        for length in range(5):
            for seq in product(range(4),repeat=length):
                self.assertEqual(decode(encode(seq)),list(seq))
                total+=1
        self.assertGreater(total,300)
        self.assertEqual(encode([1,2,1]),2700)
        self.assertEqual(decode(2700),[1,2,1])
        self.assertIsNone(decode(0))
        self.assertIsNone(decode(3**2))
        self.assertIsNone(decode(2**2*5**3))

    def test_primes_and_factorial_bounds(self):
        ps=first_primes(8)
        for a,b in zip(ps,ps[1:]):
            self.assertLess(a,b)
            self.assertLessEqual(b,factorial(a)+1)

    def test_unbounded_quantifier_certificates(self):
        s=CHAPTER.read_text(encoding='utf8')
        for term in ('rekurencyjnie przeliczalnym zbiorze aksjomatów','skończony ślad akceptacji',
                     'świadectwo pochodzenia z wyliczenia','Nie rozstrzygamy, czy program kiedyś się zatrzyma',
                     'nie korzystamy z Lematu~\\ref{res:6:5} jako przesłanki'):
            self.assertIn(term,s)

    def test_forward_refs_explicit(self):
        s=CHAPTER.read_text(encoding='utf8')
        refs=set(re.findall(r'\\(?:ref|eqref|autoref)\{([^{}]+)\}',s))
        labs=set(re.findall(r'\\label\{([^{}]+)\}',s))
        self.assertEqual(refs-labs,{
            'ch:computability-intro','def:syntax-term','def:syntax-formula',
            'res:7:6','res:7:7'})

if __name__=='__main__':unittest.main()