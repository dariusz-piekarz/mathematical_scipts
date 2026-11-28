"""Fixed stdin probe regression; only Linux CI proves container execution."""
import unittest
from unittest.mock import patch

from backend import lean_draft_transport as transport
from scripts import lean_scoped_payload_probe as probe
from scripts.lean_rootless_compiler_probe import LEAN_COMMIT

VERSION = ("Lean (version 4.26.0, x86_64-unknown-linux-gnu, commit "
           + LEAN_COMMIT + ", Release)\n").encode()


class ScopedPayloadTests(unittest.TestCase):
    def test_exact_prepared_digest_and_positive_output(self):
        prepared, exit_code = probe.prepared_fixture("true")
        self.assertEqual(exit_code, 0)
        data = b"ATLAS_INPUT_SHA256 " + prepared.input_sha256.encode() + b"\n" + VERSION
        result = probe.validate_payload_output(data + b"'atlas_draft' does not depend on any axioms\n",
                                               prepared, expected_exit=0)
        self.assertEqual(result["observed_input_sha256"], prepared.input_sha256)
        self.assertEqual(result["axioms"], [])
        for bad in (b"", data.replace(prepared.input_sha256.encode(), b"0"*64),
                    data + b"'atlas_draft' depends on axioms: [sorryAx]\n",
                    data + b"x"*transport.MAX_METADATA_BYTES):
            with self.assertRaises(ValueError):
                probe.validate_payload_output(bad, prepared, expected_exit=0)

    def test_fixed_negative_and_unknown_case(self):
        prepared, exit_code = probe.prepared_fixture("false")
        self.assertEqual(exit_code, 1)
        row = next(i for i, line in enumerate(prepared.input_bytes.decode().splitlines(), 1)
                   if line.strip() == "| omega")
        data = (b"ATLAS_INPUT_SHA256 " + prepared.input_sha256.encode() + b"\n" + VERSION
                + f"Draft.lean:{row}:4: error: omega could not prove the goal:\n".encode())
        self.assertIsNone(probe.validate_payload_output(data, prepared, expected_exit=1)["axioms"])
        with self.assertRaises(ValueError):
            probe.validate_payload_output(data.replace(b"could not prove the goal:", b"timed out"),
                                          prepared, expected_exit=1)
        with self.assertRaises(ValueError):
            probe.prepared_fixture("arbitrary")

    def test_stdin_contract_refuses_unrelated_commands_before_spawn(self):
        with patch.object(transport.subprocess, "Popen") as spawn:
            for args, value in ((("info",), b"x"),
                                (("container", "start", "--attach", "--interactive", "a"*64), b""),
                                (("container", "start", "--attach", "--interactive", "a"*64),
                                 b"x"*(transport.MAX_FIXTURE_INPUT_BYTES+1)),
                                (("container", "start", "--attach", "--interactive", "bad"), b"x")):
                with self.assertRaises(ValueError):
                    transport._command(["docker"], args, {}, fixture_input=value)
            spawn.assert_not_called()

    def test_entry_reads_only_bounded_stdin_and_hashes_file(self):
        entry = probe.payload_entry(["mathlib"])
        self.assertIn("head -c " + str(transport.MAX_FIXTURE_INPUT_BYTES + 1), entry)
        self.assertIn("sha256sum Draft.lean", entry)
        self.assertIn("exec /opt/lean/bin/lean Draft.lean", entry)


    def test_fixed_repair_loop_replays_diagnostics_and_distinct_payloads(self):
        # Simulated subprocess results for the contract test only.
        # The real workflow must independently produce all three exit codes.
        import hashlib
        seen = []
        image = "sha256:" + "a"*64

        def execute(prefix, env, actual_image, prepared, *, expected_exit):
            attempt = len(seen) + 1
            self.assertEqual(actual_image, image)
            self.assertEqual(expected_exit, 0 if attempt == 3 else 1)
            self.assertEqual(hashlib.sha256(prepared.input_bytes).hexdigest(), prepared.input_sha256)
            if expected_exit:
                line = next(i for i, line in enumerate(prepared.input_bytes.decode().splitlines(), 1)
                            if line.strip().startswith("| omega"))
                diagnostic = f"Draft.lean:{line}:4: error: omega could not prove the goal:\n".encode()
            else:
                diagnostic = b"'atlas_draft' depends on axioms: [propext]\n"
            output = b"ATLAS_INPUT_SHA256 " + prepared.input_sha256.encode() + b"\n" + VERSION + diagnostic
            row = dict(exit_code=expected_exit, image_id=image, container_id=str(attempt)*64,
                       input_sha256=prepared.input_sha256, observed_input_sha256=prepared.input_sha256,
                       code_sha256=prepared.lean_code_sha256,
                       diagnostic_sha256=hashlib.sha256(diagnostic).hexdigest(),
                       cleanup_status="removed_verified", axioms=None if expected_exit else ["propext"])
            seen.append(prepared)
            return row, output

        with patch.object(probe, "_execute_fixed_payload", side_effect=execute):
            report = probe.run_fixed_repair_loop([], {}, image)
        self.assertEqual([x["exit_code"] for x in report["attempts"]], [1, 1, 0])
        self.assertEqual(len({x.input_sha256 for x in seen}), 3)
        for row in report["attempts"]:
            self.assertTrue(row["compiler_output"].startswith("ATLAS_INPUT_SHA256 " + row["input_sha256"]))
        self.assertEqual(seen[-1].attempt, 3)
        self.assertFalse(report["execution_allowed"])
        self.assertFalse(report["certificate"])

    def test_fixed_repair_loop_stops_on_invalid_transport(self):
        with patch.object(probe, "_execute_fixed_payload", side_effect=ValueError("digest mismatch")) as run:
            with self.assertRaises(ValueError):
                probe.run_fixed_repair_loop([], {}, "sha256:" + "a"*64)
            run.assert_called_once()


    def test_persisted_report_rejects_stale_identity_and_authority(self):
        for report in ({}, {"execution_allowed": True}, {"certificate": True}):
            with self.assertRaises(ValueError):
                probe.replay_report(report, {}, {}, expected_sha="a"*40, expected_manifest_sha="b"*64)


