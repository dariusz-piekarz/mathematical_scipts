"""AA-X29: transcendence bases and algebraic extension of derivations.

Exact symbolic regression models, not formal proofs of the general theorem.
"""
from pathlib import Path
import unittest
import sympy as sp

x, y, u, v, t, z = sp.symbols("x y u v t z")


def dxy(expr):
    """The Q-derivation defined by Dx=1, Dy=x."""
    return sp.diff(expr, x) + x * sp.diff(expr, y)


def duv(expr):
    """Same derivation in coordinates u=x+y**2, v=y."""
    a = u - v**2
    return (1 + 2*a*v)*sp.diff(expr, u) + a*sp.diff(expr, v)


def dt(expr, prescribed):
    """Derivation of Q(t) with D(t)=prescribed in Q(t)."""
    return sp.diff(expr, t)*prescribed


class AA29TranscendenceDifferentialAudit(unittest.TestCase):
    def test_change_of_two_transcendence_generators(self):
        substitutions = {u:x+y**2, v:y}
        examples = (
            u, v, u**2+u*v+v**3, u**3-v**2+7*u*v,
            (u+v)/(u*v+1), (u**2+v)/(v**2+1),
        )
        for p in examples:
            with self.subTest(p=str(p)):
                in_xy = p.subs(substitutions, simultaneous=True)
                expected = duv(p).subs(substitutions, simultaneous=True)
                self.assertEqual(sp.simplify(dxy(in_xy)-expected), 0)
        self.assertEqual(sp.simplify(duv(u)-(1+2*v*(u-v**2))), 0)
        self.assertEqual(sp.simplify(duv(v)-(u-v**2)), 0)

    def test_rational_extension_preserves_product_and_quotient(self):
        a = (t**2+1)/(t-2)
        b = (t+3)/(t**2+2)
        rate = t**2+1
        self.assertEqual(sp.simplify(dt(a*b,rate)-a*dt(b,rate)-b*dt(a,rate)),0)
        self.assertEqual(sp.simplify(dt(1/a,rate)+dt(a,rate)/a**2),0)
        self.assertEqual(sp.simplify(dt(a/b,rate)-(b*dt(a,rate)-a*dt(b,rate))/b**2),0)

    def test_algebraic_extension_formula_is_representation_independent(self):
        # L=Q(t)(z), z^2=t^2+1. Multiplying the relation by a
        # polynomial cannot change the derivative of its class.
        f = z**2-t**2-1
        self.assertEqual(sp.expand(z*sp.diff(f,t)+t*sp.diff(f,z)),0)
        polynomials = (
            z+t, z**3+t*z, t**2*z+z**4,
            (z+1)*(t**3+z*t), t**2+3*z**2,
        )
        def numerator_of_derivative(p):
            return sp.expand(z*sp.diff(p,t)+t*sp.diff(p,z))
        for p in polynomials:
            for h in (1,z+t,z*t+t**2):
                with self.subTest(p=str(p),h=str(h)):
                    change = sp.expand(numerator_of_derivative(p+f*h)-numerator_of_derivative(p))
                    self.assertEqual(sp.rem(change,f,z).expand(),0)
        self.assertEqual(sp.rem(numerator_of_derivative(z**2)-2*t*z,f,z).expand(),0)

    def test_transcendence_basis_t_and_t_squared_characteristic_zero(self):
        # u=t^2 is a transcendence basis of Q(t)/Q.
        # On Q(u), prescribe D(u)=1; the forced extension has D(t)=1/(2t).
        dt_value = sp.Rational(1,2)/t
        self.assertEqual(sp.simplify(dt(t**2,dt_value)-1),0)
        self.assertEqual(sp.simplify(dt(t**4+3*t**2,dt_value)-(2*t**2+3)),0)
        # Conversely D(t)=1 forces D(t^2)=2t, not the independent choice 1.
        self.assertEqual(sp.simplify(dt(t**2,1)-2*t),0)

    def test_inseparable_characteristic_p_obstruction(self):
        # Both {t} and {t^p} are transcendence bases of F_p(t)/F_p.
        # D(t^p)=1 on F_p(t^p) does not extend to F_p(t).
        for p in (2,3,5,7,11):
            with self.subTest(p=p):
                derivative = sp.Poly(sp.diff(t**p,t),t,modulus=p)
                self.assertTrue(derivative.is_zero)
                # Any proposed value D(t) is multiplied by p*t^(p-1)=0.
                self.assertEqual(int((p*4)%p),0)
                self.assertNotEqual(1%p,0)

    def test_constants_and_nonconstant_prescriptions(self):
        # A derivation over Q can prescribe rational D(u), D(v).
        f_u, f_v = u**2+v, 1/(v+1)
        p = (u+v)/(u*v+1)
        delta = lambda r: f_u*sp.diff(r,u)+f_v*sp.diff(r,v)
        self.assertEqual(sp.simplify(delta(1)),0)
        self.assertEqual(sp.simplify(delta(u)-f_u),0)
        self.assertEqual(sp.simplify(delta(v)-f_v),0)
        self.assertEqual(sp.simplify(delta(u*p)-u*delta(p)-p*delta(u)),0)

    def test_canonical_chapters_and_references(self):
        root = Path(__file__).resolve().parents[2]
        base = root/"chapters/pl/abstract_algebra"
        self.assertEqual(len(list(base.glob("[0-9][0-9]-*.tex"))),56)
        ch37 = (base/"37-algebraiczna-niezaleznosc-i-bazy-transcendencji.tex").read_text(encoding="utf-8")
        ch43 = (base/"43-ciala-rozniczkowe-derywacje-i-rozszerzenia.tex").read_text(encoding="utf-8")
        self.assertIn(r"\label{aa:def:alg-independent}", ch37)
        self.assertIn(r"\label{aa:tw:transcendence-existence}", ch37)
        self.assertIn(r"\label{aa:tw:algebraic-derivation-extension}", ch43)
        self.assertIn(r"\ref{aa:wn:charzero-separable}", ch43)


if __name__ == "__main__":
    unittest.main()
