"""Run real reader regressions against an isolated desktop server."""
import argparse
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from urllib.request import urlopen

from websockets.sync.client import connect

ROOT = Path(__file__).resolve().parents[1]


def check_tikz_math_packages():
    """Fail if the installed TeX runtime cannot render supported math symbols."""
    from backend import figure_preview as renderer

    # Compile fresh PNGs, not cached results or mocked subprocesses.
    previous_cache = renderer.CACHE
    try:
        with tempfile.TemporaryDirectory(prefix="atlas-tikz-packages-") as temp:
            renderer.CACHE = Path(temp)
            cases = (
                ("GW-01", r"\mathscr B"),
                ("LST-35", r"\llbracket p\rrbracket"),
            )
            for module, formula in cases:
                source = (r"\begin{tikzpicture}\node {$" + formula
                          + r"$};\end{tikzpicture}")
                key = next(iter(renderer.figures(source)))
                output = renderer.render(module, source, key)
                with output.open("rb") as png:
                    if png.read(8) != b"\x89PNG\r\n\x1a\n":
                        raise RuntimeError(f"Invalid math figure PNG: {module}")
                print(f"Standalone TikZ math package: {module} {formula}: OK", flush=True)
    finally:
        renderer.CACHE = previous_cache


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--figures', action='store_true', help='Also verify standalone math packages and reader figures (requires TeX/Poppler).')
    parser.add_argument('--port', type=int, default=18770)
    args = parser.parse_args()
    if args.figures:
        check_tikz_math_packages()
    url = f'http://127.0.0.1:{args.port}'
    with tempfile.TemporaryDirectory(prefix='atlas-reader-') as temp:
        env = {**os.environ, 'MATLIB_TEST_URL': url, 'MATLIB_DRAFTS_ROOT': str(Path(temp) / 'drafts'),
               'MATLIB_SAVED_ROOT': str(Path(temp) / 'saved'), 'TEMP': tempfile.gettempdir()}
        with (Path(temp) / 'server.log').open('wb') as log:
            process = subprocess.Popen([sys.executable, '-m', 'backend.desktop', '--no-browser',
                                        '--port', str(args.port), '--close-delay', '.5'],
                                       cwd=ROOT, env=env, stdout=log, stderr=log)
            try:
                deadline = time.monotonic() + 20
                while True:
                    if process.poll() is not None:
                        raise RuntimeError((Path(temp) / 'server.log').read_text(errors='replace'))
                    try:
                        with urlopen(url + '/api/health', timeout=.5):
                            break
                    except OSError:
                        if time.monotonic() > deadline:
                            raise TimeoutError('Reader server startup')
                        time.sleep(.05)
                # Keep the process alive between independent browser sessions.
                with connect(f'ws://127.0.0.1:{args.port}/api/lifecycle/socket', origin=url) as keeper:
                    keeper.recv()
                    scripts = ['browser_reading_preferences.py', 'browser_reading_focus.py',
                               'browser_references.py', 'browser_reader_layout.py']
                    if args.figures:
                        scripts.append('browser_reader_preview.py')
                    for script in scripts:
                        subprocess.run([sys.executable, str(ROOT / 'tests' / script)], env=env, cwd=ROOT, check=True)
                if process.wait(timeout=8) != 0:
                    raise RuntimeError('Desktop process failed to stop cleanly')
            finally:
                if process.poll() is None:
                    process.terminate()
                    try:
                        process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait(timeout=5)
                # Keep CI failures reviewable even when the temporary directory is removed.
                if sys.exc_info()[0] is not None:
                    print((Path(temp) / 'server.log').read_text(errors='replace')[-12000:], file=sys.stderr)


if __name__ == '__main__':
    main()
