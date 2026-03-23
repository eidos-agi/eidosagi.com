---
id: TASK-0030
title: Add maintenance signals to tool pages
status: Done
created: '2026-03-23'
priority: medium
tags:
  - human-score
  - trust
definition-of-done:
  - Each tool page shows latest PyPI version
  - Last release date visible
  - 'Data fetched at build time, graceful fallback on failure'
updated: '2026-03-23'
---
Developers trust activity, not philosophy. Add build-time fetched signals to each tool page: latest version from PyPI, last release date, test badge if available. Not badges for vanity — evidence that someone maintains this. Moves TRUST 6→8.

**Completion notes:** PyPI version + release date fetched at build time via pypi.org/pypi/{pkg}/json. Badges show alongside stars/downloads (only when data exists). Hamburger menu + mobile nav now in global.css — shared across landing + all tool pages. Duplicate CSS removed from index.astro.
