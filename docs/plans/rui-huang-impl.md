# Implementation Plan — Rui Huang `index.html`

Single-file static HTML. No build step. Uses Google Fonts (Lato + Merriweather) and FontAwesome 6.4 from CDN. All paper thumbnails reuse existing files in `images/`.

## Tasks

1. **Boilerplate & meta**
   - `<!doctype html>`, `<html lang="en">`, viewport meta, `<title>Rui Huang | UESTC</title>`
   - Preconnect Google Fonts; load Lato (300/400/700) + Merriweather (700)
   - Load FontAwesome 6.4 from `cdnjs`
   - Load Simple Icons SVG inline-fetched (no external dependency for the 4 social icons we need)

2. **CSS variables and theme system**
   - Define `:root` with light tokens and `:root[data-theme="dark"]` with dark tokens
   - On boot: read `localStorage.theme`, fallback `prefers-color-scheme`
   - Theme toggle button fixed top-right, swaps between sun/moon

3. **Container & global typography**
   - `.container { max-width: 960px; margin: 40px auto; padding: 0 20px; }`
   - Global font: Lato 16px / 1.7
   - Headings: Merriweather 700
   - Links: primary blue, hover red

4. **Header (`.profile-header`)**
   - Flex row, gap 50px, bottom border 1px var(--border), padding-bottom 50px, margin-bottom 60px
   - Left (`.bio-text`):
     - H1 "RUI HUANG" (uppercase, Merriweather, ~2.8rem)
     - `.role-title`: "B.S. in Computer Science, Everest Project · UESTC"
     - Lines: current internship at Tencent Hunyuan, advised by Tianyu Pang
     - `.contact-info`: Email
     - `.social-links`: Email / Scholar / GitHub / LinkedIn / ORCID / CV (rounded pills with FontAwesome icons)
     - `.highlight-box`: short interest statement and openness to collaboration
   - Right (`.profile-image-container`): 300×300 circular avatar from `images/RuiHuang.png`, white border 4px, shadow

5. **Section: Biography**
   - One paragraph: who, where, what research, what next

6. **Section: News**
   - `<ul style="list-style:none;padding:0">` with `<li>` entries
   - Each: `<span class="news-date">YYYY/MM</span>` + content
   - 6 most important entries visible; remaining wrapped in `<details>` with summary "Show more"

7. **Section: Experience**
   - `.experience-list` (list-style:none)
   - 3 entries, reverse-chronological: Tencent Hunyuan → Shanghai AI Lab → CUHK MMLab
   - Each `.experience-item`: `.exp-details` (institution + advisor + 1-line topic) and `.exp-date` (right-aligned)

8. **Section: Selected Publications**
   - Caption line: `(* equal contribution; † corresponding author; ‡ project leader)`
   - Repeating `.publication` blocks: `.publogo` (180px) + `.pub-content` (title link, authors with self bold, venue tag, links row)
   - Use existing thumbnails: `images/D2C.png`, `L2P.png`, `WFANet.png`, `CoTImage.png`, `P1.png`, `P1-VL.png`, `UniVA.png`, `COLNet.png`
   - For 2 IEEE TII/TSE entries that lack thumbnails, render in a compact `.compact-pub` block (no logo)

9. **Section: Education**
   - Single experience-item: UESTC, Everest Project, B.Eng. Computer Science, GPA + ranking line, dates right

10. **Section: Honors & Awards**
    - List style identical to Experience: bold title + small detail + year right
    - Top 6 entries

11. **Section: Competition Awards**
    - Same list style, 5 entries

12. **Section: Talks & Reports**
    - Same list style, 4 most relevant items

13. **Section: Services**
    - 2 plain bullets (Reviewer AAAI 2026, Co-Founder UESTC AI Club)

14. **Footer**
    - Subtle line with year + small "Built with PageClaw" credit

15. **Responsive (≤768px)**
    - Header `column-reverse`, photo on top
    - `.publication` flex-direction column, thumbnail full width max 320px
    - `.experience-item` column, date moves below
    - Theme toggle stays accessible

16. **Verification checklist**
    - [ ] Hover/focus states on every interactive element
    - [ ] At least 3 typographic levels (H1 / section title / paper title vs body)
    - [ ] No horizontal scroll at 375px or 1200px
    - [ ] All `images/*.png` paths resolve from repo root
    - [ ] `## Links` rendered as icon pills (not bare text)
    - [ ] Aesthetic style from design doc reflected: red accent line, blue news pills, dashed dividers
    - [ ] Dark mode toggle works, persists, respects system pref on first load

## File output

`index.html` at repo root (single file, no build step).
