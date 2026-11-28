import itertools
import re
import unittest
from pathlib import Path
from fractions import Fraction as F
DIR = Path(__file__).resolve().parents[2] / "chapters/pl/functional_analysis"
S = next(DIR.glob("30-*.tex")).read_text(encoding="utf-8")

class Chapter30(unittest.TestCase):
    def test_structure(self):
        labels = re.findall(r"\\label\{([^}]+)\}", S)
        self.assertEqual(len(labels), len(set(labels)))
        stack=[]
        for op,env in re.findall(r"\\(begin|end)\{([^}]+)\}",S):
            if op=="begin": stack.append(env)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)
        ctx="\n".join(p.read_text(encoding="utf-8") for p in DIR.glob("*.tex")
                      if p.name[:2].isdigit() and int(p.name[:2])<=30)
        for ref in re.findall(r"\\ref\{([^}]+)\}",S):
            self.assertIn(r"\label{"+ref+"}",ctx)

    def test_FA30_atkinson_noncircular_01(self):
        for phrase in ("wtedy i tylko wtedy",r"g\mapsto g\circ q",
                       "przedłużenia pozostają liniowo niezależne",
                       "potrzeba z góry zakładać",r"\ker T'\subseteq\ker(I_{Y'}-K_2')"):
            self.assertIn(phrase,S)
        # finite model of annihilator of a rank-r coordinate subspace
        for n in range(6):
            for r in range(n+1):
                count=sum(all(v[j]==0 for j in range(r))
                          for v in itertools.product(range(2),repeat=n))
                self.assertEqual(count,2**(n-r))

    def test_FA30_complements_01(self):
        self.assertIn(r"\ker P_C=R",S)
        self.assertIn(r"STx=x_1",S)
        self.assertIn(r"TSy=r",S)

    def test_FA30_hilbert_reduction_01(self):
        self.assertIn(r"\|K-P_WK\|\le1/2<1",S)
        self.assertIn(r"(a,z)\mapsto(a+Gz,z)",S)
        for a,b,w,z in itertools.product(range(-2,3),repeat=4):
            self.assertEqual((a*w-b*z)+b*z,a*w)

    def test_FA30_schur_reduction_01(self):
        self.assertIn(r"M=E-FD^{-1}B",S)
        self.assertIn(r"\delta=(1+\|A^{-1}\|\|P_R\|)^{-1}",S)
        for b,d,e,f,n,x in itertools.product(range(-2,3),repeat=6):
            if not d: continue
            xp=F(x)-F(b*n,d)
            r=b*n+d*xp
            c=e*n+f*xp
            self.assertEqual(r,d*x)
            self.assertEqual(c-F(f*r,d),(e-F(f*b,d))*n)

    def test_FA30_generalized_eigenspace_01(self):
        self.assertIn(r"(K-\lambda I_X)N_m\subseteq N_{m-1}",S)
        self.assertIn("nietrywialna zależność liniowa o minimalnej liczbie",S)

    def test_FA30_volterra_01(self):
        self.assertIn(r"\int_s^t (u-s)^{n-1}/(n-1)!",S)
        self.assertIn(r"I_X-(V/\lambda)^{n+1}",S)
        import math
        for m,n in itertools.product(range(6),range(1,8)):
            v=F(math.factorial(m),math.factorial(m+n))
            self.assertEqual(v/F(m+n+1),F(math.factorial(m),math.factorial(m+n+1)))
            self.assertLessEqual(v,F(1,math.factorial(n)))

    def test_FA30_closed_range_01(self):
        self.assertIn(r"\|u_n-u_m\|\le c^{-1}\|Tu_n-Tu_m\|",S)
        self.assertIn(r"\dim(C/\operatorname{ran}M)",S)

    def test_FA30_compact_perturbation_path_01(self):
        for phrase in (r"\|(T+tK)-(T+sK)\|=|t-s|\|K\|",
                       "funkcją lokalnie stałą",r"A^{-1}D=I_{X_1}+A^{-1}(D-A)"):
            self.assertIn(phrase,S)
        for t,s,k in itertools.product((F(0),F(1,3),F(1)),repeat=3):
            self.assertEqual(abs(t*k-s*k),abs(t-s)*abs(k))

    def test_FA30_spectral_endpoints_01(self):
        for phrase in (r"A_0[I_X+(\lambda-\lambda_0)A_0^{-1}]",
                       r"\bigcup_{m\ge1}N_m=N_{m_0}",
                       r"0\in\sigma(V)",r"H/\operatorname{ran}T"):
            self.assertIn(phrase,S)
        for a,d in itertools.product(range(-3,4),repeat=2):
            if a:
                self.assertEqual(a*(1+F(d,a)),a+d)

if __name__=="__main__":
    unittest.main()
