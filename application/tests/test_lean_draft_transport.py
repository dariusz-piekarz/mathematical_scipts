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


class RuntimeTimeoutTests(unittest.TestCase):
    cid = "a" * 64
    image = "sha256:" + "b" * 64

    def records(self, *, running=True, cid=None, image=None, code=None):
        import json
        return json.dumps([{"Id": self.cid if cid is None else cid,
                            "Image": self.image if image is None else image,
                            "State": {"Status": "running" if running else "exited",
                                      "Running": running, "OOMKilled": False,
                                      "ExitCode": (0 if running else 137) if code is None else code}}]).encode()

    def test_timeout_requires_running_then_exact_stopped_state(self):
        from scripts.lean_rootless_ci_probe import stop_timed_out_fixture
        calls = []
        def call(*args):
            calls.append(args)
            return {1: self.records(), 2: b"", 3: self.records(running=False)}[len(calls)]
        state = stop_timed_out_fixture(call, self.cid, self.image)
        self.assertEqual(state, {"running_after_cli_timeout": True,
                                "container_state": "exited", "exit_code": 137})
        self.assertEqual(calls, [("container", "inspect", self.cid),
                                 ("container", "kill", "--signal=KILL", self.cid),
                                 ("container", "inspect", self.cid)])

    def test_timeout_rejects_wrong_identity_or_already_exited(self):
        from scripts.lean_rootless_ci_probe import stop_timed_out_fixture
        for data in (self.records(cid="other"), self.records(image="other"),
                     self.records(running=False)):
            def call(*args):
                self.assertEqual(args, ("container", "inspect", self.cid))
                return data
            with self.subTest(data=data), self.assertRaises(ValueError):
                stop_timed_out_fixture(call, self.cid, self.image)

    def test_timeout_rejects_unconfirmed_stop(self):
        from scripts.lean_rootless_ci_probe import stop_timed_out_fixture
        for data in (self.records(), self.records(running=False, code=0),
                     self.records(running=False, cid="other")):
            responses = iter((self.records(), b"", data))
            with self.subTest(data=data), self.assertRaises(ValueError):
                stop_timed_out_fixture(lambda *args: next(responses), self.cid, self.image)

    def test_transport_errors_are_distinct_and_compatible(self):
        from backend import lean_draft_transport as transport
        self.assertTrue(issubclass(transport.DockerCommandTimeout, TimeoutError))
        self.assertTrue(issubclass(transport.DockerOutputLimit, ValueError))
        self.assertTrue(issubclass(transport.DockerCommandFailed, ValueError))
        self.assertFalse(issubclass(transport.DockerOutputLimit, transport.DockerCommandFailed))


