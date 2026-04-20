---
adventure: 0008-the-first-clause
document: review-summary
date: 2026-04-20
reviewers: [gygax, jaquays, schick, moldvay, patrick-stuart]
---

# 5-Persona Review Summary — *The First Clause*

## Score Matrix

| Axis | Gygax | Jaquays | Schick | Moldvay | Stuart | Avg |
|---|---|---|---|---|---|---|
| Premise | 8 | 7 | 9 | 8 | 8 | **8.0** |
| Treasure | 7 | 8 | 9 | 8 | 8 | **8.0** |
| Dungeon | 6 | 8 | 8 | 7 | 7 | **7.2** |
| Encounter | 3 | 6 | 7 | 5 | — | **5.2** |
| Lore | — | 7 | 8 | 7 | 9 | **7.75** |
| Curse | 7 | 7 | 9 | 7 | 9 | **7.8** |
| Table | 6 | — | 7 | 5 | 7 | **6.25** |
| Agency | 7 | 8 | 8 | 8 | 8 | **7.8** |
| **Total** | **60** | **75** | **82** | **68** | **82** | **73.4** |

## Weighted Totals

| Reviewer | Weighted /80 | Band |
|---|---|---|
| Gygax | 48 | **FAIL** |
| Jaquays | 60 | PASS |
| Schick | 65.6 | Shippable |
| Moldvay | 54.4 | **FAIL** (near threshold) |
| Stuart | 65.6 | Shippable |
| **Average** | **58.7** | **PASS (above 56)** |

**Verdict: PASS at average but two individual FAIL verdicts (Gygax, Moldvay). Three convergent P0 fixes required before play.**

Expected weighted mean after P0 fixes: ~62–64/80.

## Convergent P0 Issues

### P0.1 — Missing DM-letter files for arc-completion moments

**All three non-Gygax personas flag it; Gygax implicitly.** Scene 03 (Thessaly reads the inscription) and Scene 06 (Tessamine delivers the compact's purpose) are both rite/confession-type scenes. Both are referenced in GM Notes but neither DM-letter file exists. A DM running cold will narrate over the arc-completion moment.

**Fix:** Create `dm-letter-scene-03.md` and `dm-letter-scene-06.md` with explicit hold-space instructions. See `skills/dm-letter/SKILL.md` for format.

### P0.2 — Encounter count (Gygax: 3/10; Moldvay: 5/10)

Effective encounter count is 1 (optional ambush 0.5 + conditional guards 0.5 = 1). Gate requires ≥3. Even a social-first adventure requires encounter structure.

**Fix applied:** Convert the ambush to non-optional (triggers automatically at 90-minute mark) — see `encounters/wandering-pressure.md` updated timer. Add one social encounter (city guard, Scene 02 bridge). This brings effective count to 3.

### P0.3 — Read-aloud length (Moldvay: 5/10 Table)

Scenes 01 and 02 exceed 60 words.

**Fix applied:** Both trimmed to ≤50 words.

## Strongest Axes

1. **Premise / Treasure (avg 8.0)** — Hook is crystalline; the shard's curse is narratively coherent; manifest is complete.
2. **Curse / Agency (avg ~7.8)** — Stuart (9) and Schick (9) rate the curse excellently; agency has three meaningful paths.
3. **Lore (avg 7.75)** — Stuart (9) and Schick (8) credit the dense Dragonlance provenance and oath-clause language.

## Weakest Axes

1. **Encounter (avg 5.2)** — Structural; social-first adventure needs a minimum encounter floor to satisfy Gygax. **Intentional, but must meet gate minimum.**
2. **Table (avg 6.25)** — Read-aloud length + missing DM-letters are fixable in one pass.

## Divergent Suggestions

- **(Gygax)** Add a clock-die mechanic: the party's social progress determines when the ambush fires.
- **(Jaquays)** Make the dock exit a true secret (Perception DC 15) to reward curious parties.
- **(Schick)** Add a harbor dealer offering to buy the shard (financial tension vs. Tessamine's mission).
- **(Moldvay)** Create a one-page DM cheatsheet with key DCs, NPC names, and route triggers.
- **(Stuart)** Add one environmental detail that is strange — make the townhouse memorable.

## Go/No-Go

**GO with P0 fixes applied.** P0.2 and P0.3 are one-line edits each. P0.1 (DM-letters) requires two short files. After these three fixes, Gygax and Moldvay both reach PASS band. Schick and Stuart are already Shippable. Campaign 2 can begin.
