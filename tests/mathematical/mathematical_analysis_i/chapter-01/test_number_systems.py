import itertools
from fractions import Fraction
import unittest

def zeq(x,y): return x[0]+y[1]==x[1]+y[0]
def za(x,y): return (x[0]+y[0],x[1]+y[1])
def zm(x,y):
    a,b=x; c,d=y
    return (a*c+b*d,a*d+b*c)
def qe(x,y): return x[0]*y[1]==x[1]*y[0]
def qa(x,y):
    a,b=x; c,d=y
    return (a*d+b*c,b*d)
def qm(x,y): return (x[0]*y[0],x[1]*y[1])

class Chapter01(unittest.TestCase):
    def test_integer_representatives(self):
        for x,y in itertools.product(itertools.product(range(4),repeat=2),repeat=2):
            xx=(x[0]+2,x[1]+2); yy=(y[0]+3,y[1]+3)
            self.assertTrue(zeq(za(x,y),za(xx,yy)))
            self.assertTrue(zeq(zm(x,y),zm(xx,yy)))
            self.assertEqual(zm(x,y)[0]-zm(x,y)[1],(x[0]-x[1])*(y[0]-y[1]))
    def test_rational_representatives(self):
        pairs=list(itertools.product(range(-4,5),range(1,5)))
        for x,y in itertools.product(pairs,repeat=2):
            xx=(2*x[0],2*x[1]); yy=(3*y[0],3*y[1])
            self.assertTrue(qe(qa(x,y),qa(xx,yy)))
            self.assertTrue(qe(qm(x,y),qm(xx,yy)))
            self.assertEqual(Fraction(*qa(x,y)),Fraction(*x)+Fraction(*y))
            self.assertEqual(Fraction(*qm(x,y)),Fraction(*x)*Fraction(*y))
            self.assertEqual(x[0]*y[1]<=x[1]*y[0],Fraction(*x)<=Fraction(*y))
            if x[0]:
                inv=(x[1],x[0]) if x[0]>0 else (-x[1],-x[0])
                self.assertGreater(inv[1],0)
                self.assertTrue(qe(qm(x,inv),(1,1)))
if __name__=="__main__": unittest.main()
