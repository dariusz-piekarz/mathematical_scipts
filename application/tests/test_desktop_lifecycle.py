import asyncio
import unittest
from unittest.mock import Mock

from fastapi.testclient import TestClient
from starlette.websockets import WebSocketDisconnect
from backend.api import app
from backend.desktop_lifecycle import DesktopLifecycle


class LifecycleTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.shutdown = Mock()
        self.lifecycle = DesktopLifecycle(self.shutdown, close_delay=.02)

    async def asyncTearDown(self):
        await self.lifecycle.stop()

    async def test_waits_for_first_page_and_last_tab(self):
        await asyncio.sleep(.03)
        self.shutdown.assert_not_called()
        first, second = self.lifecycle.connected(), self.lifecycle.connected()
        self.lifecycle.disconnected(first)
        self.lifecycle.disconnected(first)
        await asyncio.sleep(.03)
        self.shutdown.assert_not_called()
        self.lifecycle.disconnected(second)
        await asyncio.sleep(.04)
        self.shutdown.assert_called_once()

    async def test_reload_cancels_shutdown(self):
        self.lifecycle.disconnected(self.lifecycle.connected())
        await asyncio.sleep(.005)
        token = self.lifecycle.connected()
        await asyncio.sleep(.04)
        self.shutdown.assert_not_called()
        self.lifecycle.disconnected(token)
        await asyncio.sleep(.04)
        self.shutdown.assert_called_once()


class SocketOriginTests(unittest.TestCase):
    def test_other_origins_are_rejected(self):
        with TestClient(app) as client:
            with self.assertRaises(WebSocketDisconnect):
                with client.websocket_connect('/api/lifecycle/socket', headers={'origin': 'http://other.example'}):
                    self.fail('foreign website connected')

    def test_developer_server_is_not_managed(self):
        with TestClient(app, base_url='http://127.0.0.1:8765') as client:
            with client.websocket_connect('ws://127.0.0.1:8765/api/lifecycle/socket', headers={'origin': 'http://127.0.0.1:8765'}) as socket:
                self.assertEqual(socket.receive_json(), {'managed': False})


if __name__ == '__main__':
    unittest.main()
