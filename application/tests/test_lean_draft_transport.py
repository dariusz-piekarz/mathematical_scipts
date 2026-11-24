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
                           "Tmpfs": {"/tmp": "rw,noexec,nosuid,nodev,size=16777216,mode=0700,uid=65534,gid=65534"},
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

    def test_rejects_missing_or_unsafe_tmpfs_owner_mode(self):
        options = self.record["HostConfig"]["Tmpfs"]["/tmp"]
        for old, new in ((",mode=0700", ""), (",uid=65534", ""), (",gid=65534", ""),
                         ("mode=0700", "mode=0777"), ("uid=65534", "uid=0"),
                         ("gid=65534", "gid=0")):
            with self.subTest(old=old, new=new), self.assertRaises(ValueError):
                self.validate({**self.record, "HostConfig": {**self.record["HostConfig"],
                               "Tmpfs": {"/tmp": options.replace(old, new)}}})

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


@unittest.skipUnless(__import__("sys").platform.startswith("linux"),
                     "Real selector/pipe subprocess regression requires Linux")
class DraftTransportProcessTests(unittest.TestCase):
    """Real subprocess I/O on Linux, not a Docker or Lean execution test."""

    def invoke(self, script):
        import sys
        return transport._command([sys.executable, "-I", "-c"], (script,),
                                  {"PATH": "/usr/bin:/bin", "LANG": "C"})

    def test_capture_real_stdout_and_stderr(self):
        self.assertEqual(self.invoke("import sys; sys.stdout.write('abc'); "
                                     "sys.stdout.flush(); sys.stderr.write('def')"),
                         b"abcdef")

    def test_real_nonzero_exit_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "command failed"):
            self.invoke("raise SystemExit(7)")

    def test_real_excess_output_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "exceeds limit"):
            self.invoke("import sys; sys.stdout.buffer.write(b'x'*200000); sys.stdout.flush()")

    def test_real_timeout_stops_child(self):
        import time
        with patch.object(transport, "COMMAND_TIMEOUT", 0.4):
            start = time.monotonic()
            with self.assertRaises(TimeoutError):
                self.invoke("import time; time.sleep(30)")
            self.assertLess(time.monotonic() - start, 5)

    def assert_timeout_stops_group(self, *, leader_exits):
        import os
        import signal
        import tempfile
        import time

        def running(pid):
            try:
                state = Path(f"/proc/{pid}/stat").read_text().rsplit(")", 1)[1].split()[0]
                return state not in ("Z", "X")
            except FileNotFoundError:
                return False

        with tempfile.TemporaryDirectory() as directory:
            marker = Path(directory) / "child.pid"
            script = (
                "import os, time\n"
                "from pathlib import Path\n"
                "child = os.fork()\n"
                "if child == 0:\n"
                f"    Path({str(marker)!r}).write_text(str(os.getpid()))\n"
                "    time.sleep(30)\n"
                "    os._exit(0)\n"
                + ("os._exit(0)\n" if leader_exits else "time.sleep(30)\n")
            )
            try:
                with patch.object(transport, "COMMAND_TIMEOUT", 2):
                    with self.assertRaises(TimeoutError):
                        self.invoke(script)
                self.assertTrue(marker.exists(), "Child did not reach the test fixture")
                pid = int(marker.read_text())
                deadline = time.monotonic() + 3
                while running(pid) and time.monotonic() < deadline:
                    time.sleep(0.02)
                self.assertFalse(running(pid), "CLI descendant survived timeout")
            finally:
                if marker.exists():
                    pid = int(marker.read_text())
                    if running(pid):
                        try:
                            os.kill(pid, signal.SIGKILL)
                        except ProcessLookupError:
                            pass

    def test_timeout_terminates_child_in_cli_process_group(self):
        self.assert_timeout_stops_group(leader_exits=False)

    def test_timeout_terminates_pipe_holder_after_leader_exit(self):
        self.assert_timeout_stops_group(leader_exits=True)


class RuntimeCgroupObservationTests(unittest.TestCase):
    """CI fixture parser regression; not evidence of Docker enforcement."""

    def setUp(self):
        from scripts.lean_rootless_ci_probe import validate_runtime_limits
        self.validate = validate_runtime_limits
        self.valid = (b"memory.max=2147483648\nmemory.swap.max=0\n"
                      b"pids.max=64\ncpu.max=100000 100000\n")

    def test_accepts_exact_runtime_limits(self):
        self.assertEqual(self.validate(self.valid)["cpu.max"], "100000 100000")

    def test_rejects_unlimited_or_mismatched_controllers(self):
        for old, new in ((b"2147483648", b"max"), (b"swap.max=0", b"swap.max=1"),
                         (b"pids.max=64", b"pids.max=max"),
                         (b"100000 100000", b"max 100000"),
                         (b"100000 100000", b"200000 100000"),
                         (b"100000 100000", b"0 0")):
            with self.subTest(old=old, new=new), self.assertRaises(ValueError):
                self.validate(self.valid.replace(old, new))

    def test_rejects_missing_duplicate_or_unexpected_observations(self):
        for data in (self.valid.replace(b"pids.max=64\n", b""),
                     self.valid + b"pids.max=64\n",
                     self.valid + b"unknown=1\n",
                     self.valid + b"unexpected line\n"):
            with self.subTest(data=data), self.assertRaises(ValueError):
                self.validate(data)



