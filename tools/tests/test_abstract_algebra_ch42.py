#!/usr/bin/env python3
"""AA-42: Schur, character rows/columns, multiplicities, regular and central idempotents."""
from __future__ import annotations
from fractions import Fraction as Q
import cmath
import itertools
import re
import unittest
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[2] / "chapters/pl/abstract_algebra/42-lemat-schura-charaktery-i-ortogonalnosc.tex"
S3 = tuple(itertools.permutations(range(3)))
E = (0, 1, 2)
def mul(p, q):
    return tuple(p[q[i]] for i in range(3))
def inv(p):
    return tuple(p.index(i) for i in range(3))
def sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))
def chars(p):
    return (1, sign(p), sum(p[i] == i for i in range(3)) - 1)
DIMS = (1, 1, 2)
def ip(f, g):
    return sum(f(p) * g(p) for p in S3) / Q(6)
def conv(a,b):
    return {p:sum((a[q]*b[mul(inv(q),p)] for q in S3),Q(0)) for p in S3}
def central_idempotent(i):
    return {p:Q(DIMS[i]*chars(p)[i],6) for p in S3}

class TestChapterStructure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src=SOURCE.read_text(encoding="utf-8")

    def test_all_labels_unique_and_cross_refs_resolve(self):
        labels=re.findall(r"\\label\{([^}]+)\}",self.src)
        refs=re.findall(r"\\ref\{([^}]+)\}",self.src)
        self.assertGreaterEqual(len(labels),20)
        self.assertEqual(len(labels),len(set(labels)))
        external={"aa:ch:representations"}
        self.assertEqual(set(refs)-set(labels),external)

    def test_balanced_environments(self):
        stack=[]
        for op,env in re.findall(r"\\(begin|end)\{([^}]+)\}",self.src):
            if op=="begin": stack.append(env)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),env)
        self.assertEqual(stack,[])

    def test_required_results(self):
        for label in ["aa:lem:schur-first","aa:tw:schur-complex",
                      "aa:tw:matrix-orthogonality","aa:cor:character-orthogonality",
                      "aa:tw:multiplicities","aa:tw:regular-character",
                      "aa:prop:isotypic-projector","aa:tw:characters-basis",
                      "aa:cor:column-orthogonality","aa:prz:character-s3"]:
            self.assertIn(r"\label{"+label+"}",self.src)

    def test_proofs_exist_and_examples_nonempty(self):
        self.assertGreaterEqual(self.src.count(r"\begin{proof}"),13)
        self.assertGreaterEqual(self.src.count(r"\begin{przyklad}"),3)
        self.assertIn(r"\mathbb F_2",self.src)
        self.assertIn(r"\mathbb C",self.src)

