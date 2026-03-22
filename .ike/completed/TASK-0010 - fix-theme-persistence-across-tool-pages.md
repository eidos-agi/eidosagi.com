---
id: TASK-0010
title: Fix theme persistence across tool pages
status: Done
created: '2026-03-22'
priority: high
tags:
  - bug
definition-of-done:
  - 'Switch theme on landing, navigate to /tools/visionlog, theme persists'
  - All 6 themes + AI mode work on tool pages
updated: '2026-03-22'
---
Theme JS only ran on index.astro. Added inline script to Base.astro to read localStorage before paint. Verify all 8 tool pages honor the selected theme.

**Completion notes:** Fixed last session — added inline script to Base.astro that reads localStorage('eidos-theme') and sets data-theme before paint. All pages including tool pages now honor saved theme.
