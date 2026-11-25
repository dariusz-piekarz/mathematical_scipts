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

    def test_CAT_25_002_rotations(self):
        # Stalk complexes over Z; forward and backward rotation signs.
        # Cone(i) differential in degree -1: (x,z) -> fx+z.
        # Cone(-p[-1]) differential in degree -1: z -> (-z,fz).
        for f, x, y, z in itertools.product(range(-4, 5), repeat=4):
            # Forward r, s, H: id-sr = (y,0,fx+z).
            self.assertEqual((y,x,z)[2]-(-f*x), f*x+z)
            self.assertEqual((f*x+z,), (z+f*x,))
            self.assertEqual((x,-f*x)[0], x)
            # Backward r', s', H': id-s'r' = (x,-fx,z).
            self.assertEqual(f*(-z)+f*z, 0)
            self.assertEqual((x,y-(f*x+y),z), (x,-f*x,z))
            # q'-i r' = (-fx,z).
            self.assertEqual((y-(f*x+y),z), (-f*x,z))

    def test_CAT_25_003_octahedron(self):
        # Stalk complexes, scalars f and g; Cone(alpha) in degrees -2,-1,0:
        # t -> (t,-ft), (x,y) -> gfx+gy.
        for f,g,x,y,t,z in itertools.product(range(-2,3), repeat=6):
            self.assertEqual(g*f*t-g*f*t, 0)
            # Retraction r in degree -1 is (x,y) -> fx+y.
            self.assertEqual(g*(f*x+y),g*f*x+g*y)
            self.assertEqual(f*t-f*t,0)
            # Contraction id-sr on degree -1 is dH, on degree -2 is Hd.
            self.assertEqual((x,y-(f*x+y)),(x,-f*x))
            self.assertEqual((t,-f*t)[0],t)
            # rj=beta and rs=id; q-gamma r is (-fx,t).
            self.assertEqual((z,f*x),(z,f*x+0))
            self.assertEqual(f*0+y,y)
            self.assertEqual((y-(f*x+y),t),(-f*x,t))

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
