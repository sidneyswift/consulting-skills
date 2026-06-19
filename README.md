# Skills — Reusable Capabilities

> Rule of the practice: **anything we do more than once becomes a skill.**

Each skill is a folder with a `SKILL.md` (frontmatter `name` + `description`, then steps).
Authored here → packaged into a plugin → installed → triggers non-deterministically by description.
See `_packaging/README.md` for the lifecycle and `SKILL-ROADMAP.md` for the full catalog + priorities.

## All skills (27)

**Spine / orchestration**
- `consulting-call-processor` — auto-manage loop: ingest any new material end to end
- `consulting-system-auditor` — reconcile filesystem ↔ CRM, surface a punch list

**Sales & pipeline**
- `consulting-lead-intake` — triage + qualify a new lead
- `consulting-discovery-analysis` — analyze a discovery call, qualify the buyer
- `consulting-pricing-builder` — three-tier options, 5-10x anchor
- `consulting-proposal-drafting` — situational-assessment proposal (content/structure)
- `consulting-proposal-designer` — branded 2-page proposal HTML→PDF (design + copy frameworks)
- `consulting-followup-sequencer` — timed follow-up cadence
- `consulting-objection-handler` — tailored objection responses
- `consulting-deal-stage-mover` — advance a deal, keep folders/board/CRM in sync

**Content flywheel**
- `consulting-content-extraction` — mine transcripts into insights + content
- `consulting-content-idea-generator` — multi-tweet test variants
- `consulting-content-drafter` — idea → publish-ready draft (AIDA + title formula)
- `consulting-friday-review` — weekly content + system ritual
- `consulting-faq-builder` — recurring answer → canonical FAQ

**Client success**
- `consulting-client-onboarding` — stand up a won client
- `consulting-quarterly-value-review` — QBR that drives renewals + proof
- `consulting-testimonial-capture` — draft + request testimonials
- `consulting-case-study-builder` — delivered work → case study
- `consulting-expansion-spotter` — land-and-expand opportunities

**Business ops**
- `consulting-sow-generator` — SOW under the MSA
- `consulting-invoice-generator` — invoice per payment structure
- `consulting-metrics-updater` — refresh dashboard + metrics
- `consulting-ip-register-updater` — log reusable IP

**Positioning & meta**
- `consulting-positioning-refiner` — sharpen the message
- `consulting-market-scanner` — niche intel + buying signals
- `consulting-skill-packager` — bundle skills into an installable plugin

## Make them auto-trigger
They're authored as files now. Run `consulting-skill-packager` (or the `create-cowork-plugin`
skill) to bundle `skills/` into a plugin, push to GitHub, and install — then they fire by description.
