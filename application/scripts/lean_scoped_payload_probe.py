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
POLYNOMIAL = (r"\forall x:Real, \forall y:Real, "
              r"(x + y) \cdot (x + y) = (x \cdot x) + "
              r"((2:Real) \cdot x \cdot y) + (y \cdot y)")


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


def _payload_envelope(output, prepared, *, expected_exit):
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
    return version.decode("ascii"), diagnostic, text


def validate_payload_output(output, prepared, *, expected_exit):
    version, diagnostic, text = _payload_envelope(output, prepared, expected_exit=expected_exit)
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
            "lean_version": version,
            "diagnostic_sha256": hashlib.sha256(diagnostic).hexdigest(),
            "diagnostic_bytes": len(diagnostic), "axioms": axioms}


def _execute_fixed_payload(prefix, env, image, prepared, *, expected_exit):
    """Private CI helper, called only with freshly prepared fixed fixtures."""
    if (type(prepared) not in (policy.PreparedDraft, policy.PreparedRepair)
            or hashlib.sha256(prepared.input_bytes).hexdigest() != prepared.input_sha256
            or hashlib.sha256(prepared.input_bytes.removesuffix(b"\n#print axioms atlas_draft\n")).hexdigest()
            != prepared.lean_code_sha256
            or not prepared.input_bytes.endswith(b"\n#print axioms atlas_draft\n")):
        raise ValueError("Invalid prepared fixed fixture identity")
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
        version, diagnostic, text = _payload_envelope(output, prepared, expected_exit=expected_exit)
        axioms = None
        if expected_exit == 0:
            if "error:" in text.lower():
                raise ValueError("Unexpected successful fixture diagnostic")
            axioms = inspect_log(text, ["atlas_draft"])["atlas_draft"]
        elif "error:" not in text.lower():
            raise ValueError("Expected fixed fixture failure diagnostic")
        evidence = dict(observed_input_sha256=prepared.input_sha256, lean_version=version,
                        diagnostic_sha256=hashlib.sha256(diagnostic).hexdigest(),
                        diagnostic_bytes=len(diagnostic), axioms=axioms)
        state = validate_exited_fixture(transport._decode_metadata(cleanup("container", "inspect", cid)),
                                        container_id=cid, image_id=image, expected_exit=expected_exit)
    finally:
        cleanup_fixture(cleanup, cid)
    row = dict(image_id=image, container_id=cid, input_sha256=prepared.input_sha256,
               code_sha256=prepared.lean_code_sha256, source_sha256=prepared.source_sha256,
               ast_sha256=prepared.ast_sha256, cleanup_status="removed_verified", **state, **evidence)
    return row, output


def check_fixed_payload(prefix, env, image, case):
    prepared, expected_exit = prepared_fixture(case)
    row, output = _execute_fixed_payload(prefix, env, image, prepared, expected_exit=expected_exit)
    validate_payload_output(output, prepared, expected_exit=expected_exit)
    return dict(case=case, compiler_output=output.decode("utf-8"), **row)


