#!/usr/bin/env python3
"""Chapter 08: independent finite-topology checks of connectedness.

Finite spaces cannot validate the topologist's sine curve, the proof of
connectedness of R, or arbitrary infinite products: audit those by hand.
"""
from itertools import product
from pathlib import Path
import re
from test_general_topology_ch07 import all_topologies, product_topology

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'chapters/pl/general_topology/08-spojnosc.tex'
BOOK=ROOT/'books/pl/general_topology.tex'


def connected(tau, a):
    """No separation by relatively open sets of subspace a."""
    for u in tau:
        au=a&u
        if not au or au==a:
            continue
        for v in tau:
            av=a&v
            if av and not(au&av) and au|av==a:
                return False
    return True


def clopen_test(tau, a):
    """Independently test absence of nontrivial clopen subsets of a."""
    sub={u&a for u in tau}
    return not any(b!=0 and b!=a and (a^b) in sub for b in sub)


def closure(tau, a, universe):
    closed=[universe^u for u in tau]
    result=universe
    for f in closed:
        if a&f==a:
            result &= f
    return result


def components(tau,n):
    subsets=[a for a in range(1<<n) if connected(tau,a)]
    return [0 if not subsets else _union(a for a in subsets if a&(1<<x)) for x in range(n)]


def _union(it):
    out=0
    for x in it: out|=x
    return out


def finite_model_checks(topologies):
    checked=0; pairs=0; closures=0; components_count=0
    for n,topos in topologies.items():
        universe=(1<<n)-1
        for tau in topos:
            assert connected(tau,0)
            for a in range(1<<n):
                c=connected(tau,a)
                assert c==clopen_test(tau,a),(n,tau,a)
                if c:
                    b=closure(tau,a,universe)
                    assert connected(tau,b)
                    closures+=1
                checked+=1
            if connected(tau,universe):
                assert all(u==0 or u==universe or (universe^u) not in tau for u in tau)
            cs=components(tau,n)
            for x,c in enumerate(cs):
                assert c&(1<<x) and connected(tau,c)
                assert closure(tau,c,universe)==c
                assert all(not connected(tau,a) or not(a&(1<<x)) or (a&c)==a for a in range(1<<n))
                components_count+=1
                for y,d in enumerate(cs):
                    assert not(c&d) or c==d
            for a in range(1<<n):
                if not connected(tau,a): continue
                for b in range(1<<n):
                    if connected(tau,b) and (a&b):
                        assert connected(tau,a|b)
                        pairs+=1
    return checked,pairs,closures,components_count


def continuous(tau,sigma,f,n):
    return all(sum(1<<i for i in range(n) if s&(1<<f[i])) in tau for s in sigma)


def continuous_image_checks(topos):
    checks=0
    for n in range(4):
        for m in range(4):
            for tau in topos[n]:
                if not connected(tau,(1<<n)-1): continue
                for sigma in topos[m]:
                    for f in product(range(m),repeat=n):
                        if not continuous(tau,sigma,f,n): continue
                        image=_union(1<<y for y in f)
                        assert connected(sigma,image),(n,m,tau,sigma,f)
                        checks+=1
    return checks


def product_checks(topos):
    c=0
    for n in range(3):
        for m in range(3):
            for ta in topos[n]:
                for tb in topos[m]:
                    tau=product_topology(ta,tb,n,m)
                    if connected(ta,(1<<n)-1) and connected(tb,(1<<m)-1):
                        assert connected(tau,(1<<(n*m))-1),(n,m,ta,tb)
                    c+=1
    return c


def cantor_gap_checks():
    # Two ternary words of length m map to separated compact cylinders.
    cases=0
    for m in range(1,8):
        values=[]
        for digits in product((0,2),repeat=m):
            start=sum(d/3**(i+1) for i,d in enumerate(digits))
            values.append((start,start+3**(-m)))
        values.sort()
        for i in range(len(values)-1):
            assert values[i][1]<values[i+1][0]
            cases+=1
    return cases


def lint():
    src=SRC.read_text(encoding='utf-8')
    book=BOOK.read_text(encoding='utf-8')
    assert src.startswith(r'\chapter{Spójność i spójność drogowa}')
    assert r'\input{../../chapters/pl/general_topology/08-spojnosc.tex}' in book
    assert 'monotoniczna; wymagamy jedynie wskazanej ostatecznej' in (ROOT/'chapters/pl/general_topology/06-zbieznosc-topologiczna.tex').read_text()
    assert 'Droga a łuk' in src
    assert 'Dla ustalonego skończonego ciągu cyfr' in src
    assert r'Niech $n\ge1$ będzie liczbą całkowitą' in src
    assert 'Spójne obszary euklidesowe' not in src
    assert 'Dla ustalonej skończonego ciągu cyfr' not in src
    assert 'krzyw' in src.lower() and 'sin(1/x)' in src
    assert 'pierwszo przeliczalnych z rozdziału~06' in src
    assert 'z ciągłości funkcji' in src and r'$\overline G=T$' in src
    all_files=sorted((ROOT/'chapters/pl/general_topology').glob('*.tex'))
    labels=[];refs=[]
    for p in all_files:
        content=p.read_text(encoding='utf-8')
        labels+=re.findall(r'\\label\{([^}]+)\}',content)
        refs+=re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}',content)
    assert len(labels)==len(set(labels)), 'Duplicate labels'
    assert set(refs)<=set(labels),f'Missing references: {set(refs)-set(labels)}'
    for env in ('twierdzenie','lemat','stwierdzenie','wniosek','definicja','przyklad','uwaga','proof','figure'):
        assert src.count(r'\begin{'+env+'}')==src.count(r'\end{'+env+'}'),env
    assert not re.search(r'\b(kofinita|unia|sekwencj\w*|tensorowanie)\b',re.sub(r'\\label\{[^}]+\}','',src),re.I)
    required=('thm:topog-spojnosc-charakteryzacje','thm:topog-spojnosc-przedzialy','thm:topog-spojnosc-iloczyn','thm:topog-spojnosc-skladowe','thm:topog-spojnosc-droga-implikuje','ex:topog-spojnosc-sinus','thm:topog-spojnosc-lokalna-komponenty')
    assert all(l in labels for l in required)
    return len(labels),len(refs)


if __name__=='__main__':
    topo={n:list(all_topologies(n)) for n in range(5)}
    assert [len(topo[n]) for n in topo]==[1,1,4,29,355]
    c,p,z,k=finite_model_checks(topo)
    mappings=continuous_image_checks(topo)
    prods=product_checks(topo)
    cant=cantor_gap_checks()
    labels,refs=lint()
    print(f'PASS Chapter08: finite subsets={c}, unions={p}, closures={z}, components={k}; continuous images={mappings}, products={prods}, Cantor cylinders={cant}; labels={labels}, refs={refs}')
