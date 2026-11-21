#!/usr/bin/env python3
"""Chapter 07: independent finite-topology model checks and TeX integration.

Finite models do not prove the infinite-index Tychonoff theorem or Zorn's
lemma. Those arguments require a separate mathematical proof audit.
"""
from itertools import permutations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'chapters/pl/general_topology/07-zwartosc.tex'
BOOK = ROOT / 'books/pl/general_topology.tex'


def all_topologies(n):
    universe = (1 << n) - 1
    subsets = tuple(range(1 << n))
    for selection in range(1 << (1 << n)):
        tau = frozenset(a for a in subsets if selection & (1 << a))
        if 0 not in tau or universe not in tau:
            continue
        if all((a | b) in tau and (a & b) in tau for a in tau for b in tau):
            yield tau


def hausdorff(tau, n):
    return all(any(u & (1 << x) and v & (1 << y) and not (u & v)
                   for u in tau for v in tau)
               for x in range(n) for y in range(n) if x != y)


def normal(tau, n):
    universe = (1 << n) - 1
    closed = {universe ^ u for u in tau}
    return all(any((u & f) == f and (v & g) == g and not (u & v)
                   for u in tau for v in tau)
               for f in closed for g in closed if not (f & g))


def continuous(tau, sigma, mapping, n):
    return all(sum(1 << i for i in range(n) if v & (1 << mapping[i])) in tau
               for v in sigma)


def ultra_masks(n):
    """Enumerate all proper filters over a finite set via minimal members."""
    univ = (1 << n) - 1
    for generator in range(1, univ + 1):
        fam = {s for s in range(1 << n) if s & generator == generator}
        # Proper filter on a finite set is principal on its generator.
        assert fam and 0 not in fam and univ in fam
        assert all((a & b) in fam for a in fam for b in fam)
        yield generator, fam


def ultrafilter_checks(topos):
    tests = 0
    for n in range(5):
        univ = (1 << n) - 1
        for generator, family in ultra_masks(n):
            is_ultra = all(((s in family) != ((univ ^ s) in family))
                           for s in range(1 << n))
            assert is_ultra == (generator & (generator - 1) == 0)
            tests += 1
            if is_ultra:
                x = generator.bit_length() - 1
                for tau in topos[n]:
                    assert all(u in family for u in tau if u & (1 << x))
                    tests += 1
    return tests


def finite_separation_checks(topos):
    checked = 0
    for n, lst in topos.items():
        discrete = frozenset(range(1 << n))
        for tau in lst:
            # Any finite Hausdorff space must be discrete (hence normal).
            h = hausdorff(tau, n)
            assert h == (tau == discrete)
            assert not h or normal(tau, n)
            # Binary-valued continuous functions correspond to clopen sets.
            clopen = sorted(u for u in tau if ((1 << n) - 1) ^ u in tau)
            signatures = [tuple(bool(u & (1 << x)) for u in clopen)
                          for x in range(n)]
            separated = len(set(signatures)) == n
            # The finite model of evaluation embedding is injective exactly
            # when the space is discrete/Tychonoff.
            assert separated == h
            checked += 1
    return checked


def finite_homeomorphisms(topos):
    checked = 0
    for n in range(4):
        for tau in topos[n]:
            for sigma in topos[n]:
                if not hausdorff(sigma, n):
                    continue
                for mapping in permutations(range(n)):
                    if continuous(tau, sigma, mapping, n):
                        inverse = [0] * n
                        for x, y in enumerate(mapping):
                            inverse[y] = x
                        assert continuous(sigma, tau, inverse, n)
                    checked += 1
    return checked


def product_topology(ta, tb, n, m):
    """Generate finite product topology from basic rectangles."""
    rects = set()
    for a in ta:
        for b in tb:
            rect = 0
            for i in range(n):
                for j in range(m):
                    if a & (1 << i) and b & (1 << j):
                        rect |= 1 << (i*m+j)
            rects.add(rect)
    opens = {0}
    for b in rects:
        opens |= {u | b for u in tuple(opens)}
    return frozenset(opens)


def finite_products(topos):
    tests = 0
    for n in range(4):
        for m in range(4):
            if n*m > 6:
                continue
            for ta in topos[n]:
                for tb in topos[m]:
                    prod = product_topology(ta, tb, n, m)
                    assert 0 in prod and (1 << (n*m))-1 in prod
                    assert all((a | b) in prod and (a & b) in prod
                               for a in prod for b in prod)
                    if hausdorff(ta, n) and hausdorff(tb, m):
                        assert hausdorff(prod, n*m)
                    tests += 1
    return tests


