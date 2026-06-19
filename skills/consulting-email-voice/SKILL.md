---
name: consulting-email-voice
description: The house voice + grounding rules for every outbound email (1:1 nudges, broadcasts, follow-ups, newsletter). Use whenever drafting or editing any email. Enforces no em-dashes, short and direct, and reading all context on a person before writing to them.
---

# Consulting Email Voice

Non-negotiable rules for every email this practice sends. `consulting-email-atomizer`,
`consulting-followup-sequencer`, and the newsletter compile all run drafts through these before staging.

## Rules

1. **No em-dashes. Ever.** Never use "—" or "–". Recast the sentence: use a period, comma, colon,
   or parentheses. Before staging, scan the draft and remove every "—"/"–". (This is a global
   writing rule, not just email.)
2. **Short and direct beats longwinded, every time.** Lead with the point in the first line. One
   idea per sentence. Cut throat-clearing ("I wanted to reach out", "hope this finds you well",
   "I'm excited to"). If a word earns nothing, delete it. A 1:1 should land under ~90 words; shorter wins.
3. **Read all context before a personalized email.** Before writing to a named person, read
   everything available about them and their team. Do not draft from a snippet or a single source:
   - **Live Gmail:** `search_threads` for every thread to/from the person *and their colleagues*,
     then `get_thread` for the bodies that matter.
   - **Synced threads:** `integrations/gmail/threads/<deal>.json`.
   - **Deal file:** `pipeline/<stage>/<deal>/AGENTS.md` (or `clients/<client>/`).
   - **Granola notes:** `integrations/granola/Recoup/prospects|clients/<deal>/`.
   Get every name, title, and role right. Then decide **who the email is actually for**: the exec
   sponsor (keep it light, route to the team) vs. the hands-on POC (go deep on their actual pain).
   Target the message and the ask to that person, not to the company in general.

## Pre-send checklist
- [ ] Zero em-dashes.
- [ ] First line states the point.
- [ ] Every name, title, and fact verified against real context, not assumed.
- [ ] Right person, right ask (sponsor vs. POC).
- [ ] One clear, low-friction CTA.

Source: Sid's drafting notes (2026-06-19). Applies on top of every format in `library/email-templates/`.
