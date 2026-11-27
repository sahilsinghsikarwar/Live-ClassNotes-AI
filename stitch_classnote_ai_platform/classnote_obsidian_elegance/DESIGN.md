---
name: ClassNote Obsidian Elegance
colors:
  surface: '#10131a'
  surface-dim: '#10131a'
  surface-bright: '#363941'
  surface-container-lowest: '#0b0e15'
  surface-container-low: '#191b23'
  surface-container: '#1d1f27'
  surface-container-high: '#272a32'
  surface-container-highest: '#32353d'
  on-surface: '#e1e2ec'
  on-surface-variant: '#c7c4d7'
  inverse-surface: '#e1e2ec'
  inverse-on-surface: '#2d3038'
  outline: '#908fa0'
  outline-variant: '#464554'
  surface-tint: '#c0c1ff'
  primary: '#c0c1ff'
  on-primary: '#1000a9'
  primary-container: '#8083ff'
  on-primary-container: '#0d0096'
  inverse-primary: '#494bd6'
  secondary: '#7bd0ff'
  on-secondary: '#00354a'
  secondary-container: '#00a6e0'
  on-secondary-container: '#00374d'
  tertiary: '#c3c0ff'
  on-tertiary: '#1d00a5'
  tertiary-container: '#8582ff'
  on-tertiary-container: '#180092'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#07006c'
  on-primary-fixed-variant: '#2f2ebe'
  secondary-fixed: '#c4e7ff'
  secondary-fixed-dim: '#7bd0ff'
  on-secondary-fixed: '#001e2c'
  on-secondary-fixed-variant: '#004c69'
  tertiary-fixed: '#e2dfff'
  tertiary-fixed-dim: '#c3c0ff'
  on-tertiary-fixed: '#0f0069'
  on-tertiary-fixed-variant: '#3323cc'
  background: '#10131a'
  on-background: '#e1e2ec'
  surface-variant: '#32353d'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.03em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.025em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 26px
    fontWeight: '600'
    lineHeight: 34px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 26px
    letterSpacing: -0.015em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: -0.005em
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0em
  label-md:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.01em
  label-code:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.02em
  label-sm-code:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.04em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-sm: 1rem
  margin: 2rem
  margin-sm: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system targets researchers, university students, and high-performance academics who demand precision, clarity, and rapid synthesis. The aesthetic reflects an engineering-grade, minimalist philosophy rooted in computational clarity and modern craft—evoking confidence, frictionless productivity, and profound technological rigor. 

The style synthesizes modern dark-canvas minimalism with translucent structural depth. It draws from the calibrated functional density of tools like Linear and the typographic restraint and fluid polish of Apple and Stripe. Visual noise is stripped away to foreground academic content, audio wave vectors, and synchronized structural summaries. The primary experience defaults to deep obsidian tones with precision-milled borders, soft ambient bioluminescent indigo accents, and micro-calibrated status indicators.

## Colors

The palette leverages a calibrated dark default canvas built on layered obsidian navy tiers:
- **Canvas Base:** `#0A0D14` (Deep obsidian foundation)
- **Surface Elevation 1:** `#101522` (Sidebars, primary cards, content panels)
- **Surface Elevation 2:** `#171E2E` (Nested surfaces, modal dialogs, flyout controls)
- **Border Definer:** `#232D42` (Subtle 1px structural boundaries)
- **Primary / Core Accent:** `#6366F1` (Electric Indigo for primary actions, focus rings, and active semantic states)
- **Secondary Accent:** `#38BDF8` (Sky cyan for AI synthesis states, streaming completions, and live audio telemetry)
- **Tertiary Accent:** `#4F46E5` (Cobalt indigo for hover states, deep selection backgrounds, and badge tints)

### Neutral Typography Spectrum
- **Text High-Contrast:** `#F8FAFC` (Headings, primary statements, active transcript segments)
- **Text Balanced Muted:** `#94A3B8` (Metadata, unselected tabs, secondary descriptions)
- **Text Low-Contrast:** `#64748B` (Inactive states, timestamp offsets, border subtleties)

### Light Mode Mapping
When flipped to light mode, invert to a warm alabaster base (`#F8FAFC`), pure white surface elevations (`#FFFFFF`), subtle architectural slate borders (`#E2E8F0`), and dense midnight slate typography (`#0F172A`), retaining `#4F46E5` for pristine accent contrast.

## Typography

Typography establishes an analytical, academic hierarchy:
- **Headings (Plus Jakarta Sans):** Geometric yet friendly, lending an authoritative, modern feel to module titles, lecture courses, and executive summaries. Tight negative letter-spacing ensures a unified structural form at large scales.
- **Body & Controls (Inter):** Utilitarian and hyper-legible for sustained reading across long lecture transcriptions, AI synopses, and contextual annotations.
- **Data & Timestamps (JetBrains Mono):** Reserved for lecture duration counters, playback scrubbers, confidence scoring tags, API status nodes, and lecture section IDs.

## Layout & Spacing

