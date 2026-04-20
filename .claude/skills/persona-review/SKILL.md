---
name: persona-review
description: Run the 5-persona design review (Gygax, Jaquays, Schick, Moldvay, Patrick Stuart) against a compiled adventure. Each persona scores on 8 axes; SUMMARY produces weighted aggregate + convergent P0 fixes + divergent suggestions. Replaces the manual review round. Use after module-binder and before play. Produces adventures/<slug>/reviews/<persona>-<date>.md and reviews/SUMMARY.md.
---

# persona-review

Run the 5-persona design review against a compiled adventure. The personas disagree by design — their productive friction surfaces P0 issues that a single reviewer would miss.

## Pipeline position

Post-module-binder, pre-play. Input: `adventures/<slug>/module.md`. Output: `adventures/<slug>/reviews/<persona>-<date>.md` (5 files) + `reviews/SUMMARY.md`.

## Preconditions

- `adventures/<slug>/module.md` exists and is compiled.
- `adventures/<slug>/reviews/` directory may or may not exist (create if missing).
- `personas/playtest-rubric.md` exists (for current rubric version context).

## The Five Personas

| Persona | Design axis | Core question |
|---|---|---|
| **Gygax** | Attrition, temporal pressure, encounter count, player agency | Does the dungeon drain resources honestly? Do players have real choices with real costs? |
| **Jaquays** | Topology, non-linearity, secret connections, factions with dynamic behavior | Can a curious party find more than an incurious one? Is the dungeon alive between visits? |
| **Schick** | Treasure as story, signature item centrality, lore density | Does the treasure *mean* something? Does the room architecture express the object in it? |
| **Moldvay** | Table-readiness, clarity, procedure, accessible language | Can a DM run this cold? Are the read-alouds under 60 words? Are the DCs visible at a glance? |
| **Patrick Stuart** | Atmosphere, the weird, NPC interiority, sensory specificity | Does anything in this dungeon surprise me? Does it have a texture that no other dungeon has? |

Read each persona's worldview before writing their review. The voice must sound like the persona, not like a generic reviewer.

## Scoring Axes (8 per persona, weighted differently)

The 8 axes are the same as the playtest rubric — but scored against the *design*, not the session:

| Axis | What it measures at design time |
|---|---|
| Premise | Hook clarity, emotional specificity, campaign-fit |
| Treasure | Artifact centrality, manifest completeness, curse coherence |
| Dungeon | Topology, non-linearity, sensory cues, branch differentiation |
| Encounter | CR/action-economy, encounter count, wandering-pressure |
| Lore | Setting accuracy, accessibility (first-use glossing), depth |
| Curse | Emotional resonance, creeping cost, narrative symptom specificity |
| Table | Read-aloud length, DC visibility, NPC file completeness, DM-letter presence |
| Agency | Route count (A/C/D), fallback paths, PC decision moments |

Scores are 0–10. Each persona weights the 8 axes differently (see below).

## Persona Weights

| Axis | Gygax | Jaquays | Schick | Moldvay | Stuart |
|---|---|---|---|---|---|
| Premise | 1 | 1 | 1 | 1 | 1 |
| Treasure | 1 | 1 | 2 | 1 | 1 |
| Dungeon | 2 | 3 | 1 | 1 | 1 |
| Encounter | 2 | 1 | 1 | 1 | 0 |
| Lore | 0 | 1 | 1 | 1 | 2 |
| Curse | 1 | 1 | 1 | 1 | 2 |
| Table | 1 | 0 | 1 | 2 | 1 |
| Agency | 2 | 2 | 2 | 2 | 2 |
| **Weight total** | **10** | **10** | **10** | **10** | **10** |

Weighted total = sum(score × weight) for all 8 axes. Max = 100; report as /80 by convention (divide by 1.25).

## Verdict bands

| Weighted /80 | Band |
|---|---|
| ≥ 65 | Shippable — play immediately |
| 56–64 | PASS — one revision pass needed |
| < 56 | FAIL — significant structural issue |

A design that passes all 5 personas at ≥ 56 is table-ready with P0 fixes applied.

## Procedure

### 1. Read the module

Read `adventures/<slug>/module.md` in full. Note:
- Room count, encounter count, topology clues.
- Artifact name, curse, manifest symptoms in dungeon.
- NPC files present (check for Arc-Completion sections).
- Three-route outcomes (A/C/D) — are they named?
- Hint structure — plant/delivery/convergence all specified?
- DM-letter — present if a rite/confession scene exists?

