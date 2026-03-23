---
id: TASK-0061
title: Self-host substack images instead of linking LinkedIn CDN
status: To Do
created: '2026-03-23'
priority: medium
tags:
  - reliability
---
The SVG substack images reference daniel.jpg via relative path which works locally but the LinkedIn CDN URL used to download it will expire. The photo is already in public/ so this is fine for now, but verify all SVG image references resolve correctly in production.
