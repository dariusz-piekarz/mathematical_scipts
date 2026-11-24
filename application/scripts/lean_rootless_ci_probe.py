"""Real Docker rootless preflight on a dedicated CI host, using a fixed fixture.

No Lean, untrusted payload, registry access or user-provided code. The fixture
image is constructed from a system static BusyBox with a harmless entrypoint.
The preflight remains configuration-only. A separate CI-only runtime probe
starts the fixed harmless fixture to observe cgroup, security and network state.
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import uuid

from backend import lean_draft_transport as transport
from backend import lean_draft_runner as policy



# Fixed fixture: no input, no user code, no network or resource stress.
_FIXTURE = """#!/bin/busybox sh
set -eu
for key in memory.max memory.swap.max pids.max cpu.max; do
    value=$(/bin/busybox cat "/sys/fs/cgroup/$key") || exit 20
    printf '%s=%s\\n' "$key" "$value"
done
# Observe the actual credentials and kernel flags of the fixture shell.
/bin/busybox awk '
    /^(Uid|Gid):/ {key=$1; sub(/:$/, "", key); printf "%s=%s %s %s %s\\n",key,$2,$3,$4,$5}
    /^(CapEff|NoNewPrivs|Seccomp):/ {key=$1; sub(/:$/, "", key); printf "%s=%s\\n",key,$2}
' "/proc/$$/status" || exit 21
/bin/busybox awk '
    $5 == "/" {print "root.mountopts=" $6}
    $5 == "/tmp" {print "tmp.mountopts=" $6}
' "/proc/$$/mountinfo" || exit 22
# The image file is world-writable by mode, so a permissions-only refusal
# is not enough. Require the actual read-only filesystem error.
mode=$(/bin/busybox stat -c %a /opt/atlas/write-check) || exit 23
test "$mode" = 666 || exit 24
if err=$(LC_ALL=C /bin/busybox touch /opt/atlas/write-check 2>&1); then
    exit 11
fi
case "$err" in
    *"Read-only file system"*) printf 'root.write=EROFS\\n' ;;
    *) exit 12 ;;
esac
# Require the actual mount ownership and private mode, independently of write success.
tmp_owner=$(/bin/busybox stat -c '%u:%g:%a' /tmp) || exit 28
printf 'tmp.owner_mode=%s\\n' "$tmp_owner"
test "$tmp_owner" = 65534:65534:700 || exit 29
printf 'atlas-runtime-fixture' > /tmp/atlas-write-check || exit 25
test "$(/bin/busybox cat /tmp/atlas-write-check)" = atlas-runtime-fixture || exit 26
/bin/busybox rm /tmp/atlas-write-check || exit 27
printf 'tmp.write=ok\\n'
# Read kernel tables without opening a network connection. Encode raw tables
# to preserve row boundaries and let the host validator check their structure.
for key in dev route ipv6_route; do
    case "$key" in
        dev) read_code=32 ;;
        route) read_code=33 ;;
        ipv6_route) read_code=34 ;;
    esac
    # Separate kernel read errors from serialization failures. The kernel
    # tables contain no semicolons; reject a delimiter in the input.
    /bin/busybox cat "/proc/net/$key" > /tmp/atlas-net-table || exit "$read_code"
    data=$(/bin/busybox awk '{if (index($0, ";")) exit 1; printf "%s;", $0}' /tmp/atlas-net-table) || exit 38
    /bin/busybox rm /tmp/atlas-net-table || exit 37
    printf 'net.%s=%s\\n' "$key" "$data"
