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

## HUMAN DIMENSIONS (6 axes, 0–10 each, max 60)

These measure what the engineering dimensions can't: whether a human actually wants to stay, trust, and act.

### 9. TRUST (0–10)
After reading the whole page, do you trust this org to build reliable software?
- 0: Feels fake, anonymous, or like a weekend project claiming enterprise.
- 5: Competent but impersonal. Could be real, could be vaporware.
- 10: You'd bet your production stack on these people. The evidence is in the work.

**Check**: Does the page show real work (repos, code examples, install commands) or just claims? Is there a human behind it (names, contact, GitHub activity)? Does the copy overpromise? Is the design quality itself evidence of care?

### 10. MEMORABILITY (0–10)
Close the tab. What do you remember? Could you describe this site to someone?
- 0: Nothing sticks. "It was some dark site with tools."
- 5: You remember the tagline but not why it matters.
- 10: You remember the analogy, the visual, the feeling. You'd recognize it if you saw it again.

**Check**: Is there a single image, phrase, or concept that anchors the whole site? Does the design have a signature — something no other site has? Would you remember the warm brown or just "dark mode"?

### 11. EMOTIONAL ARC (0–10)
Does the page have a narrative flow, or is it just sections stacked?
- 0: List of features. No story. No build. No payoff.
- 5: Logical structure but no emotional momentum. Informative, not compelling.
- 10: The page builds — hook, context, proof, urgency, action. You feel pulled forward.

**Check**: Map the page top-to-bottom. Does each section earn the next? Is there a turning point (the urgency quote, the "we don't build LLMs" punchline)? Does the ending resolve or just stop?

### 12. DIFFERENTIATION (0–10)
Could you tell this site apart from 10 other dev tools sites in a lineup?
- 0: Interchangeable. Dark mode, sans-serif, three-column features.
- 5: Has a color palette but no identity. Swap the logo and it could be anyone.
- 10: Unmistakably this org. The palette, the typography, the voice, the flow diagram — it's a fingerprint.

**Check**: Remove the logo and brand name. Can you still identify the site? What specific elements are unique (warm brown palette, brass accents, animated flow diagram, workshop metaphor)?

### 13. DELIGHT (0–10)
Is there anything that surprises or pleases you? A moment of "oh, nice."
- 0: Functional. No surprise. No personality.
- 5: One nice touch (maybe the grain texture or a hover state).
- 10: Multiple moments of delight — the theme switcher, the animated arrows, the copy-to-clipboard, the urgency quote's bite. Rewards attention.

**Check**: Count the "oh, nice" moments. Are they in the design, the copy, the interaction, or the content? Does the page reward scrolling or just endure it?

### 14. URGENCY (0–10)
After reading, do you want to try the tools NOW or "maybe later"?
- 0: Interesting in theory. No reason to act today.
- 5: I'd bookmark it. Might come back.
- 10: I'm running `pip install` before I close the tab. The stakes are clear and the barrier is zero.

**Check**: Is the problem stated in terms that create urgency ("probabilistic coworker with production access")? Is the install command visible and copyable within 10 seconds? Is there a reason to act now vs. later?

## Composite Score

**Engineering: 8 axes × 10 = max 80**
**Human: 6 axes × 10 = max 60**
**Total: 14 axes × 10 = max 140**

| Rating | Score | Meaning |
|--------|-------|---------|
| **Legendary** | 120–140 | The site IS the product. Ship and amplify. |
| **Badass** | 100–119 | Strong on both sides. Ready for real traffic. |
| **Solid** | 80–99 | Engineering done, human side needs work (or vice versa). |
| **Mid** | 60–79 | Technically works, emotionally flat. |
| **Blah** | 40–59 | Generic. Forgettable. |
| **Broken** | 0–39 | Doesn't function or communicate. |

## Output Format

```
SCORE   <total>/140 — <rating>

  ── ENGINEERING ──
  CRAFT          ██████░░░░  6/10
  PERFORMANCE    ██████████  10/10
  COPY           ████████░░  8/10
  DX             ██████░░░░  6/10
  VISUAL         ████░░░░░░  4/10
  MARKETING      ██████░░░░  6/10
  MOBILE         ████████░░  8/10
  ACCESSIBILITY  ████████░░  8/10
                              56/80

  ── HUMAN ──
  TRUST          ██████░░░░  6/10
  MEMORABILITY   ████░░░░░░  4/10
  EMOTIONAL ARC  █████░░░░░  5/10
  DIFFERENTIATION████████░░  8/10
  DELIGHT        █████░░░░░  5/10
  URGENCY        ██████░░░░  6/10
                              34/60

  TOP 3 FIXES (highest impact):
  1. ...
  2. ...
  3. ...
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
