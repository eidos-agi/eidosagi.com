# /craft-check — The Comprehensive "Does This Look Human-Made?" Audit

## When to Use
Before final deploy. This is the master audit that combines design, performance, typography, motion, copy, and dark mode into a single pass. The ultimate gate.

## Philosophy
From the book (Ch1): "Every element reflects a decision made by a person. The opposite of AI slop is not necessarily minimalism or maximalism, retro or forward-looking. It is intention made visible."

From Ch9: "The beautiful website is not built despite the budget. It is built because of it."

The Pratfall Effect: "You earn the right to be weird by being provably good first." Lighthouse 95+ is the price of admission. Then the craft signals trust.

## The Five Pillars

### Pillar 1: Performance (from /lighthouse + /perf-pass)
- [ ] Lighthouse Performance ≥ 95
- [ ] Lighthouse Accessibility = 100
- [ ] Lighthouse Best Practices ≥ 95
- [ ] Lighthouse SEO = 100
- [ ] Total bundle < 100KB
- [ ] JS payload < 5KB (ideally zero)
- [ ] LCP < 1.5s
- [ ] CLS = 0.00

### Pillar 2: Design System (from /tokens + /design-check)
- [ ] Token file exists with all categories (color, type, spacing, borders, z-index)
- [ ] Zero magic numbers in source files
- [ ] Zero anti-commodity violations (no gradient blobs, no AI art, no three-col features)
- [ ] 8-point spacing grid enforced
- [ ] 2 font families max, 2 weights each
- [ ] Border radius ≤ 4px (no SaaS bubbles)
- [ ] Grain/texture via CSS/SVG (not raster)

### Pillar 3: Typography (from book Ch4-5)
- [ ] Heading hierarchy: clear, condensed grotesque, tight leading
- [ ] Body text: warm serif or monospace, relaxed leading (1.7)
- [ ] Measure constrained: max-width 68ch on prose
- [ ] `text-wrap: balance` on headings
- [ ] `text-wrap: pretty` on body paragraphs
- [ ] Fluid type via `clamp()` on h1/h2
- [ ] Variable fonts or subsetted self-hosted
- [ ] `font-display: optional` on all @font-face

### Pillar 4: Dark Mode (from /dark-mode)
- [ ] Dark mode is default
- [ ] All colors via tokens
- [ ] Light mode override exists
- [ ] Contrast ≥ 4.5:1 in both modes
- [ ] No hardcoded colors outside tokens
- [ ] Warm palette (no cold #fff or #000)

### Pillar 5: Copy (from /copy-audit)
- [ ] Tagline matches canonical: "Software for agents. Governance for reality."
- [ ] Voice is confident and unhurried
- [ ] No marketing jargon
- [ ] All packages listed with `pip install` commands
- [ ] Meta description on every page
- [ ] Numbers used instead of adjectives where possible

## Motion Rules (from book Ch5)
Every animation must answer one of three questions:
1. Does it help the user understand where they are? (orientation)
2. Does it confirm an action? (feedback)
3. Does it reveal content naturally? (comfort)

If it can't answer one of those three, it doesn't ship.

Additional motion checks:
- [ ] `prefers-reduced-motion: reduce` honored — all animations collapse to instant
- [ ] No parallax scrolling effects
- [ ] No bounce-on-hover
- [ ] No staggered entrance animations that delay content
- [ ] Page transitions via View Transitions API (if multi-page)
- [ ] Animation durations: entry ≠ exit (asymmetric is natural)

## Execution Steps

### 1. Run Sub-Audits
Invoke each sub-skill mentally and collect results:
- /tokens → token health
- /design-check → anti-commodity compliance
- /dark-mode → theme validation
- /copy-audit → voice consistency
- /perf-pass → performance metrics

### 2. Score Each Pillar
```
  CRAFT CHECK — eidosagi.com

  PERFORMANCE    ████████░░  8/10   Lighthouse 96, CLS 0.02
  DESIGN         ██████████  10/10  Zero violations
  TYPOGRAPHY     ████████░░  8/10   Missing text-wrap: pretty
  DARK MODE      ██████████  10/10  All contrasts pass
  COPY           █████████░  9/10   Meta description missing on /about

  OVERALL        45/50 — SHIP IT (with 2 minor fixes)
```

### 3. Verdict
- **50/50**: Perfect craft. Ship immediately.
- **45-49**: Ship with noted fixes queued.
- **40-44**: Fix before shipping. Close but not there.
- **< 40**: Not ready. Major issues need addressing.

### 4. The Human Test
Ask one final question that no checklist can answer:

> "If a skilled web developer visited this site for the first time, would they think a person made this — or would they think a template made this?"

If the answer is "template," something is wrong that the checklist didn't catch. The site needs a decision that only a human can make — a layout choice, a color shift, a typographic quirk, something that says "someone was here."

## Rules
- This is the FINAL gate before production deploy.
- All five pillars must score ≥ 8/10 to ship.
- Performance pillar is non-negotiable at ≥ 8/10 (Lighthouse 95+).
- The Human Test is not a joke. Take it seriously.
- Reference the book at `~/repos-eidos-agi/books/railway-websites/` for any decision.
