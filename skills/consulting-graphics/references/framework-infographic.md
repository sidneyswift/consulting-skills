# Template: Framework Infographic

The "save this" teaching graphic: a big "How to [outcome]" title, a **named acronym framework**, and
**worked examples** below. People save and re-share these (reach beyond followers) and they double as
lead magnets. Reverse-engineered from a top operator's system — evidence:
`positioning/swipe/posts/magali-dereu/ANALYSIS.md` (images `18-1` STORM, `60-1` PLACE, `46-1` flowchart).

**Configurable values:** `BRAND_NAME` (footer left) and `BRAND_TAGLINE` (footer right) come from
`~/.config/sid/identity.md`. The framework letters, labels, and examples are the content you pass in.
Pair this with a post from `consulting-linkedin-post-architect` (the teaching archetype).

## Visual Identity
- **Background:** warm cream `#FBF1EC`.
- **Primary accent (titles, header bands):** burnt orange `#F2683C`.
- **Color-coded blocks (rotate across rows):** purple `#E9D5FF` · blue `#DBEAFE` · green `#D1FAE5` ·
  yellow `#FEF3C7` · pink `#FCE7F3` · orange-tint `#FFE0D2`.
- **Cards:** white `#FFFFFF`, 2px border in the row's accent color, ~18px radius.
- **Text:** near-black `#1A1A1A`; muted `#6B6B6B` for sub-labels.
- High-contrast and bold — the opposite of `elegant-founder`'s minimalism. Dense but organized in cards.

## Typography
| Role | Font | Weight | Usage |
|------|------|--------|-------|
| Title | Poppins | 800 | "How to [outcome]" — huge, orange |
| Subtitle (parenthetical) | Poppins | 500 | black, under the title |
| Acronym letters | Poppins | 800 | the big S T O R M / P L A C E letters |
| Block labels | Poppins | 700 | the word each letter stands for |
| Body / examples | Inter | 400/600 | descriptions + worked examples |

```
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;700;800&family=Inter:wght@400;600&display=swap');
```

## Dimensions & formats
Default **1080 × 1350 (4:5)** — the highest-reach LinkedIn feed size and tall enough for a framework +
examples. For a longer framework, go **1080 × 1440** or split into a carousel (one framework idea per
slide). See [dimensions.md](dimensions.md). These graphics are portrait and text-dense — that's the format.

## Layout (top → bottom)
1. **Title block** (top, ~7% margins): "How to [specific outcome]" in orange Poppins 800, ~72–84px,
   2 lines max. A black parenthetical subtitle under it (~28px) — e.g. "(Plug this into AI and get a
   post in minutes)".
2. **Framework band:** an orange-tint header strip with a centered label ("The Framework" / "The Post
   Framework"), then a white card containing the **acronym row** — each letter big, with its label and
   a one-line description in a column. 4–6 letters across (wrap to 2 rows if >5).
3. **Examples band:** an orange header strip ("Examples" / "Real Examples"), then **worked examples** in
   color-coded cards — either a stacked list (numbered, each a different pastel) or 2–3 columns
   (e.g. Personal / Expertise / Sales). Put a **proof number** on examples where possible ("303K
   impressions").
4. **Footer:** `BRAND_NAME` left, `BRAND_TAGLINE` right (~16px, muted) — on every graphic for recognition.

## HTML Template Shell
```html
<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;700;800&family=Inter:wght@400;600&display=swap');
  * { margin:0; padding:0; box-sizing:border-box; }
  body { width:1080px; height:1350px; position:relative; overflow:hidden;
         background:#FBF1EC; font-family:'Inter',sans-serif; color:#1A1A1A; padding:64px 72px; }
  .title { font-family:'Poppins'; font-weight:800; font-size:78px; line-height:1.02; color:#F2683C; }
  .subtitle { font-family:'Poppins'; font-weight:500; font-size:28px; margin-top:14px; }
  .band-label { font-family:'Poppins'; font-weight:700; font-size:34px; text-align:center;
                background:#F9C7B3; color:#1A1A1A; border-radius:14px; padding:12px; margin:28px 0 16px; }
  .card { background:#fff; border:2px solid #F2683C; border-radius:18px; padding:24px; }
  .acro { display:flex; justify-content:space-between; gap:14px; }
  .acro .col { flex:1; }
  .acro .letter { font-family:'Poppins'; font-weight:800; font-size:56px; }
  .acro .lab { font-family:'Poppins'; font-weight:700; font-size:20px; margin-top:4px; }
  .acro .desc { font-size:17px; color:#444; margin-top:6px; }
  .ex { border-radius:14px; padding:18px 20px; margin-top:14px; font-size:18px; }
  .footer { position:absolute; bottom:36px; left:72px; right:72px; display:flex;
            justify-content:space-between; font-family:'Poppins'; font-weight:600; font-size:16px; color:#6B6B6B; }
</style></head>
<body>
  <div class="title">How to [OUTCOME]</div>
  <div class="subtitle">([the promise / how to use it])</div>

  <div class="band-label">The Framework</div>
  <div class="card acro">
    <!-- repeat .col per letter; rotate accent colors -->
    <div class="col"><div class="letter" style="color:#7C3AED">S</div><div class="lab">Stuck</div><div class="desc">Pain that stops the scroll.</div></div>
    <div class="col"><div class="letter" style="color:#2563EB">T</div><div class="lab">Thirst</div><div class="desc">What they wanted.</div></div>
    <div class="col"><div class="letter" style="color:#059669">O</div><div class="lab">Obstacle</div><div class="desc">Why they were stuck.</div></div>
    <div class="col"><div class="letter" style="color:#D97706">R</div><div class="lab">Revelation</div><div class="desc">The shift.</div></div>
    <div class="col"><div class="letter" style="color:#DB2777">M</div><div class="lab">Mirror</div><div class="desc">New reality + proof.</div></div>
  </div>

  <div class="band-label">Examples</div>
  <div class="ex" style="background:#E9D5FF">[Worked example 1 + proof number]</div>
  <div class="ex" style="background:#DBEAFE">[Worked example 2 + proof number]</div>
  <div class="ex" style="background:#D1FAE5">[Worked example 3 + proof number]</div>

  <div class="footer"><span>BRAND_NAME</span><span>BRAND_TAGLINE</span></div>
</body></html>
```

## Rendering
```bash
npx playwright screenshot --viewport-size="1080,1350" "file:///abs/path/infographic.html" "/abs/path/infographic.png"
```
If the content overflows 1350px, raise the height (e.g. 1080×1440) or split into a carousel.

## Quality Checklist
- [ ] Title is the biggest element, orange, one clear outcome
- [ ] Framework is a memorable **acronym**; each letter has a label + one-line description
- [ ] Examples are **worked** (real, specific) — not restatements of the framework
- [ ] Proof numbers on examples where available
- [ ] Color-coded blocks are consistent and legible (text passes contrast on its pastel)
- [ ] `BRAND_NAME` + `BRAND_TAGLINE` footer present
- [ ] Reads at phone-thumbnail scale; nothing clipped at the canvas edge
- [ ] Voice/claims cleared by `consulting-copywriting` + evidence discipline (no invented numbers)
