# Marathon — D&D Workshop

A workshop for designing D&D 5e adventures set in Dragonlance, built around the principle **the treasures are the story**.

See `docs/specs/2026-04-18-dnd-workshop-design.md` for the full design.

## Layout

```
skills/           workshop skills (SKILL.md per dir)
reference/srd/    cached 5e SRD (CC-BY-4.0)
reference/dragonlance/  curated lore pack
personas/         5 design-canon voices + rubric
adventures/       NNNN-<slug>/ per adventure
docs/             specs, plans, notes
```

## File Contract

Every generated markdown file starts with frontmatter:

```yaml
---
adventure: 0001-tomb-of-the-silver-rose   # or 'workshop' for non-adventure files
tier: 1                                   # 1-4 or omit
author: dungeon-smith                     # skill or 'human'
created: 2026-04-18
sources:
  - reference/srd/monsters-tier1.md
  - reference/dragonlance/ages.md#age-of-might
---
```

## Naming

- Adventure slug: `NNNN-kebab-case` (`0001-tomb-of-the-silver-rose`).
- Room files: `NN-<slug>.md` (`02-pillar-hall.md`).
- Treasures/encounters/npcs: `<slug>.md`.

## Cross-references

Use relative markdown links (`treasures/silver-rose.md`). `module-binder` resolves & inlines them when compiling `module.md`.

## Never Overwrite Silently

Skills append, write to a new file, or prompt. They never clobber prior work.

## YAGNI Guardrails

- Markdown only until 3+ adventures exist; no YAML migration.
- No orchestrator/pipeline skill until manual pipeline runs end-to-end twice.
- Reference packs grow on demand — every added file justified by a skill needing it.

## Accessibility Policy

**Marathon writes for readers who are interested in Dragonlance but not necessarily familiar with it.** Ratified 2026-04-18 after S01's Fresh Face lens feedback. **Clarified 2026-04-19 post-S02: Marathon is a CAMPAIGN, not an anthology.**

- **First use of setting-specific terms** (Solamnic, Krynn, Cataclysm, High Sorcery, Test, Portent, Oath, Order of the Rose, etc.) should be glossed in-fiction — a line of dialogue, a character's internal note, or a narrator's aside. Returning uses can assume the gloss landed.
- **The Oath (*Est Sularus oth Mithas*)** should be translated (*"my honor is my life"*) on first appearance in a session or module.
- **Mechanics** should be translated to fiction in narrative prose (e.g., "the cold settled into his plate" rather than "he takes 1 level of exhaustion"). The mechanical line goes in the DM-facing notes.
- **Prior reading is not assumed for setting terms**, but **cross-adventure continuity IS assumed.** A reader arriving at S03 cold can infer Dragonlance context from glosses; they may miss cross-adventure signals (e.g., Vesk's phrase echoing in Keloth's ledger) and that is acceptable. Cross-adventure signals are *bonuses* for campaign readers, not gate-keepers.
- **Session logs and modules should stand on their own for a new Dragonlance reader** but they should also *reward the campaign reader* with layers of cross-adventure continuity.

**This is the campaign-or-anthology reconciliation** that the Fresh Face lens asked for at S02. Resolved: campaign-reward layered on anthology-floor. Do not gate new readers; do reward old ones.

This policy does not dumb down. The setting's density is preserved — we just don't assume the reader arrived pre-loaded.

## Campaign Continuity

Facts established in played sessions become **campaign-permanent** and constrain future session narration. These are not module-level conventions; they are world-facts.

### Campaign-permanent facts (as of 2026-04-19, post-S03)

- **Aelric of Crownhold attuned the Varran-reliquary at S02 Scene 6.** He remembers Varran only as dying (the 60-second Minute). Every other memory of Varran is permanently consumed. No spell, ritual, or DM re-narration can restore them. In future sessions:
  - The DM **must not** re-narrate Varran as living (no flashbacks, no dreams of Varran alive, no "you remember a time when..." scenes).
  - Aelric **cannot** volunteer Varran-memories in conversation — he does not have them.
  - Aelric **can** speak of Varran's last minute in first-person; he lived it.
  - Aelric's PC sheet grief-paragraph is updated to reflect this.