def network_fixture_observation(dev=None, ipv4=None, ipv6=None, socket=b"absent"):
    if dev is None:
        dev = (b"Inter-| Receive | Transmit\n"
               b" face |bytes packets errs drop fifo frame compressed multicast"
               b"|bytes packets errs drop fifo colls carrier compressed\n"
               b" lo: " + b"0 " * 16 + b"\n")
    if ipv4 is None:
        ipv4 = b"Iface Destination Gateway Flags RefCnt Use Metric Mask MTU Window IRTT\n"
    if ipv6 is None:
        zero = b"0" * 32
        ipv6 = (zero + b" 00 " + zero + b" 00 " + zero
                + b" ffffffff 00000001 00000000 00200200 lo\n")
    return (b"net.dev=" + dev.replace(b"\n", b";") + b"\n"
            b"net.route=" + ipv4.replace(b"\n", b";") + b"\n"
            b"net.ipv6_route=" + ipv6.replace(b"\n", b";") + b"\n"
            b"net.docker_socket=" + socket + b"\n")


class RuntimeNetworkObservationTests(unittest.TestCase):
    def setUp(self):
        from scripts.lean_rootless_ci_probe import validate_runtime_network
        self.validate = validate_runtime_network
        self.valid = network_fixture_observation()

    def test_accepts_loopback_and_ipv6_reject_default(self):
        self.assertEqual(self.validate(self.valid)["net.interfaces"], "lo")

    def test_rejects_extra_or_wrong_interface(self):
        dev = self.valid.splitlines()[0].partition(b"=")[2].replace(b";", b"\n")
        for bad in (dev + b" eth0: " + b"0 " * 16 + b"\n",
                    dev.replace(b"lo:", b"eth0:"), b"", dev.replace(b"0 ", b"x ", 1)):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                self.validate(network_fixture_observation(dev=bad))

    def test_rejects_ipv4_default_gateway_and_other_interface(self):
        header = b"Iface Destination Gateway Flags RefCnt Use Metric Mask MTU Window IRTT\n"
        for row in (b"lo 00000000 00000000 0001 0 0 0 00000000 0 0 0\n",
                    b"lo 0100007F 0100007F 0003 0 0 0 FFFFFFFF 0 0 0\n",
                    b"eth0 0100007F 00000000 0001 0 0 0 FFFFFFFF 0 0 0\n",
                    b"malformed\n"):
            with self.subTest(row=row), self.assertRaises(ValueError):
                self.validate(network_fixture_observation(ipv4=header + row))
        with self.assertRaises(ValueError):
            self.validate(network_fixture_observation(ipv4=b""))

    def test_rejects_usable_ipv6_default_and_other_interface(self):
        route = self.valid.splitlines()[2].partition(b"=")[2].replace(b";", b"\n")
        for bad in (route.replace(b"00200200", b"00000001"),
                    route.replace(b" lo\n", b" eth0\n"),
                    route.replace(b" 00 ", b" FF ", 1), b"", b"malformed\n"):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                self.validate(network_fixture_observation(ipv6=bad))

    def test_rejects_socket_missing_duplicate_or_bad_encoding(self):
        for bad in (network_fixture_observation(socket=b"present"),
                    self.valid.replace(b"net.docker_socket=absent\n", b""),
                    self.valid + b"net.docker_socket=absent\n",
                    self.valid + b"unknown=1\n",
                    self.valid.replace(b"net.dev=", b"net.dev=!")):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                self.validate(bad)


