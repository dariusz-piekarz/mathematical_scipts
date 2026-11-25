"""Structural regressions for the actual functional-analysis book, not a proof checker."""
from collections import Counter
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
BOOK = ROOT / "books/pl/functional_analysis.tex"
CHAPTERS = ROOT / "chapters/pl/functional_analysis"
IDS = [f"{i:02d}" for i in range(1, 16)] + ["15A", "15B"] + [f"{i:02d}" for i in range(16, 34)]

def sources():
    book = BOOK.read_text(encoding="utf-8")
    paths = [(BOOK.parent / p).resolve() for p in re.findall(r"\\input\{([^}]+)\}", book)]
    return book, paths, [p.read_text(encoding="utf-8") for p in paths]

def without_comments_and_code(s):
    s = re.sub(r"\\begin\{(?:lstlisting|verbatim)\}.*?\\end\{(?:lstlisting|verbatim)\}", "", s, flags=re.S)
    return re.sub(r"(?<!\\)%[^\n]*", "", s)

class FunctionalAnalysisBook(unittest.TestCase):
    def test_FA_BOOK_inventory_01(self):
        book, paths, texts = sources()
        self.assertEqual([p.name.split("-")[0] for p in paths], IDS)
        self.assertEqual(len(set(paths)), 35)
        self.assertEqual(set(paths), set(CHAPTERS.glob("*.tex")))
        self.assertIn(r"\maketitle", book)
        self.assertIn(r"\tableofcontents", book)
        self.assertTrue(all(t.strip() for t in texts))
        tests = ROOT / "tools/tests"
        for identifier in IDS:
            self.assertTrue((tests / f"test_functional_analysis_ch{identifier.lower()}.py").is_file())

    def test_FA_BOOK_catalog_01(self):
        def walk(value):
            if isinstance(value, dict):
                if value.get("id") == "functional_analysis":
                    yield value
                for item in value.values():
                    yield from walk(item)
            elif isinstance(value, list):
                for item in value:
                    yield from walk(item)
        entries = list(walk(json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))))
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["entrypoint"], "books/pl/functional_analysis.tex")

    def test_FA_BOOK_references_01(self):
        book, paths, texts = sources()
        all_sources = [without_comments_and_code(s) for s in [book, *texts]]
        labels = Counter(label for s in all_sources for label in re.findall(r"\\label\{([^}]+)\}", s))
        self.assertFalse({k:v for k,v in labels.items() if v > 1})
        refs = [(str(p), ref) for p,s in zip([BOOK,*paths],all_sources)
                for ref in re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}",s)
                + re.findall(r"\\hyperref\[([^\]]+)\]",s)]
        self.assertFalse([(p,r) for p,r in refs if r not in labels])
        print(f"FA inventory: units={len(paths)}, unique_labels={len(labels)}, reference_occurrences={len(refs)}, proofs={sum(s.count(r'\begin{proof}') for s in all_sources)}")

    def test_FA_BOOK_environments_01(self):
        book, paths, texts = sources()
        for path,s in zip([BOOK,*paths],[book,*texts]):
            stack = []
            for op,env in re.findall(r"\\(begin|end)\{([^}]+)\}",without_comments_and_code(s)):
                if op == "begin":
                    stack.append(env)
                else:
                    self.assertTrue(stack, (path,env))
                    self.assertEqual(stack.pop(),env,path)
            self.assertFalse(stack,path)

if __name__ == "__main__":
    unittest.main()
