---
name: consulting-nightly-content
description: Phase 3 of the nightly pipeline — the content engine. After capture + janitor, mine the day's NEW insights into LinkedIn post drafts (voice-compliant, grounded in real captured calls/research), staged for morning review. NEVER auto-publishes. Use on "run the nightly content", "draft today's posts", or as the nightly content ritual. Feeds the flywheel: Content -> LinkedIn -> engagement -> leads.
---

# Consulting Nightly Content (the flywheel's draft engine)

Capture turns calls into insights; this turns the day's **new** insights into **staged LinkedIn post
drafts** Sid reviews and publishes in the morning. It feeds the loop: Content → LinkedIn → engagement →
leads in Attio → calls → mined into insights → Content.

The engine drafts; **Sid publishes.** Quality over volume — a couple of strong, grounded posts beat a
pile of generic ones.

## Rails
1. **Never auto-publish.** Drafts only → `content/drafts/`. Sid reviews + publishes via
   `consulting-linkedin-publisher` (`integrations/linkedin/_work/publish.py`). Do **not** call publish.
2. **Grounded, not fabricated.** Every post traces to a real captured insight/transcript — carry the
   citation. **Never invent a client name, number, or result.** Confirm before naming a client; otherwise
   write the lesson generically.
3. **Voice (writing-voice-rules).** No em-dashes. Short declaratives. Human, direct, specific. No AI-slop
   ("delve", "unlock", "seamless", "game-changer", "in today's fast-paced…", "it's not just X, it's Y").
   Lead with the problem + outcome, not your resume.
4. **Quality over volume.** 2–4 strong posts a night, max. Thin insights → don't force a post. A quiet
   night (nothing new worth posting) is a one-line report, no drafts.

## Steps
0. **Orient + find what's new.** Read the day's `business/ops/nightly-digests/<date>.md`. Gather fodder
   newer than the watermark `content/_work/LAST_DRAFTED`: new `knowledge/insights/*.md` and
   `content/ideas/*.md` (the capture sweep deposits these). `git log` for what landed today.

1. **Select 2–4.** Pick the strongest, most *specific* fresh insights — the ones with a real story or a
   non-obvious POV from an actual call/research. **Dedup:** skip anything already in `content/published/`
   or `content/drafts/` (never redraft a published idea — "never post the same post twice").

2. **Draft each via `consulting-content-drafter`.** Title formula + AIDA + specificity ladder → a
   LinkedIn post. Apply the voice rules above (run/lean on `consulting-email-voice` for the sweep). Keep
   every claim traceable to its source insight/transcript; if research-derived, pull the cited wiki page
   per `integrations/research/AGENTS.md`.

3. **Stage.** Write each to `content/drafts/<YYYY-MM-DD>-<slug>.md` with frontmatter: `source:` (the
   insight/transcript path), `hook:` (the first line), `audience:` (IC vs leadership), `status: draft`.
   **Do not publish.**

4. **Report + score + commit.** Write `business/ops/content-reports/<date>.md` (**Drafted · Skipped (why)
   · Needs Sid**), run `python evals/content/score_run.py` and put the composite + flags at the top,
   commit each draft why-first, stamp `content/_work/LAST_DRAFTED`, then stop.

## Notes
- **Mine, don't manufacture.** The fodder is real captured calls/research — if the day produced nothing
  worth saying, say nothing. The flywheel rewards signal, not cadence.
- Scored by `evals/content/score_run.py` (grounding, voice, non-duplication, throughput). Engagement →
  leads is the lagging metric — read it from the LinkedIn engagement pull, not this scorer.
