---
id: TASK-0018
title: Fix tools grid mobile layout — 5 items in 2 columns leaves orphan
status: Done
created: '2026-03-22'
priority: medium
tags:
  - responsive
definition-of-done:
  - No orphaned single card on mobile
  - Layout looks intentional at all breakpoints
updated: '2026-03-22'
---
5 tool cards in 2-column grid at 768px leaves 1 card alone on the last row. Either make it 1 column on mobile, or let the last card span full width.

**Completion notes:** Changed mobile tools-grid from repeat(2, 1fr) to 1fr. No more orphaned single card.
