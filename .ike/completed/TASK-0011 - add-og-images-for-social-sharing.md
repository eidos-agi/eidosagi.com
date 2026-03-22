---
id: TASK-0011
title: Add OG images for social sharing
status: Done
created: '2026-03-22'
priority: high
tags:
  - seo
definition-of-done:
  - Default OG image in public/og.png
  - 'og:image meta tag in Base.astro'
  - Image renders on social share preview
updated: '2026-03-22'
---
No og:image on any page. Site has no preview image when shared on Twitter/Slack/LinkedIn. Create a default OG image (1200x630) and add to Base.astro. Tool pages should ideally get tool-specific OG images.

**Completion notes:** OG image generated as SVG then converted to 1200x630 PNG (263KB). Added og:image, og:image:width, og:image:height, twitter:card, twitter:image to Base.astro. All pages share the same OG image.
