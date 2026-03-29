---
id: TASK-0064
title: /stale-check skill — detect content drift against live PyPI data
status: To Do
created: '2026-03-28'
priority: medium
tags:
  - skill
  - drift-detection
  - pypi
---
Build a /stale-check skill for the eidosagi.com repo that compares what the site displays against live PyPI data and marketplace.json.

## What it checks
- Version numbers on tool pages vs current PyPI versions
- Tool list on the index page vs marketplace.json plugins list
- Download counts (stale is fine, just flag if a tool is missing)
- Any tool page that exists in marketplace but not on the site (or vice versa)

## Output
A simple report: what's current, what's stale, what's missing. No automation — just visibility so you know what to update when you're working on the site.

## Why manual, not automated
- Site changes ~weekly, not daily
- When releasing, you're already in a session where you can run the check
- Industry pattern (docs in package repo) doesn't apply — this is a portfolio site across 13+ repos
- Automation (cron, webhooks) is overkill for the frequency of changes
