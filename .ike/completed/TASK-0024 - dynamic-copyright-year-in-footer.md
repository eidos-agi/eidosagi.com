---
id: TASK-0024
title: Dynamic copyright year in footer
status: Done
created: '2026-03-22'
priority: low
tags:
  - content
definition-of-done:
  - Footer shows current year dynamically
updated: '2026-03-22'
---
Footer hardcodes '2026'. Use new Date().getFullYear() or Astro server-side rendering to keep it current.

**Completion notes:** Both footers (index.astro + Tool.astro) now use new Date().getFullYear() instead of hardcoded 2026.
