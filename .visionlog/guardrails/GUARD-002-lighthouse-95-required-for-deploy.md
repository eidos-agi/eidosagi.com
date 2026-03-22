---
id: "GUARD-002"
type: "guardrail"
title: "Lighthouse 95+ required for deploy"
status: "active"
date: "2026-03-22"
---

## Rule
The site must score 95+ on Lighthouse Performance before any production deploy. Accessibility must be 100. No exceptions.

## Why
From the book: "You earn the right to be weird by being provably good first." Performance is the price of admission for visual distinction.

## Violation Examples
- Deploying with Lighthouse Performance at 88
- Adding a JS framework that drops the score below 95
- Loading unoptimized images that crater LCP
