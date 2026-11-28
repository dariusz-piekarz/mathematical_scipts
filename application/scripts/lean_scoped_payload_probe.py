"""CI-only stdin probe for two fixed generated drafts in an isolated image.

No arbitrary payload, endpoint, user execution authority or host fallback.
The observed file digest is emitted by the fixed image entrypoint before Lean.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import uuid

from backend import lean_draft_runner as policy
from backend import lean_draft_transport as transport
from backend.lean_draft_generator import generate
from scripts import lean_artifact_manifest as artifacts
from scripts import lean_rootless_compiler_probe as core
from scripts.lean_ci_audit import inspect_log
from scripts.lean_rootless_ci_probe import cleanup_fixture, validate_exited_fixture

CASES = {"true": (r"\top", 0), "false": (r"\bot", 1)}


def prepared_fixture(case):
    if case not in CASES:
        raise ValueError("Unknown fixed payload case")
    source, expected_exit = CASES[case]
    candidate = generate(source, consent=True)
    if candidate["status"] != "generated":
        raise ValueError("Fixed draft generation failed")
    status, prepared = policy.prepare(
        source, consent=True, expected_source_sha256=candidate["source_sha256"],
        expected_ast_sha256=candidate["ast_sha256"],
        expected_code_sha256=candidate["lean_code_sha256"])
    if (type(prepared) is not policy.PreparedDraft or status["execution_allowed"] is not False
            or status["certificate"] is not False
            or hashlib.sha256(prepared.input_bytes).hexdigest() != prepared.input_sha256
            or prepared.input_bytes != candidate["lean_code"].encode() + b"\n#print axioms atlas_draft\n"):
        raise ValueError("Fixed draft preparation mismatch")
    return prepared, expected_exit


def payload_entry(package_names):
    relocated = ":".join("/opt/packages/" + name + "/.lake/build/lib/lean" for name in sorted(package_names))
    limit = transport.MAX_FIXTURE_INPUT_BYTES
    return ("#!/bin/busybox sh\nset -eu\numask 077\ncd /tmp\n"
            "export LEAN_PATH=" + shlex.quote(relocated) + "\n"
            "/bin/busybox head -c " + str(limit + 1) + " > Draft.lean\n"
            "size=$(/bin/busybox wc -c < Draft.lean)\n"
            "[ \"$size\" -gt 0 ] && [ \"$size\" -le " + str(limit) + " ] || exit 64\n"
            "digest=$(/bin/busybox sha256sum Draft.lean)\n"
            "printf 'ATLAS_INPUT_SHA256 %s\\n' \"${digest%% *}\"\n"
            "/opt/lean/bin/lean --version\n"
            "exec /opt/lean/bin/lean Draft.lean\n")


def validate_payload_output(output, prepared, *, expected_exit):
    if (type(output) is not bytes or len(output) > policy.MAX_OUTPUT_BYTES
            or type(expected_exit) is not int or expected_exit not in (0, 1)):
        raise ValueError("Invalid bounded payload output")
    marker, sep, rest = output.partition(b"\n")
    version, sep2, diagnostic = rest.partition(b"\n")
    expected = b"ATLAS_INPUT_SHA256 " + prepared.input_sha256.encode("ascii")
    if not sep or not sep2 or marker != expected:
        raise ValueError("Observed payload digest mismatch")
    core.validate_version(version.decode("ascii"))
    text = diagnostic.decode("utf-8")
    if expected_exit == 0:
        if "error:" in text.lower():
            raise ValueError("Unexpected successful fixture diagnostic")
        axioms = inspect_log(text, ["atlas_draft"])["atlas_draft"]
    else:
        # Exact failure class/location must be accepted by the existing
        # bounded repair planner; no fabricated or host-side diagnostic.
        from backend.lean_draft_repair import plan_next
        plan = plan_next(CASES["false"][0], consent=True,
                         expected_source_sha256=prepared.source_sha256,
                         expected_ast_sha256=prepared.ast_sha256,
                         expected_initial_code_sha256=prepared.lean_code_sha256,
                         observations=[dict(code_sha256=prepared.lean_code_sha256,
                                            exit_code=1, diagnostic=diagnostic)])
        if plan["status"] != "repair_planned" or plan["execution_allowed"] is not False:
            raise ValueError("Unexpected fixed negative fixture diagnostic")
        axioms = None
    return {"observed_input_sha256": prepared.input_sha256,
            "lean_version": version.decode("ascii"),
            "diagnostic_sha256": hashlib.sha256(diagnostic).hexdigest(),
            "diagnostic_bytes": len(diagnostic), "axioms": axioms}


def check_fixed_payload(prefix, env, image, case):
    prepared, expected_exit = prepared_fixture(case)
    def call(*args):
        return transport._command(prefix, args, env)
    transport.validate_engine(transport._decode_metadata(call("info", "--format", "{{json .}}")))
    policy.validate_image_inspection(transport._decode_metadata(call("image", "inspect", image)),
                                     approved_image_id=image)
    name = "atlas-draft-" + uuid.uuid4().hex
    cid = call(*policy.isolation_arguments(image_id=image, container_name=name)).decode("ascii").strip()
    if not transport._CONTAINER_ID.fullmatch(cid):
        raise ValueError("Ambiguous fixed payload container identity")
    cleanup = transport.deferred_cleanup_command(prefix, env)
    try:
        transport.validate_container(transport._decode_metadata(call("container", "inspect", cid)),
                                     container_id=cid, image_id=image, name=name)
        try:
            output = transport._command(prefix, ("container", "start", "--attach", "--interactive", cid),
                                        env, fixture_input=prepared.input_bytes, capture_failure=True)
            actual_exit = 0
        except transport.DockerCommandFailed as exc:
            output, actual_exit = exc.output, exc.returncode
        if type(actual_exit) is not int or actual_exit != expected_exit:
            raise ValueError("Unexpected fixed payload compiler exit")
        evidence = validate_payload_output(output, prepared, expected_exit=expected_exit)
        state = validate_exited_fixture(transport._decode_metadata(cleanup("container", "inspect", cid)),
                                        container_id=cid, image_id=image, expected_exit=expected_exit)
    finally:
        cleanup_fixture(cleanup, cid)
    return dict(case=case, image_id=image, container_id=cid, input_sha256=prepared.input_sha256,
                code_sha256=prepared.lean_code_sha256, source_sha256=prepared.source_sha256,
                ast_sha256=prepared.ast_sha256, cleanup_status="removed_verified", **state, **evidence)


def run_fixed_payload_probe(*, work, context, rootfs, prefix, env, packages, source_report, checkout_sha):
    # Reuse the selected and verified scoped dependency tree, not the
    # previous fixed-source entrypoint. Restore it for the negative import test.
    entry = rootfs / "opt/atlas/run-draft"
    fixture = rootfs / "opt/atlas/Fixture.lean"
    old_entry, old_fixture = entry.read_bytes(), fixture.read_bytes()
    try:
        fixture.unlink()
        entry.write_text(payload_entry(packages), encoding="ascii")
        manifest = artifacts.create_manifest(rootfs, source_report, scope=artifacts.SCOPED_FIXTURE_SCOPE)
        raw = artifacts.encoded(manifest)
        digest = hashlib.sha256(raw).hexdigest()
        def verify():
            return artifacts.verify_manifest(rootfs, raw, expected_sha256=digest,
                expected_source_report=source_report, scope=artifacts.SCOPED_FIXTURE_SCOPE)
        verify()
        iid = work / "payload-image-id"
        subprocess.run(prefix + ["build", "--network=none", "--pull=false", "--iidfile", str(iid), str(context)],
                       check=True, timeout=360, stdin=subprocess.DEVNULL, env={**env, "DOCKER_BUILDKIT": "0"})
        image = iid.read_text("ascii").strip()
        if not policy._IMAGE.fullmatch(image):
            raise ValueError("Invalid fixed payload image ID")
        try:
            verify()
            rows = [check_fixed_payload(prefix, env, image, case) for case in CASES]
            if len({row["container_id"] for row in rows}) != len(CASES):
                raise ValueError("Fixed payload cases must use distinct containers")
        finally:
            transport._command(prefix, ("image", "rm", image), env)
        report = dict(schema=1, checkout_sha=checkout_sha, fixture_only=True,
                      manifest_sha256=digest, execution_allowed=False, offline_ready=False,
                      certificate=False, proof_status="not_run", cases=rows)
        for name, value in (("manifest", manifest), ("report", report)):
            with (Path(os.environ["RUNNER_TEMP"]) / ("atlas-mathlib-scoped-payload-" + name + ".json")).open("xb") as f:
                f.write(artifacts.encoded(value))
        print("ATLAS_SCOPED_PAYLOAD_PROBE " + json.dumps(report, sort_keys=True), flush=True)
    finally:
        entry.write_bytes(old_entry)
        fixture.write_bytes(old_fixture)
