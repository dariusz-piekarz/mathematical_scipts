"""Session draft lifecycle: X-close cleanup, persistence, safe id handling."""
from __future__ import annotations

import os
from pathlib import Path
import tempfile
import time
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient
from backend.api import app
from backend import workspaces


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.env = patch.dict(os.environ, {
            "MATLIB_DRAFTS_ROOT": str(Path(self.tmp.name) / "drafts"),
            "MATLIB_SAVED_ROOT": str(Path(self.tmp.name) / "saved")})
        self.env.start()
        self.addCleanup(self.env.stop)
        self._client_context = TestClient(app)
        self.client = self._client_context.__enter__()
        self.addCleanup(self._client_context.__exit__, None, None, None)
        self.archive = b"test-zip-content"
        self.manifest = {"title": "Test project", "modules": ["BT-00"]}

    def test_unsaved_draft_removed_at_x_close(self):
        item = workspaces.stage_project(self.archive, self.manifest)
        draft_id = item["session_id"]
        self.assertEqual(workspaces.get_draft_archive(draft_id).read_bytes(), self.archive)
        res = self.client.post(f"/api/drafts/{draft_id}/close")
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.json()["removed"])
        self.assertFalse(workspaces.get_draft_archive.__globals__["_draft_dir"](draft_id).exists())
        self.assertFalse(self.client.post(f"/api/drafts/{draft_id}/close").json()["removed"])

    def test_saved_project_survives_tab_close(self):
        item = workspaces.stage_project(self.archive, self.manifest)
        draft_id = item["session_id"]
        res = self.client.post(f"/api/drafts/{draft_id}/save")
        self.assertEqual(res.status_code, 200)
        pid = res.json()["project_id"]
        self.client.post(f"/api/drafts/{draft_id}/close")
        self.assertEqual(self.client.get(f"/api/projects/{pid}/download").content, self.archive)
        self.assertIn(pid, [x["project_id"] for x in self.client.get("/api/projects").json()["items"]])

    def test_sessions_isolated(self):
        a = workspaces.stage_project(b"first", self.manifest)
        b = workspaces.stage_project(b"second", self.manifest)
        workspaces.close_draft(a["session_id"])
        self.assertEqual(workspaces.get_draft_archive(b["session_id"]).read_bytes(), b"second")

    def test_ttl_removes_only_drafts(self):
        a = workspaces.stage_project(self.archive, self.manifest)
        saved = workspaces.save_draft(a["session_id"])
        d = Path(os.environ["MATLIB_DRAFTS_ROOT"]) / a["session_id"]
        os.utime(d, (time.time() - 3600, time.time() - 3600))
        self.assertEqual(workspaces.cleanup_stale_drafts(1000), 1)
        self.assertTrue(workspaces.get_saved_archive(saved["project_id"]).is_file())

    def test_reject_path_traversal(self):
        for invalid in ["../saved", "hi", "a"*50, "..%2fdata"]:
            with self.assertRaises(workspaces.WorkspaceError):
                workspaces.close_draft(invalid)
        self.assertEqual(self.client.get("/api/drafts/invalid/download").status_code, 404)

    def test_create_draft_api(self):
        res = self.client.post('/api/drafts',json={"modules":["BT-00"],"title":"Example","entities":[],"closure_depth":0})
        self.assertEqual(res.status_code,200,res.text)
        doc=res.json()
        self.assertGreater(doc["size_bytes"],1000)
        self.assertIn("attachment",self.client.get(doc["download_url"]).headers["content-disposition"])
        self.client.post(f'/api/drafts/{doc["session_id"]}/close')
        self.assertEqual(self.client.get(doc["download_url"]).status_code,404)

if __name__ == "__main__":
    unittest.main()