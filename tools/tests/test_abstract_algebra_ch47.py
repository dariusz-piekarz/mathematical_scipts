#!/usr/bin/env python3
"""AA-47: SymPy checks of rational integration, differential equations, Kovacic case 1."""
import unittest, re
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/"chapters/pl/abstract_algebra/47-algorytmy-rischa-i-kovacica.tex"
x,z=s.symbols("x z")

def eq(a,b=0):
    return s.cancel(s.together(a-b))==0

def rational_riccati_poly(q):
    """Executable version of AA-47 polynomial-potential rational-Riccati test.

    Returns a rational solution or None. For algebraic test coefficients
    sqrt() belongs to the chosen effective algebraic closure.
    """
    q=s.Poly(q,x)
    degree=q.degree()
    if degree==0:
        return s.sqrt(q.as_expr())
    if degree%2:
        return None
    d=degree//2
    top=s.sqrt(q.LC())
    for lead in (top,-top):
        omega=lead*x**d
        for power in range(2*d-1,d-1,-1):
            target=q.coeff_monomial(x**power)
            present=s.expand(omega**2).coeff(x,power)
            omega+=s.simplify((target-present)/(2*lead))*x**(power-d)
        omega=s.expand(omega)
        high=s.Poly(q.as_expr()-omega**2,x)
        if high.degree()>=d:
            continue
        coefficient=s.expand(q.as_expr()-omega**2-s.diff(omega,x)).coeff(x,d-1)
        n=s.simplify(coefficient/(2*lead))
        if n.is_integer is not True or n.is_nonnegative is not True:
            continue
        n=int(n)
        p_vars=s.symbols("p0:"+str(n))
        P=x**n+sum(p_vars[k]*x**k for k in range(n))
        residual=s.Poly(s.expand(s.diff(P,x,2)+2*omega*s.diff(P,x)
                               +(s.diff(omega,x)+omega**2-q.as_expr())*P),x)
        equations=[s.Eq(v,0) for v in residual.all_coeffs()]
        if not p_vars:
            if all(s.simplify(v)==0 for v in residual.all_coeffs()):
                return omega
            continue
        solutions=s.solve(equations,list(p_vars),dict=True)
        for sol in solutions:
            vals={v:sol.get(v,0) for v in p_vars}
            poly=s.factor(P.subs(vals))
            if eq(s.diff(poly,x,2)+2*omega*s.diff(poly,x)
                +(s.diff(omega,x)+omega**2-q.as_expr())*poly):
                return s.cancel(omega+s.diff(poly,x)/poly)
    return None

