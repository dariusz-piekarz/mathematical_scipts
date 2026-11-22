"""Read-only, real-environment timings of the three Lean provenance checkpoints.

The tool does not run Lean, update history, validate mathematical equivalence,
or represent a proof certificate. Run only from a trusted checkout.
Example: python scripts/benchmark_lean_fingerprint.py --samples 3
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import statistics
import sys
import time

APPLICATION = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APPLICATION))
from backend import lean_results


def _registered_inputs(lean_root: Path) -> tuple[Path, str]:
    manifest = json.loads((lean_root / "manifest.json").read_text(encoding="utf-8"))
    items = manifest.get("items") if isinstance(manifest, dict) else None
    if not isinstance(items, list) or not items or not isinstance(items[0], dict):
        raise ValueError("No registered Lean source to benchmark")
    entry = items[0]
    rel, sha = entry.get("lean_file"), entry.get("source_document_sha256")
    if (not isinstance(rel, str) or not rel.startswith("src/")
            or "\\" in rel or ".." in Path(rel).parts
            or not rel.endswith(".lean")
            or not isinstance(sha, str) or not lean_results.HEX_DIGEST.fullmatch(sha)):
        raise ValueError("Malformed registered Lean benchmark source")
    src = (lean_root / "src").resolve()
    file = (lean_root / rel).resolve()
    if not file.is_relative_to(src) or not file.is_file():
        raise ValueError("Registered Lean source is missing or outside src")
    return file, sha


def benchmark(lean_root: Path, *, samples: int = 3) -> dict:
    """Measure actual fingerprint calls; refuse dependency changes mid-benchmark."""
    if type(samples) is not int or not 1 <= samples <= 6:
        raise ValueError("samples must be an integer between 1 and 6")
    file, document_sha = _registered_inputs(lean_root)
    # Benchmark only: never save or expose this artificial binding as evidence.
    dummy_binding = hashlib.sha256(b"benchmark-only-not-an-indexed-source").hexdigest()
    durations: list[float] = []
    first: dict[str, str] | None = None
    for _ in range(samples):
        start = time.perf_counter()
        measured = lean_results.fingerprint(document_sha, file, lean_root, dummy_binding)
        elapsed = time.perf_counter() - start
        if first is not None and measured != first:
            raise RuntimeError("Dependencies changed during the fingerprint benchmark")
        first = measured
        durations.append(elapsed)
    return {
        "purpose": "timing_only_not_a_formalization_result",
        "certificate": False,
        "real_fingerprint_calls": samples,
        "samples_seconds": [round(v, 6) for v in durations],
        "median_seconds": round(statistics.median(durations), 6),
        "total_seconds": round(sum(durations), 6),
        "max_seconds": round(max(durations), 6),
        "method": "perf_counter; full source/package/toolchain/olean fingerprints; no caching",
        "stability": "all fingerprint dictionaries identical during benchmark",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lean-root", type=Path, default=APPLICATION / "lean")
    parser.add_argument("--samples", type=int, default=3)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = benchmark(args.lean_root, samples=args.samples)
    serialized = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized)


if __name__ == "__main__":
    main()
