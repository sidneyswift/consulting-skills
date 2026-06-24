---
name: consulting-comms-logger
description: Log a single comms event on a deal/client (you sent, they replied, it was opened, you got a message) and reconcile state. Use on "I sent that", "he replied", "they opened it", "got a reply from {name}", "just emailed {name}", or a screenshot of a sent/received message. Faithfully records the as-sent/as-received text + the engagement signal (open != reply), then updates the deal AGENTS.md, _board.md, any active followups sequence, and whose ball it is. NOT consulting-call-processor (the heavy "new material -> extract + mine" loop for transcripts/notes/results) and NOT consulting-inbox-triage (the radar for what needs a reply across deals) -- this is the light "log one touch and reconcile" move.
---

# Consulting Comms Logger

The fast path for **after** a touch happens. Email skills (`consulting-outbound-email`,
`consulting-followup-sequencer`) own *drafting*; this skill owns *recording the event and
reconciling the deal* once a message has actually gone out or come in. Git is the episodic
memory, so a logged touch must leave the dashboards true.

> Scope one deal. Load only that entity's folder + its live Attio/Gmail (deal-scoped loading).
> **Logging only — never auto-send, never fabricate.**

## Steps

1. **Identify the deal/client.** Locate `pipeline/<stage>/<deal>/` or `clients/<client>/`. If you
   can't tell which deal, ask.

2. **Capture the event faithfully (evidence discipline).**
   - **As-sent / as-received text, verbatim** — what *actually* went out, not the draft you think
     was sent. From a screenshot, transcribe exactly. Note the provenance ("logged from Sid's word"
     vs. "screenshot" vs. "live Gmail"), since a screenshot is stronger than a paraphrase.
   - **Channel + timestamp** (thread subject, LinkedIn, etc.), in the user's timezone.
   - **Engagement signal, read literally:** an **open / read-receipt is engagement, not a reply**;
     a reply is not a commitment. Quote the source (Superhuman receipt, screenshot, live Gmail).
     **Never upgrade a signal into momentum** ("opened in 2 min" = watching the thread, still no
     reply/booking/decision).
   - **Missing detail?** Get it from the **live** source, not a stale snapshot (e.g. a cc email: the
     synced `integrations/gmail/threads/<deal>.json` predates today's reply, so query Gmail live).
     Never guess an address or name.

3. **Decide the ball + posture.** Who owes the next move now (mirror `pull_threads.py` logic): a
   question/ask to you = **needs you**; a forward commitment ("I'll get back to you") = **on them**;
   an open with no reply = **still on them**. When the ball is on them, the posture is **don't
   chase** (let `consulting-lead-temperature` set the objective if a touch is warranted).

4. **Reconcile every state surface** (the actual job):
   - **Deal `AGENTS.md`:** the `## Reality` "where it stands" line, the **📧 Email signal** log
     (append dated), the **Next action**, and the ball. Keep the [MISSING] list honest (resolve what
     this event answered: a timeline, a stakeholder, who-signs).
   - **`pipeline/_board.md`** row (or the client board).
   - **Active `followups.md`:** **STOP the sequence the moment they reply** (mark queued touches
     `VOID`); otherwise advance it. A reply kills the nudge cadence.
   - **New stakeholder surfaced?** Capture them: live email lookup + a **dedup-safe** Attio add
     (check by email before creating; dry-run then apply) and add to the dashboard roster.

5. **Reconcile-on-touch (Attio).** A comms touch usually does **not** change the deal stage, but
   verify live and fix any drift (Attio wins on stage, the repo on artifacts). Don't copy the CRM in.

6. **Report + commit.** Summarize what changed in one or two lines; the commit is the memory. Offer
   to commit (don't auto-commit unless asked).

## Worked example (Stellar, 2026-06-23)
One thread, three touches logged in a session, dashboards kept true throughout:
- **Touch 1 sent 12:43pm ET** -> logged as-sent text; **opened ~2 min later** logged as *engaged, not
  a reply* (open != reply); ball stayed on Morten.
- **Morten replied 12:47pm** (partner-gated, no timeline) cc'ing a new stakeholder (Ryan Peterson)
  -> followups sequence **STOPPED** (Touch 2/3 voided); new stakeholder captured live from Gmail and
  added dedup-safe to Attio; Next action + board + email-signal reconciled; ball read as on him.
- **Reply-all sent 3:19pm** -> ball back on Ryan/partners; "don't chase"; watch date set.

## Related
- Heavy intake (transcript / note / result) -> `consulting-call-processor`.
- "What across all deals needs a reply?" -> `consulting-inbox-triage`.
- Drafting the next touch -> `consulting-followup-sequencer` + `consulting-outbound-email`.
- Posture/score -> `consulting-lead-temperature`. CRM mechanics -> `integrations/attio/crm-sync.md`.
