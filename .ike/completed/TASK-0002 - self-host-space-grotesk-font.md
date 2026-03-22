---
id: TASK-0002
title: Self-host Space Grotesk font
status: Done
created: '2026-03-22'
priority: medium
tags:
  - performance
definition-of-done:
  - WOFF2 files in public/fonts/
  - No Google Fonts link in head
  - 'font-display: optional on @font-face'
  - Lighthouse Performance still 95+
visionlog_goal_id: GOAL-001
updated: '2026-03-22'
---
Currently loading from Google Fonts CDN. Self-host as subsetted WOFF2 to eliminate third-party DNS lookup and guarantee load performance. The book demands it.

**Completion notes:** Self-hosted SpaceGrotesk-latin.woff2 (22KB). Variable font covers 400-700 weights. Google Fonts link removed. Preload in head. font-display: optional. Build succeeds.
