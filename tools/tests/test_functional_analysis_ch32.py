import itertools
import re
import unittest
from fractions import Fraction as F
from pathlib import Path

DIR=Path(__file__).resolve().parents[2]/"chapters/pl/functional_analysis"
S=next(DIR.glob("32-*.tex")).read_text(encoding="utf-8")

class Chapter32(unittest.TestCase):
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
        for label in re.findall(r"\\ref\{([^}]+)\}",S)+re.findall(r"\\hyperref\[([^\]]+)\]",S):
            self.assertIn(r"\label{"+label+"}",ctx)

    def test_FA32_pvm_integral_01(self):
        for phrase in (r"\label{lem:pvm-integral32}",r"I_E(s)=\sum_{j=1}^m c_j E(B_j)",
                       "wspólne rozdrobnienie podziałów","skończone","wahanie całkowite",
                       "niezależnie zdefiniowany rachunek"):
            self.assertIn(phrase,S)
        V=list(itertools.product(range(-1,2),repeat=3))
        for f,g,x in itertools.product(V,repeat=3):
            fx=[a*b for a,b in zip(f,x)]
            fgx=[a*b*c for a,b,c in zip(f,g,x)]
            self.assertEqual(fgx,[a*b for a,b in zip(g,fx)])
            self.assertEqual(sum(a*a for a in fx),sum(a*a*b*b for a,b in zip(f,x)))
            self.assertLessEqual(sum(a*a for a in fx),max(abs(a) for a in f)**2*sum(b*b for b in x))

    def test_FA32_projection_01(self):
        for a,b in itertools.product(range(8),repeat=2):
            for x in itertools.product(range(-1,2),repeat=3):
                proj=lambda m,y: tuple(v if m&(1<<i) else 0 for i,v in enumerate(y))
                self.assertEqual(proj(a,proj(b,x)),proj(a&b,x))
                if not a&b:
                    self.assertEqual(proj(a|b,x),tuple(u+v for u,v in zip(proj(a,x),proj(b,x))))

    def test_FA32_cyclic_01(self):
        for phrase in ("półnorma",r"\|h-\chi_B\|_{L^2(\nu_a)}^2",
                       "przeplata również","Gęstość w $L^2$ daje równość izometrii"):
            self.assertIn(phrase,S)

    def test_FA32_spectral_permanence_01(self):
        self.assertIn(r"m=\|B^{-1}\|^{-2}",S)
        self.assertIn(r"\sigma_A(f(T))",S)
        self.assertIn(r"4\operatorname{Re}\langle Rx,y\rangle",S)

    def test_FA32_positive_root_polar_01(self):
        for phrase in (r"p_n(B^2)\to B",r"p_n(A)\to A^{1/2}",r"B=A^{1/2}",
                       r"\langle U^*Ux,y\rangle=\langle x_1,y_1\rangle"):
            self.assertIn(phrase,S)
        for a,x in itertools.product(itertools.product(range(-2,3),repeat=3),
                                     itertools.product(range(-2,3),repeat=3)):
            p=[abs(v) for v in a]
            u=[0 if v==0 else v//abs(v) for v in a]
            self.assertEqual([v*w*y for v,w,y in zip(u,p,x)],[v*y for v,y in zip(a,x)])
            self.assertEqual([v*v for v in u],[int(v!=0) for v in a])

    def test_FA32_spectral_limits_01(self):
        self.assertIn(r"$t_n<t$",S)
        self.assertIn(r"\varepsilon/2<\varepsilon",S)
        self.assertIn(r"\{0\}\cup\{|\lambda|:",S)
        for a in itertools.product(range(-1,2),repeat=3):
            for mask in range(8):
                residual=[v if not mask&(1<<i) else 0 for i,v in enumerate(a)]
                self.assertEqual(max(map(abs,residual)),max([0]+[abs(v) for i,v in enumerate(a) if not mask&(1<<i)]))

    def test_FA32_spectral_examples_01(self):
        for phrase in (r"\lambda/2<0",r"\chi_A/\sqrt{\lambda_1(A)}",
                       r"\chi_{a^{-1}(B)}",r"\{i:|x_i|\ge1/n\}"):
            self.assertIn(phrase,S)

    def test_FA32_polarization_02(self):
        self.assertIn(r"i^k\mu_{x+i^k y}(B)",S)
        values=[complex(a,b) for a,b in itertools.product(range(-1,2),repeat=2)]
        for x,y in itertools.product(itertools.product(values,repeat=2),repeat=2):
            for mask in range(4):
                q=lambda v: sum(abs(z.real)**2+abs(z.imag)**2
                                for j,z in enumerate(v) if mask&(1<<j))
                lhs=sum(x[j]*y[j].conjugate() for j in range(2) if mask&(1<<j))
                rhs=sum((1j)**k*q([a+(1j)**k*b for a,b in zip(x,y)])
                        for k in range(4))/4
                self.assertEqual(lhs,rhs)

    def test_FA32_norm_threshold_02(self):
        self.assertIn(r"M\geq\|f(T)\|",S)
        for f in itertools.product(range(-2,3),repeat=3):
            for support in range(8):
                norm=max([0]+[abs(v) for j,v in enumerate(f) if support&(1<<j)])
                for m in range(4):
                    is_null=not any(abs(v)>m and support&(1<<j) for j,v in enumerate(f))
                    self.assertEqual(is_null,m>=norm)

    def test_FA32_polar_final_space_02(self):
        for phrase in (r"$H=\{0\}$",r"|u|^2=\chi_{K\setminus\{0\}}",
                       r"u(T)|T|x=Tx",r"\overline{\operatorname{Ran}T}",
                       r"E(K\setminus\{0\})"):
            self.assertIn(phrase,S)

if __name__=="__main__":
    unittest.main()
