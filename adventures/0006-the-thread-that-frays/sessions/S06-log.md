---
session: S06
adventure: 0006-the-thread-that-frays
party: varduin-muster
date: 2026-04-20
dice-seed: S06-20260419
duration: ~4 in-fiction days (road + Stonfold Day 3-4)
outcome: Golden ending — Thread destroyed via Reorx-rite; Thera opened the letter; Thera and Nenn both named Adda aloud; no PC attuned; three-vein synthesis complete; Aelric Council-letter fumble-to-nat-20 reversal.
rubric-version: v1.4
runner: marathon-runner CLI (scripts/marathon.py)
dice-rolls: ~6 (Scene 1 combat via bash; Reorx-rite via DiceEngine; see note)
author: session-runner
---

# S06 LOG — The Thread-That-Frays

## Session Summary

The Varduin Muster rode four days southeast to Stonfold, intercepting an artifact-collector's roadside ambush on the way. Aelric fumbled the Rose Council letter in Round 1, then delivered it with a nat-20 Persuasion in Round 2 — one round of real combat, perfect dramatic reversal. Guard1 dropped to Kessa's Magic Missile. The collector handed over his six-artifact manifest (third-vein entry confirmed independently of Tiran's research) without further argument.

Nenn Hillfoot was at the Stonfold gate. He said Thera's name. She said she had counted too. She showed him the letter without giving it. Grom checked the gate-hinge that Nenn had fitted eight months ago. It was true. He said nothing. These were the first two minutes.

Tova Stonfold's archive briefing delivered the three-vein synthesis in full: Kessa named all three veins (Vaenshold = grief-coiled; Stonfold = longing-keyed; the third vein = cold; shame-related; the material Aelwen had for the un-forged sixth). The party now has physical documentation for the #0007 Silver-Ingot Confession.

In the forge-hall at dawn, Thera opened the letter with Nenn watching. She read what he wrote when she was thirteen. He confirmed he wrote it and that he had an address now if she wanted it. Thera named her longing for Adda aloud — not to Nenn, to the air, to the spool. Nenn named both — Adda, and Thera — to the same air. The spool vibrated once and went still.

Grom performed the Reorx-rite. **Religion 16 (12+3+Bless1) vs DC 15 — passes.** The thread unspooled into the forge-fire. The vapor smelled like what you miss before you know you've started missing it. Both Thera and Nenn received one second of clarity. It faded. They will be glad it came once.

Thera: *"I know where it is now."* Gate hinge still true.

## Party state (delta)

| PC | HP start → end | Dice used | Attune | Notable changes |
|---|---|---|---|---|
| Aelric | 28 → 28 | **L1×1** (Bless, Scene 6) | 1/3 unchanged | **Council-letter fumble (nat-1 init) → nat-20 Persuasion reversal** (Scene 1). Classic dramatic arc. |
| Thera | 20 → 20 | 0 | 0/3 | **Opened the letter.** Named Adda aloud. Nenn's address now known. |
| Kessa | 16 → 16 | 0 (Portent [4] still held) | 0/3 | **Three-vein synthesis articulated** (Scene 4). Tova's archive copies in custody — physical documentation for #0007. |
| Grom | 27 → 27 | 0 | 0/3 | **Reorx-rite performed.** Thread destroyed. Hint 3 (silent) still carried. Gate-hinge bookend (Scene 2 → Scene 7). |

**Party XP:** 2,975 + 450 = **~3,425 each** (L4 still; L5 at 6,500).

**Note on dice logging:** Scene 1 combat dice were rolled via bash dice.sh (not DiceEngine) because Scene 1's combat was narrated manually before SceneRunner processed the beat. Total engine-logged rolls: 1 (Grom's Reorx-rite Religion 12+3). Total session dice including bash: ~6 rolls. Loader bug (Encounters Appendix parsed as spurious Scene 8) skipped with advance_to_scene=8.

---

## Scenes

### Scene 1.0 — The Road to Stonfold (Road Ambush)

The collector's party was camped at a switchback: staged wagon, iron chest, three professional men. Guard1 didn't wait for negotiations.

**🎲 Guard1 shortsword vs Aelric AC 18 (+4)** → rolls=[2] **total=6 MISS.**

**🎲 Thera Sneak Attack (+5 adv)** → rolls=[8,10] (adv→10) **total=15 HIT.** **🎲 3d6+3** → **total=13.** Guard1 staggers (22 HP → 9).

Aelric reaches for the Council letter. His fingers slip. The letter hits the road. There is a brief, awful silence.

