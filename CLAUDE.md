# QUEST — D&D Workshop

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

**QUEST writes for readers who are interested in Dragonlance but not necessarily familiar with it.** Ratified 2026-04-18 after S01's Fresh Face lens feedback. **Clarified 2026-04-19 post-S02: QUEST is a CAMPAIGN, not an anthology.**

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

---

## Campaign 2 — The Conclave Compact

**Party:** compact-wardens (Thessaly Nightmantle, Orik Flintback, Sera Ashfall, Calder of the Third Road; Lenne Stormwatch joined C2-S02)
**Campaign:** 7 adventures (0008–0014), conclave-compact spine.
**Central question:** *When a covenant breaks, who bears the cost of mending it?*
**Convergence deadline:** Triple-moon convergence in 88 days from C2-S02 (shortening each session). The compact must be spoken whole during this window or the next opportunity is three centuries away.

### Campaign-permanent facts (C2-S01 — 2026-04-20)

- **Clause of Witness recovered** — Korrath-by-the-Sea, Merchant Henneth's collection. Route A (honest explanation + Tessamine's letter). No combat. Thessaly carries it (unattuned).
- **Hint 1 delivered** — Thessaly read the inscription (*"Let no mortal act without witness"*); it brightened; she said *"This is the first clause."* Unprompted. Session 1.
- **Tessamine arc-completion fired** — compact's purpose spoken: *"The compact was not written to bind the Orders. It was written to bind the Orders to the people who live under the sky they argue about."* Reconstruction document (7 clauses, some incomplete) given to Thessaly.
- **Thessaly named her wound (first time)** — *"I cast a spell at my Test that I was not supposed to cast. It cost someone something I can't give back."* Spoken to Tessamine. Session 1, Scene 06.
- **Unbound Conclave courier active in Korrath** — spotted by Sera (passive 16). She saw the party leave with the shard.
- **Route D prerequisite 1/4 confirmed** — Hint 1 delivered + wound named + compact's purpose received.
- **Party XP: 300 each. Purse: 190 gp.**

### Campaign-permanent facts (C2-S02 — 2026-04-20)

- **Clause of Ambition recovered** — Volenn's Tower, Kharolis foothills, from Lenne Stormwatch. Route D. Orik named the hall, the oil, the fire, the seven apprentices: *"The shard vibrates for me because I'm still trying to prove it was worth going."* Vibration stopped before the shard left Lenne's palm. Orik carries it (unattuned).
- **Hint 2 delivered** — Triple-moon convergence in 88 days (from C2-S02). Volenn's moon-calendar annotation: *"First occurrence since the Cataclysm. If the clauses were written to align with this event — the compact can only be spoken whole when the sky is right."* Thessaly copied it verbatim. The party has a hard deadline.
- **Lenne Stormwatch joined the party** — Volenn's successor; 8 years of compact research data; Volenn's moon-calendar copy. She asked to join because Volenn was supposed to be at the convergence. She is his closest equivalent still living. Full PC sheet at `personas/parties/compact-wardens/lenne-stormwatch.md`.
- **Route D prerequisites: 2/4 confirmed** — Hint 1 (C2-S01) + Hint 2 (C2-S02).
- **Unbound Conclave agents (Osvin + Quiet One)** — fled Kharolis road ambush at 8 HP. Regrouping with mage-agent Mira Coldsteel. Will appear in adventure 0010.
- **Rubric v1.5 ratified** — act-without-announcement anchor (Atmospheric Landing 9+ band). Sera hold-space ×3 in 2 sessions confirmed pattern.
- **grief-paragraph-dialogue confirmed** as sheet-deep-reader sub-type — 3 cross-campaign instances.
- **Party XP: 712 each. Purse: 190 gp. Party of 5.**

### Campaign-permanent party state (post-C2-S02)

