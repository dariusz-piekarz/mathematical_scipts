"""Regression tests for independent and registered LaTeX chapter assets."""
from pathlib import Path
import json
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from audit_chapter_dependencies import audit


class DependencyAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for directory in ("catalog", "books/pl", "chapters/pl/example", "shared/pl"):
            (self.root / directory).mkdir(parents=True, exist_ok=True)
        book = {"books": [{
            "id": "example",
            "entrypoint": "books/pl/example.tex",
            "chapters": ["chapters/pl/example/01-test.tex"],
        }]}
        (self.root / "catalog/books.json").write_text(json.dumps(book), encoding="utf-8")
        self.entry = self.root / "books/pl/example.tex"
        self.entry.write_text(r"\input{../../chapters/pl/example/01-test.tex}", encoding="utf-8")
        self.chapter = self.root / "chapters/pl/example/01-test.tex"
        self.chapter.write_text(r"\chapter{Test}", encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def test_self_contained_chapter(self):
        self.assertEqual(audit(self.root)["errors"], [])

    def test_missing_image_and_packaged_image(self):
        self.chapter.write_text(r"\includegraphics[width=.8\linewidth]{figures/a.png}")
        self.assertTrue(any("Missing asset" in x for x in audit(self.root)["errors"]))
        (self.root / "books/pl/figures").mkdir()
        (self.root / "books/pl/figures/a.png").write_bytes(b"placeholder")
        self.assertEqual(audit(self.root)["errors"], [])

    def test_inline_tikz_and_listing_are_self_contained(self):
        self.chapter.write_text(r"""
% \includegraphics{figures/old.png}
\begin{lstlisting}
\includegraphics{figures/not-a-dependency.png}
\end{lstlisting}
\begin{tikzpicture}
\draw (0,0)--(1,1);
\end{tikzpicture}
""")
        self.assertEqual(audit(self.root)["errors"], [])

    def test_unregistered_module_is_an_error(self):
        (self.root / "chapters/pl/example/02-extra.tex").write_text("x")
        self.assertTrue(any("Unregistered" in x for x in audit(self.root)["errors"]))

    def test_book_imports_are_checked(self):
        self.entry.write_text(r"\input{../../wrong.tex}")
        self.assertTrue(any("Entrypoint imports differ" in x for x in audit(self.root)["errors"]))

    def test_stale_registry_path_is_an_error(self):
        registry = {"canonical_modules": [{"sources": [{"path": "chapters/pl/example/99-old.tex"}]}]}
        (self.root / "catalog/topic_registry.json").write_text(json.dumps(registry))
        self.assertTrue(any("Stale registry" in x for x in audit(self.root)["errors"]))

    def test_optional_supplement_can_precede_chapters(self):
        data = json.loads((self.root / "catalog/books.json").read_text())
        supplement = "chapters/pl/example/supplements/notation.tex"
        (self.root / supplement).parent.mkdir(parents=True)
        (self.root / supplement).write_text("notation")
        data["books"][0]["supplements"] = [supplement]
        (self.root / "catalog/books.json").write_text(json.dumps(data))
        self.entry.write_text(
            r"\input{../../chapters/pl/example/supplements/notation.tex}" + "\n" +
            r"\input{../../chapters/pl/example/01-test.tex}"
        )
        self.assertEqual(audit(self.root)["errors"], [])


if __name__ == "__main__":
    unittest.main()
