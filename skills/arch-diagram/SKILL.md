---
name: arch-diagram
description: This skill should be used when the user asks to create a technical architecture diagram, system diagram, pipeline flow, swimlane diagram, flowchart, data flow diagram, or any technical documentation visual. Outputs SVG + PNG. Examples: "draw the ingestion pipeline", "create an architecture diagram", "make a flowchart for X", "explain the system with a diagram".
version: 1.0.0
---

# Technical Architecture Diagram Skill

Generate professional SVG architecture diagrams and export as PNG. Designed for engineering documentation: pipeline flows, system architectures, swimlane processes, CDC flows, deployment diagrams.

## Workflow

1. **Understand the system** — ask clarifying questions only if the structure is genuinely ambiguous
2. **Choose a layout** — pick from the pattern library below based on what best communicates the content
3. **Generate the SVG** — follow the conventions strictly
4. **Export to PNG** — always run `scripts/svg_to_png.py` after saving the SVG
5. **Confirm paths** — report both SVG and PNG output paths to the user

---

## SVG Conventions

### Canvas
- Width: **1200px**, Height: **auto** (900–1100px typical)
- Always set `viewBox="0 0 {width} {height}"`
- Background: **white `#ffffff`** (default) — use dark `#1e1e2e` only if user explicitly requests it

### Fonts
```svg
<style>
  text { font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; }
  .title   { font-size: 18px; font-weight: 700; fill: #1e293b; }
  .label   { font-size: 13px; font-weight: 600; fill: #1e293b; }
  .label-sm{ font-size: 11px; fill: #475569; }
  .label-xs{ font-size: 10px; fill: #64748b; }
  .mono    { font-family: 'Cascadia Code', 'Consolas', monospace; font-size: 11px; fill: #475569; }
</style>
```

### Color Palette

Use the **brand palette** when working in a specific organization context (see Branding section below).
Use the **neutral palette** for generic/public diagrams.

#### Default Palette (neutral, works for any company)
| Role | Fill | Stroke | Text |
|------|------|--------|------|
| Lane 1 (blue) | `#eff6ff` | `#3b82f6` | `#1e40af` |
| Lane 2 (teal) | `#f0fdfa` | `#0d9488` | `#115e59` |
| Lane 3 (gray) | `#f8fafc` | `#cbd5e1` | `#475569` |
| Warning | `#fefce8` | `#eab308` | `#854d0e` |
| Error | `#fef2f2` | `#ef4444` | `#991b1b` |
| Title bar | `#1e293b` | — | `#ffffff` |

> **Rule**: Use at most **3 lane colors** per diagram.

> **Branding**: To apply a company color palette, see `references/branding.md`.

### Drop Shadow (for lane containers)
```svg
<defs>
  <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
    <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#00000018"/>
  </filter>
</defs>
```

---

## Layout Patterns

### 1. Swimlane Diagram
Best for: multi-actor processes, pipeline phases, system boundaries

```
┌─ Title Bar (full width, dark blue) ───────────────────────┐
├─ Lane 1 (blue)  ──────────────────────────────────────────┤
│  [Box] ──→ [Box] ──→ ◇ Decision ──→ [Box]                │
├─ Lane 2 (orange) ─────────────────────────────────────────┤
│  [Box] ──→ [Box]                                          │
├─ Lane 3 (green) ──────────────────────────────────────────┤
│  [Output] ──→ [Store]                                     │
└─ Legend ──────────────────────────────────────────────────┘
```

Lane structure:
```svg
<!-- Lane container -->
<rect x="20" y="60" width="1160" height="280" fill="#eff6ff" rx="10" stroke="#3b82f6" stroke-width="1.5" filter="url(#shadow)"/>
<!-- Colored left accent bar -->
<rect x="20" y="60" width="6" height="280" fill="#3b82f6" rx="3"/>
<!-- Lane title -->
<text x="40" y="82" class="label" fill="#1e40af">Phase 1 — Name</text>
```

### 2. Flowchart
Best for: decision trees, conditional logic, process steps

Shapes:
- **Process**: rounded rect `rx="8"`
- **Decision**: diamond (polygon)
- **Start/End**: ellipse or pill shape
- **Data store**: cylinder approximation with two ellipses

