"""Independent AA-52 exact quaternion enumeration over real number fields."""
import unittest
import itertools
from collections import Counter,deque
import sympy as s

def enumerate_group(radical,gens,limit):
    K=s.QQ.algebraic_field(radical)
    one=(K.one,K.zero,K.zero,K.zero)
    gens=[tuple(K.from_sympy(s.sympify(a)) for a in q) for q in gens]
    def mul(q,r):
        a,b,c,d=q; e,f,g,h=r
        return (a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,
                a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e)
    G={one}; queue=deque([one])
    while queue:
        q=queue.popleft()
        for r in gens:
            p=mul(q,r)
            if p not in G:
                G.add(p); queue.append(p)
                if len(G)>limit: raise AssertionError("closure exceeds expected bound")
    hist=Counter()
    for q in G:
        assert sum((a*a for a in q),K.zero)==K.one
        p=one
        for n in range(1,limit+1):
            p=mul(p,q)
            if p==one:
                hist[n]+=1
                break
        else: raise AssertionError("order bound")
    return G,hist,mul,one

class AA52QuaternionTests(unittest.TestCase):
    def test_tetrahedral(self):
        h=s.Rational(1,2)
        G,H,_,_=enumerate_group(s.sqrt(2),[(0,1,0,0),(0,0,1,0),(h,h,h,h)],24)
        self.assertEqual(len(G),24)
        self.assertEqual(dict(H),{1:1,2:1,3:8,4:6,6:8})
    def test_octahedral(self):
        h=s.Rational(1,2); a=s.sqrt(2)/2
        G,H,_,_=enumerate_group(s.sqrt(2),[(h,h,h,h),(a,a,0,0)],48)
        self.assertEqual(len(G),48)
        self.assertEqual(dict(H),{1:1,2:1,3:8,4:18,6:8,8:12})
    def test_icosahedral(self):
        h=s.Rational(1,2); phi=(1+s.sqrt(5))/2
        # Lift of the order-five rotation R of AA-51:
        # scalar cos(pi/5)=phi/2, vector parallel to (0,1,phi).
        G,H,_,_=enumerate_group(s.sqrt(5),[(h,h,h,h),(0,1,0,0),
            (phi/2,0,(phi-1)/2,h)],120)
        self.assertEqual(len(G),120)
        self.assertEqual(dict(H),{1:1,2:1,3:20,4:30,5:24,6:20,10:24})
if __name__=="__main__": unittest.main()
