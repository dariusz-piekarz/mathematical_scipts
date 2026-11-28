"""AA-58 independent exact trace identity for the tensor swap."""
import unittest
from itertools import product
def mul(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def tr(a):return sum(a[i][i] for i in range(len(a)))
def unit(n,i,j):return [[int(k==i and l==j) for l in range(n)] for k in range(n)]
def kron(a,b):
    return [[a[i][j]*b[k][l] for j in range(len(a)) for l in range(len(b))] for i in range(len(a)) for k in range(len(b))]
class TensorTraceTests(unittest.TestCase):
    def test_swap(self):
        for n in range(1,5):
            for i,j,k,l in product(range(n),repeat=4):
                a,b=unit(n,i,j),unit(n,k,l)
                c=kron(a,b)
                self.assertEqual(tr(c),tr(a)*tr(b))
                self.assertEqual(sum(c[(r%n)*n+r//n][r] for r in range(n*n)),tr(mul(a,b)))
if __name__=="__main__":unittest.main()
