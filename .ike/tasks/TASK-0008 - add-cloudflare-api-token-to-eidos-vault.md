---
id: TASK-0008
title: Add Cloudflare API token to eidos-vault
status: To Do
created: '2026-03-22'
priority: low
tags:
  - infra
definition-of-done:
  - Token stored in vault at infra/cloudflare/api-token
  - clawdflare added to .mcp.json or global settings
  - Can modify DNS records via MCP
visionlog_goal_id: GOAL-001
---
Create a Cloudflare API token scoped to eidosagi.com DNS, store in eidos-vault at infra/cloudflare/api-token. Then configure clawdflare as an MCP server so DNS changes can be automated.
