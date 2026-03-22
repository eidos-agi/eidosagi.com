---
id: TASK-0020
title: Add tool page mobile responsive breakpoints
status: Done
created: '2026-03-22'
priority: medium
tags:
  - responsive
definition-of-done:
  - Tool pages render cleanly on 375px width
  - No horizontal overflow
  - pip install code scrolls if needed
updated: '2026-03-22'
---
Tool.astro has only one mobile breakpoint (tool-hero padding). pip install code may overflow on narrow screens. Pre blocks need overflow-x: auto. Actions row needs flex-wrap.

**Completion notes:** Added mobile breakpoints to Tool.astro: smaller h1, stacked actions, pip code scrollable, smaller pre text, tighter page padding.
