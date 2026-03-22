# /score — Website Loss Function

## When to Use
After any change. This is the composite "is it badass?" metric. Run it to know where you stand and what to fix next.

## The Scoring Dimensions (8 axes, 0–10 each, max 80)

### 1. CRAFT (0–10)
Does it look human-made? Would a skilled designer think a person designed this?
- 0: Template. Gradient blobs, Inter font, three-column features.
- 5: Clean but generic. Could be any startup.
- 10: Unmistakably intentional. Every element reflects a decision. You can feel the hand.

**Check**: Anti-commodity violations (gradient blobs, stock art, logo bars, generic hero pattern). Token discipline (no magic numbers). Typography hierarchy. Grain/texture. Border radius discipline (≤4px). Historical era reference visible.

### 2. PERFORMANCE (0–10)
Is it provably fast?
- 0: Lighthouse < 70. JS-heavy. Slow on mobile.
- 5: Lighthouse 90. Acceptable but not impressive.
- 10: Lighthouse 97+. Zero JS. < 50KB total. LCP < 1s.

**Check**: Run `npm run build`, measure output size. Check for JS files. Check font loading strategy. Image optimization. CLS.

### 3. COPY (0–10)
Does the voice earn trust?
- 0: Marketing jargon. "Leverage synergies." Passive voice. Vague claims.
- 5: Clear but bland. Says what it does but not memorably.
- 10: Every sentence earns its place. Numbers beat adjectives. Specific, declarative, unhurried.

**Check**: Passive voice scan. Jargon detection. Paragraph length (≤3 sentences on landing). Specificity (numbers present). Voice match to "confident and unhurried." No sales pitch.

### 4. DX — Developer Experience (0–10)
Can a developer go from landing to installing in under 30 seconds?
- 0: No install commands visible. Links to docs that link to more docs.
- 5: Install commands present but buried. Need to scroll.
- 10: `pip install X` visible within the first interaction for every tool. One click to repo. Examples on the page.

**Check**: Every package has visible `pip install` command. Every package links to its GitHub repo. Tool pages (when they exist) have real examples, not just descriptions. README-level content on the site.

### 5. VISUAL RICHNESS (0–10)
Is there more than text?
- 0: Wall of text. No diagrams, no images, no visual hierarchy beyond headings.
- 5: Some visual elements but decorative, not informative.
- 10: Diagrams that explain. Charts that prove. Visual hierarchy that guides. Every visual earns its place.

**Check**: Count of meaningful SVGs/diagrams/charts. Are visuals informative (explain a concept) or decorative (just pretty)? Does the page work if you remove all text? Does it work if you remove all visuals?

### 6. MARKETING (0–10)
Would this convert a visitor into a user?
- 0: No clear value proposition. No CTA. Visitor doesn't know what to do.
- 5: Clear what it is but no urgency or differentiation.
- 10: Value prop in 5 seconds. Clear differentiator. Obvious next action. Social proof (GitHub stars, PyPI downloads). SEO-complete (meta desc, OG tags, canonical URL).

**Check**: Can you explain what this org does in one sentence from the hero? Is there a clear CTA above the fold? Meta description exists on every page. OG tags present. Canonical URL set. Is there any social proof (stars, downloads, users)?

### 7. MOBILE (0–10)
Does it work on a phone?
- 0: Broken layout. Horizontal scroll. Unreadable text.
- 5: Responsive but cramped. Desktop layout squeezed.
- 10: Feels designed for mobile first. Touch targets correct. Reading comfortable. No horizontal scroll.

**Check**: Viewport meta tag. Media queries present for ≤768px. Grid collapses gracefully. Text readable without zoom. Touch targets ≥ 44px. No horizontal overflow.

### 8. ACCESSIBILITY (0–10)
Can everyone use it?
- 0: No alt text. No focus management. Color contrast fails.
- 5: Lighthouse accessibility 90+. Basic compliance.
- 10: Lighthouse accessibility 100. WCAG AA on all text. Keyboard navigable. Screen reader tested. prefers-reduced-motion honored. prefers-color-scheme honored.

**Check**: Contrast ratios on all text-on-background pairs (4.5:1 min). Alt text on all images. Focus visible on all interactive elements. Reduced motion media query present. Color scheme media query present. Semantic HTML (nav, main, section, article, footer).

## Composite Score

| Rating | Score | Meaning |
|--------|-------|---------|
| **Legendary** | 72–80 | Ship it. Tell everyone. |
| **Badass** | 60–71 | Ship it. Fix the gaps at leisure. |
| **Solid** | 48–59 | Almost there. 1–2 dimensions dragging. |
| **Mid** | 36–47 | Works but doesn't impress. Needs focused work. |
| **Blah** | 24–35 | Generic. Could be any site. |
| **Broken** | 0–23 | Doesn't function or communicate. |

## Output Format

```
SCORE   <total>/80 — <rating>

  CRAFT          ██████░░░░  6/10   Token-driven, but layout is standard
  PERFORMANCE    ██████████  10/10  0 JS, 28KB, Lighthouse 98
  COPY           ████████░░  8/10   Voice is right, urgency line lands
  DX             ██████░░░░  6/10   pip install visible, no examples yet
  VISUAL         ████░░░░░░  4/10   Flow diagram works, rest is text
  MARKETING      ██████░░░░  6/10   Value prop clear, no social proof
  MOBILE         ████████░░  8/10   Responsive, touch targets OK
  ACCESSIBILITY  ████████░░  8/10   Contrast passes, no focus audit yet

  TOP 3 FIXES (highest impact):
  1. Add real examples to tool pages (DX +3, VISUAL +2)
  2. Add GitHub star counts (MARKETING +2)
  3. Audit keyboard navigation (ACCESSIBILITY +2)
```

## Execution Steps

1. Read all source files
2. Run `npm run build` and measure output
3. Score each dimension with evidence
4. Compute composite
5. Identify top 3 fixes by impact across multiple dimensions
6. Report

## Rules
- Be honest. A 5 is a 5.
- Evidence over vibes. Each score needs a specific reason.
- "Highest impact" fixes are ones that move multiple dimensions at once.
- Run this after every major change.
- The goal is 72+. Don't ship below 60.
