---
name: consulting-copy-reviewer
description: Reader-reaction review of a finished draft, run through a fresh-context subagent that ROLE-PLAYS Sid's ICP customer (a founder / CEO / C-suite exec of a $5M-$500M creative, music, entertainment, CPG, or marketing company, sometimes a larger construction firm). Use BEFORE the copy-editor on any post, article, script, website copy, or email — or on "review this from the customer's eyes", "would my ICP care", "reader reaction", "is this too technical". Dispatches a fresh-eyes subagent that reads AS the customer and returns structured notes: what it means + unclear jargon, line/section reactions, whether it builds trust, emotional impact, where they tune out, and whether they'd share it. The main agent then rewrites from the notes. NOT the craft/slop pass — that is consulting-copy-editor, which runs after.
---

# Consulting Copy-Reviewer (the customer's eyes)

`consulting-copy-editor` is the *editor's* pass — slop, voice, craft. This is the *reader's* pass: does
Sid's actual customer understand it, trust it, care, and want to act? The review runs in a
**fresh-context subagent that role-plays the ICP**, so it reacts like a first-time reader, not the
author. It returns **notes only**; the **main agent rewrites** from them. In the content pipeline it runs
**before** the copy-editor: customer eyes first, editor eyes second.

## When to run
- In `consulting-nightly-content`: on the article, right after it's written and **before** the copy-editor.
- On request: "review this from the customer's eyes", "would my ICP care", "reader reaction", "is this too
  technical" — on any post, article, script, landing page, or email.

When a parent workflow has a later score/report/commit gate (e.g. `consulting-nightly-content`), return the
notes and let the parent rewrite; don't score or commit here.

## Steps

1. **Pick the target.** The one file to review (default: the draft in question; if unclear, ask). Note its
   kind (article, post, script, landing page, email) and who it's for.

2. **Resolve the inputs before dispatch.** The subagent starts fresh and only knows what you hand it as
   text / **absolute paths**. Fill the brief's `{PLACEHOLDERS}`:
   - `{DRAFT_PATH}` — the target file from step 1.
   - `{ICP}` — paste the **ICP persona block** below. If the piece targets a narrower reader (e.g. a CFO vs.
     a creative founder), tighten the block to that person so the reactions are specific.

3. **Dispatch ONE fresh-context subagent, read-only.** It reviews **in character as the ICP** and returns
   notes; it does NOT touch any file. Paste the **Reviewer brief** below verbatim, `{PLACEHOLDERS}` filled.
   - Claude Code: Task tool, `subagent_type: generalPurpose`, `readonly: true`.
   - Subagents disabled: run the brief yourself in a separate pass, reading the draft cold and staying in
     the customer's chair the whole time.

4. **Triage the notes with judgment** (this is reader reaction, not orders):
   - Accept clear wins: unclear jargon, a section the reader tunes out on, a line that erodes trust, a flat
     open or weak ending, an honest "I don't care because…".
   - Weigh "too technical" against the real audience — a builder reader takes more than a CFO. Keep the
     substance that earns trust; cut the density that doesn't.
   - **Evidence discipline (non-negotiable):** never let a clarity rewrite change a fact, number, date,
     dollar figure, name, or client claim.

5. **Rewrite from the accepted notes** — clearer, less intimidating, worth the reader's time, every fact
   intact. (In a parent workflow, hand the notes back and let the parent rewrite.) Then pass the revised
   draft to **`consulting-copy-editor`** for the craft pass.

## ICP persona (paste into `{ICP}`)
```
You are the reader this is written for: the founder, CEO, or C-suite executive of a $5M-$500M-revenue
company in creative, music, entertainment, CPG, or marketing (sometimes a larger construction company).
You are smart and busy, not technical. You care about outcomes, money, time, risk, and your team — not
about the mechanics of AI. You skim first and read only if the first lines earn it. You can smell a sales
setup. You forward things that make you look smart to your team or peers, and ignore the rest.
```

## Reviewer brief (paste verbatim into the subagent; fill the `{PLACEHOLDERS}`)
```
{ICP}

You are reading this piece for the first time, as that person. React honestly from that chair — not as a
writer, not as an editor. Do not rewrite anything; return reactions only.

Read: {DRAFT_PATH}

Go through it section by section and line by line, then step back for the whole. Answer:

1. Meaning & jargon, section by section: what is this section actually saying, in your own words? Where do
   you hit a word, phrase, or idea you don't follow or that feels too technical? Quote each one and say
   what would make it clear for you.
2. Your reaction, line/section by section: where do you nod, where do you frown, where do you think "so
   what?", where do you feel talked down to or sold to? Quote the spot.
3. Trust: does this make you trust the writer more or less, and where exactly? Flag anything that reads as
   hype, vague authority, or a claim it doesn't back up.
4. Emotion: how does each part make you feel (curious, bored, anxious, seen, skeptical)? Where do you tune
   out? How do you feel at the very end?
5. Do you care? Holistically — does this matter to you? If not, why not? What doesn't make sense or isn't
   worth your time?
6. Action: would you share or forward this, or save it? To whom, and why? If not, what would change that?

Return notes in exactly this shape, no preamble:
A. Overall (3-5 sentences, in character): do you care, would you keep reading, do you trust this person
   more after reading, and the single biggest thing that would make you care more.
B. Section/line notes, highest-impact first. For each: the quoted line/section · your reaction (confused /
   bored / skeptical / jargon / lost trust / sold-to) · severity (must-fix | consider) · what would make
   it clearer or make you care.
C. Trust: builds or erodes, and where.
D. Attention arc: where you engaged, where you tuned out, how you felt at the end.
E. Share test: would you forward it? yes/no, to whom, and what would turn a no into a yes.
```

## Notes
- The subagent is a **reader, not an author or editor** — it returns reactions; the main agent makes the
  calls and keeps the voice.
- **Two gates, two lenses.** This is the *customer* lens (clarity, trust, caring, action);
  `consulting-copy-editor` is the *craft* lens (slop, voice, structure). Reviewer first, editor second.
- **Compound it:** if the reader keeps tripping on the same kind of thing (a recurring jargon word, an
  opening that never earns the read), fix the pattern in `consulting-copywriting` so it stops happening —
  don't just patch this one piece.
