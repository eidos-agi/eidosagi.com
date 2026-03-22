# /brand-sync — Propagate Brand Copy Across Ecosystem

## When to Use
After updating copy on eidosagi.com. The website is the source of truth — everything else follows.

## What Stays in Sync
| Source (eidosagi.com) | Target | File |
|-----------------------|--------|------|
| Tagline | GitHub org profile | `~/repos-eidos-agi/.github/profile/README.md` |
| Mission paragraph | GitHub org profile | `~/repos-eidos-agi/.github/profile/README.md` |
| Package list (Trilogy, MCP, Tools) | GitHub org profile | `~/repos-eidos-agi/.github/profile/README.md` |
| Join Us copy | GitHub org profile | `~/repos-eidos-agi/.github/profile/README.md` |
| Package descriptions | Individual repo READMEs | Each repo's `README.md` header |

## Execution Steps

### 1. Extract Current Website Copy
Read the Astro source files and extract:
- Tagline (hero section)
- Mission paragraph
- Package names + descriptions + install commands
- Join Us copy
- Contact email

### 2. Diff Against Targets
Read each target file and compare the equivalent sections. Show diffs for any mismatches.

### 3. Present Changes
Output a summary table:
```
  BRAND SYNC    <N> targets checked | <N> drifted | <N> in sync

  DRIFTED:
  - .github/profile/README.md — tagline differs
  - railguey/README.md — description outdated
```

### 4. Apply (with approval)
Ask the user before writing changes. Show the exact edits that will be made.

For each target:
- Read the file
- Replace the relevant section
- Write the updated file

### 5. Commit Guidance
Suggest committing the sync changes in each affected repo:
```
chore: sync brand copy from eidosagi.com
```

## Rules
- The website is ALWAYS the source of truth. Never sync FROM GitHub TO the website.
- Don't touch content that isn't part of the brand copy (e.g., technical docs in READMEs).
- Always show diffs before applying. Never auto-write.
- Package descriptions should match between the website and the repo's README, but the README can have more detail.