def run_fixed_repair_loop(prefix, env, image):
    """Actual diagnostics from the same verified image, fresh container per attempt.

    Fixed CI polynomial only. No caller-supplied source or attempt history.
    """
    from backend.lean_draft_repair import plan_next, MAX_ATTEMPTS
    if MAX_ATTEMPTS != 3:
        raise ValueError("Fixed repair attempt contract changed")
    source = POLYNOMIAL
    initial = generate(source, consent=True)
    identity = dict(expected_source_sha256=initial["source_sha256"],
                    expected_ast_sha256=initial["ast_sha256"],
                    expected_initial_code_sha256=initial["lean_code_sha256"],
                    consent=True)
    status, prepared = policy.prepare(source, consent=True,
        expected_source_sha256=identity["expected_source_sha256"],
        expected_ast_sha256=identity["expected_ast_sha256"],
        expected_code_sha256=identity["expected_initial_code_sha256"])
    if type(prepared) is not policy.PreparedDraft or status["execution_allowed"] is not False:
        raise ValueError("Fixed polynomial preparation rejected")
    original_prefix = initial["lean_code"].split(" := by\n", 1)[0]
    history, rows = [], []
    for attempt in range(1, MAX_ATTEMPTS + 1):
        expected_exit = 0 if attempt == MAX_ATTEMPTS else 1
        if (prepared.source_sha256 != initial["source_sha256"]
                or prepared.ast_sha256 != initial["ast_sha256"]
                or prepared.input_bytes.decode("utf-8").split(" := by\n", 1)[0] != original_prefix):
            raise ValueError("Fixed repair changed statement or imports")
        row, output = _execute_fixed_payload(prefix, env, image, prepared, expected_exit=expected_exit)
        version, diagnostic, _ = _payload_envelope(output, prepared, expected_exit=expected_exit)
        if (row["exit_code"] != expected_exit or row["input_sha256"] != prepared.input_sha256
                or row["observed_input_sha256"] != prepared.input_sha256
                or row["code_sha256"] != prepared.lean_code_sha256
                or row["diagnostic_sha256"] != hashlib.sha256(diagnostic).hexdigest()
                or row["cleanup_status"] != "removed_verified" or row["image_id"] != image
                or any(previous["container_id"] == row["container_id"] for previous in rows)):
            raise ValueError("Fixed repair execution evidence mismatch")
        row.update(attempt=attempt, compiler_output=output.decode("utf-8"))
        rows.append(row)
        if expected_exit == 0:
            if row["axioms"] is None:
                raise ValueError("Missing successful repair axiom audit")
            break
        history.append(dict(code_sha256=prepared.lean_code_sha256, exit_code=1, diagnostic=diagnostic))
        plan = plan_next(source, observations=history, **identity)
        if (plan["status"] != "repair_planned" or plan["signature"] != initial["signature"]
                or plan["execution_allowed"] is not False or plan["certificate"] is not False):
            raise ValueError("Real isolated proof failure did not authorize fixed repair plan")
        status, next_prepared = policy.prepare_repair(
            source, observations=history, expected_repair_code_sha256=plan["lean_code_sha256"], **identity)
        if (type(next_prepared) is not policy.PreparedRepair or next_prepared.attempt != attempt + 1
                or next_prepared.initial_code_sha256 != initial["lean_code_sha256"]
                or next_prepared.diagnostic_sha256 != tuple(r["diagnostic_sha256"] for r in rows)
                or status["execution_allowed"] is not False or status["certificate"] is not False
                or next_prepared.input_bytes != plan["lean_code"].encode() + b"\n#print axioms atlas_draft\n"):
            raise ValueError("Prepared repair identity or history mismatch")
        row["planner_status"] = plan["status"]
        prepared = next_prepared
    if len(rows) != MAX_ATTEMPTS or len({r["input_sha256"] for r in rows}) != MAX_ATTEMPTS:
        raise ValueError("Incomplete fixed isolated repair loop")
    return dict(outcome="repair_compiled", initial_code_sha256=initial["lean_code_sha256"],
                attempts=rows, max_attempts=MAX_ATTEMPTS, fixture_only=True,
                execution_allowed=False, offline_ready=False, certificate=False, proof_status="not_run")


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
            repair = run_fixed_repair_loop(prefix, env, image)
            all_rows = rows + repair["attempts"]
            if len({row["container_id"] for row in all_rows}) != len(all_rows):
                raise ValueError("Fixed payload and repair cases must use distinct containers")
        finally:
            transport._command(prefix, ("image", "rm", image), env)
        report = dict(schema=2, checkout_sha=checkout_sha, fixture_only=True,
                      manifest_sha256=digest, execution_allowed=False, offline_ready=False,
                      certificate=False, proof_status="not_run", cases=rows, repair_loop=repair)
        for name, value in (("manifest", manifest), ("report", report)):
            with (Path(os.environ["RUNNER_TEMP"]) / ("atlas-mathlib-scoped-payload-" + name + ".json")).open("xb") as f:
                f.write(artifacts.encoded(value))
        print("ATLAS_SCOPED_PAYLOAD_PROBE " + json.dumps(report, sort_keys=True), flush=True)
    finally:
        entry.write_bytes(old_entry)
        fixture.write_bytes(old_fixture)


