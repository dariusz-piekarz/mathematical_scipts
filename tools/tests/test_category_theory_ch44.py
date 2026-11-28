"""Finite regression checks for CAT-44; not substitutes for proofs."""
from functools import lru_cache
from itertools import product
import unittest


def sign(n):
    return (-1) ** (n % 2)


def reduce_once(word):
    # Columns in the one-object abelian group Z/3, with vertical identities.
    for i, (direction, value) in enumerate(word):
        if value == 0:
            yield word[:i] + word[i+1:]
        if i+1 < len(word) and direction == word[i+1][0]:
            yield word[:i] + ((direction, (value+word[i+1][1]) % 3),) + word[i+2:]


@lru_cache(maxsize=None)
def normal_forms(word):
    steps = tuple(reduce_once(word))
    if not steps:
        return frozenset((word,))
    return frozenset(form for step in steps for form in normal_forms(step))


class CategoryTheoryCh44(unittest.TestCase):
    def test_bimodule_composition_sign(self):
        for p, r, s, u, v in product(range(-3, 4), repeat=5):
            self.assertEqual(sign(r*p+u*(p+r+s)), sign(s*u+r*u+(r+u)*p))

    def test_bimodule_commuting_actions(self):
        for p, r, s in product(range(-3, 4), repeat=3):
            self.assertEqual(sign(r*p), sign(r*(p+s)+s*r))
            self.assertEqual(sign(r*p+s*(p+r)+r*s), sign((r+s)*p))

    def test_bimodule_differential_sign(self):
        for p, r, s in product(range(-3, 4), repeat=3):
            self.assertEqual(sign(r*p), sign(p+(r+1)*p))
            self.assertEqual(sign(r*p+r), sign(r*(p+1)))
            self.assertEqual(sign(r*p+r+p), sign(p+r+r*p))

    def test_shift_in_second_tensor_factor(self):
        for p, r in product(range(-3, 4), repeat=2):
            self.assertEqual(sign(p+r), sign(p)*sign(r))
            self.assertEqual(sign(p+1), -sign(p))
            self.assertEqual(-sign(p)*sign(p), -1)

    def test_hammock_reduction_confluence(self):
        alphabet = tuple(product((-1, 1), range(3)))
        for n in range(6):
            for word in product(alphabet, repeat=n):
                forms = normal_forms(word)
                self.assertEqual(len(forms), 1)
                form = next(iter(forms))
                self.assertEqual(sum(d*x for d, x in word) % 3,
                                 sum(d*x for d, x in form) % 3)
                self.assertFalse(any(x == 0 for _, x in form))
                self.assertTrue(all(a[0] != b[0] for a, b in zip(form, form[1:])))

    def test_left_arrow_square_inversion(self):
        # In Z/3, the equation u*g = g_prime*v is additive.
        for u, g, gp, v in product(range(3), repeat=4):
            if (u+g-gp-v) % 3 == 0:
                self.assertEqual((v-g) % 3, (u-gp) % 3)


if __name__ == '__main__':
    unittest.main()
