# /dev — Local Development Server

## When to Use
Starting a local dev session. Run this to spin up Astro and open the site in a browser.

## Execution Steps

### 1. Check Dependencies
Run `ls node_modules/.astro 2>/dev/null` to check if deps are installed.
If missing, run `npm install`.

### 2. Kill Stale Servers
Run `lsof -ti:4321 | xargs kill -9 2>/dev/null` to free port 4321 if occupied.

### 3. Start Astro Dev Server
Run `npm run dev` in background. Wait for the "Local" ready pattern in output.

### 4. Open in Browser
Run `open http://localhost:4321` to open the site in the default browser.

### 5. Report
Output:
```
  DEV       http://localhost:4321 — Astro dev server running
```

## Rules
- Never run `npm run dev` in foreground — it blocks the session.
- If port 4321 is busy after kill attempt, report the conflict and stop.
- Don't install unnecessary dependencies. Astro only.
