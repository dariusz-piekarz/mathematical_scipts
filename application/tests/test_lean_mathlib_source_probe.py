"""Regression tests for pinned Mathlib source closure (not real Mathlib evidence)."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts import lean_mathlib_source_probe as probe


LOCK = Path(__file__).resolve().parents[1] / "lean" / "mathlib-source-lock.json"
SHA = "a" * 40


class MathlibSourceClosureTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.lock = probe.read_json(LOCK)
        self.expected = probe.validate_lock(self.lock)
        self.packages = self.root / ".lake" / "packages"
        for name in self.expected:
            (self.packages / name).mkdir(parents=True)
        (self.root / "lean-toolchain").write_text(probe.TOOLCHAIN + "\n")
        (self.root / "lakefile.toml").write_text(
            'name = "AtlasFormalization"\n[[require]]\nname = "mathlib"\n'
            'scope = "leanprover-community"\nrev = "' + probe.PIN + '"\n')
        self.write(self.root / "mathlib-source-lock.json", self.lock)
        self.project = self.manifest("AtlasFormalization", self.expected)
        self.upstream = self.manifest("mathlib", {k:v for k,v in self.expected.items() if k != "mathlib"})
        self.write(self.root / "lake-manifest.json", self.project)
        self.write(self.packages / "mathlib" / "lake-manifest.json", self.upstream)
        self.heads = {name: value["rev"] for name, value in self.expected.items()}
        self.checkout = SHA
        self.clean_error = None
        self.committed_lock = copy.deepcopy(self.lock)
        self.committed_upstream = copy.deepcopy(self.upstream)
        self.clean_digest = probe.environment._digest({"state": "materialized", "packages": [
            {"name": name, "commit": record["rev"]} for name, record in sorted(self.expected.items())]})

    @staticmethod
    def write(path, data):
        path.write_text(json.dumps(data), encoding="utf-8")

    @staticmethod
    def manifest(name, records):
        return {"name": name, "version": "1.1.0", "packagesDir": ".lake/packages",
                "lakeDir": ".lake", "packages": [
                    {"name": key, **value, "type": "git", "subDir": None}
                    for key, value in records.items()]}

    def inspect(self):
        def git(path, *args):
            if args == ("show", SHA + ":application/lean/mathlib-source-lock.json"):
                self.assertEqual(path, self.root)
                return json.dumps(self.committed_lock)
            if args == ("show", probe.PIN + ":lake-manifest.json"):
                self.assertEqual(path, self.packages / "mathlib")
                return json.dumps(self.committed_upstream)
            self.assertEqual(args, ("rev-parse", "HEAD"))
            return self.checkout if path == self.root else self.heads[path.name]
        with patch.object(probe.environment, "_git", side_effect=git), \
                patch.object(probe.environment, "external_packages_sha256",
                             return_value=self.clean_digest, side_effect=self.clean_error):
            return probe.inspect_sources(self.root, expected_sha=SHA)

    def test_valid_closure_never_claims_offline_or_artifact_verification(self):
        report = self.inspect()
        self.assertEqual(report["package_count"], 9)
        self.assertEqual(report["mathlib_revision"], probe.PIN)
        self.assertEqual(report["checkout_sha"], SHA)
        for flag in ("artifact_bytes_verified", "offline_ready", "execution_allowed", "certificate"):
            self.assertIs(report[flag], False)

    def test_generated_manifest_drift_missing_extra_duplicate_and_subdir(self):
        for mode in ("rev", "url", "missing", "extra", "duplicate", "subdir", "type"):
            data = copy.deepcopy(self.project)
            rows = data["packages"]
            if mode == "rev":
                rows[0]["rev"] = "0" * 40
            elif mode == "url":
                rows[0]["url"] = "https://github.com/other/repo"
            elif mode == "missing":
                rows.pop()
            elif mode == "extra":
                rows.append({**rows[0], "name": "Unexpected"})
            elif mode == "duplicate":
                rows.append(dict(rows[0]))
            elif mode == "subdir":
                rows[0]["subDir"] = "other"
            else:
                rows[0]["type"] = "path"
            self.write(self.root / "lake-manifest.json", data)
            with self.subTest(mode=mode), self.assertRaises(ValueError):
                self.inspect()

    def test_installed_revision_and_dirty_checkout_fail(self):
        name = next(iter(self.heads))
        original = self.heads[name]
        self.heads[name] = "0" * 40
        with self.assertRaisesRegex(ValueError, "revision mismatch"):
            self.inspect()
        self.heads[name] = original
        self.clean_error = ValueError("Modified or untracked Lake dependency")
        with self.assertRaisesRegex(ValueError, "Modified"):
            self.inspect()

    def test_installed_package_set_must_match(self):
        extra = self.packages / "Unexpected"
        extra.mkdir()
        with self.assertRaisesRegex(ValueError, "dependency set"):
            self.inspect()
        extra.rmdir()
        (self.packages / "Qq").rmdir()
        with self.assertRaisesRegex(ValueError, "dependency set"):
            self.inspect()

    def test_upstream_manifest_and_root_checkout_are_independent(self):
        data = copy.deepcopy(self.upstream)
        data["packages"][0]["rev"] = "0" * 40
        self.write(self.packages / "mathlib" / "lake-manifest.json", data)
        with self.assertRaisesRegex(ValueError, "Upstream manifest"):
            self.inspect()
        self.write(self.packages / "mathlib" / "lake-manifest.json", self.upstream)
        self.checkout = "c" * 40
        with self.assertRaisesRegex(ValueError, "Checkout identity"):
            self.inspect()

    def test_lock_and_json_reject_ambiguous_records(self):
        for mutation in ({"schema": True}, {"lean_toolchain": "other"},
                         {"mathlib_manifest_source": "https://example.com"},
                         {"packages": self.lock["packages"][:-1]}):
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                probe.validate_lock({**self.lock, **mutation})
        path = self.root / "duplicate.json"
        path.write_text('{"rev":"a","rev":"b"}')
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            probe.read_json(path)
        path.write_bytes(b"x" * (probe.MAX_JSON_BYTES + 1))
        with self.assertRaisesRegex(ValueError, "budget"):
            probe.read_json(path)


    def test_lock_worktree_and_committed_object_must_match(self):
        changed = copy.deepcopy(self.lock)
        changed["packages"][0]["rev"] = "0" * 40
        self.write(self.root / "mathlib-source-lock.json", changed)
        with self.assertRaisesRegex(ValueError, "lock differs from committed"):
            self.inspect()

    def test_committed_upstream_is_checked_even_when_worktree_agrees(self):
        changed = copy.deepcopy(self.upstream)
        changed["packages"][0]["rev"] = "0" * 40
        self.committed_upstream = changed
        self.write(self.packages / "mathlib" / "lake-manifest.json", changed)
        with self.assertRaisesRegex(ValueError, "Pinned upstream manifest"):
            self.inspect()

    def test_clean_checkout_digest_must_describe_same_revisions(self):
        self.clean_digest = "b" * 64
        with self.assertRaisesRegex(ValueError, "identity digest"):
            self.inspect()
