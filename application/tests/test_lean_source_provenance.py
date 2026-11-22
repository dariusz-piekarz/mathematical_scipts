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

    def test_binding_digest_tracks_owner_metadata_not_just_tex_bytes(self):
        first = provenance.indexed_binding(self.con, "LST-01", LABEL, "one")
        digest = provenance.binding_sha256("LST-01", LABEL, first)
        self.assertEqual(len(digest), 64)
        self.assertEqual(digest, provenance.binding_sha256("LST-01", LABEL, first))
        # Mutating indexed theorem metadata leaves source text unchanged.
        self.con.execute("UPDATE entities SET title='Alternative' WHERE id='one'")
        second = provenance.indexed_binding(self.con, "LST-01", LABEL, "one")
        self.assertNotEqual(digest,
                            provenance.binding_sha256("LST-01", LABEL, second))
        self.assertNotEqual(digest,
                            provenance.binding_sha256("LST-02", LABEL, first))
        self.assertNotEqual(digest,
                            provenance.binding_sha256("LST-01", "t:other", first))
        with self.assertRaises(ValueError):
            provenance.binding_sha256("LST-01", LABEL, ("incomplete",))

    def test_non_theorem_owner_cannot_inherit_formalization(self):
        for kind in ("section", "definition", "proof", "example", ""):
            with self.subTest(kind=kind):
                self.con.execute("UPDATE entities SET kind=? WHERE id='one'", (kind,))
                status, entity = provenance.owner_status(self.con, "LST-01", LABEL, SOURCE)
                self.assertEqual(status, "invalid_label_binding")
                self.assertIsNone(entity)
        self.con.execute("UPDATE entities SET kind='theorem' WHERE id='one'")
        self.assertEqual(provenance.owner_status(self.con, "LST-01", LABEL, SOURCE),
                         ("ok", "one"))

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
                self.con.execute(
                    "UPDATE labels SET offset=?", (candidate.index("\\label"),))
                self.con.execute(
                    "UPDATE entities SET start_line=1,end_line=?,end_offset=? "
                    "WHERE id='one'",
                    (candidate.count("\n", 0, len(candidate) - 1) + 1,
                     len(candidate)))
                binding = provenance.indexed_binding(
                    self.con, "LST-01", LABEL, "one")
                self.assertFalse(provenance.valid_binding(binding, candidate, LABEL))

    def test_single_conflict_disagreeing_with_primary_owner_is_ambiguous(self):
        for owner, offset in (("other-entity", self.offset),
                              ("one", self.offset + 1)):
            with self.subTest(owner=owner, offset=offset):
                self.con.execute("DELETE FROM label_conflicts")
                self.con.execute("INSERT INTO label_conflicts VALUES(?,?,?,?,?,?)", (
                    LABEL, "LST-01", owner, offset, 1, ""))
                self.assertEqual(
                    provenance.owner_status(self.con, "LST-01", LABEL, SOURCE),
                    ("ambiguous_label", None))
        self.con.execute("DELETE FROM label_conflicts")
        self.con.execute("INSERT INTO label_conflicts VALUES(?,?,?,?,?,?)", (
            LABEL, "LST-01", "one", self.offset, 1, ""))
        # The parser populates this table only after detecting a duplicate.
        # Even a matching conflict row therefore signals global ambiguity.
        self.assertEqual(provenance.owner_status(self.con, "LST-01", LABEL, SOURCE),
                         ("ambiguous_label", None))

    def test_cross_document_collision_blocks_primary_owner(self):
        # The real index stores conflicts globally, not only in this document.
        self.con.execute("INSERT INTO label_conflicts VALUES(?,?,?,?,?,?)", (
            LABEL, "LST-99", "outside", 5, 1, ""))
        self.assertEqual(
            provenance.owner_status(self.con, "LST-01", LABEL, SOURCE),
            ("ambiguous_label", None))

    def test_canonical_occurrences_reject_missing_mismatched_or_duplicate_owner(self):
        self.con.execute(
            "CREATE TABLE label_occurrences("
            "occurrence_id TEXT PRIMARY KEY, name TEXT, document_id TEXT, "
            "entity_id TEXT, line INTEGER, offset INTEGER, concept_id TEXT)")
        self.assertEqual(provenance.owner_status(self.con, "LST-01", LABEL, SOURCE),
                         ("invalid_label_binding", None))
        self.con.execute("INSERT INTO label_occurrences VALUES(?,?,?,?,?,?,?)",
                         ("native", LABEL, "LST-01", "one", 1, self.offset, None))
        self.assertEqual(provenance.owner_status(self.con, "LST-01", LABEL, SOURCE),
                         ("ok", "one"))
        for field, invalid in (
                ("document_id", "LST-02"), ("entity_id", "wrong"),
                ("offset", self.offset + 1)):
            with self.subTest(field=field):
                self.con.execute(f"UPDATE label_occurrences SET {field}=?",
                                 (invalid,))
                self.assertEqual(
                    provenance.owner_status(self.con, "LST-01", LABEL, SOURCE),
                    ("invalid_label_binding", None))
                self.con.execute(f"UPDATE label_occurrences SET {field}=?",
                                 ({"document_id":"LST-01", "entity_id":"one",
                                   "offset":self.offset}[field],))
        self.con.execute("INSERT INTO label_occurrences VALUES(?,?,?,?,?,?,?)",
                         ("other", LABEL, "LST-02", "other", 1, self.offset, None))
        self.assertEqual(provenance.owner_status(self.con, "LST-01", LABEL, SOURCE),
                         ("ambiguous_label", None))

    def test_same_offset_distinct_conflict_owners_are_ambiguous(self):
        self.con.execute("INSERT INTO label_conflicts VALUES(?,?,?,?,?,?)", (
            LABEL, "LST-01", "one", self.offset, 1, ""))
        self.con.execute("INSERT INTO label_conflicts VALUES(?,?,?,?,?,?)", (
            LABEL, "LST-01", "other-entity", self.offset, 1, ""))
        self.assertEqual(
            provenance.owner_status(self.con, "LST-01", LABEL, SOURCE),
            ("ambiguous_label", None))

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