class PersistedReplayAdversarialTests(unittest.TestCase):
    """Synthetic evidence tests, separate from actual native rootless CI."""
    def setUp(self):
        import hashlib
        import tempfile
        from pathlib import Path
        from tests.test_lean_mathlib_source_probe import MathlibSourceClosureTests
        self.sha = lambda value: hashlib.sha256(value).hexdigest()
        fixture = MathlibSourceClosureTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        source = fixture.inspect()
        self.checkout = source["checkout_sha"]
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        atlas = root / "opt/atlas"
        atlas.mkdir(parents=True)
        dependency = root / "Basic.olean"
        dependency.write_bytes(b"synthetic compiled dependency")
        (atlas / "Fixture.lean").write_text("fixed fixture", encoding="utf-8")
        entry = atlas / "run-draft"
        entry.write_text("fixed entrypoint", encoding="ascii")
        scope = probe.artifacts.SCOPED_FIXTURE_SCOPE
        self.baseline = probe.artifacts.create_manifest(root, source, scope=scope)
        (atlas / "Fixture.lean").unlink()
        entry.write_text(probe.payload_entry(p["name"] for p in source["packages"]), encoding="ascii")
        self.manifest = probe.artifacts.create_manifest(root, source, scope=scope)
        self.digest = self.sha(probe.artifacts.encoded(self.manifest))
        self.image = "sha256:" + "a"*64
        self.counter = 0

        def execute(prefix, env, image, prepared, *, expected_exit):
            self.counter += 1
            if expected_exit:
                line = next(i for i, line in enumerate(prepared.input_bytes.decode().splitlines(), 1)
                            if line.strip().startswith("| omega"))
                diagnostic = f"Draft.lean:{line}:4: error: omega could not prove the goal:\n".encode()
                axioms = None
            else:
                diagnostic = b"'atlas_draft' does not depend on any axioms\n"
                axioms = []
            output = b"ATLAS_INPUT_SHA256 " + prepared.input_sha256.encode() + b"\n" + VERSION + diagnostic
            row = dict(image_id=image, container_id=str(self.counter)*64,
                       input_sha256=prepared.input_sha256, observed_input_sha256=prepared.input_sha256,
                       code_sha256=prepared.lean_code_sha256, source_sha256=prepared.source_sha256,
                       ast_sha256=prepared.ast_sha256, diagnostic_sha256=self.sha(diagnostic),
                       diagnostic_bytes=len(diagnostic), cleanup_status="removed_verified",
                       container_state="exited", exit_code=expected_exit,
                       lean_version=VERSION.decode().strip(), axioms=axioms)
            return row, output

        with patch.object(probe, "_execute_fixed_payload", side_effect=execute):
            cases = [probe.check_fixed_payload([], {}, self.image, case) for case in probe.CASES]
            loop = probe.run_fixed_repair_loop([], {}, self.image)
        self.report = dict(schema=2, checkout_sha=self.checkout, fixture_only=True,
                           manifest_sha256=self.digest, execution_allowed=False, offline_ready=False,
                           certificate=False, proof_status="not_run", cases=cases, repair_loop=loop)

    def verify(self, report=None, manifest=None, baseline=None, digest=None):
        probe.replay_report(self.report if report is None else report,
                            self.manifest if manifest is None else manifest,
                            self.baseline if baseline is None else baseline,
                            expected_sha=self.checkout,
                            expected_manifest_sha=self.digest if digest is None else digest)

    def test_complete_replay_without_subprocess(self):
        with patch.object(transport.subprocess, "Popen", side_effect=AssertionError("no execution")):
            self.verify()

    def test_mutated_row_fields_and_identity_rejected(self):
        from copy import deepcopy
        for key, value in (("exit_code", True), ("cleanup_status", "unconfirmed"),
                           ("input_sha256", "0"*64), ("observed_input_sha256", "0"*64),
                           ("code_sha256", "0"*64), ("ast_sha256", "0"*64),
                           ("source_sha256", "0"*64), ("diagnostic_sha256", "0"*64),
                           ("diagnostic_bytes", 0), ("attempt", 2),
                           ("image_id", "sha256:"+"b"*64), ("container_id", self.report["cases"][0]["container_id"])):
            with self.subTest(key=key):
                altered = deepcopy(self.report)
                altered["repair_loop"]["attempts"][0][key] = value
                with self.assertRaises(ValueError):
                    self.verify(altered)

    def test_rehashed_forbidden_diagnostic_and_axiom_rejected(self):
        from copy import deepcopy
        for attempt, old, new in ((0, "could not prove the goal:", "timed out"),
                                  (2, "does not depend on any axioms", "depends on axioms: [sorryAx]")):
            altered = deepcopy(self.report)
            row = altered["repair_loop"]["attempts"][attempt]
            row["compiler_output"] = row["compiler_output"].replace(old, new)
            diagnostic = row["compiler_output"].split("\n", 2)[2].encode()
            row["diagnostic_sha256"] = self.sha(diagnostic)
            row["diagnostic_bytes"] = len(diagnostic)
            if attempt == 2:
                row["axioms"] = ["sorryAx"]
            with self.subTest(attempt=attempt), self.assertRaises(ValueError):
                self.verify(altered)

    def test_reordered_or_truncated_history_rejected(self):
        from copy import deepcopy
        for change in ("swap", "truncate", "duplicate", "authority"):
            altered = deepcopy(self.report)
            loop = altered["repair_loop"]
            rows = loop["attempts"]
            if change == "swap":
                rows[0], rows[1] = rows[1], rows[0]
            elif change == "truncate":
                rows.pop()
            elif change == "duplicate":
                rows[1] = deepcopy(rows[0])
            else:
                loop["execution_allowed"] = True
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.verify(altered)

    def test_rehashed_modified_dependency_or_entrypoint_rejected(self):
        from copy import deepcopy
        for path in ("Basic.olean", "opt/atlas/run-draft"):
            manifest = deepcopy(self.manifest)
            next(r for r in manifest["entries"] if r["path"] == path)["sha256"] = "0"*64
            digest = self.sha(probe.artifacts.encoded(manifest))
            report = dict(self.report, manifest_sha256=digest)
            with self.subTest(path=path), self.assertRaises(ValueError):
                self.verify(report, manifest, digest=digest)
