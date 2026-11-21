"""Exhaustive finite checks of Chapter 03 assertions. Python standard library only."""
from __future__ import annotations
from itertools import product
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]
CP=ROOT/'chapters/pl/general_topology'
BOOK=ROOT/'books/pl/general_topology.tex'

def topologies(n):
    whole=(1<<n)-1
    candidates=[x for x in range(1<<n) if x not in (0,whole)]
    if n==0:
        return [frozenset({0})]
    result=[]
    for mask in range(1<<len(candidates)):
        opens={0,whole}
        opens.update(x for i,x in enumerate(candidates) if mask&(1<<i))
        if all((a|b) in opens and (a&b) in opens for a in opens for b in opens):
            result.append(frozenset(opens))
    return result

def trans(f,n,m):
    def pre(B):
        return sum((1<<x) for x,y in enumerate(f) if B&(1<<y))
    def fw(A):
        image=0
        for x,y in enumerate(f):
            if A&(1<<x):
                image|=(1<<y)
        return image
    return pre,fw

def ops(n,tau):
    W=(1<<n)-1
    clset={W^U for U in tau}
    interior={A:0 for A in range(1<<n)}
    closure={A:W for A in range(1<<n)}
    derived={}
    for A in range(1<<n):
        for U in tau:
            if U&~A == 0: interior[A]|=U
        for F in clset:
            if A&~F == 0: closure[A]&=F
        d=0
        for x in range(n):
            if all(U & (A & ~(1<<x)) for U in tau if U&(1<<x)):
                d |=1<<x
        derived[A]=d
    return clset,interior,closure,derived

def check_maps(topo):
    total=0; total_cont=0; total_homeo=0
    for n in range(4):
        for m in range(4):
            if n>0 and m==0: continue
            mapping=list(product(range(m),repeat=n)) if n>0 else [()]
            for tx in topo[n]:
                cx, ix, clx, dx=ops(n,tx)
                for ty in topo[m]:
                    cy, iy, cly, dy=ops(m,ty)
                    for f in mapping:
                        total+=1
                        pre, fw=trans(f,n,m)
                        allx=range(1<<n); ally=range(1<<m)
                        continuous=all(pre(V) in tx for V in ty)
                        from_closed=all(pre(F) in cx for F in cy)
                        from_closure=all(fw(clx[A]) & ~cly[fw(A)] == 0 for A in allx)
                        from_preclosure=all(clx[pre(B)] & ~pre(cly[B]) == 0 for B in ally)
                        from_local=all(any(U&(1<<x) and fw(U)&~V==0 for U in tx)
                            for x in range(n) for V in ty if V&(1<<f[x]))
                        # Taking the complete topology as a base or subbase.
                        basecriterion=all(pre(B) in tx for B in ty)
                        assert len({continuous,from_closed,from_closure,from_preclosure,from_local,basecriterion})==1, (n,m,tx,ty,f,'continuity')
                        if continuous:
                            total_cont+=1
                            assert all(pre(iy[B]) & ~ix[pre(B)]==0 for B in ally)
                        opened=all(fw(U) in ty for U in tx)
                        closedmap=all(fw(F) in cy for F in cx)
                        opencriterion=all(fw(ix[A]) & ~iy[fw(A)] == 0 for A in allx)
                        closedcriterion=all(cly[fw(A)] & ~fw(clx[A]) == 0 for A in allx)
                        assert opened==opencriterion
                        assert closedmap==closedcriterion
                        inj=len(set(f))==n
                        bij=inj and n==m
                        invcont=bij and all(fw(U) in ty for U in tx)
                        homeo=bool(bij and continuous and invcont)
                        assert homeo==bool(bij and continuous and opened)
                        assert homeo==bool(bij and continuous and closedmap)
                        image=fw((1<<n)-1)
                        subspace={V&image for V in ty}
                        embed=inj and continuous and all(fw(U) in subspace for U in tx)
                        direct_embed=inj and all(pre(V) in tx for V in ty) and all(fw(U) in subspace for U in tx)
                        assert embed==direct_embed
                        if homeo:
                            total_homeo+=1
                            for A in allx:
                                assert fw(ix[A])==iy[fw(A)]
                                assert fw(clx[A])==cly[fw(A)]
                                bdry_x=clx[A] & clx[((1<<n)-1)^A]
                                bdry_y=cly[fw(A)] & cly[((1<<m)-1)^fw(A)]
                                assert fw(bdry_x)==bdry_y
                                assert fw(dx[A])==dy[fw(A)]
                        # Open-cover and finite closed-cover gluing: exhaustive two-set covers.
                        if n<=2 and not continuous:
                            for U in tx:
                                for V in tx:
                                    if (U|V)==((1<<n)-1):
                                        on_u=all((pre(B)&U) in {T&U for T in tx} for B in ty)
                                        on_v=all((pre(B)&V) in {T&V for T in tx} for B in ty)
                                        assert not (on_u and on_v)
                            for F in cx:
                                for G in cx:
                                    if (F|G)==((1<<n)-1):
                                        on_f=all((pre(B)&F) in {T&F for T in tx} for B in ty)
                                        on_g=all((pre(B)&G) in {T&G for T in tx} for B in ty)
                                        assert not (on_f and on_g)
    return total,total_cont,total_homeo

def extra():
    X=range(0,4)
    # Sierpinski characteristic maps are continuous iff the characteristic set is open.
    target=frozenset({0,0b10,0b11})
    for n in X:
        for tx in topologies(n):
            for A in range(1<<n):
                f=tuple(int(bool(A&(1<<j))) for j in range(n))
                pre,_=trans(f,n,2)
                assert (all(pre(B) in tx for B in target))==(A in tx)
    # identity from discrete to indiscrete is continuous but not open/closed;
    # the opposite identity is open/closed but not continuous.
    disc=frozenset({0,1,2,3})
    anti=frozenset({0,3})
    f=(0,1)
    pre,fw=trans(f,2,2)
    assert all(pre(V) in disc for V in anti)
    assert not all(fw(U) in anti for U in disc)
    assert not all(pre(V) in anti for V in disc)
    assert all(fw(U) in disc for U in anti)

def lint():
    paths=sorted(CP.glob('*.tex'))
    book=BOOK.read_text(encoding='utf8')
    labels=[];refs=[]
    for p in paths:
        t=p.read_text(encoding='utf8')
        assert r'\input{../../chapters/pl/general_topology/'+p.name+'}' in book
        labels.extend(re.findall(r'\\label\{([^}]+)\}',t))
        refs.extend(re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}',t))
    assert len(labels)==len(set(labels)), 'duplicate labels'
    assert set(refs).issubset(set(labels)), set(refs)-set(labels)
    chapter=paths[-1].read_text(encoding='utf8')
    assert chapter.startswith(r'\chapter{Odwzorowania ciągłe}')
    assert not re.search(r'\b(kofinita|unia|tensorowanie)\b',chapter,re.I)
    assert r'\includegraphics' not in chapter
    return len(labels),len(refs)

if __name__=='__main__':
    topo={i:topologies(i) for i in range(4)}
    assert [len(topo[i]) for i in range(4)] == [1,1,4,29]
    count,cont,homeo=check_maps(topo)
    extra()
    labels,refs=lint()
    print(f'PASS Chapter03: maps={count}, continuous={cont}, homeomorphisms={homeo}; labels={labels}, refs={refs}; topology counts={[len(topo[i]) for i in range(4)]}')
