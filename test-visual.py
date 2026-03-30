#!/usr/bin/env python3
"""
Visual regression testing for eidosagi.com

Commands:
  python3 test-visual.py baseline   — capture baseline screenshots
  python3 test-visual.py test       — capture current, diff against baseline, report regressions
  python3 test-visual.py review     — open the diff report

Stores baselines in screenshots/baseline/
Stores current in screenshots/current/
Stores diffs in screenshots/diff/
Writes report to screenshots/report.md

Use --prod to test against https://eidosagi.com instead of localhost:4321
"""

import hashlib
import sys
import json
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = "https://eidosagi.com" if "--prod" in sys.argv else "http://localhost:4321"

PAGES = [
    ("/", "home"),
    ("/eidos", "eidos"),
    ("/trilogy", "trilogy"),
    ("/contract-driven-development", "contracts"),
    ("/minimum-viable-data", "mvd"),
    ("/forges", "forges"),
    ("/memory", "memory"),
    ("/agent-identity", "identity"),
    ("/case-studies", "case-studies"),
    ("/case-studies/grocery", "grocery"),
    ("/about", "about"),
    ("/changelog", "changelog"),
]

VIEWPORTS = [
    ("desktop", 1440, 900),
    ("mobile", 390, 844),
]

ROOT = Path("screenshots")
BASELINE = ROOT / "baseline"
CURRENT = ROOT / "current"
DIFF = ROOT / "diff"
MANIFEST = ROOT / "manifest.json"


def capture(output_dir: Path):
    """Screenshot every page at every viewport into output_dir."""
    output_dir.mkdir(parents=True, exist_ok=True)
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for vp_name, width, height in VIEWPORTS:
            context = browser.new_context(viewport={"width": width, "height": height})
            page = context.new_page()

            for path, name in PAGES:
                url = f"{BASE}{path}"
                fname = f"{name}-{vp_name}.png"
                fpath = output_dir / fname

                try:
                    page.goto(url, wait_until="networkidle", timeout=15000)
                    page.wait_for_timeout(500)
                    page.screenshot(path=str(fpath), full_page=True)

                    # Hash for comparison
                    sha = hashlib.sha256(fpath.read_bytes()).hexdigest()[:12]
                    results.append({"file": fname, "path": path, "viewport": vp_name, "sha": sha, "status": "ok"})
                    print(f"  OK  {fname} ({sha})")
                except Exception as e:
                    results.append({"file": fname, "path": path, "viewport": vp_name, "sha": None, "status": f"error: {e}"})
                    print(f"  FAIL {fname}: {e}")

            context.close()
        browser.close()

    return results


def do_baseline():
    """Capture baseline screenshots."""
    print(f"Capturing baseline from {BASE}\n")
    results = capture(BASELINE)

    # Save manifest
    manifest = {
        "type": "baseline",
        "timestamp": datetime.now().isoformat(),
        "base_url": BASE,
        "pages": len(PAGES),
        "viewports": len(VIEWPORTS),
        "screenshots": results,
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2))
    print(f"\nBaseline: {len(results)} screenshots in {BASELINE}/")
    print(f"Manifest: {MANIFEST}")


def do_test():
    """Capture current, diff against baseline, report."""
    if not MANIFEST.exists():
        print("No baseline. Run: python3 test-visual.py baseline")
        sys.exit(1)

    baseline_manifest = json.loads(MANIFEST.read_text())
    baseline_map = {s["file"]: s["sha"] for s in baseline_manifest["screenshots"] if s["sha"]}

    print(f"Capturing current from {BASE}\n")
    current_results = capture(CURRENT)

    # Diff
    DIFF.mkdir(parents=True, exist_ok=True)
    changed = []
    unchanged = []
    missing = []
    errors = []

    for result in current_results:
        fname = result["file"]
        if result["sha"] is None:
            errors.append(result)
            continue

        if fname not in baseline_map:
            changed.append({**result, "reason": "new page (no baseline)"})
            continue

        if result["sha"] != baseline_map[fname]:
            changed.append({**result, "reason": "visual change", "baseline_sha": baseline_map[fname]})

            # Create a simple diff by keeping both files — a human or AI reviews them
            baseline_file = BASELINE / fname
            current_file = CURRENT / fname
            if baseline_file.exists() and current_file.exists():
                # Copy both to diff dir for side-by-side review
                import shutil
                shutil.copy(baseline_file, DIFF / f"baseline-{fname}")
                shutil.copy(current_file, DIFF / f"current-{fname}")
        else:
            unchanged.append(result)

    # Report
    report = f"# Visual Regression Report\n\n"
    report += f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    report += f"**Base URL:** {BASE}\n"
    report += f"**Baseline:** {baseline_manifest['timestamp'][:10]}\n\n"

    if not changed and not errors:
        report += f"**Result: PASS** — {len(unchanged)} screenshots match baseline. No regressions.\n"
    else:
        report += f"**Result: {len(changed)} changes, {len(errors)} errors, {len(unchanged)} unchanged**\n\n"

        if changed:
            report += "## Changes\n\n"
            report += "| Page | Viewport | Reason |\n|------|----------|--------|\n"
            for c in changed:
                report += f"| {c['path']} | {c['viewport']} | {c['reason']} |\n"
            report += f"\nReview diffs in `screenshots/diff/`\n\n"

        if errors:
            report += "## Errors\n\n"
            for e in errors:
                report += f"- {e['file']}: {e['status']}\n"

    report_path = ROOT / "report.md"
    report_path.write_text(report)
    print(f"\n{'=' * 40}")
    print(report)
    print(f"Report: {report_path}")
    if changed:
        print(f"Diffs:  {DIFF}/")


def do_review():
    """Show the report."""
    report_path = ROOT / "report.md"
    if report_path.exists():
        print(report_path.read_text())
    else:
        print("No report. Run: python3 test-visual.py test")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "test"
    if cmd == "baseline":
        do_baseline()
    elif cmd == "test":
        do_test()
    elif cmd == "review":
        do_review()
    else:
        print("Usage: python3 test-visual.py [baseline|test|review] [--prod]")
