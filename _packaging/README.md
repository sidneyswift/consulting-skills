# Packaging: this repo IS an installable plugin

This repo is a self-contained plugin **and** its own single-plugin marketplace, so it installs
directly from its GitHub URL — there's no build step and no `.plugin` artifact to produce.

## How it's wired
- `skills/<name>/SKILL.md` — one folder per skill (frontmatter `name` + `description`, then steps).
  The `SKILL.md` format is the same open standard across all three tools, so the skills are shared.
- `.cursor-plugin/marketplace.json` + `.cursor-plugin/plugin.json` — make it installable in **Cursor**.
- `.claude-plugin/marketplace.json` + `.claude-plugin/plugin.json` — make it installable in **Claude Code**.
- `.codex-plugin/plugin.json` + `.agents/plugins/marketplace.json` — make it installable in **Codex**.
  Codex uses a different layout: the manifest lives in `.codex-plugin/` and the marketplace catalog
  lives in `.agents/plugins/` (Codex also reads `.claude-plugin/marketplace.json` as a legacy fallback).
- All three manifests expose one plugin, **`consulting-os`** ("Consulting OS"), whose skills live in `skills/`.

## Add or change a skill
1. Create/edit `skills/<name>/SKILL.md` (rule of the practice: anything done 2+ times becomes a skill).
   Use `/skill-creator` to scaffold the frontmatter + steps.
2. (Optional) bump `version` in the `plugin.json` + `marketplace.json` files.
3. Commit and push. That's it — the skill is now part of the plugin.

## Install it
- **Cursor:** add the repo URL (`https://github.com/sidneyswift/consulting-plugin`) as a plugin
  source (plugins panel, or Team/Enterprise → Settings → Plugins → Import from Repo), then install
  **`consulting-os`**.
- **Claude Code:** add the same repo as a marketplace, then install the **`consulting-os`** plugin.
- **Codex:** run `codex plugin marketplace add sidneyswift/consulting-plugin`, then open the plugin
  directory (`/plugins` in the CLI) and install **`consulting-os`**. (Codex skills are an experimental
  feature — if the skills don't appear, enable the experimental `skills` feature in `~/.codex/config.toml`
  per the [Codex skills docs](https://developers.openai.com/codex/skills), then restart Codex.)
- Once installed, each skill auto-triggers by its `description` — no need to point at the file.

## Naming
Prefix practice skills with `consulting-` so they group together.