def replay_report(report, manifest, baseline, *, expected_sha, expected_manifest_sha):
    """Check persisted fixed-case evidence, not independent runtime attestation."""
    from scripts import lean_mathlib_source_probe as sources
    from backend.lean_draft_repair import plan_next
    from scripts.lean_ci_audit import ALLOWED_AXIOMS
    fixed = dict(schema=2, checkout_sha=expected_sha, fixture_only=True,
                 execution_allowed=False, offline_ready=False, certificate=False,
                 proof_status="not_run", manifest_sha256=expected_manifest_sha)
    if (type(expected_sha) is not str or not sources.REV.fullmatch(expected_sha)
            or type(expected_manifest_sha) is not str or not artifacts.HEX.fullmatch(expected_manifest_sha)
            or type(report) is not dict or set(report) != set(fixed) | {"cases", "repair_loop"}
            or any(type(report[k]) is not type(v) or report[k] != v for k,v in fixed.items())):
        raise ValueError("Invalid persisted payload report identity")
    for tree in (manifest, baseline):
        artifacts.validate_manifest_structure(tree, scope=artifacts.SCOPED_FIXTURE_SCOPE)
        if artifacts.provenance(tree["source_closure"])["checkout_sha"] != expected_sha:
            raise ValueError("Stale payload source provenance")
    if hashlib.sha256(artifacts.encoded(manifest)).hexdigest() != expected_manifest_sha:
        raise ValueError("Persisted payload manifest digest mismatch")
    if manifest["source_closure"] != baseline["source_closure"]:
        raise ValueError("Payload source closure changed")
    old = {r["path"]:r for r in baseline["entries"]}
    new = {r["path"]:r for r in manifest["entries"]}
    fixture, entry = "opt/atlas/Fixture.lean", "opt/atlas/run-draft"
    if (fixture not in old or entry not in old or entry not in new
            or set(new) != set(old) - {fixture}
            or any(new[k] != old[k] for k in new if k != entry)):
        raise ValueError("Payload dependency tree differs from fixed scoped baseline")
    entry_bytes = payload_entry(p["name"] for p in manifest["source_closure"]["packages"]).encode("ascii")
    if new[entry] != dict(path=entry, kind="file", size=len(entry_bytes),
                          sha256=hashlib.sha256(entry_bytes).hexdigest()):
        raise ValueError("Payload entrypoint digest mismatch")
    ids, images = set(), set()

    def verify_row(row, prepared, expected_exit, extra):
        if type(row) is not dict or type(row.get("compiler_output")) is not str:
            raise ValueError("Missing raw compiler evidence")
        if len(row["compiler_output"]) > policy.MAX_OUTPUT_BYTES:
            raise ValueError("Oversized raw compiler evidence")
        output = row["compiler_output"].encode("utf-8")
        version, diagnostic, text = _payload_envelope(output, prepared, expected_exit=expected_exit)
        axioms = None
        if expected_exit == 0:
            if "error:" in text.lower():
                raise ValueError("Unexpected successful fixture diagnostic")
            axioms = inspect_log(text, ["atlas_draft"])["atlas_draft"]
        elif "error:" not in text.lower():
            raise ValueError("Missing negative diagnostic")
        expected = dict(input_sha256=prepared.input_sha256, observed_input_sha256=prepared.input_sha256,
                        code_sha256=prepared.lean_code_sha256, source_sha256=prepared.source_sha256,
                        ast_sha256=prepared.ast_sha256, cleanup_status="removed_verified",
                        container_state="exited", exit_code=expected_exit, lean_version=version,
                        diagnostic_sha256=hashlib.sha256(diagnostic).hexdigest(),
                        diagnostic_bytes=len(diagnostic), axioms=axioms, **extra)
        if (set(row) != set(expected) | {"image_id","container_id","compiler_output"}
                or any(type(row[k]) is not type(v) or row[k] != v for k,v in expected.items())
                or type(row["container_id"]) is not str or not transport._CONTAINER_ID.fullmatch(row["container_id"])
                or row["container_id"] in ids
                or type(row["image_id"]) is not str or not policy._IMAGE.fullmatch(row["image_id"])):
            raise ValueError("Persisted payload case evidence mismatch")
        ids.add(row["container_id"])
        images.add(row["image_id"])
        return diagnostic

    if type(report["cases"]) is not list or len(report["cases"]) != len(CASES):
        raise ValueError("Incorrect fixed case count")
    for row, case in zip(report["cases"], CASES):
        prepared, exit_code = prepared_fixture(case)
        verify_row(row, prepared, exit_code, dict(case=case))
        validate_payload_output(row["compiler_output"].encode(), prepared, expected_exit=exit_code)
    initial = generate(POLYNOMIAL, consent=True)
    identity = dict(expected_source_sha256=initial["source_sha256"],
                    expected_ast_sha256=initial["ast_sha256"],
                    expected_initial_code_sha256=initial["lean_code_sha256"], consent=True)
    _, prepared = policy.prepare(POLYNOMIAL, consent=True,
        expected_source_sha256=initial["source_sha256"], expected_ast_sha256=initial["ast_sha256"],
        expected_code_sha256=initial["lean_code_sha256"])
    loop = report["repair_loop"]
    flags = dict(outcome="repair_compiled", initial_code_sha256=initial["lean_code_sha256"],
                 max_attempts=3, fixture_only=True, execution_allowed=False,
                 offline_ready=False, certificate=False, proof_status="not_run")
    if (type(loop) is not dict or set(loop) != set(flags) | {"attempts"}
            or any(type(loop[k]) is not type(v) or loop[k] != v for k,v in flags.items())
            or type(loop["attempts"]) is not list or len(loop["attempts"]) != 3):
        raise ValueError("Invalid persisted repair loop")
    history = []
    for attempt, row in enumerate(loop["attempts"], 1):
        extra = dict(attempt=attempt)
        if attempt < 3:
            extra["planner_status"] = "repair_planned"
        diagnostic = verify_row(row, prepared, int(attempt < 3), extra)
        if attempt == 3:
            if not set(row["axioms"]).issubset(ALLOWED_AXIOMS):
                raise ValueError("Forbidden final axioms")
            break
        history.append(dict(code_sha256=prepared.lean_code_sha256, exit_code=1, diagnostic=diagnostic))
        plan = plan_next(POLYNOMIAL, observations=history, **identity)
        if plan["status"] != "repair_planned" or plan["signature"] != initial["signature"]:
            raise ValueError("Persisted diagnostic replay rejected")
        _, prepared = policy.prepare_repair(POLYNOMIAL, observations=history,
            expected_repair_code_sha256=plan["lean_code_sha256"], **identity)
        if type(prepared) is not policy.PreparedRepair or prepared.attempt != attempt + 1:
            raise ValueError("Persisted repair preparation rejected")
    if len(ids) != 5 or len(images) != 1:
        raise ValueError("Persisted container or image identity mismatch")


