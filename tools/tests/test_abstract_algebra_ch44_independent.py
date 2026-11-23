#!/usr/bin/env python3
"""AA-44: independent Fraction-polynomial oracle without SymPy."""
import unittest,re
from pathlib import Path
from fractions import Fraction as F
SRC=Path(__file__).resolve().parents[2]/"chapters/pl/abstract_algebra/44-twierdzenie-liouvillea-o-calkowaniu-elementarnym.tex"

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a or [F(0)]
def add(a,b,sgn=1):
    return trim([(a[i] if i<len(a) else 0)+sgn*(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))])
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return trim(c)
def div(a,b):
    a,b=trim(a),trim(b)
    assert b!=[0]
    q=[F(0)]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        j=len(a)-len(b);v=a[-1]/b[-1];q[j]+=v
        a=add(a,[0]*j+[v*w for w in b],-1)
    return trim(q),a
def coeff(p,x):return [F(a)*x+F(b) for a,b in p],[F(a) for a,b in p]
def derivative(v,dv,dt,exp):
    z=list(dv)+[F(0)]
    for j in range(1,len(v)):
        if exp:z[j]+=j*dt*v[j]
        else:z[j-1]+=j*dt*v[j]
    return trim(z)

class TestIndependentAA44(unittest.TestCase):
    def test_01_derivative_of_proper_fraction_stays_proper(self):
        for x in (F(-3,2),F(1,3),F(2)):
            A,Ad=coeff([(2,1),(1,2)],x)
            B,Bd=coeff([(3,1),(2,1),(0,1)],x)
            for exp,dt in ((False,F(1)/x),(True,2*x)):
                DA=derivative(A,Ad,dt,exp)
                DB=derivative(B,Bd,dt,exp)
                q,_=div(add(mul(DA,B),mul(A,DB),-1),mul(B,B))
                self.assertEqual(q,[0])
    def test_02_log_polynomial_part(self):
        for x in (F(-1),F(1,2),F(3)):
            b=x+4
            p,pd=coeff([(1,2),(3,1),(0,1)],x)
            q,qd=coeff([(1,3),(0,1)],x)
            for exp,dt in ((False,F(1)/x),(True,2*x)):
                dp=derivative(p,pd,dt,exp)
                dq=derivative(q,qd,dt,exp)
                ppoly,_=div(dp,p)
                qpoly,_=div(dq,q)
                actual=add([F(1)/b],add(ppoly,qpoly,-1))
                expected=[F(1)/b+(2*x if exp else 0)]
                self.assertEqual(actual,expected)
    def test_03_trace_norm_exact_examples(self):
        for x in (F(-7,3),F(0),F(4,5),F(3)):
            norm=-(x*x+1)
            norm_deriv=-2*x
            self.assertEqual(norm_deriv/(2*norm),x/(x*x+1))
    def test_04_exact_constant_and_logarithmic_derivation(self):
        for x in (F(-2),F(1,3),F(2)):
            # t-x: coefficient vectors and their x-derivatives.
            self.assertEqual(derivative([-x,F(1)],[-F(1),F(0)],F(1),False),[0])
            # 3t+x^2, with Dt=1/x: independent arithmetic.
            self.assertEqual(derivative([x*x,F(3)],[2*x,F(0)],F(1)/x,False),
                             [2*x+F(3)/x])
            # xt becomes a new constant if Dt/t=-1/x.
            self.assertEqual(derivative([F(0),x],[F(0),F(1)],-F(1)/x,True),[0])
    def test_05_structure(self):
        s=SRC.read_text(encoding="utf-8")
        labs=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labs),len(set(labs)))
        self.assertGreaterEqual(s.count(r"\begin{proof}"),5)
        self.assertEqual(s.count(r"\begin{proof}"),s.count(r"\end{proof}"))
        self.assertIn(r"\operatorname{pp}_t",s)
if __name__=="__main__":unittest.main()
