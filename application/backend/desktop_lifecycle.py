"""Lifetime of a local desktop session, tracked by live browser connections."""
import asyncio


class DesktopLifecycle:
    def __init__(self, shutdown, close_delay=5.0):
        self.shutdown = shutdown
        self.close_delay = close_delay
        self.connections = set()
        self.pending = None

    def connected(self):
        if self.pending is not None:
            self.pending.cancel()
            self.pending = None
        token = object()
        self.connections.add(token)
        return token

    def disconnected(self, token):
        if token not in self.connections:
            return
        self.connections.remove(token)
        if not self.connections and self.pending is None:
            self.pending = asyncio.create_task(self._finish_after_delay())

    async def _finish_after_delay(self):
        try:
            await asyncio.sleep(self.close_delay)
            if not self.connections:
                self.shutdown()
        except asyncio.CancelledError:
            pass

    async def stop(self):
        if self.pending is not None:
            self.pending.cancel()
            await self.pending
            self.pending = None
