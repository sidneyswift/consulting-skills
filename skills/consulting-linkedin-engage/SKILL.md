---
name: consulting-linkedin-engage
description: Build a daily LinkedIn comment-target queue — whose posts Sidney should comment on to warm ICP prospects, with draft angles in his voice. Use on "who should I comment on", "build my engagement queue", "LinkedIn commenting plan", "warm up prospects on LinkedIn". The agent ranks targets; Sidney writes + posts the comments himself (never auto-comment).
---

# Consulting LinkedIn Engage

Social-selling via thoughtful commenting — the safe, human-in-the-loop way. The agent decides
**where** to engage (ranked targets + angles); **Sidney writes and posts** every comment in his own
voice. This is the deliberate opposite of auto-comment tools (slop) and engagement pods (ban risk).

## Why this shape
None of the LinkedIn-native commenting tools expose an API, and unattended AI comments erode a
credibility-led brand. So the agent's job is **targeting + drafting angles**, not posting. See
`integrations/linkedin/linkedin-funnel-strategy.md` (commenting section).

## Steps
1. **Assemble the target pool** from three sources:
   - **Warm engagers** — recent `integrations/linkedin/engagement/*-enriched.json` (people who already
     engaged Sidney's posts; they carry an `icp` tier from `score_lead`).
   - **Attio Warm Leads (live)** — query the Warm Leads list; these are known prospects worth nurturing.
   - **Fresh ICP posts (outbound)** — run `python integrations/linkedin/_work/find_posts.py --query "<ICP topic>"`
     (e.g. "music AI", "catalog valuation", "label operations") to surface recent posts by ICP voices
     to comment on. (Apify post-search, ~$1.50/1k; the script confirms cost first.)
2. **Rank.** Score each target by **ICP fit** (reuse `score_lead.score_fit`; tiers A→D from
   `positioning/icp.md`) × **opportunity** (do they have a recent post to comment on?). Comment depth
   beats likes; A/B tier with a fresh post ranks highest. Drop C/D unless there's a strong reason.
3. **Draft angles, not comments.** For each top target produce: **who** (name, title, company, tier),
   **why they fit** (the ICP signal), the **specific post URL** to comment on, and **1–2 comment
   angles** — a genuine point of view grounded in *their* post + Sidney's positioning (turn scattered
   AI experimentation into coordinated capability). Angles are seeds; Sidney writes the real comment.
4. **Output the queue.** Write `integrations/linkedin/engagement/<date>-engage-queue.md` — a short
   ranked list (cap ~5–10 targets/day) Sidney can work through in one sitting. Keep it scannable.
5. **Guardrails (non-negotiable).**
   - **Never auto-comment, never connect/DM** from this skill — it produces a queue only.
   - **No engagement pods**, ever (Lempod-style coordinated engagement = shadow-ban risk).
   - Comments stay in **Sidney's voice**; the angles must be specific to the post, never generic praise.
   - **Cap the daily volume** (~5–10 thoughtful comments) and spread it out — protect the account.
6. **Close the loop.** Note which targets Sidney engaged so a later `consulting-linkedin-audience` pull
   can see who replied/engaged back → enrich → Attio. Comments that spark a reply are the warmest
   possible top-of-funnel signal.

## Chains with
- `find_posts.py` (outbound target discovery) · `pull_engagement.py` + `enrich.py` (warm engagers +
  ICP scores) · `consulting-linkedin-audience` (convert engagers who reply into Attio leads) ·
  `consulting-followup-sequencer` for the eventual follow-up (only after a real interaction).
