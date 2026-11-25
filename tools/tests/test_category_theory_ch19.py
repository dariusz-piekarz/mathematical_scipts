"""CAT-19: monoidal coherence in finite concrete models."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/19-kategorie-monoidalne-symetryczne-i-domkniete.tex"


def alpha(x):
    (a,b),c = x
    return a,(b,c)


def inv_alpha(x):
    a,(b,c) = x
    return (a,b),c


def swap(x):
    a,b = x
    return b,a


def tensor(f,g):
    return lambda x: (f(x[0]),g(x[1]))


def identity(x):
    return x


class CategoryTheoryCh19(unittest.TestCase):
    def test_CAT_19_001_pentagon(self):
        for a,b,c,d in itertools.product(range(3), repeat=4):
            x = (((a,b),c),d)
            left = alpha(alpha(x))
            right = tensor(identity,alpha)(alpha(tensor(alpha,identity)(x)))
            self.assertEqual(left,right)
            self.assertEqual(left,(a,(b,(c,d))))

    def test_CAT_19_002_triangle(self):
        for a,b in itertools.product(range(3), repeat=2):
            x = ((a,()),b)
            left = tensor(identity,lambda y:y[1])(alpha(x))
            right = tensor(lambda y:y[0],identity)(x)
            self.assertEqual(left,right)
            self.assertEqual(left,(a,b))

    def test_CAT_19_003_hexagons(self):
        for a,b,c in itertools.product(range(3), repeat=3):
            x = ((a,b),c)
            self.assertEqual(alpha(swap(alpha(x))),
                             tensor(identity,swap)(alpha(tensor(swap,identity)(x))))
            y = (a,(b,c))
            self.assertEqual(inv_alpha(swap(inv_alpha(y))),
                             tensor(swap,identity)(inv_alpha(tensor(identity,swap)(y))))
            self.assertEqual(swap(swap((a,b))),(a,b))

    def test_CAT_19_004_graded_signs(self):
        for p,q,r in itertools.product(range(-4,5), repeat=3):
            sign = lambda n: -1 if n % 2 else 1
            self.assertEqual(sign(p*(q+r)), sign(p*q)*sign(p*r))
            self.assertEqual(sign((p+q)*r), sign(p*r)*sign(q*r))
            self.assertEqual(sign(p*q)*sign(q*p), 1)

    def test_CAT_19_005_currying_naturality(self):
        # Finite sets: naturality in source X and target B.
        funcs = list(itertools.product(range(2),repeat=2))
        for f in itertools.product(range(2),repeat=4):
            for u,v in itertools.product(funcs,repeat=2):
                composed = tuple(v[f[2*u[x]+a]] for x,a in itertools.product(range(2),repeat=2))
                curried = tuple(tuple(f[2*x+a] for a in range(2)) for x in range(2))
                self.assertEqual(composed,tuple(v[curried[u[x]][a]]
                                                for x,a in itertools.product(range(2),repeat=2)))

    def test_CAT_19_007_nonsymmetric_braiding(self):
        for prime in (3,5,7):
            for q in range(1,prime):
                for p,r,s in itertools.product(range(-3,4),repeat=3):
                    power = lambda n: pow(q,n,prime)
                    self.assertEqual(power(p*(r+s)),power(p*r)*power(p*s)%prime)
                    self.assertEqual(power((p+r)*s),power(p*s)*power(r*s)%prime)
                    self.assertEqual(power(p*r)*power(-p*r)%prime,1)
                self.assertEqual(all(pow(q,2*p*r,prime)==1
                                     for p,r in itertools.product(range(-3,4),repeat=2)),
                                 q*q%prime==1)

    def test_CAT_19_008_internal_hom_composition(self):
        funcs = tuple(itertools.product(range(2),repeat=2))
        def compose(g,f):
            return tuple(g[i] for i in f)
        def internal(a,b,f):
            return compose(b,compose(f,a))
        for a,aa,b,bb,f in itertools.product(funcs,repeat=5):
            self.assertEqual(internal(aa,bb,internal(a,b,f)),
                             internal(compose(a,aa),compose(bb,b),f))

    def test_CAT_19_006_structure(self):
        s = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for label in ("cat:def:monoidal","cat:eq:pentagon","cat:eq:triangle-monoidal",
                      "cat:def:braided-symmetric","cat:def:monoidal-closed"):
            self.assertIn(label,labels)
        stack = []
        for cmd,env in re.findall(r"\\(begin|end)\{([^}]+)\}",s):
            if cmd == "begin":
                stack.append(env)
            else:
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)
