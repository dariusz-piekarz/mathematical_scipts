"""Manage ephemeral generated projects and explicitly saved projects.

Only server-owned UUID directories below the configured drafts root can be
removed. Saved projects use a separate directory and are never touched by
session cleanup. No canonical TeX files or the SQLite index are modified.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import shutil
import threading
import time
from uuid import uuid4

SESSION_ID = re.compile(r"^[0-9a-f]{32}$")
DEFAULT_TTL_SECONDS = 24 * 60 * 60
_MAX_ARCHIVE_BYTES = 32 * 1024 * 1024
_LOCK = threading.RLock()


class WorkspaceError(ValueError):
    """Invalid draft, saved project, or storage operation."""


def _root(name: str, default: Path) -> Path:
    return Path(os.environ.get(name, str(default))).expanduser().resolve()


def _directories() -> tuple[Path, Path]:
    base = Path(__file__).resolve().parents[1] / "data"
    return _root("MATLIB_DRAFTS_ROOT", base / ".temporary_projects"), _root("MATLIB_SAVED_ROOT", base / "saved_projects")


def _id(value: str) -> str:
    if not SESSION_ID.fullmatch(value):
        raise WorkspaceError("Invalid project identifier.")
    return value


def _draft_dir(session_id: str) -> Path:
    base, _ = _directories()
    return base / _id(session_id)


def _saved_path(project_id: str) -> Path:
    _, base = _directories()
    return base / (_id(project_id) + ".zip")


def stage_project(archive: bytes, manifest: dict, session_id: str | None = None) -> dict:
    """Create or replace one unsaved draft within a browser-tab session."""
    if not archive or len(archive) > _MAX_ARCHIVE_BYTES:
        raise WorkspaceError("Archive is empty or exceeds the 32 MiB draft limit.")
    with _LOCK:
        root, _ = _directories()
        root.mkdir(parents=True, exist_ok=True)
        if session_id:
            directory = _draft_dir(session_id)
            if directory.is_symlink() or not directory.is_dir():
                raise WorkspaceError("Draft session has expired.")
            sid = session_id
        else:
            sid = uuid4().hex
            directory = root / sid
            directory.mkdir(mode=0o700)
        temporary = directory / (uuid4().hex + ".tmp")
        try:
            temporary.write_bytes(archive)
            os.replace(temporary, directory / "project.zip")
            (directory / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        finally:
            temporary.unlink(missing_ok=True)
        os.utime(directory, None)
        return {"session_id": sid, "saved": False, "size_bytes": len(archive),
                "download_url": f"/api/drafts/{sid}/download",
                "modules": len(manifest.get("modules", []))}


def get_draft_archive(session_id: str) -> Path:
    with _LOCK:
        directory = _draft_dir(session_id)
        archive = directory / "project.zip"
        if not archive.is_file():
            raise WorkspaceError("Draft was not found or was already removed.")
        os.utime(directory, None)
        return archive


def save_draft(session_id: str) -> dict:
    """Explicit user save: a saved copy survives closing the browser tab."""
    with _LOCK:
        source = get_draft_archive(session_id)
        _, saved_root = _directories()
        saved_root.mkdir(parents=True, exist_ok=True)
        pid = uuid4().hex
        dest = saved_root / (pid + ".zip")
        # Exclusive creation avoids overwriting another explicitly saved project.
        with dest.open("xb") as out, source.open("rb") as src:
            shutil.copyfileobj(src, out)
        details = json.loads((_draft_dir(session_id) / "manifest.json").read_text(encoding="utf-8"))
        metadata = {"project_id": pid, "title": str(details.get("title", "Mathematical project"))[:160],
                    "created_at": time.time(), "size_bytes": dest.stat().st_size}
        (saved_root / (pid + ".json")).write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
        return {**metadata, "download_url": f"/api/projects/{pid}/download", "saved": True}


def get_saved_archive(project_id: str) -> Path:
    path = _saved_path(project_id)
    if not path.is_file():
        raise WorkspaceError("Saved project not found.")
    return path


def list_saved_projects() -> list[dict]:
    _, root = _directories()
    if not root.exists():
        return []
    projects = []
    for entry in root.glob("*.json"):
        if not SESSION_ID.fullmatch(entry.stem) or not (root / (entry.stem + ".zip")).is_file():
            continue
        try:
            data = json.loads(entry.read_text(encoding="utf-8"))
            projects.append({**data, "download_url": f"/api/projects/{entry.stem}/download"})
        except (OSError, ValueError):
            continue
    return sorted(projects, key=lambda x: x.get("created_at", 0), reverse=True)


def close_draft(session_id: str) -> bool:
    """Remove only this tab's unsaved output; never access the saved directory."""
    with _LOCK:
        directory = _draft_dir(session_id)
        if not directory.is_dir():
            return False
        shutil.rmtree(directory)
        return True


def cleanup_stale_drafts(ttl_seconds: int = DEFAULT_TTL_SECONDS) -> int:
    """Crash recovery: prune old drafts, without touching saved projects."""
    if ttl_seconds < 0:
        raise WorkspaceError("TTL must be non-negative.")
    with _LOCK:
        root, _ = _directories()
        if not root.exists():
            return 0
        threshold = time.time() - ttl_seconds
        removed = 0
        for entry in root.iterdir():
            if entry.is_symlink() or not entry.is_dir() or not SESSION_ID.fullmatch(entry.name):
                continue
            if entry.stat().st_mtime <= threshold:
                shutil.rmtree(entry)
                removed += 1
        return removed
