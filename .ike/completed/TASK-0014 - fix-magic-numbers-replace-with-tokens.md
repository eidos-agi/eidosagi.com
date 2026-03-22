---
id: TASK-0014
title: Fix magic numbers — replace with tokens
status: Done
created: '2026-03-22'
priority: medium
tags:
  - design-system
definition-of-done:
  - Zero raw px values in index.astro styles (outside SVG viewBox)
  - All spacing uses var(--space-*)
  - All font sizes use var(--text-*)
updated: '2026-03-22'
---
5 magic numbers found: hero SVG width 280px, theme dot gap 6px, fbs-btn padding 2px 6px, fbs-comment placeholder 11px, fbs-btn font-size 16px. Replace all with CSS custom properties from tokens.css.

**Completion notes:** Replaced 6px gap, 12px dot size, 2px padding, 2px 6px padding with CSS custom properties. AI reader mode kept raw values intentionally (design system stripped by design).
