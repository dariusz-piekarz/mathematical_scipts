"""Independent stabilization re-audit tests for AA-27 (Artin--Schreier)."""
import os
import re
import unittest
from pathlib import Path
from itertools import product
from sympy import Poly, symbols

DEFAULT_SOURCE=Path(__file__).resolve().parents[2]/'chapters/pl/abstract_algebra/27-teoria-artina-schreiera.tex'
SOURCE_PATH=Path(os.getenv('AA27_SOURCE', DEFAULT_SOURCE))
SRC=SOURCE_PATH.read_text(encoding='utf-8')
x,t=symbols('x t')

class Structure(unittest.TestCase):
    def test_all_references_resolved_in_chapter_or_predecessors(self):
        labels=re.findall(r'\\label\{([^}]+)\}',SRC)
        refs=re.findall(r'\\ref\{([^}]+)\}',SRC)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertEqual(set(refs)-set(labels),{'aa:ch:trace-norm','aa:ch:kummer'})
    def test_environments_balanced(self):
        for env in ('definicja','proof','twierdzenie','stwierdzenie','przyklad','uwaga'):
            self.assertEqual(len(re.findall(r'\\begin\{'+env+r'\}',SRC)),len(re.findall(r'\\end\{'+env+r'\}',SRC)),env)
    def test_correct_characteristic_assumptions(self):
        self.assertIn(r'charakterystyki $p$',SRC)
        self.assertIn(r'\mathbb F_p\subseteq F',SRC)
        self.assertNotIn(r'\mathbb F_p\subset F',SRC)
    def test_converse_uses_trace_nondegeneracy(self):
        self.assertIn('jest niezdegenerowana',SRC)
        self.assertIn(r'\operatorname{Tr}_{E/F}(u)=1',SRC)
    def test_no_pre_audit_mistakes(self):
        for x in ('injekcją','injektywne','niezerowe jednowymiarowe','W Rozdziale','Na mocy Twierdzenia'):
            self.assertNotIn(x,SRC)

class PrimeFieldPolynomials(unittest.TestCase):
    def test_as_polynomial_irreducible_nonzero_class(self):
        for p in (2,3,5,7,11):
            for a in range(1,p):
                self.assertTrue(Poly(x**p-x-a,x,modulus=p).is_irreducible,(p,a))
    def test_as_polynomial_split_zero_class(self):
        for p in (2,3,5,7,11):
            P=Poly(x**p-x,x,modulus=p)
            prod=Poly(1,x,modulus=p)
            for c in range(p):prod*=Poly(x-c,x,modulus=p)
            self.assertEqual(P,prod)
    def test_derivative_never_zero(self):
        for p in (2,3,5,7,11):
            self.assertEqual(Poly(x**p-x-1,x,modulus=p).diff(),Poly(-1,x,modulus=p))
    def test_parameter_shifts_rational_function(self):
        for p in (2,3,5,7):
            for c,d in product(range(1,p),(t*t+t+1,t**3+2*t+3)):
                b=Poly(c*t+d**p-d,t,modulus=p)
                self.assertEqual(b-Poly(c*t,t,modulus=p),Poly(d**p-d,t,modulus=p))
    def test_no_polynomial_solves_t_as_as_image(self):
        for p in (2,3,5,7):
            for coeff in product(range(p),repeat=2):
                d=coeff[0]+coeff[1]*t
                self.assertNotEqual(Poly(d**p-d,t,modulus=p),Poly(t,t,modulus=p))

# Independent arithmetic implementation using SymPy quotient polynomials.
class ExtensionArithmetic(unittest.TestCase):
    def arithmetic(self,p):
        theta=symbols('theta')
        minimal=Poly(theta**p-theta-1,theta,modulus=p)
        def elem(expr):return Poly(expr,theta,modulus=p).rem(minimal)
        def tau(v):return elem(v.as_expr().subs(theta,theta+1))
        def trace(v):
            val=elem(0)
            for _ in range(p):
                val=elem(val.as_expr()+v.as_expr())
                v=tau(v)
            return val
        return elem,theta,tau,trace
    def test_trace_one_element(self):
        for p in (2,3,5):
            elem,theta,tau,trace=self.arithmetic(p)
            self.assertEqual(trace(elem(-theta**(p-1))),elem(1))
    def test_constructed_alpha_cocycle(self):
        for p in (2,3,5):
            elem,theta,tau,trace=self.arithmetic(p)
            u=elem(-theta**(p-1))
            alpha=elem(0)
            for j in range(p):
                alpha=elem(alpha.as_expr()-j*u.as_expr())
                u=tau(u)
            self.assertEqual(elem(tau(alpha).as_expr()-alpha.as_expr()),elem(1))
            self.assertEqual(tau(elem(alpha.as_expr()**p-alpha.as_expr())),elem(alpha.as_expr()**p-alpha.as_expr()))
    def test_as_kernel_size(self):
        for p in (2,3):
            elem,theta,tau,trace=self.arithmetic(p)
            kernel=[]
            for coeffs in product(range(p),repeat=p):
                v=elem(sum(coeffs[i]*theta**i for i in range(p)))
                if elem(v.as_expr()**p-v.as_expr())==elem(0):kernel.append(v)
            self.assertEqual(len(kernel),p)
            self.assertEqual(set(map(str,kernel)),set(str(elem(c)) for c in range(p)))

if __name__=='__main__':unittest.main(verbosity=2)
