from fractions import Fraction as F
import itertools
import unittest

def add(z,w): return (z[0]+w[0],z[1]+w[1])
def neg(z): return (-z[0],-z[1])
def mul(z,w):
    a,b=z; c,d=w
    return (a*c-b*d,a*d+b*c)
def conj(z): return (z[0],-z[1])
def norm2(z): return z[0]**2+z[1]**2
def inv(z): return tuple(F(x,norm2(z)) for x in conj(z))
def matrix(z): return ((z[0],-z[1]),(z[1],z[0]))
def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
Z=list(itertools.product(range(-2,3),repeat=2))

class Chapter05(unittest.TestCase):
    def test_field_laws(self):
        for z,w,u in itertools.product(Z,repeat=3):
            self.assertEqual(mul(mul(z,w),u),mul(z,mul(w,u)))
            self.assertEqual(mul(z,add(w,u)),add(mul(z,w),mul(z,u)))
        for z in Z:
            self.assertEqual(add(z,neg(z)),(0,0))
            self.assertEqual(mul(z,(1,0)),z)
            if z!=(0,0): self.assertEqual(mul(z,inv(z)),(1,0))

    def test_conjugation_and_modulus(self):
        for z,w in itertools.product(Z,repeat=2):
            self.assertEqual(conj(add(z,w)),add(conj(z),conj(w)))
            self.assertEqual(conj(mul(z,w)),mul(conj(z),conj(w)))
            self.assertEqual(conj(conj(z)),z)
            self.assertEqual(mul(z,conj(z)),(norm2(z),0))
            self.assertEqual(norm2(mul(z,w)),norm2(z)*norm2(w))
            dot=mul(z,conj(w))[0]
            self.assertLessEqual(dot**2,norm2(z)*norm2(w))
            self.assertEqual(norm2(add(z,w)),norm2(z)+2*dot+norm2(w))
            # Exact squared criterion for the triangle inequality.
            d=norm2(add(z,w))-norm2(z)-norm2(w)
            self.assertTrue(d<=0 or d*d<=4*norm2(z)*norm2(w))

    def test_triangle_equality(self):
        for z,w in itertools.product(Z,repeat=2):
            dot=mul(z,conj(w))[0]
            equal=dot>=0 and dot**2==norm2(z)*norm2(w)
            collinear=z[0]*w[1]==z[1]*w[0] and dot>0
            self.assertEqual(equal,z==(0,0) or w==(0,0) or collinear)

    def test_matrix_representation(self):
        for z,w in itertools.product(Z,repeat=2):
            A=matrix(z)
            AT=tuple(zip(*A))
            q=norm2(z)
            self.assertEqual(mm(AT,A),((q,0),(0,q)))
            self.assertEqual(mm(A,matrix(w)),matrix(mul(z,w)))
            self.assertEqual(A[0][0]*A[1][1]-A[0][1]*A[1][0],q)

    def test_square_root_formulas(self):
        for x,y in itertools.product(range(-5,6),repeat=2):
            u,v=mul((x,y),(x,y))
            r=x*x+y*y
            self.assertEqual(r*r,u*u+v*v)
            if v:
                X=abs(x); Y=F(v,2*X)
                self.assertGreater(r+u,0)
                self.assertEqual(X*X,F(r+u,2))
                self.assertEqual(Y*Y,F(r-u,2))
                self.assertEqual(mul((X,Y),(X,Y)),(u,v))
            elif u<0: self.assertEqual(mul((0,abs(y)),(0,abs(y))),(u,0))
            elif u>0: self.assertEqual(mul((abs(x),0),(abs(x),0)),(u,0))
            else: self.assertEqual((x,y),(0,0))

    def test_quadratic_completion(self):
        for A,B,C,z in itertools.product([(1,0),(0,1),(1,1),(-2,1)],repeat=4):
            delta=add(mul(B,B),neg(mul((4,0),mul(A,C))))
            left=add(mul(add(mul((2,0),mul(A,z)),B),add(mul((2,0),mul(A,z)),B)),neg(delta))
            right=mul((4,0),mul(A,add(add(mul(A,mul(z,z)),mul(B,z)),C)))
            self.assertEqual(left,right)

    def test_unit_circle(self):
        units=[(F(1),F(0)),(F(0),F(1)),(F(3,5),F(4,5)),(F(-5,13),F(12,13))]
        for z,w in itertools.product(units,repeat=2):
            self.assertEqual(norm2(mul(z,w)),1)
            self.assertEqual(inv(z),conj(z))
            self.assertEqual(mul(z,inv(z)),(1,0))

    def test_orientation_and_rotation_converse(self):
        units=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1)),
               (F(3,5),F(4,5)),(F(-5,13),F(12,13))]
        for first,second in itertools.product(units,repeat=2):
            a,b=first
            c,d=second
            if a*c+b*d!=0: continue
            det=a*d-b*c
            self.assertIn(det,(-1,1))
            A=((a,c),(b,d))
            self.assertEqual(A==matrix(first),det==1)
            self.assertEqual(mm(tuple(zip(*A)),A),((1,0),(0,1)))

    def test_worked_complex_examples(self):
        z,w=(2,3),(1,-2)
        self.assertEqual(add(z,w),(3,1))
        self.assertEqual(mul(z,w),(8,-1))
        self.assertEqual(mul(z,inv(w)),(F(-4,5),F(7,5)))
        for root,target in [((2,1),(3,4)),((0,3),(-9,0)),((1,-2),(-3,-4))]:
            self.assertEqual(mul(root,root),target)
            self.assertEqual(mul(neg(root),neg(root)),target)

if __name__=="__main__": unittest.main()
