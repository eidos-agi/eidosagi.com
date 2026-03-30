# Site Constitution — eidosagi.com

This document governs all editorial decisions on the site. Read it before touching any page.

## What this site believes

Three arguments, in priority order:

1. **Contracts outlast skills.** JSON Schema contracts define what you want. Skills define how. Models get better at how; what doesn't change.
2. **Data outlasts code.** The smallest structured dataset that produces results is worth more than the app that processes it. Data is the primitive now.
3. **Agents need governance.** Agents deployed without guardrails, decision records, and execution tracking are liabilities with production access.

Every page serves one of these arguments. If a page doesn't serve any of them, it shouldn't exist.

## Page inventory

Each page has one job. When two pages overlap, one owns the concept and the other links.

| Page | Job | Argument served |
|------|-----|-----------------|
| `/` | Pitch the org + trilogy, convert to install | governance |
| `/contract-driven-development` | Argue contracts beat skills with real schemas | contracts |
| `/minimum-viable-data` | Argue data is the primitive, not product | data |
| `/case-studies/grocery` | Prove contracts work with real $260 order | contracts |
| `/case-studies` | Index of case studies | contracts |
| `/trilogy` | Explain the three-tool governance stack | governance |
| `/forges` | Catalog of available forges | contracts (bridge) |
| `/tools` | Index of installable packages | governance |
| `/tools/*` | One tool per page, docs-style | governance |
| `/eidos` | Explain the persistent agent architecture | governance |
| `/about` | Who built this and why | trust |
| `/memory` | EidosOmni architecture (design doc) | governance |
| `/agent-identity` | AID architecture (design doc) | governance |

### Concept ownership

| Concept | Owning page | Others may... |
|---------|-------------|---------------|
| Grocery ordering story | `/case-studies/grocery` | Reference in 1-2 sentences + link |
| Contracts vs skills argument | `/contract-driven-development` | Reference the conclusion, not re-argue |
| Bitter lesson / AlphaZero | `/contract-driven-development` | Do not repeat elsewhere |
| Trilogy pitch (3 tools) | `/` and `/trilogy` | Link, don't re-pitch |
| pip install commands | `/tools` and tool subpages | Homepage hero is fine, nowhere else |
| Grocery video | `/case-studies/grocery` and `/case-studies` | Do not embed elsewhere |

## Shipped vs unshipped

**Main navigation shows things people can install today.** The trilogy, forges, and tools are shipped. They get prominent placement.

Design docs for unbuilt features (`/memory`, `/agent-identity`, parts of `/eidos`) must:
- Carry `status="dev"` badge on PageHero
- Include an explicit "Status" section saying what's built and what isn't
- Never use future-tense language that reads like a shipping announcement
- Live under their current paths but not appear in primary navigation until shipped

## Tension register

| Tension | Resolution |
|---------|------------|
| CDD says skills decay. Forges are skills. | Forges are the bridge — they're the skills that exist until contracts make them unnecessary. The forges page should acknowledge this explicitly. |
| CDD and MVD argue the same side. | CDD argues about the AI primitive (schemas as the durable unit). MVD argues about the business case (data replaces the software layer). They share evidence but serve different readers. If they can't stay differentiated, merge them. |
| Homepage pitches everything at once. | The homepage's job is to convert a developer to `pip install`. Everything else (philosophy, enterprise, recruiting) is secondary. If a homepage section doesn't serve the install path, it's a candidate for its own page or removal. |
| Memory/Identity pages promise unshipped features. | They exist as architectural design docs. Honest framing earns more trust than marketing copy for vaporware. |

## Reader journeys

### The evaluating developer
Heard about the trilogy, wants to know if it's real.
1. `/` (problem + solution + install)
2. `/trilogy` (how the three tools work together)
3. `/tools/visionlog` or `/tools/ike` (pick one, try it)

### The architecture thinker
Interested in the contracts philosophy, found via blog/twitter.
1. `/contract-driven-development` (the argument with real schemas)
2. `/case-studies/grocery` (the proof)
3. `/minimum-viable-data` (the business implications)

### The curious clicker
Saw the grocery video, wants to understand.
1. `/case-studies/grocery` (the full story)
2. `/contract-driven-development` (the principle behind it)
3. `/forges` or `/trilogy` (what else exists)

### Rules for journeys
- Every page's RelatedLinks should nudge toward the next page in at least one journey
- No dead ends — every page links forward
- The install command should be reachable within 2 clicks from any page

## What this site is NOT

- A SaaS landing page (no pricing, no "book a demo", no testimonial carousel)
- A documentation site (tool pages are overviews, not API refs — link to GitHub for full docs)
- A blog (no dated posts, no "we're excited to announce")
- Generic (if you could swap the logo and it could be any AI company, something is wrong)

## Editorial process

Before any deploy that touches text:
1. Read this document
2. Run `/copy-audit` (voice, redundancy, anti-patterns)
3. Check page inventory — is each page still doing one job?
4. Check concept ownership — is any concept retold instead of linked?
5. Check reader journeys — do RelatedLinks still guide each persona?
