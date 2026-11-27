"""A real local process must survive reloads and exit with its last page."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from urllib.request import urlopen

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PORT = int(os.environ.get('MATLIB_LIFECYCLE_TEST_PORT', '18769'))
URL = f'http://127.0.0.1:{PORT}'


def main():
    with tempfile.TemporaryDirectory(prefix='atlas-lifecycle-') as temp:
        drafts, saved = Path(temp) / 'drafts', Path(temp) / 'saved'
        with (Path(temp) / 'server.log').open('wb') as log:
            proc = subprocess.Popen(
                [sys.executable, '-m', 'backend.desktop', '--no-browser', '--port', str(PORT), '--close-delay', '1'],
                cwd=ROOT, stdout=log, stderr=log,
                env={**os.environ, 'MATLIB_DRAFTS_ROOT': str(drafts), 'MATLIB_SAVED_ROOT': str(saved)},
            )
            try:
                deadline = time.monotonic() + 15
                while True:
                    assert proc.poll() is None, (Path(temp) / 'server.log').read_text(errors='replace')
                    try:
                        with urlopen(URL + '/api/health', timeout=.5):
                            break
                    except OSError:
                        assert time.monotonic() < deadline
                        time.sleep(.05)
                time.sleep(1.2)
                assert proc.poll() is None, 'server must wait for the first page'
                with sync_playwright() as pw:
                    browser = pw.chromium.launch(headless=True)
                    first, second = browser.new_page(), browser.new_page()
                    for page in (first, second):
                        page.goto(URL, wait_until='networkidle')
                    first.close()
                    second.wait_for_timeout(1200)
                    assert proc.poll() is None, 'another tab must keep the server running'
                    second.reload(wait_until='networkidle')
                    second.wait_for_timeout(1200)
                    assert proc.poll() is None, 'reload must reconnect before shutdown'
                    # Stage an unsaved draft and save a second copy through the real API.
                    draft = second.request.post(URL + '/api/drafts', data={'modules': ['AA-01'], 'title': 'Lifecycle test'})
                    assert draft.ok, draft.text()
                    session = draft.json()['session_id']
                    stored = second.request.post(URL + f'/api/drafts/{session}/save')
                    assert stored.ok, stored.text()
                    # A separate tab tests connection loss without the JS pagehide handler.
                    socket_page = browser.new_page()
                    socket_page.goto(URL + '/api/health')
                    socket_page.evaluate("""() => new Promise(resolve => {
                        const ws = new WebSocket('ws://' + location.host + '/api/lifecycle/socket');
                        ws.onmessage = () => {window.testSocket=ws;resolve();};
                    })""")
                    second.close()
                    socket_page.wait_for_timeout(1200)
                    assert proc.poll() is None, 'connection without pagehide must still count'
                    socket_page.close()
                    assert proc.wait(timeout=8) == 0, 'server should exit gracefully'
                    assert not list(drafts.glob('*/project.zip')), 'shutdown must clean temporary drafts'
                    assert list(saved.glob('*.zip')), 'saved projects must survive'
                    browser.close()
                print(json.dumps({'last_tab_shutdown': True, 'reload_survives': True,
                                  'multiple_tabs': True, 'no_unload_event': True,
                                  'draft_cleanup': True, 'saved_projects_preserved': True}))
            finally:
                if proc.poll() is None:
                    proc.terminate()
                    try:
                        proc.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        proc.kill()
                        proc.wait(timeout=5)


if __name__ == '__main__':
    main()
