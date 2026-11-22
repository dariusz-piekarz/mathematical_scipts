"""Deterministic version identities for kernel-derived Lean constant references.

These are synthetic protocol fixtures, not actual kernel execution evidence.
"""
from __future__ import annotations

import unittest

from backend import lean_inspection_snapshot as snapshots


def fingerprint() -> dict[str, str]:
    return {**{
        key: (str(i % 10) * 64)
        for i, key in enumerate(snapshots.DIGEST_FIELDS)
    }, "declared_toolchain": "leanprover/lean4:v4.26.0"}


class LeanInspectionSnapshotTests(unittest.TestCase):
    def describe(self, **updates):
        opts = {
            "identifier": "registration-one",
            "names": ["thmB", "thmA"],
            "classified": True,
            "fingerprint": fingerprint(),
            "constants": {"thmA": ["Nat.zero", "Eq"], "thmB": []},
            "type_constants": {"thmA": ["Eq"], "thmB": []},
            "value_constants": {"thmA": ["Nat.zero"], "thmB": []},
        }
        opts.update(updates)
        return snapshots.describe(**opts)

    def test_same_environment_and_references_same_id_despite_order(self):
        first = self.describe()
        second = self.describe(
            names=["thmA", "thmB"],
            constants={"thmB": [], "thmA": ["Eq", "Nat.zero"]},
            type_constants={"thmB": [], "thmA": ["Eq"]},
            value_constants={"thmB": [], "thmA": ["Nat.zero"]})
        self.assertEqual(first["inspection_snapshot_sha256"],
                         second["inspection_snapshot_sha256"])
        self.assertEqual(first["inspection_schema_version"], 1)
        self.assertEqual(first["inspection_provenance"], fingerprint())
        self.assertRegex(first["inspection_snapshot_sha256"], r"^[0-9a-f]{64}$")

    def test_identity_changes_for_every_environment_dependency(self):
        reference = self.describe()["inspection_snapshot_sha256"]
        for field in snapshots.DIGEST_FIELDS:
            with self.subTest(field=field):
                alternate = fingerprint()
                alternate[field] = "f" * 64 if alternate[field] != "f" * 64 else "e" * 64
                self.assertNotEqual(reference, self.describe(
                    fingerprint=alternate)["inspection_snapshot_sha256"])
        self.assertNotEqual(reference, self.describe(
            fingerprint={**fingerprint(), "declared_toolchain": "other"})[
                "inspection_snapshot_sha256"])

    def test_mode_type_value_and_result_affect_identity(self):
        baseline = self.describe()["inspection_snapshot_sha256"]
        unclassified = snapshots.describe(
            "registration-one", ["thmA", "thmB"], classified=False,
            fingerprint=fingerprint(),
            constants={"thmA": ["Eq", "Nat.zero"], "thmB": []})
        self.assertNotEqual(baseline, unclassified["inspection_snapshot_sha256"])
        different_type = self.describe(
            type_constants={"thmA": ["Nat.zero"], "thmB": []},
            value_constants={"thmA": ["Eq"], "thmB": []})
        self.assertNotEqual(baseline, different_type["inspection_snapshot_sha256"])
        self.assertNotEqual(baseline, self.describe(
            identifier="registration-two")["inspection_snapshot_sha256"])
        self.assertNotEqual(baseline, self.describe(
            constants={"thmA": ["Eq", "Nat.zero"], "thmB": ["Eq"]},
            type_constants={"thmA": ["Eq"], "thmB": ["Eq"]})[
                "inspection_snapshot_sha256"])

    def test_fails_closed_for_missing_or_inconsistent_evidence(self):
        valid = self.describe()
        self.assertEqual(valid["inspection_schema_version"], 1)
        invalid_cases = (
            {"fingerprint": {"source_document_sha256": "a" * 64}},
            {"fingerprint": {**fingerprint(), "source_binding_sha256": "broken"}},
            {"fingerprint": {**fingerprint(), "declared_toolchain": ""}},
            {"fingerprint": {**fingerprint(), "declared_toolchain": "  "}},
            {"fingerprint": {**fingerprint(), "declared_toolchain": "lean\\nforged"}},
            {"fingerprint": {**fingerprint(), "declared_toolchain": "lean\x00forged"}},
            {"constants": {"thmA": ["Eq", "Eq"], "thmB": []}},
            {"constants": {"thmA": ["Eq"], "thmB": []}},
            {"type_constants": {"thmA": ["Eq"], "thmB": ["Nat.zero"]}},
            {"names": ["thmA", "thmA"]},
            {"names": ["thmA", ["unhashable"]]},
            {"names": []},
            {"identifier": "../unsafe"},
            {"classified": 1},
        )
        for changes in invalid_cases:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.describe(**changes)
        with self.assertRaises(ValueError):
            snapshots.describe(
                "registration-one", ["thmA", "thmB"], classified=False,
                fingerprint=fingerprint(),
                constants={"thmA": ["Eq"], "thmB": []},
                type_constants={"thmA": ["Eq"], "thmB": []})


if __name__ == "__main__":
    unittest.main()