### 3. System Architecture
Best for: component relationships, deployment topology, data flows

Use boxes with icons (Unicode chars work: `⚙`, `📦`, `🗄`, `🔄`) or simple colored badges.

### 4. Timeline / Sequence
Best for: CDC flows, event sequences, time-ordered steps

Use a horizontal arrow as timeline with vertical drop-lines to event boxes.

---

## Standard Components

### Process Box
```svg
<rect x="40" y="100" width="130" height="44" fill="#ffffff" rx="8" stroke="#3b82f6" stroke-width="1.5"/>
<text x="105" y="117" text-anchor="middle" class="label">Step Name</text>
<text x="105" y="131" text-anchor="middle" class="label-xs">subtitle</text>
```

### Decision Diamond
```svg
<polygon points="490,210 560,240 490,270 420,240" fill="#fefce8" stroke="#eab308" stroke-width="1.5"/>
<text x="490" y="244" text-anchor="middle" class="label" fill="#854d0e">Decision?</text>
```

### Arrow
```svg
<!-- Horizontal arrow with arrowhead marker -->
<defs>
  <marker id="arrow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
    <polygon points="0 0, 8 3, 0 6" fill="#475569"/>
  </marker>
</defs>
<line x1="170" y1="122" x2="210" y2="122" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)"/>
```

### Data Store (cylinder)
```svg
<rect x="750" y="200" width="110" height="50" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
<ellipse cx="805" cy="200" rx="55" ry="8" fill="#dcfce7" stroke="#22c55e" stroke-width="1.5"/>
<ellipse cx="805" cy="250" rx="55" ry="8" fill="#dcfce7" stroke="#22c55e" stroke-width="1.5"/>
```

### Title Bar
```svg
<rect x="0" y="0" width="1200" height="48" fill="#1e40af"/>
<text x="20" y="30" class="title" fill="#ffffff">Diagram Title</text>
<text x="1180" y="30" text-anchor="end" class="label-sm" fill="#93c5fd">subtitle / date</text>
```

### Legend
```svg
<!-- Legend box at bottom -->
<rect x="20" y="880" width="1160" height="60" fill="#f8fafc" rx="8" stroke="#e2e8f0" stroke-width="1"/>
<text x="36" y="900" class="label-xs" fill="#94a3b8">LEGEND</text>
<!-- Legend items: colored dot + label -->
<circle cx="100" cy="898" r="5" fill="#3b82f6"/>
<text x="110" y="902" class="label-xs">Phase 1 label</text>
```

---

## Note / Callout Box
```svg
<!-- Warning callout -->
<rect x="40" y="840" width="300" height="36" fill="#fef9c3" rx="6" stroke="#eab308" stroke-width="1"/>
<text x="56" y="856" class="label-xs" fill="#854d0e">⚠ Note title:</text>
<text x="130" y="856" class="label-xs">note content here</text>
```

---

## Branding

See `references/branding.md` for instructions on applying a custom company palette.
Add `<!-- BRAND: <company> -->` at the top of the SVG to document which palette was used.

---

## Quality Checklist

Before saving the SVG, verify:
- [ ] No text overflows its box boundaries
- [ ] No overlapping elements
- [ ] All arrows connect to actual boxes (not floating)
- [ ] Consistent spacing (multiples of 8px)
- [ ] All lanes have left accent bar in matching color
- [ ] Legend explains any non-obvious color coding
- [ ] Decision diamonds have YES/NO (or equivalent) labels on branches
- [ ] viewBox matches actual height

---

## PNG Export

Always run after saving the SVG:

```bash
uv run python /path/to/scripts/svg_to_png.py <svg_path> [--scale 2]
```

Or directly in Python if `uv` is unavailable:
```python
import cairosvg
cairosvg.svg2png(url="path/to/diagram.svg", write_to="path/to/diagram.png", scale=2)
```

Output at 2× scale = ~2400px wide, suitable for documentation and presentations.

---

## Output

Always report:
- SVG path
- PNG path
- Diagram dimensions (width × height)
- Brief description of what the diagram shows
