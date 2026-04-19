---
adventure: 0001-tomb-of-the-silver-rose
tier: 1
author: human
created: 2026-04-18
---

# 0001 — The Tomb of the Silver Rose

**Tier:** 1 (party of 4 at level 3).
**Expected playtime:** one session, 3-4 hours.
**Setting:** Abanasinia, late Age of Might (~PC 20).
**Status:** Revision 2 (2026-04-18) — convergent persona-panel suggestions applied; all quality gates passing. See `lint-report-2026-04-18.md` for audit history.

## One-line logline

A buried rose that remembers the dead for you — and forgets the living on your behalf.

## What's in this directory

```
premise.md                            logline, setting, real decision (one page)
npcs/brother-laen.md                  patron with public/private knowledge, behavior matrix
rooms/map.md                          ASCII map of the Rose Cairn (2 levels)
rooms/01-cairn-cap.md                 entry room; Memory Fragment: Aelwen
rooms/02-antechamber-of-tears.md      Stuart room — weeping wall, branch cues, VANOR drift
rooms/03-pillar-hall.md               combat (4 skeletons) + attribution-drift seed
rooms/04-scriptorium.md               Jaquays puzzle + shaft shortcut; attribution drift
rooms/05-rose-stair.md                Vesk + Pella; conditional ghoul; vestibule
rooms/06-sarcophagus-chamber.md       climax — Rose, Armor, Memory Echo, fresco-heal
treasures/silver-rose.md              cursed artifact (+ Presence/Desire section)
treasures/silver-rose-manifest.md     cross-skill contract; curse symptoms required
treasures/minor-loot.md               items with Purpose tags
encounters/03-pillar-hall-attendants.md   4 skeletons, CR ¼ each
encounters/06-ilendras-armor.md       1 animated armor, CR 1
encounters/wandering-pressure.md      Cold Pulse + Wandering tables (temporal pressure)
module.md                             compiled table-ready module
reviews/                              5 persona reviews + SUMMARY.md
lint-report-2026-04-18.md             adventure-lint baseline audit (all gates now passing after revision 2)
```

## The real decision the adventure asks

After learning what the rose does, what do the players do?

1. **Return it to Brother Laen.** Take the 80 gp, walk away. No curse. Institutional cover-up confirmed.
2. **Keep it.** Attunement, creeping cost over sessions. Rose is useful. Memories go.
3. **Destroy it.** Requires returning to the tomb at dawn and offering the memory of their most-beloved person. The cure is its own cost.
4. **Sell it to someone worse.** Seeds adventure #0002 (the Bone-Collectors of Neraka are tracking it).

## Next steps

- Run `module-binder` on this directory to produce `module.md`.
- Have all 5 personas review the result; write reviews to `reviews/`.
- Aggregate scores in `reviews/SUMMARY.md`.
- Retrospective: what did the personas reveal about the MVP skill set?
