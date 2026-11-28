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
