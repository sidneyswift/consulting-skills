# DESIGN — the canonical brand system

**This is the practice's `DESIGN.md` — the brand source of truth** for everything we ship: video,
social graphics, slides, proposals, the dashboard, email headers. Palette, type, logo, and the
footer signature, as reusable CSS plus the rules for using them well. Every house skill pulls from
here — the `consulting-tasteful-design` SKILL.md is how to *apply* the brand; this file is *what* it is.

> **Shared DNA, varied expression.** Pull color/type/logo from this file; let each piece own its
> *composition*. If two pieces look interchangeable, the brief failed — vary the field, layout, and
> dominant element. (Composition templates for stills live in `consulting-graphics`; motion
> translation, the anti-slop checklist, and the pre-ship checklist live in the parent
> `consulting-tasteful-design` SKILL.md.)

## CSS variables (paste into every composition)

```css
:root {
  --ink:#0b1020; --navy:#14254a; --accent:#3f5fb0; --signal:#3d6bff;
  --tint:#f3f6fc; --tint2:#eef2fc; --hairline:#e3e9f5; --dot:#16284c;
  --paper:#ffffff; --mute:#6b7d8f; --on-dark:#dfe5f3;
}
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap');
```

| Font role | Family | Weight | When |
|---|---|---|---|
| Display / headline | `Space Grotesk` | 700 | the big line — the thing read first |
| Body / label / receipts | `Plus Jakarta Sans` | 400–800 | everything else |
| Serif accent | `Instrument Serif` italic | 400 | one pull-quote / editorial moment, occasionally |

**Type scale (1080px canvas reference):** hooks/headlines 72–110px; stat numbers 160–240px; body
24–32px; labels/kickers 16–20px. Scale to width on other canvases.

## The footer (every piece — the brand signature)

Left: Recoup mark + `Sidney Swift`. Right: `recoupable.com`. Adapt color to the background.

```html
<!-- on a LIGHT background -->
<div style="display:flex;justify-content:space-between;align-items:center;font-family:'Plus Jakarta Sans';font-weight:700;">
  <div style="display:flex;align-items:center;gap:11px;">
    <svg viewBox="0 0 223 223" width="26" height="26" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M118.106 41C112.845 41 108.581 45.2558 108.581 50.5056V88.3242C108.581 93.9241 106.846 99.3868 103.613 103.964C98.5169 111.179 90.2239 115.471 81.3785 115.471H57.525C52.2645 115.471 48 119.727 48 124.977V172.304C48 177.554 52.2645 181.81 57.525 181.81H104.894C110.155 181.81 114.419 177.554 114.419 172.304V139.968C114.419 133.432 116.445 127.056 120.218 121.714L120.885 120.77C126.833 112.348 136.512 107.339 146.836 107.339H165.475C170.736 107.339 175 103.083 175 97.833V50.5056C175 45.2558 170.736 41 165.475 41H118.106Z" fill="#0b1020"/></svg>
    <span style="font-size:19px;color:#0b1020;letter-spacing:-0.01em;">Sidney Swift</span>
  </div>
  <span style="font-size:16px;color:#8aa0b6;letter-spacing:0.02em;">recoupable.com</span>
</div>
```
On a DARK background: set the mark `fill="#ffffff"`, the name `color:#ffffff`, the url `color:#9bb2ec`.

## Bold, not boring — the principles (read before composing)

These retire the old "no color / 40% empty / no decoration" rules that made everything forgettable.

1. **Commit to a color field.** Each piece has a dominant field: full-bleed `--ink`/`--navy` (dark,
   high-conviction), or `--paper`/`--tint` (light, scannable). Pale washed-out gradients are banned —
   they read as generic. If you use the dark field, go *all the way* dark; if light, keep it crisp.
2. **One thing is huge.** A headline, a number, or a framework — legible as a thumbnail. Display type
   runs big (see the type scale above).
3. **Color carries meaning.** `--accent` for structure (numbers, labels, rules); `--signal` for *one*
   energy pop per piece (the word/number you want the eye to hit). Never rainbow it.
4. **Make it saveable.** A named framework, an acronym, worked examples with receipts (real numbers).
   Build things people screenshot and re-share — the specificity *is* the design.
5. **Vary expression across a series.** A week of posts should include a dark statement, a light
   framework, a big-stat, maybe a meme/screenshot. Sameness is the failure mode we're fixing.
6. **Texture is allowed, clutter isn't.** The dotwave motif (`--dot`) or a single accent shape can add
   depth. Decoration that doesn't carry meaning still gets cut — but "interesting" is a goal, not a sin.
7. **Mobile-first.** If the hook doesn't land at phone-thumbnail scale, it fails. Test small.
