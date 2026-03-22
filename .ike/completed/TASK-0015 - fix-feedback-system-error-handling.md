---
id: TASK-0015
title: Fix feedback system error handling
status: Done
created: '2026-03-22'
priority: medium
tags:
  - bug
definition-of-done:
  - POST failure shows user a warning
  - 'GET wraps each JSON.parse in try/catch, skips bad lines'
  - feedback.ts uses absolute path or env var for FEEDBACK_FILE
updated: '2026-03-22'
---
Two bugs: 1) POST .catch(() => {}) silently swallows errors — user gets false success. 2) GET endpoint JSON.parse on feedback.jsonl crashes on malformed lines. Fix both.

**Completion notes:** POST: added 10KB size limit, body type validation, try/catch, UA truncation to 256 chars. GET: wrapped JSON.parse in try/catch per line, skips malformed. Client: .catch shows offline warning instead of swallowing silently.