- **Sir Venric of the Sword fell defending Varduin at S02's feint raid.** Pyre at Varduin. The three Solamnic knights who defended with him: two survived. Canon.
- **Keloth of Neraka is dead** (S02 Scene 6). Idra is dead. The cell is fragmented; seven members west scattered; three east survivors were the S03 threat.
- **Pella stays at Brother Laen's mother's in Varduin.** By her own choice. Visits by the party expected but she does not travel with them.
- **Aelwen's Letter is in the Rose Council's archive** (S01 outcome). The Mira-letter was delivered to Brother Laen post-S02; Council contract was formal and has now been fulfilled at S03.
- **The cross-adventure phrase *"I will not look at the rose again"*** exists on Keloth's wall-ledger in the vault (S02, physically present uncredited) AND in Mira's sales-ledger margin (S03, caught by Kessa Investigation 16). Kessa has now transcribed BOTH instances into Vethrenn's commonplace book. **The pattern-link between her S02 vault-transcription and Mira's ledger-phrase is NOT YET FORGED** — she has both phrases separately; she has not cross-referenced them. Recovery path remains open for S04+ (between-adventure journal-reading beat expected).

#### S05-specific campaign-permanent facts (2026-04-19)

- **Pride-Circlet is in party custody, UNATTUNED.** Velvet-wrapped. Second House archive lists it as "in care of Varduin Muster pending disposition." No PC attuned. **Must be destroyed (Reorx-rite) or otherwise disposed of before #0007 finale.**
- **No PC attuned the Pride-Circlet.** Aelric picked it up, felt it warm, set it down without holding it to his head. Oath was sufficient. **No Pride-Lock curse on any PC.**
- **Lady Tiran: heard without the Circlet.** She told Wena Laen what Edric saw. She is at peace and dying. Not attuned. Her final-state is closed; she is not a campaign thread.
- **Wena Laen stays at Korrath-by-the-Sea.** Chapter-house novice. Post-campaign arc. She has a hinge to install.
- **Kessa carries Tiran's six-forging research** (original; most complete Aelwen manifest). Sixth forging: shame-keyed, provenance unknown, not in any known market.
- **Aelwen triplet complete in Kessa's custody:** journal page (#0003, doubt) + apron-scrap (#0004, resolve) + water-reflection fragment (#0005, horror). Three Aelwen writings recovered across three adventures.
- **Hint 4 pre-synthesis articulated by Kessa in-voice (S05 Scene 03).** *"I think the sixth is not an object she made. I think it is the object she could not make because she was too ashamed to."* This names the ingot-as-missing-ending theory — the intellectual foundation of the #0007 Silver-Ingot Confession. **Campaign-permanent; the #0007 finale will confirm this theory, not deliver it cold.**
- **Aelric's breast-pouch: three objects** — Wena's note + Laen's formal letter + Varran's blue-leather saddle-lashing. The saddle-lashing was named as a carried object for the first time.
- **Party XP: 2,525 each (L4; L5 threshold 6,500).**

#### S04-specific campaign-permanent facts (2026-04-19)

