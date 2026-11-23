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

    def test_disjoint_additivity_for_singleton_neighborhood(self):
        n = covering_numbers(1 << IDX[E])
        for a in range(64):
            self.assertEqual(n[a], a.bit_count())
            for b in range(64):
                if not a & b:
                    self.assertEqual(n[a | b], n[a] + n[b])

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

    def test_source_guards(self):
        s = SOURCE.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        self.assertEqual(len(labels), len(set(labels)))
        for label in ("thm:haar-main-23", "lem:haar-cutoff-23",
                      "lem:haar-fubini-compact-23", "thm:haar-unique-23",
                      "thm:haar-modular-23", "ex:haar-affine-23"):
            self.assertIn(label, labels)
        self.assertIn(r"\widetilde\mu=c\mu", s)
        self.assertIn(r"\int_Gh(x)\,\mathrm d\widetilde\mu(x)", s)
        self.assertIn(r"\mu(E(c,t))=t^{-1}\mu(E)", s)
        self.assertIn("odwrotną inkluzję", s)
        self.assertIn(r"\bigcup_{j=1}^n g_jKK^{-1}", s)
        self.assertIn(r"\mu(G)\ge\sum_{n\ge1}\mu(g_nK)=+\infty", s)
        self.assertIn(r"m^*(\varnothing)=t(\varnothing)=0", s)
        stack = []
        for m in re.finditer(r"\\(begin|end)\{([^}]+)\}", s):
            if m[1] == "begin":
                stack.append(m[2])
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), m[2])
        self.assertFalse(stack)


if __name__ == "__main__":
    unittest.main()
