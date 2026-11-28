#!/usr/bin/env python3
"""Chapter 09 regression and independent finite-model tests.

Finite spaces test the structural countability consequences.  The
uncountable counterexamples and Sorgenfrey line are independently
reviewed mathematically; their infinite nature is not simulated.
"""
from pathlib import Path
import re

from test_general_topology_ch07 import all_topologies, product_topology

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'chapters/pl/general_topology/09-aksjomaty-przeliczalnosci.tex'
BOOK=ROOT/'books/pl/general_topology.tex'
STANDALONE=ROOT/'books/pl/general_topology_ch09.tex'


def minimum_neighborhoods(topology, n):
    """In finite spaces, U_x=intersection of all open neighborhoods x."""
    X=(1<<n)-1
    return tuple(_meet([u for u in topology if u&(1<<x)],X) for x in range(n))


def _meet(values, initial):
    z=initial
    for v in values: z &=v
    return z


def bases_and_density():
    counts={'spaces':0,'point_neighborhoods':0,'open_reconstructions':0,
            'density_checks':0,'heredity_checks':0}
    for n in range(5):
        X=(1<<n)-1
        for tau in all_topologies(n):
            counts['spaces']+=1
            m=minimum_neighborhoods(tau,n)
            # U_x open and contained in every open set containing x
            assert all(u in tau and u&(1<<x) for x,u in enumerate(m))
            for u in tau:
                reconstructed=0
                for x in range(n):
                    if u&(1<<x):
                        assert (m[x]&u)==m[x]
                        reconstructed |=m[x]
                assert reconstructed==u
                counts['open_reconstructions']+=1
            counts['point_neighborhoods']+=n
            # Every finite topology has a dense set: choose one point
            # from every nonempty open set, or simply use X.
            dense=[d for d in range(1<<n)
                   if all(u==0 or d&u for u in tau)]
            assert dense
            for d in range(1<<n):
                assert (d in dense)==all(u==0 or d&u for u in tau)
                counts['density_checks']+=1

            # The trace of the full base is a base for any subspace.
            for a in range(1<<n):
                trace={u&a for u in tau}
                assert 0 in trace and a in trace
                for u in trace:
                    assert (u&a)==u
                counts['heredity_checks']+=1
    assert counts['spaces']==390
    return counts


def product_base_checks():
    total=0
    for n in range(4):
        for m in range(3):
            for ta in all_topologies(n):
                for tb in all_topologies(m):
                    tau=product_topology(ta,tb,n,m)
                    min_a=minimum_neighborhoods(ta,n)
                    min_b=minimum_neighborhoods(tb,m)
                    min_prod=minimum_neighborhoods(tau,n*m)
                    for i in range(n):
                        for j in range(m):
                            box=0
                            for a in range(n):
                                for b in range(m):
                                    if min_a[i]&(1<<a) and min_b[j]&(1<<b):
                                        box |=1<<(a*m+b)
                            assert min_prod[i*m+j]==box,(n,m,i,j,ta,tb)
                            total+=1
    return total


def lower_limit_residual_checks():
    """Finite rational grids verify the disjoint-right-interval argument.

    For each finite cover with intervals [x,b), construct its union G of
    interiors.  Each uncovered left endpoint x has a right interval
    (x,q_x) in G; q_x is strictly increasing on residual points.
    """
    points=list(range(-8,9))
    cases=0
    for step in (1,2,3,4):
        for phase in range(1,25):
            intervals=[(x, x+step+((i+phase)%4)+1)
                       for i,x in enumerate(points)]
            # The family covers all listed left endpoints.
            assert all(any(a<=x<b for a,b in intervals) for x in points)
            residual=[x for x in points
                      if not any(a<x<b for a,b in intervals)]
            anchors=[]
            for x in residual:
                lengths=[b for a,b in intervals if a==x and b>x]
                assert lengths
                # q_x may be taken halfway from x to an eligible endpoint.
                q=x+(min(lengths)-x)/2
                anchors.append((x,q))
                assert all(not(x<y<q) for y in residual)
            for (_,q), (y,p) in zip(anchors,anchors[1:]):
                assert q<=y<p
            cases+=1
    return cases


