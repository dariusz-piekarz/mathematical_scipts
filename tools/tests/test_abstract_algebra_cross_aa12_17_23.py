"""AA-X20: Smith invariants and localization of integral trace pairings."""
from itertools import combinations, product
from math import gcd
from pathlib import Path
import re
import unittest

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

ROOT=Path(__file__).resolve().parents[2]
x=sp.Symbol("x")
CASES=(
 (x**2-5,((2,0),(0,10)),(2,10),20),
 (x**2-2,((2,0),(0,4)),(2,4),8),
 (x**3-2,((3,0,0),(0,0,6),(0,6,0)),(3,6,6),-108),
 (x**3-3*x+1,((3,0,6),(0,6,-3),(6,-3,18)),(3,3,9),81),
 (x**4-2,((4,0,0,0),(0,0,0,8),(0,0,8,0),(0,8,0,0)),(4,8,8,8),-2048),
)

def companion_multiplication(f):
    p=sp.Poly(f,x,domain=sp.QQ)
    n=p.degree()
    columns=[]
    for j in range(n):
        q=sp.Poly(x**(j+1),x,domain=sp.QQ).rem(p)
        columns.append(sp.Matrix([q.nth(i) for i in range(n)]))
    return sp.Matrix.hstack(*columns)

def gram(f):
    A=companion_multiplication(f)
    n=A.rows
    traces=[sp.trace(A**j) for j in range(2*n-1)]
    return sp.Matrix(n,n,lambda i,j:traces[i+j])

def minors_gcd(A,order):
    d=0
    for rows in combinations(range(A.rows),order):
        for cols in combinations(range(A.cols),order):
            d=gcd(d,abs(int(A.extract(rows,cols).det())))
    return d

def modular_rank(A,p):
    """Independent Gaussian elimination over F_p."""
    a=[[int(A[i,j])%p for j in range(A.cols)] for i in range(A.rows)]
    r=0
    for col in range(A.cols):
        pivot=next((i for i in range(r,A.rows) if a[i][col]),None)
        if pivot is None:
            continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][col],-1,p)
        a[r]=[(inv*v)%p for v in a[r]]
        for i in range(A.rows):
            if i!=r:
                factor=a[i][col]
                a[i]=[(a[i][j]-factor*a[r][j])%p for j in range(A.cols)]
        r+=1
        if r==A.rows:
            break
    return r

def primes(n):
    return set(sp.factorint(abs(int(n))).keys())

class TraceSmithLocalizationInterface(unittest.TestCase):
    def test_trace_gram_from_multiplication_matrices(self):
        for f,expected,invariant,disc in CASES:
            with self.subTest(f=str(f)):
                self.assertTrue(sp.Poly(f,x,domain=sp.QQ).is_irreducible)
                G=gram(f)
                self.assertEqual(G,sp.Matrix(expected))
                self.assertEqual(G.det(),disc)
                self.assertEqual(G.det(),sp.discriminant(f,x))
                self.assertTrue(all(v.q==1 for v in G))

    def test_smith_against_independent_minor_gcd(self):
        for f,entries,invariant,disc in CASES:
            with self.subTest(f=str(f)):
                G=sp.Matrix(entries)
                D=smith_normal_form(G,domain=sp.ZZ)
                self.assertEqual(tuple(abs(int(D[i,i])) for i in range(G.rows)),invariant)
                for k in range(1,G.rows+1):
                    self.assertEqual(minors_gcd(G,k),sp.prod(invariant[:k]))
                self.assertEqual(sp.prod(invariant),abs(disc))
                self.assertTrue(all(b%a==0 for a,b in zip(invariant,invariant[1:])))

    def test_reduction_rank_and_modular_cokernel(self):
        for f,entries,invariant,disc in CASES:
            G=sp.Matrix(entries)
            n=G.rows
            for p in (2,3,5,7,11):
                with self.subTest(f=str(f),p=p):
                    rank=modular_rank(G,p)
                    self.assertEqual(rank,sum(d%p!=0 for d in invariant))
                    self.assertEqual(rank==n,disc%p!=0)
                    self.assertEqual(p**(n-rank),sp.prod(p for d in invariant if d%p==0))
                    if n<=3 and p<=5:
                        kernel=sum(all(sum(int(G[i,j])*v[j] for j in range(n))%p==0
                                       for i in range(n))
                                   for v in product(range(p),repeat=n))
                        self.assertEqual(kernel,p**(n-rank))

    def test_localization_unit_condition_and_residual_primes(self):
        for f,entries,invariant,disc in CASES:
            bad=primes(disc)
            self.assertTrue(bad)
            for N in (1,2,3,5,6,10,15,30,210):
                with self.subTest(f=str(f),N=N):
                    inverted=primes(N)
                    self.assertEqual(bad<=inverted,
                                     all(primes(d)<=inverted for d in invariant))
                    for p in (2,3,5,7,11):
                        if N%p:
                            self.assertEqual(modular_rank(sp.Matrix(entries),p)==len(invariant),
                                             p not in bad)

    def test_nonmaximal_order_versus_integral_basis(self):
        G=gram(x**2-5)
        S=sp.Matrix([[1,sp.Rational(1,2)],[0,sp.Rational(1,2)]])
        H=S.T*G*S
        self.assertEqual(G,sp.diag(2,10))
        self.assertEqual(H,sp.Matrix([[2,1],[1,3]]))
        self.assertEqual((G.det(),H.det()),(20,5))
        self.assertEqual(int(abs(1/S.det())),2)
        D=smith_normal_form(H,domain=sp.ZZ)
        self.assertEqual(tuple(abs(int(D[i,i])) for i in range(2)),(1,5))
        self.assertEqual((modular_rank(G,2),modular_rank(H,2)),(0,2))
        self.assertEqual((modular_rank(G,5),modular_rank(H,5)),(1,1))
        # The first order's mod-2 degeneracy is not proof of ramification at 2.

    def test_source_labels_and_references(self):
        folder=ROOT/"chapters/pl/abstract_algebra"
        all_files=sorted(folder.glob("[0-9][0-9]-*.tex"))
        self.assertEqual(len(all_files),50)
        sources={p.name:p.read_text(encoding="utf-8") for p in all_files}
        labels=[m for src in sources.values()
                for m in re.findall(r"\\label\{([^{}]+)\}",src)]
        self.assertEqual(len(labels),len(set(labels)))
        focus=(
          "12-pierwiastniki-idealow-i-lokalizacja-pierscieni.tex",
          "17-moduly-nad-dziedzinami-idealow-glownych-i-postac-smitha.tex",
          "23-slad-norma-i-wyroznik.tex",
        )
        self.assertEqual(sum(len(re.findall(r"\\label\{",sources[p])) for p in focus),82)
        refs=[m for p in focus
              for m in re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^{}]+)\}",
                                  sources[p])]
        self.assertEqual(len(refs),34)
        self.assertFalse(set(refs)-set(labels),set(refs)-set(labels))
        for name in ("aa:def:localization","aa:tw:localization-universal",
                     "aa:tw:smith-uniqueness","aa:def:determinantal-ideals",
                     "aa:def:trace-discriminant",
                     "aa:lem:trace-discriminant-base-change"):
            self.assertIn(name,labels)

if __name__=="__main__":
    unittest.main()
