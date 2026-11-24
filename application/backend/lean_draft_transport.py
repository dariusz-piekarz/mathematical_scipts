"""L1.5.6c: local rootless Docker preflight, never starts a container.

The first transport increment creates, inspects and removes an empty probe.
No draft, host mount, network request, or Lean execution is permitted here.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import selectors
import signal
import stat
import subprocess
import sys
import tempfile
import time
import uuid

from backend import lean_draft_runner as policy

MAX_METADATA_BYTES = 131072
COMMAND_TIMEOUT = 15
_CONTAINER_ID = re.compile(r"[0-9a-f]{64}\Z")
_DOCKER = Path("/usr/bin/docker")


def validate_engine(info: object) -> None:
    if type(info) is not dict:
        raise ValueError("Missing engine info")
    opts = info.get("SecurityOptions")
    if (type(opts) is not list or any(type(x) is not str for x in opts)
            or "name=rootless" not in opts
            or [x for x in opts if x.startswith("name=seccomp")] != ["name=seccomp,profile=builtin"]):
        raise ValueError("Rootless engine with seccomp required")
    if info.get("OSType") != "linux" or info.get("CgroupVersion") != "2":
        raise ValueError("Linux cgroup v2 required")
    for flag in ("MemoryLimit", "SwapLimit", "PidsLimit", "CpuCfsQuota"):
        if info.get(flag) is not True:
            raise ValueError("Missing engine resource support: " + flag)


def validate_container(records: object, *, container_id: str, image_id: str, name: str) -> None:
    if (type(container_id) is not str or not _CONTAINER_ID.fullmatch(container_id) or
            type(image_id) is not str or not policy._IMAGE.fullmatch(image_id) or
            type(name) is not str or not policy._NAME.fullmatch(name) or
            type(records) is not list or len(records) != 1 or type(records[0]) is not dict):
        raise ValueError("Invalid container inspection")
    r = records[0]
    if (r.get("Id") != container_id or r.get("Image") != image_id
            or r.get("Name") != "/" + name or r.get("Path") != policy.ENTRYPOINT
            or r.get("Args") != []):
        raise ValueError("Container identity mismatch")
    state, cfg, host = (r.get(k) for k in ("State", "Config", "HostConfig"))
    if any(type(x) is not dict for x in (state, cfg, host)):
        raise ValueError("Incomplete container inspection")
    if state.get("Status") != "created" or state.get("Running") is not False:
        raise ValueError("Probe must never have started")
    expected = {"NetworkMode": "none", "IpcMode": "private", "CgroupnsMode": "private",
                "ReadonlyRootfs": True, "Privileged": False,
                "Memory": policy.MEMORY_BYTES, "MemorySwap": policy.MEMORY_BYTES,
                "PidsLimit": policy.PIDS_LIMIT, "NanoCpus": 1000000000}
    for key, value in expected.items():
        if type(host.get(key)) is not type(value) or host[key] != value:
            raise ValueError("Unexpected container setting: " + key)
    if (host.get("CapDrop") != ["ALL"] or host.get("SecurityOpt") not in
            (["no-new-privileges"], ["no-new-privileges:true"], ["no-new-privileges=true"])):
        raise ValueError("Missing container privilege restriction")
    for key in ("Binds", "Mounts", "Devices", "DeviceRequests", "CapAdd", "PortBindings",
                "VolumesFrom", "Links", "DeviceCgroupRules", "GroupAdd", "ExtraHosts"):
        if host.get(key) not in (None, [], {}):
            raise ValueError("Unexpected host access: " + key)
    if r.get("Mounts") != []:
        raise ValueError("Unexpected container mounts")
    if host.get("Tmpfs") != {"/tmp": "rw,noexec,nosuid,nodev,size=16777216,mode=0700,uid=65534,gid=65534"}:
        raise ValueError("Unexpected tmpfs configuration")
    for key in ("PidMode", "UTSMode", "UsernsMode"):
        # Docker represents default private namespaces as empty strings.
        if host.get(key) != "":
            raise ValueError("Unexpected namespace: " + key)
    if host.get("PublishAllPorts") is not False or host.get("AutoRemove") is not False:
        raise ValueError("Unexpected lifecycle or published ports")
    limits = host.get("Ulimits")
    if type(limits) is not list or len(limits) != 2:
        raise ValueError("Missing explicit ulimits")
    seen = {}
    for limit in limits:
        if (type(limit) is not dict or set(limit) != {"Name", "Soft", "Hard"}
                or type(limit["Name"]) is not str
                or type(limit["Soft"]) is not int or type(limit["Hard"]) is not int
                or limit["Name"] in seen):
            raise ValueError("Malformed ulimit")
        seen[limit["Name"]] = (limit["Soft"], limit["Hard"])
    if seen != {"nofile": (256, 256), "core": (0, 0)}:
        raise ValueError("Unexpected ulimits")
    restart, log = host.get("RestartPolicy"), host.get("LogConfig")
    if type(restart) is not dict or restart.get("Name") != "no":
        raise ValueError("Restart forbidden")
    if type(log) is not dict or log.get("Type") != "none":
        raise ValueError("Persistent log forbidden")
    if cfg.get("User") != "65534:65534" or cfg.get("WorkingDir") != "/tmp":
        raise ValueError("Unexpected user or directory")
    if cfg.get("OpenStdin") is not True or cfg.get("Tty") is not False:
        raise ValueError("Unexpected input mode")
    env = cfg.get("Env")
    if (type(env) is not list or any(type(x) is not str for x in env)
            or len(env) != len(set(env)) or set(env) != policy._IMAGE_ENV):
        raise ValueError("Unexpected environment")


def _local_socket() -> Path:
    if not sys.platform.startswith("linux") or os.geteuid() == 0:
        raise ValueError("Non-root Linux host required")
    uid = os.geteuid()
    path = Path("/run/user") / str(uid) / "docker.sock"
    for p in (path.parent, path):
        st = p.lstat()
        if p.is_symlink() or st.st_uid != uid or st.st_mode & 0o022:
            raise ValueError("Untrusted Docker socket path")
    if not stat.S_ISSOCK(path.lstat().st_mode):
        raise ValueError("Local rootless Docker socket required")
    if not _DOCKER.is_file() or _DOCKER.stat().st_uid != 0 or _DOCKER.stat().st_mode & 0o022:
        raise ValueError("Trusted system Docker CLI required")
    return path


class DockerCommandTimeout(TimeoutError):
    """Local CLI time budget exceeded; no claim about daemon state."""


class DockerOutputLimit(ValueError):
    """Local CLI output exceeded the capture budget."""


class DockerCommandFailed(ValueError):
    """Local CLI returned a nonzero exit code."""


def _command(prefix: list[str], args: tuple[str, ...], env: dict[str, str]) -> bytes:
    """Bound wall time and all captured output, with no shell."""
    with subprocess.Popen(prefix + list(args), env=env, stdin=subprocess.DEVNULL,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          start_new_session=True) as p:
        assert p.stdout is not None
        out = bytearray()
        end = time.monotonic() + COMMAND_TIMEOUT
        try:
            with selectors.DefaultSelector() as sel:
                sel.register(p.stdout, selectors.EVENT_READ)
                while True:
                    remaining = end - time.monotonic()
                    if remaining <= 0 or not sel.select(remaining):
                        raise DockerCommandTimeout("Docker metadata timeout")
                    chunk = os.read(p.stdout.fileno(), 8192)
                    if not chunk:
                        break
                    if len(chunk) > MAX_METADATA_BYTES - len(out):
                        raise DockerOutputLimit("Docker metadata exceeds limit")
                    out.extend(chunk)
            try:
                returncode = p.wait(timeout=max(0.01, end-time.monotonic()))
            except subprocess.TimeoutExpired as exc:
                raise DockerCommandTimeout("Docker metadata timeout") from exc
            if returncode != 0:
                raise DockerCommandFailed("Docker command failed")
            return bytes(out)
        except BaseException:
            # Kill the local CLI group before reaping its leader: a child
            # can still hold the pipe after the leader exits.
            # This is not Docker daemon/container cleanup or a sandbox.
            if p.returncode is None:
                try:
                    os.killpg(p.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                finally:
                    p.wait(timeout=5)
            raise


def _decode_metadata(data: bytes):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("Duplicate Docker metadata member")
            result[key] = value
        return result
    def invalid_constant(_):
        raise ValueError("Invalid JSON constant")
    return json.loads(data, object_pairs_hook=unique, parse_constant=invalid_constant)


def probe(approved_image_id: str) -> dict:
    """Administrator-only preflight, not an application endpoint.

    Success means configuration inspection only. No container start, no
    payload, no proof status update. A failed create can leave an inert probe;
    cleanup uses only the ID returned by create, never a possibly unrelated
    name. An ambiguous create is reported for administrative reconciliation.
    """
    result = {"status": "blocked", "execution_allowed": False,
              "proof_status": "not_run", "certificate": False}
    if type(approved_image_id) is not str or not policy._IMAGE.fullmatch(approved_image_id):
        return {**result, "error": "invalid_approved_image"}
    name = "atlas-draft-" + uuid.uuid4().hex
    cleanup = "not_created"
    try:
        socket = _local_socket()
        with tempfile.TemporaryDirectory(prefix="atlas-docker-config-") as directory:
            prefix = [str(_DOCKER), "--host", "unix://" + str(socket), "--config", directory]
            env = {"PATH": "/usr/bin:/bin", "HOME": directory, "LANG": "C"}
            def call(*args):
                return _command(prefix, args, env)
            validate_engine(_decode_metadata(call("info", "--format", "{{json .}}")))
            policy.validate_image_inspection(_decode_metadata(call("image", "inspect", approved_image_id)),
                                             approved_image_id=approved_image_id)
            cid = None
            cleanup = "create_outcome_unknown"
            try:
                raw_id = call(*policy.isolation_arguments(image_id=approved_image_id,
                                                        container_name=name)).decode("ascii").strip()
                if not _CONTAINER_ID.fullmatch(raw_id):
                    raise ValueError("Invalid create response")
                cid = raw_id
                cleanup = "removal_unconfirmed"
                validate_container(_decode_metadata(call("container", "inspect", cid)),
                                   container_id=cid, image_id=approved_image_id, name=name)
            finally:
                # Never start a probe. Failure to remove blocks success.
                if cid is not None:
                    call("container", "rm", cid)
                    cleanup = "removed"
    except (OSError, ValueError, RecursionError, subprocess.SubprocessError):
        return {**result, "error": "preflight_failed", "cleanup_status": cleanup,
                **({"probe_name": name} if cleanup in ("create_outcome_unknown", "removal_unconfirmed") else {})}
    return {**result, "status": "configuration_checked", "image_id": approved_image_id,
            "cleanup_status": cleanup}
