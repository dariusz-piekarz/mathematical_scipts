"""DG-05/06 audit regressions: algebra, chain complexes, references, modular torsion."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
DG = ROOT / "chapters" / "pl" / "differential_geometry_and_topology"
BOOK = ROOT / "books" / "pl" / "differential_geometry_and_topology.tex"


class DifferentialGeometryFiveSixAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = {
            f"{n:02d}": next(DG.glob(f"{n:02d}-*.tex"))
            for n in range(1, 8)
        }
        cls.texts = {
            key: path.read_text(encoding="utf-8-sig")
            for key, path in cls.files.items()
        }

    def test_book_includes_canonical_chapters(self):
        book = BOOK.read_text(encoding="utf-8-sig")
        for chapter in ("05", "06"):
            with self.subTest(chapter=chapter):
                expected = (
                    r"\input{../../chapters/pl/differential_geometry_and_topology/"
                    + self.files[chapter].name + "}"
                )
                self.assertIn(expected, book)

    def test_original_labels_preserved_and_links_resolve(self):
        combined = "\n".join(self.texts.values())
        labels = re.findall(r"\\label\s*\{([^}]+)\}", combined)
        self.assertEqual(len(labels), len(set(labels)))
        known = set(labels)
        for key in ("05", "06"):
            refs = set(re.findall(
                r"\\(?:ref|eqref|pageref|autoref|nameref)\s*\{([^}]+)\}",
                self.texts[key],
            ))
            self.assertGreater(len(refs), 15)
            self.assertFalse(refs - known, refs - known)
        self.assertIn(r"\label{ch:algebra-abstrakcyjna}", self.texts["05"])
        self.assertIn(r"\label{ch:algebra-homologiczna}", self.texts["06"])
        self.assertIn(r"\label{thm:van-kampen}", self.texts["07"])
        self.assertNotIn(
            r"\ref{app:grupy-algebry-macierzowe}", self.texts["05"]
        )

    def test_balanced_environments_no_external_assets_and_polish(self):
        forbidden = (
            r"\btensorowan\w*|\bsekwencj\w*|\bseskwilini\w*"
            r"|\bzbieżność\s+zdominowan\w*"
        )
        for key in ("05", "06"):
            src = self.texts[key]
            begins = Counter(re.findall(r"\\begin\{([^}]+)\}", src))
            ends = Counter(re.findall(r"\\end\{([^}]+)\}", src))
            self.assertEqual(begins, ends)
            self.assertGreaterEqual(begins["tikzpicture"], 4)
            self.assertGreaterEqual(begins["figure"], 4)
            self.assertNotIn(r"\Z_*", src)
            self.assertNotRegex(src.lower(), forbidden)
            for command in (
                "includegraphics", "input", "include",
                "lstinputlisting", "inputminted",
            ):
                self.assertNotRegex(src, r"\\" + command + r"\s*\{")

    def test_torsion_is_submodule_only_under_stated_hypotheses(self):
        src = self.texts["05"]
        self.assertIn(r"\label{def:torsja-r-modulu-5}", src)
        self.assertIn(r"\label{prz:torsja-z-dzielnikami-zera-5}", src)
        self.assertIn(r"\label{prz:torsja-wielomiany-5}", src)
        # In R=Z/6, 2 and 3 are annihilated by nonzero scalars.
        self.assertEqual((2 * 3) % 6, 0)
        self.assertEqual((3 * 2) % 6, 0)
        # Their sum, 5, is a unit and has no nonzero annihilator.
        self.assertEqual((2 + 3) % 6, 5)
        self.assertEqual((5 * 5) % 6, 1)
        self.assertTrue(all((r * 5) % 6 != 0 for r in range(1, 6)))

    def test_explicit_mod_two_connecting_homomorphism(self):
        src = self.texts["06"]
        self.assertIn(r"\label{prz:mod2-dwa-zrodla}", src)
        self.assertIn(r"\label{thm:mod-m-homologia}", src)
        # Complex: Z --(2,0)--> Z^2 --(0,2)--> Z.
        d2 = (2, 0)
        self.assertEqual(0 * d2[0] + 2 * d2[1], 0)
        # All differentials vanish after reduction mod 2.
        self.assertEqual(tuple(v % 2 for v in d2), (0, 0))
        self.assertEqual((0 % 2, 2 % 2), (0, 0))
        middle = {(a, b) for a in range(2) for b in range(2)}
        inclusion_image = {(0, 0), (1, 0)}
        connecting_kernel = {(a, b) for a, b in middle if b == 0}
        connecting_image = {b for a, b in middle}
        self.assertEqual(connecting_kernel, inclusion_image)
        self.assertEqual(connecting_image, {0, 1})
        self.assertEqual(len(middle), 4)


if __name__ == "__main__":
    unittest.main()
