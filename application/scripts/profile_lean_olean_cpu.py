"""Read-only cProfile of ONE genuine Lean compiled-artifact fingerprint pass.

This is diagnostic profiling, NOT proof verification, a semantic review, a
performance baseline comparable to unprofiled timings or an extra security
attestation. Execute only in a trusted checkout with pinned dependencies.
"""
from __future__ import annotations

import argparse
import cProfile
import hashlib
import json
from pathlib import Path
import pstats
import re
import sys

APPLICATION = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APPLICATION))

from backend import lean_environment
from scripts.benchmark_lean_fingerprint import _registered_inputs

HEX = re.compile(r"[0-9a-f]{64}\Z")
MAX_ENTRIES = 20


def profile_olean_cpu(lean_root: Path, *, limit: int = 12) -> dict:
    """Profile the original digest exactly once; preserve its failure behavior."""
    if type(limit) is not int or not 1 <= limit <= MAX_ENTRIES:
        raise ValueError("limit must be an integer between 1 and 20")
    # Same path-validation contract as the existing fingerprint benchmark.
    _registered_inputs(lean_root)

    profiler = cProfile.Profile()
    profiler.enable()
    try:
        digest = lean_environment.compiled_artifacts_sha256(lean_root)
    finally:
        profiler.disable()
    if not isinstance(digest, str) or HEX.fullmatch(digest) is None:
        raise ValueError("Unexpected compiled-artifact fingerprint format")

    stats = pstats.Stats(profiler)
    # Keep original function identity and retain profiler's cumulative-cost
    # ordering; no second walk, filesystem inspection or digest is performed.
    ranked = sorted(
        stats.stats.items(), key=lambda item: item[1][3], reverse=True
    )
    hotspots = []
    for (source, line, function), (primitive, calls, self_time, cumulative, _) in ranked[:limit]:
        hotspots.append({
            "file": Path(source).name,
            "line": line,
            "function": function,
            "primitive_calls": primitive,
            "total_calls": calls,
            "self_seconds": round(self_time, 6),
            "cumulative_seconds": round(cumulative, 6),
        })
    return {
        "purpose": "diagnostic_cpu_profile_not_formalization_result",
        "certificate": False,
        "profile_method": "cProfile around a single original compiled_artifacts_sha256 call",
        "actual_digest_calls": 1,
        "compiled_artifacts_sha256": digest,
        "profiled_seconds": round(stats.total_tt, 6),
        "profiled_total_calls": stats.total_calls,
        "hotspots": hotspots,
        "limits": {
            "top_entries": limit,
            "content_hash_budget_bytes": lean_environment.MAX_OLEAN_HASH_BYTES,
            "maximum_olean_files": lean_environment.MAX_OLEAN_FILES,
        },
        "interpretation": (
            "cProfile adds overhead; compare function rankings, not its total "
            "time against unprofiled elapsed benchmarks"
        ),
    }



def require_matching_benchmark(benchmark: object, cpu_report: object) -> None:
    """Fail closed if separate genuine observations refer to different artifacts.

    This compares evidence already obtained by two tools; it does not read
    an .olean file or invoke a second fingerprint pass.
    """
    if not isinstance(benchmark, dict) or not isinstance(cpu_report, dict):
        raise ValueError("Malformed Lean benchmark/profile evidence")
    first = benchmark.get("compiled_artifacts_sha256")
    second = cpu_report.get("compiled_artifacts_sha256")
    if (not isinstance(first, str) or HEX.fullmatch(first) is None
            or not isinstance(second, str) or HEX.fullmatch(second) is None
            or benchmark.get("certificate") is not False
            or cpu_report.get("certificate") is not False
            or type(benchmark.get("real_fingerprint_calls")) is not int
            or benchmark["real_fingerprint_calls"] < 1
            or cpu_report.get("actual_digest_calls") != 1):
        raise ValueError("Incomplete or invalid Lean benchmark/profile provenance")
    if first != second:
        raise RuntimeError(
            "Lean .olean artifacts changed between benchmark and CPU profile")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lean-root", type=Path, default=APPLICATION / "lean")
    parser.add_argument("--top", type=int, default=12)
    parser.add_argument("--compare-with", type=Path,
                        help="Previously recorded genuine full fingerprint benchmark JSON")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = profile_olean_cpu(args.lean_root, limit=args.top)
    if args.compare_with is not None:
        if args.compare_with.stat().st_size > 2 * 1024 * 1024:
            raise ValueError("Lean benchmark evidence is unexpectedly large")
        prior = json.loads(args.compare_with.read_text(encoding="utf-8"))
        require_matching_benchmark(prior, report)
    serialized = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized)


if __name__ == "__main__":
    main()
