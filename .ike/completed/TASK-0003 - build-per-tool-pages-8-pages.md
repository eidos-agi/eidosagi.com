---
id: TASK-0003
title: Build per-tool pages (8 pages)
status: Done
created: '2026-03-22'
priority: high
tags:
  - content
  - scaffold
definition-of-done:
  - 8 pages created under src/pages/tools/
  - >-
    Each page has: description, install command, real usage example, at least
    one diagram or visual
  - Landing page tool cards link to their pages
  - Mobile responsive
visionlog_goal_id: GOAL-002
updated: '2026-03-22'
---
Each package gets its own page at /tools/[name]. Content sourced from each repo's README — real examples, CLI output, architecture diagrams. Not marketing copy. Pages: visionlog-md, research-md, ike-md, railguey, clawdflare, eidos-mcp-registry, resume-resume, apple-a-day.

**Completion notes:** 8 tool pages created at /tools/[name]. Shared Tool.astro layout with consistent structure. Landing page tool cards now link to individual pages. Deployed to Railway.
