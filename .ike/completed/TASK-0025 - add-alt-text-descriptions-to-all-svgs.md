---
id: TASK-0025
title: Add alt text / descriptions to all SVGs
status: Done
created: '2026-03-23'
priority: high
tags:
  - accessibility
  - score
definition-of-done:
  - All SVGs have aria-label or figcaption
  - Screen reader announces diagram purpose
  - 'Score: ACCESSIBILITY 10/10'
updated: '2026-03-23'
---
Flow diagram and trilogy mini-charts have no screen reader descriptions. Wrap in figure/figcaption or add role='img' aria-label='...'. Moves ACCESSIBILITY 8→10. ~15 min.

**Completion notes:** Added role='img' + aria-label to all 4 SVGs: flow diagram, guardrail bars, decision funnel, task checklist. Screen readers now announce purpose of each visual.
