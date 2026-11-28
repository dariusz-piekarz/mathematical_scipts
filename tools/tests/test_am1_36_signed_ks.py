"""Finite exact regression checks for cancelled KS jumps and point spikes."""
from fractions import Fraction as Q
import unittest


class TestSignedKS(unittest.TestCase):
    def test_cancelled_atoms_nonvanishing_local_jump(self):
        for n in range(1, 21):
            r = Q(1, 2**n)
            f = Q(2**n)
            self.assertEqual(r-r, 0)
            self.assertEqual(f*r, 1)
            self.assertEqual(f*(-r), -1)
        self.assertEqual(sum(2*Q(1, 2**n) for n in range(1, 21)),
                         2*(1-Q(1, 2**20)))

    def test_point_spike_summation_and_matched_tags(self):
        nodes = [Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)]
        spikes = [Q(0), Q(3, 7), Q(0), Q(-2, 9), Q(0)]
        f = lambda t: 3*t-1
        tags = [nodes[1], nodes[1], nodes[3], nodes[3]]
        direct = sum(f(t)*(v-u) for t,u,v in zip(tags,spikes,spikes[1:]))
        by_parts = sum(spikes[i]*(f(tags[i-1])-f(tags[i]))
                       for i in range(1, len(nodes)-1))
        self.assertEqual(direct, by_parts)
        self.assertEqual(direct, 0)
        tags[0] = Q(0)
        self.assertNotEqual(sum(f(t)*(v-u) for t,u,v in zip(tags,spikes,spikes[1:])), 0)

    def test_weighted_tail(self):
        for n in range(1, 12):
            # r_k=4^-k, f(c_k)=2^k, weighted tail equals 2^-n.
            partial = sum(Q(1, 2**k) for k in range(n+1, 25))
            self.assertEqual(partial+Q(1, 2**24), Q(1, 2**n))


if __name__ == '__main__':
    unittest.main()
