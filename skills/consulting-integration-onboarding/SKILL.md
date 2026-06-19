---
name: consulting-integration-onboarding
description: Stand up a new external integration (a data source / channel like Granola, Attio, LinkedIn, Gmail, Slack) the same way every time. Use on "add an integration", "connect <tool>", "set up the <tool> integration", or when wiring a new live source into the OS.
---

# Consulting Integration Onboarding

Scaffold a new `integrations/<tool>/` so it matches the established pattern (Gmail/Slack are the
references) and actually feeds the flywheel — instead of a one-off. Mirror, don't reinvent.

## Steps
1. **Pick the ownership type** (decides what belongs in the repo): **mirror** (can't organize in the
   source → the repo copy *is* the artifact, e.g. Granola) · **query** (live system of record → keep
   only thin snapshots, e.g. Attio) · **log** (you log distilled signal, raw stays in the tool, e.g.
   Gmail/Slack/LinkedIn) · **mine** (read-only content source, e.g. Research). See `integrations/AGENTS.md`.
2. **Scaffold `integrations/<tool>/`:**
   - `AGENTS.md` — what it is, the ownership type, what's in- vs out-of-repo, signal-vs-noise, and the
     non-negotiables (never auto-send, never auto-delete/sweep, cite primary sources).
   - `_work/_lib.py` — `load_env()` reading repo-root `.env.local` + an API client (stdlib `urllib` +
     `certifi` SSL context + HTTP 429 retry; mirror `integrations/slack/_work/_lib.py`).
   - `_work/check_auth.py` — verify the credential(s); print who you're authed as.
   - pull/ingest scripts that write **deal-scoped** snapshots next to the relevant `clients/`/`pipeline/`
     entity; raw lands in `_work/staging/` (**gitignored**).
   - `_work/LAST_SYNCED` — the delta watermark.
3. **Secrets:** add the API key(s) to repo-root `.env.local` (gitignored) and **document the key names**
   in `integrations/AGENTS.md` (env-key list + ownership table + folders table).
4. **Wire into the cadence so it can't go stale:** add the source to **`consulting-integrations-sync`**
   (Friday) and **`consulting-nightly-ingestion`** (bounded `--days` delta off `LAST_SYNCED` — never an
   unbounded backfill for rate-limited sources).
5. **Verify end-to-end:** run `check_auth.py`, do one real pull, confirm a snapshot lands in the right
   entity folder, then commit (why-first message).

Non-negotiables: **never auto-send** (drafts only), **never auto-delete/sweep**, deal-scoped loading,
cite primary sources, and never copy a live system of record wholesale into the repo.
