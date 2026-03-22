---
id: TASK-0022
title: Truncate User-Agent in feedback logs
status: Done
created: '2026-03-22'
priority: low
tags:
  - security
definition-of-done:
  - UA truncated to 256 chars in feedback.ts
updated: '2026-03-22'
---
User-Agent header stored raw in feedback.jsonl. Truncate to 256 chars to prevent data bloat from malformed UA strings.

**Completion notes:** Done as part of TASK-0015 — UA sliced to 256 chars.
