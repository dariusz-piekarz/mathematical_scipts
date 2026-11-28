"""Independent finite CAL regressions retained after migration; not proofs."""
from fractions import Fraction as Q
import unittest


class TestLebesgueCalculus(unittest.TestCase):
    def test_nonabsolute_fubini_rectangles(self):
        a = lambda m, n: int(n == m) - int(n == m + 1)
        for k in range(1, 20):
            self.assertEqual(sum(a(m, n) for m in range(1, k+1) for n in range(1, k+2)), 0)
            self.assertEqual(sum(a(m, n) for m in range(1, k+1) for n in range(1, k+1)), 1)
            self.assertEqual(sum(abs(a(m, n)) for m in range(1, k+1) for n in range(1, k+2)), 2*k)

    def test_product_integral_finite_weights(self):
        p = [Q(1, 3), Q(2, 3)]
        q = [Q(1, 4), Q(3, 4)]
        f = [[Q(-2), Q(5)], [Q(3), Q(-1)]]
        left = sum(p[i]*sum(q[j]*f[i][j] for j in range(2)) for i in range(2))
        right = sum(q[j]*sum(p[i]*f[i][j] for i in range(2)) for j in range(2))
        self.assertEqual(left, right)

    def test_linear_jacobian_area(self):
        a, b, c, d = Q(2), Q(3, 2), Q(-1), Q(4)
        vertices = [(0, 0), (a, c), (a+b, c+d), (b, d)]
        twice_area = sum(x*v-y*u for (x,y),(u,v) in zip(vertices, vertices[1:]+vertices[:1]))
        self.assertEqual(abs(twice_area)/2, abs(a*d-b*c))

if __name__ == "__main__":
    unittest.main()
