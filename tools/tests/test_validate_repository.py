"""Regression checks for executable imports and immutable source provenance."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import validate_repository as validator


class RepositoryValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for directory in ("books/pl", "chapters/pl", "sources/pl", "catalog"):
            (self.root / directory).mkdir(parents=True)
        self.root_patch = patch.object(validator, "ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)

    def test_comments_and_verbatim_do_not_create_dependencies(self):
        (self.root / "books/pl/test.tex").write_text(
            r"\input{../../chapters/pl/test.tex}" + "\n"
            + r"% \input{missing-book.tex}", encoding="utf-8")
        chapter = self.root / "chapters/pl/test.tex"
        chapter.write_text(
            r"% \input{missing-comment.tex}" + "\n"
            + r"\begin{verbatim}" + "\n" + r"\input{missing-code.tex}"
            + "\n" + r"\end{verbatim}", encoding="utf-8")
        self.assertEqual(validator.validate_books(), [])
        with chapter.open("a", encoding="utf-8") as f:
            f.write("\n" + r"\input{missing-real.tex}")
        self.assertEqual(len(validator.validate_books()), 1)
        self.assertIn("missing-real.tex", validator.validate_books()[0])

    def make_archive(self):
        original = "Original chapter\n"
        entries = []
        for i in range(1, 21):
            source = f"sources/pl/{i}.tex"
            canonical = f"chapters/pl/{i}.tex"
            (self.root / source).write_bytes(original.encode("utf-8"))
            (self.root / canonical).write_text("Revised canonical chapter\n", encoding="utf-8")
            entries.append({
                "source": f"{i}.tex", "source_copy": source,
                "canonical_path": canonical,
                "repository_normalized_sha256": hashlib.sha256(original.encode("utf-8")).hexdigest(),
                "repository_normalized_characters": len(original),
            })
        (self.root / "catalog/new_chapters.json").write_text(json.dumps(entries), encoding="utf-8")

    def test_canonical_edits_do_not_invalidate_original_import(self):
        self.make_archive()
        self.assertEqual(validator.validate_attachments(), [])

    def test_archived_source_tampering_is_detected(self):
        self.make_archive()
        (self.root / "sources/pl/1.tex").write_text("Changed original\n", encoding="utf-8")
        errors = validator.validate_attachments()
        self.assertTrue(any("SHA-256 mismatch" in error for error in errors))

    def test_missing_canonical_source_is_detected(self):
        self.make_archive()
        (self.root / "chapters/pl/1.tex").unlink()
        self.assertTrue(any("Missing canonical" in error for error in validator.validate_attachments()))


if __name__ == "__main__":
    unittest.main()
