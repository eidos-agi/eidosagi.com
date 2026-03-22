---
id: TASK-0024
title: Dynamic copyright year in footer
status: To Do
created: '2026-03-22'
priority: low
tags:
  - content
definition-of-done:
  - Footer shows current year dynamically
---
Footer hardcodes '2026'. Use new Date().getFullYear() or Astro server-side rendering to keep it current.
