"""CI-only host measurement of a fixed full-Mathlib import and tactic suite.

This is not a container build, authenticated dependency manifest, or proof
of offline readiness. Existing admission limits and runner remain unchanged.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import tempfile
import time

from scripts import lean_artifact_manifest as artifacts
from scripts import lean_mathlib_source_probe as sources
from scripts import lean_offline_fixture as offline

# Measurement-only scan budget, not an admission budget.
INVENTORY_MAX_ENTRIES = 200000
INVENTORY_SECONDS = 120
SOURCE = """import Mathlib
set_option maxHeartbeats 100000
set_option maxRecDepth 1000

example (p : Prop) (h : p) : p := by assumption
example : (0 : Nat) = 0 := by rfl
example : True := by exact True.intro
example : ∃ n : Nat, n = 0 := by exact ⟨0, rfl⟩
example (p q : Prop) (h : p ∧ q) : q ∧ p := by tauto
example (n : Nat) : n + 1 > n := by omega
example (p : Prop) (h : p) : p := by solve_by_elim
example (p : Prop) (h : p) : p := by simp_all
example (p q : Prop) (h : p ∧ q) : q := by aesop
example (x y : Real) : (x + y)^2 = x^2 + 2*x*y + y^2 := by ring
theorem atlas_isolated_fixture (p q : Prop) : (p ∧ q) ↔ (q ∧ p) := and_comm
#print axioms atlas_isolated_fixture
"""
# Independently pinned reference profile; generator must match it exactly.
# Keep the fixture body identical for a fair comparison of import closures.
SCOPED_IMPORTS = (
    "Mathlib.Data.Real.Basic",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.Tauto",
    "Aesop",
    "Lean.Elab.Tactic.Omega",
)
SCOPED_HEADER = "".join("import " + name + "\n" for name in SCOPED_IMPORTS)
SCOPED_SOURCE = SCOPED_HEADER + SOURCE.split("\n", 1)[1]


def scoped_fixture_copy(payload: bytes) -> bytes:
    """CI-only transformation of an already generated fixed fixture.

    Not an admission function: never invoke this on a user draft or treat
    the resulting digest as the original generator's digest.
    """
    header = b"import Mathlib\n"
    if (type(payload) is not bytes or len(payload) > 65536 + 128
            or not payload.startswith(header)
            or not payload.endswith(b"\n#print axioms atlas_draft\n")):
        raise ValueError("Unexpected fixed fixture payload")
    return SCOPED_HEADER.encode("ascii") + payload[len(header):]


def full_fixture_copy(payload: bytes) -> bytes:
    """Reverse only the exact fixed header for the CI parity control."""
    header = SCOPED_HEADER.encode("ascii")
    if (type(payload) is not bytes or len(payload) > 65536 + 128
            or not payload.startswith(header)
            or not payload.endswith(b"\n#print axioms atlas_draft\n")):
        raise ValueError("Unexpected fixed scoped fixture payload")
    return b"import Mathlib\n" + payload[len(header):]


def fixture_source(profile: str) -> str:
    if profile == "full":
        return SOURCE
    if profile == "scoped":
        return SCOPED_SOURCE
    raise ValueError("Unknown fixed measurement profile")


def inventory(root: Path, *, deadline: float, remaining: int) -> dict:
    """Logical file sizes in a selected tree; never follow directory links."""
    result = dict(entries=0, files=0, bytes=0, largest_file=0,
                  symlinks=0, missing=False)
    if not root.exists() and not root.is_symlink():
        result["missing"] = True
        return result
    if not root.is_dir() or root.is_symlink():
        raise ValueError("Invalid compiled artifact inventory root")

    def fail(error):
        raise error

    for directory, dirs, files in os.walk(root, followlinks=False, onerror=fail):
        for name in dirs + files:
            if time.monotonic() >= deadline or result["entries"] >= remaining:
                raise ValueError("Inventory measurement budget exceeded")
            result["entries"] += 1
            info = (Path(directory) / name).lstat()
            if stat.S_ISLNK(info.st_mode):
                result["symlinks"] += 1
                if name in dirs:
                    dirs.remove(name)
            elif stat.S_ISREG(info.st_mode):
                result["files"] += 1
                result["bytes"] += info.st_size
                result["largest_file"] = max(result["largest_file"], info.st_size)
            elif not stat.S_ISDIR(info.st_mode):
                raise ValueError("Unexpected special inventory entry")
    return result


def observe(work: Path, toolchain: Path, packages: dict[str, Path], *, profile="full") -> dict:
    source = fixture_source(profile)
    fixture = work / "Fixture.lean"
    fixture.write_text(source, encoding="utf-8")
    env = {"PATH": str(toolchain / "bin") + ":/usr/bin:/bin",
           "HOME": str(work), "LANG": "C", "LEAN_NUM_THREADS": "1",
           "LEAN_PATH": ":".join(str(p / ".lake/build/lib/lean") for p in packages.values())}
    result = {"status": "blocked", "trace_files": 0, "trace_bytes": 0,
              "profile": profile, "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
              "host_fixture_compiled": False,
              "measurement_trace_limit": offline.MEASUREMENT_TRACE_BYTES,
              "admission_trace_limit": offline.MAX_TRACE_BYTES}
    nonportable = set()
    try:
        version = offline.trace_command([str(toolchain / "bin/lean"), "--version"],
                                        work / "version-trace", cwd=work, env=env, measurement_only=True)
        offline.core.validate_version(version.decode("ascii").strip())
        raw = offline.trace_command([str(toolchain / "bin/lean"), str(fixture)],
                                    work / "fixture-trace", cwd=work, env=env, measurement_only=True)
        if "'atlas_isolated_fixture' does not depend on any axioms" not in raw.decode("utf-8").splitlines():
            raise ValueError("Unexpected full-import fixture output")
        result['host_fixture_compiled'] = True
        traces = list(work.glob("*-trace.*"))
        result.update(trace_files=len(traces), trace_bytes=sum(p.stat().st_size for p in traces))
        if not 1 <= result["trace_files"] <= offline.MAX_TRACE_FILES or result["trace_bytes"] > offline.MEASUREMENT_TRACE_BYTES:
            raise ValueError("Aggregate dependency trace budget exceeded")
        paths = {toolchain / "bin/lean", toolchain / "bin/lake", Path("/bin/busybox")}
        observed = set()
        for trace in traces:
            with trace.open("rb") as handle:
                observed.update(offline.parse_trace(handle.read(offline.MEASUREMENT_TRACE_BYTES + 1),
                                                    cwd=work, allow_empty=True, measurement_only=True,
                                                    nonportable_components=nonportable))
            if len(observed) > offline.MEASUREMENT_TRACE_ENTRIES:
                raise ValueError("Aggregate measurement entry budget exceeded")
        if not observed:
            raise ValueError("Empty full-import trace")
        paths.update(observed)
        for binary in (toolchain / "bin/lean", toolchain / "bin/lake"):
            paths.update(offline.elf_dependencies(subprocess.check_output(
                ["/usr/bin/ldd", str(binary)], env=env, timeout=15)))
        sizes = {}
        for path in sorted(paths):
            if path == fixture or any(path.is_relative_to(r) for r in offline.KERNEL_ROOTS):
                continue
            target = offline.destination(path, toolchain, packages, nonportable_components=nonportable)
            resolved = Path(path).resolve(strict=True)
            offline.destination(resolved, toolchain, packages, nonportable_components=nonportable)
            info = artifacts.checked_stat(resolved)
            if stat.S_ISDIR(info.st_mode):
                continue
            if target in sizes:
                raise ValueError("Colliding observed dependency")
            sizes[target] = info.st_size
        if not sizes:
            raise ValueError("Empty observed dependency set")
        result.update(status="host_observation_measured", observed_files=len(sizes),
                      observed_bytes=sum(sizes.values()), largest_file=max(sizes.values()),
                      within_file_count_limit=len(sizes) < artifacts.MAX_ENTRIES,
                      within_total_byte_limit=sum(sizes.values()) <= artifacts.MAX_TOTAL_BYTES,
                      within_single_file_limit=max(sizes.values()) <= artifacts.MAX_FILE_BYTES)
    except (ValueError, subprocess.TimeoutExpired) as exc:
        # A blocked measurement is explicit evidence of non-readiness, not a
        # successful import, valid trace, or permission to enlarge the limits.
        traces = list(work.glob("*-trace.*"))
        result.update(trace_files=len(traces), trace_bytes=sum(p.stat().st_size for p in traces),
                      reason=str(exc)[:2000])
    result['nonportable_component_count'] = len(nonportable)
    result['nonportable_component_examples'] = sorted(nonportable)[:20]
    result['portable_paths'] = not nonportable if result['status'] == 'host_observation_measured' else None
    result["within_trace_byte_limit"] = result["trace_bytes"] <= offline.MAX_TRACE_BYTES
    return result


def main() -> int:
    if os.name != "posix" or not Path("/proc/sys/kernel").is_dir():
        raise ValueError("Full-import measurement requires Linux CI")
    lean_root = Path(__file__).resolve().parents[1] / "lean"
    sha = os.environ["GITHUB_SHA"]
    sources.inspect_sources(lean_root, expected_sha=sha)
    lock = sources.validate_lock(sources.read_json(lean_root / "mathlib-source-lock.json"))
    packages = {name: (lean_root / ".lake/packages" / name).resolve(strict=True) for name in lock}
    toolchain = (Path(os.environ["RUNNER_TEMP"]) / "atlas-offline-host-toolchain" /
                 "lean-4.26.0-linux").resolve(strict=True)
    roots = {"lean-core": toolchain / "lib/lean",
             **{name: p / ".lake/build/lib/lean" for name, p in packages.items()}}
    rows = {}
    deadline = time.monotonic() + INVENTORY_SECONDS
    remaining = INVENTORY_MAX_ENTRIES
    for name, root in sorted(roots.items()):
        row = inventory(root, deadline=deadline, remaining=remaining)
        rows[name] = row
        remaining -= row["entries"]
    with tempfile.TemporaryDirectory(prefix="atlas-full-mathlib-") as directory:
        observation = observe(Path(directory), toolchain, packages)
    with tempfile.TemporaryDirectory(prefix="atlas-scoped-mathlib-") as directory:
        scoped_observation = observe(Path(directory), toolchain, packages, profile="scoped")
    report = {"schema": 1, "checkout_sha": sha,
              "source_sha256": hashlib.sha256(SOURCE.encode()).hexdigest(),
              "fixture_only": True, "host_only": True, "execution_allowed": False,
              "offline_ready": False, "certificate": False, "inventory": rows,
              "inventory_totals": {key: sum(row[key] for row in rows.values())
                                   for key in ("entries", "files", "bytes", "symlinks")},
              "observation": observation, "scoped_imports": list(SCOPED_IMPORTS),
              "scoped_observation": scoped_observation}
    path = Path(os.environ["RUNNER_TEMP"]) / "atlas-full-mathlib-measurement.json"
    with path.open("xb") as handle:
        handle.write(artifacts.encoded(report))
    print("ATLAS_FULL_MATHLIB_MEASUREMENT " + json.dumps(report, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
