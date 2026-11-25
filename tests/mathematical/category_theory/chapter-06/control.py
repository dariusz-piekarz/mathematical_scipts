from itertools import product, permutations
from collections import Counter

counts = Counter()

def maps(n, m):
    return list(product(range(m), repeat=n))

def topologies(n):
    subsets = range(1 << n)
    for mask in range(1 << (1 << n)):
        t = frozenset(s for s in subsets if mask >> s & 1)
        if 0 in t and (1 << n)-1 in t and all(a|b in t and a&b in t for a,b in product(t, repeat=2)):
            yield t

def pre(f, u):
    return sum(1 << i for i,x in enumerate(f) if u >> x & 1)

def continuous(f, t, s):
    return all(pre(f,u) in t for u in s)

# CAT-06-010: all topologies on sets of size 0, 1, 2.
spaces = [(n,t) for n in range(3) for t in topologies(n)]
for (a,ta),(b,tb),(n,tn) in product(spaces, repeat=3):
    pairs = list(product(range(a),range(b)))
    p,q = tuple(x for x,y in pairs),tuple(y for x,y in pairs)
    rectangles = {pre(p,u)&pre(q,v) for u,v in product(ta,tb)}
    tp = {0}
    for r in rectangles:
        tp |= {s|r for s in tp}
    tc = {u | (v << a) for u,v in product(ta,tb)}
    for f in maps(n,a*b):
        assert continuous(f,tn,tp) == (continuous(tuple(p[i] for i in f),tn,ta) and continuous(tuple(q[i] for i in f),tn,tb))
        counts['top_product'] += 1
    for f in maps(a+b,n):
        assert continuous(f,tc,tn) == (continuous(f[:a],ta,tn) and continuous(f[a:],tb,tn))
        counts['top_coproduct'] += 1

# CAT-06-009: evaluation of alternating C2*C2 words in S3.
G = list(permutations(range(3)))
e = (0,1,2)
def mul(a,b): return tuple(a[b[i]] for i in range(3))
def reduce_word(w):
    s=[]
    for x in w:
        if s and s[-1]==x: s.pop()
        else: s.append(x)
    return tuple(s)
def evaluate(w,a,b):
    out=e
    for x in w: out=mul(out,(a,b)[x])
    return out
involutions=[g for g in G if mul(g,g)==e]
words=[w for n in range(7) for w in product(range(2), repeat=n)]
for a,b,w in product(involutions,involutions,words):
    assert evaluate(w,a,b)==evaluate(reduce_word(w),a,b)
    counts['free_product_relations']+=1
for a,b in product(involutions,repeat=2):
    for u,v in product(words[:31],repeat=2):
        assert evaluate(reduce_word(u+v),a,b)==mul(evaluate(u,a,b),evaluate(v,a,b))
        counts['free_product_composition']+=1

# CAT-06-011: universal maps out of finite direct sums over Z/4.
for n in range(5):
    for coeff in product(range(4),repeat=n):
        for x in product(range(4),repeat=n):
            value=sum(a*b for a,b in zip(coeff,x))%4
            for r in range(4):
                assert sum(a*((r*b)%4) for a,b in zip(coeff,x))%4 == r*value%4
                counts['module_linearity']+=1
print(dict(counts))
print('Total:',sum(counts.values()))
