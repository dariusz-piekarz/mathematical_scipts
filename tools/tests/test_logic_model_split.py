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

    def test_sugeno_zero_order(self):
        self.assertEqual(F(1, 4)*2 + F(3, 4)*6, 5)


if __name__ == "__main__":
    unittest.main()