- **Thane Krun Ironhaft — Reorx-exiled by Grom.** Ritual-bound exile; cannot return to Thorbardin. Kruntharrak mine-hold passes to Thora Stoneforge (Krun's second cousin; line-continuity rule). **Krun cannot be re-introduced as a hold-holder in any future session.**
- **The Wrath-Coin is DESTROYED** via Grom's Reorx-rite at Gavrek's Anvil's forge at dawn. **Six loaded grievance-sparks dispersed east** (Krun's father's killer; Sigga's un-spoken rage; Aelwen's un-spoken order-rage; Heva's grief-rage; the unnamed Kharolis merchant; Jarek's guilt). The coin was destroyed per Aelwen's intent — mirror-smooth-face-up, redemption-face up. **TWO of Aelwen's six forgings are now destroyed** (Mirror + Coin). #0007 finale Silver-Ingot Confession must account for both as completed absences.
- **Duren Coalbeard's hammer is in the grave.** Grom re-performed the three-year rite with the hammer present. **Grom's burn-scar on his left hand stopped aching** — the three-year pulse that has ached every dawn since Duren's death is gone. **Campaign-permanent.**
- **Krun-Duren half-kinship is public** (within party + Gavrek's Anvil + Thorbardin Council). Hilda Stoneforge named in shrine-ledger.
- **Jarek Stoneforge captured alive** via Grom's Guiding Bolt overshoot Scene 1 (did not reach instakill threshold). Delivered to Thorbardin Council for separate tribunal. Expected: exile or mine-sentence (Grom's Reorx-exile of Krun sets precedent).
- **Hint 2 UNLOCKED** — Vethrenn's warded margin-note surfaced at Scene 3 Reorx-rite (Kessa's commonplace book warmed; the ink re-readable): *"We made the rose to hold. We did not try to release. I think release is possible. I do not know how. — V., the night I went."* Dated PC 100. **Campaign-permanent.**
- **Hint 3 PLANTED** (silent) — Grom received Reorx's Judgment at Scene 3 via craft-witness channel (silent reception; self-check articulation failed). **Grom holds, non-verbally, the understanding that Aelwen's forgings are "grief-coiled, not forged-with-intent" and that "a coil can be uncoiled."** He has not articulated this aloud to the party. It drove his Scene 6 Reorx-exile invocation without speech. **Campaign-permanent; synthesis with Hint 2 reserved for #0007 finale (or earlier if Grom articulates between-adventure).**
- **Aelwen's apron-scrap** (#0004 Scene 4) in Kessa's custody. Diptych with #0003 journal page complete. Both "night before." **Ready for #0007 Silver-Ingot Confession synthesis.**
- **Wena Laen's sealed note to Aelric** (S04 Scene 7). Seed for #0005 — she is at a southern Revered Daughters of Paladine convent; she has been approached by a Pride-Circlet-seeker connected to Lady Tiran's faction in Istar.
- **Party now at L4** (XP 2,075 each). Scales for #0005 encounter design.
- **Mira / Sigga / Harel / Tova Stonfold craft-chain** — female-smith witness thread locked across three adventures.

#### S03-specific campaign-permanent facts (2026-04-19)

