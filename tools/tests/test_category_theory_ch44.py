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


    def test_kan_horn_filler(self):
        # Nerve of the additive group F_3, a simplicial abelian group.
        def face(w, i):
            if i == 0:
                return w[1:]
            if i == len(w):
                return w[:-1]
            return w[:i-1] + ((w[i-1]+w[i]) % 3,) + w[i+1:]

        def correct(y, x, i, s):
            error = tuple((a-b) % 3 for a, b in zip(x, face(y, i)))
            degenerate = error[:s] + (0,) + error[s:]
            return tuple((a+b) % 3 for a, b in zip(y, degenerate))

        for n in range(1, 7):
            for w in product(range(3), repeat=n):
                for j in range(n+1):
                    y = (0,) * n
                    for i in range(j):
                        y = correct(y, face(w, i), i, i)
                    for i in range(n, j, -1):
                        y = correct(y, face(w, i), i, i-1)
                    for i in range(n+1):
                        if i != j:
                            self.assertEqual(face(y, i), face(w, i))

    def test_tilting_a3_hom_and_ext(self):
        # Thin representations over F_3: vertex dimensions and arrow scalars.
        p1 = ((1, 1, 1), (1, 1))
        p2 = ((0, 1, 1), (0, 1))
        p3 = ((0, 0, 1), (0, 0))
        s2 = ((0, 1, 0), (0, 0))

        def hom(src, dst):
            ds, fs = src
            dt, ft = dst
            choices = [range(3) if a*b else (0,) for a, b in zip(ds, dt)]
            return {x for x in product(*choices)
                    if all((ft[i]*x[i]-x[i+1]*fs[i]) % 3 == 0
                           for i in range(2))}

        terms = (p1, p2, s2)
        self.assertEqual([[len(hom(x, y)) for y in terms] for x in terms],
                         [[3, 1, 1], [3, 3, 3], [1, 1, 3]])
        # Restriction along P3 -> P2 keeps only the component at vertex 3.
        for target in terms:
            self.assertEqual({(0, 0, x[2]) for x in hom(p2, target)},
                             hom(p3, target))


    def test_inverse_matrix_bimodules(self):
        # Balanced row/column tensor over M_m(F_3).
        for m in range(1, 6):
            width = m*m
            pivots = {}
            for i, a, b, j in product(range(m), repeat=4):
                row = [0]*width
                # (u_i E_ab) tensor t_j - u_i tensor (E_ab t_j)
                if i == a:
                    row[b*m+j] += 1
                if b == j:
                    row[i*m+a] -= 1
                self.assertEqual(sum(row[z*m+z] for z in range(m)) % 3, 0)
                row = [x % 3 for x in row]
                for col in sorted(pivots):
                    factor = row[col]
                    row = [(x-factor*y) % 3 for x, y in zip(row, pivots[col])]
                if any(row):
                    col = next(i for i, x in enumerate(row) if x)
                    inv = pow(row[col], -1, 3)
                    pivots[col] = [(x*inv) % 3 for x in row]
            self.assertEqual(width-len(pivots), 1)
            # Unbalanced column/row tensor maps its basis to matrix units.
            units = {tuple(int(r == i and c == j)
                           for r, c in product(range(m), repeat=2))
                     for i, j in product(range(m), repeat=2)}
            self.assertEqual(len(units), width)


if __name__ == '__main__':
    unittest.main()
