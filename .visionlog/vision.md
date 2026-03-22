---
title: "eidosagi.com — The public face of Eidos AGI"
type: "vision"
date: "2026-03-22"
---

## What this is

The website for Eidos AGI. Not a marketing site — a workshop. A place where engineers, researchers, and security people can see what we build, understand why we build it, and start using it in under 30 seconds.

## North star

Amazon didn't create the internet. It created the trust infrastructure that made people willing to buy from strangers online. We're doing the same thing for AI agents. This site must communicate that clearly, quickly, and without sales pitch.

## Design philosophy

Follows the book at `~/repos-eidos-agi/books/railway-websites/`:
- Swiss precision as structure, 1970s warmth as mood
- Anti-commodity: no gradient blobs, no AI illustrations, no three-column feature grids
- Lighthouse 95+ before earning the right to be weird
- A well-organized workshop, not a showroom
- Every element reflects a decision made by a person

## What the site must do

1. Show the tools (Trilogy + MCP + Agent) with pip install commands visible immediately
2. Explain the trust thesis (open source as trust infrastructure, not charity)
3. Convert visitors into users — GitHub repos, PyPI installs
4. Each tool gets its own page with real examples, graphs, and usage
5. Multiple themes for personality, AI reader mode for agents
6. Feedback system that logs user reactions to guide iteration

## Stack

- Astro + @astrojs/node (hybrid SSR for feedback API)
- Railway deployment, Cloudflare DNS
- Space Grotesk typography, warm token palette
- Zero framework JS — vanilla scripts only
- Server-side feedback logging to feedback.jsonl