class RuntimeOutputLimitTests(unittest.TestCase):
    def test_exact_capture_boundary_and_one_byte_over(self):
        import sys
        from unittest.mock import patch
        from backend import lean_draft_transport as transport
        with patch.object(transport, "MAX_METADATA_BYTES", 8192):
            for size in (0, 8192):
                raw = transport._command([sys.executable, "-I", "-c"],
                                         (f"import sys; sys.stdout.buffer.write(b'x'*{size})",), {})
                self.assertEqual(raw, b"x" * size)
            with self.assertRaises(transport.DockerOutputLimit):
                transport._command([sys.executable, "-I", "-c"],
                                   ("import sys; sys.stdout.buffer.write(b'x'*8193)",), {})

    def test_combined_stdout_and_stderr_are_bounded(self):
        import sys
        from unittest.mock import patch
        from backend import lean_draft_transport as transport
        with patch.object(transport, "MAX_METADATA_BYTES", 8192):
            with self.assertRaises(transport.DockerOutputLimit):
                transport._command([sys.executable, "-I", "-c"],
                                   ("import os; os.write(1,b'x'*4096); os.write(2,b'y'*4097)",), {})

    def test_output_fixture_requires_typed_limit_not_other_errors(self):
        from unittest.mock import patch
        from scripts import lean_rootless_ci_probe as probe
        from backend import lean_draft_transport as transport
        cid, image = "a" * 64, "sha256:" + "b" * 64
        for failure in (transport.DockerCommandTimeout("timeout"),
                        transport.DockerCommandFailed("nonzero"), ValueError("other"), None):
            def command(prefix, args, env):
                if args[0] == "create":
                    return cid.encode()
                if args[:2] == ("container", "start") and failure is not None:
                    raise failure
                return b"{}"
            with self.subTest(failure=failure), \
                    patch.object(transport, "_command", side_effect=command), \
                    patch.object(transport, "validate_engine"), \
                    patch.object(probe.policy, "validate_image_inspection"), \
                    patch.object(transport, "validate_container"), \
                    patch.object(probe, "_stop_interrupted_fixture") as stop, \
                    patch.object(probe, "cleanup_fixture") as cleanup:
                with self.assertRaises((ValueError, TimeoutError)):
                    probe.check_runtime_output_limit([], {}, image)
                stop.assert_not_called()
                cleanup.assert_called_once()

    def test_output_fixture_is_finite_and_larger_than_capture_limit(self):
        from scripts.lean_rootless_ci_probe import _OUTPUT_FIXTURE
        from backend import lean_draft_transport as transport
        self.assertIn(f"i<{2 * transport.MAX_METADATA_BYTES};", _OUTPUT_FIXTURE)
        self.assertIn("exec /bin/busybox sleep 90", _OUTPUT_FIXTURE)
        self.assertNotIn("while", _OUTPUT_FIXTURE)
        self.assertNotIn("/dev/zero", _OUTPUT_FIXTURE)


