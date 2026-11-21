"""Finite exhaustive regression for Chapter 02. No external dependencies."""
from __future__ import annotations
from itertools import combinations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
BOOK = ROOT / 'books/pl/general_topology.tex'
CHAPTERS = sorted((ROOT / 'chapters/pl/general_topology').glob('*.tex'))


def powerset(n: int) -> range:
    return range(1 << n)


def enumerate_topologies(n: int):
    X = (1 << n) - 1
    subsets = list(powerset(n))
    candidate = [s for s in subsets if s not in (0, X)]
    # For the empty space, 0 = X and there is just one topology.
    if X == 0:
        yield frozenset({0})
        return
    for bits in range(1 << len(candidate)):
        opens = {0, X}
        opens.update(s for i, s in enumerate(candidate) if bits & (1 << i))
        if all((a | b) in opens and (a & b) in opens for a in opens for b in opens):
            yield frozenset(opens)


def check_topology(n: int, tau: frozenset[int]):
    X = (1 << n) - 1
    subsets = list(powerset(n))
    closed = {X ^ U for U in tau}
    interior = {A: 0 for A in subsets}
    closure = {A: X for A in subsets}
    for A in subsets:
        for U in tau:
            if (U & ~A) == 0:
                interior[A] |= U
        for F in closed:
            if (A & ~F) == 0:
                closure[A] &= F
    boundary = {A: closure[A] & ~interior[A] & X for A in subsets}
    ext = {A: interior[X ^ A] for A in subsets}
    derived = {}
    isolated = {}
    for A in subsets:
        d = 0
        for x in range(n):
            bit = 1 << x
            if all((U & (A & ~bit)) != 0 for U in tau if U & bit):
                d |= bit
        derived[A] = d
        isolated[A] = A & ~d
    is_t1 = all((X ^ (1 << x)) in tau for x in range(n))
    for A in subsets:
        assert interior[A] & ~A == 0
        assert A & ~closure[A] == 0
        assert interior[interior[A]] == interior[A]
        assert closure[closure[A]] == closure[A]
        assert closure[0] == 0
        assert closure[A] == A | derived[A]
        assert isolated[A] == (A & ~derived[A])
        # A is perfect iff A = A' in every topological space, even without T1.
        assert (closure[A] == A and isolated[A] == 0) == (A == derived[A])
        assert boundary[A] == (closure[A] & closure[X ^ A])
        assert boundary[A] == boundary[X ^ A]
        assert boundary[A] in closed
        assert ((interior[A] | boundary[A] | ext[A]) == X)
        assert interior[A] & boundary[A] == 0
        assert interior[A] & ext[A] == 0
        assert boundary[A] & ext[A] == 0
        assert closure[A] == interior[A] | boundary[A]
        assert (X ^ interior[A]) == closure[X ^ A]
        assert (X ^ closure[A]) == interior[X ^ A]
        assert (closure[A] == X) == all(not U or (U & A) for U in tau)
        assert (interior[closure[A]] == 0) == all(
            not U or any(V and (V & ~closure[A]) == V and (V & ~U) == 0
                         for V in tau)
            for U in tau
        )
        if is_t1:
            assert derived[A] in closed
        for B in subsets:
            assert (interior[A] & interior[B]) == interior[A & B]
            assert (closure[A] | closure[B]) == closure[A | B]
            assert (derived[A] | derived[B]) == derived[A | B]
            assert (boundary[A | B] & ~(boundary[A] | boundary[B])) == 0
            if A & ~B == 0:
                assert interior[A] & ~interior[B] == 0
                assert closure[A] & ~closure[B] == 0
                assert derived[A] & ~derived[B] == 0
            if interior[closure[A]] == 0 and interior[closure[B]] == 0:
                assert interior[closure[A | B]] == 0
    assert {A for A in subsets if closure[A] == A} == closed


def source_lint():
    labels, refs = [], []
    for p in CHAPTERS:
        src = p.read_text(encoding='utf-8')
        labels += re.findall(r'\\label\{([^}]+)\}', src)
        refs += re.findall(r'\\(?:ref|eqref)\{([^}]+)\}', src)
        for ln, line in enumerate(src.splitlines(), 1):
            if r'\label{' in line or line.strip().startswith('%'):
                continue
            assert not re.search(r'\bunia\b|\bkofinita\b', line, re.I), (p,ln,line)
        assert src.count(r'\begin{proof}') == src.count(r'\end{proof}'), p
    assert len(labels) == len(set(labels)), 'Duplicate labels'
    assert set(refs).issubset(set(labels)), set(refs)-set(labels)
    book = BOOK.read_text(encoding='utf-8')
    for p in CHAPTERS:
        required = r'\input{../../chapters/pl/general_topology/' + p.name + '}'
        assert required in book, required
    print(f'LATEX labels: {len(labels)} unique; references {len(refs)} resolved')


def main():
    counts = {}
    for n in range(5):
        k = 0
        for tau in enumerate_topologies(n):
            check_topology(n, tau)
            k += 1
        counts[n] = k
    assert counts == {0: 1, 1: 1, 2: 4, 3: 29, 4: 355}, counts
    # Non-T1 counterexample: indiscrete two-point X, A={a}, A'={b}.
    indiscrete = frozenset({0, 3})
    assert indiscrete in enumerate_topologies(2)
    # In that example {b} is not closed.
    assert 2 not in {3 ^ U for U in indiscrete}
    source_lint()
    print('Finite model verification passed:', counts)

if __name__ == '__main__':
    main()
