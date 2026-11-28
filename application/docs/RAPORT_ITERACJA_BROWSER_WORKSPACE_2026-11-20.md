# Browser workspace lifecycle — 2026-11-20

Real GitHub Actions run [#44707579176](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44707579176) passed on commit 61d12f0: unit tests, Chromium reader/graph, draft creation, explicit save, navigation away, draft cleanup, saved ZIP retention. Test now uses a dynamic port and the current Python interpreter. The frontend has a beforeunload fallback alongside pagehide.

**Limit:** Playwright page.close did not demonstrate reliable cleanup; the green test uses navigation to about:blank. This is a page-leave test, **not a verified browser X-close test**. Crash recovery remains TTL-based. No mathematical chapters were edited.
