"""Global integration checks for algebraic geometry TeX sources."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTERS = sorted((ROOT / "chapters/pl/algebraic_geometry").glob("*.tex"))
MONOLITH = ROOT / "sources/pl/geometria_algebraiczna(1).tex"
SHARED = [
    ROOT / "shared/pl/rozdmuchanie_punktu_normalna.tex",
    ROOT / "shared/pl/slabe_twierdzenie_lefschetza.tex",
    ROOT / "shared/pl/rozdmuchanie_punktu_kohomologia.tex",
]


class ALGGlobalIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chapters = [p.read_text(encoding="utf-8") for p in CHAPTERS]
        cls.monolith = MONOLITH.read_text(encoding="utf-8")

    def test_monolith_matches_all_canonical_chapters(self):
        self.assertEqual([int(p.name[:2]) for p in CHAPTERS], list(range(11)))
        self.assertEqual(self.monolith.count(r"\chapter{"), 11)
        starts = []
        for i, source in enumerate(self.chapters):
            section = source.rstrip()
            title = section.splitlines()[0]
            with self.subTest(chapter=i):
                self.assertEqual(self.monolith.count(title), 1)
                start = self.monolith.index(title)
                starts.append(start)
                self.assertEqual(self.monolith[start:start + len(section)], section)
        self.assertEqual(starts, sorted(starts))
        self.assertTrue(self.monolith.rstrip().endswith(r"\end{document}"))

    def test_labels_and_references_in_all_chapters_and_shared_modules(self):
        all_text = "\n".join(self.chapters + [
            p.read_text(encoding="utf-8") for p in SHARED
        ])
        labels = re.findall(r"\\label\{([^}]+)\}", all_text)
        references = re.findall(
            r"\\(?:eqref|ref|autoref|pageref|cref|Cref)\{([^}]+)\}",
            all_text,
        )
        self.assertEqual(len(labels), len(set(labels)))
        self.assertEqual(len(labels), 406)
        self.assertFalse(set(references) - set(labels))

    def test_shared_dependencies_and_labels_in_monolith(self):
        active = "\n".join(self.chapters)
        for p in SHARED:
            self.assertIn(r"\input{../../shared/pl/" + p.name + "}", active)
        labels = lambda text: set(re.findall(r"\\label\{([^}]+)\}", text))
        self.assertEqual(labels(active), labels(self.monolith))


if __name__ == "__main__":
    unittest.main()