def main():
    import argparse
    from scripts import lean_mathlib_source_probe as sources
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence-directory", type=Path, required=True)
    parser.add_argument("--expected-manifest-sha256", required=True)
    parser.add_argument("--expected-baseline-sha256", required=True)
    parser.add_argument("--expected-report-sha256", required=True)
    args = parser.parse_args()
    def read(name, limit, digest=None):
        with (args.evidence_directory / name).open("rb") as handle:
            raw = handle.read(limit + 1)
        if len(raw) > limit or (digest is not None and hashlib.sha256(raw).hexdigest() != digest):
            raise ValueError("Oversized or changed persisted evidence")
        return json.loads(raw, object_pairs_hook=sources.unique_object)
    report = read("atlas-mathlib-scoped-payload-report.json", 256000, args.expected_report_sha256)
    manifest = read("atlas-mathlib-scoped-payload-manifest.json", artifacts.MAX_MANIFEST_BYTES,
                    args.expected_manifest_sha256)
    baseline = read("atlas-mathlib-scoped-manifest.json", artifacts.MAX_MANIFEST_BYTES,
                    args.expected_baseline_sha256)
    replay_report(report, manifest, baseline, expected_sha=os.environ.get("GITHUB_SHA",""),
                  expected_manifest_sha=args.expected_manifest_sha256)
    print("ATLAS_SCOPED_PAYLOAD_REPLAY_VALIDATED")


if __name__ == "__main__":
    main()
