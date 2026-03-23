---
id: "ADR-001"
type: "decision"
title: "No inline feedback UI — thumbs-up/down creates heft"
status: "accepted"
date: "2026-03-23"
---

## Decision

Remove all thumbs-up/thumbs-down voting UI, per-component vote bars, and the feedback drawer from the site. The feedback API endpoint (/api/feedback) can stay for programmatic use, but no visible voting interface on the site.

## Why

The founder observed that inline voting widgets create heft — visual weight and interaction complexity that doesn't justify itself on a site this size. Every button, drawer, and badge adds cognitive load. For a site whose identity is "confident and unhurried," a slide-out feedback panel with 12 voting rows is the opposite of that.

## What was removed

- Feedback toggle button (?)
- Feedback drawer with per-section voting
- data-component attributes on all sections
- Per-component hover vote bars
- ~200 lines of CSS
- ~120 lines of JS

## What remains

- /api/feedback POST endpoint (server-side, for programmatic use)
- feedback.jsonl logging (if the endpoint is called)

## Applies to

All Eidos AGI web properties. Don't build inline thumbs-up/down UIs. If feedback is needed, use GitHub Issues or direct conversation.
