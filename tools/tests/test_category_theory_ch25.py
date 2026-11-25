"""Finite matrix models and structural regressions for CAT-25, not formal proofs."""
import itertools
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/25-kategorie-triangulowane-i-pochodne.tex"


class CategoryTheoryCh25(unittest.TestCase):
    def test_CAT_25_001_cone_homotopy(self):
        # Two-term complexes with differential d in degrees 0 -> 1.
        # f = g + d h + h d, so f_0 = f_1 = g + dh.
        for d, g, h in itertools.product(range(-4, 5), repeat=3):
            f = g + d*h
            # Cone has degrees -1, 0, 1; check square zero.
            self.assertEqual(d*f-f*d, 0)
            # Upper triangular T: Cone(f) -> Cone(g), degree zero.
            for x, y in itertools.product(range(-3, 4), repeat=2):
                self.assertEqual(d*(y+h*x)+g*x, d*y+f*x)
                self.assertEqual((f*x-h*d*x, -d*x), (g*x, -d*x))
                self.assertEqual((y+h*x-h*x, x), (y,x))

    @staticmethod
    def _models():
        # Constant Z-graded complex: Z^4 with d(u,v)=(v,0), u,v in Z^2.
        # Chain maps act by the same 2x2 matrix on u,v. f and g need not commute.
        zero=(0,0,0,0)
        def add(x,y):
            return tuple(a+b for a,b in zip(x,y))
        def neg(x):
            return tuple(-a for a in x)
        def d(x):
            return (x[2],x[3],0,0)
        def action(m,x):
            a,b,c,e=m
            u,v,w,t=x
            return (a*u+b*v,c*u+e*v,a*w+b*t,c*w+e*t)
        for fm,gm in [((1,2,0,1),(1,0,3,1)),((0,-1,1,0),(2,1,0,-1)),
                      ((0,0,0,0),(1,0,0,1))]:
            f=lambda x: action(fm,x)
            g=lambda x: action(gm,x)
            yield zero,add,neg,d,f,g

    def test_CAT_25_002_rotations(self):
        for O,add,neg,d,f,g in self._models():
            def D(yxz):
                y,x,z=yxz
                return add(add(d(y),f(x)),z),neg(d(x)),neg(d(z))
            def r(v): return v[1]
            def s(x): return O,x,neg(f(x))
            def H(v): return O,O,v[0]
            def k(v): return v[0]
            def q(v): return v[2]
            def Dback(v):
                x,y,z=v
                return add(d(x),neg(z)),add(d(y),f(z)),neg(d(z))
            def rb(v): return add(f(v[0]),v[1])
            def sb(y): return O,y,O
            def Hb(v): return O,O,neg(v[0])
            def kb(v): return O,neg(v[0])
            def DC(v): return add(d(v[0]),f(v[1])),neg(d(v[1]))
            # Test every basis vector and one mixed vector; all maps are linear.
            basis=[tuple(int(i==j) for i in range(12)) for j in range(12)]
            basis.append(tuple(range(-6,6)))
            for vflat in basis:
                v=tuple(vflat[i:i+4] for i in range(0,12,4))
                self.assertEqual(D(D(v)),(O,O,O))
                self.assertEqual(r(D(v)),neg(d(r(v))))
                self.assertEqual(D(s(r(v))),s(neg(d(r(v)))))
                self.assertEqual(r(s(r(v))),r(v))
                self.assertEqual(tuple(add(x,y) for x,y in zip(D(H(v)),H(D(v)))),
                                 tuple(add(x,neg(y)) for x,y in zip(v,s(r(v)))))
                self.assertEqual(add(neg(d(k(v))),k(D(v))),add(q(v),f(r(v))))
                self.assertEqual(Dback(Dback(v)),(O,O,O))
                self.assertEqual(rb(Dback(v)),d(rb(v)))
                self.assertEqual(Dback(sb(rb(v))),sb(d(rb(v))))
                self.assertEqual(rb(sb(rb(v))),rb(v))
                self.assertEqual(tuple(add(x,y) for x,y in zip(Dback(Hb(v)),Hb(Dback(v)))),
                                 tuple(add(x,neg(y)) for x,y in zip(v,sb(rb(v)))))
                self.assertEqual(tuple(add(x,y) for x,y in zip(DC(kb(v)),kb(Dback(v)))),
                                 (add(v[1],neg(rb(v))),v[2]))

    def test_CAT_25_003_octahedron(self):
        for O,add,neg,d,f,g in self._models():
            def D(v):
                z,x,y,t=v
                return (add(add(d(z),g(f(x))),g(y)),add(neg(d(x)),t),
                        add(neg(d(y)),neg(f(t))),d(t))
            def DW(v): return add(d(v[0]),g(v[1])),neg(d(v[1]))
            def DU(v): return add(d(v[0]),f(v[1])),neg(d(v[1]))
            def r(v): return v[0],add(f(v[1]),v[2])
            def s(v): return v[0],O,v[1],O
            def H(v): return O,O,O,v[1]
            def k(v): return O,v[1]
            def gamma(v): return v[1],O
            def q(v): return v[2],v[3]
            basis=[tuple(int(i==j) for i in range(16)) for j in range(16)]
            basis.append(tuple(range(-8,8)))
            for flat in basis:
                v=tuple(flat[i:i+4] for i in range(0,16,4))
                self.assertEqual(D(D(v)),(O,O,O,O))
                self.assertEqual(r(D(v)),DW(r(v)))
                self.assertEqual(D(s(r(v))),s(DW(r(v))))
                self.assertEqual(r(s(r(v))),r(v))
                self.assertEqual(tuple(add(x,y) for x,y in zip(D(H(v)),H(D(v)))),
                                 tuple(add(x,neg(y)) for x,y in zip(v,s(r(v)))))
                self.assertEqual(tuple(add(neg(x),y) for x,y in zip(DU(k(v)),k(D(v)))),
                                 tuple(add(x,neg(y)) for x,y in zip(q(v),gamma(r(v)))))
                # beta alpha = d_W H0 + H0 d_U
                u=v[2],v[1]
                H0=lambda u: (O,u[0])
                self.assertEqual(tuple(add(x,y) for x,y in zip(DW(H0(u)),H0(DU(u)))),
                                 (g(u[0]),f(u[1])))

    def test_CAT_25_004_yoneda_sign_normalization(self):
        sign = lambda n: (-1)**(n % 2)
        for p,q in itertools.product(range(31), repeat=2):
            self.assertEqual(sign(p*(p-1)//2+q*(q-1)//2+p*q),
                             sign((p+q)*(p+q-1)//2))
            for j in range(1,q+1):
                self.assertEqual(sign(p+p*j), sign(p*(j-1)))
        for n in range(61):
            eps=1
            for p in range(1,n+1):
                prev=eps
                eps*=sign(n+p+1)
                self.assertEqual(prev*sign(n)+sign(p)*eps,0)
                self.assertEqual(sign(n+p-1)*prev,eps)
            self.assertEqual(eps,sign(n*(n+1)//2))
            self.assertEqual(eps*sign(n*(n-1)//2),sign(n))

    def test_CAT_25_006_fraction_localization(self):
        # One-object preadditive category: Z/12, S = elements invertible mod 3.
        # 4 in S is a zero divisor, so cancellation really requires refinement.
        R=range(12)
        S=[s for s in R if s%3]
        mul=lambda a,b: a*b%12
        value=lambda roof: roof[1]*pow(roof[0]%3,-1,3)%3
        roofs=list(itertools.product(S,R))
        def equivalent(x,y):
            s,f=x
            t,g=y
            return any(mul(s,a)==mul(t,b) and mul(f,a)==mul(g,b)
                       for a,b in itertools.product(S,repeat=2))
        for a,b in itertools.product(R,repeat=2):
            self.assertEqual(mul(a,b) in S,a in S and b in S)
        for t,f,g in itertools.product(S,R,R):
            if mul(t,f)==mul(t,g):
                self.assertTrue(any(mul(f,a)==mul(g,a) for a in S))
        for x,y in itertools.product(roofs,repeat=2):
            self.assertEqual(equivalent(x,y),value(x)==value(y))
            s,f=x
            t,g=y
            # Commutativity gives one Ore square; all other choices must agree.
            target=mul(s,t),mul(g,f)
            self.assertEqual(value(target),value(x)*value(y)%3)
            self.assertEqual(value((mul(s,t),(mul(f,t)+mul(g,s))%12)),
                             (value(x)+value(y))%3)
            for a,b in itertools.product(S,R):
                if mul(f,a)==mul(t,b):
                    self.assertEqual(value((mul(s,a),mul(g,b))),value(target))
        self.assertTrue(equivalent((1,3),(1,0)))
        self.assertNotEqual(3,0)

    def test_CAT_25_005_structure(self):
        text=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",text)
        self.assertEqual(len(labels),len(set(labels)))
        all_labels=[]
        for p in CHAPTER.parent.glob("*.tex"):
            all_labels.extend(re.findall(r"\\label\{([^}]+)\}",p.read_text(encoding="utf-8")))
        for ref in re.findall(r"\\(?:ref|eqref)\{([^}]+)\}",text):
            self.assertEqual(all_labels.count(ref),1,ref)
        stack=[]
        for kind,env in re.findall(r"\\(begin|end)\{([^}]+)\}",text):
            if kind=="begin":
                stack.append(env)
            else:
                self.assertTrue(stack,env)
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)
        top=ROOT/"chapters/pl/algebraic_topology/03-algebra-homologiczna-moduly-kompleksy-i-ko-homologie.tex"
        top_labels=re.findall(r"\\label\{([^}]+)\}",top.read_text(encoding="utf-8"))
        for script,label in re.findall(r"\\atlasref\{([^:}]+)::([^}]+)\}",text):
            self.assertEqual(script,"TOP-03")
            self.assertEqual(top_labels.count(label),1,label)
        book=(ROOT/"books/pl/category_theory.tex").read_text(encoding="utf-8")
        self.assertIn(CHAPTER.relative_to(ROOT).as_posix(),book)


if __name__ == "__main__":
    unittest.main()
