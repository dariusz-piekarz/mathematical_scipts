"""IT-05: finite exact-rational regression for gap-envelope correction.
Source: it:lem:perron-null-correction, it:thm:perron-hk.
These examples test inequalities, not the general existence proof.
"""
from fractions import Fraction as Q
import unittest


class TestPerronCorrection(unittest.TestCase):
    def test_it05_two_sided_gap_envelope(self):
        # Piecewise linear residual on a gap, with two separated maxima.
        R = list(map(Q, [0, 3, 1, 4, 2, 0]))
        L = [max(R[:i+1]) for i in range(len(R))]
        B = [max(R[i:]) for i in range(len(R))]
        K = [l+B[0]-b for l, b in zip(L, B)]
        self.assertEqual(K[-1]-K[0], 2*max(R))
        self.assertTrue(all(a <= b for a,b in zip(K, K[1:])))
        for i,r in enumerate(R):
            self.assertGreaterEqual(K[i]-K[0], r)
            self.assertGreaterEqual(K[-1]-K[i], r)

    def test_it05_boundary_and_signed_secants(self):
        R = list(map(Q, [4, 1, 3, 0]))
        B = [max(R[i:]) for i in range(len(R))]
        K = [B[0]-b for b in B]
        for i,r in enumerate(R):
            self.assertGreaterEqual(K[-1]-K[i], r)
        # At an exceptional tag, |F increment| + |f(tag)| * length
        # is sufficient on either side, even for a negative value of f.
        for dy in (Q(-1,8), Q(1,8)):
            for dF in (Q(-3,5), Q(3,5)):
                for f in (Q(-17), Q(17)):
                    dH = (abs(dF)+abs(f)*abs(dy)) * (1 if dy>0 else -1)
                    self.assertGreaterEqual((dF+dH)/dy, f)
                    self.assertLessEqual((dF-dH)/dy, f)


if __name__ == '__main__':
    unittest.main()
