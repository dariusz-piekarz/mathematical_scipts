from itertools import product
from collections import Counter

counts = Counter()

def maps(n,m):
    return list(product(range(m),repeat=n))

# CAT-07-003: both implications for arbitrary commuting left squares,
# not just canonical iterated pullbacks. The right square is canonical.
for x,y,z,r,n in product(range(3),repeat=5):
    for u,v,w in product(maps(x,y),maps(y,z),maps(r,z)):
        Q=[(j,k) for j,k in product(range(y),range(r)) if v[j]==w[k]]
        L={(i,l) for i in range(x) for l,(j,k) in enumerate(Q) if u[i]==j}
        O={(i,k) for i,k in product(range(x),range(r)) if v[u[i]]==w[k]}
        for p,a in product(maps(n,x),maps(n,len(Q))):
            left=list(zip(p,a))
            if not set(left)<=L:
                continue
            outer=[(i,Q[l][1]) for i,l in left]
            is_left=len(left)==len(set(left)) and set(left)==L
            is_outer=len(outer)==len(set(outer)) and set(outer)==O
            assert is_left==is_outer
            counts['pasting_equivalence']+=1

# CAT-07-005: modules Z/m, including nonfields; universal maps
# from the pushout to Z/m and from Z/m to the pullback.
for m in range(2,6):
    pairs=list(product(range(m),repeat=2))
    for f,g in pairs:
        K={(a,b) for a,b in pairs if (f*a-g*b)%m==0}
        R={((t*f)%m,(-t*g)%m) for t in range(m)}
        for a,b in pairs:
            assert ((a,b) in K)==all(((f*a-g*b)*t)%m==0 for t in range(m))
            counts['module_pullback']+=1
        classes={frozenset(((a+x)%m,(b+y)%m) for x,y in R) for a,b in pairs}
        assert sum(map(len,classes))==m*m
        for u,v in pairs:
            constant=all(len({(u*a+v*b)%m for a,b in cls})==1 for cls in classes)
            assert constant==((u*f-v*g)%m==0)
            counts['module_pushout']+=1

# CAT-07-010: pullback of bijections has bijective opposite projection.
for a,b,c in product(range(4),repeat=3):
    for f,g in product(maps(a,c),maps(b,c)):
        if len(set(g))!=b or set(g)!=set(range(c)):
            continue
        P=[(i,j) for i,j in product(range(a),range(b)) if f[i]==g[j]]
        assert sorted(i for i,j in P)==list(range(a))
        counts['pullback_iso']+=1
print(dict(counts))
print('Total:',sum(counts.values()))
