# Proposal Design + Copy Frameworks

The reusable system behind the Recoup 2-page proposal. Reference this while filling the template.
Distilled from the Stellar Music proposal (2026-06-16). **Keep the structure; swap the slots.**

---

## A. Design framework (the look — don't change these)

**Format.** Single A4 HTML file, 17mm margins, ~720px content column, renders to a 2-page PDF.
Page 1 = the story (problem → outcome → approach). Page 2 = the money (investment → close).

**Type scale.** Doc title 18pt/800; section labels 8pt uppercase tracked, accent blue `#3f5fb0`;
lead paragraphs 11pt/1.6; body 9.5–10pt. Navy ink `#14254a` for emphasis, slate `#252b36` for body.

**Color tokens.**
- Accent blue `#3f5fb0` — labels, step numbers, recommended pill, checkmarks.
- Navy `#14254a` — headings, emphasis, the investment-box border.
- Dark `#0b1020` — the "Where this takes you" panel and the Close box (the two high-conviction moments).
- Tints `#f3f6fc` / `#eef2fc` — panel and recommended-row backgrounds; hairlines `#e3e9f5`.

**Brand furniture (fixed).** Dotwave SVG motif top-right + Recoup wordmark top-left; "Proposal"
kicker; 52px accent rule under the title; running header on page 2; centered footer line.

**The 5-block spine (always in this order):**
1. Two lead paragraphs (the reframe).
2. Two-up panels: "Where {client} is today" (light) vs. "Where this takes you" (dark) — visual
   before/after that makes the gap feel physical.
3. "How we get there" — four numbered steps across one row: **Audit · Own it · Build it · Maintain It.**
4. Investment — three-tier table, recommended row tinted + pill, project band below, assurance line.
5. Close — dark box: one value-anchor sentence + a hairline + 3 numbered next steps.

---

## B. Copy framework (the voice — adapt per company)

### 1. Headline / title
Pattern: name the transformation as something they *own*. Stellar → "Make AI something Stellar
owns, not something that walks out the door." Formula: **"Make {capability} something {Client}
owns, not something that {current failure mode}."**

### 2. Lead paragraph 1 — "the rare thing + the upside"
Open by crediting a *specific, verifiable* win (their proof), then pivot to the upside of going
all-in. Stellar: #1 AI song in Sweden, 25M streams → "making {Client} genuinely AI-native: more
output from the same team, faster than competitors, with an edge to show investors and customers."
Slot = `{{LEAD_PARA_1}}`. Rule: one concrete proof point, then the aspirational reframe. No fluff.

### 3. Lead paragraph 2 — "the real problem (it's ownership)"
Reframe their pain as *capability living in individuals, not the company* — so it walks out the
door. Cite their specific incident if you have one (Stellar: the AI lead who left, 9 months gone).
End on the fix: scattered, person-dependent AI → **infrastructure the company owns** that compounds.
Slot = `{{LEAD_PARA_2}}`. This is the spine of the whole pitch; it makes "owned AI" the hero.

### 4. Now / Next panels (3 bullets each)
- **Now** = blunt, specific pains in their words (no AI ownership; manual reporting; automation
  not nailed). Slots `{{NOW_1..3}}`.
- **Next** = the mirror-image outcomes, bolded lead-in (AI that survives departures; a content
  engine on autopilot; self-serve reporting + IP for the raise). Slots `{{NEXT_1..3}}`.
- Keep them parallel: each Now bullet should have a Next bullet that answers it.

### 5. "How we get there" — fully fixed (names AND sentences)
**Audit → Own it → Build it → Maintain It** is the standard method and the sentences stay the same
on every proposal — don't rewrite them per deal:
- **Audit** — Map how the team uses AI, find your early adopters and who needs upskilling.
- **Own it** — Setup a shared skills + knowledge-base repo with data privacy.
- **Build it** — Turn personal workflows into custom agents and connected systems.
- **Maintain It** — Keep the company, its systems, and its culture cutting-edge and always on.

(Already baked into the template as literal text — no slot to fill.)

### 6. Investment — capacity, not features (the core rule)
Three tiers differ by **how much we build in parallel**, never by which features are "allowed."
- **Advisory $5,000/mo** — audit + roadmap, owned skills repo, custom agents for the top priority,
  weekly calls + unlimited Slack. *One build at a time, they pick it.*
- **Comprehensive $15,000/mo (RECOMMENDED — tint + pill)** — adds a dedicated forward-deployed
  engineer + API/MCP connections; 2–3 builds in parallel. Clean 3x of base.
- **Partnership $30,000/mo** — full team at speed, same-day access, custom platforms end-to-end.
  ~6x anchor (within the 5–10x rule); ≈ the cost of one loaded senior in-house hire.
- **Project band:** state it openly — "big platform builds are fixed-price, typically $50k–$150k
  over 3–6 months, approved before any work starts." Transparency = a higher anchor, not a surprise.
- **Assurance line (always):** month-to-month, no lock-in, most work fits the retainer, **no
  surprise invoices**. This answers the #1 budget objection in writing.
- Only edit tier numbers/features (`{{TIER_*}}`) if this deal genuinely differs from the standard.

### 7. Close box — value anchor + next steps
One dark-box sentence comparing the whole offer to a single cheaper-looking alternative they
already considered. Stellar: "for about the cost of one senior AI hire: a full team and a system
that compounds, cancellable anytime." Slot = `{{CLOSE_ANCHOR}}`. Formula: **"{Client} {owns the
capability} instead, for about the cost of {the one expensive thing they'd otherwise buy}."**
Then 3 fixed next steps: (1) 25-min review call, (2) align the partners/stakeholders, (3) kickoff +
send the team the 5-min AI survey.

---

## C. Fill order (fastest path)
1. Title + leads (para 1 proof, para 2 ownership reframe).
2. Now/Next (write them as matched pairs).
3. "How we get there" — leave as-is (fixed boilerplate, no slot).
4. Confirm tier numbers (usually unchanged) + close anchor.
5. Render, check 2 pages + no stray `{{`.

## D. Do-not list
- Don't lock a feature to a tier. Don't negotiate price in prose. Don't add a 4th tier.
- Don't bury the assurance line. Don't change the 4 step names or the block order.
- Don't invent client facts in the leads — pull proof from the discovery transcript/analysis.
