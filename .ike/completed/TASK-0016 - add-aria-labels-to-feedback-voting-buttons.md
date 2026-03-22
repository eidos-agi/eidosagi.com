---
id: TASK-0016
title: Add aria-labels to feedback voting buttons
status: Done
created: '2026-03-22'
priority: medium
tags:
  - accessibility
definition-of-done:
  - All .fbs-btn elements have aria-label
  - Feedback toggle has aria-label
  - 'Screen reader announces ''Like [section name]'' / ''Dislike [section name]'''
updated: '2026-03-22'
---
Emoji thumbs up/down buttons have no aria-label. Screen readers announce them as unicode code points. Add aria-label='Like' and aria-label='Dislike' to all vote buttons. Also add aria-label to feedback toggle button.

**Completion notes:** Added aria-label='Like [section]' and aria-label='Dislike [section]' to all dynamically created vote buttons. Added aria-label='Open feedback panel' to toggle button.
