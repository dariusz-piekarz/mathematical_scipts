"""Cross-file regression checks for the canonical Polish measure theory book.

This is a structural/source audit; successful tests do not certify the
mathematical proofs, rendering, or completion of GitHub Actions.
Run: python -m unittest tools.tests.test_measure_theory_book_integrity -v
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MASTER = ROOT / "books/pl/measure_theory.tex"
PREFIX = "../../chapters/pl/measure_theory/"


def without_comments(source):
    """Remove TeX comments while preserving escaped percentage signs."""
    lines = []
    for line in source.splitlines():
        for i, char in enumerate(line):
            if char != "%":
                continue
            slash_count = 0
            j = i - 1
            while j >= 0 and line[j] == "\\":
                slash_count += 1
                j -= 1
            if slash_count % 2 == 0:
                line = line[:i]
                break
        lines.append(line)
    return "\n".join(lines)


def imported_sources():
    master = without_comments(MASTER.read_text(encoding="utf-8"))
    imported = re.findall(r"\\input\{([^{}]+)\}", master)
    paths = [MASTER.parent / value for value in imported if value.startswith(PREFIX)]
    return [path.resolve() for path in paths]


def corpus():
    return {
        path: without_comments(path.read_text(encoding="utf-8"))
        for path in imported_sources()
    }


class TestMeasureTheoryBookIntegrity(unittest.TestCase):
    def test_book_imports_exactly_31_ordered_chapters_and_two_supplements(self):
        paths = imported_sources()
        self.assertEqual(len(paths), 33)
        chapters = [path for path in paths if re.match(r"\d{2}-", path.name)]
        self.assertEqual(len(chapters), 31)
        self.assertEqual([path.name[:2] for path in chapters], [f"{n:02}" for n in range(1, 32)])
        self.assertEqual(len(set(paths)), len(paths))
        for path in paths:
            self.assertTrue(path.is_file(), f"Missing imported TeX source: {path}")
        for path in chapters:
            text = without_comments(path.read_text(encoding="utf-8"))
            self.assertEqual(
                len(re.findall(r"\\chapter(?:\[[^\]]*\])?\{", text)), 1,
                f"Expected exactly one chapter declaration: {path.name}",
            )

    def test_all_labels_unique_and_all_direct_references_resolve(self):
        sources = corpus()
        labels = {}
        for path, body in sources.items():
            for m in re.finditer(r"\\label\{([^{}]+)\}", body):
                label = m.group(1)
                self.assertNotIn(
                    label, labels,
                    f"Duplicate label {label!r}: {labels.get(label)} and {path.name}",
                )
                labels[label] = path.name
        self.assertGreaterEqual(len(labels), 300)
        refs = []
        for path, body in sources.items():
            for m in re.finditer(r"\\(?:ref|eqref|pageref|autoref|nameref|cref|Cref)\*?\{([^{}]+)\}", body):
                refs.extend((path.name, name.strip()) for name in m.group(1).split(","))
            for m in re.finditer(r"\\hyperref\[([^\]]+)\]", body):
                refs.append((path.name, m.group(1)))
        self.assertGreaterEqual(len(refs), 300)
        missing = [(path, name) for path, name in refs if name not in labels]
        self.assertFalse(missing, f"Unresolved direct cross-references: {missing[:30]!r}")

    def test_latex_environments_and_characteristic_function_notation(self):
        for path, body in corpus().items():
            stack = []
            for m in re.finditer(r"\\(begin|end)\{([^{}]+)\}", body):
                if m.group(1) == "begin":
                    stack.append(m.group(2))
                else:
                    self.assertTrue(stack, f"Unmatched end in {path.name}: {m.group(2)}")
                    self.assertEqual(stack.pop(), m.group(2), f"Environment nesting in {path.name}")
            self.assertEqual(stack, [], f"Open environments in {path.name}: {stack!r}")
            self.assertNotRegex(body, r"\\(?:mathbf|mathbb)\{1\}_", f"Use chi_A in {path.name}")

    def test_chapter_15_cross_dependencies(self):
        sources = corpus()
        chapter_14 = next(body for path, body in sources.items() if path.name.startswith("14-"))
        chapter_15 = next(body for path, body in sources.items() if path.name.startswith("15-"))
        labels_14 = set(re.findall(r"\\label\{([^{}]+)\}", chapter_14))
        labels_15 = set(re.findall(r"\\label\{([^{}]+)\}", chapter_15))
        refs_15 = set(re.findall(r"\\(?:ref|eqref)\{([^{}]+)\}", chapter_15))
        expected = {"ch:przestrzenie-lp", "thm:holder-14", "thm:riesz-fischer-14"}
        self.assertEqual(refs_15 - labels_15, expected)
        self.assertTrue(expected.issubset(labels_14))
        self.assertEqual(len(labels_15), 17)


if __name__ == "__main__":
    unittest.main()
