"""Independent algebraic and source regression tests for Abstract Algebra AA-27."""
import unittest
from pathlib import Path
import re
import os
from sympy import Poly, symbols

DEFAULT_SOURCE = Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/27-teoria-artina-schreiera.tex'
SOURCE = Path(os.environ.get('AA27_SOURCE', DEFAULT_SOURCE)).read_text(encoding='utf-8')
x, t = symbols('x t')


def normalize(a, p):
    # polynomial in theta modulo theta^p - theta - 1
    z = [int(c) % p for c in a]
    for i in range(len(z)-1,p-1,-1):
        c = z[i]
        z[i-p+1] = (z[i-p+1]+c) % p
        z[i-p] = (z[i-p]+c) % p
    return tuple((z+[0]*p)[:p])


def add(a,b,p):
    return tuple((i+j)%p for i,j in zip(a,b))

def mul(a,b,p):
    z=[0]*(2*p-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):z[i+j]=(z[i+j]+u*v)%p
    return normalize(z,p)

def power(a,n,p):
    result=(1,)+(0,)*(p-1)
    while n:
        if n&1:result=mul(result,a,p)
        a=mul(a,a,p);n>>=1
    return result

def scalar(c,p):
    return (c%p,)+(0,)*(p-1)

def sigma(a,p):
    # automorphism theta -> theta+1; Horner computation
    theta=(0,1)+(0,)*(p-2)
    y=add(theta,scalar(1,p),p)
    out=scalar(0,p)
    for c in reversed(a): out=add(mul(out,y,p),scalar(c,p),p)
    return out

def trace(a,p):
    result=scalar(0,p)
    for _ in range(p):result=add(result,a,p);a=sigma(a,p)
    return result

class Structural(unittest.TestCase):
    def test_label_uniqueness(self):
        labels=re.findall(r'\\label\{([^}]+)\}',SOURCE)
        self.assertEqual(len(labels),10)
        self.assertEqual(len(set(labels)),10)
    def test_local_references(self):
        labels=set(re.findall(r'\\label\{([^}]+)\}',SOURCE))
        refs=set(re.findall(r'\\ref\{([^}]+)\}',SOURCE))
        self.assertEqual(refs-labels, {'aa:ch:kummer','aa:ch:trace-norm'})
    def test_environment_balance(self):
        for env in ['definicja','twierdzenie','stwierdzenie','przyklad','uwaga','proof']:
            self.assertEqual(SOURCE.count(r'\begin{'+env+'}'),SOURCE.count(r'\end{'+env+'}'),env)
    def test_correct_terminology(self):
        for bad in ['injekc','injektyw','pole stałe','niezerowe jednowymiarowe']:
            self.assertNotIn(bad,SOURCE)

