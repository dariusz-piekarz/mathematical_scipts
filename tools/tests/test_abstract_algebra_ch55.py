"""AA-55: graph dimensions, symmetric powers and all finite SL2 families."""
import unittest

def arms_graph(lengths):
    edges=[]
    last=0
    for length in lengths:
        prev=0
        for _ in range(length):
            last+=1
            edges.append((prev,last))
            prev=last
    return last+1,edges,last

def d_graph(n):
    # n-1 vertices on the central chain; four leaves
    k=n-1
    return k+4,[(j,j+1) for j in range(k-1)]+[(0,k),(0,k+1),(k-1,k+2),(k-1,k+3)],k

def act(edges,v):
    result=[0]*len(v)
    for i,j in edges:
        result[i]+=v[j]
        result[j]+=v[i]
    return result

def dimensions(n,edges,root):
    # Exact positive solution via leaf-root propagation / rational elimination.
    import sympy as s
    a=s.zeros(n)
    for i,j in edges:
        a[i,j]+=1
        a[j,i]+=1
    basis=(2*s.eye(n)-a).nullspace()
    assert len(basis)==1
    return [x/basis[0][root] for x in basis[0]]

def multiplicities(n,edges,root,limit):
    a=[int(j==root) for j in range(n)]
    yield a
    b=act(edges,a)
    for _ in range(limit):
        yield b
        a,b=b,[u-v for u,v in zip(act(edges,b),a)]

def coeff(k,p,q,r):
    return sum((k-e*r-i*p)%q==0 for e in (0,1)
               for i in range(max(0,(k-e*r)//p+1)))

class McKayTests(unittest.TestCase):
    def check_graph(self,graph,order,ones,p,q,r):
        n,edges,root=graph
        d=dimensions(n,edges,root)
        self.assertTrue(all(x>0 and x.is_Integer for x in d))
        self.assertEqual(sum(x*x for x in d),order)
        self.assertEqual(d.count(1),ones)
        for k,v in enumerate(multiplicities(n,edges,root,120)):
            self.assertTrue(all(x>=0 for x in v))
            self.assertEqual(sum(x*y for x,y in zip(d,v)),k+1)
            self.assertEqual(v[root],coeff(k,p,q,r))
    def test_exceptional(self):
        for arms,order,ones,p,q,r in [
            ((2,2,2),24,3,6,8,12),((1,3,3),48,2,8,12,18),
            ((1,2,5),120,1,12,20,30)]:
            self.check_graph(arms_graph(arms),order,ones,p,q,r)
    def test_dicyclic(self):
        for n in range(2,13):
            self.check_graph(d_graph(n),4*n,4,4,2*n,2*n+2)
    def test_cyclic(self):
        for m in range(2,15):
            edges=[(j,(j+1)%m) for j in range(m)]
            for k,v in enumerate(multiplicities(m,edges,0,120)):
                self.assertEqual(v[0],sum((k-2*j)%m==0 for j in range(k+1)))
                self.assertEqual(sum(v),k+1)

if __name__=="__main__": unittest.main()
