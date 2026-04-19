---
adventure: 0001-tomb-of-the-silver-rose
author: adventure-lint (human-simulated, 2026-04-18)
created: 2026-04-18
baseline: post-initial-build, post-persona-review, pre-revision
---

# Lint Report — Tomb of the Silver Rose

First-ever run of `adventure-lint` against adventure #0001, baselined before the convergent-suggestion revisions are applied.

## Summary
- ✗ **10 violations** (must-fix before re-running module-binder)
- ⚠ **3 warnings** (fix recommended)
- ✓ **14 passed**

## Per-Lens Scorecard (baseline)

| Lens | Passed | Failed |
|---|---|---|
| Jaquays (topology) | 4 | 2 |
| Gygax (pressure + agency) | 3 | 0 |
| Stuart (atmosphere) | 1 | 4 |
| Schick (treasure framing) | 2 | 1 |
| Moldvay (table-readiness) | 4 | 3 |

Stuart lens is the worst-hit — predictable, given his weighted-score lead was not echoed by compliance with the *mechanisms* he cares about. The visible symptoms were there in prose; the gates show they were not *systematic*.

## Violations (must-fix)

### ✗ Jaquays — Room 02: branches not distinguished
**File:** `rooms/02-antechamber-of-tears.md`
**Section:** "Features"
**Issue:** east and west archways are described identically. Parties have no sensory reason to pick one over the other; the Scriptorium (west) will be frequently skipped.
**Fix:** add one line per archway — a draft, a sound, a smell — that hints at what lies beyond.

### ✗ Jaquays — inhabitants static, not dynamic
**Files:** all `rooms/*.md` and `encounters/03-pillar-hall-attendants.md`
**Issue:** attendants rise on trigger and fall; they do not patrol, reposition, or react to distant noise.
**Fix:** (accepted as scope-bounded for tier 1; flagged for dungeon #0002) OR add a one-line "inter-visit drift" to Room 03 encounter file.

### ✗ Stuart — no Memory Fragment in any room's GM Notes
**Files:** all 6 `rooms/*.md`
**Issue:** gate requires every room's GM Notes to include an optional Memory Fragment beat. None do.
**Fix:** add one per room. Keep to 1-2 sentences, optional-to-read, ideally from a prior bearer's perspective.

### ✗ Stuart — no Curse Symptoms Manifest for Silver Rose
**File:** expected `treasures/silver-rose-manifest.md`; missing.
**Issue:** `treasure-forger` is required to emit a manifest for any cursed artifact. This is the cross-skill handshake with `dungeon-smith`.
**Fix:** generate the manifest from the curse description.

### ✗ Stuart — Presence / Desire section missing from silver-rose.md
**File:** `treasures/silver-rose.md`
**Issue:** the artifact has no "what does it want" paragraph. The reviews noted specifically that the rose's desire is underdeveloped in prose.
**Fix:** add a Presence / Desire section between Appearance and Provenance.

### ✗ Stuart — manifest symptoms not distributed to rooms
**Files:** various room files.
**Issue:** symptoms like attribution-drift, orthographic-drift (e.g., Vaenor→Vanor), and repeated-phrase beats are not systematically placed. The pillar-scoring is a visual symptom, but only one symptom type is represented.
**Fix:** add one textual-drift or sensory-drift symptom to at least 3 additional rooms per the manifest.

### ✗ Schick — no reaction moment when artifact is taken
**File:** `rooms/06-sarcophagus-chamber.md`
**Issue:** the Memory Echo appears but the room/dungeon does not *react* physically to the rose's removal. Gate requires a heals/shifts/reveals moment.
**Fix:** let one of the scored frescoes restore itself (Panel 6 — Ilendra's parents' funeral) on removal, showing faces she had forgotten.

### ✗ Moldvay — Room 06 retrieval options not consolidated
**File:** `rooms/06-sarcophagus-chamber.md`
**Section:** "Retrieving the Rose"
**Issue:** four options (A, B, C, D). B and C differ only in noise-level (B = quiet-catch, C = quiet-sword-key); both trigger the same downstream consequence except for the Armor.
**Fix:** merge B into C — the hidden catch IS the notched-sword slot. Three options remain.

### ✗ Moldvay — Memory Echo has no interaction rule
**File:** `rooms/06-sarcophagus-chamber.md` and `encounters/06-ilendras-armor.md`
**Issue:** gate requires every non-statted entity to have a one-line "if players try to interact" rule. Ilendra's Memory Echo does not.
**Fix:** add one sentence to GM Notes specifying what happens if a player speaks to her, reaches for her, speaks her brother's name.

### ✗ Moldvay — premise.md too long
**File:** `premise.md`
**Issue:** 141 lines; gate target ≤ 80.
**Fix:** move provenance to `treasures/silver-rose.md` (already there — deduplicate); move Brother Laen NPC detail to `npcs/brother-laen.md` (now exists — deduplicate); keep premise to logline, setting, artifact-seed, scope, real-decision.

## Warnings (should-fix)

### ⚠ Schick — incidental items job-tagging incomplete
**File:** `treasures/minor-loot.md`
**Issue:** items generally serve purposes but aren't explicitly tagged (evidence / key / clue / roleplay).
**Fix (soft):** add a Purpose column to the minor-loot table.

### ⚠ Moldvay — attunement rules not inlined on cheatsheet
**File:** `module.md`, DM Cheatsheet section
**Issue:** cheatsheet has the pointer `"see reference/srd/attunement.md"` but gate requires the 3 critical sentences inline.
**Fix:** inline the short-rest / 3-item-limit / revealed-on-attunement lines.

### ⚠ Moldvay — paralyzed condition not inlined on cheatsheet
**File:** `module.md`
**Issue:** Room 05 ghoul's paralysis is referenced but the condition's effects aren't inlined in the cheatsheet.
**Fix:** add a "Conditions used" section to the cheatsheet with paralysis summarized.

## Passing gates (sample)

- Jaquays ✓: map loop present (2→3→5→4→2), vertical element (stairs + shaft), 2 paths to artifact, shortcut (shaft unlocks via Scriptorium).
- Gygax ✓: 4 retrieval paths + 4 post-recovery outcomes; wandering-pressure.md now exists.
- Stuart ✓: Antechamber of Tears is atmospheric (Stuart room).
- Schick ✓: each treasure sits in a room that cites it; Notched Longsword as key is signature design.
- Moldvay ✓: every read-aloud ≤ 60 words (verified per room); DCs inline in each room.
- Filename conventions: all pass.

## Strongest Recommended Fix

**Create the Curse Symptoms Manifest (`treasures/silver-rose-manifest.md`) and distribute its symptoms across rooms.** This single action clears 2 Stuart violations, enables the cross-skill contract, and raises Stuart's lens score from 1/5 to 4/5 or 5/5. Higher leverage than any other fix.

## Next Actions

Apply the 10 violations + 3 warnings in a single revision pass, then re-run lint to verify pass-state.
