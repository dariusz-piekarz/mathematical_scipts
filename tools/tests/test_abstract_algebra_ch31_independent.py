"""Second independent AA-31 audit: constructive symmetric-polynomial algorithms.

Requires SymPy. All tests operate over Z/mZ, including rings with zero divisors.
No symbolic polynomial division by nonunits is used.
"""
from itertools import combinations, permutations
from pathlib import Path
from random import Random
import re
import unittest
from sympy import Poly, expand, prod, symbols, sympify

SRC = Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/31-wielomiany-symetryczne-i-wzory-viete.tex'
X = symbols('x1 x2 x3 x4')


def ek(xs, k):
    if k == 0:
        return 1
    return sum((prod(t) for t in combinations(xs, k)), 0)


def coefficients(expr, xs, m):
    """Return canonical coefficient table over Z/mZ, removing zeros."""
    return {mon: int(co) % m for mon, co in Poly(expand(expr), *xs).terms()
            if int(co) % m != 0}


def build_from_elementaries(P, ts, xs):
    return expand(sympify(P).subs(dict(zip(ts, (ek(xs, k) for k in range(1, len(xs)+1)))), simultaneous=True))


def reconstruct(expr, xs, m):
    """Greedy subtraction, returning the actual UNIQUE P, not just termination."""
    ts = symbols('t1:'+str(len(xs)+1))
    target = coefficients(expr, xs, m)
    P = 0
    limit = 400
    while target:
        a = max(target)
        c = target[a]
        assert all(a[i] >= a[i+1] for i in range(len(a)-1)), (a, target)
        b = tuple(a[j] - (a[j+1] if j+1 < len(a) else 0) for j in range(len(a)))
        Tmon = prod(t**k for t,k in zip(ts, b))
        P += c*Tmon
        emon = prod(ek(xs, k+1)**b[k] for k in range(len(xs)))
        correction = coefficients(c*emon, xs, m)
        out = dict(target)
        for mon, coeff in correction.items():
            nxt = (out.get(mon,0)-coeff) % m
            if nxt:
                out[mon] = nxt
            else:
                out.pop(mon, None)
        if out:
            assert max(out) < a, (a, max(out))
        target = out
        limit -= 1
        assert limit > 0
    return expand(P), ts


class IndependentSymmetricAudit(unittest.TestCase):
    def test_source_has_both_core_theorems(self):
        text = SRC.read_text()
        self.assertIn(r'\label{aa:tw:fundamental-symmetric}', text)
        self.assertIn(r'\label{aa:tw:vieta-general}', text)

    def test_label_references(self):
        s=SRC.read_text()
        labels=re.findall(r'\\label\{([^}]+)\}',s)
        refs=re.findall(r'\\(?:eqref|ref|pageref)\{([^}]+)\}',s)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertEqual(set(refs)-set(labels),set())

    def test_degrees_of_generators(self):
        for n in range(1,5):
            xs=X[:n]
            for k in range(1,n+1):
                self.assertEqual(Poly(ek(xs,k),*xs).total_degree(),k)

    def test_leading_coefficient_unity(self):
        for n in range(1,5):
            xs=X[:n]
            for k in range(1,n+1):
                p=Poly(ek(xs,k),*xs)
                lead=(1,)*k+(0,)*(n-k)
                self.assertEqual(max(p.monoms()),lead)
                self.assertEqual(p.coeff_monomial(lead),1)

    def test_permuted_generators(self):
        xs=X[:4]
        for k in range(1,5):
            e=ek(xs,k)
            for perm in permutations(xs):
                self.assertEqual(expand(e-e.xreplace(dict(zip(xs,perm)))),0)

    def test_symmetric_basis_reconstruction(self):
        xs=X[:3]
        x,y,z=xs
        f=sum(u*u*v for u in xs for v in xs if u!=v)
        P,ts=reconstruct(f,xs,6)
        self.assertFalse(coefficients(P-(ts[0]*ts[1]-3*ts[2]),ts,6))
        self.assertFalse(coefficients(f-build_from_elementaries(P,ts,xs),xs,6))

    def test_viete_repeated_roots_char2(self):
        t=symbols('t')
        roots=(1,1,0,0)
        f=Poly(prod(t-r for r in roots),t)
        for k in range(1,5):
            c=f.coeff_monomial(t**(4-k))
            a=ek(roots,k)
            self.assertEqual((int(c)-((-1)**k)*int(a))%2,0)

    def test_viete_repeated_roots_char3(self):
        t=symbols('t')
        roots=(0,1,1,2)
        f=Poly(prod(t-r for r in roots),t)
        for k in range(1,5):
            c=f.coeff_monomial(t**(4-k))
            self.assertEqual((int(c)-((-1)**k)*int(ek(roots,k)))%3,0)

    def test_cubic_power_sums(self):
        a,b,c=symbols('a b c')
        e1,e2,e3=ek((a,b,c),1),ek((a,b,c),2),ek((a,b,c),3)
        self.assertEqual(expand((a**3+b**3+c**3)-(e1**3-3*e1*e2+3*e3)),0)

    def test_no_division_or_fraction_field_assumption(self):
        s=SRC.read_text()
        self.assertIn('pierścieniem zerowym',s)
        self.assertIn('dzielnikami zera',s)
        self.assertNotIn('injektyw',s)


def make_modular_case(n,m):
    def check(self):
        rng=Random(n*1000+m)
        xs=X[:n]
        ts=symbols('t1:'+str(n+1))
        for _ in range(8):
            # A random polynomial of weighted degree up to 6, including zero-divisors.
            P=0
            for __ in range(8):
                exps=tuple(rng.randint(0,3) for j in range(n))
                if sum((j+1)*k for j,k in enumerate(exps))>6:
                    continue
                coefficient=rng.randrange(m)
                P+=coefficient*prod(t**k for t,k in zip(ts,exps))
            image=build_from_elementaries(P,ts,xs)
            result,returned_ts=reconstruct(image,xs,m)
            self.assertEqual(returned_ts,ts)
            self.assertEqual(coefficients(P-result,ts,m),{},(n,m,P,result))
            self.assertEqual(coefficients(image-build_from_elementaries(result,ts,xs),xs,m),{})
    return check

for n in (1,2,3):
    for m in (2,3,4,5,6,8):
        setattr(IndependentSymmetricAudit, f'test_full_inverse_mod_{m}_n_{n}',make_modular_case(n,m))

if __name__=='__main__':
    unittest.main(verbosity=2)