class RuntimeReportTests(unittest.TestCase):
    sha = "f" * 40

    def report(self):
        from scripts.lean_rootless_ci_probe import build_success_report
        flags = {"certificate": False, "execution_allowed": False, "proof_status": "not_run"}
        cases = {}
        for i, (name, status, code) in enumerate((
            ("normal", "runtime_limits_security_network_checked", 0),
            ("controlled_failure", "controlled_failure_checked", 42),
            ("timeout", "timeout_checked", 137), ("output_limit", "output_limit_checked", 137)
        ), 1):
            cases[name] = {**flags, "status": status, "cleanup_status": "removed_verified",
                           "image_id": "sha256:" + str(i)*64, "container_id": str(i+4)*64,
                           "exit_code": code, "container_state": "exited"}
        cases["preflight"] = {**flags, "status": "configuration_checked",
                              "cleanup_status": "removed", "image_id": cases["normal"]["image_id"]}
        cases["normal"]["observations"] = {
            "memory.max": str(policy.MEMORY_BYTES), "memory.swap.max": "0",
            "pids.max": str(policy.PIDS_LIMIT), "cpu.max": "100000 100000",
            "Uid": "65534 65534 65534 65534", "Gid": "65534 65534 65534 65534",
            "CapEff": "0000000000000000", "NoNewPrivs": "1", "Seccomp": "2",
            "root.write": "EROFS", "tmp.write": "ok", "tmp.owner_mode": "65534:65534:700",
            "root.mountopts": "ro,relatime", "tmp.mountopts": "rw,noexec,nosuid,nodev",
            "net.interfaces": "lo", "net.ipv4_default": "absent", "net.ipv6_usable_default": "absent",
            "net.docker_socket": "absent", "net.ipv4_rows": 0, "net.ipv6_rows": 3}
        cases["timeout"].update(running_after_cli_timeout=True, cli_timeout_seconds=transport.COMMAND_TIMEOUT)
        cases["output_limit"].update(running_after_cli_output_limit=True, capture_limit_bytes=transport.MAX_METADATA_BYTES)
        return build_success_report(checkout_sha=self.sha, expected_sha=self.sha,
                                    docker={"client": "28.0.4", "server": "28.0.4"}, cases=cases)

    def test_success_report_is_strict_and_checkout_bound(self):
        from scripts.lean_rootless_ci_probe import validate_success_report
        report = self.report()
        validate_success_report(report, expected_sha=self.sha)
        for key, value in (("checkout_sha", "a"*40), ("schema_version", True),
                           ("certificate", True), ("execution_allowed", True),
                           ("proof_status", "verified"), ("extra", None)):
            changed = {**report, key: value}
            with self.subTest(key=key), self.assertRaises(ValueError):
                validate_success_report(changed, expected_sha=self.sha)

    def test_missing_case_duplicate_id_or_wrong_image_is_rejected(self):
        from scripts.lean_rootless_ci_probe import validate_success_report
        for mode in ("missing", "extra", "duplicate_container", "duplicate_image", "preflight_mismatch"):
            report = self.report()
            c = report["cases"]
            if mode == "missing":
                del c["timeout"]
            elif mode == "extra":
                c["unknown"] = c["normal"]
            elif mode == "duplicate_container":
                c["timeout"]["container_id"] = c["normal"]["container_id"]
            elif mode == "duplicate_image":
                c["timeout"]["image_id"] = c["normal"]["image_id"]
            else:
                c["preflight"]["image_id"] = c["timeout"]["image_id"]
            with self.subTest(mode=mode), self.assertRaises(ValueError):
                validate_success_report(report, expected_sha=self.sha)

    def test_case_flags_cleanup_and_exit_are_not_promotable(self):
        from scripts.lean_rootless_ci_probe import validate_success_report
        for key, value in (("cleanup_status", "removed"), ("exit_code", True),
                           ("certificate", True), ("execution_allowed", True),
                           ("status", "not_run"), ("running_after_cli_timeout", False)):
            report = self.report()
            report["cases"]["timeout"][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                validate_success_report(report, expected_sha=self.sha)

    def test_missing_or_unsafe_summary_observations_are_rejected(self):
        from scripts.lean_rootless_ci_probe import validate_success_report
        for key, value in (("net.ipv4_rows", True), ("net.ipv6_rows", 0),
                           ("root.mountopts", "rw"), ("memory.max", "0"),
                           ("net.interfaces", "eth0"), ("cpu.max", "max 100000")):
            report = self.report()
            report["cases"]["normal"]["observations"][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                validate_success_report(report, expected_sha=self.sha)
        report = self.report()
        del report["cases"]["normal"]["observations"]["CapEff"]
        with self.assertRaises(ValueError):
            validate_success_report(report, expected_sha=self.sha)

    def test_engine_versions_required_from_both_endpoints(self):
        from scripts.lean_rootless_ci_probe import report_engine_versions
        self.assertEqual(report_engine_versions({"Client": {"Version": "28.0.4"},
                         "Server": {"Version": "28.0.4"}}),
                         {"client": "28.0.4", "server": "28.0.4"})
        for data in ({}, {"Client": {"Version": "28.0.4"}},
                     {"Client": {"Version": True}, "Server": {"Version": "28.0.4"}},
                     {"Client": {"Version": "28.0.4"}, "Server": {"Version": "28.0.4\n"}}):
            with self.subTest(data=data), self.assertRaises(ValueError):
                report_engine_versions(data)


class RuntimeReportFileTests(unittest.TestCase):
    def test_success_file_round_trip_and_no_overwrite(self):
        import tempfile
        from pathlib import Path
        from scripts.lean_rootless_ci_probe import read_success_report, write_success_report
        fixture = RuntimeReportTests()
        report = fixture.report()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            write_success_report(path, report, expected_sha=fixture.sha)
            self.assertEqual(read_success_report(path, expected_sha=fixture.sha), report)
            with self.assertRaises(FileExistsError):
                write_success_report(path, report, expected_sha=fixture.sha)
            with self.assertRaises(ValueError):
                read_success_report(path, expected_sha="a"*40)

    def test_duplicate_top_level_and_nested_keys_rejected(self):
        import json
        import tempfile
        from pathlib import Path
        from scripts.lean_rootless_ci_probe import read_success_report
        fixture = RuntimeReportTests()
        raw = json.dumps(fixture.report(), sort_keys=True)
        for changed in (raw.replace('"schema_version": 1', '"schema_version": 1, "schema_version": 1'),
                        raw.replace('"client": "28.0.4"', '"client": "28.0.4", "client": "28.0.4"')):
            self.assertNotEqual(raw, changed)
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "report.json"
                path.write_text(changed, encoding="utf-8")
                with self.assertRaises(ValueError):
                    read_success_report(path, expected_sha=fixture.sha)

    def test_missing_malformed_oversized_and_nonstandard_json_rejected(self):
        import tempfile
        from pathlib import Path
        from scripts.lean_rootless_ci_probe import read_success_report, MAX_REPORT_BYTES
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            with self.assertRaises(FileNotFoundError):
                read_success_report(path, expected_sha=RuntimeReportTests.sha)
            for raw in (b"", b"\xff", b"{}{}", b'{"x":NaN}', b'{"x":Infinity}',
                        b" " * (MAX_REPORT_BYTES + 1), b"[" * 2000 + b"]" * 2000):
                path.write_bytes(raw)
                with self.subTest(raw=raw[:20]), self.assertRaises(ValueError):
                    read_success_report(path, expected_sha=RuntimeReportTests.sha)

    def test_invalid_success_report_not_written(self):
        import tempfile
        from pathlib import Path
        from scripts.lean_rootless_ci_probe import write_success_report
        fixture = RuntimeReportTests()
        report = fixture.report()
        report["execution_allowed"] = True
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            with self.assertRaises(ValueError):
                write_success_report(path, report, expected_sha=fixture.sha)
            self.assertFalse(path.exists())


    def test_report_reader_rejects_symlink_and_fifo(self):
        import os
        import sys
        import tempfile
        from pathlib import Path
        from scripts.lean_rootless_ci_probe import read_success_report, write_success_report
        if not sys.platform.startswith("linux"):
            self.skipTest("Linux CI report file safety")
        fixture = RuntimeReportTests()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            valid = root / "valid.json"
            write_success_report(valid, fixture.report(), expected_sha=fixture.sha)
            link = root / "link.json"
            link.symlink_to(valid)
            fifo = root / "fifo.json"
            os.mkfifo(fifo)
            for path in (link, fifo, root):
                with self.subTest(path=path), self.assertRaises((OSError, ValueError)):
                    read_success_report(path, expected_sha=fixture.sha)


class RuntimeDiagnosticReportTests(unittest.TestCase):
    sha = "f" * 40

    def test_every_failure_stage_and_progress(self):
        from scripts.lean_rootless_ci_probe import build_failure_report, _DIAGNOSTIC_STAGES
        cases = _DIAGNOSTIC_STAGES[1:-1]
        for i, stage in enumerate(_DIAGNOSTIC_STAGES):
            completed = cases[:max(0, i-1)]
            report = build_failure_report(expected_sha=self.sha, stage=stage, completed=completed)
            self.assertEqual(report["status"], "runtime_checks_failed")
            self.assertFalse(report["execution_allowed"])
            self.assertFalse(report["certificate"])
            self.assertEqual(report["proof_status"], "not_run")
            for j, name in enumerate(cases, 1):
                self.assertEqual(report["cases"][name], "passed" if j < i else
                                 "failed" if j == i else "not_run")

    def test_reject_inconsistent_progress_and_flags(self):
        from scripts.lean_rootless_ci_probe import build_failure_report, validate_failure_report
        for completed in ((), ("normal",), ("preflight", "normal")):
            with self.assertRaises(ValueError):
                build_failure_report(expected_sha=self.sha, stage="normal", completed=completed)
        for key, value in (("certificate", True), ("execution_allowed", True),
                           ("proof_status", "verified"), ("status", "runtime_checks_passed"),
                           ("failed_stage", "unknown")):
            report = build_failure_report(expected_sha=self.sha, stage="normal", completed=("preflight",))
            report[key] = value
            with self.assertRaises(ValueError):
                validate_failure_report(report, expected_sha=self.sha)
        report = build_failure_report(expected_sha=self.sha, stage="normal", completed=("preflight",))
        report["cases"]["timeout"] = "passed"
        with self.assertRaises(ValueError):
            validate_failure_report(report, expected_sha=self.sha)

    def test_failure_file_never_accepted_as_success(self):
        import tempfile
        from pathlib import Path
        from scripts.lean_rootless_ci_probe import (build_failure_report, read_failure_report,
                                                     write_failure_report, read_success_report)
        report = build_failure_report(expected_sha=self.sha, stage="setup", completed=())
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "failure.json"
            write_failure_report(path, report, expected_sha=self.sha)
            self.assertEqual(read_failure_report(path, expected_sha=self.sha), report)
            with self.assertRaises(ValueError):
                read_success_report(path, expected_sha=self.sha)
            with self.assertRaises(FileExistsError):
                write_failure_report(path, report, expected_sha=self.sha)

    def test_main_preserves_failure_and_reports_only_verified_checkout(self):
        import os
        import tempfile
        from pathlib import Path
        from unittest.mock import patch
        from scripts import lean_rootless_ci_probe as probe
        for verified in (False, True):
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "failure.json"
                def failing(progress):
                    if verified:
                        progress.update(checkout_sha=self.sha, stage="normal", completed=["preflight"])
                    raise RuntimeError("private exception text")
                with patch.dict(os.environ, {"ATLAS_ROOTLESS_FAILURE_REPORT_PATH": str(path)}), \
                        patch.object(probe, "run_probe", side_effect=failing):
                    with self.assertRaisesRegex(RuntimeError, "private exception text"):
                        probe.main()
                self.assertEqual(path.exists(), verified)
                if verified:
                    report = probe.read_failure_report(path, expected_sha=self.sha)
                    self.assertEqual(report["cases"]["normal"], "failed")
                    self.assertNotIn("private exception text", path.read_text())


    def test_diagnostic_write_failure_preserves_original_exception(self):
        import os
        import tempfile
        from pathlib import Path
        from unittest.mock import patch
        from scripts import lean_rootless_ci_probe as probe
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "missing-parent" / "failure.json"
            original = RuntimeError("original probe failure")
            def failing(progress):
                progress.update(checkout_sha=self.sha, stage="normal", completed=["preflight"])
                raise original
            with patch.dict(os.environ, {"ATLAS_ROOTLESS_FAILURE_REPORT_PATH": str(path)}), \
                    patch.object(probe, "run_probe", side_effect=failing):
                with self.assertRaises(RuntimeError) as caught:
                    probe.main()
            self.assertIs(caught.exception, original)
            self.assertFalse(path.exists())


class TransportTestDiscoveryTests(unittest.TestCase):
    def test_no_shadowed_test_classes_or_methods(self):
        import ast
        from collections import Counter
        from pathlib import Path

        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
        classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
        duplicate_classes = [name for name, count in Counter(
            node.name for node in classes).items() if count > 1]
        self.assertEqual(duplicate_classes, [], "Duplicate top-level test class names")
        for cls in classes:
            methods = [node.name for node in cls.body
                       if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                       and node.name.startswith("test_")]
            with self.subTest(cls=cls.name):
                self.assertEqual([name for name, count in Counter(methods).items() if count > 1],
                                 [], "Duplicate test method names")
        required = {
            "RuntimeFailureReportTests": {
                "test_known_fixture_failure_is_blocked",
                "test_rejects_unconfirmed_identity_and_state",
                "test_unknown_failure_does_not_claim_known_cause",
            },
            "RuntimeDiagnosticReportTests": {
                "test_every_failure_stage_and_progress",
                "test_failure_file_never_accepted_as_success",
                "test_main_preserves_failure_and_reports_only_verified_checkout",
                "test_reject_inconsistent_progress_and_flags",
                "test_diagnostic_write_failure_preserves_original_exception",
            },
        }
        for name, expected in required.items():
            cls = globals().get(name)
            self.assertIsNotNone(cls, name)
            discovered = set(unittest.defaultTestLoader.getTestCaseNames(cls))
            self.assertTrue(expected <= discovered, (name, expected - discovered))



class SharedCleanupDeadlineTests(unittest.TestCase):
    def test_shared_deadline_is_not_reset_between_calls(self):
        from unittest.mock import patch
        with patch.object(transport.time, "monotonic", side_effect=[100, 101, 120, 130]), \
                patch.object(transport, "_command", return_value=b"") as command:
            call = transport.cleanup_command(["docker"], {})
            call("container", "rm", "a" * 64)
            call("container", "ls")
            with self.assertRaises(transport.DockerCleanupDeadline):
                call("container", "inspect", "a" * 64)
            self.assertEqual(command.call_count, 2)
            self.assertEqual([c.kwargs["deadline"] for c in command.call_args_list], [130, 130])

    def test_expired_or_nonfinite_deadline_never_spawns(self):
        import time
        with patch.object(transport.subprocess, "Popen") as spawn:
            for deadline in (time.monotonic() - 1, float("nan"), float("inf")):
                with self.subTest(deadline=deadline), self.assertRaises(transport.DockerCleanupDeadline):
                    transport._command(["docker"], ("info",), {}, deadline=deadline)
            spawn.assert_not_called()

    @unittest.skipUnless(__import__("sys").platform.startswith("linux"), "Linux subprocess")
    def test_real_command_respects_short_shared_deadline(self):
        import sys
        import time
        start = time.monotonic()
        with self.assertRaises(transport.DockerCommandTimeout):
            transport._command([sys.executable, "-I", "-c"], ("import time; time.sleep(30)",), {},
                               deadline=start + 1)
        self.assertLess(time.monotonic() - start, 2.5)

    def test_unconfirmed_reap_does_not_enter_implicit_context_wait(self):
        import subprocess
        from unittest.mock import Mock
        proc = Mock()
        proc.returncode = None
        proc.pid = 12345
        proc.wait.side_effect = subprocess.TimeoutExpired("fake", 0)
        with patch.object(transport.subprocess, "Popen", return_value=proc), \
                patch.object(transport.os, "killpg") as kill, \
                patch.object(transport.selectors, "DefaultSelector", side_effect=ValueError("fake selector")):
            with self.assertRaises(transport.DockerCLIReapUnconfirmed):
                transport._command(["docker"], ("info",), {})
        kill.assert_called_once()
        proc.wait.assert_called_once()
        proc.stdout.close.assert_called_once()


    def test_unconfirmed_reap_and_cleanup_deadline_are_not_expected_cli_timeout(self):
        from scripts import lean_rootless_ci_probe as probe
        for error in (transport.DockerCLIReapUnconfirmed, transport.DockerCleanupDeadline):
            self.assertFalse(issubclass(error, transport.DockerCommandTimeout))
            self.assertTrue(issubclass(error, TimeoutError))
            for fixture in (probe.check_runtime_timeout, probe.check_runtime_output_limit):
                failure = error("unconfirmed")
                def command(prefix, args, env):
                    if args[0] == "create":
                        return b"a" * 64
                    if args[:2] == ("container", "start"):
                        raise failure
                    return b"{}"
                with self.subTest(error=error.__name__, fixture=fixture.__name__), \
                        patch.object(transport, "_command", side_effect=command), \
                        patch.object(transport, "validate_engine"), \
                        patch.object(probe.policy, "validate_image_inspection"), \
                        patch.object(transport, "validate_container"), \
                        patch.object(probe, "_stop_interrupted_fixture") as stop, \
                        patch.object(probe, "cleanup_fixture") as cleanup:
                    with self.assertRaises(error) as caught:
                        fixture([], {}, "sha256:" + "b" * 64)
                    self.assertIs(caught.exception, failure)
                    stop.assert_not_called()
                    cleanup.assert_called_once()
