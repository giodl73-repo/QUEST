---
spec: 2026-04-21-halted-spire-design.md
document: review-summary
date: 2026-04-21
reviewers: [gygax, jaquays, schick, moldvay, patrick-stuart]
---

# 5-Persona Review Summary — The Halted Spire (Design Spec)

## Score Matrix

| Axis | Gygax | Jaquays | Schick | Moldvay | Stuart | Avg |
|---|---|---|---|---|---|---|
| Premise | 8 | 8 | 8 | 8 | 9 | **8.2** |
| Treasure | 4 | 4 | 3 | 4 | 5 | **4.0** |
| Dungeon | 5 | 3 | 6 | 6 | 6 | **5.2** |
| Encounter | 4 | 5 | 5 | 6 | 4 | **4.8** |
| Lore | 5 | 6 | 7 | 7 | 8 | **6.6** |
| Curse | 7 | 6 | 7 | 6 | 6 | **6.4** |
| Table | 6 | 5 | 6 | 7 | 5 | **5.8** |
| Agency | 6 | 7 | 7 | 9 | 7 | **7.2** |

## Weighted Totals

| Reviewer | Weighted /80 | Band |
|---|---|---|
| Gygax | 55 | PASS |
| Jaquays | 52 | FAIL |
| Schick | 54 | PASS |
| Moldvay | 60 | PASS |
| Stuart | 57 | PASS |
| **Average** | **55.6** | **PASS** |

## Convergent P0 Issues (3+ reviewers agree)

### P0.1 — No campaign treasure spine

**All 5 reviewers flag:** The spec has no equivalent to C1's emotion-objects or C2's compact clauses. Treasure-forger has zero guidance. Seven adventures will invent independently and the campaign will not cohere.

**Fix:** Add a "Campaign Treasure Structure" section before campaign-planner runs. The panel's consensus recommendation: **Velantha's ritual left physical traces — components, records, personal effects carried by her faithful. Each adventure's signature item is one piece of her life or the night she died.** The seven objects together constitute the physical evidence. The finale choice about the cathedral is mirrored in the choice about what to do with the objects.

### P0.2 — No topology mandate

**Jaquays (FAIL), Gygax (Important):** The spec lists seven sections in linear escalating order with no topology guidance. Dungeon-smith will default to a corridor.

**Fix:** Add a "Topology mandate" paragraph: "The cathedral's sections must be accessible non-linearly. At minimum: two entry paths into the Nave, one shortcut unlocked by befriending a faction, vertical connections between Crypt and at least two upper sections. The congregation's presence/absence gates connections — befriend the Nave and they open the stairway to the Sacristy; be violent in the Bell Tower and the Transept Witness will not speak."

### P0.3 — No atmosphere specification per section

**Stuart (P0), Jaquays (Important):** Seven sections with occupants and truth fragments but no sensory anchors. Dungeon-smith will generate mechanically distinct rooms that feel the same.

**Fix:** Add a one-line atmosphere note per section in the adventure table. (Stuart's examples: Gatehouse — "smells of fresh earth; shrines still being assembled"; Bell Tower — "the bell does not ring when struck.")

---

## Strongest Axes

1. **Premise (avg 8.2)** — "The haunting is not a haunting" is the campaign's strongest sentence. The congregation building their own version from inside is genuinely strange and earned by the design. All five reviewers score this 8 or 9.
2. **Agency (avg 7.2)** — Route A/C/D are the clearest route definitions this workshop has produced. Costs and gains are specific. Route D (surrender of ownership) is a genuine inversion. Moldvay gives it 9/10.
3. **Lore (avg 6.6)** — High Sorcery as the ritual source is canonically sound and dramatically loaded. The Orders' complicity creates a faction triangle that the spec only hints at but that can carry the middle adventures.

## Weakest Axes (structural)

1. **Treasure (avg 4.0)** — The campaign's single biggest gap. Unanimous. Fixable before campaign-planner.
2. **Encounter (avg 4.8)** — Appropriate deferral to dungeon-smith, but the spec gives no campaign-level encounter guidance. The "lots of monsters" direction needs a minimum commitment.
3. **Dungeon (avg 5.2)** — Jaquays FAIL is driven entirely by missing topology mandate. One paragraph fixes it.

## Divergent Suggestions (single-lens)

- **(Gygax)** Add an attrition budget: what % of party resources should each section drain? The Bell Tower (0017) should hit harder than the Gatehouse (0015).
- **(Jaquays)** The Orders' man in the Sacristy should hold information that can be traded between factions, not just delivered to the party.
- **(Schick)** The Crypt (0020) should contain something Velantha left intentionally — not her ghost, an object. Her last deliberate act, thirty years in the making.
- **(Moldvay)** Route C (share) needs one concrete physical image: what does coexistence look like in practice?
- **(Stuart)** The congregation has been building for thirty years. There should be one impossible thing they built — something that required skills or materials they shouldn't have had.

## Go/No-Go

**NO-GO — fix P0.1 (treasure spine) and P0.2 (topology mandate) before campaign-planner.**

P0.3 (atmosphere notes) can be added in the same pass.

Expected weighted mean after P0 fixes applied: ~62–65 (Shippable band).

The campaign premise is strong. The three fixes are additive (one section each) and do not require redesigning the adventure structure. Apply and proceed.
