---
name: screenshot
description: >
  Capture a full-page screenshot of any public URL using Playwright's headless Chromium browser.
  Use this skill whenever the user provides a URL and asks to take a screenshot, capture a page,
  grab a visual snapshot, or see what a website looks like. Also trigger when the user says things
  like "screenshot this", "capture this page", "show me what this site looks like", or
  "get a screenshot of [URL]". Works on GitHub, Docker Hub, dev.to, npm, PyPI, and any public website.
  No API key required — uses a local headless browser via Playwright.
version: 1.0.0
---

# Screenshot Skill

Capture full-page screenshots of any public URL using Playwright's headless Chromium browser.
Save as PNG and describe the visual content. No API key or external service required.

---

## Prerequisites

- Node.js installed
- Playwright available via `npx playwright`
- Chromium browser downloaded for Playwright

If Playwright browsers are not installed, run:
```bash
npx playwright install chromium
```

---

## Workflow

### Step 1 — Validate inputs

1. Confirm the user has provided a valid URL (must start with `http://` or `https://`).
   If no protocol is given, prepend `https://`.
2. Quick-check that Playwright is available:
   ```bash
   npx playwright --version
   ```
   If this fails, tell the user to install it:
   ```bash
   npm install -g playwright
   npx playwright install chromium
   ```

### Step 2 — Derive the output filename

Strip the URL to create a clean filename:
- Remove `https://` or `http://`
- Remove `www.` prefix if present
- Remove trailing slashes
- Replace all dots, slashes, and special characters with underscores
- Truncate to 60 characters max
- Append `.png`

Examples:
| URL | Filename |
|-----|----------|
| `https://github.com/anthropics/claude-code` | `github_com_anthropics_claude-code.png` |
| `https://hub.docker.com` | `hub_docker_com.png` |
| `https://news.ycombinator.com` | `news_ycombinator_com.png` |
| `https://dev.to` | `dev_to.png` |

### Step 3 — Take the screenshot

Run this command, substituting the URL and derived filename:

```bash
npx playwright screenshot --full-page --wait-for-timeout 3000 "URL" "FILENAME"
```

**Options to use depending on context:**
- `--full-page` — captures the entire scrollable page (always use)
- `--wait-for-timeout 3000` — wait 3 seconds for JS to load (default)
- `--ignore-https-errors` — add if the site has SSL issues
- `--block-service-workers` — add if the page is slow or uses service workers

If the default screenshot fails (e.g., timeout, rendering issues), retry with extended options:
```bash
npx playwright screenshot --full-page --wait-for-timeout 5000 --block-service-workers --ignore-https-errors "URL" "FILENAME"
```

After running, verify the file was created and is non-empty:
```bash
[ -s "FILENAME" ] && echo "Success: $(wc -c < FILENAME) bytes" || echo "Failed"
```

**Common errors:**
| Error | Cause | Fix |
|-------|-------|-----|
| Executable doesn't exist | Chromium not installed | Run `npx playwright install chromium` |
| Timeout | Page takes too long | Increase `--wait-for-timeout` to 10000 |
| Empty file | Page blocked rendering | Try with `--block-service-workers` |
| Navigation error | Invalid URL or DNS failure | Check URL is correct and accessible |

### Step 4 — View and describe the screenshot

After a successful capture:

1. Use the Read tool to open and visually inspect the PNG file.
2. Tell the user the exact file path and file size.
3. Write a single sentence describing what is visible in the screenshot.

---

## Response format

```
Screenshot captured!

Location: /path/to/FILENAME.png
Size: XXX KB

What's in it: [One-sentence visual description]
```