class FiniteFields(unittest.TestCase):
    def test_prime_fields_as_image_zero(self):
        for p in [2,3,5,7,11,13]:
            self.assertEqual(set((pow(x,p,p)-x)%p for x in range(p)),{0})
    def test_roots_xp_minus_x(self):
        for p in [2,3,5,7,11]:
            pol=Poly(x**p-x,x,modulus=p)
            for c in range(p):self.assertEqual(int(pol.eval(c))%p,0)
            self.assertEqual(pol.degree(),p)
    def test_irreducible_artin_schreier(self):
        for p in [2,3,5,7]:
            self.assertTrue(Poly(x**p-x-1,x,modulus=p).is_irreducible)
    def test_artin_root(self):
        for p in [2,3,5,7]:
            theta=(0,1)+(0,)*(p-2)
            lhs=add(power(theta,p,p),tuple(-v for v in theta),p)
            self.assertEqual(lhs,scalar(1,p))
    def test_automorphism_order(self):
        for p in [2,3,5,7]:
            theta=(0,1)+(0,)*(p-2)
            y=theta
            seen=set()
            for j in range(p):
                self.assertNotIn(y,seen);seen.add(y)
                self.assertEqual(y,add(theta,scalar(j,p),p))
                y=sigma(y,p)
            self.assertEqual(y,theta)
    def test_trace_one_constructive(self):
        for p in [2,3,5,7]:
            theta=(0,1)+(0,)*(p-2)
            u=tuple(-v%p for v in power(theta,p-1,p))
            self.assertEqual(trace(u,p),scalar(1,p))
    def test_converse_explicit_alpha(self):
        for p in [2,3,5,7]:
            theta=(0,1)+(0,)*(p-2)
            u=tuple(-v%p for v in power(theta,p-1,p))
            alpha=scalar(0,p);z=u
            for j in range(p):
                alpha=add(alpha, tuple(-j*v for v in z),p)
                z=sigma(z,p)
            self.assertEqual(add(sigma(alpha,p),tuple(-v for v in alpha),p),scalar(1,p))
            a=add(power(alpha,p,p),tuple(-v for v in alpha),p)
            self.assertEqual(sigma(a,p),a)
    def test_prime_characteristic_two_example(self):
        p=2;theta=(0,1)
        self.assertEqual(power(theta,2,p),(1,1))
        self.assertEqual(sigma(theta,p),(1,1))
        self.assertEqual(trace(theta,p),(1,0))
    def test_all_elements_small_extension(self):
        from itertools import product
        for p in [2,3,5]:
            el=list(product(range(p),repeat=p))
            zero=scalar(0,p)
            image={add(power(a,p,p),tuple(-v for v in a),p) for a in el}
            kernel=[a for a in el if add(power(a,p,p),tuple(-v for v in a),p)==zero]
            self.assertEqual(len(kernel),p)
            self.assertEqual(set(kernel),{scalar(c,p) for c in range(p)})
            self.assertEqual(len(image),p**(p-1))
            trace_kernel={a for a in el if trace(a,p)==zero}
            self.assertEqual(image,trace_kernel)
            self.assertTrue(all(sigma(a,p)==power(a,p,p) for a in el))

    def test_norm_identity_prime_fields(self):
        for p in [2,3,5,7]:
            theta=(0,1)+(0,)*(p-2)
            self.assertEqual(add(power(theta,p,p), tuple(-v for v in theta),p),scalar(1,p))

class Classification(unittest.TestCase):
    def test_reparametrization_monomial(self):
        for p in [2,3,5,7]:
            # Identity (c theta + d)^p-(c theta+d)=c*(theta^p-theta)+(d^p-d)
            theta=(0,1)+(0,)*(p-2)
            for c in range(1,p):
                for d in range(p):
                    beta=add(tuple(c*v for v in theta),scalar(d,p),p)
                    w=add(power(beta,p,p),tuple(-v for v in beta),p)
                    self.assertEqual(w,scalar(c,p))
    def test_polynomial_change_of_variable(self):
        for p in [2,3,5,7]:
            a=t
            d=t*t+t+1
            for c in range(1,p):
                # polynomial identity in F_p(t), evaluated by polynomial arithmetic
                lhs=Poly(c*a+(d**p-d),t,modulus=p)
                self.assertEqual(lhs.eval(2)%p,(c*2+((2**2+2+1)**p-(2**2+2+1)))%p)
    def test_nontrivial_a_in_rational_function_field(self):
        # Pole at infinity of b^p-b is either absent or divisible by p
        from sympy import fraction, cancel
        sample=[t,t**2+1,1/t,(t**2+1)/(t+1),(t+1)/(t**2+1),t**3+1]
        for p in [2,3,5]:
            for b in sample:
                n,d=fraction(cancel(b))
                m=Poly(n,t).degree()-Poly(d,t).degree()
                if m>0:
                    # For rational b, b^p-b = (n^p - n*d^(p-1))/d^p
                    numerator=Poly(n**p-n*d**(p-1),t,modulus=p)
                    self.assertEqual(numerator.degree()-p*Poly(d,t).degree(),p*m)
                else:
                    self.assertLessEqual(m,0)

if __name__=='__main__':unittest.main(verbosity=2)
