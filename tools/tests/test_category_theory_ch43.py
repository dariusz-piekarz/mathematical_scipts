"""Finite regression checks for CAT-43 sign conventions, not formal proofs."""
from collections import Counter
from itertools import product
import unittest


def sign(n):
    return (-1) ** (n % 2)


def apply_blocks(word, degrees, operations):
    result = Counter()
    for r in range(len(word)):
        for j, op in operations.items():
            if r + j <= len(word):
                for value, coeff in op(word[r:r+j]).items():
                    result[word[:r] + (value,) + word[r+j:]] += (
                        sign(sum(degrees[x] for x in word[:r])) * coeff
                    )
    return result


def twice(word, degrees, operations):
    result = Counter()
    for middle, a in apply_blocks(word, degrees, operations).items():
        for output, b in apply_blocks(middle, degrees, operations).items():
            result[output] += a * b
    return {word: c for word, c in result.items() if c}


class CategoryTheoryCh43(unittest.TestCase):
    def test_unsuspended_stasheff_sign(self):
        for n in range(1, 8):
            for u in product(range(2), repeat=n):
                common = sum((n-a-1)*x for a, x in enumerate(u))
                for j in range(1, n+1):
                    for r in range(n-j+1):
                        t = n-r-j
                        outer = u[:r] + (1+sum(u[r:r+j]),) + u[r+j:]
                        suspended = (sum(u[:r])
                                     + sum((j-a-1)*x for a, x in enumerate(u[r:r+j]))
                                     + sum((len(outer)-a-1)*x for a, x in enumerate(outer)))
                        unsuspended = common + t+j*r+(2-j)*sum(x+1 for x in u[:r])
                        self.assertEqual(sign(suspended), sign(unsuspended))

    def test_bar_square_contractible_dg_algebra(self):
        # Exterior generator theta of degree -1, with d(theta)=1.
        degrees = {'1': -1, 't': -2}  # suspended degrees

        def b1(w):
            return {'1': 1} if w == ('t',) else {}

        def b2(w):
            x, y = w
            if x == y == 't':
                return {}
            return {y if x == '1' else x: sign(degrees[x])}

        for n in range(1, 8):
            for word in product(degrees, repeat=n):
                self.assertEqual(twice(word, degrees, {1: b1, 2: b2}), {})

    def test_pure_ternary_operation(self):
        degrees = {'a': 0, 'c': 1}
        b3 = lambda w: {'c': 1} if w == ('a', 'a', 'a') else {}
        for n in range(1, 8):
            for word in product(degrees, repeat=n):
                self.assertEqual(twice(word, degrees, {3: b3}), {})

    def test_tensor_contraction(self):
        # d(l)=b, h(b)=l, ip projects onto the cohomology basis z.
        degrees = {'l': 0, 'b': 1, 'z': 0}

        def d(word):
            return apply_blocks(word, degrees, {1: lambda w: {'b': 1} if w == ('l',) else {}})

        def h(word):
            result = Counter()
            for r, x in enumerate(word):
                if x == 'b' and all(v == 'z' for v in word[:r]):
                    result[word[:r] + ('l',) + word[r+1:]] += sign(sum(degrees[v] for v in word[:r]))
            return result

        for n in range(1, 6):
            for word in product(degrees, repeat=n):
                out = Counter()
                for first, second in [(d, h), (h, d)]:
                    for w, a in first(word).items():
                        for v, b in second(w).items():
                            out[v] += a*b
                expected = {} if all(x == 'z' for x in word) else {word: 1}
                self.assertEqual({w: c for w, c in out.items() if c}, expected)

    def test_opposite_composition_associativity(self):
        for p, q, r in product(range(-3, 4), repeat=3):
            self.assertEqual(sign(p*q+(p+q)*r), sign(q*r+p*(q+r)))
            self.assertEqual(sign(p*q), sign(q+(p+1)*q))
            self.assertEqual(sign(p*q+p), sign(p*(q+1)))


if __name__ == '__main__':
    unittest.main()
