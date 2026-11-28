#!/usr/bin/env python3
"""Finite-model tests of chapter 04: subspaces, products, sums and universal properties."""
from itertools import product
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
CH = ROOT / 'chapters/pl/general_topology/04-konstrukcje-przestrzeni-topologicznych.tex'
BOOK = ROOT / 'books/pl/general_topology.tex'


def powerset(elements):
    elements = tuple(elements)
    return tuple(frozenset(elements[i] for i in range(len(elements)) if mask >> i & 1)
                 for mask in range(1 << len(elements)))


def topology(tau, x):
    tau = frozenset(tau)
    assert all(u <= x for u in tau)
    return frozenset() in tau and x in tau and all(
        a | b in tau and a & b in tau for a in tau for b in tau)


def topologies(x):
    return tuple(frozenset(t) for t in powerset(powerset(x)) if topology(t, x))


def subspace(x, tau, a):
    return frozenset(a & u for u in tau)


def cl(x, tau, a):
    return frozenset.intersection(*(x-u for u in tau if a <= x-u))


def inte(x,tau,a):
    return frozenset().union(*(u for u in tau if u <= a))


def continuous(x, tx, y, ty, f):
    return all(frozenset(a for a in x if f[a] in v) in tx for v in ty)


def initial(x, maps):
    generators = frozenset(frozenset(a for a in x if f[a] in v)
                           for y, ty, f in maps for v in ty)
    inters = {x}
    for g in generators:
        inters.update({w & g for w in tuple(inters)})
    unions = {frozenset()}
    for b in inters:
        unions.update({u | b for u in tuple(unions)})
    assert topology(unions, x)
    return frozenset(unions)


def final(y, maps):
    ty = frozenset(v for v in powerset(y)
                   if all(frozenset(a for a in x if f[a] in v) in tx for x, tx, f in maps))
    assert topology(ty,y)
    return ty


def all_maps(x,y):
    for values in product(tuple(y), repeat=len(x)):
        yield dict(zip(sorted(x),values))


def product_topology(x,tx,y,ty):
    xy = frozenset(product(x,y))
    boxes = frozenset(frozenset(product(a,b)) for a in tx for b in ty)
    assert topology(frozenset(frozenset().union(*e) for e in powerset(boxes)),xy)
    return xy, frozenset(frozenset().union(*e) for e in powerset(boxes))


count = 0
for n in range(4):
    x = frozenset(range(n))
    all_tau = topologies(x)
    assert len(all_tau) == (1,1,4,29)[n]
    for tau in all_tau:
        for a in powerset(x):
            sa = subspace(x,tau,a)
            assert topology(sa,a)
            for b in powerset(a):
                assert cl(a,sa,b) == a & cl(x,tau,b)
                assert inte(a,sa,b) == a - cl(x,tau,a-b)
                assert (cl(a,sa,b) - inte(a,sa,b)) == a & cl(x,tau,b) & cl(x,tau,a-b)
                assert (b in sa) == any(b == a&u for u in tau)
                assert (a-b in sa) == any(b == a & (x-u) for u in tau)
                count += 1
            for b in powerset(a):
                sb = subspace(a,sa,b)
                assert sb == subspace(x,tau,b)
print('PASS subspaces: relative topology, closure, interior, boundary, and inheritance',count)

count = 0
# All spaces up to 2 points, including empty spaces and every possible function.
for nx in range(3):
    x = frozenset(range(nx))
    for ny in range(3):
        y = frozenset(range(ny))
        for tx in topologies(x):
            for ty in topologies(y):
                xy, txy = product_topology(x,tx,y,ty)
                for a in powerset(x):
                    for b in powerset(y):
                        assert cl(xy,txy,frozenset(product(a,b))) == frozenset(
                            product(cl(x,tx,a),cl(y,ty,b)))
                        count += 1
                for u in txy:
                    assert frozenset(a for a,b in u) in tx
                    assert frozenset(b for a,b in u) in ty
                for nz in range(3):
                    z = frozenset(range(nz))
                    for tz in topologies(z):
                        # test all maps z -> x*y
                        for f in all_maps(z,xy):
                            p1 = {a:p[0] for a,p in f.items()}
                            p2 = {a:p[1] for a,p in f.items()}
                            assert continuous(z,tz,xy,txy,f) == (
                                continuous(z,tz,x,tx,p1) and continuous(z,tz,y,ty,p2))
print('PASS binary products: basic neighborhoods, projections, closure, universal property',count)

count = 0
for nx in range(3):
    x = frozenset(range(nx))
    for ny in range(3):
        y = frozenset(range(ny))
        for tx in topologies(x):
            for ty in topologies(y):
                s = frozenset({(0,a) for a in x}|{(1,b) for b in y})
                ts = frozenset(w for w in powerset(s)
                               if frozenset(a for _,a in w if _ == 0) in tx
                               and frozenset(a for _,a in w if _ == 1) in ty)
                assert topology(ts,s)
                assert frozenset({(0,a) for a in x}) in ts
                assert frozenset({(1,b) for b in y}) in ts
                for nz in range(3):
                    z = frozenset(range(nz))
                    for tz in topologies(z):
                        for f in all_maps(s,z):
                            f0={a:f[(0,a)] for a in x}
                            f1={a:f[(1,a)] for a in y}
                            assert continuous(s,ts,z,tz,f) == (
                                continuous(x,tx,z,tz,f0) and continuous(y,ty,z,tz,f1))
                            count += 1
