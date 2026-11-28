"""Launch Atlas and stop its server after the last browser tab closes."""
import argparse
import asyncio
import webbrowser

import uvicorn

from backend.api import app
from backend.desktop_lifecycle import DesktopLifecycle


async def run(port=8765, no_browser=False, close_delay=5.0):
    url = f'http://127.0.0.1:{port}/'
    server = uvicorn.Server(uvicorn.Config(
        app, host='127.0.0.1', port=port, ws='websockets',
        ws_ping_interval=10, ws_ping_timeout=20, timeout_graceful_shutdown=5,
    ))
    app.state.desktop_lifecycle = DesktopLifecycle(
        lambda: setattr(server, 'should_exit', True), close_delay=close_delay,
    )
    serving = asyncio.create_task(server.serve())
    try:
        # Open the page only when the listener is ready to accept requests.
        while not server.started and not serving.done():
            await asyncio.sleep(.05)
        if server.started:
            print(f'Atlas: {url}\nClosing the last browser tab stops the application.', flush=True)
            if not no_browser:
                await asyncio.to_thread(webbrowser.open, url)
        await serving
    finally:
        await app.state.desktop_lifecycle.stop()
        del app.state.desktop_lifecycle


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--no-browser', action='store_true')
    parser.add_argument('--close-delay', type=float, default=5.0)
    args = parser.parse_args()
    if not 0 < args.port < 65536 or args.close_delay < .1:
        parser.error('port must be 1..65535 and close-delay must be at least 0.1 seconds')
    asyncio.run(run(args.port, args.no_browser, args.close_delay))


if __name__ == '__main__':
    main()
