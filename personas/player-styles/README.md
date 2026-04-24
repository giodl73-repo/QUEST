---
name: player-styles-readme
description: Emergent player-archetype catalog. Styles are PROMOTED from clustered innovations (3+ entries across ≥ 2 sessions). Empty at start by design.
author: human
created: 2026-04-18
status: empty catalog (no styles yet)
---

# Player Styles — Emergent Catalog

This directory is a catalog of **player archetypes that emerge across playtest sessions**. It is not designed up front. Entries are **promoted** by `playtest-innovation` when ≥ 3 clustered innovations share a theme across ≥ 2 sessions.

## Chronicle's analog

`guides/VOICE-SPECTRUM.md` in `C:\src\chronicle` contains 45+ prose voice registers that emerged from clustered writing innovations — not designed but *discovered*. Chronicle's first voice registers landed at chapter-v1.4 after roughly 15 chapters. Expect similar pacing here: **no player-style is likely to emerge before session 3-5**, and the first few styles will feel tentative.

## Entry Format (when entries exist)

Each entry is a markdown file at `player-styles/<slug>.md`:

```markdown
---
style: <slug>
name: <Descriptive name>
discovered: <YYYY-MM-DD>
promoted-from-innovations:
  - <innovation entry ID 1>
  - <innovation entry ID 2>
  - <innovation entry ID 3>
source-sessions:
  - S01 — <adventure slug>
  - S02 — <adventure slug>
scope: [party-specific / universal]
---

# <Name>

## Definition
What this player-style IS — not a list, a recognition.

## Triggers / Signals
What a session log looks like when this style is active.

## Cross-applicability
Which party archetypes or adventure types this style amplifies (or is undermined by).

## Seeded innovations
(Full list of `playtest-innovations.md` entries that clustered into this style.)

## Play implications
How an adventure should behave when a PC / player exhibits this style. What the module should plan for.
```

## Current Catalog

**2 styles promoted** (as of 2026-04-19, post-S02):

| Slug | Name | Instances | Source sessions |
|---|---|---|---|
| [`sheet-deep-reader`](sheet-deep-reader.md) | The Sheet-Deep Reader | 4 | S01 (3) + S02 (1) |
| [`craft-witness`](craft-witness.md) | The Craft-Witness | 4 | S01 (2) + S02 (2) |

Both promoted simultaneously post-S02 after cluster-trigger (3+ innovations across ≥ 2 sessions) fired. **First-ever promotions.** Chronicle's analog took ~15 chapters before first voice-registers; the QUEST workshop surfaced clusters at session 2. Difference explainable by denser PC sheets + 5-persona weight-spread producing productive disagreement earlier.

## YAGNI Discipline

Do not pre-populate this catalog from imagined player archetypes. The discovery-based approach is the entire point — premature population produces the same thing as never running the loop at all: archetypes that describe *ideas about players* rather than *observations of play*.
