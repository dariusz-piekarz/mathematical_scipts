#!/usr/bin/env python3
"""AA-42 second independent regression: actual standard matrices, projectors, class Fourier."""
from __future__ import annotations
from fractions import Fraction as Q
import itertools
import unittest

P=tuple(itertools.permutations(range(3)))
E=(0,1,2)
def mul(p,q):return tuple(p[q[i]] for i in range(3))
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
def inv(p):return tuple(p.index(i) for i in range(3))
def on_3(p,v):
    w=[0,0,0]
    for i,j in enumerate(p): w[j]=v[i]
    return tuple(w)
def mat_std(p):
    # basis a=(1,-1,0), b=(0,1,-1), coords x*a-z*b
    a=on_3(p,(1,-1,0))
    b=on_3(p,(0,1,-1))
    return ((a[0],b[0]),(-a[2],-b[2]))
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def tr(A):return sum(A[i][i] for i in range(len(A)))
def char(p):return (1,sign(p),tr(mat_std(p)))
def scalar(a,A):return tuple(tuple(a*x for x in row) for row in A)
def matrix_sum(*args):return tuple(tuple(sum(A[i][j] for A in args) for j in range(len(args[0][0]))) for i in range(len(args[0])))
def ident(n):return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def projection(k):
    dims=(1,1,2)
    return matrix_sum(*(scalar(Q(dims[k]*char(p)[k],6),tuple(tuple(int(p[j]==i) for j in range(3)) for i in range(3))) for p in P))

class TestExplicitStandardMatrices(unittest.TestCase):
    def test_trace_matches_fixed_points_minus_one(self):
        for p in P:self.assertEqual(char(p)[2],sum(p[i]==i for i in range(3))-1)

    def test_representation_law(self):
        for p,q in itertools.product(P,repeat=2):
            self.assertEqual(mm(mat_std(p),mat_std(q)),mat_std(mul(p,q)))

    def test_schur_averaging_in_nonorthonormal_basis(self):
        # (e1-e2,e2-e3) is NOT orthonormal. Average conjugates,
        # which has the basis-independent form tr(A)*I/d.
        for a,b in itertools.product(range(2),repeat=2):
            A=tuple(tuple(int(i==a and j==b) for j in range(2)) for i in range(2))
            terms=[mm(mm(mat_std(p),A),mat_std(inv(p))) for p in P]
            average=scalar(Q(1,6),matrix_sum(*terms))
            self.assertEqual(average,scalar(Q(int(a==b),2),ident(2)))

    def test_sign_standard_mixed_orthogonality(self):
        for a,b in itertools.product(range(2),repeat=2):
            self.assertEqual(sum(sign(p)*mat_std(p)[a][b] for p in P),0)
            self.assertEqual(sum(mat_std(p)[a][b] for p in P),0)

    def test_standard_irreducibility_via_trace(self):
        self.assertEqual(sum(tr(mat_std(p))**2 for p in P),6)

class TestActualIsotypicProjections(unittest.TestCase):
    def test_complete_decomposition_of_permutation_rep(self):
        X=[projection(k) for k in range(3)]
        self.assertEqual(matrix_sum(*X),ident(3))
        self.assertEqual(X[1],tuple(tuple(Q(0) for _ in range(3)) for _ in range(3)))
        self.assertEqual(X[0],tuple(tuple(Q(1,3) for _ in range(3)) for _ in range(3)))
        self.assertEqual(tuple(tr(A) for A in X),(1,0,2))

    def test_idempotents_and_commutation(self):
        X=[projection(k) for k in range(3)]
        for i,j in itertools.product(range(3),repeat=2):
            self.assertEqual(mm(X[i],X[j]),X[i] if i==j else scalar(0,ident(3)))
        for p in P:
            M=tuple(tuple(int(p[j]==i) for j in range(3)) for i in range(3))
            for A in X:self.assertEqual(mm(A,M),mm(M,A))

    def test_projection_on_sample_vectors(self):
        X=[projection(k) for k in range(3)]
        for v in itertools.product(range(-2,3),repeat=3):
            column=tuple((x,) for x in v)
            a=mm(X[0],column)
            b=mm(X[2],column)
            self.assertEqual(tuple(a[i][0]+b[i][0] for i in range(3)),v)
            self.assertEqual(a[0],a[1])
            self.assertEqual(a[1],a[2])
            self.assertEqual(sum(b[i][0] for i in range(3)),0)

class TestClassFunctionFourier(unittest.TestCase):
    def test_expansion_all_three_class_indicators(self):
        classes=[]
        for p in P:
            C=frozenset(mul(mul(q,p),inv(q)) for q in P)
            if C not in classes:classes.append(C)
        self.assertEqual(len(classes),3)
        for C in classes:
            f=lambda p:int(p in C)
            coeff=[sum(f(p)*char(p)[i] for p in P)/Q(6) for i in range(3)]
            for p in P:
                self.assertEqual(sum(coeff[i]*char(p)[i] for i in range(3)),f(p))

    def test_column_weights(self):
        classes=[]
        for p in P:
            C=frozenset(mul(mul(q,p),inv(q)) for q in P)
            if C not in classes:classes.append(C)
        for C,D in itertools.product(classes,repeat=2):
            p=next(iter(C));q=next(iter(D))
            avg=sum(char(p)[i]*char(q)[i] for i in range(3))
            self.assertEqual(avg,Q(6,len(C)) if C==D else 0)

if __name__=="__main__":
    unittest.main(verbosity=2)
