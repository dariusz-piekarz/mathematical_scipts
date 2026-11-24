"""AA-53: exact polynomial relations and independent basis ranks."""
import unittest
import sympy as s

class AA53PolynomialTests(unittest.TestCase):
    def test_cyclic_relation(self):
        x,y=s.symbols("x y")
        for m in range(1,10):
            self.assertEqual(s.expand(x**m*y**m-(x*y)**m),0)
    def test_dicyclic_generators(self):
        x,y=s.symbols("x y")
        for n in range(2,8):
            u=(x*y)**2
            v=x**(2*n)+y**(2*n)
            w=x*y*(x**(2*n)-y**(2*n))
            for f in (u,v,w):
                self.assertEqual(s.expand(f.subs({x:-y,y:x},simultaneous=True)-f),0)
                self.assertTrue(all((a-b)%(2*n)==0 for (a,b),c in s.Poly(f,x,y).terms()))
            self.assertEqual(s.expand(w*w-u*v*v+4*u**(n+1)),0)
    def test_dicyclic_basis_rank(self):
        x,y=s.symbols("x y")
        for n in range(2,6):
            u=(x*y)**2; v=x**(2*n)+y**(2*n); w=x*y*(x**(2*n)-y**(2*n))
            for d in range(25):
                polys=[s.Poly(u**i*v**j*w**e,x,y) for i in range(d//4+1)
                       for j in range(d//(2*n)+1) for e in (0,1)
                       if 4*i+2*n*j+(2*n+2)*e==d]
                if polys:
                    M=s.Matrix([[p.coeff_monomial(x**a*y**(d-a)) for p in polys] for a in range(d+1)])
                    self.assertEqual(M.rank(),len(polys))
if __name__=="__main__": unittest.main()
