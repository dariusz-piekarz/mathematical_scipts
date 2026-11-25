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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--figures', action='store_true', help='Also compile the four ALG-08 figures (requires TeX/Poppler).')
    parser.add_argument('--port', type=int, default=18770)
    args = parser.parse_args()
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
                    scripts = ['browser_reading_preferences.py', 'browser_reading_focus.py', 'browser_references.py']
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


if __name__ == '__main__':
    main()
