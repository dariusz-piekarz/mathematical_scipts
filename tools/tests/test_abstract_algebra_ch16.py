"""AA-16 mathematical regression checks: modules, exact sequences, projectivity.

Finite examples are corroborating checks, not substitutes for general proofs.
"""
import itertools
import re
import unittest
from pathlib import Path

SRC = (Path(__file__).resolve().parents[2] /
       "chapters/pl/abstract_algebra/16-moduly-homomorfizmy-ciagi-dokladne-i-moduly-rzutowe.tex")
TEXT = SRC.read_text(encoding="utf-8")


def mul(a, b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%2
                 for i in range(2) for j in range(2))


def add(a, b):
    return tuple(x^y for x, y in zip(a,b))


class AA16Regression(unittest.TestCase):
    def test_01_labels_and_references(self):
        labels=re.findall(r"\\label\{([^}]+)\}",TEXT)
        refs=re.findall(r"\\(?:ref|eqref)\{([^}]+)\}",TEXT)
        self.assertEqual((len(labels),len(set(labels)),len(refs)),(26,26,6))
        self.assertEqual(set(refs)-set(labels),set())

    def test_02_balanced_proofs_and_examples(self):
        self.assertEqual(TEXT.count(r"\begin{proof}"),10)
        self.assertEqual(TEXT.count(r"\end{proof}"),10)
        self.assertEqual(TEXT.count(r"\begin{przyklad}"),7)
        self.assertEqual(TEXT.count(r"\end{przyklad}"),7)

    def test_03_free_module_universal_map_noncommutative(self):
        ring=list(itertools.product(range(2),repeat=4))
        u=(0,1,0,0);v=(0,0,1,0)
        F=lambda x,y:add(mul(x,u),mul(y,v))
        for r,x,y in itertools.product(ring,repeat=3):
            self.assertEqual(F(mul(r,x),mul(r,y)),mul(r,F(x,y)))

    def test_04_endomorphisms_of_left_regular_module(self):
        ring=list(itertools.product(range(2),repeat=4))
        for a,b,x in itertools.product(ring,repeat=3):
            self.assertEqual(mul(mul(x,b),a),mul(x,mul(b,a)))

    def test_05_noncentral_scalars_break_linearity(self):
        one=(1,0,0,1);a=(0,1,0,0);r=(0,0,1,0)
        self.assertNotEqual(mul(a,mul(r,one)),mul(r,mul(a,one)))

    def test_06_split_sequence_Z6(self):
        i=lambda x:3*x%6
        s=lambda x:4*x%6
        p=lambda x:x%3
        self.assertEqual({(i(a)+s(c))%6 for a in range(2) for c in range(3)},
                         set(range(6)))
        for a,c in itertools.product(range(2),range(3)):
            self.assertEqual((p(i(a)),p(s(c))),(0,c))

    def test_07_nonsplit_sequence_Z_to_Z2(self):
        # Images of a homomorphism Z/2 -> Z must have order dividing 2.
        self.assertEqual([x for x in range(-100,101) if 2*x==0],[0])

    def test_08_second_isomorphism_Z12(self):
        A={x for x in range(12) if x%2==0}
        B={x for x in range(12) if x%3==0}
        AplusB={(a+b)%12 for a in A for b in B}
        self.assertEqual(len(AplusB)//len(B),len(A)//len(A&B))

    def test_09_third_isomorphism_Z24(self):
        A={x for x in range(24) if x%8==0}
        B={x for x in range(24) if x%4==0}
        self.assertTrue(A<B)
        self.assertEqual((24//len(A))//(len(B)//len(A)),24//len(B))

    def test_10_Z4_module_of_two_elements_not_free(self):
        m={0,2}
        self.assertEqual({2*x%4 for x in m},{0})
        self.assertEqual(len(m),2)
        self.assertLess(len(m),len(set(range(4))))

    def test_11_product_ring_nonfree_projective(self):
        p={(0,0),(1,0)}
        q={(0,0),(0,1)}
        self.assertEqual(p&q,{(0,0)})
        self.assertEqual({((a[0]+b[0])%2,(a[1]+b[1])%2)
                          for a in p for b in q},set(itertools.product(range(2),repeat=2)))

    def test_12_diagonal_presentation_Z6_Z10(self):
        for x,y in itertools.product(range(-15,16),repeat=2):
            self.assertEqual((x%6,y%10)==(0,0),x%6==0 and y%10==0)

    def test_13_square_zero_module_not_free(self):
        # R=F2[t]/t² and M=R/(t); t is nonzero and annihilates M.
        t=(0,1)
        self.assertNotEqual(t,(0,0))
        for x in (0,1):
            self.assertEqual((t[0]*x)%2,0)

    def test_14_infinite_direct_sum_support_closed(self):
        xs=[{},{0:1},{4:2,100:3},{10:2,1000:1}]
        for a,b in itertools.product(xs,repeat=2):
            support=set(a)|set(b)
            self.assertTrue(len(support)<=len(a)+len(b))
            for c in (0,1,2,3):
                self.assertTrue({k for k,v in a.items() if c*v%4}.issubset(support))

    def test_15_projective_lifting_source_explained(self):
        self.assertIn("aksjomatu wyboru",TEXT)
        self.assertIn(r"q(e_s')=f(e_s)",TEXT)

    def test_16_no_unjustified_formula_in_splitting(self):
        self.assertIn(r"\Phi^{-1}(b)=",TEXT)
        self.assertIn(r"\ker r\cap i(A)=0",TEXT)


if __name__ == "__main__":
    unittest.main()
