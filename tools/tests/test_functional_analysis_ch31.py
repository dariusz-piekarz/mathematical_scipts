import itertools
import math
import re
import unittest
from fractions import Fraction as F
from pathlib import Path

DIR=Path(__file__).resolve().parents[2]/"chapters/pl/functional_analysis"
S=next(DIR.glob("31-*.tex")).read_text(encoding="utf-8")

class Chapter31(unittest.TestCase):
    def test_structure(self):
        labels=re.findall(r"\\label\{([^}]+)\}",S)
        self.assertEqual(len(labels),len(set(labels)))
        stack=[]
        for op,env in re.findall(r"\\(begin|end)\{([^}]+)\}",S):
            if op=="begin": stack.append(env)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)
        ctx="\n".join(p.read_text(encoding="utf-8") for p in DIR.glob("*.tex"))
        for label in re.findall(r"\\(?:ref|hyperref)\{([^}]+)\}",S)+re.findall(r"\\hyperref\[([^\]]+)\]",S):
            self.assertIn(r"\label{"+label+"}",ctx)

    def test_FA31_resolvent_01(self):
        self.assertIn(r"(-1)^n(z-z_0)^n R_a(z_0)^{n+1}",S)
        for a,z,w in itertools.product(range(-4,5),repeat=3):
            if z!=a and w!=a:
                self.assertEqual(F(1,z-a)-F(1,w-a),F(w-z,(z-a)*(w-a)))

    def test_FA31_radius_01(self):
        self.assertIn(r"L/|z|<q<1",S)
        self.assertIn(r"1_A-a^{N+1}z^{-N-1}",S)
        for a,z,N in itertools.product(range(-3,4),range(1,5),range(8)):
            self.assertEqual((z-a)*sum(F(a**n,z**(n+1)) for n in range(N+1)),1-F(a**(N+1),z**(N+1)))

    def test_FA31_maximal_ideal_01(self):
        for x in ("suma łańcucha jest ideałem",r"\overline M=M",r"[c][b]=[1_A]",r"[1_A]^2=[1_A]"):
            self.assertIn(x,S)

    def test_FA31_contour_01(self):
        for x in (r"\overline D_i\subset D_o",r"\overline D_0\subset D_1\cap D_2","Wewnętrzne krawędzie usuwamy",r"\operatorname{Ind}_{\Gamma_o}(w)=1"):
            self.assertIn(x,S)
        # Exact winding number for an integer square chain; horizontal ray
        # through half-integer cell centers avoids all vertices.
        for mask in range(1,1<<9):
            cells={(i,j) for i in range(3) for j in range(3) if mask&(1<<(3*i+j))}
            edges=set()
            for i,j in cells:
                pts=[(i,j),(i+1,j),(i+1,j+1),(i,j+1)]
                for u,v in zip(pts,pts[1:]+pts[:1]):
                    if (v,u) in edges: edges.remove((v,u))
                    else: edges.add((u,v))
            for i,j in itertools.product(range(-1,4),repeat=2):
                x,y=F(2*i+1,2),F(2*j+1,2)
                winding=sum((1 if v[1]>u[1] else -1)
                            for u,v in edges if u[0]==v[0] and u[0]>x
                            and min(u[1],v[1])<y<max(u[1],v[1]))
                self.assertEqual(winding,int((i,j) in cells))

    def test_FA31_bernstein_01(self):
        self.assertIn(r"k(k-1)\binom nk",S)
        for n in range(1,13):
            for t in [F(j,8) for j in range(9)]:
                p=[math.comb(n,k)*t**k*(1-t)**(n-k) for k in range(n+1)]
                self.assertEqual(sum(p),1)
                self.assertEqual(sum(F(k,n)*p[k] for k in range(n+1)),t)
                self.assertEqual(sum((F(k,n)-t)**2*p[k] for k in range(n+1)),t*(1-t)/n)

    def test_FA31_shift_01(self):
        self.assertIn(r"dla $\lambda=0$ daje $x=0$",S)
        self.assertIn(r"\chi\mapsto\chi(e_1)",S)

if __name__=="__main__":
    unittest.main()