class TestS3CharacterIdentities(unittest.TestCase):
    def test_group_laws(self):
        for p in S3:
            self.assertEqual(mul(p, E),p)
            self.assertEqual(mul(E,p),p)
            self.assertEqual(mul(p,inv(p)),E)
            for q in S3:
                self.assertEqual(mul(inv(q),mul(q,p)),p)

    def test_class_function_and_sign(self):
        for p in S3:
            for q in S3:
                conj=mul(mul(q,p),inv(q))
                self.assertEqual(chars(conj),chars(p))
                self.assertEqual(sign(mul(q,p)),sign(q)*sign(p))

    def test_row_orthogonality(self):
        for i,j in itertools.product(range(3),repeat=2):
            self.assertEqual(ip(lambda p:chars(p)[i],lambda p:chars(p)[j]),int(i==j))

    def test_character_dimensions(self):
        self.assertEqual(chars(E),DIMS)
        self.assertEqual(sum(d*d for d in DIMS),len(S3))

    def test_regular_character(self):
        chi_reg=lambda p:6 if p==E else 0
        for i in range(3):
            self.assertEqual(ip(chi_reg,lambda p:chars(p)[i]),DIMS[i])
        for p in S3:
            self.assertEqual(chi_reg(p),sum(DIMS[i]*chars(p)[i] for i in range(3)))

    def test_three_conjugacy_classes(self):
        classes=[]
        for p in S3:
            C=frozenset(mul(mul(q,p),inv(q)) for q in S3)
            if C not in classes:classes.append(C)
        self.assertEqual(sorted(map(len,classes)),[1,2,3])

    def test_column_orthogonality(self):
        classes=[]
        for p in S3:
            C=frozenset(mul(mul(q,p),inv(q)) for q in S3)
            if C not in classes:classes.append(C)
        reps=[next(iter(C)) for C in classes]
        for i,j in itertools.product(range(3),repeat=2):
            lhs=sum(chars(reps[i])[k]*chars(reps[j])[k] for k in range(3))
            rhs=Q(6,len(classes[i])) if i==j else 0
            self.assertEqual(lhs,rhs)

    def test_central_idempotents_orthogonal(self):
        zero={p:Q(0) for p in S3}
        for i in range(3):
            for j in range(3):
                self.assertEqual(conv(central_idempotent(i),central_idempotent(j)),
                                 central_idempotent(i) if i==j else zero)

    def test_central_idempotents_sum_to_identity(self):
        for p in S3:
            self.assertEqual(sum(central_idempotent(i)[p] for i in range(3)),int(p==E))

    def test_centrality(self):
        for i in range(3):
            z=central_idempotent(i)
            for p,q in itertools.product(S3,repeat=2):
                self.assertEqual(z[mul(mul(q,p),inv(q))],z[p])

    def test_standard_permutation_character(self):
        for p in S3:
            fixed=sum(p[i]==i for i in range(3))
            self.assertEqual(fixed-1,chars(p)[2])

    def test_multiplicities_tensor_example(self):
        # (triv + sign + 2*std) has dimension 6 and is the regular module.
        chi=lambda p:chars(p)[0]+chars(p)[1]+2*chars(p)[2]
        for i in range(3):
            self.assertEqual(ip(chi,lambda p:chars(p)[i]),DIMS[i])

class TestCyclicCharacters(unittest.TestCase):
    def test_cyclic_fourier_orthogonality(self):
        for n in range(2,10):
            z=cmath.exp(2j*cmath.pi/n)
            for i,j in itertools.product(range(n),repeat=2):
                val=sum(z**((i-j)*k) for k in range(n))/n
                self.assertAlmostEqual(val.real,float(i==j),places=9)
                self.assertAlmostEqual(val.imag,0.,places=9)

    def test_cyclic_columns_orthogonal(self):
        for n in range(2,8):
            z=cmath.exp(2j*cmath.pi/n)
            for a,b in itertools.product(range(n),repeat=2):
                val=sum(z**(i*(a-b)) for i in range(n))
                self.assertAlmostEqual(val.real,float(n if a==b else 0),places=9)
                self.assertAlmostEqual(val.imag,0.,places=9)

class TestCharacteristicWarnings(unittest.TestCase):
    def test_r_c3_rotation_non_scalar_commutant(self):
        import math
        c=math.cos(2*math.pi/3);s=math.sin(2*math.pi/3)
        R=((c,-s),(s,c))
        J=((0.,-1.),(1.,0.))
        def mm(A,B):
            return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
        X,Y=mm(R,J),mm(J,R)
        for i,j in itertools.product(range(2),repeat=2):
            self.assertAlmostEqual(X[i][j],Y[i][j],places=12)
        self.assertNotEqual(J[0][1],0)
        self.assertLess((2*c)**2 - 4,0)

    def test_modular_trace_failure(self):
        p=2
        I=((1,0),(0,1))
        J=((1,1),(0,1))
        self.assertNotEqual(I,J)
        self.assertEqual((I[0][0]+I[1][1])%p,(J[0][0]+J[1][1])%p)
        self.assertEqual((J[0][0]*J[0][0]+J[0][1]*J[1][0])%p,1)
        self.assertEqual(J[0][1]*J[1][1]+J[0][0]*J[0][1],2)

if __name__=="__main__":
    unittest.main(verbosity=2)
