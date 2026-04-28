# Design Doc — Rui Huang Personal Page

## Design Context

**Subject.** Rui Huang, third-year UESTC undergraduate, Computer Science (Everest Project, ranked 1/164). Currently a research intern at Tencent Hunyuan (Qingyun Program). Active publications in CV/diffusion (CVPR 2026 ×2, AAAI 2025 Oral) and reasoning (P1 / P1-VL with the PRIME-RL group). Already admitted to a PhD program; building this homepage as a long-term, personally satisfying portfolio rather than an admissions artifact.

**Audience.** PhD-track collaborators, mentors, paper readers, and conference acquaintances. Reads on desktop primarily, mobile occasionally.

**Brand personality.** Earnest, well-credentialed, technically broad (vision + reasoning + multimodal). Should signal "serious research, not personal-brand spectacle" — explicitly the opposite of the over-listed, founder/influencer-style page (e.g. Tianxing Chen) that this user did not want to imitate.

**Aesthetic direction.** Reading-Room Minimal, calibrated to closely follow the Weiyang Jin HKU MMLab homepage (`waynejin0918.github.io/home`). User's explicit instruction: "尽量贴近 Weiyang Jin 就行了."

### Reference

From `waynejin0918.github.io/home`:

- **Typography.** `Lato` (300/400/700) for body and UI, `Merriweather` serif for H1/H2/H3 and paper titles. Body 16px / line-height 1.7.
- **Color temperature.** Cool, near-monochrome with two restrained accents: primary `#0056b3` (academic blue), accent `#d82644` (red, used only for the 60px underline below section titles).
- **Spatial density.** Airy. 960px max-width container, 60px between sections, dashed/solid hairline rules between items.
- **Surface treatment.** Almost flat — `border-radius: 6px` on paper thumbnails, shadow `0 8px 24px rgba(0,0,0,0.12)` on the avatar only, social pill backgrounds `#f0f2f5` with translateY hover. No glassmorphism, no gradients, no neumorphism.
- **Layout.** Two-column header (bio text left + 300×300 circular photo right), then single column for all sections. Mobile: header column-reverses (photo on top).
- **Decoration.** A red 60px line under each section title (`::after`), monospace blue pills for News dates, dashed bottom border between Experience items.
- **Animation.** Minimal — hover translate on social pills, hover scale(1.02) on paper thumbnails, color transition on links. No scroll animations.

## Design System

### Tokens

| Token | Light | Dark |
|-------|-------|------|
| `--bg` | `#ffffff` | `#0f1115` |
| `--bg-elev` | `#f9f9f9` | `#171a21` |
| `--text` | `#333333` | `#e5e7eb` |
| `--text-muted` | `#666666` | `#9ca3af` |
| `--text-strong` | `#1a1a1a` | `#f3f4f6` |
| `--primary` | `#0056b3` | `#5aa9ff` |
| `--accent` | `#d82644` | `#ff6b7a` |
| `--link-hover` | `#b32424` | `#ffb1bb` |
| `--border` | `#eeeeee` | `#262a33` |
| `--pill-bg` | `#f0f2f5` | `#1f242d` |
| `--pill-bg-news` | `#eef4fa` | `#0f2030` |

### Typography

- Body: `Lato`, 400, 16px, line-height 1.7
- H1 (name in header): `Merriweather` 700, ~2.8rem desktop / 2.2rem mobile
- H2 (section titles): `Merriweather` 700, 1.75rem
- Paper titles: `Merriweather` 700, 1.15rem
- Dates / tags: `ui-monospace, SFMono-Regular, Menlo, monospace`

### Aesthetic Implementation

- **Layout structure.** Single 960px centered container. Header is `flex` two-column (bio left, photo right, gap 50px), all subsequent sections single column. Mobile breakpoint at 768px collapses header to `column-reverse`.
- **Surface treatment.** Flat with hairline borders. `border-radius: 6px` on paper thumbnails, `border-radius: 50%` on avatar. Single elevation for avatar only (`box-shadow: 0 8px 24px rgba(0,0,0,0.12)`).
- **Typography expression.** Strong hierarchy: serif headings vs sans-serif body. Heading-to-body weight ratio 700/400. Letter-spacing -0.5px on H1 only.
- **Decorative rules.** Allowed: 60px red `::after` under section titles, monospace blue date pills in News, dashed bottom borders between list items, social pill bg with hover translateY(-2px). Forbidden: gradients, glassmorphism, color-shifting borders, drop shadows beyond avatar, full-bleed colored sections.
- **Spatial rhythm.** Airy. 60px between sections, 40px between paper entries, 20px between Experience entries. Container 960px max width keeps lines comfortable for reading.
- **Signature CSS.**

```css
.section-title {
  font-family: 'Merriweather', serif;
  font-weight: 700;
  font-size: 1.75rem;
  border-bottom: 2px solid var(--border);
  padding-bottom: 10px;
  margin-top: 60px;
  position: relative;
}
.section-title::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 60px;
  height: 2px;
  background-color: var(--accent);
}
.news-date {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  background: var(--pill-bg-news);
  color: var(--primary);
  padding: 2px 8px;
  border-radius: 4px;
  font-weight: 700;
}
```

### Overrides

- **Dark mode** is added (PageClaw build spec requires it; Weiyang Jin's page does not have one). Toggle is a small sun/moon button fixed top-right, persists to `localStorage`, defaults to `prefers-color-scheme`. Implementation kept minimal so it does not disturb the reference's clean character.
- **Honors / Awards / Talks / Services** sections are added (Weiyang Jin's page does not have these). They reuse the Experience list pattern (left detail + right-aligned date) so they feel native to the existing visual system.
