---
name: consulting-integration-scaffolder
description: Stand up a new external-tool integration in one move. Use on "add an integration for X", "connect <tool>", "I have an API key for X", or whenever a new data source/channel should flow into the OS. Scaffolds integrations/<tool>/ in the house pattern.
---

# Consulting Integration Scaffolder

The repeatable recipe behind `integrations/linkedin/` and `integrations/gmail/`. Given a tool + API
key, build the standard structure so every integration looks and works the same.

## First: classify the ownership type (decides what lives in the repo)
Per `integrations/AGENTS.md`: **Granola you mirror, Attio you query, LinkedIn/Gmail you log, Research you mine.**
- **Read-only source** (can't organize at source) → mirror + index in the repo.
- **System of record** (full API) → store only a thin regenerated snapshot; query live.
- **Channel** (read signal + write actions) → log distilled signal + published artifacts.
- **Read-only content source** (e.g. a local knowledge repo) → mine the delta into `content/` only;
  cite, don't copy. No mirror, and no scripts if it's local files (see `integrations/research/`).

## Steps
1. **Put the key in `.env.local`** (repo root, gitignored) — never in the integration folder.
   Confirm with the user; show key *names* only.
2. **Create the folder:** `integrations/<tool>/` with a `_work/` dir + the signal subfolders the
   ownership type implies (e.g. `published/`, `engagement/`, `threads/`). Add `.gitkeep` to empties.
3. **Write `_work/_lib.py`** — stdlib-only env loader + an SSL-safe HTTP/auth helper. Reuse the
   pattern from `integrations/linkedin/_work/_lib.py` (certifi-backed `ssl` context; macOS
   Python.framework lacks linked CA certs, so always set the context explicitly).
4. **Write the scripts:** a `pull_*`/read script and (if it's a channel) a `publish_*`/write script.
   Writes must **confirm before sending** and default to draft/dry-run. Add a `LAST_SYNCED` marker.
5. **Verify live** with a free/read-only call (token check, list accounts) before claiming it works.
6. **Write `integrations/<tool>/AGENTS.md`** (agent-native, not a README) — accounts/IDs,
   in-vs-out-of-repo rules, scripts table, examples, and activation steps. Add a row to the folder
   table in `integrations/AGENTS.md`.
7. **Author companion skills** if there's a recurring task (a publisher, an audience/triage skill).
8. **Gitignore any credential cache** (tokens) and commit. `__pycache__/` is already ignored.

Output: a working, documented integration that the `consulting-integrations-sync` skill can keep fresh.
