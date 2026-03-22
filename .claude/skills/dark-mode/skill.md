# /dark-mode — Dark Mode Validation

## When to Use
After building or modifying any visual component. Dark mode is the DEFAULT for eidosagi.com (we're a tools org with a dark cockpit theme). Light mode is the polite accommodation.

## Philosophy
From the book (Ch4): "Dark mode is not a feature bolted on at the end. It's the same design vocabulary, adjusted for a different light condition. Every value should feel like it belongs to the same family as its light-mode counterpart."

## Eidos AGI Dark/Light Strategy

**Default: Dark** (matches cockpit-eidos theme)
```
--color-bg:      #0a0a0f   /* near-black with blue-violet warmth */
--color-surface: #12121a   /* raised surfaces */
--color-text:    #c8c8d4   /* warm light grey, not cold white */
--color-muted:   #606078   /* secondary text with violet tint */
--color-primary: #6c8aff   /* the eidos blue-violet */
```

**Override: Light** (`prefers-color-scheme: light`)
- Background should be warm off-white, not pure white
- Text should be warm near-black, not pure black (#000)
- Primary accent should darken slightly to maintain contrast
- Muted should lighten to maintain the same relative contrast ratio
- The mood should feel like the same workshop with the lights on

## Validation Checklist

### Color Contrast (WCAG AA — 4.5:1 minimum)
Check every text-on-background combination in BOTH modes:
- [ ] `--color-text` on `--color-bg` (dark mode body text)
- [ ] `--color-muted` on `--color-bg` (dark mode secondary text)
- [ ] `--color-primary` on `--color-bg` (dark mode links/accents)
- [ ] `--color-text` on `--color-surface` (dark mode cards/panels)
- [ ] All of the above in light mode overrides

### Semantic Consistency
- [ ] Same CSS custom properties used in both modes (just different values)
- [ ] No `color: #fff` or `background: #000` hardcoded anywhere
- [ ] All color references go through tokens, never raw hex
- [ ] Interactive elements (links, buttons) use the same `--color-primary` in both modes

### Visual Coherence
- [ ] Grain/texture overlay works in both modes (may need opacity adjustment)
- [ ] Borders use `--color-muted` or equivalent, visible in both modes
- [ ] Images don't blow out in either mode (check if blend modes are needed)
- [ ] Code blocks/`<pre>` elements have appropriate surface contrast in both modes

### Transition
- [ ] No flash of wrong theme on page load (dark is default, light is `@media` override)
- [ ] Smooth transition if toggled (optional — media query respects OS setting)

## Execution Steps

### 1. Audit Token File
Read `tokens.css` or equivalent. Verify dark mode values exist and light mode is `@media (prefers-color-scheme: light)`.

### 2. Check Contrast Ratios
For each text-on-background pair, calculate the contrast ratio. Flag any below 4.5:1.

### 3. Grep for Hardcoded Colors
```
grep -rn '#[0-9a-fA-F]\{3,8\}' src/ --include="*.astro" --include="*.css" | grep -v tokens
```
Every result outside the token file is a potential dark mode bug.

### 4. Visual Spot Check
Suggest the user toggle `prefers-color-scheme` in DevTools:
1. DevTools → Rendering → Emulate CSS media `prefers-color-scheme: light`
2. Check every section of the page
3. Toggle back to dark

### 5. Report
```
  DARK MODE     <N> contrasts checked | <N> pass | <N> fail
                <N> hardcoded colors found

  FAILURES:
  - --color-muted on --color-bg: ratio 3.2:1 (need 4.5:1) — darken muted or lighten bg
  - src/pages/index.astro:34: hardcoded #e5e5e5 — replace with var(--color-text)

  LIGHT MODE:
  - Override exists: yes/no
  - All tokens overridden: yes/no
  - Contrast passes: yes/no
```

## Rules
- Dark mode is DEFAULT. It is not an afterthought.
- No cold whites (#ffffff) or cold blacks (#000000). Everything has warmth.
- Same design vocabulary, different values. Not a different design.
- Contrast ratios are non-negotiable. WCAG AA minimum (4.5:1).
- If the site looks good in dark but broken in light, the tokens are wrong — fix the light overrides.
