from itertools import product
from collections import Counter
# CAT-01-001: heterogeneous sets including the empty set.
def rels(n,m):
    p=list(product(range(n),range(m)))
    return [frozenset(q for i,q in enumerate(p) if mask>>i&1) for mask in range(1<<len(p))]
def comp(s,r):
    return frozenset((a,c) for a,b in r for bb,c in s if b==bb)
counts=Counter()
for a,b,c,d in product(range(3),repeat=4):
    for r,s,t in product(rels(a,b),rels(b,c),rels(c,d)):
        assert comp(t,comp(s,r))==comp(comp(t,s),r)
        counts['rel_assoc']+=1
for a,b in product(range(3),repeat=2):
    for r in rels(a,b):
        assert comp(r,frozenset((i,i) for i in range(a)))==r
        assert comp(frozenset((i,i) for i in range(b)),r)==r
        counts['rel_identity']+=1
# CAT-01-003: underlying associativity for opposite arrows.
def funcs(n,m): return list(product(range(m),repeat=n))
def fc(g,f): return tuple(g[i] for i in f)
for a,b,c,d in product(range(3),repeat=4):
    for f,g,h in product(funcs(a,b),funcs(b,c),funcs(c,d)):
        assert fc(h,fc(g,f))==fc(fc(h,g),f)
        counts['op_assoc']+=1
# CAT-01-004: left regular module over M2(F2).
mats=list(product(range(2),repeat=4))
def mul(a,b): return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%2 for i in range(2) for j in range(2))
def add(a,b): return tuple(x^y for x,y in zip(a,b))
for a,b in product(mats,repeat=2):
    def h(x): return mul(mul(x,a),b)
    for x,y in product(mats,repeat=2):
        assert h(add(x,y))==add(h(x),h(y)); counts['module_add']+=1
    for r,x in product(mats,repeat=2):
        assert h(mul(r,x))==mul(r,h(x)); counts['module_scalar']+=1
print(dict(counts), 'total',sum(counts.values()))
