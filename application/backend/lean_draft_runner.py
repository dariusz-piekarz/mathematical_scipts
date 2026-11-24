"""Experimental L1.5.6b admission and fixed OCI isolation contract.

No execution is enabled by this module. The transport must be implemented and
verified separately on an actual rootless engine before an execution path is
exposed. Never fall back to the registered Lean runner.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import re

from backend import lean_draft_generator

_HEX = re.compile(r"[0-9a-f]{64}\Z")
_IMAGE = re.compile(r"sha256:[0-9a-f]{64}\Z")
_NAME = re.compile(r"atlas-draft-[0-9a-f]{32}\Z")
MAX_OUTPUT_BYTES = 16000
TIMEOUT_SECONDS = 45
MEMORY_BYTES = 2 * 1024**3
PIDS_LIMIT = 64
INPUT_PATH = "/tmp/Draft.lean"
ENTRYPOINT = "/opt/atlas/run-draft"
_IMAGE_ENV = frozenset({
    "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    "HOME=/tmp", "LEAN_NUM_THREADS=1",
})


@dataclass(frozen=True)
class PreparedDraft:
    """Internal data, never a client-supplied execution capability."""
    source_sha256: str
    ast_sha256: str
    lean_code_sha256: str
    input_sha256: str
    input_bytes: bytes


def prepare(source: str, *, segments: list | None = None,
            expected_source_sha256: str, expected_ast_sha256: str,
            expected_code_sha256: str, consent: bool = False) -> tuple[dict, PreparedDraft | None]:
    """Regenerate rather than accept arbitrary Lean, AST or a cached result.

    Consent is separate from generation and bound to all three digests.
    No subprocess, file, network operation or registry write occurs.
    """
    flags = {"status": "blocked", "proof_status": "not_run",
             "statement_status": "needs_review", "certificate": False,
             "execution_allowed": False, "external_transfer_allowed": False,
             "external_cost_minor_units": 0}
    if consent is not True:
        return {**flags, "error": "execution_consent_required"}, None
    hashes = (expected_source_sha256, expected_ast_sha256, expected_code_sha256)
    if any(type(h) is not str or not _HEX.fullmatch(h) for h in hashes):
        return {**flags, "error": "invalid_expected_digest"}, None
    r = lean_draft_generator.generate(source, segments=segments, consent=True)
    if r["status"] != "generated":
        return {**flags, "error": "regeneration_rejected"}, None
    actual = (r["source_sha256"], r["ast_sha256"], r["lean_code_sha256"])
    if actual != hashes:
        return {**flags, "error": "stale_candidate"}, None
    payload = (r["lean_code"] + "\n#print axioms atlas_draft\n").encode("utf-8")
    draft = PreparedDraft(*actual, hashlib.sha256(payload).hexdigest(), payload)
    return {**flags, "error": "isolated_transport_not_verified",
            "admission_status": "prepared", "input_sha256": draft.input_sha256}, draft


def validate_image_inspection(inspection: object, *, approved_image_id: str) -> None:
    """Fail closed on Docker image metadata before a future transport.

    approved_image_id comes from trusted local administration, never from
    the client or inspection itself. This checks metadata only; the future
    transport must fetch it from the same local rootless engine that creates
    the container, and verify actual container configuration before start.
    A matching ID is not proof that the image contents were audited.
    """
    if type(approved_image_id) is not str or not _IMAGE.fullmatch(approved_image_id):
        raise ValueError("Administrator-approved immutable image ID required")
    if (type(inspection) is not list or len(inspection) != 1
            or type(inspection[0]) is not dict):
        raise ValueError("Expected one image inspection record")
    image = inspection[0]
    if image.get("Id") != approved_image_id or image.get("Os") != "linux":
        raise ValueError("Image identity or OS mismatch")
    cfg = image.get("Config")
    if type(cfg) is not dict:
        raise ValueError("Missing image configuration")
    required = {"Volumes", "Entrypoint", "Cmd", "Env", "User", "OnBuild"}
    if not required.issubset(cfg):
        raise ValueError("Incomplete image configuration")
    if cfg["Volumes"] is not None and cfg["Volumes"] != {}:
        raise ValueError("Image volumes forbidden")
    if cfg["Entrypoint"] != [ENTRYPOINT] or cfg["Cmd"] not in (None, []):
        raise ValueError("Unexpected default entrypoint or command")
    if cfg["User"] != "65534:65534" or cfg["OnBuild"] not in (None, []):
        raise ValueError("Unexpected user or build triggers")
    if cfg.get("Healthcheck") not in (None, {"Test": ["NONE"]}):
        raise ValueError("Image healthcheck forbidden")
    env = cfg["Env"]
    if (type(env) is not list or any(type(v) is not str for v in env)
            or len(env) != len(set(env)) or set(env) != _IMAGE_ENV):
        raise ValueError("Unexpected image environment")


def isolation_arguments(*, image_id: str, container_name: str) -> tuple[str, ...]:
    """Fixed policy for an administrator-provisioned local image.

    This is a policy specification, not evidence of enforcement. Transport
    must reject non-rootless engines, untrusted images/volumes, and failures
    to enforce limits. Input will be supplied via stdin to a fixed entrypoint;
    no host paths, mounts, secrets or client-controlled arguments.
    """
    if type(image_id) is not str or not _IMAGE.fullmatch(image_id):
        raise ValueError("Exact local image ID required")
    if type(container_name) is not str or not _NAME.fullmatch(container_name):
        raise ValueError("Invalid internal container name")
    return (
        "create", "--name", container_name, "--pull=never", "--interactive",
        "--network=none", "--ipc=private", "--cgroupns=private",
        "--read-only", "--cap-drop=ALL", "--security-opt=no-new-privileges",
        "--user=65534:65534", "--pids-limit=" + str(PIDS_LIMIT),
        "--memory=" + str(MEMORY_BYTES), "--memory-swap=" + str(MEMORY_BYTES),
        "--cpus=1", "--ulimit=nofile=256:256", "--ulimit=core=0:0",
        "--tmpfs=/tmp:rw,noexec,nosuid,nodev,size=16777216",
        "--no-healthcheck", "--log-driver=none", "--restart=no",
        "--env=HOME=/tmp", "--env=LEAN_NUM_THREADS=1",
        "--workdir=/tmp", "--entrypoint=" + ENTRYPOINT,
        image_id,
    )
