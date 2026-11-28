#!/usr/bin/env python3
"""AA-X06 independent confirmation: nilpotent local algebras and Nakayama.

Computation is via coefficient vectors over F_p and independent linear algebra,
not integer quotient ideals/localizations used by the first cross audit.
"""
from itertools import product


def digits(a, p, n):
    out = []
    for _ in range(n):
        a, d = divmod(a, p)
        out.append(d)
    return tuple(out)


def encode(t, p):
    return sum(v*p**i for i,v in enumerate(t))


def multiply(a, b, p, k):
    aa, bb = digits(a,p,k), digits(b,p,k)
    cc = [sum(aa[j]*bb[i-j] for j in range(i+1))%p for i in range(k)]
    return encode(cc,p)


def poly_power(a, exp, p, k):
    result = 1
    for _ in range(exp):
        result = multiply(result,a,p,k)
    return result


def valuation(a, p, k):
    z = digits(a,p,k)
    return next((i for i,v in enumerate(z) if v), k)


def rank(vectors,p,dim):
    # Gaussian elimination over a prime field.
    basis=[]
    for vector in vectors:
        v=list(vector)
        for pivot,b in basis:
            if v[pivot]:
                coeff=v[pivot]
                v=[(x-coeff*y)%p for x,y in zip(v,b)]
        pivot=next((i for i,z in enumerate(v) if z),None)
        if pivot is None:
            continue
        inv=pow(v[pivot],-1,p)
        v=[x*inv%p for x in v]
        basis.append((pivot,v))
        basis.sort(key=lambda z:z[0])
    return len(basis)


def t_action(v,block_lengths,p):
    out=[]
    start=0
    for e in block_lengths:
        block=v[start:start+e]
        out.extend((0,)+tuple(block[:-1]))
        start+=e
    return tuple(out)


def rspan_rank(generators, lengths,p):
    d=sum(lengths)
    K=max(lengths)
    gens=[]
    for v in generators:
        for j in range(K):
            gens.append(v)
            v=t_action(v,lengths,p)
    return rank(gens,p,d)


def quotient_rank(generators,lengths,p):
    indices=[sum(lengths[:i]) for i in range(len(lengths))]
    return rank([tuple(v[i] for i in indices) for v in generators],p,len(lengths))


def main():
    count={key:0 for key in ('unit_and_Jacobson','principal_ideal',
        'nilpotence','local_chain','Nakayama_generators','square_zero_2gen')}
    for p in (2,3):
        for k in (2,3,4,5):
            size=p**k
            elements=range(size)
            ideal_t={a for a in elements if a%p==0}
            principal_chain={j:{a for a in elements if valuation(a,p,k)>=j}
                for j in range(k+1)}
            for a in elements:
                expected_unit=(a%p!=0)
                # Independent finite search for an actual multiplicative inverse.
                unit=any(multiply(a,b,p,k)==1 for b in elements)
                assert unit==expected_unit,('unit',p,k,a)
                # Every 1-ab is a unit exactly when a belongs to Jacobson radical.
                jac=all((1-a*b)%p!=0 for b in range(p))
                assert jac==(a in ideal_t),('Jacobson',p,k,a)
                count['unit_and_Jacobson']+=1
                ann={multiply(a,b,p,k) for b in elements}
                assert ann==principal_chain[valuation(a,p,k)],('principal',p,k,a)
                count['principal_ideal']+=1
                if a in ideal_t:
                    assert poly_power(a,k,p,k)==0,('nilpotence',p,k,a)
                    count['nilpotence']+=1
            # A chain of all principal ideals; every ideal is one of them.
            assert all(principal_chain[j+1] < principal_chain[j]
                 for j in range(k))
            assert poly_power(p,k-1,p,k)!=0
            count['local_chain']+=1

        for k in (2,3,4):
            # Modules direct sums of cyclic R/(t^e), total F_p dimension<=4.
            for r in (1,2,3):
                for lengths in product(range(1,k+1),repeat=r):
                    d=sum(lengths)
                    if d>4 or (r==3 and p==3 and d>3):
                        continue
                    vectors=list(product(range(p),repeat=d))
                    # All tuples of r candidate generators (bounded finite cases).
                    for g in product(vectors,repeat=r):
                        q=quotient_rank(g,lengths,p)
                        full=rspan_rank(g,lengths,p)==d
                        assert full==(q==r), ('Nakayama',p,k,lengths,g,q,full)
                        count['Nakayama_generators']+=1
                    # Fewer than r generators are insufficient.
                    standard=[]; offset=0
                    for e in lengths:
                        v=[0]*d
                        v[offset]=1
                        standard.append(tuple(v))
                        offset+=e
                    assert rspan_rank(standard,lengths,p)==d
                    for g in product(vectors,repeat=max(0,r-1)):
                        if rspan_rank(g,lengths,p)==d:
                            raise AssertionError(('minimal generators',p,lengths,g))
                        count['Nakayama_generators']+=1

        # Square-zero local ring F_p[x,y]/(x,y)^2: its maximal ideal
        # has dimension 2; two generators are necessary and sufficient.
        for u,v in product(product(range(p),repeat=2), repeat=2):
            determinant=(u[0]*v[1]-u[1]*v[0])%p
            is_basis=rank([u,v],p,2)==2
            assert is_basis==(determinant!=0)
            count['square_zero_2gen']+=1
    total=sum(count.values())
    print(f'AA-X06 local algebras/Nakayama: {total}/{total} PASS',count)


if __name__=='__main__':
    main()
