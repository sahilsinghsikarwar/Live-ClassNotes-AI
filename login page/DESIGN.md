---
name: Obsidian Kinetic
colors:
  surface: '#0e1320'
  surface-dim: '#0e1320'
  surface-bright: '#343947'
  surface-container-lowest: '#090e1b'
  surface-container-low: '#161b29'
  surface-container: '#1a1f2d'
  surface-container-high: '#252a38'
  surface-container-highest: '#303443'
  on-surface: '#dee2f5'
  on-surface-variant: '#c7c4d7'
  inverse-surface: '#dee2f5'
  inverse-on-surface: '#2b303e'
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
  tertiary: '#ddb7ff'
  on-tertiary: '#490080'
  tertiary-container: '#b76dff'
  on-tertiary-container: '#400071'
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
  tertiary-fixed: '#f0dbff'
  tertiary-fixed-dim: '#ddb7ff'
  on-tertiary-fixed: '#2c0051'
  on-tertiary-fixed-variant: '#6900b3'
  background: '#0e1320'
  on-background: '#dee2f5'
  surface-variant: '#303443'
typography:
  display-hero:
    fontFamily: Plus Jakarta Sans
    fontSize: 56px
    fontWeight: '700'
    lineHeight: 64px
    letterSpacing: -0.03em
  display-hero-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.025em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 26px
    fontWeight: '600'
    lineHeight: 34px
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.015em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 26px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
    letterSpacing: -0.005em
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: 0em
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0em
  label-caps:
    fontFamily: Plus Jakarta Sans
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.08em
  code-mono:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: -0.01em
  tabular-metric:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  margin: 2rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system embodies high-craft academic intelligence, synthesized with the surgical precision of modern product leaders like Linear, Apple, and Stripe. The experience must feel scholarly yet hyper-advanced—transforming chaotic lectures, dense scientific papers, and fragmented research into crystalline, structured cognition. 

The aesthetic is anchored in **Precision Glassmorphism and Structural Minimalism**:
- **Tactile Restraint:** Surfaces avoid garish multi-stop gradients in favor of deep volumetric surfaces, micro-sheen perimeter strokes (1px hairpins), and laser-focused typography.
- **Cognitive Flow:** The interface creates an atmosphere of deep work. It removes sensory noise, providing high legibility and quiet, confident AI surfaces that illuminate context rather than distract.
- **Computational Luminance:** Sub-pixel glowing halos and subtle indigo-cyan ambient flares indicate algorithmic processing, vector indexing, and generative synthesis without breaking focus.

## Colors

The system uses an atmospheric, layered color architecture engineered for prolonged academic study and research, with Dark Mode as the foundational reference and Light Mode maintaining identical optical weight and precision.

### Dark Mode Architecture (Default)
- **Canvas Base:** `#090D16` (Deep Obsidian Void).
- **Surface Level 1 (Panels, Nav):** `#0D121F` (Obsidian Navy).
- **Surface Level 2 (Cards, Modules):** `#131B2E` (Layered Slate Navy).
- **Surface Level 3 (Hover, Modals, Menus):** `#1E293B` (Translucent Structural Slate).
- **Hairline Strokes:** `rgba(255, 255, 255, 0.08)` to `rgba(99, 102, 241, 0.2)` on active frontiers.
- **Text & Foreground:** `#F8FAFC` (Primary Text, 100%), `#94A3B8` (Secondary Details, 65%), `#475569` (Tertiary/Muted Meta, 45%).

### Light Mode Architecture
- **Canvas Base:** `#F8FAFC` (Warm Alabaster).
- **Surface Level 1:** `#FFFFFF` (Pure Studio Crisp).
- **Surface Level 2:** `#F1F5F9` (Subtle Ice Slate).
- **Hairline Strokes:** `#E2E8F0` with elevated focus rings at `rgba(99, 102, 241, 0.3)`.
- **Text & Foreground:** `#0F172A` (Primary Ink), `#475569` (Body Slate), `#94A3B8` (Muted Captions).

### Accents & Semantic Channels
- **Primary Kinetic Accent:** `#6366F1` (Electric Indigo) with hover target `#4F46E5`.
- **Secondary AI Luminance:** `#38BDF8` (Cyan Flare) used for vector tokens, AI transcription chips, and live highlights.
- **Tertiary Synthetic:** `#A855F7` (Amethyst Core) paired with Cyan for gradient mesh glows behind high-impact AI summarization cards.
- **Functional Semantics:**
  - Emerald Verified: `#10B981` (Formula parsed, transcription synced).
  - Amber Warning: `#F59E0B` (Low lecture audio fidelity, missing citations).
  - Rose Critical: `#F43F5E` (Sync failed, invalid syntax).
  - Sky Informational: `#0284C7` (System indexing, academic cross-references).

## Typography

The type ecosystem prioritizes reading stamina, mathematical/academic legibility, and technical elegance:
- **Display & Content Engine:** Built on *Plus Jakarta Sans*, offering humanist warmth combined with geometric structure. Headlines use tight, negative tracking (`-0.015em` to `-0.03em`) for a sculpted, authoritative appearance.
- **Monospace & Metadata Engine:** *JetBrains Mono* is employed for timestamps, transcript synchronizations, token counts, LaTeX equations, and citation keys. Tabular figures (`tnum`) are enabled globally across metrics and timestamps to prevent layout shifting during real-time lecture transcription.
- **Micro-Tracked Overlines:** Category indicators, AI state badges, and structural sections utilize all-caps labels with `+0.08em` tracking and `600` weight to introduce structural hierarchy without visual weight.

