"""Finite algebraic regression models for CAT-24; not a substitute for proofs."""
import itertools
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/24-funktory-pochodne-ext-i-tor.tex"


class CategoryTheoryCh24(unittest.TestCase):
    def test_CAT_24_001_cyclic_ext_tor(self):
        for m, k in itertools.product(range(2, 41), repeat=2):
            g = math.gcd(m,k)
            image = {m*x % k for x in range(k)}
            kernel = {x for x in range(k) if m*x % k == 0}
            self.assertEqual(image, set(range(0,k,g)))
            self.assertEqual(kernel, set(range(0,k,k//g)))
            self.assertEqual(len(kernel),g)
            self.assertEqual(k//len(image),g)

    def test_CAT_24_002_connecting_map(self):
        # A concentrated in degree zero, C in degree one, B differential t.
        # H_1(B)=ker(t), H_0(B)=coker(t), connecting map is t.
        for k in range(2,21):
            for t in range(k):
                kernel = {x for x in range(k) if t*x % k == 0}
                image = {t*x % k for x in range(k)}
                g = math.gcd(t,k)
                quotient = {x % g for x in range(k)}
                self.assertEqual(kernel,set(range(0,k,k//g)))
                self.assertEqual(image,{x for x in range(k) if x % g == 0})
                self.assertEqual(len(quotient),g)
                for u in range(k):
                    # Naturality for multiplication by u on all three complexes.
                    for x in range(k):
                        self.assertEqual(t*(u*x % k)%k, u*(t*x % k)%k)

    def test_CAT_24_003_totalization_signs(self):
        # Two-term chain complexes over Z, maps a and b.
        # Tot_2 -> Tot_1 -> Tot_0. Signs must cancel also in odd characteristic.
        for a,b,x in itertools.product(range(-5,6),repeat=3):
            # Coordinates of Tot_1: (1,0),(0,1).
            y,z = -b*x,a*x
            self.assertEqual(a*y+b*z,0)
            # Transposition multiplies degree (1,1) by -1.
            self.assertEqual((-a*(-x),b*(-x)),(z,y))
            # Cohomological total: degree 0 -> 1 -> 2.
            y,z = a*x,b*x
            self.assertEqual(-b*y+a*z,0)

    def test_CAT_24_004_baer_sum_cyclic(self):
        # E_a = (Z/k x Z)/<(a,-m)>.
        # Normal form (n,y), 0<=y<m; reduce by y=m*q+r.
        for m,k in itertools.product(range(2,9),repeat=2):
            def normal(n,y,a):
                q,r = divmod(y,m)
                return ((n+a*q)%k,r)
            for a,b in itertools.product(range(k),repeat=2):
                for x,y in itertools.product(range(m),repeat=2):
                    left = normal(0,x+y,a)
                    right = normal(0,x+y,b)
                    summed = ((left[0]+right[0])%k,left[1])
                    self.assertEqual(summed,normal(0,x+y,(a+b)%k))
                self.assertEqual(normal(0,m,a),(a,0))
                for h in range(k):
                    ap=(a+m*h)%k
                    # [n,y]_a -> [n-h*y,y]_ap respects the relation.
                    self.assertEqual(normal(a+h*m,-m,ap),(0,0))

    def test_CAT_24_005_yoneda_dual_numbers(self):
        # R=F_l[e]/(e^2), residue field k. Periodic resolution by e.
        # All differentials in Hom_R(P,k) vanish; lift a cocycle by scalar.
        for l in (2,3,5,7):
            def prod(x,y):
                return (x[0]*y[0]%l,(x[0]*y[1]+x[1]*y[0])%l)
            eps=(0,1)
            elements=list(itertools.product(range(l),repeat=2))
            self.assertEqual({prod(eps,x) for x in elements},
                             {x for x in elements if prod(eps,x)==(0,0)})
            for a,b,c in itertools.product(range(l),repeat=3):
                for x in elements:
                    lift=(a,0)
                    self.assertEqual(prod(eps,prod(lift,x)),prod(lift,prod(eps,x)))
                self.assertEqual((c*(b*a%l))%l,((c*b%l)*a)%l)
                self.assertEqual((b*(a+c))%l,(b*a+b*c)%l)
            # Nonzero positive powers of the degree-one generator.
            self.assertEqual(prod((1,0),(1,0)),(1,0))

    def test_CAT_24_006_structure(self):
        c=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",c)
        self.assertEqual(len(labels),len(set(labels)))
        all_labels=[]
        for p in CHAPTER.parent.glob("*.tex"):
            all_labels.extend(re.findall(r"\\label\{([^}]+)\}",p.read_text(encoding="utf-8")))
        for label in re.findall(r"\\(?:ref|eqref)\{([^}]+)\}",c):
            self.assertEqual(all_labels.count(label),1,label)
        stack=[]
        for cmd,env in re.findall(r"\\(begin|end)\{([^}]+)\}",c):
            if cmd=="begin":
                stack.append(env)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)
        targets={
            "TOP-03":"algebraic_topology/03-algebra-homologiczna-moduly-kompleksy-i-ko-homologie.tex",
            "AA-18":"abstract_algebra/18-iloczyn-tensorowy-modulow-i-jego-wlasnosci.tex",
        }
        for code,label in re.findall(r"\\atlasref\{([^:}]+)::([^}]+)\}",c):
            t=(ROOT/"chapters/pl"/targets[code]).read_text(encoding="utf-8")
            self.assertEqual(t.count(r"\label{"+label+"}"),1,label)
        self.assertIn(CHAPTER.name,(ROOT/"books/pl/category_theory.tex").read_text(encoding="utf-8"))
        for label in ("cat:thm:abelian-homology-les","cat:thm:derived-les",
                      "cat:thm:ext-balanced","cat:thm:tor-balanced",
                      "cat:thm:ext-extensions","cat:prop:baer-sum",
                      "cat:thm:effaceable-universal","cat:thm:acyclic-resolution",
                      "cat:thm:yoneda-product"):
            self.assertIn(label,labels)
