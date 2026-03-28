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

### Option 1 — Install as plugin from GitHub (recommended)

Run this inside Claude Code:

```
/plugin install sawallesalfo/claude-skills
```

Once installed, just describe what you want — Claude will use the skill automatically:
> *"Create an architecture diagram for our data pipeline"*
> *"Draw a swimlane diagram showing the user authentication flow"*

### Option 2 — Copy skill to your project

Add the skill directly to your project (tracked in git, available to your team):

```bash
# Copy to your project's .claude/skills/ directory
mkdir -p .claude/skills
cp -r skills/arch-diagram .claude/skills/arch-diagram
```

### Option 3 — Copy skill globally (personal)

Make the skill available across all your projects:

```bash
# macOS / Linux
mkdir -p ~/.claude/skills
cp -r skills/arch-diagram ~/.claude/skills/arch-diagram

# Windows (PowerShell)
Copy-Item -Recurse skills\arch-diagram $env:USERPROFILE\.claude\skills\arch-diagram
```

After any option, invoke with `/arch-diagram` or just ask Claude to create a diagram — it will detect the skill automatically from the description.

---

## How Skills Work

A skill is a folder with a `SKILL.md` file. Claude reads it when the task matches the skill's description (defined in the YAML frontmatter). Skills can also include:

- `references/` — documentation loaded into context as needed
- `scripts/` — reusable scripts Claude can run
- `assets/` — templates, examples, fonts

```
skills/
└── arch-diagram/
    ├── SKILL.md              <- instructions + metadata (required)
    ├── references/
    │   └── branding.md       <- how to apply company colors
    ├── scripts/
    │   └── svg_to_png.py     <- SVG -> PNG conversion
    └── assets/
        ├── example.svg       <- reference diagram
        └── example.png
```

See the [Agent Skills spec](https://agentskills.io) and [Anthropic's documentation](https://support.claude.com/en/articles/12512176-what-are-skills) for more details.

---

## Usage Example

After installing `arch-diagram`, ask Claude:

> *"Draw a 3-lane swimlane diagram for our document ingestion pipeline: sources -> processing -> storage. Use the green & gold palette from branding.md."*

Claude will generate an SVG, export a 2x PNG, and report both paths.

---

## Contributing

Skills are plain Markdown — no build step, no dependencies. To add a skill:

1. Create a folder under `skills/your-skill-name/`
2. Add a `SKILL.md` with YAML frontmatter (`name`, `description`)
3. Open a PR

---

## License

MIT — see [LICENSE](./LICENSE).