- **Thessaly** — carries Clause of Witness (unattuned) + Clause of Ambition (unattuned) + reconstruction document + convergence date (85 days and closing). Named her wound C2-S01. Does not yet know if she will attune.
- **Orik** — named the hall C2-S02. Carries the Clause of Ambition (unattuned). craft-witness candidate (doorframe inside-curve check C2-S02). His grief is named; not yet resolved.
- **Sera** — three consecutive hold-space acts in two sessions (act-without-announcement confirmed). Spotted Unbound Conclave courier C2-S01. Has not yet named the settlement.
- **Calder** — reads endings. Has not said what he thinks about Tessamine's timeline or Volenn's note. Full resources both sessions.
- **Lenne** — joined C2-S02. Relived Volenn's death holding the Clause of Grief (S03). Didn't document the arc-completion scene. Documentation-suspension: first time she let something land uncategorized.
- **Sera** — **Named the settlement (S03). Saw them safe.** Carries Clause of Grief (unattuned). act-without-announcement confirmed: 5 C2 instances.
- **Calder** — Named the chapel promise at the doorway (S03): *"The chapel will be in the witness-list. That was a promise."* Campaign-permanent.

### Campaign-permanent facts (C2-S04 — 2026-04-20)

- **Clause of Defiance recovered** — Session 4. Route D. Hint 3 delivered. Calder named the plague village. Thessaly carries it (unattuned). Four shards total.
- **Hint 3 delivered** — *"What any mortal swore, any mortal may unsay. This was always true."* The new compact can incorporate Sylaren's amendment. It does not need to restore the original verbatim.
- **Route D prerequisites: 4/4 confirmed** — Hints 1+2+3 delivered; bilateral arc-completion (Sera+Morreth S03); Mira as compact witness; three Orders assembled.
- **The Dalimvar protocol** — specific instrument: Healing Tier protocol, PC 199-onwards, still operating 300yr later when Calder arrived three days late. The protocol killed forty-one people. The compact allowed it. The new compact must not.
- **Splinter cell intel** — 3 cells; Palanthas contact (name unknown). The splinter faction operates outside Mira's authority. This is the 0012 antagonist.
- **79 days to convergence** (from S04).
- **Party XP: 1,312 each.**

### Campaign-permanent facts (C2-S03 — 2026-04-20)

- **Clause of Grief recovered** — Route D. Bilateral arc-completion: Sera named the settlement; Morreth named Ven. Route D gift delivered (Sera saw settlement intact). Sera carries it (unattuned).
- **Mira Coldsteel permanently stood down** — Unbound Conclave no longer a direct combat threat. Mira will witness the new compact. This is campaign-permanent.
- **Chapel in witness-list** — Calder's promise at the doorway. Campaign-permanent commitment.
- **Three shards: Witness (Thessaly) + Ambition (Orik) + Grief (Sera).** All unattuned.
- **Route D prerequisites: 3/4.**
- **Convergence: 83 days.**
- **Party XP: 1,012 each.**

### Campaign-permanent facts (C2-S05 — 2026-04-20)

- **Clause of Reckoning recovered** — Thessaly, unattuned. Five shards total.
- **Hint 4 delivered** — compact was a protection mechanism. The reckoning is performed in the speaking.
- **Thessaly named Test wound to Vorn Haleth** — first peer to hear it. Campaign-permanent.
- **Vorn Haleth as witness and collaborator** — knows Forgiveness shard location; is drafting accountability language for new compact with Lenne; will witness the compact speaking.
- **Witness-list confirmed (Calder named them):** Mira, Deva, Vorn, Sevven (letter), Morreth's chapel.
- **Five shards:** Witness, Ambition, Grief, Defiance, Reckoning. All unattuned.
- **Route D: 4/4 prerequisites confirmed.**
- **Convergence: 79 days.**
- **Party XP: 1,612 each.**

### Campaign-permanent facts (C2-S07 — 2026-04-20) — CAMPAIGN COMPLETE