- **Aelwen's Mirror is DESTROYED.** Grom performed the Reorx-shattering rite at Crystalmir's smith-forge at dawn, rescued by Kessa's Portent [14]. The obsidian shattered along Aelwen's unconverged polish-lines; the silver un-forged. Grom retains ~8 oz of inert un-forged Vaenshold moon-silver (the Mirror's matter; no longer magical). **No future session may re-introduce Aelwen's Mirror as intact.** The **#0007 finale's Silver-Ingot Confession must account for the Mirror as a completed absence** — one of the six artifacts destroyed before the finale, not an uncompleted work.
- **No PC attuned the Mirror.** All four Varduin Muster PCs declined — Kessa catalog'd, Thera found no profit, Grom named it unmendable, Aelric held to the Measure. Collective restraint. No self-image-replacement curse was taken on by any PC. **The Mirror's curse is absent from the party.**
- **Mira Vaenshold-Silversmith has left Crystalmir-by-the-Fells for Stonfold**, with Harel her apprentice, by her own decision at dawn post-assault. Shop closed and will not reopen. **Mira will not return to Crystalmir under any future-session narration.** She is at Stonfold under the care of her mother's cousin Tova Stonfold.
- **Mira wrote her mother's name in ink** — the first time in 30 years — on a Council file-note she gave to Grom at the forge-rite's close. *"A daughter's note. My mother's name was Seralen. I am grateful. — M. Vaenshold."* The note is in Grom's pouch with Duren's tongs. Seralen's name is now writable — her refusal-of-naming is *over*.
- **Kann of Neraka is dead** (S03 Scene 5). Kessa's Magic Missile took him in the street as he fled at 5 HP. **Kann cannot return in future sessions.** The module had preferred escape; dice said otherwise; dice win. Campaign adapts: the east-regrouped Bone-Collectors now number four (three S02 east-escapees + Gorr if released on oath, which Brother Laen is expected to grant) — reduced threat vector for #0006/#0007 planning.
- **Vend of Neraka is dead** (S03 Scene 5). Grom's Guiding Bolt. Vend died without speaking, as he had lived for eleven years.
- **Pevra, Lorn, Gorr captured alive** and delivered to Crystalmir town-watch with Brother Laen's letter. Expected dispositions: Lorn (most committed; Nerakan-combatant trial); Pevra (grieving Idra; possible turn-coat, Grom may vouch); Gorr (released on oath). These are expected outcomes, not yet final.
- **Tova Stonfold** (Stonfold smith-family matriarch; non-Vaenshold moon-silver lineage) was named aloud by Mira. **The Stonfold smith-family is now canon** — 80 miles southwest of Crystalmir. Seed for #0006 + #0007 active.
- **Felor of the Second House of Istar** is canon as the Istaran client who contracted Kann. Engraved in tiny Nerakan on Kann's Stonfold finger-bone cord; confirmed by Kessa Identify ritual. Felor works for **Lady Tiran of the Purple Rose's faction** — seed for #0005 active.
- **Aelwen's journal page** is in Kessa's custody. Contains: "I made six. I made the Rose first. I made the Reliquary second. I made the Mirror third. I made three more in secret after the Mirror and I can no longer remember what I named them. I think I should have forged an ingot instead." **Hint 4 pre-plant for #0007 finale** — the ingot-reference is now in play.

#### S06-specific campaign-permanent facts (2026-04-20)

- **Thread-That-Frays DESTROYED** via Grom's Reorx-rite at Stonfold forge-hall at dawn (Religion 16). **Four of Aelwen's six forgings are now destroyed** (Mirror S03 + Coin S04 + Thread S06) plus one forged-complete (Ingot S07). Two remain: Varran-Reliquary (attuned by Aelric; campaign-permanent) + Silver Rose (Solamnic archive; never in party hands). No future session may re-introduce the Thread as intact.
- **Thera opened Vesk's letter.** She named her longing for Adda aloud — in Stonfold, in the forge-hall, with Nenn Hillfoot present. She said *"I counted too"* when Nenn said he had counted. This is the first time Thera has named Adda's absence in this campaign. **Thera's Adda-grief is no longer unexpressed.**
- **Nenn Hillfoot named both longing-objects** (Adda + Thera) by his own initiative. He was not prompted. The golden path was completed by Nenn, not the party. **Nenn's address is known to Thera.** He is at Stonfold; the gate-hinge he fitted eight months ago was true. He will receive visits.
- **Three-vein synthesis COMPLETE** — Kessa recovered Tova's archive copies confirming all three cold-vein sources: Vaenshold (grief-vein; Aelwen's estate), Stonfold (longing-vein; Tova's family mine), and the unnamed Kharolis border vein (shame-vein; cold-vein silver; Tova's pencil-sketch map). **Kessa has the physical documentation.** The Silver-Ingot Confession's material provenance is confirmed.
- **Hint 4 foundation physically confirmed.** The three-vein synthesis from Tova's archive made Hint 4's auto-delivery at #0007 a confirmed structural event, not a theory.
- **v1.4 cross-character mechanical compound fired** for the first time: Aelric's Bless cast on Grom for the Reorx-rite. The ratified amendment validated on first use.
- **Party XP: ~3,425 each (L4; L5 threshold 6,500).** Party purse ~1,180 gp + artifacts.

#### S07-specific campaign-permanent facts (2026-04-20) — CAMPAIGN COMPLETE

