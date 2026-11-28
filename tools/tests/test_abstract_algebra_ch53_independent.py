"""AA-53: exact integer dimension counting from monomial action."""
import unittest

def cyclic_count(m,d):
    return sum((2*a-d)%m==0 for a in range(d+1))

def dicyclic_count(n,d):
    if d%2: return 0
    allowed={a for a in range(d+1) if (2*a-d)%(2*n)==0}
    return sum(a<d-a or (a==d-a and a%2==0) for a in allowed)

class AA53IntegerTests(unittest.TestCase):
    def test_cyclic_dimensions(self):
        for m in range(1,31):
            for d in range(101):
                expected=sum((1 if j==0 else 2) for j in range(d//m+1) if (d-m*j)%2==0)
                self.assertEqual(cyclic_count(m,d),expected)
    def test_dicyclic_dimensions(self):
        for n in range(2,31):
            for d in range(101):
                expected=sum(1 for e in (0,1) for j in range(d//(2*n)+1)
                             if d-(2*n+2)*e-2*n*j>=0 and (d-(2*n+2)*e-2*n*j)%4==0)
                self.assertEqual(dicyclic_count(n,d),expected)
    def test_minimum(self):
        for n in range(2,31):
            self.assertEqual([dicyclic_count(n,d) for d in range(5)],[1,0,0,0,2 if n==2 else 1])
if __name__=="__main__": unittest.main()
