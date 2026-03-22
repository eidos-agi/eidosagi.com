# /design-check — Anti-Commodity Design Validator

## When to Use
After building or modifying any visual component. This is the aesthetic gate — the complement to /lighthouse's performance gate.

## Philosophy
From the book (Ch1): "The opposite of AI slop is not necessarily minimalism or maximalism, retro or forward-looking. It is intention made visible. Human effort, legible on the surface."

From CLAUDE.md: "No gradient blobs, no AI illustrations, no 'Trusted by' logo bars, no three-column feature grids. Look like a human made it."

## The Anti-Commodity Checklist

### HARD FAILURES (any one of these = redesign)
Scan all `.astro`, `.css`, and `.html` files for:

- [ ] **Gradient blobs** — `background: linear-gradient` or `radial-gradient` used decoratively (functional gradients for depth are OK)
- [ ] **AI illustrations** — any `<img>` referencing stock AI art, Midjourney, DALL-E output
- [ ] **"Trusted by" logo bars** — any section with a row of company logos
- [ ] **Three-column feature grids** — icon + heading + 2-sentence pattern repeated 3x
- [ ] **Inter font** — `font-family` containing 'Inter' (the universal AI default)
- [ ] **Generic hero pattern** — gradient bg + centered text + two buttons (filled + ghost)
- [ ] **Border-radius: 8px** everywhere — the SaaS default radius
- [ ] **Box-shadow soup** — heavy shadows on cards (`box-shadow` with spread > 10px)
- [ ] **Stock testimonial cards** — avatar + name + role + quote in a card grid

### SOFT WARNINGS (flag but don't block)
- [ ] **More than 2 font weights of same family** — Swiss rule: 2 max
- [ ] **Line length > 75ch** — disrespects reading comfort
- [ ] **Missing grain/texture** — the site should have surface, not flatness
- [ ] **Cold colors without warmth** — pure greys (#333, #666, #999) instead of warm tones
- [ ] **Symmetrical button pairs** — one filled, one ghost, side by side (the SaaS tell)
- [ ] **Generic section spacing** — uniform padding everywhere instead of rhythmic variation

### POSITIVE SIGNALS (things we WANT to see)
- [ ] **Token-driven values** — CSS custom properties, not magic numbers
- [ ] **Typographic hierarchy** — clear distinction between heading levels
- [ ] **Intentional whitespace** — generous but purposeful
- [ ] **Dark mode as same vocabulary** — not just color inversion
- [ ] **Texture/grain** — SVG noise or CSS-based, not raster images
- [ ] **68ch max measure on prose** — the reading comfort constraint
- [ ] **Variable fonts or self-hosted subsets** — not CDN-loaded full families

## Execution Steps

### 1. Scan All Source Files
Read every `.astro`, `.css`, and inline `<style>` block.

### 2. Run Each Checklist Item
For hard failures: grep for the specific patterns.
For soft warnings: analyze the CSS values and HTML structure.
For positive signals: check for their presence.

### 3. Report
```
  DESIGN CHECK    <N> hard failures | <N> warnings | <N>/<total> positive signals

  HARD FAILURES:
  ✗ Three-column feature grid found in src/pages/index.astro:45

  WARNINGS:
  △ Line length unconstrained in .prose — add max-width: 68ch

  POSITIVE:
  ✓ Token-driven spacing
  ✓ SVG grain texture
  ✗ Missing dark mode
```

## Rules
- Hard failures MUST be fixed before deploy.
- This check runs automatically as part of /deploy.
- The aesthetic is "confident and unhurried" — not flashy, not minimal, not generic.
- When in doubt, reference the book at `~/repos-eidos-agi/books/railway-websites/`.
