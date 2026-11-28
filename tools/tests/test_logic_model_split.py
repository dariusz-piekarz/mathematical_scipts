"""Migration guard and exact rational tests of the first fuzzy-logic chapter."""
import hashlib
import itertools
import json
import re
import unittest
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = json.loads((ROOT / "catalog/logic_model_migration.json").read_text("utf8"))
CATALOG = json.loads((ROOT / "catalog/books.json").read_text("utf8"))["books"]
BY_ID = {book["id"]: book for book in CATALOG}
LST = BY_ID["logic_and_set_theory"]
MOD = BY_ID["model_theory"]
FUZZY = ROOT / "chapters/pl/logic_and_set_theory/40-logika-rozmyta-i-zbiory-rozmyte.tex"
LABEL = re.compile(r"\\label\{([^}]+)\}")
REF = re.compile(r"\\(?:ref|eqref|autoref|pageref)\{([^}]+)\}|\\hyperref\[([^\]]+)\]")


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


class TestLogicModelSplit(unittest.TestCase):
    def test_archive_byte_identity_and_registration(self):
        for old in MANIFEST["legacy_chapters"]:
            with self.subTest(path=old["path"]):
                self.assertEqual(git_blob_sha((ROOT / old["archived"]).read_bytes()), old["sha"])
                self.assertFalse((ROOT / old["path"]).exists())
                self.assertNotIn(old["path"], MOD["chapters"])
        self.assertEqual(len(MANIFEST["legacy_chapters"]), 19)
        for moved in MANIFEST["moved_chapters"]:
            with self.subTest(path=moved["dest"]):
                self.assertFalse((ROOT / moved["src"]).exists())
                self.assertIn(moved["dest"], MOD["chapters"])
                self.assertNotIn(moved["src"], LST["chapters"])
                self.assertTrue((ROOT / moved["dest"]).is_file())

    def test_cross_book_labels_and_book_imports(self):
        paths = LST["chapters"] + MOD["chapters"]
        sources = [(ROOT / path).read_text("utf8") for path in paths]
        labels = [x for src in sources for x in LABEL.findall(src)]
        refs = {a or b for src in sources for a, b in REF.findall(src)}
        self.assertEqual(len(labels), len(set(labels)))
        self.assertFalse(refs - set(labels), refs - set(labels))
        for book in (LST, MOD):
            text = (ROOT / book["entrypoint"]).read_text("utf8")
            self.assertEqual(re.findall(r"\\input\{\.\./\.\./([^}]+)\}", text), book["chapters"])
        self.assertIn(str(FUZZY.relative_to(ROOT)), LST["chapters"])
        self.assertEqual([Path(p).name[:2] for p in MOD["chapters"][:9]],
                         ["24", "25", "26", "27", "28", "20", "21", "22", "23"])
        self.assertEqual(len(MANIFEST["moved_chapters"]), 9)

    def test_no_active_reference_to_archive_only_label(self):
        historical = {label for old in MANIFEST["legacy_chapters"]
                      for label in LABEL.findall((ROOT / old["archived"]).read_text("utf8"))}
        active_sources = [(path, path.read_text("utf8"))
                          for path in (ROOT / "chapters/pl").rglob("*.tex")]
        active_labels = {label for _, src in active_sources for label in LABEL.findall(src)}
        # A legacy-only target must not become dangling because of the migration.
        lost = historical - active_labels
        dangling = [(str(path.relative_to(ROOT)), a or b)
                    for path, src in active_sources for a, b in REF.findall(src)
                    if (a or b) in lost]
        self.assertFalse(dangling, dangling)

    def test_fuzzy_chapter_structure(self):
        src = FUZZY.read_text("utf8")
        self.assertIn(r"\label{ch:lst-fuzzy-logic}", src)
        self.assertIn(r"\label{thm:lst-fuzzy-residuation}", src)
        self.assertIn(r"\label{thm:lst-fuzzy-extension-cuts}", src)
        self.assertIn(r"\label{thm:lst-fuzzy-mcnaughton}", src)
        self.assertIn(r"\label{thm:lst-fuzzy-filter-quotient}", src)
        self.assertIn(r"\label{thm:lst-fuzzy-prime-separation}", src)
        self.assertIn(r"\label{thm:lst-fuzzy-strong-chain-completeness}", src)
        self.assertIn(r"\label{thm:lst-fuzzy-local-deduction}", src)
        self.assertIn(r"\label{eq:lst-fuzzy-syntactic-residuation}", src)
        self.assertIn(r"\label{eq:lst-fuzzy-syntactic-cases}", src)
        self.assertIn(r"\label{lem:lst-fuzzy-clipped-affine}", src)
        self.assertIn(r"\label{lem:lst-fuzzy-lattice-representation}", src)
        stack = []
        for kind, env in re.findall(r"\\(begin|end)\{([^}]+)\}", src):
            if kind == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack and stack.pop() == env, env)
        self.assertFalse(stack)


