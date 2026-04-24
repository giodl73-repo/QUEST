---
adventure: 0023-the-supply-run
author: adventure-lint
created: 2026-04-22
violations: 0
warnings: 2
passed: 22
---

# Lint Report — The Supply Run

## Summary

- ✗ **0 violations** (must-fix before module-binder)
- ⚠ **2 warnings** (fix recommended)
- ✓ **22 passed**

*Two issues caught and fixed during this lint run: Room 03 connections lacked sensory cues (fixed); Room 05 lacked token reaction moment (fixed).*

---

## Per-Lens Scorecard

| Lens | Passed | Failed | Notes |
|---|---|---|---|
| Jaquays (topology) | 7 | 0 | All topology gates pass post-fix |
| Gygax (pressure + agency) | 3 | 0 | Encounter count 3.0 (threshold 3); pressure table ✓ |
| Stuart (atmosphere) | 5 | 0 | All 5 Memory Fragments present; no cursed artifact |
| Schick (treasure framing) | 3 | 0 | Contractor token + sealed correspondence with purpose tags; Maret reaction moment added |
| Moldvay (table-readiness) | 6 | 0 | All read-alouds ≤60 words; all NPCs have files |

---

## Violations (must-fix) — NONE REMAINING

### ✓ FIXED — Jaquays: Room 03 exit branches lacked sensory cues
- **Was:** North, up, and south exits listed without distinguishing sensory detail
- **Fix applied:** North = "cold wind from open pass, smells of mountain"; Up = "handholds visible, ledge visible as stone shelf in early light"; South = "mule tracks in dust, road widens ahead" (`rooms/03-choke-point.md`, Connections)

### ✓ FIXED — Schick: Room 05 lacked token reaction moment
- **Was:** Maret's token delivery described only in the premise; Room 05 had no reaction moment
- **Fix applied:** Added reaction moment to Room 05 GM Notes — Maret removes the token from its cord without looking at the crate contents; the token is warm from being worn (`rooms/05-irathon-road.md`, GM Notes)

---

## Warnings (should-fix)

### ⚠ Moldvay: premise.md length exceeds 80-line target
- **File:** `premise.md`
- **Issue:** ~160 lines. Same situation as 0022 — the between-session resource mechanics require documentation that exceeds single-page. Acceptable given the campaign's new resource system being established. Module-binder will separate DM cheatsheet from scene text.
- **No immediate action needed.**

### ⚠ Gygax: combat retreat fallback not explicitly documented
- **File:** `encounters/ambush-remnant.md`, End states section
- **Issue:** "If scouts disengage south" is documented; "if the party retreats north" is not. A party that routes during the ambush needs a documented consequence.
- **Recommended fix:** Add one line to encounter GM Notes: *"If the party retreats north: scouts do not pursue past the choke point (standing orders). Party may return with garrison reinforcement. Supply cart remains; Aldric remains; note in handoff."*

---

## Passing gates (22)

**Jaquays (7/7):**
- ✓ `rooms/map.md` exists
- ✓ Loop: Room 03 ↔ Room 04 (choke point → ledge → choke point descent)
- ✓ Vertical: Room 03 → Room 04 (30-foot climb, Athletics DC 12)
- ✓ ≥ 2 paths to supply cart (Path A: ground trail; Path B: upper ledge first, descend with Surprise)
- ✓ Shortcut: upper ledge approach (cold smoke spotted at passive DC 14) delivers Surprise in combat
- ✓ All branch exits now have distinguishing sensory cues (post-fix)
- ✓ Dynamic inhabitants: mercenary scouts have Cunning Action disengage + morale retreat behavior

**Gygax (3/3):**
- ✓ `encounters/supply-run-pressure.md` exists (temporal pressure for outdoor passage)
- ✓ Encounter count: 3.0 effective (combat=1.0 + exposure checks=0.5+0.5 + social Pren=0.5 + pressure table=0.5)
- ✓ Pren disposition has ≥3 valid outcomes (prisoner / release with head start / leave on ledge)

**Stuart (5/5):**
- ✓ Memory Fragment in all 5 rooms
- ✓ No cursed artifact — manifest gate N/A
- ✓ Cold fire ring, provision cache, and sealed correspondence all reward attention
- ✓ No non-statted entities without interaction rules
- ✓ Critical-roll failure states: Stealth failure = one arrow (documented); Survival miss = less information (adventure continues)

**Schick (3/3):**
- ✓ Contractor's token: purpose tag "evidence → 0024 Hessa seed" in Room 03 Treasure
- ✓ Sealed correspondence: purpose tag "evidence → Rose Council non-response thread" in Room 03 Treasure
- ✓ Maret's token reaction moment added to Room 05 GM Notes (post-fix)

**Moldvay (6/6):**
- ✓ All read-alouds ≤60 words (Room 01: ~50w; Room 02: ~38w; Room 03: ~55w; Room 04: ~55w; Room 05: ~35w)
- ✓ All DCs inline with hazards
- ✓ All NPCs named in premise have files: Maret Stave (existing, 0022), Aldric (aldric-scout.md ✓), Pren (pren-reconstitution.md ✓), Dex (dex-contractor.md ✓)
- ✓ Aldric (1 HP NPC) has stat block and interaction rules in his NPC file
- ✓ No duplicate retrieval options
- ✓ Frontmatter complete on all 12 files

**Campaign-awareness (6/6):**
- ✓ Premise references campaign spine (thorngate-watch.md)
- ✓ Seeds retrieved: supply-cart-ambush-third-party (non-Reconstitution ambush confirmed)
- ✓ Seeds planted: contractor-token-hessa-link (→0024), Pren H1 partial (→H1 chain), sealed correspondence (→Rose Council thread), Maret double-rations deepened
- ✓ H1 partial delivery scheduled and present (Pren scene, Room 04, passive DC 12 fallback)
- ✓ Sava spotlight: Room 01 (supply count), Room 03 (combat healing decision), Room 05 (Maret token)
- ✓ Decision-point fallbacks: combat (noted retreat option), Pren disposition (3 options documented)

**P0 checks (2/2):**
- ✓ Decision fallbacks present for all choice scenes
- ✓ No rite/confession scene — dm-letter gate N/A

---

## File inventory

| File | Status |
|---|---|
| `premise.md` | ✓ |
| `rooms/map.md` | ✓ |
| `rooms/01-postern-exit.md` | ✓ |
| `rooms/02-low-trail.md` | ✓ |
| `rooms/03-choke-point.md` | ✓ (fixed) |
| `rooms/04-upper-ledge.md` | ✓ |
| `rooms/05-irathon-road.md` | ✓ (fixed) |
| `encounters/ambush-remnant.md` | ✓ |
| `encounters/supply-run-pressure.md` | ✓ |
| `npcs/pren-reconstitution.md` | ✓ |
| `npcs/dex-contractor.md` | ✓ |
| `npcs/aldric-scout.md` | ✓ |

---

## Recommended before module-binder

Apply the ⚠ Gygax retreat fallback (one line in `encounters/ambush-remnant.md` End states). Then compile.
