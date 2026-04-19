---
adventure: 0002-the-bone-collector-trap
author: adventure-lint
created: 2026-04-18
baseline: pre-module-binder; first lint pass
---

# Lint Report — The Bone-Collector Trap

Pre-module-binder gate validation. Rubric version: **v1.1** (target at design time).

## Summary

- ✗ **2 violations** (must-fix before `module-binder`)
- ⚠ **3 warnings** (fix recommended)
- ✓ **27 passed**

## Per-Lens Scorecard (baseline, pre-fix)

| Lens | Passed | Failed |
|---|---|---|
| Jaquays (topology) | 7 | 0 |
| Gygax (pressure + agency) | 5 | 0 |
| Stuart (atmosphere) | 6 | 0 |
| Schick (treasure framing) | 3 | 0 |
| Moldvay (table-readiness) | 6 | 2 |

Moldvay lens is the only one with violations — both from the same failure mode: read-aloud length discipline.

## Violations (must-fix)

### ✗ Moldvay — Scene 06 read-aloud exceeds 60-word cap

**File:** `rooms/06-reliquary-vault.md`
**Section:** "Read-aloud"
**Measured length:** ~82 words.
**Cap:** 60 words.
**Issue:** The read-aloud merges the room description and Pella's description into one block. The climax deserves clean delivery; an 82-word read-aloud under DM pressure will get paraphrased at the table.
**Fix:** Trim to ~50-55 words. Keep the three key images: the shelf of silver-bound skulls, Keloth standing, Pella bound on the altar.

### ✗ Moldvay — Scene 07 read-aloud exceeds 60-word cap

**File:** `rooms/07-cell-block.md`
**Section:** "Read-aloud"
**Measured length:** ~64 words.
**Cap:** 60 words.
**Issue:** Barely over the cap. The prose is carrying a single beat too many.
**Fix:** Tighten by one sentence. Cut redundant description of the empty cells.

## Warnings (should-fix)

### ⚠ Read-alouds at the Moldvay edge

Scenes 02 (pursuit), 03, 05 are at ~58 words each. Under cap but tight. If any additional edit adds a phrase, they will fail. Keep vigilance on any future revision pass.

### ⚠ Encounter count at threshold

**Measured:** 4 proper encounters (trap-ambush, stable-yard patrol, vault-approach guard-post, vault-climax) plus wandering-table rolls.
**Required:** ⌈7 rooms / 2⌉ = 4.
**Status:** Passes by exactly 0.

Consider promoting the Cell-Block Alert-patrol (Sub-encounter C in `stronghold-guards.md`) from conditional to routine to give a +1 margin. Otherwise, if the party takes the stealth path entirely (well → cell-block → vault), they may bypass Sub-encounters A and B, leaving the session with only the Howl-Stones and Vault fights. That would drop effective encounter count to 2 in stealth-playthrough.

### ⚠ Stealth-playthrough coverage

A party that rolls well on:
- Stealth at Howl-Stones (DC 13)
- Investigation in Stable Yard (DC 13 finding the well)
- Climb DC 10 silently down the well
- Bypass Cell-Block Alert (not yet present)

...will reach the Vault with zero prior combat. Rubric-wise this is fine (they earned it). But the session's pacing depends on the Vault-climax being substantial, which the design handles well. No change needed; flagged for awareness.

## Passing gates (sample)

### Jaquays (topology) — 7/7

- ✓ Map has loop: [5]→[6]→[7]→[5] via iron door.
- ✓ Vertical: stair [3]→[5] + well-shaft [4]↔[7].
- ✓ ≥2 paths to climax: frontal via [5], stealth via well-[7].
- ✓ Shortcut: the well (earned via Investigation DC 13 on straw pile).
- ✓ Branch cues distinguished: stair (visible), well (hidden under straw; deliberate discovery).
- ✓ Inhabitant dynamic behavior: patrol every 10 min, Alert status escalation, Pella's off-screen distraction (Wandering 5), Keloth's surrender-at-half-HP.
- ✓ Multi-location structural variety: wilderness + discovery + trap + stronghold vs. #0001's single-dungeon delve.

### Stuart (atmosphere) — 6/6

- ✓ Memory Fragment in every room's GM Notes (Scenes 01-07; 7/7).
- ✓ Manifest exists: `treasures/reliquary-manifest.md`.
- ✓ ≥3 manifest symptoms in dungeon: **6 symptoms** distributed across 6 rooms (over-delivery).
- ✓ Presence/Desire expressed in ≥1 room: Scene 06 expresses the reliquary's warming + chiming.
- ✓ Per-PC reception documented in each room's GM Notes.
- ✓ Inter-PC chain setup in Scene 06 climax (Aelric's attunement decision chains to Grom/Thera/Kessa).

### Schick (treasure framing) — 3/3

- ✓ Every treasure has a room citing it.
- ✓ Reaction moment on artifact removal: five reliquaries dim by one degree when Varran-reliquary is lifted.
- ✓ Incidental items purpose-tagged: Purpose column in `treasures/minor-loot.md`.

### Gygax (pressure + agency) — 5/5

- ✓ Wandering-pressure.md exists.
- ✓ Proper encounter count ≥ threshold.
- ✓ ≥2 retrieval paths for central artifact: Accept / Refuse / Negotiate / Destroy (via Grom).
- ✓ Post-recovery ≥3 outcomes: Attune / Destroy / Keep unattuned / Return to Council.
- ✓ Central artifact forces a meaningful resource decision (memory economy).

### Moldvay (table-readiness) — 6/8 (2 violations)

- ✓ Every DC inline with hazard.
- ✓ Every NPC named in premise has `npcs/<slug>.md` (Pella, Keloth, Mensa; Brother Laen in #0001's npcs; Wena is mentioned-only).
- ✓ Non-statted entity interaction rules: Pella has stats; Memory-Minute has rules in reliquary.md.
- ✓ No duplicate retrieval options.
- ✓ premise.md ≤ 80 lines.
- ✓ Critical SRD rules to be inlined on compile (attunement, paralyzed, exhaustion).
- ✗ **Scene 06 read-aloud > 60 words.**
- ✗ **Scene 07 read-aloud > 60 words.**

## Strongest Recommended Fix

**Apply the two read-aloud trims inline.** Both are under five minutes of editing. After the fix, re-run lint (should return zero violations) and proceed to `module-binder`.

## Next Actions

1. ✓ Apply the 2 read-aloud trims to Scenes 06 and 07.
2. Re-run lint (optional, since both fixes are unambiguous).
3. Proceed to `module-binder` → compile `module.md`.
4. Optional: 5-persona design review before S02.
5. Run S02 — Varduin Muster on #0002 rev 1.
