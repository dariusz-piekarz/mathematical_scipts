"""Exact finite regressions for chapter 04 (Lebesgue measure).

Independent checks of finite-grid volume, Cantor constructions and
geometric covering bounds. Finite examples cannot replace the proofs.
"""
from fractions import Fraction
from itertools import combinations

def check_grid_volume():
    # Nine disjoint half-open unit cells in [0,3)^2.
    # Every mask is an element of the corresponding finite set algebra.
    masks = range(1 << 9)
    count = 0
    for a in masks:
        va = a.bit_count()
        for b in masks:
            vb = b.bit_count()
            if a & b == a:
                assert va <= vb
            assert (a | b).bit_count() <= va + vb
            if not (a & b):
                assert (a | b).bit_count() == va + vb
            count += 1
    assert count == 512**2
    print(f"PASS finite-grid volume: {count} ordered pairs")

def cantor_interval_stages():
    intervals = [(Fraction(0), Fraction(1))]
    for n in range(11):
        assert len(intervals) == 2**n
        assert all(b-a == Fraction(1, 3**n) for a, b in intervals)
        assert sum((b-a for a,b in intervals), Fraction(0)) == Fraction(2,3)**n
        if n == 10:
            break
        nxt = []
        for a, b in intervals:
            third = (b-a)/3
            nxt.extend(((a,a+third),(b-third,b)))
        intervals = nxt
    print("PASS Cantor: 11 stages, 2047 exact stage intervals")

def smith_volterra_cantor():
    intervals = [(Fraction(0), Fraction(1))]
    for n in range(1, 11):
        gap = Fraction(1, 4**n)
        nxt = []
        for a,b in intervals:
            mid = (a+b)/2
            assert b-a > gap
            nxt.extend(((a, mid-gap/2), (mid+gap/2,b)))
        intervals = nxt
        expected_length = Fraction(1,2**(n+1)) + Fraction(1,2**(2*n+1))
        assert len(intervals) == 2**n
        assert all(b-a == expected_length for a,b in intervals)
        assert sum((b-a for a,b in intervals), Fraction(0)) == (
            Fraction(1,2) + Fraction(1,2**(n+1))
        )
    print("PASS Smith-Volterra-Cantor: 10 exact stages, limit mass 1/2")

def cantor_function_non_absolute_continuity():
    for n in range(1, 15):
        total_cover_length = Fraction(2,3)**n
        total_function_increment = sum(
            (Fraction(1, 2**n) for _ in range(2**n)), Fraction(0)
        )
        assert total_cover_length < 1 and total_function_increment == 1
    print("PASS Cantor function: 14 exact finite-stage witnesses")

def graph_cover_bound():
    # The covering computation used for an L-Lipschitz graph, with
    # a=0, b=1 and eta=delta^2. Test exact rational bounds.
    L = Fraction(3,2)
    previous = None
    for N in (1,2,4,8,16,32,64,128,256):
        delta = Fraction(1,N)
        cover_area = N*(delta+2*delta**2)*(2*L*delta+2*delta**2)
        assert cover_area > 0
        if previous is not None:
            assert cover_area < previous
        previous = cover_area
    assert previous < Fraction(1, 50)
    print("PASS Lipschitz graph: 9 rational covering bounds")

if __name__ == "__main__":
    check_grid_volume()
    cantor_interval_stages()
    smith_volterra_cantor()
    cantor_function_non_absolute_continuity()
    graph_cover_bound()