- **THE CONCLAVE COMPACT HAS BEEN SPOKEN.** Route D. New compact with Sylaren amendment + Lenne accountability language + Thessaly opening sentence.
- **Thessaly's opening sentence:** "We speak this not to bind the Orders to each other but to bind each Order to the people who live beneath the consequences of what the Orders do."
- **The seventh space in the Istar vault filled.**
- **Witnesses:** Mira, Deva, Vorn, coordinator, Sevven (letter), Morreth chapel (record).
- **Campaign 2: COMPLETE.** Seven adventures, seven sessions, Route D every session, 100% manifest every session.
- **Party XP: 2,312 each.**

### Campaign-permanent facts (C2-S06 — 2026-04-20)

- **Clause of Forgiveness recovered** — Thessaly, unattuned. Six shards total.
- **Last splinter cell stood down** — Calder answered the coordinator's question. She will come to hear the compact. Unbound Conclave field network fully inactive.
- **Thessaly wrote the compact opening sentence** — In reconstruction document margin. Not shared yet. Campaign-permanent: the new compact has a first sentence.
- **Six shards all with Thessaly, all unattuned.**
- **Witness-list complete:** Mira, Deva, Vorn, Sevven (letter), Morreth (chapel record), Coordinator (Calder's invitation).
- **Convergence: 76 days.**
- **Party XP: 1,812 each.**

### Updates

Campaign 2 continuity is updated post-every-session in `HANDOFF-S{N}.md` and aggregated here. If any DM narration contradicts a campaign-permanent fact, the fact wins.

## Campaign 3 — The Halted Spire

**Party:** the-witnesses (Maret Sorn, Calla Fosse, Renn Ashkeld, Dren Holt)
**Campaign:** 7 adventures (0015–0021), halted-spire spine.
**Central question:** *Who gets to decide who is worth saving — and who gets to decide what counts as faith?*
**Outcome:** Route D every session. Keystone set with Velantha's name. Magistra Doran commissioned second cathedral. COMPLETE.

### Campaign-permanent facts (C3 FINAL — 2026-04-21)

- **The Halted Spire is ceded to the congregation of Velantha of Mireth.** Velantha's name is in the keystone. The building is consecrated as what it actually is — a cathedral to an unauthorized miracle, built by the people it saved.
- **Magistra Doran of Mireth commissioned a second cathedral on clean ground.** The commission is signed. Construction begins in spring. She said: *"The town I know will not like this. I am doing it anyway."*
- **Calla Fosse spoke Velantha's true account at the Keystone.** Verbatim in `adventures/0021-the-keystone/sessions/S7-log.md`. Campaign-permanent; the account will not change.
- **The dispensation letter** (Velantha's forged authorization, written by Aldric Voss) is indestructible, warm, and in party custody at campaign end.
- **The healer's journal** final entry after keystone setting: *"They set the stone with my name in it. That is what I would have asked for, if anyone had thought to ask. I am glad."* With Calla.
- **Renn Ashkeld's pact** is known to the full party (disclosed aloud in the Crypt, S6). Three unauthorized acts were in the Keystone room simultaneously: the letter (Aldric's), the working (Velantha's), the pact (Renn's).
- **Dren Holt named what he will do** about Aldis's family (S7). He keeps Aldis's insignia until he finds the family and tells them. Campaign-permanent commitment.
- **Maret Sorn's craft-witness practice** confirmed session-invariant across all 7 sessions. Private three breaths performed before Calla's account — returned to its original form.
- **8 NPC arc-completions** fired by character logic: Mig (S1), Veth (S2), Gorret (S2), Sharr (S3), Morren (S4), Aldric (S5), Velantha (S6), Doran (S7).
- **Party XP: 1,500 each. Level 3. Campaign complete.**

### Campaign-permanent party state (FINAL — post-S7)

- **Maret Sorn** — craft-witness confirmed. Practice is her own. The campaign confirmed it requires no institution, no hall, no witness other than herself.
- **Calla Fosse** — verbal-documentation-arc Stage 3 complete. Account spoken. Journal carries the last rewrite.
- **Renn Ashkeld** — pact known to party. Carries ritual focus (Aldric's mark), warm copper coin, dispensation letter. His pact and Velantha's working and Aldric's copying are all under the same roof now.
- **Dren Holt** — bilateral arc complete. Carries promise-cord (unattuned), Aldis's insignia (pending family). His second arc beat was naming the act.

### Updates

Campaign 3 continuity is aggregated in `HANDOFF-S7.md` and in `docs/campaign/halted-spire-retrospective.md`. Campaign is concluded; no further sessions.

## Campaign 4 — The Thorngate Watch

**Party:** the-relief (Davan Fostermark Fighter/Battle Master, Sava Dawnmere Cleric/Life, Talis Oremm Ranger/Hunter, Caelith Vor Wizard/Divination)
**Campaign:** 7 adventures (0022–0028), thorngate-watch spine.
**Central question:** *How much of yourself do you spend on people who don't trust you yet?*
**Outcome:** Route E achieved Day 36. Siege ended. 47 refugees walked into afternoon light. COMPLETE.

### Campaign-permanent facts (C4 FINAL — 2026-04-22)

- **Siege of Thorngate Keep ended on Day 36.** Commander Saren Coldforge withdrew her forces. The pass remains under Solamnic garrison authority.
- **Route E achieved.** All 7 garrison tokens earned. Both arc-completions fired simultaneously from the parley table.
- **Davan Fostermark's accounting speech spoken at the parley table, Day 36.** Verbatim in `adventures/0028-the-parley/sessions/C4-S7-log.md`. He named his brother Orel Fostermark — the first time in the campaign. The speech synthesizes the letter-vs-people tension that drove the siege for twenty years.
- **Davan named Orel Fostermark aloud for the first time.** At the parley table, to Saren and Asholt. Orel was cashiered from the Order of the Sword following a tribunal at which Davan's testimony was the deciding factor. This is now campaign-permanent and known to all present at the parley.
- **Warden Bren Asholt's arc-completion:** *"She was right about the Oath. I was right about the people. I should have told you that twenty years ago."* Spoken to Saren at the parley table. Campaign-permanent.
- **Commander Saren Coldforge's arc-completion:** *"Twenty years. I knew it the day I left. I didn't know how to come back."* Spoken at the parley table when Asholt gave her the rejoined disc. Campaign-permanent.
- **The garrison disc rejoined.** Asholt's half + party's half. Held by Saren at the table. She kept both halves.
- **47 refugees formally acknowledged.** Dene Flor sheltered them in the lower keep's eastern chambers for three years. Warden Asholt now knows. Saren's withdrawal without contesting it is implicit recognition.
- **Sergeant Caur** (captured Wave 1 sergeant, S4) disclosed the Reconstitution's operating doctrine: *"We're not here for the pass. We're here because she told us there was a question that needed answering before it could change hands."* Prisoner at Thorngate. Not a recurring threat.
- **Mik** (Reconstitution deserter, S6) gave the party H4 intel and requested shelter. At Thorngate under garrison care. Not a recurring threat.
- **Caelith's grey-blue margin annotations** accumulated across 7 sessions converged in S6 with: *"She is not waiting to win. She is waiting to be heard."* Final notation in S7: *"unable to categorize"* under Saren's entry. His notes are in the keep.
- **Talis drew her shortsword (S6).** First melee weapon use of the campaign. She was in the breach beside Davan.
- **The Supply Die never recovered.** Exhausted at S5. Seven sessions with no long rest; Caelith's Portent dice were never reset.
- **Davan's accounting speech:** four layers across four sessions (S4: the Oath doesn't tell me this; S5: letter vs. people; S6: cost of correctness; S7: both sides' expenditures named and Orel named).

### Campaign-permanent party state (FINAL — post-C4-S7)

- **Davan Fostermark** — named Orel at the table. The accounting is complete. Carries Tomek's token, Dene's token, and the rest. The Oath's gap has been spoken aloud to the people who needed to hear it.
- **Sava Dawnmere** — carries Maret's token, Hessa's token. Asked "Why did she leave?" in Asholt's corridor (S6). The supply column has a fresh page.
- **Talis Oremm** — crossed the gap alone to fetch Asholt (S7). Spoke one line to the older girl (S5): "She's been doing this a long time." Carries Asha's cord.
- **Caelith Vor** — asked "What did you need to know?" (S5). Notes closed. Last entry: unable to categorize. Carries Luca's token.

### Updates

Campaign 4 continuity is aggregated in `HANDOFF-C4-S7.md` and in `docs/campaign/thorngate-watch.md`. Campaign is concluded; no further sessions.

## Campaign 5 — The Silken Ledger

**Party:** the-guild (Tessaly Ink Rogue/Mastermind, Darro Velt Rogue/Thief, Mira Calloway Bard/Whispers, Cael Ironback Fighter/Battle Master)
**Campaign:** 7 adventures (0029–0035), silken-ledger spine.
**Central question:** *When the guild you serve becomes the thing you're stealing from, who do you still work for?*
**Outcome:** Route B achieved. Pale investigated and removed. COMPLETE (2026-04-22).

### Campaign-permanent facts (C5 FINAL — 2026-04-22)

- **Orren Pale has been removed as guild master** by Harbor Authority investigation. Revenue Intelligence correspondence extracted from his operational vault and delivered to Rue Ashen. Pale faces investigation. The Silken Ledger continues under different leadership.
- **The false dossier (MARTEN-7) is in Pale's operational vault.** Mira Calloway produced it from six sessions of silent framework accumulation. It describes the party as a low-yield fencing network with no intelligence-gathering component and no Revenue Intelligence value. Pale was removed before he could run an active check on it.
- **Tessaly's ledger is accurate and complete.** Final entry: *0035 / PC 188 / route B / complete. The ledger is accurate. The record stands.*
- **Gale's ledger recovered (S1).** Three named guild members protected.
- **Aldras Bent named Pale on the street (S2)** without being asked — professional debt paid in truth. Bone coin (dockside voucher) held by Tessaly.
- **Pale knew Tessaly's coding conventions** from a billing review 18 months ago. The false dossier used pre-Pale-access era formatting.
- **Pale tested the party at the Anchor Bell (S5)** and knows the code holds. He arranged the test through Pell Dorvast. Pell wrote a voluntary admission note after.
- **Pale found the substitute ledger at the S6 audit** and chose not to call it. He closed the ledger after four seconds of silence. He has been removed before acting on this knowledge.

### Campaign-permanent party state (FINAL — post-C5-S7)

- **Tessaly Ink** — ledger complete and accurate. Guild Markers: Rue Ashen + Aldras bone coin + Gorren Dock Road key. Out of the frame.
- **Darro Velt** — pick set intact (twelve picks, all maintained). Morning maintenance performed the day after campaign ended. Professional identity confirmed as independent of the campaign's narrative.
- **Mira Calloway** — paper case intact; framework (six components) remains inside alongside the three identities of the people she helped disappear. False dossier deployed. The identities are safe.
- **Cael Ironback** — contract with Tessaly honored fully. Disposal clause read and answered by Route B action. The contract terms were met.

### Research Validation Results (C5)

- **RV1 CONFIRMED:** Sheet-deep-reader fires from professional code without grief hooks. Zero grief-triggered instances across 7 sessions, 40+ professionally-triggered instances. Professional code is sufficient and stable as a player-style trigger.
- **RV2 CONFIRMED:** Morally-grey NPC arc-completion by character logic. Aldras (S2, professional debt paid in truth) + Pell (S5, voluntary note from professional response). Both professionally-triggered, no grief, no persuasion.
- **RV3 CONFIRMED:** PC-authored deliverable (false dossier MARTEN-7) accumulated across 6 sessions, produced and placed verbatim in S7. Logged verbatim in C5-S7-log.md.
- **RV4 CONFIRMED:** Act-without-announcement fires from professional code. Mira's framework (six sessions, announced at deployment); Cael's code-stops (S5 — "We're not selling a name to the Watch"; S7 — "Rue gets the correspondence tonight"). All professionally-triggered.

### Mira's False Dossier (verbatim)

**Operational File MARTEN-7 (false version):**
Four-person professional fencing network. No intelligence-gathering component. Cover identities: Heila Voss (accounts regularisation), Berren Wick (dock logistics), Callum Shore (enforcement), Sondra Pen (planning). Client record: textile factor (income regularisation, completed); dock-adjacent merchant (manifesto, cancelled — product deficiency). References: Bessa Tor, Rue Ashen (standard contact). Assessment: low-yield fencing network within normal guild parameters. Independence risk: low. Revenue Intelligence value: none. Recommend: file inactive. Coded in pre-Pale-access era formatting throughout.

*Full verbatim text in `adventures/0035-the-final-job/sessions/C5-S7-log.md` (MARTEN-7 section).*

### Updates

Campaign 5 continuity is aggregated in HANDOFF files per session and in `docs/campaign/thieves-guild.md`. Campaign is concluded; no further sessions.

## Campaign 6 — The Border Watch

**Party:** the-unit (Commander Varet Senn, Medic Lenne Orr, Navigator Taris Cole, Veteran Dorn Ashfeld)
**Campaign:** 7 adventures (0036–0042), border-watch spine.
**Central question:** *When the orders you're following become wrong, how do you know — and who do you tell?*
**Campaign mechanic:** Unit Cohesion Die (d12 → d10 → d8). Degrades when unit member lost or order defied. Die result = soldiers available next session. Between-session HP carry-over (end HP + 1 hit die, capped at max).
**PC-authored deliverable:** Commander Varet's field journal — she documents every order and anomaly; presented verbatim at S7 tribunal.

### Campaign-permanent facts (C6 — CAMPAIGN COMPLETE 2026-04-22)

- **Route E achieved.** Varet presented the field journal verbatim in the tribunal room without permission.
- **Ossian investigation opened.** General Sel Hadren: 48-hour verification. Drev Ossian (Istaran trade factor) → Sorn → Veth → unit. Chain confirmed. Unit on administrative stand-down, full pay.
- **Journal discrepancy count: 7. Outcome count: 3.** Ratio inverted at Day 4; arc fired at Day 7.
- **Unit Cohesion Die: d8 at campaign close.** Degraded twice: d12→d10 (S3, order defied to rescue Brek) and d10→d8 (S6, Carra incapacitated in ambush).
- **Brek Aldren: alive and a witness.** Rescued S3. Testified at tribunal.
- **Carra: incapacitated S6, stabilized.** Present at tribunal.
- **Dorn Ashfeld's arc-completion:** Read Clause 4 to Ossren (S4). Contract held. Third reading at tribunal (Derrath present).
- **Taris Cole's arc-completion:** Showed map to Varet, S5. "I made it legible when I saw what it was."
- **Lenne Orr's arc-completion:** Named three "cause: unclear" entries aloud at tribunal. Handed medical log to Major Fey.
- **Arren Vole's arc-completion:** "Nine years. It was in the journal the whole time." Spoke as himself when asked directly.
- **Varet Senn's arc-completion:** Read journal verbatim in tribunal room. "This is my accurate report."
- **Captain Veth's arc-completion:** "I knew what the orders said. I didn't know what they meant."

### RV research verdicts (C6 — FINAL)

- **RV5 CONFIRMED:** Depletion-amplification. Character Agency 7→8→9→10→10→10→10 across 7 sessions. Cohesion Die depletion tracks inversely with agency scores. Tracking other people (not party HP) produces the same amplification pattern.
- **RV6 CONFIRMED:** Journal accumulates reception layer (margin notes) beyond designed column structure from Day 1. Self-referential arc-firing: "the arc fires" written in journal, read aloud at tribunal. The journal was the arc, not the record of the arc.
- **RV7 CONFIRMED:** Duty-spine mean 74.6/80 vs grief-spine (C1) comparable. Campaign spine built on duty/obedience central question produces equivalent emotional density. The driver is obligation-collision, not spine-type.
- **RV8 CONFIRMED:** PC-authored deliverable as document produces MORE effect than speech in institutional context. Evidence (field provenance) vs. advocacy (composed for occasion). Derrath could not challenge journal dates.

### Updates

Campaign 6 continuity is aggregated in HANDOFF files per session and in `docs/campaign/border-watch-retrospective.md`. Campaign is concluded; no further sessions.

## Campaign 7 — The Convergence

**Party:** the-strangers (Brek Ashfall, Sera Windholt, Tam Overfield, Vess Ironmark)
**Campaign:** 7 adventures (0043-0049), the-convergence spine.
**Central question:** *When people with nothing in common have to act as one, what do they actually share?*
**Outcome:** Route E. All four chose the south road from Stonehaven's south gate, Day 8. COMPLETE.

### Campaign-permanent facts (C7 FINAL — 2026-04-22)

- **The four travelers chose the south road together** from Stonehaven on Day 8. No ceremony. No name for the group. Vess found a reason; Brek named completion; Tam arranged his circuit; Sera walked through without speaking.
- **Maret Sunn's inn** is gone (fire, Day 2). She is rebuilding at the stable. Her son helped build it (eight years ago, fourteen years old). Arc complete.
- **Elder Daven Sorr** reached Haverford with her eleven refugees. Named her garden (forty years) to Tam. Gave him three seed packets. Arc complete.
- **Warden Cassel** admitted Vess was never the target — she was used as a test shipment for the Doss network investigation. Cassel's arc complete.
- **Torven Aldric's** operation at the river ford is ended. He had the money prepared (240 gp, two years in a pouch). Brek collected it and split it four ways: 60 gp each.
- **Vess redirected the package** — forfeited 50 gp delivery fee, "refused delivery" notation on courier license. Package and Torven's documents sent to Cassel's investigation.
- **Havel** (the merchant from Session 1) was the Doss network's courier-scout. He was at the roadblock specifically to confirm Vess's package was in transit.
- **Sera is going to Millhaven** to find out what happened to Torvens Mikela (researcher, disappeared three months prior, likely detained at a toll station). Committed without deliberation (first time in campaign).
- **Tam carries Elder Sorr's three seed packets** in his breast pocket.
- **Vess at camp**: within sight of the fire. Position change from seven sessions of sitting outside the firelight.
- **25 Reciprocal Acts** across 7 sessions. Trigger type arc: situational (S1-S3) → relationship-driven (S4-S7).

### RV9-RV12 Verdicts (FINAL)

- **RV9 POSITIVE:** Player styles fired situationally S1-S3 (7 instances before any relationship existed); shifted to relationship-driven S4-S7. Same player styles, trigger-type change tracks session number.
- **RV10 POSITIVE:** Tam S6: "I suppose we're traveling the same road tomorrow." Route E S7: four simultaneous relational choices.
- **RV11 POSITIVE:** Route E by genuine character logic, four PCs with no grief paragraphs, no loyalty objects, no professional codes.
- **RV12 POSITIVE:** Maret (S2), Sorr (S3), Cassel (S4) — all three before S6, all from situational acts or smart questions.

### Updates

Campaign 7 continuity is aggregated in HANDOFF files per session and in `docs/campaign/the-convergence-retrospective.md`. Campaign is concluded; no further sessions.

## Canon Policy

**QUEST is Dragonlance-native, not Dragonlance-adjacent.** We invent where Dragonlance is silent. We do not contradict canon where canon speaks. Every invented name (location, character, item, event) is tracked in `reference/dragonlance/workshop-canon.md`.
