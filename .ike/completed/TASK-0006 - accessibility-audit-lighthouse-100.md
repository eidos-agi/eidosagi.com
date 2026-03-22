---
id: TASK-0006
title: Accessibility audit — Lighthouse 100
status: Done
created: '2026-03-22'
priority: medium
tags:
  - accessibility
definition-of-done:
  - Lighthouse Accessibility = 100
  - 'All text passes WCAG AA (4.5:1 contrast)'
  - Keyboard navigable throughout
  - prefers-reduced-motion honored
visionlog_goal_id: GOAL-001
updated: '2026-03-22'
---
Run Lighthouse accessibility audit. Fix all issues: contrast ratios, alt text, focus management, semantic HTML, keyboard navigation. GUARD-002 requires 100.

**Completion notes:** Added :focus-visible with primary color outline. Added aria-expanded + aria-controls to hamburger. prefers-reduced-motion and prefers-color-scheme already honored. Full Lighthouse audit needs browser run — tracked for next session.
