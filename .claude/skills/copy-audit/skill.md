# /copy-audit — Voice & Copy Consistency Check

## When to Use
After writing or modifying any text content on the site. Before deploy. The copy IS the product for a landing page.

## Voice Definition
From CLAUDE.md: **Confident and unhurried.** We ship real software. We don't need to prove it with flashy animations. The repos speak for themselves.

### What the Voice Sounds Like
- Declarative, not persuasive. State facts, don't sell.
- Short sentences. No filler. No "leverage synergies."
- Technical fluency — we can say "MCP server" without explaining it.
- Invitational, not exclusive — "You don't need to quit your job."
- Specific, not vague — "9 packages on PyPI" not "a growing collection of tools."

### What the Voice Does NOT Sound Like
- Marketing-speak: "Revolutionize your workflow with AI-powered solutions"
- Startup hype: "We're building the future of X"
- Corporate: "Our mission is to deliver world-class enterprise solutions"
- Apologetic: "We're just a small team trying to..."
- Over-explaining: paragraphs where a sentence would do

## Canonical Copy (from CLAUDE.md)

### Tagline
**Software for agents. Governance for reality.**

### Mission
We're a stealth group of engineers, AI researchers, and cybersecurity experts. Some of us have day jobs. We work under this banner because it gives us the freedom to build what industry won't.

Our toolkit empowers you to leverage existing AI to go further than it otherwise could — governance, decisions, execution, and shipping standards that make agents reliable enough to trust with real work. Not new models. Not wrappers. The infrastructure that turns today's AI into tomorrow's workforce.

### Urgency Line
Agents are getting deployed into real systems right now — if you don't give them governed tools, explicit decisions, and agent-grade interfaces, you're shipping a probabilistic coworker with production access.

### Join Us
We're looking for engineers, researchers, and security people who want to build the infrastructure layer for agentic software. You don't need to quit your job. You don't need permission. If you see the gap between where AI is and where it could be with proper tooling — and you want to close it — reach out.

## Execution Steps

### 1. Extract All Text Content
Read every `.astro` page and extract all visible text — headings, paragraphs, button labels, alt text, meta descriptions.

### 2. Check Against Canonical Copy
For sections that have canonical copy defined above, verify exact match or intentional deviation.

### 3. Voice Check
For all text, flag:
- **Jargon soup** — buzzwords stacked without meaning
- **Passive voice** — "solutions are delivered" instead of "we ship X"
- **Vague claims** — "powerful," "innovative," "cutting-edge" (say what it DOES)
- **Filler phrases** — "In order to," "It's important to note that," "At the end of the day"
- **Over-length** — any paragraph > 4 sentences (on a landing page, 2-3 is ideal)
- **Missing specifics** — if we can replace a claim with a number, we should

### 4. Package Descriptions Check
Verify each package listed has:
- A one-line description that says what it DOES (not what it IS)
- A `pip install` command
- A link to the repo

### 5. Report
```
  COPY AUDIT    <N> sections checked | <N> issues

  ISSUES:
  - Hero subtitle: passive voice — "solutions are delivered" → "we ship X"
  - About section: 6 sentences — trim to 3
  - Missing: meta description for homepage
```

## Rules
- Canonical copy from CLAUDE.md is the source of truth for core sections.
- The tagline is exact. Do not rephrase it.
- Numbers beat adjectives. "9 PyPI packages" > "many tools."
- Every package gets a `pip install` command visible on the page.
- Meta description must exist on every page and match the voice.
