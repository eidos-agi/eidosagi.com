# /copy-audit — Editorial Audit

## When to Use
After writing or modifying text on any page. Before deploy. The copy IS the product for a philosophy site.

## Voice Definition

### Target Register
Confident technical writing. Think well-edited blog post by someone who builds things — not a keynote, not a press release, not a LinkedIn post. The writer has opinions and evidence, and doesn't need rhetorical tricks to land them.

### Voice Rules
- Write real sentences. Combine related ideas into flowing prose.
- Be specific — numbers, file names, tool names beat adjectives.
- Be declarative. State what's true, don't sell.
- Technical fluency assumed — say "MCP server" without explaining it.
- Earn every sentence. If removing it changes nothing, remove it.

### Anti-Patterns (kill on sight)
- **Staccato fragments**: "No software. No database. No code." → Join into a real sentence.
- **Parallel triplets**: "Research earns. Visionlog records. Ike executes." → Write prose.
- **"That's [noun]."** as dramatic punctuation.
- **"Not X — Y"** used for false profundity: "Not a chatbot. A participant."
- **Rhetorical laddering**: three short sentences building to a punchline.
- **Hollow intensifiers**: "by a lot", "the real difference isn't X — it's Y", "that bet has never paid off."
- **Em dash as dramatic pause** more than once per page.
- **Marketing sentence starters**: "Imagine...", "What if...", "Here's the thing."

### Rewrite Protocol
When an anti-pattern is found, rewrite it as one clear sentence that carries the same information. Don't add words — restructure.

**Before**: "No software. No database. No code. Just YAML preferences and three JSON Schema contracts."
**After**: "A GitHub repo containing nothing but YAML preferences and three JSON Schema contracts."

## Execution Steps

### Pass 1: Redundancy Map
Read every `.astro` page in `src/pages/`. Build a table:

```
| Concept / Example        | Pages where it appears |
|--------------------------|------------------------|
| grocery ordering example | cdd, grocery, mvd, case-studies/index |
| AlphaZero analogy        | cdd                    |
| ...                      |                        |
```

Flag any concept that appears on 3+ pages. Propose which page OWNS it and where others should link instead of repeating.

### Pass 2: "So What?" Test
For every `<section class="content-section">` on every page, read it and ask: "so what?" If the section doesn't answer that — if removing it wouldn't change the reader's understanding — flag it for cut or rewrite.

Output:
```
PAGE: /contract-driven-development
  Section "The bitter lesson" — PASSES (core argument, earns the analogy)
  Section "The transition" — WEAK (restates what prior sections already established)
```

### Pass 3: Cut 30%
For each page, count total words. Target: remove 30% without losing meaning. Identify:
- Paragraphs that restate the previous paragraph in different words
- Throat-clearing openers ("The AI ecosystem is building skills — ...")
- Sections that exist to transition rather than inform
- Adjectives and adverbs that add no information

Output word count before/after per page.

### Pass 4: Progressive Disclosure
For each page, check: does the most compelling content come first?
- The hook (why should I care?) must be above the fold.
- Evidence and examples before theory and philosophy.
- If the page has a video or demo, it should be near the top, not buried.

Flag pages where the interesting part requires 3+ scrolls to reach.

### Pass 5: One Page, One Job
For each page, state its single job in ≤10 words. If you can't, the page is doing too many things.

```
/contract-driven-development — Argue that contracts beat skills
/forges — Catalog of available forges
/trilogy — Explain the three-tool governance stack
/case-studies/grocery — Prove contracts work with a real order
/minimum-viable-data — Argue that data beats code
```

Flag pages whose job overlaps with another page. Propose consolidation or clearer differentiation.

### Pass 6: Voice Consistency
Read all pages back-to-back in one sitting. Flag where tone shifts — e.g., one page reads like documentation, another like a manifesto, another like marketing copy. All should match the voice definition above.

### Pass 7: Anti-Pattern Grep
Run pattern matching for known AI tells across all pages:
- `. No [A-Z]` (staccato negation chains)
- Sentences under 5 words that aren't headings
- Three consecutive sentences starting with the same word
- "That's" followed by a period within 15 characters
- Paragraphs over 5 sentences (too long for web)

## Report Format

```
EDITORIAL AUDIT — eidosagi.com
<date>

REDUNDANCY MAP
  <concept>: owned by <page>, duplicated on <pages> — ACTION: <link/cut/rewrite>

"SO WHAT?" FAILURES
  <page> / <section> — <reason>

CUT TARGETS (30% goal)
  <page>: <before> words → <target> words
    - <specific cut>
    - <specific cut>

PROGRESSIVE DISCLOSURE
  <page>: <issue or PASS>

ONE PAGE ONE JOB
  <page>: <job> — <overlap concern or CLEAN>

VOICE SHIFTS
  <page>: <description of shift>

ANTI-PATTERNS
  <file>:<line> — <pattern found> → <suggested rewrite>

SUMMARY: <N> issues across <N> pages. Top 3 fixes by impact:
  1. ...
  2. ...
  3. ...
```

## Rules
- Be honest. Flag real problems, not nitpicks.
- Every flag must include a specific fix, not just "this is bad."
- Redundancy is the #1 problem on philosophy sites. Prioritize it.
- The grocery example is powerful but loses impact when it appears on every page.
- Don't add words to fix copy. Restructure or cut.
- Run this before every deploy that touches text content.
