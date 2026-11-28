"""AM1-36: finite exact regressions for spike criteria, not limit proofs."""
from fractions import Fraction as Q
from itertools import product
import unittest


class TestSpikeCriteria(unittest.TestCase):
    def test_variation_atom_comparison(self):
        for left, right in product(range(-5, 6), repeat=2):
            signed = abs(left + right)
            variation = abs(left) + abs(right)
            self.assertLessEqual(signed, variation)
            self.assertLessEqual(abs(right), variation)
            self.assertLessEqual(variation, signed + 2*abs(right))

    def test_isolated_spike_first_cell_error(self):
        f_a = Q(7, 3)
        for n in range(2, 20):
            nodes = [Q(0), Q(1, 2**n), Q(1, 2**(n-1)), Q(1)]
            vals = [f_a, Q(2**n, n), Q(2**(n-1), n-1)]
            # Separate the two spikes with a zero node and matching tags.
            g = [Q(0), nodes[1], Q(0), nodes[2], Q(0)]
            vals = [f_a, vals[1], vals[2], vals[2]]
            direct = sum(f*(v-u) for f,u,v in zip(vals,g,g[1:]))
            self.assertEqual(direct, f_a*nodes[1]-Q(1,n))
            self.assertLessEqual(abs(direct), abs(f_a)*nodes[1]+Q(1,n))

    def test_nonsummable_products(self):
        for k in range(1, 10):
            block = sum(Q(1,n) for n in range(2**k,2**(k+1)))
            self.assertGreaterEqual(block,Q(1,2))
            self.assertEqual(Q(2**k,k)*Q(1,2**k),Q(1,k))


if __name__ == '__main__':
    unittest.main()