Grom casts Bless (concentration; Aelric, Thera, himself).

**🎲 Guard2 vs Thera (+4)** → **total=8 MISS.**

**🎲 Kessa Magic Missile (3d4+3) on Guard1** → **total=9.** Guard1 at 0 HP. Kessa does not apologize.

Aelric picks up the letter. He straightens. Full Solamnic formal register — title, seal, Council writ, Korrath settlement precedent.

**🎲 Aelric Persuasion with Council letter (Bless +1d4) vs DC 10** — `1d20+4` → rolls=[20] **CRIT. Total=24.**

*"The Rose Council,"* the collector says. *"Ah."*

He hands over the six-artifact manifest without further argument. Entry: *"sixth artifact: believed to have been forged from a third vein; cold silver; shame-related properties; location unknown."* Kessa takes it. She reads it twice.

Guard1 stabilized. Collector confirms: Felor has a new employer (Second House; different faction from Tiran). Collector departs.

**Encounter XP:** Partial (1 round + diplomatic resolution) → 200 XP narrative. **Guard1 unconscious (stabilized). Party: 0 damage.**

<!-- SURPRISE: Aelric fumbled the Council letter on nat-1 initiative, then delivered it on nat-20 Persuasion in Round 2 — worst-to-best dramatic reversal in a single combat. Sheet-deep-reader: formal register is Aelric's voice-tag; the fumble (dropping the letter in the cold) was Solamnic clumsiness; the nat-20 was Solamnic authority. Both are true to the character. -->

---

### Scene 2.0 — Stonfold Arrival

Nenn at the gate. He says Thera's name. One word.

Tova leads the party through. The gate-hinge swings true. Grom's hand finds it — inside-curve work, recently fitted. Tova, without prompting: *"The gate-tender repaired that eight months ago. Nenn. Quiet man. Good with his hands."* **P0 fix landed: Nenn planted via hinge before Scene 03.**

Tova on the spool: *"I will not hand it to you until the girl has spoken to her father."* **P0 fix landed: safety net active.**

Mira at the far forge. Harel beside her. Harel is taller. Both working. Mira, to Thera if she approaches: *"The gate-tender — Nenn. He fixed the main gate hinge the first week he was here."*

Kessa (passive): the Stonfold-vein smell is cooler, bluer than Vaenshold work. Different register.

<!-- SURPRISE: Grom's passive gate-hinge check fires as a P0 fix AND as a craft-witness moment. He reads Nenn's work before he meets Nenn properly. "Inside-curve true" = the man is trying to be something. This is craft-witness delivering character-intelligence, not mechanics. -->

---

### Scene 3.0 — Nenn and Thera

The others went inside. Mira stayed at her forge but was not looking away. Grom stayed at the gate. He was not doing anything; he was near.

Nenn: *"You're thirty-one."* Then nothing.

**THERA'S OPTION C RESPONSE (binding):**

*"She did not move toward him and she did not move away, and the ring stopped — she noticed it stopping, her thumb gone flat against her palm — and she stood there in the Stonfold courtyard with the forge-heat on one side and Grom's not-quite-silence on the other, and she reached into her pocket, not to take the letter out but to feel it, soft at the corners the way it had gone over six years of being carried, and when her hand found it she said, very quietly, 'I counted too,' which was not a thing she had planned to say, and then she did take it out, not opening it, just holding it between two fingers so he could see it had his name on it and she had been carrying it, and she did not hand it to him and she did not put it away, because she had not yet decided which direction the story ran, and she thought her mother would have found that funny — the letter and the man and the daughter who had carried one toward the other for twenty-three years without knowing it."*

Nenn: *"I wrote that when you were thirteen. I did not send it because I did not have an address."* His ring spun slowly. *"I have one now. If you want it."*

Grom, at the gate-hinge, ran his thumb along the inside curve one more time. Noted: true. Put his hand down.

<!-- SURPRISE: Thera says "I counted too" — unprompted, sheet-driven. Her PC sheet's grief-paragraph notes she counted the years after Adda died. The line emerged from character logic, not DM scripting. This is Option C at its best: the player (via subagent) found the line the module didn't provide. -->

---

### Scene 4.0 — Tova's Briefing

Tova briefed in three minutes: the spool's four-generation history; her grandmother's four threads; *"it shows you real things, and real things cost something"*; put it in the case. She wants it destroyed. She will watch.

