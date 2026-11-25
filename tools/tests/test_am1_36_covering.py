"""AM1-36: finite interval-covering regressions (not a proof of the lemma)."""
from fractions import Fraction as Q
from itertools import combinations
import unittest


def select(intervals):
    chosen = []
    for a, b in sorted(intervals, key=lambda i: i[1]-i[0], reverse=True):
        if all(b <= c or d <= a for c, d in chosen):
            chosen.append((a, b))
    return chosen


class TestCovering(unittest.TestCase):
    def test_finite_cover_with_touching_endpoints(self):
        intervals = [(Q(a, 2), Q(b, 2)) for a in range(-2, 4)
                     for b in range(a+1, 5)]
        for family in combinations(intervals, 3):
            chosen = select(family)
            for (a,b),(c,d) in combinations(chosen,2):
                self.assertTrue(b <= c or d <= a)
            for a,b in family:
                self.assertTrue(any(c-2*(d-c) <= a and b <= d+2*(d-c)
                                    for c,d in chosen))

    def test_saks_henstock_signed_error_bound(self):
        errors = [Q(1, 4), Q(-1, 3), Q(1, 5), Q(-1, 6)]
        eps = Q(1, 2)
        for k in range(len(errors)+1):
            for group in combinations(errors, k):
                self.assertLessEqual(abs(sum(group)), eps)
        self.assertLessEqual(sum(map(abs, errors)), 2*eps)


if __name__ == '__main__':
    unittest.main()