## Layout & Spacing

The layout is built on a rigid 8pt base grid with an inner 4pt sub-grid for icons and micro-indicators.

### Grid Models
- **Desktop (>= 1280px):** 12-column layout with `2rem` outer canvas padding and `1.5rem` gutters. The academic workspace adopts a 3-pane structure: Fixed collapsible sidebar (260px), Central dynamic note canvas (fluid, max-width 840px for line-length readability), and Contextual AI Copilot drawer (380px).
- **Tablet (768px - 1279px):** 8-column layout with `1.5rem` outer margins. Secondary panels collapse into overlay glass sheets.
- **Mobile (< 768px):** 4-column layout with `1rem` margins and `0.75rem` gutters. The studio condenses into stacked focus views with a persistent bottom floating utility bar.

### Spacing Philosophy
Rhythm follows content density. Internal card structures use compact, precise steps (`space-sm` to `space-md`), preserving breathing room (`space-lg` to `space-xl`) between modular sections to maintain focus during long research sessions.

## Elevation & Depth

Visual hierarchy uses physical material stacks rather than heavy dropped shadows. Depth is communicated via ambient lighting, refractive boundaries, and layered glass:

- **Level 0 (Canvas Base):** Flat `#090D16` (Dark) / `#F8FAFC` (Light). Completely non-reflective.
- **Level 1 (Docked Containers & Sidebar):** Semi-opaque background (`rgba(13, 18, 31, 0.75)` / `rgba(255, 255, 255, 0.8)`), backed by `backdrop-filter: blur(16px)`. Bordered by a continuous 1px outline: `rgba(255, 255, 255, 0.06)` in dark mode, `#E2E8F0` in light mode.
- **Level 2 (Active Cards & Floating Modules):** Subtle upward ambient lift. In dark mode, a dual-layer shadow: `0 4px 20px -2px rgba(0, 0, 0, 0.5)`, paired with an inset top-edge highlight (`box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1)`).
- **Level 3 (Command Palettes, Popovers & Contextual AI):** Deep volumetric elevation: `0 20px 40px -15px rgba(0, 0, 0, 0.7)`. Outlines adopt a dual sheen with an indigo-to-transparent linear border stroke.
- **AI Aurora Glow (Active Processing):** Dynamic radial backdrop glow centered behind generation zones: `radial-gradient(circle at 50% 0%, rgba(99, 102, 241, 0.15), transparent 70%)`.

## Shapes

The design uses balanced, rounded corner geometry:
- **Base Components (Inputs, Buttons, Pills):** `0.5rem` (8px) for buttons and inputs; circular pills (`9999px`) for status indicators, audio badges, and category labels.
- **Cards & Modules (`rounded-lg`):** `1rem` (16px) delivers modern framing for academic blocks, flashcard stacks, and lecture transcripts.
- **Dialogs & Master Surfaces (`rounded-xl`):** `1.5rem` (24px) for full-scale modal windows, floating command surfaces, and AI generation viewports.
- **Borders:** Consistent hairline thickness of `1px`. Heavy or unrefined borders are forbidden; visual boundaries rely on contrasting fill values and micro-strokes.

## Components

### Buttons
- **Primary (Kinetic Indigo):** Solid `#6366F1` background, white text, 1px highlight border `rgba(255, 255, 255, 0.2)`. On hover: subtle scale `1.01`, brightness increase, and a soft indigo glow (`0 0 16px rgba(99, 102, 241, 0.4)`).
- **Secondary (Obsidian Glass):** Background `rgba(255, 255, 255, 0.05)`, border `1px solid rgba(255, 255, 255, 0.1)`. On hover: background `rgba(255, 255, 255, 0.08)`, border turns into primary indigo tint.
- **Ghost:** Minimal neutral with micro-interaction hover fill (`rgba(255, 255, 255, 0.04)`).

### Badges & Pill Chips
- Pill geometry (`border-radius: 9999px`) with padding `2px 10px`.
- Features an ultra-small status dot (`6px`) with optional pulsing animation for live recordings.
- Uses semantic tints with `10%` alpha backgrounds and matching `20%` alpha stroke (e.g., Sky for `#0284C7` with `JetBrains Mono` label).

### Input Fields & Search Bars
- Background `rgba(13, 18, 31, 0.6)` with 1px hairline border `#1E293B`.
- Integrated shortcut token (`⌘K`) anchored at the trailing edge in `JetBrains Mono`.
- On focus: Outline transitions smoothly to `#6366F1` with an outer focus halo `0 0 0 2px rgba(99, 102, 241, 0.25)`.

### Cards & Knowledge Blocks
- Surface container `#131B2E` with 16px corner radius and hairline perimeter sheen.
- Hover states initiate a subtle 1px border gradient shift from neutral slate to electric indigo.
- Header zones contain micro-actions (Pin, Export, AI Synthesize) that reveal gracefully on container hover.

### Specialized AI & Academic Components
- **Live Waveform & Audio Player:** Dark frosted bar with custom SVG scrubber, tabular duration counter (`00:42 / 58:10`), and real-time audio energy bars tinted with cyan `#38BDF8`.
- **Flashcard & Synthesis Decks:** Multi-layered card stack utilizing depth offsets, glassmorphic surface blur, and directional swipe gestures.
- **Citations & Footnotes:** Subtle superscript tags with micro-popover triggers that display instant source abstracts on hover.