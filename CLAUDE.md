# CLAUDE.md — eidosagi.com

> The Eidos AGI website. Astro + Railway. Craft, not commodity.

## What This Is

The public face of Eidos AGI — a stealth group of engineers, AI researchers, and cybersecurity experts building agentic-first software. The site must communicate:

1. **Who we are** — stealth group, day jobs, building what industry won't
2. **What we build** — infrastructure that makes existing AI go further (9 PyPI packages, all open source)
3. **Why it matters** — agents are getting deployed into real systems NOW, they need governance
4. **Join us** — open invitation to engineers, researchers, security people

## Design Philosophy

Follow the book at `~/repos-eidos-agi/books/railway-websites/` — specifically:

- **Chapter 4** (Design System from History): Swiss precision + warmth. Not a SaaS landing page. A well-organized workshop.
- **The Pratfall Effect**: Earn the right to be weird. Lighthouse 95 first, personality second.
- **Anti-commodity**: No gradient blobs, no AI illustrations, no "Trusted by" logo bars, no three-column feature grids. Look like a human made it.

### Eidos AGI's aesthetic direction (from VISION.md):
> "Our websites should look like what they are — tools made by people who care about craft. A well-organized workshop, not a showroom."

Emotional register: **confident and unhurried**. We ship real software. We don't need to prove it with flashy animations. The repos speak for themselves.

### Editorial Rules
Write real sentences, not keynote fragments. AI-generated copy has recognizable tells that undermine credibility on a site about AI architecture:

- **No staccato negation chains**: "No software. No database. No code." → join into one sentence
- **No parallel triplets**: "Research earns. Visionlog records. Ike executes." → write prose
- **No rhetorical laddering**: three short sentences building to a punchline
- **No "Not X — Y" profundity**: "Not a chatbot. A participant." → say what it IS
- **One em dash per page max** as a dramatic pause
- **Earn every sentence** — if removing it changes nothing, remove it

The full editorial process is in `.claude/skills/copy-audit/skill.md`. Run `/copy-audit` before any deploy that touches text.

## Tech Stack

- **Astro** — content-first, partial hydration, native performance
- **Railway** — deployment, custom domain (eidosagi.com already on Cloudflare)
- **No React/Vue/Svelte** — static HTML + minimal JS. The site is content, not an app.

## Pages

### 1. Landing page (`/`)
- Hero: tagline + one-paragraph mission
- The Trilogy: visionlog, research.md, ike.md — with `pip install` commands
- MCP Servers: railguey, clawdflare, eidos-mcp-registry
- Agent Tools: resume-resume, apple-a-day
- Join Us: open invitation + email

### 2. About (`/about`) — optional, could be on landing page
- Stealth group identity
- Why we exist
- What "agentic-first" means

## Copy

### Tagline
**Software for agents. Governance for reality.**

### Mission paragraph
We're a stealth group of engineers, AI researchers, and cybersecurity experts. Some of us have day jobs. We work under this banner because it gives us the freedom to build what industry won't.

Our toolkit helps you get more out of existing AI — governance, decisions, execution, and shipping standards that make agents reliable enough to trust with real work. We're not building new models or wrappers; we're building the infrastructure that turns today's AI into tomorrow's workforce.

### Join Us copy
We're looking for engineers, researchers, and security people who want to build the infrastructure layer for agentic software. You don't need to quit your job. You don't need permission. If you see the gap between where AI is and where it could be with proper tooling — and you want to close it — reach out.

### Urgency line (use somewhere prominent)
Agents are getting deployed into real systems right now — if you don't give them governed tools, explicit decisions, and agent-grade interfaces, you're shipping a probabilistic coworker with production access.

## References

- Book: `~/repos-eidos-agi/books/railway-websites/` — full design philosophy + code patterns
- GitHub profile: `~/repos-eidos-agi/.github/profile/README.md` — current copy (keep in sync)
- Domain: `eidosagi.com` on Cloudflare (account ID in cockpit-eidos memory)
- Email: `daniel@eidosagi.com` (Migadu SMTP)

## Deployment

- Railway service (create new)
- Dockerfile or nixpacks for Astro
- Custom domain: eidosagi.com (CNAME to Railway)
- SSL: automatic via Railway

## Brand & Messaging Unification

The website, GitHub profile, and all forge templates should use consistent copy. When the website copy changes, update:
1. `.github/profile/README.md`
2. foss-forge templates (CONTRIBUTING.md.tmpl references)
3. Any forge README that mentions Eidos AGI

Future: a brand-forge skill that propagates copy changes across all repos.