def lint():
    src=SRC.read_text(encoding='utf8')
    full=BOOK.read_text(encoding='utf8')
    standalone=STANDALONE.read_text(encoding='utf8')
    assert src.startswith(r'\chapter{Aksjomaty przeliczalności i własności pokrewne}')
    assert r'\input{../../chapters/pl/general_topology/09-aksjomaty-przeliczalnosci.tex}' in full
    assert r'\setcounter{chapter}{8}' in standalone
    assert r'\input{../../chapters/pl/general_topology/09-aksjomaty-przeliczalnosci.tex}' in standalone
    assert 'quasi-składow' not in src.lower()
    # Keep the final counterexample together and do not repeat
    # the metric equivalence in the figure and in its caption.
    assert r'\begin{samepage}' in src and r'\end{samepage}' in src
    assert 'górny, środkowy dolny' not in src
    assert re.search(r'topologią\s+koskończoną',src)
    assert 'nie spełnia drugiego aksjomatu przeliczalności' in src
    for tag in (
        'def:topog-druga-przeliczalnosc','thm:topog-druga-pierwsza',
        'thm:topog-przeliczalnosc-dziedziczenie',
        'thm:topog-druga-iloczyn-przeliczalny',
        'def:topog-osrodkowosc','def:topog-lindelof',
        'thm:topog-druga-osrodkowa-lindelof',
        'thm:topog-osrodk-lindelof-zachowanie',
        'thm:topog-metryczne-trzy-warunki',
        'thm:topog-sorgenfrey-wlasnosci-przeliczalnosc',
        'ex:topog-sorgenfrey-iloczyn-nie-lindelof',
        'ex:topog-osrodkowosc-nie-dziedziczna',
        'ex:topog-lindelof-nie-dziedziczna',
        'fig:topog-przeliczalnosc-implikacje'
    ):
        assert '\\label{'+tag+'}' in src,tag
    for env in ('twierdzenie','lemat','stwierdzenie','wniosek',
                'definicja','przyklad','uwaga','proof','figure','tikzpicture'):
        assert src.count('\\begin{'+env+'}')==src.count('\\end{'+env+'}'),env
    texfiles=list((ROOT/'chapters/pl/general_topology').glob('*.tex'))
    labels=[];refs=[]
    for p in texfiles:
        t=p.read_text(encoding='utf8')
        labels+=re.findall(r'\\label\{([^}]+)\}',t)
        refs+=re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}',t)
    assert len(labels)==len(set(labels)),"Duplicate labels"
    assert set(refs)<=set(labels),f"Missing labels {set(refs)-set(labels)}"
    no_labels=re.sub(r'\\label\{[^}]+\}','',src)
    # Global terminology: no adjectival 'first/second countable' forms.
    for p in texfiles:
        prose=re.sub(r'\\(?:label|ref|eqref|pageref)\{[^}]+\}', '', p.read_text(encoding='utf8'))
        assert not re.search(r'\b(?:pierwszo\s+przeliczaln\w*|drugoprzeliczaln\w*|pierwsz\w*\s+przeliczalno\w*|drug\w*\s+przeliczalno\w*)',prose,re.I),p

    assert not re.search(r'\b(kofinita|unia|sekwencj\w*|tensorowanie)\b',no_labels,re.I)
    return len(labels),len(refs)


if __name__=='__main__':
    finite=bases_and_density()
    products=product_base_checks()
    lower=lower_limit_residual_checks()
    labels,refs=lint()
    print(f'PASS Chapter09: finite={finite}; product-local-neighborhoods={products}; '
          f'Sorgenfrey-rational-grid={lower}; labels={labels}, refs={refs}')