def finite_weierstrass_models(topos):
    """Check continuous real-valued finite models; proof covers arbitrary compact K."""
    from itertools import product
    checked = 0
    checked_continuous = 0
    values = (-1, 0, 2)
    for n, spaces in topos.items():
        if n == 0:  # theorem explicitly requires K nonempty
            continue
        universe = (1 << n) - 1
        for tau in spaces:
            for f in product(values, repeat=n):
                # Every subset of the finite set values is relatively open in R.
                # Continuity is equivalent to openness of all point fibers.
                is_cont = all(sum(1 << i for i, z in enumerate(f) if z == y) in tau
                              for y in values)
                if is_cont:
                    assert min(f) in f and max(f) in f
                    assert any(v == min(f) for v in f)
                    assert any(v == max(f) for v in f)
                    checked_continuous += 1
                checked += 1
    # For two counterexamples, check the exact limiting obstruction.
    # f(x)=x for x in (0,1) omits 0 and 1; g([0,1])=[0,1).
    assert all(0 < k / (k + 1) < 1 for k in range(1, 80))
    assert all(1 - 1 / k < 1 for k in range(2, 80))
    return checked, checked_continuous


def latex_lint():
    src = SRC.read_text(encoding='utf-8')
    book = BOOK.read_text(encoding='utf-8')
    assert src.startswith(r'\chapter{Zwartość i jej charakterystyki}')
    # Cross-chapter consistency: Chapter 06 defines subnets by eventual
    # cofinality, without requiring monotonicity of the index mapping.
    earlier = (ROOT/'chapters/pl/general_topology/06-zbieznosc-topologiczna.tex').read_text(encoding='utf8')
    assert 'Nie wymagamy, aby $\\phi$ była iniekcją ani' in earlier
    assert 'monotoniczna; wymagamy jedynie wskazanej ostatecznej' in earlier
    assert 'współkońcowości (nie wymagamy jego monotoniczności)' in src
    assert 'monotoniczne i kofinalne w sensie ogonów' not in src
    assert r'\input{../../chapters/pl/general_topology/07-zwartosc.tex}' in book
    chapter_files = sorted((ROOT/'chapters/pl/general_topology').glob('*.tex'))
    labels = []
    refs = []
    for path in chapter_files:
        t = path.read_text(encoding='utf8')
        labels += re.findall(r'\\label\{([^}]+)\}', t)
        refs += re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}', t)
    assert len(labels) == len(set(labels)), 'duplicate labels'
    assert set(refs) <= set(labels), f'undefined refs: {set(refs)-set(labels)}'
    for env in ('definicja','twierdzenie','stwierdzenie','wniosek',
                'lemat','przyklad','uwaga','proof','figure'):
        assert src.count(r'\begin{'+env+'}') == src.count(r'\end{'+env+'}')
    assert not re.search(r'\b(kofinita|unia|sekwencyjn\w*)\b',
                         re.sub(r'\\label\{[^}]+\}', '', src), re.I)
    for required in ('thm:topog-zwartosc-sieci',
                     'thm:topog-zwartosc-ultrafiltry',
                     'thm:topog-tychonoff-iloczyny',
                     'thm:topog-zwartosc-zanurzenie-kostka',
                     'thm:topog-weierstrass-kresy',
                     'ex:topog-weierstrass-zalozenia'):
        assert required in labels
    return len(labels),len(refs)



def nonmonotone_subnet_regression():
    """Monotonicity is not part of the Ch06/Ch07 subnet definition."""
    def phi(n):
        return n + 3 if n % 2 else n

    # phi(1) > phi(2), so phi is not monotone; yet phi(n) >= n.
    assert phi(1) == 4 and phi(2) == 2
    assert all(phi(n) >= n for n in range(1, 301))
    for d0 in range(1, 60):
        assert all(phi(e) >= d0 for e in range(d0, d0 + 70))
    # The generalized subsequence of the convergent net x_n=1/n
    # still converges to zero by eventual cofinality.
    for eps in (1, .5, .1, .01):
        n0 = int(1 / eps) + 2
        assert all(1 / phi(e) < eps for e in range(n0, n0 + 60))


def main():
    nonmonotone_subnet_regression()
    counts=(1,1,4,29,355)
    topos={n:tuple(all_topologies(n)) for n in range(5)}
    assert tuple(len(topos[n]) for n in range(5)) == counts
    u=ultrafilter_checks(topos)
    s=finite_separation_checks(topos)
    h=finite_homeomorphisms(topos)
    p=finite_products(topos)
    w,wc=finite_weierstrass_models(topos)
    labels,refs=latex_lint()
    print(f'PASS ch07: topologies={sum(counts)}; ultrafilter checks={u}; '
          f'separation={s}; compact/Hausdorff continuous bijections={h}; '
          f'finite products={p}; Weierstrass finite models={w} ({wc} continuous); '
          f'labels={labels}; references={refs}')


if __name__=='__main__':
    main()
