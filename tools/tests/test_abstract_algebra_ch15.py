"""AA-15 regression tests: structural checks and independent finite models.

These finite computations do not replace mathematical proofs.
"""
import itertools
import re
import unittest
from pathlib import Path

SOURCE = (Path(__file__).resolve().parents[2] /
          "chapters/pl/abstract_algebra/15-pierscienie-nieprzemienne-i-algebry-grupowe.tex")
TEXT = SOURCE.read_text(encoding="utf-8")


def mm(a, b, p=2):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % p
                 for i in range(2) for j in range(2))


def cyc(a, b, p):
    n = len(a)
    return tuple(sum(a[k]*b[(i-k) % n] for k in range(n)) % p
                 for i in range(n))


def perm(a, b):
    return tuple(a[b[i]] for i in range(3))


class AA15Regression(unittest.TestCase):
    def test_01_labels_unique(self):
        labels = re.findall(r"\\label\{([^}]+)\}", TEXT)
        self.assertEqual(len(labels), 25)
        self.assertEqual(len(labels), len(set(labels)))

    def test_02_references_exist(self):
        labels = set(re.findall(r"\\label\{([^}]+)\}", TEXT))
        refs = set(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", TEXT))
        self.assertEqual(refs - labels, set())

    def test_03_proofs_and_examples(self):
        self.assertEqual(TEXT.count(r"\begin{proof}"), 11)
        self.assertEqual(TEXT.count(r"\end{proof}"), 11)
        self.assertEqual(TEXT.count(r"\begin{przyklad}"), 7)
        self.assertEqual(TEXT.count(r"\end{przyklad}"), 7)

    def test_04_environments_balanced(self):
        for name in ("definicja", "twierdzenie", "lemat", "stwierdzenie",
                     "wniosek", "przyklad"):
            self.assertEqual(TEXT.count(r"\begin{" + name + "}"),
                             TEXT.count(r"\end{" + name + "}"), name)

    def test_05_matrix_units_F2(self):
        z = (0,0,0,0)
        e = [tuple(int(i==r and j==c) for i in range(2) for j in range(2))
             for r in range(2) for c in range(2)]
        for i,j,k,l in itertools.product(range(2), repeat=4):
            self.assertEqual(mm(e[2*i+j],e[2*k+l]),
                             e[2*i+l] if j==k else z)

    def test_06_matrix_associativity_F2(self):
        ring = list(itertools.product(range(2), repeat=4))
        for a,b,c in itertools.product(ring, repeat=3):
            self.assertEqual(mm(mm(a,b),c),mm(a,mm(b,c)))

    def test_07_matrix_F2_center(self):
        ring = list(itertools.product(range(2),repeat=4))
        center = {a for a in ring if all(mm(a,b)==mm(b,a) for b in ring)}
        self.assertEqual(center,{(0,0,0,0),(1,0,0,1)})

    def test_08_matrix_Z4_center(self):
        ring = list(itertools.product(range(4),repeat=4))
        center = {a for a in ring if all(mm(a,b,4)==mm(b,a,4) for b in ring)}
        self.assertEqual(center,{(r,0,0,r) for r in range(4)})

    def test_09_matrix_nontrivial_left_ideal(self):
        ring = list(itertools.product(range(2),repeat=4))
        left = {a for a in ring if a[1]==a[3]==0}
        self.assertEqual(len(left),4)
        self.assertTrue(all(mm(a,b) in left for a in ring for b in left))
        self.assertFalse(all(mm(b,a) in left for a in ring for b in left))

    def test_10_matrix_nontrivial_right_ideal(self):
        ring = list(itertools.product(range(2),repeat=4))
        right = {a for a in ring if a[2]==a[3]==0}
        self.assertTrue(all(mm(b,a) in right for a in ring for b in right))
        self.assertFalse(all(mm(a,b) in right for a in ring for b in right))

    def test_11_matrix_F2_simple(self):
        ring = list(itertools.product(range(2),repeat=4))
        for a in ring[1:]:
            products = {mm(mm(x,a),y) for x in ring for y in ring}
            span = {(0,0,0,0)}
            for v in products:
                span.update(tuple(x^y for x,y in zip(w,v)) for w in tuple(span))
            self.assertEqual(len(span),16)

    def test_12_opposite_ring_associative(self):
        ring = list(itertools.product(range(2),repeat=4))
        op = lambda x,y: mm(y,x)
        self.assertTrue(all(op(op(a,b),c)==op(a,op(b,c))
                            for a,b,c in itertools.product(ring,repeat=3)))

    def test_13_cyclic_group_algebra_associative(self):
        p = 2
        ring = list(itertools.product(range(p),repeat=3))
        for a,b,c in itertools.product(ring,repeat=3):
            self.assertEqual(cyc(cyc(a,b,p),c,p),cyc(a,cyc(b,c,p),p))

    def test_14_cyclic_nilpotent_in_characteristic_p(self):
        for p in (2,3,5,7):
            u=(p-1,1)+(0,)*(p-2)
            ans=(1,)+(0,)*(p-1)
            for _ in range(p):
                ans=cyc(ans,u,p)
            self.assertEqual(ans,(0,)*p)

    def test_15_Z4_C2_universal_hom(self):
        # Generator maps to the order-two unit diag(1,-1).
        ev=lambda a: ((a[0]+a[1])%4,0,0,(a[0]-a[1])%4)
        ring=list(itertools.product(range(4),repeat=2))
        for a,b in itertools.product(ring,repeat=2):
            self.assertEqual(ev(cyc(a,b,4)),mm(ev(a),ev(b),4))

    def test_16_S3_noncommutative(self):
        a=(1,0,2); b=(0,2,1)
        self.assertNotEqual(perm(a,b),perm(b,a))

    def test_17_word_normal_forms(self):
        for n in range(9):
            for letters in itertools.product("xy",repeat=n):
                word="".join(letters)
                while "yx" in word:
                    before=sum(word[i]=="y" and word[j]=="x"
                               for i in range(len(word))
                               for j in range(i+1,len(word)))
                    word=word.replace("yx","xy",1)
                    after=sum(word[i]=="y" and word[j]=="x"
                              for i in range(len(word))
                              for j in range(i+1,len(word)))
                    self.assertEqual(after,before-1)
                self.assertEqual(word,"x"*letters.count("x")+"y"*letters.count("y"))

    def test_18_relation_not_true_in_matrix_ring(self):
        x=(0,1,0,0); y=(0,0,1,0)
        self.assertNotEqual(mm(x,y),mm(y,x))


if __name__ == "__main__":
    unittest.main()
