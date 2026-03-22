# /perf-pass — The Performance Pass

## When to Use
After the site is feature-complete, before final deploy. This is the push from "good" to "exceptional." Run this when the site works but hasn't been optimized.

## Philosophy
From the book (Ch12): "The difference between a Lighthouse 90 and a Lighthouse 97 is the difference between a site that passes and a site that earns its price point."

From Ch1: "You earn the right to be weird by being provably good first."

## The Audit Sequence (ROI order)

### 1. LCP — Largest Contentful Paint (target: < 1.5s)
The single metric that moves the needle most. 200-300ms improvement = ~5 Lighthouse points.

**Check:**
- What is the LCP element? (hero image, heading text, background?)
- If image: does it have `fetchpriority="high"` and `loading="eager"`?
- If image: is there a `<link rel="preload" as="image">` in `<head>`?
- Is the image AVIF format? (not JPEG, not PNG)
- Does the image have explicit `width` and `height`?

**For eidosagi.com specifically:**
- The LCP element is likely the hero heading or background
- No heavy photography expected (tools org, not e-commerce)
- Custom fonts are the main LCP risk

### 2. INP — Interaction to Next Paint (target: < 100ms)
Matters less for a landing page (minimal interactivity), but check anyway.

**Check:**
- Any click handlers doing synchronous DOM updates?
- Any `fetch()` calls in event handlers blocking render?
- Third-party scripts (analytics, chat widgets) loading synchronously?

### 3. CLS — Cumulative Layout Shift (target: < 0.01)
**Check:**
- All `<img>` elements have explicit `width` and `height`
- `font-display: optional` on all `@font-face` declarations
- No dynamically injected content above the fold
- Font `size-adjust` on fallback if swap is visible

### 4. Bundle Analysis
**Check:**
- `npm run build` — what's the total output size?
- Any JS in the output? (Should be near-zero for a static landing page)
- CSS total size
- Font files: are they subsetted? Self-hosted?

### 5. Network Waterfall
**Check:**
- How many requests on first load?
- Any third-party domains? (Each costs a DNS lookup)
- Are fonts preloaded?
- Is anything render-blocking?

### 6. Image Optimization
**Check:**
- All images in AVIF or WebP format
- `sizes` attribute on responsive images
- `loading="lazy"` on below-fold images
- No raster textures (use CSS/SVG instead — Ch4 rule)

## Execution Steps

### 1. Build
```bash
npm run build
```
Report output size.

### 2. Audit Build Output
```bash
ls -la dist/
du -sh dist/
find dist -name "*.js" -exec ls -la {} \;
find dist -name "*.css" -exec ls -la {} \;
```

### 3. Check HTML Output
Read the built HTML and verify:
- `fetchpriority="high"` on LCP element
- `font-display: optional` in CSS
- Explicit image dimensions
- `<link rel="preload">` for critical fonts
- No render-blocking scripts

### 4. Run Lighthouse
Via CLI or instruct user to run in DevTools.

### 5. Report
```
  PERF PASS    LCP <time> | INP <time> | CLS <score>
               Bundle <size> | Requests <count> | JS <size>

  FIXES APPLIED:
  - Added fetchpriority="high" to hero
  - Subsetted fonts: 120KB → 28KB
  - Removed render-blocking script

  REMAINING:
  - Font swap still visible on first load (acceptable with font-display: optional)
```

## Targets for eidosagi.com
| Metric | Target | Notes |
|--------|--------|-------|
| Performance | 97+ | Static site, should be achievable |
| Total bundle | < 100KB | No JS framework, minimal CSS |
| JS payload | < 5KB | Near-zero — this is a static page |
| LCP | < 1.0s | Text-based hero should be instant |
| CLS | 0.00 | No dynamic content, no excuse |
| Requests | < 10 | HTML + CSS + fonts + maybe 1-2 images |

## Rules
- Run on production build, never dev server.
- Fix in ROI order: LCP first, then CLS, then everything else.
- No raster texture images. SVG/CSS only.
- Self-host fonts. No Google Fonts CDN in production.
- Zero JS is the ideal. Every byte of JS must justify itself.
