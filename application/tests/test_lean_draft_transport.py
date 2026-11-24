"""Preflight contract tests. Fake metadata is not real isolation evidence."""
import copy
import json
import unittest
from pathlib import Path
from unittest.mock import patch
from backend import lean_draft_transport as transport
from backend import lean_draft_runner as policy


class DraftTransportTests(unittest.TestCase):
    def setUp(self):
        self.image = "sha256:" + "a"*64
        self.cid = "b"*64
        self.name = "atlas-draft-" + "c"*32
        self.info = {"SecurityOptions": ["name=rootless", "name=seccomp,profile=builtin"],
                     "OSType": "linux", "CgroupVersion": "2",
                     "MemoryLimit": True, "SwapLimit": True, "PidsLimit": True, "CpuCfsQuota": True}
        self.image_record = {"Id": self.image, "Os": "linux", "Config": {
            "Volumes": None, "Entrypoint": [policy.ENTRYPOINT], "Cmd": None,
            "Env": sorted(policy._IMAGE_ENV), "User": "65534:65534", "OnBuild": None}}
        self.record = {"Id": self.cid, "Image": self.image, "Name": "/"+self.name,
                       "Path": policy.ENTRYPOINT, "Args": [], "Mounts": [],
                       "State": {"Status": "created", "Running": False},
                       "Config": {"User": "65534:65534", "WorkingDir": "/tmp",
                                  "OpenStdin": True, "Tty": False, "Env": sorted(policy._IMAGE_ENV)},
                       "HostConfig": {"NetworkMode": "none", "IpcMode": "private",
                           "CgroupnsMode": "private", "ReadonlyRootfs": True, "Privileged": False,
                           "Memory": policy.MEMORY_BYTES, "MemorySwap": policy.MEMORY_BYTES,
                           "PidsLimit": policy.PIDS_LIMIT, "NanoCpus": 1000000000,
                           "CapDrop": ["ALL"], "SecurityOpt": ["no-new-privileges"],
                           "Tmpfs": {"/tmp": "rw,noexec,nosuid,nodev,size=16777216"},
                           "RestartPolicy": {"Name": "no"}, "LogConfig": {"Type": "none"},
                           "PidMode": "", "UTSMode": "", "UsernsMode": "",
                           "PublishAllPorts": False, "AutoRemove": False,
                           "Ulimits": [{"Name": "nofile", "Soft": 256, "Hard": 256},
                                       {"Name": "core", "Soft": 0, "Hard": 0}]}}

    def test_rootless_engine_requires_all_limits(self):
        transport.validate_engine(self.info)
        for key in ("MemoryLimit", "SwapLimit", "PidsLimit", "CpuCfsQuota"):
            with self.subTest(key=key), self.assertRaises(ValueError):
                transport.validate_engine({**self.info, key: False})
        for opts in ([], ["name=rootless"], ["name=rootless","name=seccomp,profile=unconfined"]):
            with self.assertRaises(ValueError):
                transport.validate_engine({**self.info, "SecurityOptions": opts})

    def validate(self, record):
        transport.validate_container([record], container_id=self.cid, image_id=self.image, name=self.name)

    def test_container_exact_configuration(self):
        self.validate(self.record)

    def test_container_rejects_missing_or_unsafe_limits(self):
        for key, value in (("NetworkMode","host"),("Memory",0),("MemorySwap",-1),
                           ("NanoCpus",0),("PidsLimit",0),("ReadonlyRootfs",False),
                           ("Privileged",True),("Binds",["/:/host"]),("CapDrop",[]),
                           ("SecurityOpt",[]),("Tmpfs",{})):
            with self.subTest(key=key):
                rec = copy.deepcopy(self.record)
                rec["HostConfig"][key] = value
                with self.assertRaises(ValueError):
                    self.validate(rec)

    def test_container_refuses_other_image_or_running_probe(self):
        for key, value in (("Image","wrong"),("Args",["unexpected"]),("Mounts",[{"Source":"/host"}]),
                           ("State",{"Status":"running","Running":True})):
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.validate({**self.record, key: value})

    def fake_probe(self, bad_inspect=False, bad_cleanup=False, bad_create=False):
        calls = []
        def command(prefix, args, env):
            calls.append(args)
            self.assertIn("unix:///run/user/1000/docker.sock", prefix)
            self.assertEqual(set(env), {"PATH", "HOME", "LANG"})
            if args[0] == "info":
                return json.dumps(self.info).encode()
            if args[:2] == ("image","inspect"):
                return json.dumps([self.image_record]).encode()
            if args[0] == "create":
                if bad_create:
                    raise TimeoutError("create response lost")
                return self.cid.encode()
            if args[:2] == ("container","inspect"):
                rec = {**self.record, "Name":"/wrong"} if bad_inspect else self.record
                return json.dumps([rec]).encode()
            if args[:2] == ("container","rm"):
                if bad_cleanup:
                    raise ValueError("remove failed")
                return b"removed"
            raise AssertionError("Unexpected command")
        with patch.object(transport, "_local_socket", return_value=Path("/run/user/1000/docker.sock")), \
             patch.object(transport.uuid, "uuid4") as uid, patch.object(transport, "_command", side_effect=command):
            uid.return_value.hex = "c"*32
            result = transport.probe(self.image)
        return result, calls

    def test_probe_never_starts_and_always_removes(self):
        result, calls = self.fake_probe()
        self.assertEqual(result["status"], "configuration_checked")
        self.assertFalse(result["execution_allowed"])
        self.assertEqual(result["proof_status"], "not_run")
        self.assertEqual(calls[-1], ("container","rm",self.cid))
        self.assertFalse(any("start" in args or "run" in args for args in calls))

    def test_probe_blocks_on_inspection_or_cleanup_failure(self):
        for inspect, cleanup in ((True,False),(False,True)):
            result, calls = self.fake_probe(inspect,cleanup)
            self.assertEqual(result["status"], "blocked")
            self.assertFalse(result["execution_allowed"])
            self.assertEqual(calls[-1], ("container","rm",self.cid))

    def test_invalid_image_never_touches_engine(self):
        with patch.object(transport, "_local_socket", side_effect=AssertionError):
            self.assertEqual(transport.probe("latest")["status"],"blocked")


    def test_ambiguous_create_never_removes_by_name(self):
        result, calls = self.fake_probe(bad_create=True)
        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["cleanup_status"], "create_outcome_unknown")
        self.assertEqual(result["probe_name"], self.name)
        self.assertFalse(any(args[:2] == ("container", "rm") for args in calls))

    def test_cleanup_failure_is_explicit(self):
        result, _ = self.fake_probe(bad_cleanup=True)
        self.assertEqual(result["cleanup_status"], "removal_unconfirmed")
        self.assertEqual(result["probe_name"], self.name)

    def test_rejects_host_namespaces_and_other_unsafe_defaults(self):
        for key, value in (("PidMode", "host"), ("UTSMode", "host"),
                           ("UsernsMode", "host"), ("PublishAllPorts", True),
                           ("AutoRemove", True), ("VolumesFrom", ["other"]),
                           ("SecurityOpt", ["no-new-privileges", "seccomp=unconfined"]),
                           ("SecurityOpt", "no-new-privileges"),
                           ("RestartPolicy", None), ("LogConfig", []),
                           ("Ulimits", [{"Name": "core", "Soft": 1, "Hard": 1}])):
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.validate({**self.record, "HostConfig": {**self.record["HostConfig"], key: value}})

    def test_rejects_missing_or_malformed_ulimits(self):
        for limits in (None, [], [{"Name":"nofile","Soft":256,"Hard":256}]*2,
                       [{"Name":"nofile","Soft":256,"Hard":256},
                        {"Name":"core","Soft":False,"Hard":0}]):
            with self.subTest(limits=limits), self.assertRaises(ValueError):
                self.validate({**self.record, "HostConfig": {**self.record["HostConfig"], "Ulimits": limits}})

    def test_duplicate_json_and_nonfinite_metadata_rejected(self):
        for data in (b'{"Memory": 0, "Memory": 1}', b'{"Memory": NaN}',
                     b'{"Memory": Infinity}', b'{"Config":{"Env":[],"Env":[]}}'):
            with self.subTest(data=data), self.assertRaises(ValueError):
                transport._decode_metadata(data)

    def test_engine_refuses_conflicting_or_custom_seccomp(self):
        for opts in (["name=rootless","name=seccomp,profile=builtin","name=seccomp,profile=unconfined"],
                     ["name=rootless","name=seccomp,profile=custom"]):
            with self.assertRaises(ValueError):
                transport.validate_engine({**self.info, "SecurityOptions":opts})