class TestFuzzyOperations(unittest.TestCase):
    grid = tuple(F(i, 8) for i in range(9))
    norms = (
        (min, lambda a, b: F(1) if a <= b else b),
        (lambda a, b: a*b, lambda a, b: F(1) if a <= b else b/a),
        (lambda a, b: max(F(0), a+b-1), lambda a, b: min(F(1), 1-a+b)),
    )

    def test_axioms_and_residuation(self):
        for t, implication in self.norms:
            for a, b, c in itertools.product(self.grid, repeat=3):
                self.assertEqual(t(a, F(1)), a)
                self.assertEqual(t(a, F(0)), 0)
                self.assertEqual(t(a, b), t(b, a))
                self.assertEqual(t(t(a, b), c), t(a, t(b, c)))
                self.assertEqual(t(a, c) <= b, c <= implication(a, b))
                self.assertEqual(t(a, implication(a, b)), min(a, b))
                if b <= c:
                    self.assertLessEqual(t(a, b), t(a, c))

    def test_triangular_sum_cuts(self):
        for alpha in self.grid[1:]:
            a = (1 + alpha, 4 - 2*alpha)
            b = (3*alpha, 5 - 2*alpha)
            self.assertEqual((a[0] + b[0], a[1] + b[1]),
                             (1 + 4*alpha, 9 - 4*alpha))

    def test_clipped_affine_recurrence(self):
        clip = lambda x: min(F(1), max(F(0), x))
        for m in range(1, 5):
            for ys in itertools.product(self.grid[::2], repeat=m):
                partial = sum(ys[:-1], F(0))
                for k in range(-1, m + 2):
                    first = clip(partial - k)
                    carry = max(F(0), clip(partial - k + 1) + ys[-1] - 1)
                    self.assertEqual(min(F(1), first + carry), clip(partial + ys[-1] - k))

    def test_mcnaughton_tent(self):
        for x in self.grid:
            self.assertEqual(min(min(F(1), 2*x), min(F(1), 2*(1-x))),
                             min(2*x, 2-2*x))

    def test_filter_quotient_finite_chains(self):
        for star, implication in (self.norms[0], self.norms[2]):
            grid = self.grid
            for threshold in grid:
                filt = {x for x in grid if x >= threshold}
                if any(star(x, y) not in filt for x in filt for y in filt):
                    continue
                eq = lambda a, b: implication(a, b) in filt and implication(b, a) in filt
                for a, b, c in itertools.product(grid, repeat=3):
                    self.assertEqual(eq(a, F(1)), a in filt)
                    self.assertEqual(eq(min(a, b), a), implication(a, b) in filt)
                    if eq(a, b):
                        for op in (min, max, star, implication):
                            self.assertTrue(eq(op(a, c), op(b, c)))
                            self.assertTrue(eq(op(c, a), op(c, b)))

    def test_filter_separation_product_of_boolean_chains(self):
        a = frozenset({0})
        b = frozenset({1})
        top = a | b
        grid = (frozenset(), a, b, top)
        filters = [{x for x in grid if g <= x} for g in grid]
        for filt in filters:
            for c in set(grid) - filt:
                candidates = [p for p in filters if filt <= p and c not in p]
                maximal = [p for p in candidates if not any(p < q for q in candidates)]
                self.assertTrue(maximal)
                for p in maximal:
                    for x, y in itertools.product(grid, repeat=2):
                        if x | y in p:
                            self.assertTrue(x in p or y in p)

    def test_mtl_case_rule_and_join(self):
        for star, implication in self.norms:
            for a, b, r in itertools.product(self.grid, repeat=3):
                join = min(implication(implication(a, b), b),
                           implication(implication(b, a), a))
                self.assertEqual(join, max(a, b))
                if implication(a, b) <= r and implication(b, a) <= r:
                    self.assertEqual(r, 1)
                self.assertEqual(implication(star(a, b), r),
                                 implication(a, implication(b, r)))

    def test_local_deduction_not_global(self):
        star, implication = self.norms[2]
        p = F(1, 2)
        self.assertEqual(implication(p, star(p, p)), F(1, 2))
        for p in self.grid:
            self.assertEqual(implication(star(p, p), star(p, p)), 1)

    def test_sugeno_zero_order(self):
        self.assertEqual(F(1, 4)*2 + F(3, 4)*6, 5)


if __name__ == "__main__":
    unittest.main()
