---
id: '0004'
title: 'JSON Schema is the established industry standard for machine-readable contracts'
status: open
evidence: REASONED
sources:
- text: 'API Evangelist: JSON Schema Defining and Validating API Operations — ''every
    aspect of API operations defined by JSON Schema'' (content_hash:c4ca597c)'
  tier: EXPERT
- text: Model Context Protocol specification (modelcontextprotocol.io) — uses JSON
    Schema for tool definitions
  tier: PRIMARY
disconfirmation: 'Protocol Buffers, Avro, and TypeScript types also define contracts.
  But JSON Schema is the most adopted for AI agent interfaces (MCP, OpenAPI) and the
  most human-readable, aligning with MVD''s principle that data should be readable
  without tools.'
created: '2026-03-29'
---

## Claim

JSON Schema is already the backbone of machine-readable contracts across the industry. OpenAPI and AsyncAPI both use it. The Model Context Protocol (MCP) — the standard for AI agent tool interfaces — uses JSON Schema for tool definitions. Using JSON Schema as the contract format for MVD extends an established standard from API contracts to AI agent contracts. This is not a new format — it's applying an existing one to a new domain.

## Supporting Evidence

> **Source [EXPERT]:** API Evangelist: JSON Schema Defining and Validating API Operations — 'every aspect of API operations defined by JSON Schema' (content_hash:c4ca597c), retrieved 2026-03-29
>
> **Source [PRIMARY]:** Model Context Protocol specification (modelcontextprotocol.io) — uses JSON Schema for tool definitions, retrieved 2026-03-29

## Disconfirmation Search

Protocol Buffers, Avro, and TypeScript types also define contracts. But JSON Schema is the most adopted for AI agent interfaces (MCP, OpenAPI) and the most human-readable, aligning with MVD's principle that data should be readable without tools.

## Caveats

None identified yet.
