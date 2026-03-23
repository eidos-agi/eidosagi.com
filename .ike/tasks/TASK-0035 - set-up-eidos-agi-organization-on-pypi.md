---
id: TASK-0035
title: Set up Eidos AGI organization on PyPI
status: To Do
created: '2026-03-23'
priority: high
tags:
  - infra
  - brand
definition-of-done:
  - PyPI org 'eidos-agi' created
  - All 9 packages transferred to org
  - Org profile has description + URL + logo
  - pypi.org/org/eidos-agi/ shows all packages
---
PyPI now supports organizations. Set up the eidos-agi org so all 9 packages are owned by the org, not a personal account. This gives us a branded profile page at pypi.org/org/eidos-agi/ and lets multiple maintainers manage packages.

Instructions:
1. Go to https://pypi.org/manage/organizations/
2. Create organization:
   - Name: eidos-agi
   - Display name: Eidos AGI
   - Organization URL: https://eidosagi.com
   - Description: Open-source governance infrastructure for AI agents. 9 packages. All MIT.
3. Choose plan (Community plan is free for open-source)
4. Add members: invite co-maintainers with appropriate roles
5. Transfer packages: for each of the 9 packages, go to Settings → Transfer → select eidos-agi org
   - visionlog-md
   - research-md
   - ike-md
   - railguey
   - clawdflare
   - eidos-mcp-registry
   - resume-resume
   - apple-a-day
   - claude-session-commons
6. Update org profile: add logo, description, links
7. Verify: check https://pypi.org/org/eidos-agi/ shows all packages