done
# No attempt to connect to a daemon. Check known paths and dangling links.
for path in /var/run/docker.sock /run/docker.sock /run/user/*/docker.sock; do
    if test -e "$path" || test -L "$path"; then
        exit 31
    fi
done
printf 'net.docker_socket=absent\\n'
"""


def validate_runtime_limits(output: bytes) -> dict:
    """Require actual cgroup v2 observations, not Docker inspect metadata."""
    expected = {"memory.max": str(policy.MEMORY_BYTES),
                "memory.swap.max": "0", "pids.max": str(policy.PIDS_LIMIT)}
    values = {}
    for line in output.decode("ascii").splitlines():
        key, sep, value = line.partition("=")
        if not sep or key in values:
            raise ValueError("Malformed or duplicate cgroup observation")
        values[key] = value
    if set(values) != set(expected) | {"cpu.max"}:
        raise ValueError("Missing or unexpected cgroup observation")
    if any(values[k] != v for k, v in expected.items()):
        raise ValueError("Actual memory, swap or PID limit differs from policy")
    fields = values["cpu.max"].split()
    if (len(fields) != 2 or any(not field.isascii() or not field.isdecimal() for field in fields)
            or int(fields[0]) <= 0 or int(fields[0]) != int(fields[1])):
        raise ValueError("Actual CPU quota differs from one CPU")
    return values



def validate_runtime_security(output: bytes) -> dict:
    """Check observed credentials, kernel restrictions and filesystem probes."""
    values = {}
    for line in output.decode("ascii").splitlines():
        key, sep, value = line.partition("=")
        if not sep or key in values:
            raise ValueError("Malformed or duplicate security observation")
        values[key] = value
    exact = {"Uid": "65534 65534 65534 65534", "Gid": "65534 65534 65534 65534",
             "CapEff": "0000000000000000", "NoNewPrivs": "1", "Seccomp": "2",
             "root.write": "EROFS", "tmp.write": "ok",
             "tmp.owner_mode": "65534:65534:700"}
    if set(values) != set(exact) | {"root.mountopts", "tmp.mountopts"}:
        raise ValueError("Missing or unexpected security observation")
    if any(values[k] != v for k, v in exact.items()):
        raise ValueError("Runtime credentials, restrictions or write probes differ")
    root_opts = set(values["root.mountopts"].split(","))
    tmp_opts = set(values["tmp.mountopts"].split(","))
    if "ro" not in root_opts or "rw" in root_opts:
        raise ValueError("Root mount must be read-only")
    if not {"rw", "noexec", "nosuid", "nodev"} <= tmp_opts or tmp_opts & {"ro", "exec", "suid", "dev"}:
        raise ValueError("Unexpected runtime temporary mount options")
    return values



_NET_KEYS = {b"net.dev", b"net.route", b"net.ipv6_route", b"net.docker_socket"}


def _decode_network_table(value: str) -> list[str]:
    if len(value) > 32768:
        raise ValueError("Oversized network observation")
    if not value:
        return []
    if not value.endswith(";") or any(c != "\t" and not 32 <= ord(c) <= 126 for c in value):
        raise ValueError("Malformed network observation encoding")
    rows = value[:-1].split(";")
    if any(not row.strip() for row in rows):
        raise ValueError("Empty network observation row")
    return rows


def _hex_field(value: str, width: int) -> bool:
    return re.fullmatch("[0-9a-fA-F]{" + str(width) + "}", value) is not None


def validate_runtime_network(output: bytes) -> dict:
    """Verify observed kernel interface/route tables, not just NetworkMode."""
    values = {}
    for line in output.decode("ascii").splitlines():
        key, sep, value = line.partition("=")
        if not sep or key in values:
            raise ValueError("Malformed or duplicate network observation")
        values[key] = value
    if set(values) != {key.decode("ascii") for key in _NET_KEYS}:
        raise ValueError("Missing or unexpected network observation")
    if values["net.docker_socket"] != "absent":
        raise ValueError("Unexpected Docker socket path")
    dev = _decode_network_table(values["net.dev"])
    if (len(dev) != 3 or dev[0].split() != ["Inter-|", "Receive", "|", "Transmit"]
            or dev[1].split("|")[0].strip() != "face"
            or len(dev[1].split("|")) != 3):
        raise ValueError("Expected exactly one network interface")
    interface, sep, counters = dev[2].partition(":")
    fields = counters.split()
    if (not sep or interface.strip() != "lo" or len(fields) != 16
            or any(not field.isdecimal() for field in fields)):
        raise ValueError("Expected loopback interface only")
    ipv4 = _decode_network_table(values["net.route"])
    if not ipv4 or ipv4[0].split() != [
        "Iface", "Destination", "Gateway", "Flags", "RefCnt", "Use",
        "Metric", "Mask", "MTU", "Window", "IRTT"
    ]:
        raise ValueError("Malformed IPv4 routing table")
    for line in ipv4[1:]:
        f = line.split()
        if (len(f) != 11 or any(not _hex_field(f[i], 8) for i in (1, 2, 7))
                or not _hex_field(f[3], 4)
                or any(not f[i].isdecimal() for i in (4, 5, 6, 8, 9, 10))):
            raise ValueError("Malformed IPv4 route")
        # A loopback-only namespace may have local routes, never a gateway.
        if (f[0] != "lo" or f[2] != "00000000"
                or (f[1] == "00000000" and f[7] == "00000000")):
            raise ValueError("Unexpected IPv4 route")
    ipv6 = _decode_network_table(values["net.ipv6_route"])
    # The kernel may provide reject default routes on lo even without egress.
    # A successful empty read is possible with IPv6 disabled; require actual
    # kernel evidence rather than accepting an empty/omitted table.
    if not ipv6:
        raise ValueError("Empty IPv6 routing table is unconfirmed")
    for line in ipv6:
        f = line.split()
        widths = (32, 2, 32, 2, 32, 8, 8, 8, 8)
        if (len(f) != 10 or any(not _hex_field(v, n) for v, n in zip(f, widths))
                or int(f[1], 16) > 128 or int(f[3], 16) > 128):
            raise ValueError("Malformed IPv6 route")
        if f[9] != "lo" or f[4] != "0" * 32:
            raise ValueError("Unexpected IPv6 interface or gateway")
        if f[0] == "0" * 32 and int(f[1], 16) == 0 and not int(f[8], 16) & 0x200:
            raise ValueError("Usable IPv6 default route")
    return {"net.interfaces": "lo", "net.ipv4_default": "absent",
            "net.ipv6_usable_default": "absent", "net.docker_socket": "absent",
            "net.ipv4_rows": len(ipv4) - 1, "net.ipv6_rows": len(ipv6)}


def validate_runtime_observations(output: bytes) -> dict:
    cgroup = []
    security = []
    network = []
    for line in output.splitlines():
        key = line.partition(b"=")[0]
        if key in {b"memory.max", b"memory.swap.max", b"pids.max", b"cpu.max"}:
            cgroup.append(line)
        elif key in _NET_KEYS:
            network.append(line)
        else:
            security.append(line)
    return {**validate_runtime_limits(b"\n".join(cgroup)),
            **validate_runtime_security(b"\n".join(security)),
            **validate_runtime_network(b"\n".join(network))}



_FIXTURE_EXIT_STAGES = {
    11: "root_write_unexpected_success", 12: "root_write_not_readonly_error",
    20: "cgroup_read", 21: "process_status_read", 22: "mountinfo_read",
    23: "root_fixture_stat", 24: "root_fixture_mode", 25: "tmp_write",
    26: "tmp_readback", 27: "tmp_remove", 28: "tmp_stat", 29: "tmp_owner_mode",
    30: "network_table_read", 31: "docker_socket_present",
    32: "network_dev_read", 33: "network_ipv4_read", 34: "network_ipv6_read",
    35: "network_base64_encode", 36: "network_base64_unwrap", 37: "network_temp_remove",
    38: "network_row_serialize",
}


def runtime_failure_report(records: object, *, container_id: str, image_id: str) -> dict:
    """Report only bounded, typed state of the fixed CI fixture; never declare success."""
    report = {"status": "blocked", "execution_allowed": False,
              "proof_status": "not_run", "certificate": False}
    if (type(records) is not list or len(records) != 1 or type(records[0]) is not dict
            or records[0].get("Id") != container_id or records[0].get("Image") != image_id):
        return {**report, "stage": "state_identity_unconfirmed"}
    state = records[0].get("State")
    if type(state) is not dict or type(state.get("ExitCode")) is not int:
        return {**report, "stage": "state_unconfirmed"}
    code = state["ExitCode"]
    status = state.get("Status")
    if type(status) is not str or status not in ("created", "running", "exited", "dead", "paused", "restarting", "removing"):
        status = "unknown"
    return {**report, "container_state": status, "exit_code": code,
            "stage": (_FIXTURE_EXIT_STAGES.get(code, "unclassified_fixture_failure")
                      if status == "exited" else "container_not_exited")}



def validate_exited_fixture(records: object, *, container_id: str, image_id: str,
                            expected_exit: int) -> dict:
    """A successful CLI exit alone is not evidence of container termination."""
    if (type(records) is not list or len(records) != 1 or type(records[0]) is not dict
            or records[0].get("Id") != container_id or records[0].get("Image") != image_id):
        raise ValueError("Runtime fixture identity mismatch")
    state = records[0].get("State")
    if (type(state) is not dict or state.get("Status") != "exited"
            or state.get("Running") is not False or type(state.get("ExitCode")) is not int
            or state["ExitCode"] != expected_exit or state.get("OOMKilled") is not False):
        raise ValueError("Runtime fixture did not exit as expected")
    return {"container_state": "exited", "exit_code": state["ExitCode"]}


def remove_and_confirm(call, cid: str) -> None:
    """Use exact ID and a successful independent daemon listing, not failed inspect."""
    if not transport._CONTAINER_ID.fullmatch(cid):
        raise ValueError("Invalid cleanup identity")
    call("container", "rm", "--force", cid)
    remaining = call("container", "ls", "--all", "--no-trunc", "--filter",
                     "id=" + cid, "--format", "{{.ID}}")
    if remaining != b"":
        raise ValueError("Container removal not confirmed")


def cleanup_fixture(call, cid: str) -> None:
    try:
        remove_and_confirm(call, cid)
    except (OSError, ValueError, subprocess.SubprocessError):
        print("ATLAS_ROOTLESS_CLEANUP_FAILURE " + json.dumps({
            "status": "blocked", "container_id": cid, "cleanup_status": "unconfirmed",
            "execution_allowed": False, "proof_status": "not_run", "certificate": False,
        }, sort_keys=True), flush=True)
        raise


# An independent local scratch image, no user input or scenario arguments.
_FAILURE_FIXTURE = "#!/bin/busybox sh\nprintf 'atlas-controlled-failure\\n'\nexit 42\n"


def check_controlled_failure(prefix: list[str], env: dict[str, str], image_id: str) -> dict:
    def call(*args):
        return transport._command(prefix, args, env)

    transport.validate_engine(transport._decode_metadata(call("info", "--format", "{{json .}}")))
    policy.validate_image_inspection(transport._decode_metadata(call("image", "inspect", image_id)),
                                     approved_image_id=image_id)
    name = "atlas-draft-" + uuid.uuid4().hex
    cid = call(*policy.isolation_arguments(image_id=image_id, container_name=name)).decode("ascii").strip()
    if not transport._CONTAINER_ID.fullmatch(cid):
        raise ValueError("Ambiguous controlled failure creation: " + name)
    try:
        transport.validate_container(transport._decode_metadata(call("container", "inspect", cid)),
                                     container_id=cid, image_id=image_id, name=name)
        try:
            call("container", "start", "--attach", cid)
        except transport.DockerCommandFailed:
            # Independently verify exit 42; timeout or oversized output is not success.
            pass
        else:
            raise ValueError("Expected controlled nonzero exit")
        state = validate_exited_fixture(transport._decode_metadata(call("container", "inspect", cid)),
                                       container_id=cid, image_id=image_id, expected_exit=42)
    finally:
        cleanup_fixture(call, cid)
    return {"status": "controlled_failure_checked", **state, "image_id": image_id,
            "container_id": cid, "cleanup_status": "removed_verified",
            "execution_allowed": False, "proof_status": "not_run", "certificate": False}



_TIMEOUT_FIXTURE = "#!/bin/busybox sh\nexec /bin/busybox sleep 90\n"


def _stop_interrupted_fixture(call, cid: str, image_id: str) -> dict:
    """Prove the interrupted CLI left a running fixture, then stop that exact ID."""
    if not transport._CONTAINER_ID.fullmatch(cid) or not policy._IMAGE.fullmatch(image_id):
        raise ValueError("Invalid interrupted fixture identity")
    records = transport._decode_metadata(call("container", "inspect", cid))
    if (type(records) is not list or len(records) != 1 or type(records[0]) is not dict
            or records[0].get("Id") != cid or records[0].get("Image") != image_id):
        raise ValueError("Interrupted fixture identity mismatch")
    state = records[0].get("State")
    if (type(state) is not dict or state.get("Status") != "running"
            or state.get("Running") is not True or state.get("OOMKilled") is not False):
        raise ValueError("Running fixture after CLI interruption not confirmed")
    call("container", "kill", "--signal=KILL", cid)
    stopped = validate_exited_fixture(transport._decode_metadata(call("container", "inspect", cid)),
                                     container_id=cid, image_id=image_id, expected_exit=137)
    return stopped


def stop_timed_out_fixture(call, cid: str, image_id: str) -> dict:
    return {"running_after_cli_timeout": True, **_stop_interrupted_fixture(call, cid, image_id)}


def check_runtime_timeout(prefix: list[str], env: dict[str, str], image_id: str) -> dict:
    def call(*args):
        return transport._command(prefix, args, env)

    transport.validate_engine(transport._decode_metadata(call("info", "--format", "{{json .}}")))
    policy.validate_image_inspection(transport._decode_metadata(call("image", "inspect", image_id)),
                                     approved_image_id=image_id)
    name = "atlas-draft-" + uuid.uuid4().hex
    cid = call(*policy.isolation_arguments(image_id=image_id, container_name=name)).decode("ascii").strip()
    if not transport._CONTAINER_ID.fullmatch(cid):
        raise ValueError("Ambiguous timeout fixture creation: " + name)
    try:
        transport.validate_container(transport._decode_metadata(call("container", "inspect", cid)),
                                     container_id=cid, image_id=image_id, name=name)
        try:
            call("container", "start", "--attach", cid)
        except transport.DockerCommandTimeout:
            pass
        else:
            raise ValueError("Expected typed CLI timeout")
        # Each cleanup command has its own bounded transport budget.
        state = stop_timed_out_fixture(call, cid, image_id)
    except (OSError, ValueError, subprocess.SubprocessError):
        print("ATLAS_ROOTLESS_TIMEOUT_FAILURE " + json.dumps({
            "status": "blocked", "container_id": cid, "image_id": image_id,
            "execution_allowed": False, "proof_status": "not_run", "certificate": False,
        }, sort_keys=True), flush=True)
        raise
    finally:
        cleanup_fixture(call, cid)
    return {"status": "timeout_checked", **state, "image_id": image_id,
            "container_id": cid, "cleanup_status": "removed_verified",
            "cli_timeout_seconds": transport.COMMAND_TIMEOUT,
            "execution_allowed": False, "proof_status": "not_run", "certificate": False}



# Finite 256 KiB of harmless ASCII (twice the capture limit), followed by sleep.
# No /dev/zero, unbounded writer, persistent log or user-controlled content.
_OUTPUT_FIXTURE = """#!/bin/busybox sh
/bin/busybox awk 'BEGIN { for(i=0;i<262144;i++) printf "x" }' || exit 43
exec /bin/busybox sleep 90
"""


def check_runtime_output_limit(prefix: list[str], env: dict[str, str], image_id: str) -> dict:
    def call(*args):
        return transport._command(prefix, args, env)

    transport.validate_engine(transport._decode_metadata(call("info", "--format", "{{json .}}")))
    policy.validate_image_inspection(transport._decode_metadata(call("image", "inspect", image_id)),
                                     approved_image_id=image_id)
    name = "atlas-draft-" + uuid.uuid4().hex
    cid = call(*policy.isolation_arguments(image_id=image_id, container_name=name)).decode("ascii").strip()
    if not transport._CONTAINER_ID.fullmatch(cid):
        raise ValueError("Ambiguous output fixture creation: " + name)
    try:
        transport.validate_container(transport._decode_metadata(call("container", "inspect", cid)),
                                     container_id=cid, image_id=image_id, name=name)
        try:
            call("container", "start", "--attach", cid)
        except transport.DockerOutputLimit:
            pass
        else:
            raise ValueError("Expected typed CLI output limit")
        state = _stop_interrupted_fixture(call, cid, image_id)
    except (OSError, ValueError, subprocess.SubprocessError):
        print("ATLAS_ROOTLESS_OUTPUT_FAILURE " + json.dumps({
            "status": "blocked", "container_id": cid, "image_id": image_id,
            "execution_allowed": False, "proof_status": "not_run", "certificate": False,
        }, sort_keys=True), flush=True)
        raise
    finally:
        cleanup_fixture(call, cid)
    return {"status": "output_limit_checked", **state, "image_id": image_id,
            "container_id": cid, "cleanup_status": "removed_verified",
            "running_after_cli_output_limit": True,
            "capture_limit_bytes": transport.MAX_METADATA_BYTES,
            "execution_allowed": False, "proof_status": "not_run", "certificate": False}


def check_runtime_limits(prefix: list[str], env: dict[str, str], image_id: str) -> dict:
    """CI only; never pass source, accept commands or enable draft execution."""
    def call(*args):
        return transport._command(prefix, args, env)

    transport.validate_engine(transport._decode_metadata(call("info", "--format", "{{json .}}")))
    policy.validate_image_inspection(transport._decode_metadata(call("image", "inspect", image_id)),
                                     approved_image_id=image_id)
    name = "atlas-draft-" + uuid.uuid4().hex
    raw_id = call(*policy.isolation_arguments(image_id=image_id, container_name=name))
    cid = raw_id.decode("ascii").strip()
    if not transport._CONTAINER_ID.fullmatch(cid):
        raise ValueError("Ambiguous runtime fixture creation: " + name)
    try:
        transport.validate_container(transport._decode_metadata(call("container", "inspect", cid)),
                                     container_id=cid, image_id=image_id, name=name)
        try:
            output = call("container", "start", "--attach", cid)
        except (OSError, ValueError, subprocess.SubprocessError):
            # The production CLI helper intentionally suppresses failed output.
            # Inspect the same fixed CI container before removing it, so a
            # failure is diagnosable without exposing arbitrary process output.
            try:
                failed = transport._decode_metadata(call("container", "inspect", cid))
                report = runtime_failure_report(failed, container_id=cid, image_id=image_id)
            except (OSError, ValueError, RecursionError, subprocess.SubprocessError):
                report = {"status": "blocked", "stage": "inspection_failed",
                          "execution_allowed": False, "proof_status": "not_run", "certificate": False}
            print("ATLAS_ROOTLESS_RUNTIME_FAILURE " + json.dumps(report, sort_keys=True), flush=True)
            raise
        try:
            values = validate_runtime_observations(output)
        except ValueError:
            # Fixed local fixture only; JSON-escaped and bounded by _command.
            print("ATLAS_ROOTLESS_RUNTIME_INVALID " + json.dumps({
                "status": "blocked", "observations_raw": output.decode("ascii", errors="replace")[:4096],
                "execution_allowed": False, "proof_status": "not_run", "certificate": False,
            }, sort_keys=True), flush=True)
            raise
        state = validate_exited_fixture(transport._decode_metadata(call("container", "inspect", cid)),
                                       container_id=cid, image_id=image_id, expected_exit=0)
    finally:
        cleanup_fixture(call, cid)
    return {"status": "runtime_limits_security_network_checked", "observations": values,
            **state, "container_id": cid, "image_id": image_id, "cleanup_status": "removed_verified",
            "execution_allowed": False, "proof_status": "not_run", "certificate": False}



_REPORT_CASES = {
    "preflight": ("configuration_checked", None),
    "normal": ("runtime_limits_security_network_checked", 0),
    "controlled_failure": ("controlled_failure_checked", 42),
    "timeout": ("timeout_checked", 137),
    "output_limit": ("output_limit_checked", 137),
}
_REPORT_FLAGS = {"execution_allowed": False, "proof_status": "not_run", "certificate": False}
_REPORT_NET = {"net.interfaces": "lo", "net.ipv4_default": "absent",
               "net.ipv6_usable_default": "absent", "net.docker_socket": "absent"}


def _exact_fields(value: object, fields: dict) -> None:
    if type(value) is not dict or any(type(value.get(k)) is not type(v) or value[k] != v
                                     for k, v in fields.items()):
        raise ValueError("Unexpected report field value or type")


def _version(value: object) -> str:
    if type(value) is not str or not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+[A-Za-z0-9.+_-]{0,80}", value):
        raise ValueError("Invalid Docker version")
    return value


def report_engine_versions(records: object) -> dict:
    if type(records) is not dict or any(type(records.get(k)) is not dict for k in ("Client", "Server")):
        raise ValueError("Missing Docker client/server version")
    return {"client": _version(records["Client"].get("Version")),
            "server": _version(records["Server"].get("Version"))}


def validate_report_observations(values: object) -> None:
    """Validate the already-derived summary; not a substitute for raw kernel reads."""
    cgroup = {"memory.max", "memory.swap.max", "pids.max", "cpu.max"}
    security = {"Uid", "Gid", "CapEff", "NoNewPrivs", "Seccomp", "root.write",
                "tmp.write", "tmp.owner_mode", "root.mountopts", "tmp.mountopts"}
    net_counts = {"net.ipv4_rows", "net.ipv6_rows"}
    if type(values) is not dict or set(values) != cgroup | security | set(_REPORT_NET) | net_counts:
        raise ValueError("Incomplete report observations")
    for group, validator in ((cgroup, validate_runtime_limits), (security, validate_runtime_security)):
        if any(type(values[k]) is not str or not values[k].isascii() or
               "\n" in values[k] or "\r" in values[k] for k in group):
            raise ValueError("Malformed report observation")
        validator("\n".join(k + "=" + values[k] for k in sorted(group)).encode("ascii"))
    _exact_fields(values, _REPORT_NET)
    if (type(values["net.ipv4_rows"]) is not int or values["net.ipv4_rows"] < 0
            or type(values["net.ipv6_rows"]) is not int or values["net.ipv6_rows"] < 1):
        raise ValueError("Invalid report route counts")


def validate_success_report(report: object, *, expected_sha: str) -> None:
    """Strict successful-report contract for the fixed CI fixture only."""
    if type(expected_sha) is not str or not re.fullmatch(r"[0-9a-f]{40}", expected_sha):
        raise ValueError("Invalid expected checkout SHA")
    fields = {"schema_version": 1, "checkout_sha": expected_sha,
              "status": "runtime_checks_passed", **_REPORT_FLAGS}
    _exact_fields(report, fields)
    if set(report) != set(fields) | {"docker", "cases"}:
        raise ValueError("Unexpected report keys")
    versions = report["docker"]
    if type(versions) is not dict or set(versions) != {"client", "server"}:
        raise ValueError("Missing report versions")
    for version in versions.values():
        _version(version)
    cases = report["cases"]
    if type(cases) is not dict or set(cases) != set(_REPORT_CASES):
        raise ValueError("Missing or unexpected report cases")
    image_ids, container_ids = set(), set()
    for name, (status, exit_code) in _REPORT_CASES.items():
        record = cases[name]
        expected = {"status": status, **_REPORT_FLAGS,
                    "cleanup_status": "removed" if exit_code is None else "removed_verified"}
        if exit_code is not None:
            expected.update(container_state="exited", exit_code=exit_code)
        if name == "timeout":
            expected.update(running_after_cli_timeout=True, cli_timeout_seconds=transport.COMMAND_TIMEOUT)
        if name == "output_limit":
            expected.update(running_after_cli_output_limit=True, capture_limit_bytes=transport.MAX_METADATA_BYTES)
        _exact_fields(record, expected)
        keys = set(expected) | {"image_id"}
        if exit_code is not None:
            keys.add("container_id")
        if name == "normal":
            keys.add("observations")
        if set(record) != keys:
            raise ValueError("Unexpected report case keys")
        image = record["image_id"]
        if type(image) is not str or not policy._IMAGE.fullmatch(image):
            raise ValueError("Invalid report image ID")
        if name != "preflight":
            cid = record["container_id"]
            if type(cid) is not str or not transport._CONTAINER_ID.fullmatch(cid) or cid in container_ids:
                raise ValueError("Invalid or repeated report container ID")
            if image in image_ids:
                raise ValueError("Repeated runtime image ID")
            container_ids.add(cid)
            image_ids.add(image)
        if name == "normal":
            validate_report_observations(record["observations"])
    if cases["normal"]["image_id"] != cases["preflight"]["image_id"]:
        raise ValueError("Preflight and normal fixture image mismatch")


def build_success_report(*, checkout_sha: str, expected_sha: str, docker: dict, cases: dict) -> dict:
    report = {"schema_version": 1, "checkout_sha": checkout_sha,
              "status": "runtime_checks_passed", **_REPORT_FLAGS, "docker": docker, "cases": cases}
    validate_success_report(report, expected_sha=expected_sha)
    return report



MAX_REPORT_BYTES = 32768


def _unique_report_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate report key")
        result[key] = value
    return result


def _reject_report_constant(value):
    raise ValueError("Nonstandard JSON constant")


def read_success_report(path: Path, *, expected_sha: str) -> dict:
    """Read at most one bounded JSON document; fail closed on missing or invalid file."""
    with path.open("rb") as stream:
        raw = stream.read(MAX_REPORT_BYTES + 1)
    if not raw or len(raw) > MAX_REPORT_BYTES:
        raise ValueError("Invalid report byte length")
    try:
        report = json.loads(raw.decode("utf-8"), object_pairs_hook=_unique_report_keys,
                            parse_constant=_reject_report_constant)
    except (UnicodeError, RecursionError) as exc:
        raise ValueError("Invalid report JSON") from exc
    validate_success_report(report, expected_sha=expected_sha)
    return report


def write_success_report(path: Path, report: dict, *, expected_sha: str) -> None:
    validate_success_report(report, expected_sha=expected_sha)
    raw = (json.dumps(report, sort_keys=True, ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")
    if len(raw) > MAX_REPORT_BYTES:
        raise ValueError("Report exceeds byte limit")
    # Exclusive creation: a stale file or symlink cannot be overwritten.
    with path.open("xb") as stream:
        stream.write(raw)
    if read_success_report(path, expected_sha=expected_sha) != report:
        raise ValueError("Report serialization mismatch")


def main() -> int:
    expected_sha = os.environ.get("GITHUB_SHA", "")
    checkout_sha = subprocess.check_output(["git", "rev-parse", "HEAD"],
                                           cwd=Path(__file__).resolve().parents[2],
                                           timeout=5).decode("ascii").strip()
    if not re.fullmatch(r"[0-9a-f]{40}", expected_sha) or checkout_sha != expected_sha:
        raise ValueError("CI checkout identity mismatch")
    socket = transport._local_socket()
    with tempfile.TemporaryDirectory(prefix="atlas-rootless-fixture-") as directory:
        root = Path(directory)
        context = root / "context"
        context.mkdir()
        config = root / "config"
        config.mkdir(mode=0o700)
        busybox = Path("/bin/busybox")
        if not busybox.is_file():
            raise RuntimeError("Missing system busybox-static fixture")
        shutil.copyfile(busybox, context / "busybox")
        (context / "busybox").chmod(0o755)
        # Fixed read-only observations; the configuration preflight never starts it.
        entry = context / "run-draft"
        entry.write_text(_FIXTURE, encoding="utf-8")
        entry.chmod(0o755)
        writable = context / "write-check"
        writable.write_bytes(b"fixed harmless fixture")
        writable.chmod(0o666)
        (context / "Dockerfile").write_text(
            "FROM scratch\n"
            "COPY busybox /bin/busybox\n"
            "COPY run-draft /opt/atlas/run-draft\n"
            "COPY write-check /opt/atlas/write-check\n"
            "ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\n"
            "ENV HOME=/tmp LEAN_NUM_THREADS=1\n"
            "USER 65534:65534\n"
            "WORKDIR /tmp\n"
            'ENTRYPOINT ["/opt/atlas/run-draft"]\n',
            encoding="utf-8",
        )
        prefix = [str(transport._DOCKER), "--host", "unix://" + str(socket),
                  "--config", str(config)]
        env = {"PATH": "/usr/bin:/bin", "HOME": directory, "LANG": "C"}
        info = transport._decode_metadata(transport._command(
            prefix, ("info", "--format", "{{json .}}"), env))
        transport.validate_engine(info)
        versions = report_engine_versions(transport._decode_metadata(transport._command(
            prefix, ("version", "--format", "{{json .}}"), env)))
        iid = root / "image-id"
        subprocess.run(prefix + ["build", "--network=none", "--pull=false",
                                 "--iidfile", str(iid), str(context)],
                       env={**env, "DOCKER_BUILDKIT": "0"}, stdin=subprocess.DEVNULL,
                       check=True, timeout=120)
        image_id = iid.read_text(encoding="ascii").strip()
        try:
            result = transport.probe(image_id)
            print("ATLAS_ROOTLESS_PREFLIGHT " + json.dumps(result, sort_keys=True), flush=True)
            if (result.get("status") != "configuration_checked"
                    or result.get("cleanup_status") != "removed"
                    or result.get("execution_allowed") is not False
                    or result.get("proof_status") != "not_run"
                    or result.get("certificate") is not False):
                return 1
            runtime = check_runtime_limits(prefix, env, image_id)
            print("ATLAS_ROOTLESS_RUNTIME " + json.dumps(runtime, sort_keys=True), flush=True)
        finally:
            transport._command(prefix, ("image", "rm", image_id), env)
        # Build a separate immutable local image for a controlled failure.
        entry.write_text(_FAILURE_FIXTURE, encoding="utf-8")
        iid.unlink()
        subprocess.run(prefix + ["build", "--network=none", "--pull=false",
                                 "--iidfile", str(iid), str(context)],
                       env={**env, "DOCKER_BUILDKIT": "0"}, stdin=subprocess.DEVNULL,
                       check=True, timeout=120)
        failure_image = iid.read_text(encoding="ascii").strip()
        if not policy._IMAGE.fullmatch(failure_image) or failure_image == image_id:
            raise ValueError("Invalid controlled failure image identity")
        try:
            failure = check_controlled_failure(prefix, env, failure_image)
            print("ATLAS_ROOTLESS_LIFECYCLE " + json.dumps(failure, sort_keys=True), flush=True)
        finally:
            transport._command(prefix, ("image", "rm", failure_image), env)
        entry.write_text(_TIMEOUT_FIXTURE, encoding="utf-8")
        iid.unlink()
        subprocess.run(prefix + ["build", "--network=none", "--pull=false",
                                 "--iidfile", str(iid), str(context)],
                       env={**env, "DOCKER_BUILDKIT": "0"}, stdin=subprocess.DEVNULL,
                       check=True, timeout=120)
        timeout_image = iid.read_text(encoding="ascii").strip()
        if not policy._IMAGE.fullmatch(timeout_image) or timeout_image in (image_id, failure_image):
            raise ValueError("Invalid timeout image identity")
        try:
            timeout = check_runtime_timeout(prefix, env, timeout_image)
            print("ATLAS_ROOTLESS_TIMEOUT " + json.dumps(timeout, sort_keys=True), flush=True)
        finally:
            transport._command(prefix, ("image", "rm", timeout_image), env)
        entry.write_text(_OUTPUT_FIXTURE, encoding="utf-8")
        iid.unlink()
        subprocess.run(prefix + ["build", "--network=none", "--pull=false",
                                 "--iidfile", str(iid), str(context)],
                       env={**env, "DOCKER_BUILDKIT": "0"}, stdin=subprocess.DEVNULL,
                       check=True, timeout=120)
        output_image = iid.read_text(encoding="ascii").strip()
        if not policy._IMAGE.fullmatch(output_image) or output_image in (image_id, failure_image, timeout_image):
            raise ValueError("Invalid output fixture image identity")
        try:
            output = check_runtime_output_limit(prefix, env, output_image)
            print("ATLAS_ROOTLESS_OUTPUT " + json.dumps(output, sort_keys=True), flush=True)
        finally:
            transport._command(prefix, ("image", "rm", output_image), env)
        report = build_success_report(checkout_sha=checkout_sha, expected_sha=expected_sha,
                                      docker=versions, cases={"preflight": result, "normal": runtime,
                                      "controlled_failure": failure, "timeout": timeout,
                                      "output_limit": output})
        report_path = os.environ.get("ATLAS_ROOTLESS_REPORT_PATH")
        if not report_path:
            raise ValueError("Missing CI report output path")
        write_success_report(Path(report_path), report, expected_sha=expected_sha)
        print("ATLAS_ROOTLESS_REPORT " + json.dumps(report, sort_keys=True), flush=True)
        return 0


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--validate-report":
        read_success_report(Path(sys.argv[2]), expected_sha=os.environ.get("GITHUB_SHA", ""))
        print("ATLAS_ROOTLESS_REPORT_FILE_VALIDATED", flush=True)
        sys.exit(0)
    if len(sys.argv) != 1:
        raise SystemExit("Invalid CI probe arguments")
    sys.exit(main())
