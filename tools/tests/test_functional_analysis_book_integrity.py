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

DT_BOOK = ROOT / "books/pl/distribution_theory.tex"

def catalog():
    return json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))

def migration():
    return json.loads((ROOT / "catalog/distribution_theory_migration.json").read_text(encoding="utf-8"))

def dt_active():
    return any(b["id"] == "distribution_theory" for b in catalog()["books"])

def sources(master=BOOK):
    book = master.read_text(encoding="utf-8")
    paths = [(master.parent / p).resolve() for p in re.findall(r"\\input\{([^}]+)\}", book)]
    return book, paths, [p.read_text(encoding="utf-8") for p in paths]

def without_comments_and_code(s):
    s = re.sub(r"\\begin\{(?:lstlisting|verbatim)\}.*?\\end\{(?:lstlisting|verbatim)\}", "", s, flags=re.S)
    return re.sub(r"(?<!\\)%[^\n]*", "", s)

class FunctionalAnalysisBook(unittest.TestCase):
    def test_FA_BOOK_inventory_01(self):
        book, paths, texts = sources()
        expected = [i for i in IDS if not (dt_active() and i.isdigit()
                                          and 17 <= int(i) <= 25)]
        self.assertEqual([p.name.split("-")[0] for p in paths], expected)
        self.assertEqual(len(set(paths)), len(expected))
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
        external = set(re.findall(r"\\importDTreference\{([^}]+)\}", book))
        if dt_active():
            _, _, dt_texts = sources(DT_BOOK)
            dt_labels = {label for t in dt_texts for label in
                         re.findall(r"\\label\{([^}]+)\}", without_comments_and_code(t))}
            self.assertLessEqual(external, dt_labels)
            self.assertFalse(external.intersection(labels))
        else:
            self.assertFalse(external)
        self.assertFalse([(p,r) for p,r in refs if r not in labels and r not in external])
        proofs = sum(s.count(r"\begin{proof}") for s in all_sources)
        print(f"FA inventory: units={len(paths)}, unique_labels={len(labels)}, reference_occurrences={len(refs)}, proofs={proofs}")

    def test_FA_BOOK_terminology_02(self):
        _, paths, texts = sources()
        # Label and reference identifiers are intentionally preserved.
        forbidden = re.compile(
            r"zbieżnoś[ćc][^\n]{0,16}zdominowan|tensorowani|\bunia\b|"
            r"\bdual(?:u|em|owi|e|ach|ów)?\b|\\mathrm d\^3x|"
            r"przestrze(?:ń|ni|nie|nia|nią) (?:hilbertowsk|banachowsk)",
            re.IGNORECASE,
        )
        hits = []
        for path, source in zip(paths, texts):
            text = without_comments_and_code(source)
            text = re.sub(r"\\(?:label|ref|eqref|pageref|autoref)\{[^}]+\}|\\hyperref\[[^\]]+\]", "", text)
            # Atlas references also carry stable identifiers; retain their visible captions.
            text = re.sub(r"\\atlasref\{[^{}]+\}", "", text)
            hits.extend((path.name, m.group()) for m in forbidden.finditer(text))
        self.assertFalse(hits)

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

class DistributionTheoryBook(unittest.TestCase):
    def test_DT_inventory_and_references(self):
        manifest = migration()
        book, paths, texts = sources(DT_BOOK)
        key = "target_path" if dt_active() else "staged_path"
        self.assertEqual(paths, [(ROOT / c[key]).resolve()
                                 for c in manifest["chapters"]])
        self.assertEqual(len(set(paths)), 19)
        self.assertIn(r"\maketitle", book)
        self.assertIn(r"\tableofcontents", book)
        self.assertTrue(all(t.strip() for t in texts))
        labels = Counter()
        for chapter, path, text in zip(manifest["chapters"], paths, texts):
            clean = without_comments_and_code(text)
            current = re.findall(r"\\label\{([^}]+)\}", clean)
            self.assertLessEqual(set(chapter["labels"]), set(current), path)
            labels.update(current)
            stack = []
            for op, env in re.findall(r"\\(begin|end)\{([^}]+)\}", clean):
                if op == "begin":
                    stack.append(env)
                else:
                    self.assertTrue(stack, (path, env))
                    self.assertEqual(stack.pop(), env, path)
            self.assertFalse(stack, path)
        self.assertFalse({k: v for k, v in labels.items() if v > 1})
        external = set(re.findall(r"\\importFAreference\{([^}]+)\}", book))
        self.assertEqual(external, set(manifest["external_unqualified_labels"]))
        _, _, af_texts = sources()
        af_labels = {label for t in af_texts for label in
                     re.findall(r"\\label\{([^}]+)\}", without_comments_and_code(t))}
        self.assertLessEqual(external, af_labels)
        self.assertFalse(external.intersection(labels))
        seen = set(external)
        for path, text in zip(paths, texts):
            clean = without_comments_and_code(text)
            seen.update(re.findall(r"\\label\{([^}]+)\}", clean))
            refs = (re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}", clean)
                    + re.findall(r"\\hyperref\[([^\]]+)\]", clean))
            self.assertFalse(set(refs) - seen, (path, set(refs) - seen))


if __name__ == "__main__":
    unittest.main()
