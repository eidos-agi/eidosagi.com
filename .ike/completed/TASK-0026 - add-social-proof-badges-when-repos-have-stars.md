---
id: TASK-0026
title: Add social proof badges when repos have stars
status: Done
created: '2026-03-23'
priority: medium
tags:
  - marketing
  - score
definition-of-done:
  - GitHub star count visible on each tool card
  - PyPI monthly downloads on tool pages
  - 'Data is live, not hardcoded'
  - Graceful fallback if API is down
updated: '2026-03-23'
---
GitHub stars and PyPI download counts on tool cards + tool pages. Use Shields.io badges or build-time fetch from GitHub/PyPI APIs. Currently all repos at 0 stars — implement now but it'll show value when repos gain traction. Moves MARKETING 7→9.

**Completion notes:** Build-time fetch from GitHub API + pypistats.org. Badges render only when count > 0. resume-resume: 238 downloads/mo. eidos-mcp-registry: 115. Stars will appear when repos gain traction — zero code change needed.
