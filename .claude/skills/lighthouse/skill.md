# /lighthouse — Lighthouse Performance Audit

## When to Use
After any visual or structural change. Before every deploy. This is the gate.

## Philosophy
From the book: "Lighthouse 95 is the price of admission for using a ransom-note font. A perfect Core Web Vitals score is the prerequisite for the layout experiment that breaks every grid convention. You earn the right to be weird by being provably good first."

## Execution Steps

### 1. Build + Preview
```bash
npm run build && npm run preview &
```
Wait for the preview server to be ready on port 4321.

### 2. Run Lighthouse CLI
If `lighthouse` CLI is available:
```bash
npx lighthouse http://localhost:4321 \
  --output=json --output=html \
  --output-path=./lighthouse-report \
  --chrome-flags="--headless --no-sandbox" \
  --preset=desktop
```

If not available, instruct the user to run Lighthouse from Chrome DevTools (incognito, simulated Slow 4G throttling).

### 3. Parse Results
Extract and display the four scores:

```
  LIGHTHOUSE  Performance  Accessibility  Best Practices  SEO
              <score>      <score>        <score>         <score>
```

### 4. Diagnose Failures
For each score below target:

**Performance < 95:**
- Check LCP element — is `fetchpriority="high"` on the hero image?
- Check font loading — is `font-display: optional` set?
- Check for synchronous JS on the main thread
- Check image optimization — are images AVIF with explicit dimensions?
- Check CLS — any missing width/height on images?

**Accessibility < 100:**
- Color contrast ratios (WCAG 4.5:1 for normal text)
- Missing alt text
- Focus management on interactive elements
- Missing `<meta name="description">`

**Best Practices < 100:**
- Console errors
- Mixed content
- Missing security headers

**SEO < 100:**
- Missing meta description
- Missing canonical URL
- Missing Open Graph tags

### 5. Report with Action Items
For each failing metric, output the specific fix needed with file path and line number.

## Targets
| Metric | Target | Hard Floor |
|--------|--------|------------|
| Performance | 97 | 95 |
| Accessibility | 100 | 100 |
| Best Practices | 100 | 95 |
| SEO | 100 | 100 |

## Rules
- The Performance hard floor of 95 is NON-NEGOTIABLE for deploy.
- Accessibility 100 is expected, not aspirational.
- Always test on the production build, never the dev server.
- Kill the preview server when done.
