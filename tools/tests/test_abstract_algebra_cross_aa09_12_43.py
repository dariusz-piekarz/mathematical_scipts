"""AA-X31: derivations on quotients, localizations and differential ideals.

Exact symbolic regressions. They test examples; the general theorems
are proved in the corresponding audit report.
"""
from itertools import product
from pathlib import Path
import unittest
import sympy as sp

x, y = sp.symbols("x y")
f = y - x**2

def delta(poly):
    """Q-derivation of Q[x,y]: D(x)=x, D(y)=2y."""
    return sp.diff(poly, x)*x + sp.diff(poly, y)*2*y

def euler(poly):
    """Q-derivation on Q[x,y]: D(x)=x, D(y)=y."""
    return sp.diff(poly, x)*x + sp.diff(poly, y)*y

def trunc_add(a, b, p):
    return tuple((q+r) % p for q, r in zip(a,b))

def trunc_mul(a, b, p):
    """Multiplication in F_p[eps]/(eps^2)."""
    return ((a[0]*b[0]) % p, (a[0]*b[1]+a[1]*b[0]) % p)

def trunc_d(a, p):
    """Candidate D(a+b eps)=b."""
    return (a[1] % p, 0)


class TestAA31DerivationsQuotientsLocalization(unittest.TestCase):
    def test_stable_ideal_and_quotient_derivation(self):
        # (y-x^2) is D-stable for D=x d/dx + 2y d/dy.
        self.assertEqual(sp.expand(delta(f)-2*f),0)
        polynomials = (1,x,y,x*y,x**3+y**2,(x+y)**4,3*x*y**2+x**5)
        multipliers = (1,x+y,2*x**2+y,3*y*x)
        for P in polynomials:
            for H in multipliers:
                with self.subTest(P=str(P),H=str(H)):
                    difference = sp.expand(delta(P+f*H)-delta(P))
                    self.assertEqual(sp.expand(sp.rem(difference,f,y)),0)
                    self.assertEqual(
                        sp.simplify(delta(P).subs(y,x**2)-
                                    x*sp.diff(sp.sympify(P).subs(y,x**2),x)),0)

    def test_nonstable_ideals_do_not_admit_induced_derivation(self):
        self.assertEqual(sp.diff(x,x),1)
        self.assertNotEqual(sp.rem(sp.diff(x,x),x,x),0)
        self.assertNotEqual(sp.rem(sp.diff(x**2,x),x**2,x),0)
        # The failure already occurs on two representatives of zero:
        # x+(x)=0+(x), but D(x)=1 and D(0)=0 differ in the quotient.
        self.assertEqual(sp.rem(x,x,x),0)
        self.assertEqual(sp.rem(1,x,x),1)

    def test_localization_derivative_quotient_formula(self):
        # R=Q[x,y], S={x^k}; every x^k becomes invertible.
        polynomials = (1,x,y,x*y,x**2+y,3*x**3+x*y**2,(x+y)**3)
        for P,k in product(polynomials,range(5)):
            with self.subTest(P=str(P),k=k):
                expr=P/x**k
                expected=(x**k*delta(P)-P*delta(x**k))/x**(2*k)
                self.assertEqual(sp.simplify(delta(expr)-expected),0)
                self.assertEqual(sp.simplify(delta(expr)+
                                  delta(x**k)*P/x**(2*k)-
                                  delta(P)/x**k),0)
                # Two different fractional representations agree.
                for r in (0,1,3):
                    other=P*x**r/x**(k+r)
                    self.assertEqual(sp.simplify(delta(expr)-delta(other)),0)

    def test_localization_quotient_compatibility(self):
        # (S^-1 R)/(S^-1(y-x^2)) = Q[x,x^-1],
        # with the induced D(x)=x.
        polynomials = (1,x,y,x*y,x**3+y**2,(x+y)**3)
        for P,k in product(polynomials,range(5)):
            with self.subTest(P=str(P),k=k):
                q=P/x**k
                qbar=sp.cancel(q.subs(y,x**2))
                self.assertEqual(
                    sp.simplify(delta(q).subs(y,x**2)-x*sp.diff(qbar,x)),0)
                # A representative may be changed by (y-x^2)/x^k.
                changed=q+f*(1+x+y)/x**k
                self.assertEqual(
                    sp.simplify((delta(changed)-delta(q)).subs(y,x**2)),0)

    def test_positive_characteristic_nilpotent_quotient(self):
        # In characteristic p, (x^p) is D-stable for D=d/dx.
        for p in (2,3,5,7):
            for P in (1,x,x**2+1,x**3+2*x+1):
                with self.subTest(p=p,P=str(P)):
                    d=sp.Poly(sp.diff(x**p*P,x),x,modulus=p)
                    modulus=sp.Poly(x**p,x,modulus=p)
                    self.assertTrue(d.rem(modulus).is_zero)
            # In characteristic zero the same ideal is not stable.
            self.assertNotEqual(sp.rem(sp.diff(x**p,x),x**p,x),0)
        # Full multiplication table for F2[eps]/(eps^2).
        elems=list(product(range(2),repeat=2))
        for a,b in product(elems,repeat=2):
            lhs=trunc_d(trunc_mul(a,b,2),2)
            rhs=trunc_add(trunc_mul(trunc_d(a,2),b,2),
                          trunc_mul(a,trunc_d(b,2),2),2)
            self.assertEqual(lhs,rhs)
        eps=(0,1)
        # In F3[eps]/(eps^2), the same candidate is impossible:
        self.assertNotEqual(trunc_d(trunc_mul(eps,eps,3),3),
                            trunc_add(trunc_mul(trunc_d(eps,3),eps,3),
                                      trunc_mul(eps,trunc_d(eps,3),3),3))

    def test_localized_differential_ideal_remains_stable(self):
        # I=(xy) is stable for E=x d/dx+y d/dy.
        self.assertEqual(sp.expand(euler(x*y)-2*x*y),0)
        for P,k in product((1,x,y,x+y,x**2+y**2,(x+y)**3),range(5)):
            with self.subTest(P=str(P),k=k):
                element=x*y*P/x**k
                derived=euler(element)
                # S^-1(xy)=(y) because x becomes invertible.
                self.assertEqual(sp.simplify(derived.subs(y,0)),0)

    def test_source_chapters_and_reference_contract(self):
        base=Path(__file__).resolve().parents[2]/"chapters/pl/abstract_algebra"
        self.assertEqual(len(list(base.glob("[0-9][0-9]-*.tex"))),50)
        sources={
            9:(base/"09-pierscienie-idealy-i-homomorfizmy.tex").read_text(encoding="utf-8"),
            12:(base/"12-pierwiastniki-idealow-i-lokalizacja-pierscieni.tex").read_text(encoding="utf-8"),
            43:(base/"43-ciala-rozniczkowe-derywacje-i-rozszerzenia.tex").read_text(encoding="utf-8"),
        }
        for label in ("aa:def:ideal","aa:tw:ring-quotient"):
            self.assertIn(r"\label{"+label+"}",sources[9])
        for label in ("aa:def:localization","aa:tw:localization-universal"):
            self.assertIn(r"\label{"+label+"}",sources[12])
        for label in ("aa:def:differential-field","aa:tw:algebraic-derivation-extension"):
            self.assertIn(r"\label{"+label+"}",sources[43])


if __name__=="__main__":
    unittest.main()
