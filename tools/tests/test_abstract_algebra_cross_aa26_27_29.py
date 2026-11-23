"""AA-X26: exact Artin-Schreier / Kummer Frobenius bridge over finite fields.

Finite fields F_{p^m} are implemented by elementary polynomial arithmetic;
the gcd and Frobenius tests do not assume a factorization oracle.
"""
from pathlib import Path
import re
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
X = sp.Symbol("X")


class SmallField:
    """F_p[u]/(monic irreducible modulus), elements encoded in base p."""

    def __init__(self, p, modulus):
        self.p = p
        self.modulus = tuple(modulus)
        self.m = len(modulus)-1
        self.q = p**self.m
        assert modulus[-1] == 1

    def digits(self, a):
        return tuple((a//self.p**i) % self.p for i in range(self.m))

    def encode(self, digits):
        return sum((int(c) % self.p) * self.p**i
                   for i, c in enumerate(digits))

    def add(self, a, b):
        return self.encode(x+y for x, y in zip(self.digits(a),
                                               self.digits(b)))

    def neg(self, a):
        return self.encode(-x for x in self.digits(a))

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        u, v = self.digits(a), self.digits(b)
        coeff = [0]*(2*self.m-1)
        for i, x in enumerate(u):
            for j, y in enumerate(v):
                coeff[i+j] = (coeff[i+j]+x*y) % self.p
        for i in range(len(coeff)-1, self.m-1, -1):
            c = coeff[i] % self.p
            if c:
                for j, t in enumerate(self.modulus):
                    coeff[i-self.m+j] = (coeff[i-self.m+j]-c*t) % self.p
        return self.encode(coeff[:self.m])

    def power(self, a, exponent):
        assert exponent >= 0
        out = 1
        while exponent:
            if exponent & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            exponent >>= 1
        return out

    def inverse(self, a):
        assert a != 0
        return self.power(a, self.q-2)

    def trace(self, a):
        out, z = 0, a
        for _ in range(self.m):
            out = self.add(out, z)
            z = self.power(z, self.p)
        assert 0 <= out < self.p  # image of absolute trace is F_p
        return out

    def artin_schreier(self, a):
        return self.sub(self.power(a, self.p), a)

    def order(self, a):
        assert a != 0
        z = 1
        for k in range(1, self.q):
            z = self.mul(z, a)
            if z == 1:
                return k
        raise AssertionError("multiplicative order not found")


def trim(poly):
    z = list(poly)
    while len(z) > 1 and z[-1] == 0:
        z.pop()
    return z


def poly_add(field, a, b):
    z = [0]*max(len(a), len(b))
    for i in range(len(z)):
        z[i] = field.add(a[i] if i < len(a) else 0,
                         b[i] if i < len(b) else 0)
    return trim(z)


def poly_sub(field, a, b):
    return poly_add(field, a, [field.neg(x) for x in b])


def poly_mul(field, a, b):
    z = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i+j] = field.add(z[i+j], field.mul(x, y))
    return trim(z)


def poly_rem(field, numerator, divisor):
    assert divisor != [0]
    z = trim(numerator)
    n = len(divisor)-1
    lead_inv = field.inverse(divisor[-1])
    while len(z)-1 >= n and z != [0]:
        scale = field.mul(z[-1], lead_inv)
        idx = len(z)-n-1
        for j, c in enumerate(divisor):
            z[idx+j] = field.sub(z[idx+j], field.mul(scale, c))
        z = trim(z)
    return z


def poly_gcd(field, a, b):
    a, b = trim(a), trim(b)
    while b != [0]:
        a, b = b, poly_rem(field, a, b)
    if a == [0]:
        return a
    inv = field.inverse(a[-1])
    return trim([field.mul(inv, c) for c in a])


def poly_x_power_mod(field, exponent, modulus):
    z = [1]
    b = poly_rem(field, [0, 1], modulus)
    while exponent:
        if exponent & 1:
            z = poly_rem(field, poly_mul(field, z, b), modulus)
        b = poly_rem(field, poly_mul(field, b, b), modulus)
        exponent >>= 1
    return z


def fixed_root_count(field, monic, k):
    # Degree of gcd(f, X^(q^k)-X): all roots are simple in the
    # separable cases, and gcd counts Frobenius-fixed roots.
    r = poly_x_power_mod(field, field.q**k, monic)
    return len(poly_gcd(field, monic,
                        poly_sub(field, r, [0, 1])))-1


def as_polynomial(field, a):
    # X^p-X-a in F_q[X] (p=2 is handled automatically).
    z = [field.neg(a)] + [0]*(field.p-1) + [1]
    z[1] = field.neg(1)
    return z


def kummer_polynomial(field, n, a):
    return [field.neg(a)] + [0]*(n-1) + [1]


FIELDS = (
    SmallField(2, (0, 1)),
    SmallField(3, (0, 1)),
    SmallField(5, (0, 1)),
    SmallField(7, (0, 1)),
    SmallField(11, (0, 1)),
    SmallField(13, (0, 1)),
    SmallField(17, (0, 1)),
    SmallField(2, (1, 1, 1)),       # F4
    SmallField(2, (1, 1, 0, 1)),    # F8
    SmallField(2, (1, 1, 0, 0, 1)), # F16
    SmallField(3, (1, 0, 1)),       # F9
    SmallField(3, (1, 2, 0, 1)),    # F27
    SmallField(5, (2, 0, 1)),       # F25
)


class KummerArtinSchreierFiniteFieldAudit(unittest.TestCase):
    def test_field_models_multiplicative_orders_and_frobenius(self):
        for field in FIELDS:
            with self.subTest(q=field.q):
                self.assertEqual(len({field.power(a, field.q)
                                      for a in range(field.q)}), field.q)
                for a in range(field.q):
                    self.assertEqual(field.power(a, field.q), a)
                    self.assertEqual(
                        field.power(field.power(a, field.p),
                                    field.p**(field.m-1)), a)
                    if a:
                        self.assertEqual(
                            field.mul(a, field.inverse(a)), 1)
                        self.assertEqual((field.q-1) % field.order(a), 0)

    def test_artin_schreier_image_equals_absolute_trace_kernel(self):
        for field in FIELDS:
            with self.subTest(q=field.q):
                image = {field.artin_schreier(x)
                         for x in range(field.q)}
                kernel = {x for x in range(field.q)
                          if field.trace(x) == 0}
                self.assertEqual(image, kernel)
                self.assertEqual(len(image), field.q//field.p)
                self.assertEqual({field.trace(a)
                                  for a in range(field.q)},
                                 set(range(field.p)))
                self.assertEqual(sum(field.artin_schreier(x) == 0
                                     for x in range(field.q)), field.p)
                for a in range(field.q):
                    tr = field.trace(a)
                    roots = sum(field.artin_schreier(x) == a
                                for x in range(field.q))
                    self.assertEqual(roots, field.p if tr == 0 else 0)

    def test_artin_schreier_frobenius_fixed_roots(self):
        models = (FIELDS[0], FIELDS[1], FIELDS[2], FIELDS[3],
                  FIELDS[7], FIELDS[8], FIELDS[10], FIELDS[11], FIELDS[12])
        for field in models:
            for a in range(field.q):
                with self.subTest(q=field.q, a=a):
                    f = as_polynomial(field, a)
                    tr = field.trace(a)
                    for k in range(1, field.p+1):
                        count = fixed_root_count(field, f, k)
                        expected = field.p if (
                            tr == 0 or k % field.p == 0) else 0
                        self.assertEqual(count, expected)
                    # The characteristic-p polynomial is always separable.
                    self.assertEqual(
                        poly_gcd(field, f, [field.neg(1)]), [1])

    def test_kummer_frobenius_order_predicts_factor_degrees(self):
        verified = 0
        for field in FIELDS:
            q = field.q
            for n in range(2, min(q-1, 9)+1):
                if (q-1) % n:
                    continue
                self.assertNotEqual(n % field.p, 0)
                for a in range(1, q):
                    with self.subTest(q=q, n=n, a=a):
                        eta = field.power(a, (q-1)//n)
                        self.assertEqual(field.power(eta, n), 1)
                        d = field.order(eta)
                        self.assertEqual(n % d, 0)
                        f = kummer_polynomial(field, n, a)
                        for k in range(1, n+1):
                            expected = n if k % d == 0 else 0
                            self.assertEqual(
                                fixed_root_count(field, f, k), expected)
                        verified += 1
        self.assertGreater(verified, 100)

    def test_kummer_quotient_and_additive_extension_class(self):
        for field in FIELDS:
            q, p = field.q, field.p
            for n in range(2, min(q-1, 9)+1):
                if (q-1) % n:
                    continue
                classes = {field.power(a, (q-1)//n)
                           for a in range(1, q)}
                powers = {field.power(a, n) for a in range(1, q)}
                self.assertEqual(len(classes), n)
                self.assertEqual(len(powers), (q-1)//n)
                self.assertEqual(
                    {a for a in range(1, q)
                     if field.power(a, (q-1)//n) == 1}, powers)
            nonzero = [a for a in range(q) if field.trace(a) != 0]
            # F_q / wp(F_q) is one-dimensional over F_p:
            # all nonzero Artin-Schreier classes define the same F_{q^p}.
            for a in nonzero:
                for b in nonzero:
                    c = (field.trace(b) *
                         pow(field.trace(a), p-2, p)) % p
                    self.assertNotEqual(c, 0)
                    delta = field.sub(b, field.mul(c, a))
                    self.assertEqual(field.trace(delta), 0)

    def test_explicit_small_field_edge_cases(self):
        f13 = next(f for f in FIELDS if f.q == 13)
        self.assertEqual(f13.order(f13.power(2, 3)), 4)
        self.assertEqual(f13.order(f13.power(4, 3)), 2)
        self.assertEqual(fixed_root_count(
            f13, kummer_polynomial(f13, 4, 2), 4), 4)
        self.assertEqual(fixed_root_count(
            f13, kummer_polynomial(f13, 4, 2), 2), 0)
        self.assertEqual(fixed_root_count(
            f13, kummer_polynomial(f13, 4, 4), 2), 4)
        f4 = next(f for f in FIELDS if f.q == 4)
        self.assertEqual(f4.trace(1), 0)
        self.assertEqual(f4.trace(2), 1)
        self.assertEqual(fixed_root_count(f4, as_polynomial(f4, 1), 1), 2)
        self.assertEqual(fixed_root_count(f4, as_polynomial(f4, 2), 1), 0)
        f9 = next(f for f in FIELDS if f.q == 9)
        self.assertEqual(f9.trace(1), 2)
        self.assertEqual(f9.trace(3), 0)
        self.assertEqual(fixed_root_count(f9, as_polynomial(f9, 1), 3), 3)
        # In F_q every element is a p-th power; X^p-a is (X-b)^p.
        for field in FIELDS:
            for a in range(field.q):
                b = field.power(a, field.p**(field.m-1))
                self.assertEqual(field.power(b, field.p), a)

    def test_prime_field_sympy_factorization_independent_crosscheck(self):
        for field in FIELDS:
            if field.m != 1 or field.p > 13:
                continue
            p = field.p
            for n in range(2, min(p-1, 8)+1):
                if (p-1) % n:
                    continue
                for a in range(1, p):
                    f = sp.Poly(X**n-a, X, modulus=p)
                    factors = sp.factor_list(f)[1]
                    degrees = sorted(g.degree() for g, e in factors
                                     for _ in range(e))
                    eta = pow(a, (p-1)//n, p)
                    d = field.order(eta)
                    self.assertEqual(degrees, [d]*(n//d))
                    self.assertEqual(sum(degrees), n)
            for a in range(p):
                f = sp.Poly(X**p-X-a, X, modulus=p)
                factors = sp.factor_list(f)[1]
                degrees = sorted(g.degree() for g, e in factors
                                 for _ in range(e))
                self.assertEqual(degrees,
                                 [1]*p if a == 0 else [p])

    def test_source_hypotheses_labels_references_all_chapters(self):
        folder = ROOT / "chapters/pl/abstract_algebra"
        paths = sorted(folder.glob("[0-9][0-9]-*.tex"))
        self.assertEqual(len(paths), 50)
        sources = {p.name:p.read_text(encoding="utf8") for p in paths}
        labels = [m for s in sources.values()
                  for m in re.findall(r"\\label\{([^{}]+)\}", s)]
        self.assertEqual(len(labels), len(set(labels)))
        focus = (
            "26-rozszerzenia-cykliczne-i-teoria-kummera.tex",
            "27-teoria-artina-schreiera.tex",
            "29-struktura-cial-skonczonych-i-wielomiany-nierozkladalne.tex",
        )
        self.assertEqual(
            sum(len(re.findall(r"\\label\{", sources[f]))
                for f in focus), 33)
        refs = [z for f in focus
                for z in re.findall(
                    r"\\(?:ref|pageref|eqref|autoref)\{([^{}]+)\}",
                    sources[f])]
        self.assertEqual(len(refs), 16)
        self.assertEqual(set(refs)-set(labels), set())
        for label in (
            "aa:tw:kummer-radical-cyclic",
            "aa:tw:kummer-converse",
            "aa:tw:as-forward", "aa:tw:as-classification",
            "aa:tw:finite-frobenius-roots",
        ):
            self.assertIn(label, labels)
        self.assertIn("charakterystyki", sources[focus[1]])
        self.assertIn("\\mu_n(F)", sources[focus[0]])


if __name__ == "__main__":
    unittest.main()
