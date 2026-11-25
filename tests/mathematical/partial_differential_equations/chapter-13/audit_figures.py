"""Compile every canonical PDE figure using the real Atlas renderer, with a fresh cache."""
import hashlib
import json
from pathlib import Path
import struct
import sys
import time

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "application"))
from backend import figure_preview

def main():
    out = ROOT / "pde-figure-audit"
    out.mkdir(exist_ok=True)
    figure_preview.CACHE = out / "cache"
    if figure_preview.CACHE.exists() and any(figure_preview.CACHE.iterdir()):
        raise RuntimeError("Use a fresh cache for the audit")
    manifest = json.loads((ROOT / "catalog/partial_differential_equations_manifest.json").read_text(encoding="utf-8"))
    rows = []
    for chapter in manifest["chapters"]:
        path = ROOT / chapter["path"]
        source = path.read_text(encoding="utf-8-sig")
        module = "PDE-" + path.name.split("-",1)[0]
        for index, (digest, picture) in enumerate(figure_preview.figures(source).items(), 1):
            row = dict(module=module, index=index, sha256=digest,
                       source_sha256=hashlib.sha256(source.encode()).hexdigest())
            started = time.monotonic()
            try:
                png = figure_preview.render(module, source, digest)
                raw = png.read_bytes()
                assert raw[:8] == b"\x89PNG\r\n\x1a\n" and raw[12:16] == b"IHDR"
                w,h = struct.unpack(">II", raw[16:24])
                assert w > 0 and h > 0
                dest = out / f"{module}-{index:02d}.png"
                dest.write_bytes(raw)
                row.update(status="PASS", width=w, height=h, bytes=len(raw), image=dest.name)
            except Exception as exc:
                row.update(status="FAIL", error=str(exc))
            row["seconds"] = round(time.monotonic()-started,3)
            rows.append(row)
            print(json.dumps(row, ensure_ascii=False), flush=True)
    (out / "report.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    assert rows, "No figures found"
    assert all(row["status"] == "PASS" for row in rows), "One or more figures failed"

if __name__ == "__main__":
    main()
