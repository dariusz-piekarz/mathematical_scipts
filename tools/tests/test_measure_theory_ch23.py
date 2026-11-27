"""Finite models and source regressions for Haar measure, chapter 23.

These tests do not establish the theorem on arbitrary locally compact groups.
"""
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/pl/measure_theory/23-miara-haara-na-grupach-lokalnie-zwartych.tex"
S3 = list(permutations(range(3)))
E = (0, 1, 2)
IDX = {g: i for i, g in enumerate(S3)}


def mul(g, h):
    return tuple(g[h[i]] for i in range(3))


def translate(g, mask):
    return sum(1 << IDX[mul(g, h)] for i, h in enumerate(S3) if mask & (1 << i))


def covering_numbers(v):
    shifts = [translate(g, v) for g in S3]
    result = [7] * 64
    for i in range(64):
        union = 0
        for j, s in enumerate(shifts):
            if i & (1 << j):
                union |= s
        for k in range(64):
            if union & k == k:
                result[k] = min(result[k], i.bit_count())
    return result


class TestHaarChapter23(unittest.TestCase):
    def test_covering_numbers_noncommutative_group(self):
        for v in range(64):
            if not v & (1 << IDX[E]):
                continue
            n = covering_numbers(v)
            self.assertEqual(n[0], 0)
            for a in range(64):
                for g in S3:
                    self.assertEqual(n[translate(g, a)], n[a])
                for b in range(64):
                    self.assertLessEqual(n[a | b], n[a] + n[b])
                    if a & b == a:
                        self.assertLessEqual(n[a], n[b])

    def test_normalized_covering_number_bounds(self):
        neighborhoods = [v for v in range(64) if v & (1 << IDX[E])]
        counts = {v: covering_numbers(v) for v in neighborhoods}
        for v0 in neighborhoods:
            base = counts[v0]
            for k0 in neighborhoods:
                if v0 & k0 != v0:
                    continue
                for v in neighborhoods:
                    denom = counts[v][k0]
                    self.assertGreater(denom, 0)
                    self.assertEqual(Fraction(counts[v][k0], denom), 1)
                    for k in range(64):
                        self.assertLessEqual(counts[v][k], base[k]*denom)

    def test_disjoint_additivity_for_singleton_neighborhood(self):
        n = covering_numbers(1 << IDX[E])
        for a in range(64):
            self.assertEqual(n[a], a.bit_count())
            for b in range(64):
                if not a & b:
                    self.assertEqual(n[a | b], n[a] + n[b])

    def test_haar_uniqueness_double_integral_identity(self):
        # Exhaust nonempty 0/1 kernels and signed test functions on S3.
        # Avoid division by the normalizing mass by cross multiplication.
        inv = {g: next(h for h in S3 if mul(g, h) == E) for g in S3}
        left = [[IDX[mul(inv[y], x)] for y in S3] for x in S3]
        right = [[IDX[mul(y, z)] for z in S3] for y in S3]
        for mask in range(1, 64):
            phi = [(mask >> i) & 1 for i in range(6)]
            for fmask in range(64):
                f = [1 if fmask & (1 << i) else -1 for i in range(6)]
                direct = sum(f[i]*phi[left[i][j]]
                             for i in range(6) for j in range(6))
                substituted = sum(f[right[j][k]]*phi[k]
                                  for j in range(6) for k in range(6))
                self.assertEqual(direct, substituted)
                self.assertEqual(direct, sum(phi)*sum(f))

    def test_uniqueness_requires_normalizing_factor(self):
        for a in range(1, 5):
            for b in range(1, 5):
                c = Fraction(b, a)
                for mask in range(64):
                    self.assertEqual(c * a * mask.bit_count(), b * mask.bit_count())

    def test_affine_left_and_right_jacobian(self):
        for a in map(Fraction, (1, 2, 3, 5)):
            for t in (Fraction(1, 3), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)):
                self.assertEqual(t*t / (t*a)**2, 1/a**2)
                self.assertEqual(t / (a*t)**2, (1/t) / a**2)
                self.assertEqual(t / (a*t), 1/a)
                # Inversion (b,a) -> (-b/a,1/a) has abs Jacobian a^(-3).
                self.assertEqual(1/a**3 / (1/a)**2, 1/a)

    def test_affine_inner_automorphism_module_and_inversion(self):
        for a in map(Fraction, (1, 2, 3, 5)):
            for b in map(Fraction, (-2, 0, 3)):
                for t in (Fraction(1, 3), Fraction(1), Fraction(2), Fraction(5)):
                    for c in map(Fraction, (-3, 0, 2)):
                        # (c,t)(b,a)(c,t)^(-1) = (tb+c(1-a), a).
                        bp, ap = c + t*b - a*c, a
                        self.assertEqual((bp-c*(1-ap))/t, b)
                        self.assertEqual(t/ap**2, t/a**2)
                        self.assertEqual(t, 1/(1/t))
                        # Inversion takes the left density to the right one.
                        bi, ai = -b/a, 1/a
                        self.assertEqual((-bi/ai, 1/ai), (b, a))
                        self.assertEqual((1/a**3)/ai**2, 1/a)
                        # Modularity is unchanged by conjugation.
                        self.assertEqual(1/ap, 1/a)

    def test_disjoint_translates_and_torus_invariance(self):
        # Z is noncompact; translates of a finite interval can be disjoint.
        K = set(range(-3, 4))
        translates = [{x + 7*n for x in K} for n in range(20)]
        self.assertEqual(len(set.union(*translates)), 20 * len(K))
        # Discrete torus models: translation preserves every subset's mass.
        for n in range(2, 9):
            for mask in range(1 << n):
                A = {i for i in range(n) if mask & (1 << i)}
                for t in range(n):
                    B = {(i+t) % n for i in A}
                    self.assertEqual(Fraction(len(A), n), Fraction(len(B), n))

    def test_convolution_finite_noncommutative_group(self):
        def conv(f, g):
            out = [0] * len(S3)
            for x in S3:
                for y in S3:
                    out[IDX[mul(x, y)]] += f[IDX[x]] * g[IDX[y]]
            return out
        f = [1, -2, 0, 3, 1, -1]
        g = [0, 1, 2, -1, 0, 3]
        h = [2, 1, 0, 0, -2, 1]
        self.assertEqual(conv(conv(f, g), h), conv(f, conv(g, h)))
        self.assertEqual(sum(conv(f, g)), sum(f) * sum(g))
        self.assertLessEqual(sum(map(abs, conv(f, g))),
                             sum(map(abs, f)) * sum(map(abs, g)))
        x, y = next((x, y) for x in S3 for y in S3 if mul(x, y) != mul(y, x))
        delta_x = [int(z == x) for z in S3]
        delta_y = [int(z == y) for z in S3]
        self.assertNotEqual(conv(delta_x, delta_y), conv(delta_y, delta_x))

    def test_affine_inversion_integrability_counterexample(self):
        # On [0,1] x [2**k, 2**(k+1)] the left Haar mass is
        # 2**(-k-1), while the inversion-weighted mass is log(2).
        # The latter has a uniform positive lower bound 1/2.
        for n in (1, 4, 16, 64):
            masses = []
            weighted_lower_bounds = []
            for k in range(n):
                a, b = 2**k, 2**(k+1)
                masses.append(Fraction(1, a) - Fraction(1, b))
                weighted_lower_bounds.append(Fraction(b-a, b))
            self.assertEqual(sum(masses), 1-Fraction(1, 2**n))
            self.assertEqual(sum(weighted_lower_bounds), Fraction(n, 2))

    def test_convolution_with_rescaled_counting_measure(self):
        f = [Fraction(x) for x in (1, -2, 0, 3, 1, -1)]
        g = [Fraction(x) for x in (0, 1, 2, -1, 0, 3)]

        def conv(scale):
            out = [Fraction(0)] * len(S3)
            for x in S3:
                for y in S3:
                    out[IDX[mul(x, y)]] += scale*f[IDX[x]]*g[IDX[y]]
            return out

        base = conv(Fraction(1))
        for c in (Fraction(1, 6), Fraction(2), Fraction(5, 3)):
            scaled = conv(c)
            self.assertEqual(scaled, [c*x for x in base])
            self.assertEqual(c*sum(scaled), (c*sum(f))*(c*sum(g)))
            self.assertLessEqual(c*sum(map(abs, scaled)),
                                 (c*sum(map(abs, f)))*(c*sum(map(abs, g))))

    def test_source_guards(self):
        s = SOURCE.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        self.assertEqual(len(labels), len(set(labels)))
        for label in ("thm:haar-main-23", "lem:haar-cutoff-23",
                      "lem:haar-fubini-compact-23", "thm:haar-unique-23",
                      "thm:haar-modular-23", "ex:haar-affine-23",
                      "eq:inwersja", "it:thm:haar-l1-convolution",
                      "tw:haar-automorfizm", "it:cor:haar-lie-automorphism"):
            self.assertIn(label, labels)
        self.assertIn(r"\widetilde\mu=c\mu", s)
        self.assertIn(r"\int_Gh(x)\,\mathrm d\widetilde\mu(x)", s)
        self.assertIn(r"\mu(E(c,t))=\int_E\frac{t}{(at)^2}", s)
        self.assertIn(r"=t^{-1}\mu(E)", s)
        self.assertIn("odwrotną inkluzję", s)
        self.assertIn(r"\bigcup_{j=1}^n g_jKK^{-1}", s)
        self.assertIn(r"\mu(G)\ge\sum_{n\ge1}\mu(g_nK)=+\infty", s)
        self.assertIn(r"m^*(\varnothing)=t(\varnothing)=0", s)
        self.assertNotRegex(s, r"\\R(?![A-Za-z])", "Use the supported mathbb R notation")
        stack = []
        for m in re.finditer(r"\\(begin|end)\{([^}]+)\}", s):
            if m[1] == "begin":
                stack.append(m[2])
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), m[2])
        self.assertFalse(stack)
        known = set(labels)
        for path in SOURCE.parent.glob("[0-9][0-9]-*.tex"):
            known.update(re.findall(r"\\label\{([^}]+)\}", path.read_text(encoding="utf-8")))
        refs = set(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", s))
        self.assertFalse(refs - known, f"Missing references: {sorted(refs - known)}")
        folders = {"ME": "measure_theory", "GT": "general_topology"}
        for code, label in re.findall(r"\\atlasref\{([^{}:]+)::([^{}]+)\}", s):
            with self.subTest(code=code, label=label):
                prefix, chapter = code.split("-")
                targets = list((ROOT / "chapters/pl" / folders[prefix]).glob(chapter + "-*.tex"))
                self.assertEqual(len(targets), 1)
                self.assertIn(r"\label{" + label + "}", targets[0].read_text(encoding="utf-8"))



if __name__ == "__main__":
    unittest.main()
