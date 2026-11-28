from itertools import product
from collections import Counter

counts = Counter()

# CAT-02-001: the group-epi witness on every proper subgroup of D_8.
G = list(product(range(4), range(2)))
identity = (0, 0)

def mul(a, b):
    return ((a[0] + (-1)**a[1]*b[0]) % 4, (a[1]+b[1]) % 2)

for mask in range(1, 1 << len(G)):
    K = {g for i, g in enumerate(G) if mask >> i & 1}
    if identity not in K or K == set(G) or any(mul(a,b) not in K for a,b in product(K,repeat=2)):
        continue
    counts['proper_subgroups'] += 1
    def tau(p):
        x,i = p
        return (x,1-i) if x in K else p
    def u(h,p):
        x,i = p
        return mul(h,x),i
    def v(h,p):
        return tau(u(h,tau(p)))
    X = list(product(G,range(2)))
    for a,b,p in product(G,G,X):
        assert v(mul(a,b),p) == v(a,v(b,p))
        counts['group_action'] += 1
    for k,p in product(K,X):
        assert u(k,p) == v(k,p)
        counts['agreement'] += 1
    for h in set(G)-K:
        assert u(h,(identity,0)) != v(h,(identity,0))
        counts['distinction'] += 1

# CAT-02-002/007: all composable finite-set maps, including empty sets.
def maps(n,m):
    return list(product(range(m),repeat=n))
def comp(g,f):
    return tuple(g[i] for i in f)
def inj(f):
    return len(set(f)) == len(f)
def surj(f,m):
    return set(f) == set(range(m))
for n,m,k in product(range(4),repeat=3):
    for f,g in product(maps(n,m),maps(m,k)):
        h = comp(g,f)
        assert not (inj(f) and inj(g)) or inj(h)
        assert not (surj(f,m) and surj(g,k)) or surj(h,k)
        assert not inj(h) or inj(f)
        assert not surj(h,k) or surj(g,k)
        counts['cancellation'] += 1
for n,m in product(range(4),repeat=2):
    for f in maps(n,m):
        for g in maps(m,n):
            left = comp(g,f) == tuple(range(n))
            right = comp(f,g) == tuple(range(m))
            assert not (inj(f) and right) or left
            assert not (surj(f,m) and left) or right
            counts['one_sided_inverse'] += 1
print(dict(counts))
print('Total cases (excluding subgroup count):',sum(v for k,v in counts.items() if k!='proper_subgroups'))
