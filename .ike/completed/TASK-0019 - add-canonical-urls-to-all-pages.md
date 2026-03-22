---
id: TASK-0019
title: Add canonical URLs to all pages
status: Done
created: '2026-03-22'
priority: medium
tags:
  - seo
definition-of-done:
  - 'Every page has <link rel=''canonical'' href=''https://eidosagi.com/...''>'
  - URL matches the actual page path
updated: '2026-03-22'
---
No canonical meta tags on any page. Add <link rel='canonical'> to Base.astro with dynamic URL based on current path.

**Completion notes:** Canonical URLs added to Base.astro using Astro.url.pathname. All 9 pages now have <link rel=canonical>.