class RuntimeSecurityObservationTests(unittest.TestCase):
    """Parser regression, not a substitute for the real container fixture."""

    def setUp(self):
        from scripts.lean_rootless_ci_probe import validate_runtime_security
        self.validate = validate_runtime_security
        self.valid = (b"Uid=65534 65534 65534 65534\nGid=65534 65534 65534 65534\n"
                      b"CapEff=0000000000000000\nNoNewPrivs=1\nSeccomp=2\n"
                      b"root.mountopts=ro,relatime\ntmp.mountopts=rw,nodev,nosuid,noexec,relatime\n"
                      b"root.write=EROFS\ntmp.write=ok\ntmp.owner_mode=65534:65534:700\n")

    def test_accepts_expected_runtime_security(self):
        self.assertEqual(self.validate(self.valid)["root.write"], "EROFS")

    def test_rejects_wrong_credentials_or_kernel_flags(self):
        for old, new in ((b"Uid=65534", b"Uid=0"), (b"Gid=65534", b"Gid=0"),
                         (b"CapEff=0000000000000000", b"CapEff=0000000000000001"),
                         (b"NoNewPrivs=1", b"NoNewPrivs=0"), (b"Seccomp=2", b"Seccomp=0")):
            with self.subTest(old=old), self.assertRaises(ValueError):
                self.validate(self.valid.replace(old, new))

    def test_rejects_unsafe_mounts_or_write_results(self):
        for old, new in ((b"root.mountopts=ro", b"root.mountopts=rw"),
                         (b"root.mountopts=ro", b"root.mountopts=ro,rw"),
                         (b",noexec", b""), (b",nosuid", b""), (b",nodev", b""),
                         (b",noexec", b",noexec,exec"),
                         (b"root.write=EROFS", b"root.write=EACCES"),
                         (b"tmp.write=ok", b"tmp.write=failed"),
                         (b"tmp.owner_mode=65534:65534:700", b"tmp.owner_mode=0:0:700"),
                         (b"tmp.owner_mode=65534:65534:700", b"tmp.owner_mode=65534:65534:777")):
            with self.subTest(old=old), self.assertRaises(ValueError):
                self.validate(self.valid.replace(old, new))

    def test_rejects_missing_duplicate_or_unexpected_security(self):
        for data in (self.valid.replace(b"Seccomp=2\n", b""), self.valid + b"Seccomp=2\n",
                     self.valid + b"unknown=1\n", self.valid + b"invalid line\n"):
            with self.subTest(data=data), self.assertRaises(ValueError):
                self.validate(data)

    def test_combined_parser_preserves_both_checks(self):
        from scripts.lean_rootless_ci_probe import validate_runtime_observations
        cgroup = (b"memory.max=2147483648\nmemory.swap.max=0\n"
                  b"pids.max=64\ncpu.max=100000 100000\n")
        network = network_fixture_observation()
        result = validate_runtime_observations(cgroup + self.valid + network)
        self.assertEqual(len(result), 20)
        for invalid in (cgroup + self.valid.replace(b"Seccomp=2", b"Seccomp=0") + network,
                        cgroup.replace(b"pids.max=64", b"pids.max=max") + self.valid + network,
                        cgroup + self.valid + network + b"cpu.max=100000 100000\n",
                        cgroup + self.valid,
                        cgroup + self.valid + network.replace(b"net.docker_socket=absent", b"net.docker_socket=present")):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                validate_runtime_observations(invalid)

    def test_fixture_reads_its_own_process_status_and_mountinfo(self):
        from scripts.lean_rootless_ci_probe import _FIXTURE
        self.assertIn('"/proc/$$/status"', _FIXTURE)
        self.assertIn('"/proc/$$/mountinfo"', _FIXTURE)


class RuntimeFailureReportTests(unittest.TestCase):
    def test_known_fixture_failure_is_blocked(self):
        from scripts.lean_rootless_ci_probe import runtime_failure_report
        for code, stage in ((11, "root_write_unexpected_success"),
                            (12, "root_write_not_readonly_error"),
                            (24, "root_fixture_mode"), (25, "tmp_write"),
                            (27, "tmp_remove"), (32, "network_dev_read"),
                            (33, "network_ipv4_read"), (34, "network_ipv6_read"),
                            (35, "network_base64_encode"), (36, "network_base64_unwrap"),
                            (37, "network_temp_remove"), (38, "network_row_serialize")):
            with self.subTest(code=code):
                report = runtime_failure_report(
                    [{"Id": "c", "Image": "i", "State": {"Status": "exited", "ExitCode": code}}],
                    container_id="c", image_id="i")
                self.assertEqual(report["stage"], stage)
                self.assertEqual(report["exit_code"], code)
                self.assertEqual(report["status"], "blocked")
                self.assertFalse(report["execution_allowed"])
                self.assertFalse(report["certificate"])
                self.assertEqual(report["proof_status"], "not_run")

    def test_rejects_unconfirmed_identity_and_state(self):
        from scripts.lean_rootless_ci_probe import runtime_failure_report
        for records, stage in (
            ([{"Id": "other", "Image": "i", "State": {"Status": "exited", "ExitCode": 25}}],
             "state_identity_unconfirmed"),
            ([{"Id": "c", "Image": "i", "State": {"Status": "exited", "ExitCode": True}}],
             "state_unconfirmed"),
            ([{"Id": "c", "Image": "i", "State": {"Status": "running", "ExitCode": 0}}],
             "container_not_exited"),
        ):
            with self.subTest(stage=stage):
                result = runtime_failure_report(records, container_id="c", image_id="i")
                self.assertEqual(result["stage"], stage)
                self.assertEqual(result["status"], "blocked")
                self.assertFalse(result["certificate"])

    def test_unknown_failure_does_not_claim_known_cause(self):
        from scripts.lean_rootless_ci_probe import runtime_failure_report
        result = runtime_failure_report(
            [{"Id": "c", "Image": "i", "State": {"Status": "exited", "ExitCode": 1}}],
            container_id="c", image_id="i")
        self.assertEqual(result["stage"], "unclassified_fixture_failure")
        self.assertEqual(result["status"], "blocked")


