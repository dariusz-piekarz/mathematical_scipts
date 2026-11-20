"""Regression gates for AT/DG/AG dependency integrity.

Cross-book collisions are recorded for mathematical review, not renamed.
"""
from __future__ import annotations

import unittest
from pathlib import Path
import sys

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from audit_cross_volume_geometry_topology import audit, strip_tex_comments


class CrossVolumeAuditTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = audit()

    def test_comments_exclude_phantom_labels_but_not_escaped_percent(self):
        src = (
            "a \\label{actual} % \\label{phantom}\n"
            "b \\% visible \\ref{actual} % \\ref{phantom}\n"
        )
        clean = strip_tex_comments(src)
        self.assertIn(r"\label{actual}", clean)
        self.assertIn(r"\ref{actual}", clean)
        self.assertNotIn(r"\label{phantom}", clean)
        self.assertNotIn(r"\ref{phantom}", clean)
        self.assertIn(r"\%", clean)

    def test_canonical_volumes_are_independent_and_complete_to_imported_scope(self):
        info = self.report["summary"]
        self.assertEqual(info["chapters"], {"AT": 30, "DG": 20, "AG": 11})
        self.assertEqual(set(self.report["volumes"]), {"AT", "DG", "AG"})

    def test_shared_math_sources_are_reused_by_path_not_copied(self):
        shared = self.report["shared_source_reuse"]
        self.assertEqual(set(shared), {
            "shared/pl/slabe_twierdzenie_lefschetza.tex",
            "shared/pl/rozdmuchanie_punktu_normalna.tex",
            "shared/pl/rozdmuchanie_punktu_kohomologia.tex",
        })
        # AT and AG source books have the same shared proofs and historic labels.
        for value in shared.values():
            self.assertEqual(value, ["AG", "AT"])
        conflicts = self.report["cross_volume_conflicts"]
        conflict_names = {item["label"] for item in conflicts}
        for protected in (
            "tw:ga10-weak", "thm:xvii-weak-lefschetz",
            "st:ga6-exceptional-normal", "lem:xvii-exceptional",
            "tw:ga10-blowup", "thm:xvii-blowup",
        ):
            self.assertNotIn(protected, conflict_names)

    def test_all_collisions_report_distinct_source_owners(self):
        for item in self.report["cross_volume_conflicts"]:
            self.assertGreater(len(set(item["source_files"])), 1)
            self.assertEqual(item["status"],
                             "requires_manual_mathematical_disambiguation")

    def test_review_pairs_cover_the_intersection_of_all_three_volumes(self):
        pairs = {(x["left"], x["right"]) for x in
                 self.report["overlap_candidates"]}
        for item in (
            ("AT-02", "DG-05"), ("AT-03", "DG-06"),
            ("AT-09", "DG-10"), ("AT-28", "AG-10"),
            ("AT-28", "AG-09"), ("AT-30", "DG-01"),
            ("AT-30", "DG-15"), ("AT-30", "DG-16"),
        ):
            self.assertIn(item, pairs)
        for item in self.report["overlap_candidates"]:
            self.assertEqual(item["decision"],
                             "review_and_preserve_union_of_unique_content")

    def test_no_external_unknown_label_is_claimed_resolved(self):
        for name, volume in self.report["volumes"].items():
            for item in volume["unresolved_references"]:
                self.assertEqual(item["external_candidates"], [])
                self.assertIn(item["status"],
                              ("not_in_imported_DG_scope",
                               "missing_in_three_imported_volumes"))
            for item in volume["unlinked_external_references"]:
                self.assertTrue(item["external_candidates"])
                self.assertIn(item["status"],
                              ("external_unique_unlinked",
                               "external_ambiguous_unlinked"))
        # This scope intentionally excludes 16 not-yet-imported DG chapters.
        self.assertEqual(self.report["policy"]["rename_labels"], False)
        self.assertFalse(self.report["policy"]
                         ["same_label_different_files_implies_same_theorem"])


if __name__ == "__main__":
    unittest.main()
