---
id: TASK-0034
title: Add diagrams to tool pages (at least trilogy)
status: Done
created: '2026-03-23'
priority: medium
tags:
  - visual
  - human-score
definition-of-done:
  - 'visionlog, research, ike pages each have 1 diagram'
  - Diagrams match the visual style of hero flow diagram
  - Animated where appropriate
updated: '2026-03-23'
---
Tool pages are text + code blocks. Each trilogy tool page should have a diagram showing where it sits in the governance flow. visionlog: guardrail enforcement diagram. research.md: decision funnel with phases. ike.md: task lifecycle (To Do → In Progress → Done with dependencies). Reuse the flow diagram style from the landing page.

**Completion notes:** Three animated diagrams: visionlog (guardrail enforcement gate), research.md (6-phase decision pipeline with lock marker), ike.md (task lifecycle with DoD check). All use shared td-* CSS classes in Tool.astro.
