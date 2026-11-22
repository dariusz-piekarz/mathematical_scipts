#!/usr/bin/env python3
"""Independent AA-37 audit II checks; finite tests do not prove infinite claims.

These tests use (i) coefficient-ring injectivity over finite fields,
(ii) invertible triangular substitutions, (iii) irreducible generic
quadratics over function fields, and (iv) exponents modulo p.
"""
import random
import re
import unittest
from pathlib import Path
import sympy as sp

CHAPTER = (Path(__file__).resolve().parents[2] / "chapters/pl/abstract_algebra/37-algebraiczna-niezaleznosc-i-bazy-transcendencji.tex")
SOURCE = CHAPTER.read_text(encoding="utf-8")

class IndependentStructure(unittest.TestCase):
    def test_labels_and_references(self):
        labels=re.findall(r"\\label\{([^}]+)\}",SOURCE)
        refs=re.findall(r"\\ref\{([^}]+)\}",SOURCE)
        self.assertEqual(len(labels),15)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertEqual(set(refs)-set(labels),{"aa:tw:fundamental-symmetric"})

    def test_balanced_environment_nesting(self):
        tok=re.compile(r"\\(begin|end)\{(definicja|lemat|twierdzenie|proof|przyklad|uwaga|enumerate)\}")
        stack=[]
        for m in tok.finditer(SOURCE):
            mode,tag=m.groups()
            if mode=="begin":stack.append(tag)
            else:
                self.assertTrue(stack)
                self.assertEqual(tag,stack.pop())
        self.assertFalse(stack)

    def test_all_core_theorems_present(self):
        for label in ["aa:lem:transcendence-maximal","aa:tw:transcendence-existence",
                      "aa:lem:transcendence-exchange","aa:lem:transcendence-irreducible-pure",
                      "aa:lem:transcendence-essential-variable","aa:tw:transcendence-degree",
                      "aa:tw:transcendence-tower","aa:prz:transcendence-infinite"]:
            self.assertIn(r"\label{"+label+"}",SOURCE)

    def test_source_preserves_choice_caveat(self):
        self.assertIn("Lemat Zorna",SOURCE)
        self.assertIn("aksjomatu wyboru",SOURCE)
        self.assertIn("C\\times\\mathbb N",SOURCE)

    def test_purely_inseparable_and_char2(self):
        for phrase in [r"[K(t):K(t^p)]=p",r"charakterystyce $2$",r"T^p-t^p=0"]:
            self.assertIn(phrase,SOURCE)


def make_invariants_case(p,n,seed):
    def test(self):
        xs=sp.symbols("x0:"+str(n))
        ts=sp.symbols("T0:"+str(n))
        e=[sum((sp.prod(c) for c in __import__('itertools').combinations(xs,k)),sp.Integer(0))
           for k in range(1,n+1)]
        rng=random.Random(10007*p+433*n+seed)
        P=sp.Integer(1)+sum(rng.randint(0,p-1)*ts[i]**(1+(seed+i)%2) for i in range(n))
        P+=sum(rng.randint(0,p-1)*ts[i]*ts[j] for i in range(n) for j in range(i+1,n))
        if sp.Poly(P,*ts,modulus=p).is_zero: P+=1
        F=sp.expand(P.subs(dict(zip(ts,e)),simultaneous=True))
        self.assertFalse(sp.Poly(F,*xs,modulus=p).is_zero,
                         'Nonzero polynomial in elementary symmetric functions must remain nonzero')
    return test


def make_triangular_case(p,n,seed):
    def test(self):
        vs=sp.symbols("z0:"+str(n))
        formal=sp.symbols("U0:"+str(n))
        rng=random.Random(27011*p+941*n+seed)
        shifts=[sp.Integer(0)]
        for i in range(1,n):
            shifts.append(sum(rng.randrange(p)*vs[j]**(1+(i+j+seed)%2) for j in range(i)))
        transformed=[vs[i]+shifts[i] for i in range(n)]
        # triangular map has determinant one, so no polynomial relation is created
        jac=sp.det(sp.Matrix([[sp.diff(formal_expr,v) for v in vs] for formal_expr in transformed]))
        self.assertEqual(jac,1)
        P=sum((i+seed+1)*formal[i]**2 for i in range(n))+formal[0]*formal[-1]+1
        Q=sp.expand(P.subs(dict(zip(formal,transformed)),simultaneous=True))
        self.assertFalse(sp.Poly(Q,*vs,modulus=p).is_zero)
    return test