print('PASS disjoint sums: components clopen and universal property',count)

count = 0
for nx in range(3):
    x = frozenset(range(nx))
    for ny in range(3):
        y = frozenset(range(ny))
        for tx in topologies(x):
            for ty in topologies(y):
                for f in all_maps(x,y):
                    ti = initial(x,[(y,ty,f)])
                    tf = final(y,[(x,tx,f)])
                    assert continuous(x,ti,y,ty,f)
                    assert continuous(x,tx,y,tf,f)
                    for u in ti:
                        assert u in ti
                    for v in tf:
                        assert frozenset(a for a in x if f[a] in v) in tx
                    for tz in topologies(x):
                        if continuous(x,tz,y,ty,f):
                            assert ti <= tz
                    for tz in topologies(y):
                        if continuous(x,tx,y,tz,f):
                            assert tz <= tf
                    for nz in range(3):
                        z=frozenset(range(nz))
                        for tz in topologies(z):
                            for g in all_maps(z,x):
                                fg={a:f[g[a]] for a in z}
                                assert continuous(z,tz,x,ti,g) == continuous(z,tz,y,ty,fg)
                            for h in all_maps(y,z):
                                hf={a:h[f[a]] for a in x}
                                assert continuous(y,tf,z,tz,h) == continuous(x,tx,z,tz,hf)
                    count += 1
print('PASS initial and final topologies: extremal conditions and both universal properties',count)

count = 0
for nx in range(4):
    x=frozenset(range(nx))
    for ny in range(nx+1):
        y=frozenset(range(ny))
        for f in all_maps(x,y):
            if frozenset(f.values()) != y: continue
            for tx in topologies(x):
                ty=final(y,[(x,tx,f)])
                for a in powerset(x):
                    sat=frozenset(p for p in x if f[p] in frozenset(f[v] for v in a))
                    im=frozenset(f[v] for v in a)
                    assert (im in ty) == (sat in tx)
                    assert (y-im in ty) == (x-sat in tx)
                    if sat==a:
                        assert (im in ty)==(a in tx)
                count += 1
print('PASS quotient spaces, saturation, and open/closed images',count)

count = 0
for nx in range(3):
    x=frozenset(range(nx))
    assert initial(x,[]) == frozenset({frozenset(),x})
    assert final(x,[]) == frozenset(powerset(x))
    for ny in range(3):
        y=frozenset(range(ny))
        for nz in range(3):
            z=frozenset(range(nz))
            for ty in topologies(y):
                for tz in topologies(z):
                    for f in all_maps(x,y):
                        for g in all_maps(x,z):
                            ti=initial(x,[(y,ty,f),(z,tz,g)])
                            for tx in topologies(x):
                                if continuous(x,tx,y,ty,f) and continuous(x,tx,z,tz,g):
                                    assert ti<=tx
                            count+=1
print('PASS initial topology: empty and two-arrow families',count)

count = 0
for ny in range(3):
    y=frozenset(range(ny))
    for nx in range(3):
        x=frozenset(range(nx))
        for nz in range(3):
            z=frozenset(range(nz))
            for tx in topologies(x):
                for tz in topologies(z):
                    for f in all_maps(x,y):
                        for g in all_maps(z,y):
                            ta=final(y,[(x,tx,f)])
                            tb=final(y,[(z,tz,g)])
                            tc=final(y,[(x,tx,f),(z,tz,g)])
                            assert tc == ta & tb
                            count+=1
print('PASS final topology: empty and two-arrow families',count)

src=CH.read_text(encoding='utf-8')
book=BOOK.read_text(encoding='utf-8')
labels=re.findall(r'\\label\{([^}]+)\}', src)
refs=re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}', src)
assert len(labels)==len(set(labels))
all_src='\n'.join(p.read_text(encoding='utf-8') for p in
                  sorted((ROOT/'chapters/pl/general_topology').glob('*.tex')))
all_labels=set(re.findall(r'\\label\{([^}]+)\}',all_src))
assert set(refs)<=all_labels,set(refs)-all_labels
assert r'\input{../../chapters/pl/general_topology/04-konstrukcje-przestrzeni-topologicznych.tex}' in book
for env in ('twierdzenie','stwierdzenie','definicja','przyklad','uwaga','proof','figure'):
    assert src.count(r'\begin{'+env+'}')==src.count(r'\end{'+env+'}')
assert not re.search(r'\b(kofinita|unia|sekwencyjn[ayie])\b',re.sub(r'\\label\{[^}]+\}','',src),re.I)
print(f'PASS LaTeX: {len(labels)} distinct labels; {len(refs)} resolved references, environments and terminology')
