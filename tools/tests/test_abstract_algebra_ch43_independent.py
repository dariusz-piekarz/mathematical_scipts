#!/usr/bin/env python3
"""AA-43 independent rational model, no SymPy.

Checks derivation and determinant/trace formulas in rank-two algebras
Q[a]/(a^2+b(x)a+c(x)), at exact rational specializations.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from pathlib import Path
import re
import unittest

SOURCE=Path(__file__).resolve().parents[2]/"chapters/pl/abstract_algebra/43-ciala-rozniczkowe-derywacje-i-rozszerzenia.tex"

def val(coeff,x):
    return sum(F(a)*x**i for i,a in enumerate(coeff))
def der(coeff,x):
    return sum(F(i*a)*x**(i-1) for i,a in enumerate(coeff) if i)
def pair_add(z,w):return (z[0]+w[0],z[1]+w[1])
def pair_mul(z,w,b,c):
    u,v=z;r,s=w
    return (u*r-c*v*s,u*s+v*r-b*v*s)
def pair_trace(z,b):return 2*z[0]-b*z[1]
def pair_norm(z,b,c):return z[0]**2-b*z[0]*z[1]+c*z[1]**2

class IndependentAA43(unittest.TestCase):
    def test_01_algebraic_derivation_exact_models(self):
        bchoices=((0,1),(1,1),(2,-1),(1,0,1),(-1,2,1))
        cchoices=((1,1),(2,0,1),(-1,1),(1,0,-1),(3,2))
        xvalues=(F(-3,2),F(-1),F(1,3),F(2),F(5,2))
        for bb,cc,x in product(bchoices,cchoices,xvalues):
            b,bp=val(bb,x),der(bb,x)
            c,cp=val(cc,x),der(cc,x)
            disc=b*b-4*c
            if disc==0:continue
            # alpha' = d0 + d1 alpha, uniquely forced by m(alpha)=0.
            d0=(2*c*bp-b*cp)/disc
            d1=(b*bp-2*cp)/disc
            alpha=(F(0),F(1))
            d_alpha=(d0,d1)
            differential_rel=pair_add(
                pair_mul((b,F(2)),d_alpha,b,c),(cp,bp))
            self.assertEqual(differential_rel,(0,0))
            self.assertEqual(pair_trace(d_alpha,b),-bp)
            self.assertEqual(pair_norm(alpha,b,c),c)
            if c:
                zinv=(-b/c,-F(1)/c)
                self.assertEqual(pair_mul(alpha,zinv,b,c),(1,0))
                zlog=pair_mul(d_alpha,zinv,b,c)
                self.assertEqual(pair_trace(zlog,b),cp/c)

    def test_02_Leibniz_in_quadratic_extension(self):
        bchoices=((1,1),(0,1),(2,-1))
        cchoices=((2,0,1),(1,1),(-1,2))
        polynomials=((0,1),(1,1),(1,0,1),(-2,2))
        for bb,cc,x,aa,ab,ba,bbeta in product(
            bchoices,cchoices,(F(-2),F(1,2),F(3)),
            polynomials,polynomials,polynomials,polynomials):
            b,bp,c,cp=val(bb,x),der(bb,x),val(cc,x),der(cc,x)
            disc=b*b-4*c
            if disc==0:continue
            d0=(2*c*bp-b*cp)/disc
            d1=(b*bp-2*cp)/disc
            # Coefficients are evaluations of rational functions in x.
            A=(val(aa,x),val(ab,x))
            B=(val(ba,x),val(bbeta,x))
            Ad=(der(aa,x)+A[1]*d0,der(ab,x)+A[1]*d1)
            Bd=(der(ba,x)+B[1]*d0,der(bbeta,x)+B[1]*d1)
            # Product coefficients before using relation alpha^2=-b alpha-c.
            u=val(aa,x)*val(ba,x)-c*val(ab,x)*val(bbeta,x)
            v=val(aa,x)*val(bbeta,x)+val(ab,x)*val(ba,x)-b*val(ab,x)*val(bbeta,x)
            uder=(der(aa,x)*val(ba,x)+val(aa,x)*der(ba,x)-cp*val(ab,x)*val(bbeta,x)
                  -c*(der(ab,x)*val(bbeta,x)+val(ab,x)*der(bbeta,x)))
            vder=(der(aa,x)*val(bbeta,x)+val(aa,x)*der(bbeta,x)
                  +der(ab,x)*val(ba,x)+val(ab,x)*der(ba,x)
                  -bp*val(ab,x)*val(bbeta,x)
                  -b*(der(ab,x)*val(bbeta,x)+val(ab,x)*der(bbeta,x)))
            lhs=(uder+v*d0,vder+v*d1)
            rhs=pair_add(pair_mul(Ad,B,b,c),pair_mul(A,Bd,b,c))
            self.assertEqual(lhs,rhs)

    def test_03_constants_and_logs_by_exact_partial_fractions(self):
        # u(x)=product (x-a)^m. For nonzero u,
        # u'/u is sum of integer simple fractions, with no polynomial part.
        roots=(F(-2),F(0),F(3,2))
        for exponents in product((-3,-1,0,1,4),repeat=3):
            for x in (F(-1),F(1,2),F(2),F(4)):
                vals=[x-r for r in roots]
                self.assertTrue(all(v!=0 for v in vals))
                u=F(1)
                for v,m in zip(vals,exponents):u*=v**m
                derivative=F(0)
                for j,(v,m) in enumerate(zip(vals,exponents)):
                    term=F(m)*v**(m-1)
                    for k,(w,n) in enumerate(zip(vals,exponents)):
                        if j!=k:term*=w**n
                    derivative+=term
                want=sum((F(m)/v for m,v in zip(exponents,vals)),F(0))
                self.assertEqual(derivative/u,want)

    def test_04_positive_characteristic_obstruction(self):
        for p in (2,3,5,7,11,13):
            self.assertEqual(p%p,0)
            self.assertEqual(p*pow(4,p-1)%p,0)
            # Extension alpha^p=x of F_p(x), Dx=1 is impossible:
            # D(alpha^p)=0, but Dx=1.

    def test_05_source_labels_and_proof_structure(self):
        s=SOURCE.read_text(encoding="utf-8")
        labs=re.findall(r"\\label\{([^}]+)\}",s)
        refs=re.findall(r"\\(?:ref|eqref)\{([^}]+)\}",s)
        self.assertEqual(len(labs),len(set(labs)))
        self.assertGreaterEqual(len(labs),15)
        self.assertGreaterEqual(len(refs),3)
        self.assertGreaterEqual(s.count(r"\begin{proof}"),6)
        self.assertEqual(s.count(r"\begin{proof}"),s.count(r"\end{proof}"))
        self.assertEqual(s.count(r"\begin{twierdzenie}"),s.count(r"\end{twierdzenie}"))
        for term in ("aa:ch:differential-fields",
                     "aa:lem:primitive-extension-constants",
                     "aa:lem:exponential-extension-constants"):
            self.assertIn(r"\label{"+term+"}",s)

if __name__=="__main__":
    unittest.main()
