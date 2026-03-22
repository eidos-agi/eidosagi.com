# /deploy — Build + Deploy to Railway

## When to Use
Ship the site to production. Builds locally first to catch errors, then deploys via Railway.

## Execution Steps

### 1. Pre-flight Checks
- Run `npm run build` — must succeed with zero errors
- Check that `dist/` was generated
- Verify no `.env` files or secrets would be deployed

### 2. Run /lighthouse (inline)
Before deploying, run a Lighthouse audit on the built preview. The site must score 95+ on Performance before shipping. If it doesn't, STOP and fix.

```bash
npm run preview &
# Wait for server ready
# Run lighthouse audit
# Kill preview
```

### 3. Git State Check
- `git status` — warn about uncommitted changes
- Recommend committing before deploy

### 4. Deploy to Railway
Use the railguey MCP or `railway up` CLI:
```bash
railway up --detach
```

If no Railway project is linked, prompt the user to run `railway link` first.

### 5. Verify Deployment
- Check Railway deployment status
- Hit the production URL and verify 200 response
- Report the live URL

### 6. Report
```
  DEPLOY    eidosagi.com — live | Lighthouse <score> | Build <time>
```

## Rules
- NEVER deploy if Lighthouse Performance < 95. The book demands it.
- NEVER deploy uncommitted changes without explicit user approval.
- Always build locally first — don't rely on Railway's build to catch errors.
