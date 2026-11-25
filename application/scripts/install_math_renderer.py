"""Install version-pinned local KaTeX assets; the browser uses no CDN."""
from pathlib import Path
import base64
import hashlib
import io
import json
import shutil
import tarfile
import tempfile
from urllib.request import urlopen

VERSION = "0.16.22"
REGISTRY = "https://registry.npmjs.org/katex/"
DEST = Path(__file__).resolve().parents[1] / "frontend/vendor/katex"
REQUIRED = ("katex.min.js", "katex.min.css", "contrib/auto-render.min.js", "LICENSE")


def ready(folder):
    return all((folder / p).is_file() for p in REQUIRED) and any((folder / "fonts").glob("*.woff2"))


def install():
    marker = DEST / ".version"
    if ready(DEST) and marker.is_file() and marker.read_text() == VERSION:
        return
    with urlopen(REGISTRY + VERSION, timeout=30) as response:
        metadata = json.load(response)
    url = REGISTRY + "-/katex-" + VERSION + ".tgz"
    if metadata["version"] != VERSION or metadata["dist"]["tarball"] != url:
        raise RuntimeError("Unexpected distribution")
    with urlopen(url, timeout=60) as response:
        data = response.read(20 * 1024 * 1024 + 1)
    digest = "sha512-" + base64.b64encode(hashlib.sha512(data).digest()).decode("ascii")
    if len(data) > 20 * 1024 * 1024 or digest != metadata["dist"]["integrity"]:
        raise RuntimeError("KaTeX archive integrity check failed")
    DEST.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=DEST.parent) as tmp:
        stage = Path(tmp) / "katex"
        stage.mkdir()
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as archive:
            for member in archive:
                if not member.isfile():
                    continue
                if member.name == "package/LICENSE":
                    name = "LICENSE"
                elif member.name.startswith("package/dist/"):
                    name = member.name.removeprefix("package/dist/")
                else:
                    continue
                parts = name.split("/")
                if name not in REQUIRED and not (len(parts) == 2 and parts[0] == "fonts" and "\\" not in name and Path(parts[1]).suffix in {".woff", ".woff2", ".ttf"}):
                    continue
                target = stage / name
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.extractfile(member) as source, target.open("wb") as output:
                    shutil.copyfileobj(source, output)
        if not ready(stage):
            raise RuntimeError("Incomplete KaTeX distribution")
        (stage / ".version").write_text(VERSION)
        if DEST.exists():
            shutil.rmtree(DEST)
        stage.rename(DEST)
    print("Local KaTeX", VERSION, "installed")


if __name__ == "__main__":
    install()
