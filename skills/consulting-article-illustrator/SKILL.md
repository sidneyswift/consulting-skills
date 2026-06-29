---
name: consulting-article-illustrator
description: Generate hand-drawn "whiteboard / excalidraw"-style explainer images for articles and posts — the doodle-marker diagrams that sit inside a pillar to explain a concept (a flow, a comparison, a loop, a stack, a hub-and-spoke, a numbered framework). Locked palette: light-grey background, black marker line work + hand-lettering, a single blue accent (no yellow). Two render paths: gpt-image (the hand-drawn vibe) and an HTML+rough.js path (crisp exact text); plans a figure set by article density (~1 per section) and embeds inline. Use when asked to "make an article image / diagram / explainer / infographic", a "hand-drawn / sketch / whiteboard / excalidraw" visual, or to illustrate a blog post / LinkedIn article / pillar. NOT for clean HTML social graphics (use consulting-graphics) or anything animated (use consulting-hyperframes-video).
---

# Consulting Article Illustrator

Hand-drawn **whiteboard explainer diagrams** for articles — the friendly doodle-marker visuals that
make a concept legible inside a pillar post. Produced with **gen AI** (the reference look is itself
AI-generated, not literal Excalidraw), so this skill is a **prompt + style system**, not an HTML kit.

> **Lineage — this skill is a merge of two.** A first version (built on another machine) had the
> **work** — density rules, a two-render-path A/B (HTML vs gpt-image), article-embedding + a preview PDF,
> and a nightly-pipeline hook — but the **wrong style** (white background + yellow badges). Today's build
> nailed the **style** (light grey / black marker / one blue). This skill keeps **today's style** and
> folds in **the other's work** (reconstructed from the recovered `content/03-drafts/2026-06-27-build-for-the-agent/`
> artifacts, since the original plugin commit was stranded/unpushed). It also absorbed the duplicate
> `consulting-article-images`. The parent nightly-content pipeline refers to this skill by name — keep it
> `consulting-article-illustrator`.

- **This skill** = hand-drawn, doodle, marker — concept *explainers* inside articles.
- **`consulting-graphics`** = clean **HTML→PNG** social graphics (statement / stat / framework-blocks).
- **`consulting-hyperframes-video`** = anything animated/motion.

Style lineage + Sid's decoded preference: `swipe/article-image-referances/_index.md` (the references and
the palette correction that defines this skill).

