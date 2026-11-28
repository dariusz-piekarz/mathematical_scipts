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
    # If a=b the graph is one point; arbitrarily small boxes suffice.
    singleton_areas = [Fraction(4, N*N) for N in (2, 4, 8, 16, 32)]
    assert all(singleton_areas[i+1] < singleton_areas[i]
               for i in range(len(singleton_areas)-1))
    assert singleton_areas[-1] < Fraction(1, 100)
    # A constant function (L=0) on a non-degenerate interval is covered
    # by the same construction; its covering area still tends to zero.
    flat_areas = [
        N*(Fraction(1,N)+2*Fraction(1,N**2))*(2*Fraction(1,N**2))
        for N in (2, 4, 8, 16, 32, 64, 128)
    ]
    assert all(flat_areas[i+1] < flat_areas[i]
               for i in range(len(flat_areas)-1))
    assert flat_areas[-1] < Fraction(1, 5000)
    print("PASS Lipschitz graph: positive L, singleton and L=0 boundary cases")


def affine_interval_regression():
    """Exact 1D checks for negative scaling and endpoint conventions in R04.

    The image of [a,b) under t<0 is (tb,ta], not [tb,ta).
    Finite endpoints have zero Lebesgue measure, so an arbitrarily
    small half-open enlargement gives the correct outer-measure bound.
    """
    intervals = [
        (Fraction(-7, 3), Fraction(-1, 4)),
        (Fraction(0), Fraction(5, 6)),
        (Fraction(1, 9), Fraction(17, 8)),
    ]
    scales = (Fraction(-5, 2), Fraction(-1, 3), Fraction(1, 2), Fraction(7, 3))
    shifts = (Fraction(-4, 7), Fraction(0), Fraction(11, 5))
    cases = 0
    for a, b in intervals:
        assert a < b
        for t in scales:
            for shift in shifts:
                image_a, image_b = shift+t*a, shift+t*b
                lo, hi = min(image_a, image_b), max(image_a, image_b)
                assert hi-lo == abs(t)*(b-a)
                if t < 0:
                    # Image of the half-open interval [a,b) is (lo,hi].
                    # A half-open box [lo-eps,hi+eps) covers that image.
                    for eps in (Fraction(1, 10), Fraction(1, 1000)):
                        cover_a, cover_b = lo-eps, hi+eps
                        assert cover_a < lo < hi < cover_b
                        assert cover_b-cover_a == abs(t)*(b-a)+2*eps
                else:
                    # Positive scaling and translation preserve [a,b).
                    assert image_a == lo and image_b == hi
                cases += 1
    assert cases == 36
    print(f"PASS affine half-open interval regression: {cases} rational cases")


if __name__ == "__main__":
    check_grid_volume()
    cantor_interval_stages()
    smith_volterra_cantor()
    cantor_function_non_absolute_continuity()
    graph_cover_bound()
    affine_interval_regression()
