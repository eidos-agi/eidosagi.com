---
id: TASK-0017
title: Add copy button to pip install code blocks
status: Done
created: '2026-03-22'
priority: medium
tags:
  - dx
  - ux
definition-of-done:
  - Copy button visible on hover over code blocks
  - Click copies text to clipboard
  - Visual confirmation (checkmark or 'Copied')
updated: '2026-03-22'
---
Users must manually select and copy pip install commands. Add a small copy-to-clipboard button on each code block. Vanilla JS, no dependencies.

**Completion notes:** Copy button appears on hover over any pre block in tool pages. Uses navigator.clipboard API. Shows "Copied" for 1.5s. Styled with tokens, hidden until hover.
