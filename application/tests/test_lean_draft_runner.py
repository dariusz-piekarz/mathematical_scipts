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


class DraftImagePolicyTests(unittest.TestCase):
    def setUp(self):
        self.image_id = "sha256:" + "a" * 64
        self.record = {"Id": self.image_id, "Os": "linux", "Config": {
            "Volumes": None, "Entrypoint": [runner.ENTRYPOINT], "Cmd": None,
            "Env": sorted(runner._IMAGE_ENV), "User": "65534:65534",
            "OnBuild": None, "Healthcheck": None,
        }}

    def check(self, record):
        return runner.validate_image_inspection([record], approved_image_id=self.image_id)

    def test_exact_approved_image_metadata(self):
        self.assertIsNone(self.check(self.record))

    def test_identity_os_and_inspection_shape(self):
        for record in ([], [self.record, self.record], {}, None,
                       [{**self.record, "Id": "sha256:" + "b" * 64}],
                       [{**self.record, "Os": "windows"}]):
            with self.subTest(record=record):
                with self.assertRaises(ValueError):
                    runner.validate_image_inspection(record, approved_image_id=self.image_id)
        with self.assertRaises(ValueError):
            runner.validate_image_inspection([self.record], approved_image_id="lean:latest")

    def test_image_defaults_cannot_bypass_isolation(self):
        mutations = {
            "Volumes": {"/host": {}}, "Entrypoint": ["/bin/sh"],
            "Cmd": ["unexpected"], "User": "0:0", "OnBuild": ["RUN unexpected"],
            "Healthcheck": {"Test": ["CMD", "unexpected"]},
            "Env": sorted(runner._IMAGE_ENV) + ["LD_PRELOAD=/tmp/injected.so"],
        }
        for key, value in mutations.items():
            with self.subTest(key=key):
                record = {**self.record, "Config": {**self.record["Config"], key: value}}
                with self.assertRaises(ValueError):
                    self.check(record)

    def test_missing_or_malformed_image_metadata_fails_closed(self):
        for key in ("Volumes", "Entrypoint", "Cmd", "Env", "User", "OnBuild"):
            cfg = dict(self.record["Config"])
            del cfg[key]
            with self.subTest(key=key):
                with self.assertRaises(ValueError):
                    self.check({**self.record, "Config": cfg})
        for env in (None, "PATH=/bin", [1], sorted(runner._IMAGE_ENV)*2, []):
            with self.subTest(env=env):
                with self.assertRaises(ValueError):
                    self.check({**self.record, "Config": {**self.record["Config"], "Env": env}})

    def test_no_automatic_restart_and_input_path_matches_tmpfs(self):
        args = runner.isolation_arguments(image_id=self.image_id,
                                          container_name="atlas-draft-"+"b"*32)
        self.assertIn("--restart=no", args)
        self.assertEqual(runner.INPUT_PATH, "/tmp/Draft.lean")
        self.assertIn("--tmpfs=/tmp:rw,noexec,nosuid,nodev,size=16777216,mode=0700,uid=65534,gid=65534", args)
