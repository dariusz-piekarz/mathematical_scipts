"""Admission and isolation-policy regressions; not real container tests."""
import hashlib
import unittest
from dataclasses import FrozenInstanceError
from unittest.mock import patch
from backend import lean_draft_generator as generator
from backend import lean_draft_runner as runner


class DraftRunnerAdmissionTests(unittest.TestCase):
    def setUp(self):
        self.source = r"\forall P:Prop, P \implies P"
        r = generator.generate(self.source, consent=True)
        self.hashes = dict(expected_source_sha256=r["source_sha256"],
                           expected_ast_sha256=r["ast_sha256"],
                           expected_code_sha256=r["lean_code_sha256"])

    def test_admission_regenerates_and_binds_payload(self):
        status, draft = runner.prepare(self.source, **self.hashes, consent=True)
        self.assertEqual(status["admission_status"], "prepared")
        self.assertEqual(status["status"], "blocked")
        self.assertFalse(status["execution_allowed"])
        self.assertFalse(status["certificate"])
        self.assertEqual(status["proof_status"], "not_run")
        self.assertEqual(draft.input_sha256, hashlib.sha256(draft.input_bytes).hexdigest())
        self.assertTrue(draft.input_bytes.endswith(b"#print axioms atlas_draft\n"))
        with self.assertRaises(FrozenInstanceError):
            draft.input_bytes = b"tampered"

    def test_no_consent_no_generation(self):
        with patch.object(generator, "generate", side_effect=AssertionError):
            for value in (False, None, 1, "true"):
                status, draft = runner.prepare(self.source, **self.hashes, consent=value)
                self.assertEqual(status["error"], "execution_consent_required")
                self.assertIsNone(draft)

    def test_each_digest_is_required(self):
        for key in self.hashes:
            for digest in ("0"*64, "invalid", None, ["0"*64]):
                changed = {**self.hashes, key: digest}
                status, draft = runner.prepare(self.source, **changed, consent=True)
                self.assertIsNone(draft)
                self.assertFalse(status["execution_allowed"])

    def test_source_changed_or_invalid(self):
        for source in (self.source+" ", self.source+"; #eval IO.println", r"\bot"):
            status, draft = runner.prepare(source, **self.hashes, consent=True)
            self.assertIsNone(draft)
            self.assertEqual(status["proof_status"], "not_run")

    def test_no_arbitrary_code_argument(self):
        with self.assertRaises(TypeError):
            runner.prepare(self.source, **self.hashes, consent=True, lean_code="arbitrary")

    def test_policy_has_all_required_constraints(self):
        args = runner.isolation_arguments(image_id="sha256:"+"a"*64,
                                          container_name="atlas-draft-"+"b"*32)
        for token in ("--pull=never", "--network=none", "--ipc=private",
                      "--cgroupns=private", "--read-only", "--cap-drop=ALL",
                      "--security-opt=no-new-privileges", "--user=65534:65534",
                      "--pids-limit=64", "--memory=2147483648",
                      "--memory-swap=2147483648", "--cpus=1",
                      "--no-healthcheck", "--log-driver=none",
                      "--entrypoint=/opt/atlas/run-draft"):
            self.assertIn(token, args)
        self.assertFalse(any(x.startswith(("--volume", "--mount", "--privileged",
                                           "--device", "--publish", "--env-file")) for x in args))
        self.assertEqual(args[-1], "sha256:"+"a"*64)

    def test_policy_refuses_tags_and_option_injection(self):
        good_id = "sha256:"+"a"*64
        good_name = "atlas-draft-"+"b"*32
        for image in ("lean:latest", "--privileged", "sha256:"+"A"*64, None):
            with self.assertRaises(ValueError):
                runner.isolation_arguments(image_id=image, container_name=good_name)
        for name in ("other", "--privileged", good_name+"\n", None):
            with self.assertRaises(ValueError):
                runner.isolation_arguments(image_id=good_id, container_name=name)

    def test_no_os_process_calls_during_admission(self):
        with patch("subprocess.Popen", side_effect=AssertionError("execution forbidden")):
            status, draft = runner.prepare(self.source, **self.hashes, consent=True)
            self.assertIsNotNone(draft)
            self.assertFalse(status["execution_allowed"])
