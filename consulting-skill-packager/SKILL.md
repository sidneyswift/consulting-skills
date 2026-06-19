---
name: consulting-skill-packager
description: Bundle the skills/ directory into an installable plugin. Use on "package the skills", "publish the plugin", or after authoring a new skill so it can trigger non-deterministically.
---

# Consulting Skill Packager

## Steps
1. Validate each `skills/{name}/SKILL.md` has valid frontmatter (name + description) and clear steps.
2. Bundle `skills/` into a plugin (plugin manifest + the skill folders). Use the `create-cowork-plugin` skill to produce the `.plugin` file.
3. Publish to GitHub as a plugin/marketplace repo (versioned, shareable).
4. Guide installing the plugin into the Claude workspace.
5. Confirm installed skills now trigger by description (no need to point at files).

Full lifecycle: `skills/_packaging/README.md`.
