"""AM1-36: exact finite checks for KS split atoms and variation measure."""
from fractions import Fraction as Q
import unittest


class TestKSMeasure(unittest.TestCase):
    def test_split_atoms(self):
        # Values of g at a,a+,c-,c,c+,b-,b, with continuous mass between.
        a, ap, cm, c, cp, bm, b = map(Q, [0, 2, 3, 5, 8, 10, 11])
        nu_left = (cm-ap)+(ap-a)+(c-cm)
        nu_right = (bm-cp)+(cp-c)+(b-bm)
        self.assertEqual(nu_left, c-a)
        self.assertEqual(nu_right, b-c)
        self.assertEqual(nu_left+nu_right, b-a)
        self.assertEqual((c-cm)+(cp-c), cp-cm)
        self.assertEqual((ap-a)+(cp-cm)+(b-bm)+(cm-ap)+(bm-cp), b-a)

    def test_cancelling_one_sided_jumps(self):
        # A point spike: signed mass vanishes, variation mass is positive.
        gm, g0, gp = Q(0), Q(3), Q(0)
        self.assertEqual(gp-gm, 0)
        self.assertEqual(abs(g0-gm)+abs(gp-g0), 6)
        for f in [Q(0), Q(-5, 3), Q(11)]:
            self.assertEqual(f*(g0-gm)+f*(gp-g0), 0)


if __name__ == '__main__':
    unittest.main()
