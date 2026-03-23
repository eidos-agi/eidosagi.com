---
id: TASK-0033
title: Add interactive diagram to agent-identity page
status: Done
created: '2026-03-23'
priority: high
tags:
  - visual
  - human-score
definition-of-done:
  - Delegation flow diagram on agent-identity page
  - Shows human → token → agent → system
  - Animated arrows (CSS only)
  - Responsive
updated: '2026-03-23'
---
The agent-identity page is 3 short text sections. Add an SVG showing the delegation flow: Human (principal) → signs delegation token → Agent (executor) → presents to System (verifier). Animated arrows like the trilogy flow diagram. Shows the separation of authority visually.

**Completion notes:** Two animated SVG diagrams: 1) Problem diagram showing borrowed identity (red arrows, 'Who actually did this?'), 2) Delegation flow showing Human → signs AID Token → Agent carries → presents to System → System verifies (animated dashed arrows, feedback loop). Same visual style as hero flow diagram.
