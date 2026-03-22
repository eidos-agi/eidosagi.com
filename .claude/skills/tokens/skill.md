# /tokens — Design Token System Management

## When to Use
When building or modifying the design system. When adding new colors, type sizes, or spacing values. When you need to audit that no magic numbers have crept in.

## Philosophy
From the book (Ch4): "A constraint is not a limitation. It is a decision made once, so you don't have to make it again."

The token file is the single source of truth. Nothing in the codebase should contain a color value, spacing value, or font size that isn't defined here or derived from here.

## Eidos AGI Token Palette

The aesthetic for eidosagi.com is NOT Greyfield (letterpress warmth). It is:
- **Emotional register**: Confident and unhurried. We ship real software. Workshop, not showroom.
- **Visual language**: Swiss precision as structure, but with warmth. Dark-first (like the cockpit theme).
- **Cockpit theme reference** (from state.json): primary `#6c8aff`, danger `#ef4444`, warning `#f59e0b`, bg `#0a0a0f`, surface `#12121a`, text `#c8c8d4`, muted `#606078`

### Adapting the Book's System

The book's token architecture applies directly — change the values, keep the system:

| Book Token | Eidos Equivalent | Why |
|------------|-----------------|-----|
| `--color-paper` | `--color-bg` | Dark background, not warm paper |
| `--color-ink` | `--color-text` | Light text on dark |
| `--color-sage` | `--color-primary` | The eidos blue-violet `#6c8aff` |
| `--color-terracotta` | `--color-accent` | A warm accent that contrasts the cool primary |
| `--font-heading` | Condensed grotesque | Same Swiss principle — Barlow Condensed or similar |
| `--font-body` | Monospace or clean sans | Code-forward identity — we're a tools org |

### Token Categories (from Ch4)
1. **Color** — light mode + dark mode (dark is default for Eidos)
2. **Type Scale** — Major Third (1.25), 16px base
3. **Spacing** — 8-point grid
4. **Typography** — 2 families max, 2 weights per family max
5. **Borders & Radius** — hairline borders, subtle rounding (2-4px max)
6. **Z-Index** — named scale, not raw integers

## Execution Steps

### 1. Check for Token File
Look for `src/styles/tokens.css` or equivalent. If missing, generate one.

### 2. Audit for Magic Numbers
Grep all `.astro` and `.css` files for:
- Raw color hex values not in tokens (`#[0-9a-f]{3,8}` outside tokens.css)
- Raw pixel values for spacing (`padding: 24px` instead of `var(--space-6)`)
- Raw font sizes (`font-size: 16px` instead of `var(--text-base)`)
- Raw font families (inline `font-family` instead of `var(--font-heading)`)

### 3. Report Token Health
```
  TOKENS    <N> defined | <N> in use | <N> magic numbers found

  VIOLATIONS:
  - src/pages/index.astro:23 — raw color #333 (use var(--color-muted))
  - src/pages/index.astro:45 — raw spacing 32px (use var(--space-8))
```

### 4. Generate Missing Tokens
If the token file doesn't exist, generate `src/styles/tokens.css` following the book's architecture with Eidos AGI's palette.

## Rules
- Every value in the codebase traces back to a token. No exceptions.
- 8-point spacing grid. No arbitrary values.
- Major Third type scale (1.25 ratio). No viewport-relative font sizes for editorial content.
- 2 font families max. 2 weights per family max. (Swiss rule)
- Subtle border radius only (2-4px). No heavy rounding (16px+).
- Dark mode is default. Light mode is the override.
