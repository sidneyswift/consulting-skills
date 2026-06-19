---
name: consulting-proposal-designer
description: Build the branded, 2-page Recoup proposal (HTML → PDF) from the reusable design + copy frameworks. Use after the copy/pricing is decided (e.g. via consulting-proposal-drafting + consulting-pricing-builder) and you need the polished client-facing artifact. Most of the proposal is fixed boilerplate; only the company-specific slots change. Triggers: "design the proposal", "build the proposal PDF", "make the branded proposal", "turn this into the 2-pager".
---

# Consulting Proposal Designer

Turns decided copy into the finished, branded 2-page proposal — the same layout and voice
every time, so only the **company-specific slots** change deal to deal. The framework is the
product; the client text is the variable.

> Sibling skills: `consulting-proposal-drafting` decides the *content/structure*,
> `consulting-pricing-builder` decides the *numbers*. This skill owns the *design + final render*.
> Run it last.

## When to run
After the situational copy and the 3-tier pricing are settled for a qualified deal — when you
need the shareable PDF (usually paired with a Loom; see `consulting-followup-sequencer`).

## Inputs you need first
- The two situational lead paragraphs (problem framing).
- "Where they are today" (3 bullets) and "Where this takes you" (3 bullets).
- The 3-tier investment numbers + the project band (from `consulting-pricing-builder`).
- The close anchor (the value comparison) and the client name/contact/date.

## What's FIXED vs. what CHANGES
**Fixed boilerplate (carry over almost verbatim — this is the framework):**
- Brand header: dotwave motif + Recoup wordmark, "Proposal" kicker, accent rule.
- The 5-block spine: Lead paragraphs → Now/Next panels → "How we get there" → Investment tiers →
  dark Close box with numbered next steps.
- The entire **"How we get there"** block — the four steps AND their sentences (Audit · Own it ·
  Build it · Maintain It) — is fixed across every proposal. Don't rewrite it per deal.
- The capacity-not-features pricing model: Advisory / **Comprehensive (recommended)** / Partnership,
  with the middle tier visually highlighted and the project band stated openly.
- The "no surprise invoices / month-to-month" assurance and the 25-min review-call ask.
- All CSS, type scale, and color tokens in the template.

**Company-specific slots (the only things you rewrite — marked `{{LIKE_THIS}}` in the template):**
- `{{CLIENT_NAME}}`, `{{CLIENT_CONTACT}}`, `{{DOC_DATE}}`
- `{{LEAD_PARA_1}}`, `{{LEAD_PARA_2}}` — their specific proof + their specific gap
- `{{NOW_1..3}}` / `{{NEXT_1..3}}` — their current state vs. outcomes
- `{{TIER_*}}` — only if the numbers/feature lines differ from the standard $5k/$15k/$30k
- `{{CLOSE_ANCHOR}}` — the value comparison ("for about the cost of one senior AI hire…")

## Steps
1. Read `assets/copy-and-design-frameworks.md` — the patterns and the rules behind each slot.
2. Copy `assets/proposal-template.html` to the deal's `02-proposals/{client-slug}-proposal.html`.
3. Fill every `{{SLOT}}` using the frameworks doc. Touch nothing outside the slots.
4. Render to PDF with Chromium (highest fidelity) → `{client-slug}-proposal-YYYY-MM-DD.pdf`:
   ```
   python3 assets/render.py 02-proposals/{client-slug}-proposal.html
   ```
   (WeasyPrint is an acceptable fallback if Chromium is unavailable; expect minor spacing drift.)
5. Verify: 2 pages, no leftover `{{` placeholders, prices read correctly.
6. Keep the `.html` as the editable source of truth; the `.md` canonical copy lives alongside it.
7. Remind: deliver within 48h, attach the Loom, lock the review call (per playbook Ch. 14).

## Quality bar (from the Stellar build)
- Passes the **Simplicity Test**: the offer is repeatable in one sentence.
- Sells **capacity, not features** — no feature is locked to a tier.
- Pre-empts the budget objection in writing (the assurance line), never negotiates price in the body.
- Tiers map to *involvement*, with a clean 3x recommended middle and a 5–10x anchor top.
