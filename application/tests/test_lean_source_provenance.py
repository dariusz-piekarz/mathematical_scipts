"""Shared source provenance contract, independent of Lean subprocess execution."""
from __future__ import annotations

import sqlite3
import unittest

from backend import lean_source_provenance as provenance


SOURCE = "\\begin{twierdzenie}\\label{thm:test}\nP oraz Q.\n\\end{twierdzenie}\n"
LABEL = "thm:test"


class SourceProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(":memory:")
        self.addCleanup(self.con.close)
        self.con.row_factory = sqlite3.Row
        self.con.executescript("""
            CREATE TABLE entities(
                id TEXT, document_id TEXT, kind TEXT, title TEXT,
                start_line INTEGER, end_line INTEGER,
                start_offset INTEGER, end_offset INTEGER);
            CREATE TABLE labels(name TEXT, entity_id TEXT, offset INTEGER);
            CREATE TABLE label_conflicts(
                name TEXT, document_id TEXT, entity_id TEXT,
                offset INTEGER, line INTEGER, excerpt TEXT);
        """)
        self.con.execute("INSERT INTO entities VALUES(?,?,?,?,?,?,?,?)", (
            "one", "LST-01", "theorem", "Twierdzenie", 1, 3, 0, len(SOURCE)))
        self.offset = SOURCE.index("\\label")
        self.con.execute("INSERT INTO labels VALUES(?,?,?)", (LABEL, "one", self.offset))

    def test_registered_label_is_current_with_terminal_newline(self):
        status, entity = provenance.owner_status(self.con, "LST-01", LABEL, SOURCE)
        self.assertEqual((status, entity), ("ok", "one"))
        binding = provenance.indexed_binding(self.con, "LST-01", LABEL, "one")
        self.assertTrue(provenance.valid_binding(binding, SOURCE, LABEL))

    def test_shifted_label_offset_is_never_current(self):
        for offset in (self.offset + 1, self.offset - 1, len(SOURCE), -1, None):
            with self.subTest(offset=offset):
                self.con.execute("UPDATE labels SET offset=?", (offset,))
                status, entity = provenance.owner_status(self.con, "LST-01", LABEL, SOURCE)
                self.assertEqual(status, "invalid_label_binding")
                self.assertIsNone(entity)

    def test_label_inside_comment_and_verbatim_is_not_a_mapping(self):
        for candidate in (
            "% \\label{thm:test}\n",
            "\\begin{verbatim}\\label{thm:test}\\end{verbatim}\n",
            "\\verb+\\label{thm:test}+\n",
        ):
            with self.subTest(candidate=candidate):
                self.con.execute("UPDATE labels SET offset=0")
                self.con.execute(
                    "UPDATE entities SET start_line=1,end_line=? "
                    "WHERE id='one'", (candidate.count("\n") + 1,))
                binding = provenance.indexed_binding(
                    self.con, "LST-01", LABEL, "one")
                self.assertFalse(provenance.valid_binding(binding, candidate, LABEL))

    def test_missing_and_duplicate_owners_are_not_navigable(self):
        self.con.execute("DELETE FROM labels")
        self.assertEqual(
            provenance.owner_status(self.con, "LST-01", LABEL, SOURCE),
            ("unlinked_label", None))
        self.con.execute("INSERT INTO labels VALUES(?,?,?)", (LABEL, "one", self.offset))
        self.con.execute("INSERT INTO entities VALUES(?,?,?,?,?,?,?,?)", (
            "two", "LST-01", "theorem", "Inne", 1, 3, 0, len(SOURCE)))
        self.con.execute("INSERT INTO labels VALUES(?,?,?)", (LABEL, "two", self.offset))
        self.assertEqual(
            provenance.owner_status(self.con, "LST-01", LABEL, SOURCE),
            ("ambiguous_label", None))
        self.con.execute("DELETE FROM labels WHERE entity_id='two'")
        self.con.execute("INSERT INTO label_conflicts VALUES(?,?,?,?,?,?)", (
            LABEL, "LST-01", "one", self.offset, 1, ""))
        self.con.execute("INSERT INTO label_conflicts VALUES(?,?,?,?,?,?)", (
            LABEL, "LST-01", "two", self.offset + 1, 1, ""))
        self.assertEqual(
            provenance.owner_status(self.con, "LST-01", LABEL, SOURCE),
            ("ambiguous_label", None))


if __name__ == "__main__":
    unittest.main()
