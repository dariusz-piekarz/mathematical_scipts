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
NCL = BY_ID["nonclassical_logic"]
FUZZY = ROOT / "chapters/pl/nonclassical_logic/01-logika-rozmyta-i-zbiory-rozmyte.tex"
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
        paths = LST["chapters"] + MOD["chapters"] + NCL["chapters"]
        sources = [(ROOT / path).read_text("utf8") for path in paths]
        labels = [x for src in sources for x in LABEL.findall(src)]
        refs = {a or b for src in sources for a, b in REF.findall(src)}
        self.assertEqual(len(labels), len(set(labels)))
        self.assertFalse(refs - set(labels), refs - set(labels))
        for book in (LST, MOD, NCL):
            text = (ROOT / book["entrypoint"]).read_text("utf8")
            self.assertEqual(re.findall(r"\\input\{\.\./\.\./([^}]+)\}", text), book["chapters"])
        self.assertIn(str(FUZZY.relative_to(ROOT)), NCL["chapters"])
        self.assertNotIn(str(FUZZY.relative_to(ROOT)), LST["chapters"])
        self.assertFalse((ROOT / "chapters/pl/logic_and_set_theory/40-logika-rozmyta-i-zbiory-rozmyte.tex").exists())
        self.assertEqual(MANIFEST["nonclassical_logic_move"]["dest"], str(FUZZY.relative_to(ROOT)))
        self.assertTrue((ROOT / "application/config/preambles/NCL.tex").is_file())
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
        self.assertIn(r"\label{thm:lst-fuzzy-equivalence-cuts}", src)
        self.assertIn(r"\label{prop:lst-fuzzy-quantifier-laws}", src)
        self.assertIn(r"\label{ex:lst-fuzzy-mamdani-centroid}", src)
        self.assertIn(r"\label{ex:lst-fuzzy-sugeno-comparison}", src)
        self.assertIn(r"\label{thm:lst-fuzzy-transitive-closure}", src)
        self.assertIn(r"\label{prop:lst-fuzzy-interval-arithmetic}", src)
        self.assertIn(r"\label{thm:lst-fuzzy-mtl-standard}", src)
        self.assertIn(r"\label{thm:lst-fuzzy-godel-standard}", src)
        self.assertIn(r"\label{thm:lst-fuzzy-finite-standard}", src)
        self.assertIn(r"\label{thm:lst-fuzzy-bl-ordinal-decomposition}", src)
        self.assertIn(r"\label{lem:lst-fuzzy-finite-ordinal-tnorm}", src)
        self.assertIn(r"\label{thm:lst-fuzzy-bl-finite-countermodel}", src)
        self.assertIn(r"\label{lem:lst-fuzzy-ordered-linear-transfer}", src)
        self.assertIn(r"\label{thm:lst-fuzzy-mv-rational-countermodel}", src)
        self.assertIn(r"\label{thm:lst-fuzzy-product-finite-countermodel}", src)
        self.assertIn(r"\label{thm:lst-fuzzy-bl-noncompactness}", src)
        self.assertIn(r"\label{def:lst-fuzzy-product-logic}", src)
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

    def test_product_axioms_and_cancellation(self):
        star, implication = self.norms[1]
        neg = lambda a: implication(a, F(0))
        for a, b, c in itertools.product(self.grid, repeat=3):
            self.assertEqual(implication(min(a, neg(a)), F(0)), 1)
            inner = implication(implication(star(a, c), star(b, c)),
                                implication(a, b))
            self.assertEqual(implication(neg(neg(c)), inner), 1)
            if c > 0:
                self.assertEqual(star(a, c) <= star(b, c), a <= b)

    def test_bl_noncompact_finite_witnesses(self):
        for n in range(1, 21):
            a = F(1, 2)
            b = 1 - F(1, 2*n)
            for star, implication in self.norms[1:]:
                power = F(1)
                for k in range(1, n+1):
                    power = star(power, b)
                    self.assertEqual(implication(a, power), 1)
                self.assertLess(implication(a, star(a, b)), 1)

    def test_godel_order_embeddings_preserve_operations(self):
        star, implication = self.norms[0]
        embedding = {x: x*x for x in self.grid}
        for a, b in itertools.product(self.grid, repeat=2):
            for op in (min, max, star, implication):
                self.assertEqual(embedding[op(a, b)],
                                 op(embedding[a], embedding[b]))

    def test_fuzzy_equivalence_and_thresholds(self):
        r = ((F(1), F(4,5), F(3,10), F(3,10)),
             (F(4,5), F(1), F(3,10), F(3,10)),
             (F(3,10), F(3,10), F(1), F(3,5)),
             (F(3,10), F(3,10), F(3,5), F(1)))
        for i,j,k in itertools.product(range(4), repeat=3):
            self.assertLessEqual(min(r[i][j], r[j][k]), r[i][k])
            for alpha in (F(3,10), F(3,5), F(4,5), F(1)):
                if r[i][j] >= alpha and r[j][k] >= alpha:
                    self.assertGreaterEqual(r[i][k], alpha)
        self.assertEqual(F(1,2)*F(1,2), F(1,4))
        self.assertLess(F(1,4), F(1,2))

    def test_fuzzy_transitive_closure(self):
        r = ((F(1), F(4,5), F(1,5)),
             (F(4,5), F(1), F(3,5)),
             (F(1,5), F(3,5), F(1)))
        def compose(a,b):
            return tuple(tuple(max(min(a[i][k], b[k][j]) for k in range(3))
                               for j in range(3)) for i in range(3))
        r2 = compose(r,r)
        self.assertEqual(r2[0][2], F(3,5))
        self.assertEqual(compose(r2,r2), r2)
        for i,j in itertools.product(range(3), repeat=2):
            self.assertGreaterEqual(r2[i][j], r[i][j])

    def test_interval_arithmetic_and_dependence(self):
        for alpha in self.grid[1:]:
            a = (1+alpha, 4-2*alpha)
            b = (3*alpha, 5-2*alpha)
            self.assertEqual((a[0]-b[1], a[1]-b[0]), (-4+3*alpha, 4-5*alpha))
            self.assertEqual((a[0]-a[1], a[1]-a[0]), (-3+3*alpha, 3-3*alpha))
        for a,b in itertools.product(((-3,-1), (-2,4), (1,5)), repeat=2):
            corners = [F(x*y) for x,y in itertools.product(a,b)]
            for i,j in itertools.product(range(9), repeat=2):
                x = F(a[0]) + F(i,8)*(a[1]-a[0])
                y = F(b[0]) + F(j,8)*(b[1]-b[0])
                self.assertLessEqual(min(corners), x*y)
                self.assertLessEqual(x*y, max(corners))
                if b[0]*b[1] > 0:
                    quot = [F(u,v) for u,v in itertools.product(a,b)]
                    self.assertLessEqual(min(quot), x/y)
                    self.assertLessEqual(x/y, max(quot))

    def test_fuzzy_quantifier_laws(self):
        for star, implication in self.norms:
            for a,b,c in itertools.product(self.grid, repeat=3):
                self.assertEqual(star(c,max(a,b)), max(star(c,a),star(c,b)))
                self.assertEqual(implication(c,min(a,b)),
                                 min(implication(c,a),implication(c,b)))
                self.assertEqual(implication(max(a,b),c),
                                 min(implication(a,c),implication(b,c)))
        r = ((F(1),F(1,4)),(F(1,2),F(3,4)))
        self.assertEqual(min(map(max,r)),F(3,4))
        self.assertEqual(max(map(min,zip(*r))),F(1,2))

    def test_mamdani_centroid(self):
        def area(w):
            return 4*w-2*w*w
        a,b = area(F(1,4)),area(F(3,4))
        self.assertEqual((a,b),(F(7,8),F(15,8)))
        self.assertEqual((2*a+6*b)/(a+b),F(52,11))
        for x in self.grid:
            a,b = area(1-x),area(x)
            m = (2*a+6*b)/(a+b)
            self.assertEqual(m,(2*(1-x*x)+6*(2*x-x*x))/(1+2*x-2*x*x))
            self.assertLessEqual(2,m)
            self.assertLessEqual(m,6)
            self.assertEqual((2*(1-x)+6*x),2+4*x)

    def test_finite_mv_rational_countermodels(self):
        for n in range(1, 21):
            grid = [F(i,n) for i in range(n+1)]
            star, implication = self.norms[2]
            for a,b in itertools.product(grid, repeat=2):
                for op in (min,max,star,implication):
                    self.assertIn(op(a,b),grid)

    def test_product_group_exponents(self):
        star, implication = self.norms[1]
        for x,y in itertools.product(range(-8,1), repeat=2):
            a,b = F(2)**x,F(2)**y
            self.assertEqual(star(a,b),F(2)**(x+y))
            self.assertEqual(implication(a,b),F(2)**min(0,y-x))
            self.assertEqual(implication(a,F(0)),0)
            self.assertEqual(implication(F(0),b),1)

    def test_finite_lexicographic_constraints(self):
        # The full lexicographic group is not Archimedean, but finite
        # inequalities n*epsilon < unit admit rational realizations.
        for n in range(1, 50):
            u, eps = F(1), F(1,n+1)
            self.assertGreater(eps,0)
            self.assertTrue(all(k*eps<u for k in range(1,n+1)))

    def test_ordinal_sum_tnorm(self):
        intervals = [(F(0),F(1,3),self.norms[2]),
                     (F(1,2),F(5,6),self.norms[1])]
        def star(a,b):
            for l,r,(op,_) in intervals:
                if l <= a <= r and l <= b <= r:
                    return l+(r-l)*op((a-l)/(r-l),(b-l)/(r-l))
            return min(a,b)
        def imp(a,b):
            if a <= b:
                return F(1)
            for l,r,(_,op) in intervals:
                if l <= b < a <= r:
                    return l+(r-l)*op((a-l)/(r-l),(b-l)/(r-l))
            return b
        grid = tuple(F(i,12) for i in range(13))
        for a,b,c in itertools.product(grid, repeat=3):
            self.assertEqual(star(star(a,b),c),star(a,star(b,c)))
            self.assertEqual(star(a,c) <= b,c <= imp(a,b))
            self.assertEqual(star(a,imp(a,b)),min(a,b))
        self.assertEqual(star(F(2,3),F(2,3)),F(7,12))
        self.assertEqual(imp(F(2,3),F(1,4)),F(1,4))

    def test_sugeno_zero_order(self):
        self.assertEqual(F(1, 4)*2 + F(3, 4)*6, 5)


if __name__ == "__main__":
    unittest.main()
