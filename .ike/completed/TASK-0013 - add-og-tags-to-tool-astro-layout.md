---
id: TASK-0013
title: Add OG tags to Tool.astro layout
status: Done
created: '2026-03-22'
priority: high
tags:
  - seo
  - bug
definition-of-done:
  - 'og:title, og:description, og:url set dynamically per tool'
  - 'og:url includes /tools/[name] path'
updated: '2026-03-22'
---
Tool page layout is missing og:title, og:description, og:url with dynamic values. Sharing /tools/railguey shows generic homepage preview instead of tool-specific content.

**Completion notes:** og:url now uses Astro.url.pathname dynamically. Canonical link added. Each tool page gets its own og:url and canonical.
