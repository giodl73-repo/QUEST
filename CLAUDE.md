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

### Campaign-permanent party state (post-S03)

- **Varduin Muster** is a four-PC party at **XP 1,675 each (L3; 125 shy of L4).** Next adventure should guarantee L4.
- **Aelric** attuned to the Varran-reliquary (1/3 slots used). Memory-state unchanged. **New:** a silver pendant from Mira's rack, gifted Scene 7 — "made in anger last year," no mechanical effect, sentimental only.
- **Thera** carries Pella's drawings + Vesk's sealed letter "to P, when you are ten" + **Seralen's *"Do not look"* note** (S03 Scene 6, folded three times in her pocket; unexamined) + scouts' map + Lorn's longbow + Pevra's worry-stones (Idra's).
- **Kessa** carries Keloth's mother's bracelet (unattuned, archival) + S02 vault-ledger transcription + **Aelwen's journal page (Hint 4 pre-plant)** + **Kann's Stonfold moon-silver finger-bone (ID'd; "Felor" engraved; unattuned)** + ledger-phrase transcription (S03 recovery; pattern-link pending). **Portent [1] still held.**
- **Grom** carries Duren's tongs + Istari traveler's token + **~8 oz inert un-forged Mirror moon-silver** (post-destruction) + **Mira's Council file-note with Seralen's name in ink.** Did not shatter any S02 reliquary; the 5 shelf-reliquaries + 1 empty remain with Rose Council.

### Updates

Campaign-continuity is updated post-every-session in `HANDOFF-S{N}.md` and aggregated here. If any DM narration contradicts a campaign-permanent fact, the fact wins.

## Canon Policy

**Marathon is Dragonlance-native, not Dragonlance-adjacent.** We invent where Dragonlance is silent. We do not contradict canon where canon speaks. Every invented name (location, character, item, event) is tracked in `reference/dragonlance/workshop-canon.md`.