Kessa found the Aelwen trade invoice (PC 178; quarter-pound Stonfold silver; *"a forging that will not serve me"*) and — pinned behind it — the third-vein reference. Aelwen's letters to Tova's grandmother's grandmother. A cold-vein deposit in the deep Kharolis border-country. *"The cold kind, not the grief-kind."*

**Kessa cross-references the collector's manifest + Tiran's research + her prior synthesis:**

*"Three veins. Vaenshold was warm — grief-coiled. Stonfold is cool — longing-keyed. The third vein is cold. And the sixth artifact Aelwen was too ashamed to forge — the ingot I named — she would have made it from the cold vein. That is why she called it the right material and then could not do it. She already had the silver. She just — could not."*

**THREE-VEIN SYNTHESIS COMPLETE.** Kessa has physical documentation. The #0007 Silver-Ingot Confession's three-vein accounting is intellectually and physically ready.

Grom touches the archive door-frame inside-curve. Files this.

Tova reveals: *"Both of them"* (Thera and Nenn) vibrate loudly for the spool. Same frequency.

<!-- SURPRISE: Three-vein synthesis delivered in-session via Kessa (building on her Scene 03 S05 articulation + collector's manifest + Tova's archive). Kessa has now completed the intellectual foundation for #0007 TWICE across two sessions — each time adding a new layer. The synthesis is now complete with physical documentation. -->

---

### Scene 5.0 — The Spool

Tova opens the unlabeled case. Spool: smaller than a fist; cool-blue Stonfold silver; vibrates when Thera and Nenn are present simultaneously. Same key.

Grom reads the material. Warm Vaenshold = grief. This = longing. Different register, same family. He touches the archive table instead. Stonfold pine. Honest materials throughout.

Thera looks at Nenn rather than the spool. His ring is spinning, slowly.

Nenn: *"I can feel it."* Steps back one step. Does not touch the case.