### 2. Write each persona review

Create `adventures/<slug>/reviews/<persona-slug>-<YYYY-MM-DD>.md` per persona:

```markdown
---
adventure: <slug>
persona: <persona-slug>
date: <today>
author: persona-review
weighted-total: <N>/80
band: [Shippable / PASS / FAIL]
---

# <Persona Name> — Review of <Adventure Title>

## Score Matrix

| Axis | Score /10 | Weight | Weighted |
|---|---:|---:|---:|
| Premise | N | W | N×W |
| Treasure | N | W | N×W |
| Dungeon | N | W | N×W |
| Encounter | N | W | N×W |
| Lore | N | W | N×W |
| Curse | N | W | N×W |
| Table | N | W | N×W |
| Agency | N | W | N×W |
| **Total** | | | **N** |
| **Weighted /80** | | | **N/80** |

## Verdict: [Shippable / PASS / FAIL]

## Strongest axes (≥ 8/10)

Cite specific room/scene evidence. Quote if possible.

## Weakest axes (≤ 5/10)

For each weak axis: what specifically is missing and the exact fix.

## P0 issues (blocking — will fail at table without this)

For any axis score ≤ 4/10: name the specific P0 and the fix. If none, write "None."

## Suggestions (non-blocking)

1–3 suggestions in the persona's voice. Non-blocking means the adventure is playable without them.
```

### 3. Write the SUMMARY

Create `adventures/<slug>/reviews/SUMMARY.md`:

```markdown
---
adventure: <slug>
document: review-summary
date: <today>
reviewers: [gygax, jaquays, schick, moldvay, patrick-stuart]
---

# 5-Persona Review Summary — <Adventure Title>

## Score Matrix

| Axis | Gygax | Jaquays | Schick | Moldvay | Stuart | Avg |
|---|---|---|---|---|---|---|
| Premise | N | N | N | N | N | **N.N** |
| Treasure | N | N | N | N | N | **N.N** |
| Dungeon | N | N | N | N | N | **N.N** |
| Encounter | N | N | N | N | N | **N.N** |
| Lore | N | N | N | N | N | **N.N** |
| Curse | N | N | N | N | N | **N.N** |
| Table | N | N | N | N | N | **N.N** |
| Agency | N | N | N | N | N | **N.N** |
| **Total** | **N** | **N** | **N** | **N** | **N** | **N.N** |

## Weighted Totals

| Reviewer | Weighted /80 | Band |
|---|---|---|
| Gygax | N | [Shippable/PASS/FAIL] |
| Jaquays | N | |
| Schick | N | |
| Moldvay | N | |
| Stuart | N | |
| **Average** | **N** | **[band]** |

## Convergent P0 Issues (ALL or MOST reviewers agree)

### P0.1 — <Issue title>

**All N reviewers flag:** <what is missing>

**Fix:** <exact, imperative fix — one edit, one scene>

(Add P0.2, P0.3 etc. as needed. If none: "No convergent P0 issues. Ship.")

## Strongest Axes

1. **<Axis> (avg N.N)** — cite specific evidence.
2. ...
3. ...

## Weakest Axes (structural)

1. **<Axis> (avg N.N)** — whether intentional or fixable.

## Divergent Suggestions (single-lens)

- **(Persona)** suggestion in their voice.

## Go/No-Go

**[GO / NO-GO] with P0 fixes applied.**

Expected weighted mean after P0 fixes: ~N–N.
```

### 4. Never overwrite silently

If review files exist for today, write `<persona>-<date>.v2.md`.

## Output to user

- Score matrix table (inline).
- Verdict for each persona (Shippable / PASS / FAIL).
- Panel average weighted /80.
- P0 convergent issues count.
- Suggested next step: apply P0 fixes, then re-run adventure-lint, then session-runner.

## Scoring discipline

- **Scores are about the design, not the session.** A 10/10 premise means the hook is crystalline, not that the session was fun.
- **Counter-evidence is required for any score ≥ 8.** What would lower it?
- **P0 issues must be specific.** "The table-readiness is low" is not a P0. "Scene 04 has no fallback path if the party refuses the reliquary" is a P0.
- **Personas disagree by design.** If all 5 give identical scores, re-read the module — something was missed.

## Anti-patterns

- Reviews that sound identical across personas.
- P0 issues without a specific fix.
- Scores ≥ 8 without counter-evidence.
- Divergent suggestions framed as blocking issues.
- Skipping SUMMARY (each individual review is incomplete without cross-persona synthesis).
