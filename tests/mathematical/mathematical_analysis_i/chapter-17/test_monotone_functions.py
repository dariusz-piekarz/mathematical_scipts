from fractions import Fraction as F
from unittest import TestCase, main

def step(x,c):
    return F(0) if x<0 else (c if x==0 else F(1))

def staircase(x,points,weights):
    return sum((w for p,w in zip(points,weights) if p<=x),F(0))

class Chapter17(TestCase):
    def test_square_monotone_intervals(self):
        for i in range(21):
            for j in range(i+1,21):
                x,y=F(i,7),F(j,7)
                self.assertEqual(y*y-x*x,(y-x)*(y+x))
                self.assertGreater(y*y,x*x)
                self.assertGreater((-y)**2,(-x)**2)

    def test_floor_order(self):
        pts=[F(i,7) for i in range(-30,31)]
        for x,y in zip(pts,pts[1:]):
            a,b=x//1,y//1
            self.assertTrue(a<=x<a+1)
            self.assertLessEqual(a,b)

    def test_finite_one_sided_witness(self):
        p=F(2,3)
        for n in range(1,50):
            x,y=p-F(1,n),p+F(1,n)
            self.assertLess(x,p)
            self.assertGreater(y,p)
            self.assertEqual(p-x,y-p)

    def test_step_parameter(self):
        pts=[F(-1),F(0),F(1)]
        for c in [F(0),F(1,3),F(1),F(-1),F(2)]:
            values=[step(x,c) for x in pts]
            self.assertEqual(values[2]-values[0],1)
            self.assertEqual(values==sorted(values),0<=c<=1)

    def test_disjoint_jump_intervals(self):
        points=[F(1,5),F(2,5),F(3,5),F(4,5)]
        weights=[F(1,3),F(2,3),F(1,7),F(2,7)]
        bounds=[]
        for p,w in zip(points,weights):
            lower=staircase(p-F(1,10),points,weights)
            upper=staircase(p+F(1,10),points,weights)
            self.assertEqual(upper-lower,w)
            bounds.append((lower,upper))
        for i in range(len(bounds)-1):
            self.assertLessEqual(bounds[i][1],bounds[i+1][0])
        for l,u in bounds:
            self.assertTrue(l<(l+u)/2<u)

    def test_large_jump_budget(self):
        jumps=[F(1,8),F(1,4),F(3,8),F(1,2)]
        total=sum(jumps)
        for eta in [F(1,16),F(1,8),F(1,4),F(1,2),F(1)]:
            count=sum(j>=eta for j in jumps)
            self.assertLessEqual(count*eta,total)

    def test_telescoping_jump_identity(self):
        bounds=[(F(1),F(2)),(F(3),F(5)),(F(6),F(9))]
        lhs=sum(u-l for l,u in bounds)
        rhs=bounds[-1][1]-bounds[0][0]-sum(bounds[i+1][0]-bounds[i][1] for i in range(len(bounds)-1))
        self.assertEqual(lhs,rhs)

    def test_dense_jumps_finite_witness(self):
        pts=[F(1,2),F(1,3),F(2,3),F(1,4),F(3,4)]
        weights=[F(1,2**(n+1)) for n in range(len(pts))]
        for p,w in zip(pts,weights):
            for n in range(1,20):
                x=p-p/(n+1)
                self.assertGreaterEqual(staircase(p,pts,weights)-staircase(x,pts,weights),w)
        self.assertEqual(sum(weights),1-F(1,2**len(pts)))

    def test_dense_jumps_tail(self):
        pts=[F(1,2),F(1,3),F(2,3),F(1,4),F(3,4)]
        p=F(1,5)
        for N in range(1,len(pts)):
            delta=min(abs(p-r) for r in pts[:N])
            x=p+delta/2
            weights=[F(1,2**(n+1)) for n in range(len(pts))]
            self.assertEqual(staircase(x,pts[:N],weights[:N]),staircase(p,pts[:N],weights[:N]))
            self.assertLessEqual(abs(staircase(x,pts,weights)-staircase(p,pts,weights)),F(1,2**N))

    def test_inverse_jump(self):
        f=lambda x:x if x<0 else x+1
        g=lambda u:u if u<0 else u-1
        pts=[F(i,8) for i in range(-20,21)]
        for x in pts:
            self.assertEqual(g(f(x)),x)
            self.assertTrue(f(x)<0 or f(x)>=1)
        for x,y in zip(pts,pts[1:]):
            self.assertLess(f(x),f(y))
        for eps in [F(1,10),F(1),F(2)]:
            for x in pts:
                u=f(x)
                if abs(u-1)<min(1,eps):
                    self.assertGreaterEqual(u,1)
                    self.assertLess(abs(g(u)),eps)

    def test_inverse_bracket_witness(self):
        f=lambda x:x if x<0 else x+1
        for p in [F(-1),F(0),F(1)]:
            for eps in [F(1,10),F(1),F(3)]:
                a,b=p-eps/2,p+eps/2
                d=min(1,f(p)-f(a),f(b)-f(p))
                self.assertGreater(d,0)
                for k in range(-20,21):
                    x=p+F(k,10)*eps
                    if abs(f(x)-f(p))<d:
                        self.assertTrue(a<x<b)
                        self.assertLess(abs(x-p),eps)

    def test_exact_jump_and_right_continuity(self):
        pts=[F(1,2),F(1,3),F(2,3),F(1,4),F(3,4)]
        weights=[F(1,2**(k+1)) for k in range(len(pts))]
        for k,p in enumerate(pts):
            delta=min([p,1-p]+[abs(p-q) for q in pts if q!=p])/2
            left=staircase(p-delta,pts,weights)
            at=staircase(p,pts,weights)
            right=staircase(p+delta,pts,weights)
            self.assertEqual(at-left,weights[k])
            self.assertEqual(right,at)
            others=[q for i,q in enumerate(pts) if i!=k]
            otherweights=[w for i,w in enumerate(weights) if i!=k]
            self.assertEqual(staircase(p-delta,others,otherweights),staircase(p+delta,others,otherweights))
        self.assertEqual(staircase(F(1),pts,weights)-staircase(F(0),pts,weights),sum(weights))

if __name__ == "__main__": main()