def make_mod_p_exponents_case(p,seed):
    def test(self):
        rng=random.Random(1999*p+seed)
        t=sp.Symbol('t')
        vectors=[]
        for i in range(p):
            v=[rng.randrange(p) for _ in range(4)]
            vectors.append(v)
        vectors[seed%p][0]=1
        H=sp.expand(sum(a*t**(p*j+i) for i,v in enumerate(vectors) for j,a in enumerate(v)))
        self.assertFalse(sp.Poly(H,t,modulus=p).is_zero)
        # Each coefficient belongs to a unique residue class modulo p.
        result=sp.Poly(H,t,modulus=p)
        for (exp,),coeff in result.terms():
            self.assertEqual(int(coeff)%p,vectors[exp%p][exp//p]%p)
    return test


class ExplicitAlgebra(unittest.TestCase):
    def test_quadratic_generic_irreducible(self):
        T,S,P=sp.symbols('T S P')
        q=T*T-S*T+P
        self.assertTrue(sp.Poly(q,T,domain=sp.QQ.frac_field(S,P)).is_irreducible)
        self.assertEqual(sp.discriminant(q,T),S*S-4*P)

    def test_algebraic_extension_may_not_be_equal_field(self):
        u,v=sp.symbols('u v');S,P=sp.symbols('S P')
        # Over Q(S,P), u is algebraic of degree 2, not rational.
        Q=sp.Poly(u*u-S*u+P,u,domain=sp.QQ.frac_field(S,P))
        self.assertTrue(Q.is_irreducible)
        self.assertEqual(Q.degree(),2)

    def test_critical_intersection_identity_examples(self):
        u,v,w=sp.symbols('u v w');a=u*u+v*w; b=1+v+v*w
        r=sp.cancel(a/b)
        self.assertEqual(sp.together(r-a/b),0)
        # If a rational expression depends on w, a generic shift of w changes it.
        shifted=sp.cancel(r.subs({w:w+1})-r)
        self.assertNotEqual(shifted,0)
        self.assertEqual(sp.cancel(sp.simplify(shifted)-sp.factor(shifted)),0)

    def test_pure_transcendence_vs_transcendental_tower(self):
        u,v,S=sp.symbols('u v S')
        self.assertEqual(sp.expand((u+v)-v-u),0)
        self.assertEqual(sp.Poly(S-u-v,S).degree(),1)
        self.assertNotEqual(sp.Poly(u+v,u).LC(),0)

    def test_single_parameter_power_basis(self):
        t,T=sp.symbols('t T')
        for n in [2,3,4,5,7]:
            self.assertEqual(sp.Poly(T**n-t**n,T).degree(),n)
            self.assertEqual(sp.expand((t**n)**2-t**(2*n)),0)

    def test_infinite_basis_automorphism_inverse(self):
        z0,z1,z2,z3,z4=sp.symbols('z0 z1 z2 z3 z4')
        P=z0*z2*z4+z1*z3+z0**3+z3**2+1
        Q=sp.expand(P.subs({z0:z0+z1},simultaneous=True))
        R=sp.expand(Q.subs({z0:z0-z1},simultaneous=True))
        self.assertEqual(R,P)

    def test_exchange_quad_triangulation(self):
        u,v,z=sp.symbols('u v z')
        x=u+v*v
        self.assertEqual(sp.expand(x-v*v-u),0)
        self.assertEqual(sp.Poly(z-x+v*v,z).degree(),1)

    def test_transcendence_inequality_sample(self):
        # finite supports behave as a model for cardinality argument
        B={i for i in range(9)}
        C=range(5)
        supports=[{0,1},{2},{3,4},{5,6},{7,8}]
        self.assertEqual(B,set().union(*supports))
        self.assertEqual(len(B),sum(map(len,supports)))
        self.assertTrue(len(B)<=len(C)*2)

for pp in (2,3,5,7):
    for nn in (2,3,4):
        for seed in range(3):
            setattr(ExplicitAlgebra,f'test_e_symmetric_p{pp}_n{nn}_s{seed}',make_invariants_case(pp,nn,seed))
            setattr(ExplicitAlgebra,f'test_triangular_p{pp}_n{nn}_s{seed}',make_triangular_case(pp,nn,seed))
    for seed in range(4):
        setattr(ExplicitAlgebra,f'test_mod_p_classes_p{pp}_s{seed}',make_mod_p_exponents_case(pp,seed))

if __name__ == '__main__':
    unittest.main(verbosity=2)