class AA47SymPyRegression(unittest.TestCase):
    def test_01_rational_hermite_decomposition(self):
        R=x**2-s.Rational(3,2)/(x-1)**2
        f=2*x+3/(x-1)**3+5/(x-1)
        self.assertTrue(eq(f,s.diff(R,x)+5/(x-1)))
        self.assertEqual(s.residue(f,x,1),5)
        self.assertEqual(s.residue(s.diff(R,x),x,1),0)

    def test_02_zero_residues_are_rationally_integrable(self):
        examples=[s.diff((x+1)/(x**2+1),x),
                  s.diff(1/x**3+3*x,x),
                  s.diff((x**2+1)/(x-2)**4,x)]
        for f in examples:
            den=s.denom(s.cancel(f))
            roots=s.solve(s.Eq(den,0),x)
            self.assertTrue(all(eq(s.residue(f,x,a)) for a in roots))

    def test_03_rothstein_trager_resultant(self):
        A=s.Integer(1);B=x**2+1;Bp=s.diff(B,x)
        resultant=s.resultant(B,A-z*Bp,x)
        self.assertTrue(eq(resultant,1+4*z**2))
        self.assertTrue(eq(1/B,1/(2*s.I)*(1/(x-s.I)-1/(x+s.I))))

    def test_04_rt_equal_residues(self):
        A=2*x;B=x**2+1
        r=s.factor(s.resultant(B,A-z*s.diff(B,x),x))
        self.assertTrue(eq(r,4*(1-z)**2))
        self.assertEqual(s.monic(s.Poly(s.gcd(B,A-s.diff(B,x)),x)).as_expr(),B)
        self.assertTrue(eq(A/B,s.diff(B,x)/B))

    def test_05_risch_polynomial_h_positive(self):
        examples=[(s.Integer(1),-1/x,1/x**2-1/x),
                  (-2*x,s.Rational(-1,2),x),
                  (2*x,s.Rational(1,2),x),
                  (3,x**2+2,s.diff(x**2+2,x)+3*(x**2+2))]
        for h,r,rhs in examples:
            self.assertTrue(eq(s.diff(r,x)+h*r,rhs))

    def test_06_risch_simple_pole_and_degree_obstruction(self):
        self.assertEqual(s.residue(1/x,x,0),1)
        # With h regular, r'+h*r cannot have a simple pole if RHS has only one.
        for m in range(1,7):
            r=x**(-m)
            self.assertEqual(s.limit(x**(m+1)*(s.diff(r,x)+r),x,0),-m)
        self.assertLess(s.degree(s.Integer(1),x),s.degree(-2*x,x))

    def test_07_riccati_algorithm_positive(self):
        for q in (x**2+1,x**2-1,x**2+3,x**4+2*x,x**4+4*x):
            r=rational_riccati_poly(q)
            self.assertIsNotNone(r,q)
            self.assertTrue(eq(s.diff(r,x)+r*r,q),(q,r))

    def test_08_riccati_algorithm_negative_or_constant(self):
        for q in (x,x**3+1,x**5+3*x+1,x**2+2):
            self.assertIsNone(rational_riccati_poly(q),q)
        for q in (s.Integer(0),s.Integer(9),s.Rational(1,4)):
            r=rational_riccati_poly(q)
            self.assertIsNotNone(r)
            self.assertTrue(eq(r*r,q))

    def test_09_kovacic_quadratic_riccati(self):
        r=s.sqrt(x)-1/(4*x)
        q=x+5/(16*x*x)
        self.assertTrue(eq(s.diff(r,x)+r*r,q))
        self.assertTrue(eq(s.diff(x**(-s.Rational(1,4))*
                                  s.exp(s.Rational(2,3)*x**s.Rational(3,2)),x,2)
                           / (x**(-s.Rational(1,4))*
                              s.exp(s.Rational(2,3)*x**s.Rational(3,2))),q))

    def test_10_normal_form(self):
        a=2/x;b=3
        q=s.diff(a,x)/2+a*a/4-b
        self.assertTrue(eq(q,-3))
        w=s.symbols("w")
        # explicit y=z/x for a=2/x, z=exp(i sqrt(3) x) satisfies y''+2/x y'+3y=0
        yy=s.exp(s.I*s.sqrt(3)*x)/x
        self.assertTrue(eq(s.diff(yy,x,2)+a*s.diff(yy,x)+b*yy))

    def test_11_labels_proofs_and_scope(self):
        text=SRC.read_text(encoding="utf-8")
        labs=re.findall(r"\\label\{([^}]+)\}",text)
        self.assertEqual(len(labs),len(set(labs)))
        self.assertGreaterEqual(len(labs),27)
        self.assertEqual(text.count(r"\begin{proof}"),text.count(r"\end{proof}"))
        self.assertGreaterEqual(text.count(r"\begin{proof}"),8)
        for lab in ("aa:tw:rational-integration-algorithm",
                    "aa:tw:rothstein-trager",
                    "aa:tw:risch-polynomial-h-algorithm",
                    "aa:tw:kovacic-polynomial-rational-decision",
                    "aa:tw:kovacic-classification"):
            self.assertIn(r"\label{"+lab+"}",text)
        self.assertIn("wynik klasyczny",text.lower())
if __name__=="__main__":unittest.main()