## The locked look (Sid, 2026-06-29)
> "light grey background, black marker, and blue highlights." (Explicitly **not** the references' yellow.)

| Role | Value | Notes |
|---|---|---|
| Background | **light grey** `#e9ebee` | soft, flat — never pure white, never a gradient |
| Line work + lettering | **black marker** | wobbly hand-drawn boxes/arrows; legible hand-lettering |
| Accent / highlight | **one blue** (riso-blue, currently `#2a5bd0`) | highlighter swashes, underlines, numbered circles, checkmarks, accent ticks |
| Yellow | **never** | the single most important correction — no yellow anywhere |

Everything else is the doodle vocabulary: slightly-wobbly rounded-rectangle boxes, hand-drawn solid +
dashed arrows, simple line-doodle icons (brain, gears, laptop, clock, lightbulb, magnet, file, server…),
optional friendly mascot, lots of whitespace, flat — no photoreal, no gradients. Defer exact brand
tokens to the project **`DESIGN.md`**; this skill only fixes the *article-image* palette + style.

## Two render paths (pick per figure)
Both produce the **same hand-drawn look in the locked palette** — they differ in how text behaves:

| Path | How | Best for | Watch |
|---|---|---|---|
| **A — gpt-image** (default) | `GenerateImage` tool, or Higgsfield `gpt-image-2 --image $REF` | the friendly hand-drawn *vibe*; heros; ≤6 elements, short labels | **garbles long/exact text** → keep labels ≤3–4 words |
| **B — HTML + rough.js** (crisp text) | hand-coded HTML using rough.js sketchy shapes + a handwriting font, rendered HTML→Playwright PNG (`references/html-figure-template.html`) | **exact** labels, numbers, code, many elements, repeatable series | more effort per figure |

> This is the recovered A/B ("Excalidraw vs gpt-image") — resolved: **vibe → A, text-precision → B**, both
> in the locked palette (the old build's white+yellow is replaced). Don't fall back to a *clean* vector
> chart; Path B stays hand-drawn via rough.js.

## Density & placement (how many, where)
- **~1 diagram per major section/concept.** A 4-section pillar → ~4 figures (the `build-for-the-agent`
  pillar is the worked example); a single-idea post → **1 hero** diagram. Cap **~4–6** per article.
- **Place each at its section break**, right after that section's point lands.
- **Lead concept → strongest archetype** (a comparison or a flow usually reads fastest).
- **Embed inline** in the article: `![alt](images/<concept>.png)`. For a multi-figure pillar, assemble a
  quick **preview** (the article with figures inline → HTML/PDF) to sanity-check the set before publish.

## Workflow
1. **Plan the figure set.** Read the draft; list its major sections; per **Density & placement** decide
   the concept + archetype for each (≈1 per section; single-idea post → 1 hero). One idea per figure.
2. **Per figure, pick the render path** (A gpt-image for vibe, B HTML+rough.js for exact text).
3. **Make it:**
   - *Path A* — prompt = **style block** + **archetype block** with real labels
     ([references/prompt-kit.md](references/prompt-kit.md)); generate via `GenerateImage`, or Higgsfield
     `gpt-image-2 --image $REF` for tighter style-matching. Landscape ~3:2 in-article (1:1/4:5 if also a post).
   - *Path B* — start from [references/html-figure-template.html](references/html-figure-template.html),
     fill labels, render `npx playwright screenshot --viewport-size="1024,683" file.html out.png`.
4. **Run the bar** (below). Regenerate/fix on **any yellow**, white (not grey) background, garbled text,
   or a clean (non-hand-drawn) chart. Path A text fidelity is the weak spot → labels ≤3–4 words, or use Path B.
5. **Save + embed:** write each to `content/03-drafts/<YYYY-MM-DD-slug>/images/<concept>.png` (the piece's
   own bundle — `content/AGENTS.md`) and embed inline at its section break. Multi-figure pillar → assemble a
   **preview** (article + figures → HTML/PDF) to review the set. Scratch/tests → `content/_work/article-images/`.

## Layout archetypes
| Archetype | Use for | Shape |
|---|---|---|
| **Flow / pipeline** | a process, before→after, a path | 2–4 boxes left→right joined by arrows; dash + blue-highlight the pivotal box |
| **Comparison** | X vs Y, old vs new, tool vs system | vertical split; two headings (blue underline); blue-highlight pill verdict under each |
| **Cycle / loop** | a compounding/repeating system | 4–6 boxes in a ring, curved arrows, blue numbered circles |
| **Stack / layers** | a layered architecture | stacked rows + a left brace label; blue-highlight the key layer |
| **Hub-and-spoke** | one core + its parts | center node + satellite boxes on connectors |
| **Framework** | a named N-part model, inputs→output | numbered rows (blue circles) between a "messy inputs" cluster and a clean "output" |

## The bar — check every render before showing
- [ ] **Light-grey** background (not white), flat?
- [ ] **Black marker** line work + legible hand-lettering (labels spelled correctly)?
- [ ] **Blue** the *only* accent — and **zero yellow**?
- [ ] Hand-drawn feel — Path A doodle **or** Path B rough.js sketch (never a clean vector chart)?
- [ ] One clear idea, lots of whitespace, reads at article width?
- [ ] On-brand vibe vs the references (`swipe/article-image-referances/`) and `samples/`?

Fail any box → don't ship it; fix the prompt and regenerate.

## Samples (locked exemplars)
`samples/` holds approved renders to match against: `flow.png`, `compare.png`, `cycle.png` (Path A,
gpt-image), plus `html-figure-example.png` (Path B, rough.js). Worked multi-figure pillar:
`content/04-published/2026-06-24-the-skill-is-the-easy-part/images/` (4 figures, one per section).

## Nightly pipeline hook
The `consulting-nightly-content` engine can **auto-illustrate** a staged pillar: apply **Density &
placement** (≈1 figure per section, Path A default), save into the draft's `images/`, embed inline, and
leave it staged for review (never auto-publish). This is the integration the earlier build wired in;
re-add it there when wiring nightly illustration back on.

> **Taste authority:** `consulting-tasteful-design` + `DESIGN.md` govern brand look across every medium;
> this skill is their hand-drawn-explainer implementation. Keep it bold and friendly, never yellow.