- **Moon-Silver Cycle: COMPLETE.** Route D (full inversion) achieved at dawn, PC 20, Vaenshold workshop. Religion 23.
- **The Silver-Ingot Confession was performed** by Grom Ironhand of the Varduin Muster, at Aelwen's forge, 200 years after she could not. His exact words are verbatim in `adventures/0007-the-silver-ingot-confession/sessions/S07-log.md`. The ingot carries two shames: Aelwen's (things made to hold grief; the tool withheld; shame held the hammer) and Grom's (the failed pre-blessing at the vein; *"I was slow and I was proud and I called it patience"*). Both are named. Both are forged.
- **All four hints delivered simultaneously** at Scene 06 ingot-forging:
  - Hint 1 (Fresco-Heal, S01): fresco of Ilendra's parents changed. Their faces no longer hold what they were holding.
  - Hint 2 (Vethrenn's margin, S01): already unlocked S04; Kessa's book warmed at the workshop threshold and she confirmed *"I know how"* before the night began.
  - Hint 3 (Reorx's Judgment, S04): Grom performed it. The understanding planted silently in S04 spoke through his hands into the silver at the confession.
  - Hint 4 (Aelwen's Confession, S03/S05): auto-delivered at passive 15. Every PC heard: *"I should have forged an ingot instead."* Kessa: *"She did. We did it for her."*
- **The ingot is in the sixth vault-space at Vaenshold workshop.** The vault door is not locked. It is findable. This is the ending-condition of the Silver-Ingot Confession and the campaign.
- **Pride-Circlet DESTROYED** in the same forge, same dawn (Religion 15 exactly). The Circlet's desire to be worn simply stopped. No vapor. No drama. The obsidian splintered along its laurel-band seam. **Five of Aelwen's six forgings are resolved.** One (Varran-Reliquary) remains with Aelric as a campaign-permanent commitment.
- **Aelric held the Varran-reliquary without opening it.** His d6 rolled letter-of-Measure (2): honor what you committed to. He committed to the Minute in S02. He acknowledged it as release without replaying it. **He does not play the Minute again.** His grief for Varran is named, carried, and honored.
- **Kessa's commonplace book (Vethrenn's, with her margin answer)** is on the Vaenshold workshop archive shelf. She wrote: *"She was right. Here is how: you name the shame over hot metal, in the place where the grief began. You do not ask for anything. You name it and forge it and that is the releasing. — K., PC 20, Vaenshold workshop."* She did not take the book. It is findable. The 200-year-old question is answered.
- **Thera cut bread long-ways** on the road home from Vaenshold. First time since Adda died when she was eight. She was aware of doing it. She did not explain. **Thera's Adda-grief is complete.** She acts from the named longing (S06) without announcement.
- **The cross-adventure phrase *"I will not look at the rose again"*** — delivered S03 from Mira's ledger; source Keloth's vault-ledger (S02). Campaign echo fully closed. Kessa's transcription (S02) and Mira's ledger instance (S03) are in her notebook; the pattern-link was not formally cross-referenced in play but the campaign is complete and the phrase's purpose is fulfilled.
- **Party XP: ~3,925 each. Level 4. Campaign over. L5 (6,500) never reached — campaign ended at its proper conclusion.**

### Campaign-permanent party state (FINAL — post-S07)

- **Varduin Muster** — four PCs, campaign complete. XP 3,925 each (L4).
- **Aelric** — attuned to Varran-reliquary (1/3 slots; campaign-permanent). Held reliquary without opening it at S07 finale. Told the Vaenshold steward: *"We completed work that was left unfinished two hundred years ago."*
- **Thera** — carries Pella's drawings + Vesk's sealed letter (read S06) + Seralen's note + scouts' map. **Cut bread long-ways on the road home from S07.** The longing is named; the act follows.
- **Kessa** — carries Keloth's mother's bracelet (unattuned, archival) + vault-ledger transcription + Kann's finger-bone + Portent [4] (never deployed). **Left Vethrenn's commonplace book in the Vaenshold workshop archive.** Catalog complete; archive is the right home.
- **Grom** — carries Duren's final letter + Duren's tongs + ~8 oz inert Mirror-silver + ~1 oz inert Coin-silver. Burn-scar stopped aching S04. **Performed the Silver-Ingot Confession S07.** Campaign-permanent: the confession is verbatim in the session log; it speaks for him.

### Updates

Campaign-continuity is updated post-every-session in `HANDOFF-S{N}.md` and aggregated here. If any DM narration contradicts a campaign-permanent fact, the fact wins.

Campaign-continuity is updated post-every-session in `HANDOFF-S{N}.md` and aggregated here. If any DM narration contradicts a campaign-permanent fact, the fact wins.

## Canon Policy

**Marathon is Dragonlance-native, not Dragonlance-adjacent.** We invent where Dragonlance is silent. We do not contradict canon where canon speaks. Every invented name (location, character, item, event) is tracked in `reference/dragonlance/workshop-canon.md`.
