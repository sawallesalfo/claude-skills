# claude-skills

A collection of reusable skills for [Claude Code](https://claude.ai/code) — technical documentation, architecture diagrams, and engineering workflows.

Skills are modular extensions that teach Claude specialized workflows. Each skill lives in its own folder and is loaded dynamically when needed.

---

## Available Skills

| Skill | Description |
|-------|-------------|
| [`arch-diagram`](./skills/arch-diagram/) | Generate technical architecture diagrams as SVG + PNG (pipeline flows, swimlanes, system diagrams) |

More skills coming.

---

## Installation

### Option 1 — Claude Code marketplace (recommended)

Run this command inside Claude Code:

```
/plugin marketplace add <your-github-username>/claude-skills
```

Then install a skill:
1. Run `/plugin install`
2. Select `claude-skills`
3. Select `arch-diagram`

Once installed, just describe what you want — Claude will use the skill automatically:
> *"Create an architecture diagram for our data pipeline"*
> *"Draw a swimlane diagram showing the user authentication flow"*

### Option 2 — Manual install

Copy the skill folder to your local Claude plugins directory:

```bash
# macOS / Linux
cp -r skills/arch-diagram ~/.claude/plugins/skills/

# Windows
xcopy skills\arch-diagram %USERPROFILE%\.claude\plugins\skills\arch-diagram /E /I
```

---

## How Skills Work

A skill is a folder with a `SKILL.md` file. Claude reads it when the task matches the skill's description (defined in the YAML frontmatter). Skills can also include:

- `references/` — documentation loaded into context as needed
- `scripts/` — reusable scripts Claude can run
- `assets/` — templates, examples, fonts

```
skills/
└── arch-diagram/
    ├── SKILL.md              ← instructions + metadata (required)
    ├── references/
    │   └── branding.md       ← how to apply company colors
    ├── scripts/
    │   └── svg_to_png.py     ← SVG → PNG conversion
    └── assets/
        ├── example.svg       ← reference diagram
        └── example.png
```

See the [Agent Skills spec](https://agentskills.io) and [Anthropic's documentation](https://support.claude.com/en/articles/12512176-what-are-skills) for more details.

---

## Usage Example

After installing `arch-diagram`, ask Claude:

> *"Draw a 3-lane swimlane diagram for our document ingestion pipeline: sources → processing → storage. Use the green & gold palette from branding.md."*

Claude will generate an SVG, export a 2× PNG, and report both paths.

---

## Contributing

Skills are plain Markdown — no build step, no dependencies. To add a skill:

1. Create a folder under `skills/your-skill-name/`
2. Add a `SKILL.md` with YAML frontmatter (`name`, `description`)
3. Open a PR

---

## License

MIT — see [LICENSE](./LICENSE).
