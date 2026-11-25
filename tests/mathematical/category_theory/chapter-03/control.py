from itertools import product
from collections import Counter

counts = Counter()

def maps(n, m):
    return list(product(range(m), repeat=n))

def act(a, b, u):
    return tuple(b[u[i]] for i in a)

# CAT-03-001: mixed variance, unequal cardinalities and empty sets.
for p, q, r, s, t, v in product(range(3), repeat=6):
    for a, aa, b, bb, u in product(maps(q,p), maps(r,q), maps(s,t), maps(t,v), maps(p,s)):
        assert act(aa,bb,act(a,b,u)) == act(tuple(a[i] for i in aa),tuple(bb[i] for i in b),u)
        counts['hom'] += 1

# CAT-03-008: polynomial pullbacks of one-forms, calculated coefficientwise.
def add(p,q):
    return tuple((p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(max(len(p),len(q))))

def mul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            out[i+j]+=a*b
    return tuple(out)

def compose(p,q):
    out=(0,)
    for c in reversed(p):
        out=add(mul(out,q),(c,))
    return out

def diff(p):
    return tuple(i*p[i] for i in range(1,len(p))) or (0,)

def normalize(p):
    while len(p)>1 and p[-1]==0:
        p=p[:-1]
    return p

def pull(f,w):
    return normalize(mul(compose(w,f),diff(f)))

polys=list(product(range(-1,2),repeat=3))
for f,g,w in product(polys,repeat=3):
    assert pull(compose(g,f),w)==pull(f,pull(g,w))
    counts['pullback']+=1
for f,w in product(polys,repeat=2):
    assert normalize(diff(compose(w,f)))==pull(f,diff(w))
    counts['exterior_d']+=1
print(dict(counts))
print('Total:',sum(counts.values()))