class RuntimeNetworkEncodingTests(unittest.TestCase):
    def test_row_serialization_preserves_raw_rows(self):
        from scripts.lean_rootless_ci_probe import _decode_network_table
        raw = "header\n" + "row " * 40 + "\nlast row\n"
        self.assertEqual(_decode_network_table(raw.replace("\n", ";")), raw.splitlines())
        for invalid in ("header", "header;;", "header;\x00;", "header;\r;", "header; ;",
                        "x" * 32769 + ";"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                _decode_network_table(invalid)

    def test_fixture_uses_portable_encoding_and_distinct_read_codes(self):
        from scripts.lean_rootless_ci_probe import _FIXTURE
        self.assertNotIn("/bin/busybox base64", _FIXTURE)
        self.assertIn('awk \'{if (index($0, ";")) exit 1; printf "%s;", $0}\'', _FIXTURE)
        for key, code in (("dev", 32), ("route", 33), ("ipv6_route", 34)):
            self.assertIn(f"{key}) read_code={code} ;;", _FIXTURE)
        self.assertIn('|| exit "$read_code"', _FIXTURE)
        self.assertIn("|| exit 38", _FIXTURE)


class RuntimeLifecycleTests(unittest.TestCase):
    cid = "a" * 64
    image = "sha256:" + "b" * 64

    def state(self, code=42, **changes):
        return [{"Id": self.cid, "Image": self.image,
                 "State": {"Status": "exited", "Running": False, "ExitCode": code,
                           "OOMKilled": False, **changes}}]

    def test_exact_exit_code_and_identity(self):
        from scripts.lean_rootless_ci_probe import validate_exited_fixture
        for code in (0, 42):
            self.assertEqual(validate_exited_fixture(self.state(code), container_id=self.cid,
                             image_id=self.image, expected_exit=code)["exit_code"], code)
        for records in (self.state(0), self.state(True), self.state(Running=True),
                        self.state(Status="running"), self.state(OOMKilled=True),
                        [{"Id": "wrong", "Image": self.image, "State": self.state()[0]["State"]}],
                        [{"Id": self.cid, "Image": "wrong", "State": self.state()[0]["State"]}]):
            with self.subTest(records=records), self.assertRaises(ValueError):
                validate_exited_fixture(records, container_id=self.cid,
                                       image_id=self.image, expected_exit=42)

    def test_cleanup_requires_independent_successful_empty_listing(self):
        from scripts.lean_rootless_ci_probe import remove_and_confirm
        calls = []
        def call(*args):
            calls.append(args)
            return b""
        remove_and_confirm(call, self.cid)
        self.assertEqual(calls, [
            ("container", "rm", "--force", self.cid),
            ("container", "ls", "--all", "--no-trunc", "--filter", "id=" + self.cid,
             "--format", "{{.ID}}")])

    def test_cleanup_rejects_remaining_container_or_failed_daemon_query(self):
        from scripts.lean_rootless_ci_probe import remove_and_confirm
        for mode in ("remaining", "listing_error", "remove_error"):
            def call(*args):
                if args[1] == "rm":
                    if mode == "remove_error":
                        raise ValueError("remove failed")
                    return b""
                if mode == "listing_error":
                    raise TimeoutError("daemon unavailable")
                return self.cid.encode("ascii") + b"\n"
            with self.subTest(mode=mode), self.assertRaises((ValueError, TimeoutError)):
                remove_and_confirm(call, self.cid)

    def test_invalid_id_never_issues_cleanup_command(self):
        from scripts.lean_rootless_ci_probe import remove_and_confirm
        def call(*args):
            self.fail("invalid identity reached daemon")
        with self.assertRaises(ValueError):
            remove_and_confirm(call, "short")
