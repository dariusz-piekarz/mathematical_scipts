"""AM1-36: finite regressions for variation additivity and point-tag sums."""
from fractions import Fraction as Q
from itertools import combinations
import unittest


class TestVariationAndPointTags(unittest.TestCase):
    def test_variation_additivity_on_finite_nodes(self):
        values = [Q(0), Q(5, 3), Q(-1), Q(3, 2), Q(0)]
        def variation(u, v):
            if u == v:
                return Q(0)
            middle = range(u+1, v)
            return max(sum(abs(values[j]-values[i])
                           for i,j in zip(nodes, nodes[1:]))
                       for k in range(len(middle)+1)
                       for subset in combinations(middle,k)
                       for nodes in [(u,*subset,v)])
        for c in range(len(values)):
            self.assertEqual(variation(0,4), variation(0,c)+variation(c,4))

    def test_point_tag_telescope_and_endpoints(self):
        q = Q(-7,3)
        for n in range(2, 12):
            e = Q(1, 2**n)
            left, center, right = Q(1)+e, Q(4), Q(3)-e
            target = q*(Q(3)-Q(1))
            self.assertEqual(q*(center-left)+q*(right-center), q*(right-left))
            self.assertLessEqual(abs(q*(right-left)-target), 2*abs(q)*e)
            self.assertLessEqual(abs(q*(right-center)-q*(3-center)), abs(q)*e)
            self.assertLessEqual(abs(q*(center-left)-q*(center-1)), abs(q)*e)


if __name__ == '__main__':
    unittest.main()