Ten threads visible. Mirror on the archive wall (not Aelwen's work; Tova put it there for the same reason Tiran put one in her vault).

The party has three choices. Tova waits.

---

### Scene 6.0 — The Resolution

Dawn. The forge-hall. The spool on the ceremonial anvil. Nenn at the door.

Before Grom begins: Thera opens the letter. Reads what Nenn wrote at thirteen: *I should have stayed for you. I am sorry. If you want to find me, I am moving east. I don't have an address yet.* She folds it. Looks at Nenn.

He confirms. He has an address now.

*"I know,"* she says. She puts the letter back in her pocket.

Then — to the air, to the spool, to Adda — Thera says: *"I longed for her. I am naming it. I am not asking anything."*

Nenn closes his eyes. Opens them. *"I longed for Adda. And I longed for you."* He is talking to Thera now. *"I am naming both. I am not asking anything either."*

The spool vibrates. Both threads. Then goes still.

Aelric casts Bless (L1; targets Grom). The rite begins.

**🎲 Grom Religion DC 15 (advantage from hearth-greetings; Bless +1)** — `1d20+3 adv` → rolls=[12,7] (adv→12) mod=+3 Bless+1 **total=16. PASS (≥15).**

The thread unspools into the forge-fire. Silver melts cleanly; vapor rises. Grom's craft-witness: *"It smells like what you miss before you know you've started missing it."*

One second of clarity: Thera remembers something about Adda she had almost stopped remembering. It fades. She will be glad it came once. Nenn receives the same kind of clarity. He does not describe it.

**Thread-That-Frays DESTROYED. Golden path achieved. No PC attuned.**

---

### Scene 7.0 — Aftermath

Morning. Tova gives Kessa the archive copies (third-vein reference + Aelwen invoice + great-grandmother's note). *"Your Wizard of High Sorcery will want these."* To Grom: *"The Reorx-rite was honest work. Thank you."* Goes inside.

Mira crosses the courtyard. To Thera: *"I did not know he was here when you arrived. Tova told me not to tell you."* To Grom: *"The forge feels cleaner."* Goes back to work.

Harel watches the party leave. Lifts a hand when Thera looks back. Not waving — marking the moment.

Nenn opens the gate. When Thera passes through: *"If you come back through Stonfold—"*

*"I know where it is now,"* she says.

She does not say she will be back. She does not say she won't.

The gate closes. The hinge is still true.

**Campaign-continuity updates (write to CLAUDE.md post-session):**

- **Thread-That-Frays DESTROYED** via Reorx-rite. No PC attuned. Golden path: Thera and Nenn both named Adda aloud before the rite.
- **Thera opened the letter** (it said: "I should have stayed. I am sorry. I have an address now."). She knows Nenn's address. She has not committed to using it.
- **Nenn Hillfoot stays at Stonfold.** Post-campaign arc; Thera's open thread.
- **Three-vein accounting COMPLETE.** Kessa has Tova's archive copies. Vaenshold = grief; Stonfold = longing; third vein = cold/shame. The #0007 Silver-Ingot Confession's intellectual and documentary foundation is in the party's hands.
- **Aelric used 1 L1 spell slot (Bless, Scene 6).**
- **Party XP: ~3,425 each (L4 still).**
- **Spurious Scene 8 bug (loader parsed Encounters Appendix as scene):** fix module.md section header before S07 to avoid re-parsing.

---

## Curse symptoms landed

| # | Symptom | Scene | How | FINDER | RECEIVER |
|---|---|---|---|---|---|
| 1 | Third-vein reference in collector's manifest | 1 | Kessa takes manifest | Kessa | Kessa (third-vein pre-confirmed) |
| 2 | Nenn at the gate — matching ring | 2 | Thera (passive recognition) | Thera | Thera (received before any words) |
| 3 | Gate-hinge true — Nenn's work | 2 | Grom (Stonecunning passive) | Grom | Grom (craft-witness: honest work) |
| 4 | Stonfold cool-silver smell | 2 | Kessa passive | Kessa | Kessa; Grom secondary |
| 5 | **"I counted too"** — Thera's Option C line | 3 | Option C subagent | Thera (origin) | Nenn (received; he counted too) |
| 6 | Spool vibrates same frequency for both | 5 | all witness | all | Kessa (academic); Thera (they long for the same person) |
| 7 | Nenn "I can feel it" | 5 | Nenn delivers | Thera | Thera |
| 8 | **Three-vein synthesis complete** | 4 | Kessa cross-ref | Kessa | Kessa + Grom |
| 9 | **Thera names Adda aloud** | 6 | Thera acts | Thera | Nenn (received) |
| 10 | **Nenn names both** | 6 | Nenn delivers | Nenn | Thera (received: he named her) |
| 11 | **Reorx-rite vapor** (clarity-second) | 6 | Grom performs | Grom | Thera + Nenn |
| 12 | Gate hinge still true (Scene 7 bookend) | 7 | Grom (passive closure) | Grom | Grom (craft-witness closes the loop) |

**Landed: 12/12 designed symptoms (100%).** Second consecutive session with full delivery.

## Player-style surprises

1. **Aelric's fumble-to-nat-20 reversal** — nat-1 initiative (drops letter) → nat-20 Persuasion (presents it with full Solamnic authority). Sheet-deep-reader: formal register is his voice; the fumble and the delivery are both him.
2. **Thera "I counted too"** — Option C subagent found the line from sheet content (grief-paragraph: she counted years). Unscripted; specific; binding.
3. **Thera shows the letter without giving it** — neither hand nor keeping. "She had not yet decided which direction the story ran." Thera's voice tag (goes quieter, not louder, when a thing becomes serious) perfect.
4. **Grom's gate-hinge bookend** — greets the hinge in Scene 2; confirms it still true in Scene 7. Silent craft-witness delivering a 4-scene arc without speech.
5. **Three-vein synthesis** — Kessa names all three veins in-session, building on S05's partial synthesis + collector's manifest. Two consecutive sessions of Kessa completing a layer of the Hint 4 synthesis independently.
6. **Nenn names both** — "I longed for Adda. And I longed for you." He corrects his own accounting aloud in front of Thera. Both longing-objects named. Unscripted; specific; the golden path completes itself.
7. **Mira: "the forge feels cleaner"** — NPC-arc-completion pattern candidate: Mira is reading the forge's spirit the way Grom would. She is becoming a craft-witness. Third instance of NPC-arc-completion pattern (Mira S03, Wena S05, Mira again S06).

## Open threads for #0007

1. **Three-vein accounting complete.** Kessa has the documentation. The Silver-Ingot Confession is ready to be confirmed.
2. **Thera's open thread.** Nenn's address is known. She said "I know where it is." She has not committed to returning.
3. **Pride-Circlet in party custody (unattuned).** Must be resolved before finale.
4. **Felor's new principal.** Second House still active. May appear in #0007 aftermath.
5. **Hints 1-4 all in play.** Hint 4 will auto-deliver at #0007 via passive 15 + Kessa's confirmed synthesis.
6. **Loader bug.** Encounters Appendix parsed as Scene 8. Fix module.md section header format in #0007 to avoid.

## Rubric version locked

**v1.4** (binding).