The layout is built on a responsive 12-column adaptive fluid grid with strict content ceilings for dense data readouts:
- **Desktop (1280px+):** 12 columns, 1.5rem (`24px`) gutters, 2rem (`32px`) canvas margin. Multi-column pane layout accommodating simultaneous audio playback, live transcription columns, and AI executive summaries. Max workspace container width: `1440px`.
- **Tablet (768px – 1279px):** 8 columns, 1rem (`16px`) gutters, 1.5rem (`24px`) margins. Sidebar transforms into a collapsed rail or slide-over drawer; transcript and synthesis stack into switchable tabs.
- **Mobile (< 768px):** 4 columns, 0.75rem (`12px`) gutters, 1rem (`16px`) margins. Full single-column vertical flow with sticky bottom playback telemetry and audio capture status.

## Elevation & Depth

Visual hierarchy uses a refined dark-surface stacking system reinforced by razor-sharp border highlights and subtle ambient lighting rather than heavy drop shadows:

1. **Base Tier (Ground):** `#0A0D14`. Background canvas across all major route views.
2. **Layer 1 (Card/Container Tier):** Surface `#101522` framed by a 1px solid border of `#232D42`. Inner top-edge highlight using an inset box-shadow: `inset 0 1px 0 0 rgba(255, 255, 255, 0.05)`.
3. **Layer 2 (Overlays / Modals / Hovered Cards):** Surface `#171E2E` with a 1px border of `#334155`. Soft ambient shadow: `0 12px 32px -8px rgba(0, 0, 0, 0.6)`.
4. **Translucent Glass Headers:** Top navbars, sticky scrubbers, and fixed floating command palettes apply `background: rgba(16, 21, 34, 0.75)` with `backdrop-filter: blur(12px)` and a bottom border of `rgba(35, 45, 66, 0.8)`.
5. **AI Active Illumination:** Interactive AI elements utilize a concentrated micro-glow: `0 0 24px -4px rgba(99, 102, 241, 0.25)`.

## Shapes

The design uses a Level 2 (`0.5rem` / `8px` to `0.75rem` / `12px`) roundedness scale, matching the industrial feel of modern pro-grade developer and analytical tooling:
- **Base UI elements:** Buttons, text fields, search bars, and dropdown triggers use `8px` (`0.5rem`).
- **Cards and Panels:** Lecture overview containers, media playback pods, and note segments use `12px` (`0.75rem`) to remain sharp yet approachable.
- **Modals and Drawers:** Elevated canvases utilize `16px` (`1rem`).
- **Badges and Pills:** Audio duration tokens, AI status tags, and segmented steppers use `9999px` full-pill rounding.

## Components

### Buttons
- **Primary:** Solid `#6366F1` background, `#FFFFFF` text, `8px` radius. Subtle inner top stroke (`rgba(255,255,255,0.2)`). Hover: `#4F46E5` with `0 0 12px rgba(99,102,241,0.4)` glow.
- **Secondary:** Surface `#171E2E`, 1px border `#232D42`, text `#F8FAFC`. Hover: Border `#6366F1`, text `#FFFFFF`.
- **Ghost:** Transparent background, `#94A3B8` text. Hover: Background `#101522`, text `#F8FAFC`.

### Chips & Badges
- **Status Pills:** Background `rgba(99, 102, 241, 0.1)`, 1px border `rgba(99, 102, 241, 0.3)`, text `#38BDF8`. Integrated 6px circular pulsing indicator dot for active transcription.
- **Metadata Badges:** Font JetBrains Mono `10px`, background `#101522`, border `#232D42`, text `#94A3B8`.

### Input Fields
- Dark canvas input background (`#101522`), 1px border (`#232D42`), height `40px`, padding `0 12px`.
- Focus state: Border transitions to `#6366F1` with an outer ring of `0 0 0 2px rgba(99, 102, 241, 0.2)`. Placeholder color: `#64748B`.

### Cards & Grouping
- Surface `#101522`, border `1px solid #232D42`, corner radius `12px`. 
- Padding: `space-lg` (`24px`) for primary sections; `space-md` (`16px`) for nested sub-cards.
- Interactive cards elevate on hover with `border-color: #38BDF8` and a subtle `translateY(-1px)` transition (150ms ease).

### Checkboxes & Segmented Controls
- **Checkboxes:** `16px` square, `4px` radius, border `#232D42`. Checked: Background `#6366F1`, stroke icon in pure white `#FFFFFF`.
- **Segmented Steppers:** Encapsulated pill shell (`#101522`, border `#232D42`), inner active thumb (`#171E2E`, text `#F8FAFC`, shadow `0 2px 4px rgba(0,0,0,0.4)`), inactive text `#94A3B8`.

### Specialized Domain Components
- **Audio Waveform Timeline:** Integrated monospaced scrub counter (`JetBrains Mono`), `#232D42` inactive rail, `#6366F1` buffered segment, and dynamic `#38BDF8` frequency bars.
- **Live Transcript Synchronizer:** Inactive phrases colored `#64748B`, transitioning smoothly to `#F8FAFC` with an ambient indigo highlight block when matching audio timestamp position.