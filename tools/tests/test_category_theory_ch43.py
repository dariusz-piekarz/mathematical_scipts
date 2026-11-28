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


    def test_normalized_unit_defect(self):
        # Arbitrary homogeneous operations satisfying only the unit rules.
        # The normalized defect lemma does not require the Stasheff identities.
        degrees = {'u': -1, 'a': 0, 'b': 1}
        by_degree = {d: x for x, d in degrees.items() if x != 'u'}

        def operation(w):
            if 'u' in w:
                if len(w) != 2:
                    return {}
                x, y = w
                return {y: -1} if x == 'u' else {x: sign(degrees[x])}
            output = by_degree.get(1 + sum(degrees[x] for x in w))
            return {output: 1} if output is not None else {}

        def compositions(n):
            if n == 0:
                yield ()
            else:
                for j in range(1, n+1):
                    for tail in compositions(n-j):
                        yield (j,) + tail

        for n in range(2, 7):
            def f(w):
                if len(w) == 1:
                    return {w[0]: 1}
                if len(w) >= n or 'u' in w:
                    return {}
                output = by_degree.get(sum(degrees[x] for x in w))
                return {output: sign(len(w))} if output is not None else {}

            for word in product(degrees, repeat=n):
                if 'u' not in word:
                    continue
                left, right = Counter(), Counter()
                for parts in compositions(n):
                    start, blocks = 0, []
                    for j in parts:
                        blocks.append(f(word[start:start+j]))
                        start += j
                    for terms in product(*(block.items() for block in blocks)):
                        args = tuple(x for x, _ in terms)
                        coeff = 1
                        for _, a in terms:
                            coeff *= a
                        for value, b in operation(args).items():
                            left[value] += coeff*b
                for middle, a in apply_blocks(word, degrees, {j: operation for j in range(1, n+1)}).items():
                    for value, b in f(middle).items():
                        right[value] += a*b
                self.assertEqual({x: a for x, a in left.items() if a},
                                 {x: a for x, a in right.items() if a})

    def test_nonformal_exterior_algebra(self):
        # Bits 1, 2, 4 encode x, y, z, in that order; dz=xy.
        def mul(a, b):
            if a & b:
                return {}
            inversions = sum(1 for i in range(3) for j in range(i)
                             if a & (1 << i) and b & (1 << j))
            return {a | b: sign(inversions)}

        def d(a):
            return {3: 1} if a == 4 else {}

        def combine(target, terms, scalar=1):
            for x, a in terms.items():
                target[x] += scalar*a

        for a, b in product(range(8), repeat=2):
            left, right = Counter(), Counter()
            for c, s in mul(a, b).items():
                combine(left, d(c), s)
            for c, s in d(a).items():
                combine(right, mul(c, b), s)
            for c, s in d(b).items():
                combine(right, mul(a, c), s*sign(a.bit_count()))
            self.assertEqual({x: s for x, s in left.items() if s},
                             {x: s for x, s in right.items() if s})
        cycles = {a for a in range(8) if not d(a)}
        boundaries = {b for a in range(8) for b in d(a)}
        representatives = cycles - boundaries
        self.assertEqual(representatives, {0, 1, 2, 5, 6, 7})
        self.assertEqual([sum(a.bit_count() == n for a in representatives)
                          for n in range(4)], [1, 2, 2, 1])
        for a, b in product((1, 2), repeat=2):
            self.assertTrue(set(mul(a, b)).issubset(boundaries))

        def b2(a, b):
            return {c: s*sign(a.bit_count()-1) for c, s in mul(a, b).items()}

        # I2=-h b2(i,i), where h(sxy)=sz and h vanishes otherwise.
        def i2(a, b):
            return {4: -s for c, s in b2(a, b).items() if c == 3}

        self.assertEqual(i2(1, 1), {})
        self.assertEqual(i2(1, 2), {4: -1})
        obstruction = Counter()
        for c, s in i2(1, 2).items():
            combine(obstruction, b2(1, c), s)
        for c, s in i2(1, 1).items():
            combine(obstruction, b2(c, 2), s)
        # B2 vanishes on H^1 pairs, hence the two remaining terms are zero.
        self.assertEqual({c: s for c, s in obstruction.items()
                          if c in representatives and s}, {5: -1})


if __name__ == '__main__':
    unittest.main()
