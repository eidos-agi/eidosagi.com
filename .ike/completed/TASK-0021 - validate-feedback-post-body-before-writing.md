---
id: TASK-0021
title: Validate feedback POST body before writing
status: Done
created: '2026-03-22'
priority: medium
tags:
  - security
definition-of-done:
  - POST body validated for expected shape
  - Reject payloads > 10KB
  - Invalid bodies return 400
updated: '2026-03-22'
---
feedback.ts writes request.json() directly to disk without validation. Malformed or oversized payloads could corrupt the JSONL file or fill disk. Add schema validation and size limits.

**Completion notes:** Done as part of TASK-0015 — POST body validated, 10KB limit, rejects with 400.
