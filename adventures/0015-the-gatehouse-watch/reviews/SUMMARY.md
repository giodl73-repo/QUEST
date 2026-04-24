---
adventure: 0015-the-gatehouse-watch
document: review-summary
date: 2026-04-21
reviewers: [gygax, jaquays, schick, moldvay, patrick-stuart]
---

# 5-Persona Review Summary — The Gatehouse Watch

## Score Matrix

| Axis | Gygax | Jaquays | Schick | Moldvay | Stuart | Avg |
|---|---|---|---|---|---|---|
| Premise | 8 | 8 | 8 | 8 | 9 | **8.2** |
| Treasure | 6 | 7 | 9 | 7 | 8 | **7.4** |
| Dungeon | 8 | 9 | 7 | 7 | 7 | **7.6** |
| Encounter | 4 | 7 | 6 | 7 | — | **6.0** |
| Lore | 5 | 7 | 7 | 7 | 8 | **6.8** |
| Curse | 5 | 6 | 6 | 6 | 7 | **6.0** |
| Table | 5 | — | 7 | 4 | 7 | **5.8** |
| Agency | 9 | 8 | 8 | 8 | 8 | **8.2** |

## Weighted Totals

| Reviewer | Weighted /80 | Band |
|---|---|---|
| Gygax | 53 | FAIL |
| Jaquays | 62 | PASS |
| Schick | 60 | PASS |
| Moldvay | 53 | FAIL |
| Stuart | 62 | PASS |
| **Average** | **58** | **PASS** |

## Convergent P0 Issues

### P0.1 — Module_binder inlines encounter H2 headers mid-scene

**Gygax + Moldvay flag (one flags it as table-readiness; both are blocked by it):** The compiled `module.md` contains raw `## Type` and `## Setup` headers at H2 level inside scene encounter sections. A DM running cold sees major section headers mid-room-description. Scene 2 and Scene 3 are affected.

**Fix:** In `module_binder._inline_encounter`, strip H1/H2/H3 headers from inlined encounter content by converting them to bold text: `## Type` → `**Type:**`, `## Setup` → `**Setup:**`. One-line change in the inlining loop.

### P0.2 — Encounter pressure insufficient for a level 3 party

**Gygax flags (sole fail axis):** All three encounters are CR ¼. Against a level 3 party of four, no meaningful resources are drained. The adventure delivers approximately 150 XP in combat — below Easy.

**Fix:** Add one **Ghoul** (CR 1, 200 XP, from SRD `reference/srd/monsters-tier1.md`) in the crawlspace under R2/R3. It pre-dates the congregation's arrival; it's why the congregation is uneasy around the grate. Single addition, no new rooms, raises adventure to Easy–Medium range. Gully dwarves' fear of the grate becomes legible.

### P0.3 — Gully dwarves lack setting gloss on first use

**Stuart flags (sole P0); Lore avg 6.8 reflects the gap:** The background section introduces gully dwarves without explaining that they are considered incapable of faith, memory, or sustained purpose by every Krynnish faction. Without this context, the congregation's thirty-year vigil reads as ordinary rather than extraordinary.

**Fix:** Add to the background section: "Gully dwarves — Aghar, in the old tongue — are considered by Krynnish society to be incapable of sustained purpose, faith, or memory. The congregation in this gatehouse has maintained a daily practice for thirty years."

---

## Strongest Axes

1. **Agency (avg 8.2)** — Routes A/C/D are the clearest this workshop has produced. Costs and gains are specific. Route D (surrender the building) is a genuine inversion — restraint is optimal. The portcullis dual-function mechanic is well-designed.

2. **Premise (avg 8.2)** — "The haunting is not a haunting" is a strong premise sentence. Stuart gives it 9/10; all others give it 8/10. The inversion is clean and earned. The logline undersells the central surprise.

3. **Dungeon (avg 7.6)** — Topology passes all gates: loop confirmed, vertical confirmed, conditional shortcut confirmed, two exterior entries, faction repositioning between visits. The flanking approach via R3 yields a meaningfully different first encounter.

## Weakest Axes (structural)

1. **Encounter (avg 6.0)** — All CR ¼ vs level 3 party. No attrition designed in. P0.2 addresses this.

2. **Table (avg 5.8)** — Dragged down by P0.1 (H2 headers mid-scene) and the 61-word read-aloud in Scene 1. Both are module_binder artifacts, not design flaws. The adventure design would score ~7.5 here if the compilation were clean.

3. **Curse (avg 6.0)** — The relic is purely beneficial; the relic test is moral rather than mechanical. No drain on the party from possessing the satchel. Appropriate for this adventure's tone (it is an opener, not a climax) but the workshop's tradition of costly treasure is not maintained.

## Divergent Suggestions (single-lens)

- **(Gygax)** Make the wandering pressure structural hazard more frequent (every 20 min, not 30 min). The dungeon needs some teeth.
- **(Jaquays)** Give two of the four unnamed congregation members one distinguishing behavior each. The congregation should feel like people.
- **(Schick)** Route C needs a physical image: where do the gully dwarves sit during a human service? One sentence makes the coexistence route playable.
- **(Moldvay)** Add "unnamed congregation member — non-combatant, HP 6, follows Mig" to the NPCs section. Completes the encounter reference.
- **(Stuart)** Give Dova (the First-Keeper, five years in R5 before she died) a physical trace in the adventure — a worn spot, a stone she handled daily. Not a ghost, not a stat block.

## Go/No-Go

**NO-GO — fix P0.1 and P0.3 before play; fix P0.2 before play is ideal.**

P0.1 is a module_binder code fix (strip encounter headers during inlining) — 10 minutes. P0.3 is a one-sentence addition to the background section — 2 minutes. P0.2 is an adventure design fix (add a Ghoul to the crawlspace) — 30 minutes.

Expected weighted mean after P0 fixes applied: **~64–66 (Shippable band)**.

The adventure design is strong. The two FAILs are both downstream of compilation artifacts (P0.1) and the encounter pressure gap (P0.2). Neither touches the premise, the relic, the topology, or the agency structure — all of which are solid.
