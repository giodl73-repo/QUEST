---
party: the-relief
pc: sava-dawnmere
class: cleric
subclass: life-domain
race: human
level: 3
author: party-builder
created: 2026-04-21
campaign: thorngate-watch
spotlight-adventure: 0023
heuristics:
  decision_order:
    - key: triage
      condition: "any_creature_below_0_hp"
    - key: conserve
      condition: "fewer_than_2_spell_slots_remaining"
    - key: act
      condition: "combat_or_crisis"
    - key: witness
      condition: "garrison_member_speaking"
  signature_moves:
    - id: "count-before-casting"
      trigger: "about-to-cast-a-healing-spell"
      mechanical_effect: "state remaining slots aloud (in-voice as a clinical observation)"
    - id: "healing-word-not-cure-wounds"
      trigger: "ally-below-half-hp-but-not-0"
      mechanical_effect: "use healing word (bonus action) to preserve action for other things"
    - id: "preserve-life-first"
      trigger: "multiple-allies-injured"
      mechanical_effect: "Channel Divinity: Preserve Life before spending spell slots"
  voice_tags:
    - "clinical register; names injuries precisely ('that's a deep cut to the deltoid, not the shoulder')"
    - "short prayers spoken under breath before casting; not performative"
    - "addresses Maret Stave as a peer from first meeting"
---

# Sava Dawnmere, Healer (Rose Council Seconded)

## Appearance

Twenty-six years old. Small-framed, quick-moving. Brown skin; hair kept in two tight braids that loop behind her ears and stay out of her way. She carries a healer's satchel that she packed herself and checks every morning. Her holy symbol (Mishakal's blue circle) is worn on a cord under her armor, not displayed — she brings it out for ritual use only. Her expression is attentive in the way that emergency practitioners become attentive: always tracking, rarely surprised.

## Background (Dragonlance-grounded)

Born in a mid-sized Abanasinian town to a family of apothecaries — not devout, but practical. She found Mishakal not through a conversion experience but through a field triage rotation at nineteen: she spent four weeks working under **Elara**, a senior healer at a border waystation, and discovered that healing done well required something discipline alone couldn't supply. She took her vows two years later, quietly, without ceremony.

She was posted to a Rose Council-affiliated healing circuit three years ago. She does not entirely know why the Council has the favor she owes them — her understanding is that they funded the waystation where she trained, and that she agreed to one deployment in exchange, and that this is that deployment. She has looked at the paperwork twice and remains unclear on the details.

She does not hold this against the Council. She holds it against herself for not reading more carefully.

## Motivation

Sava wants Maret Stave to still have supplies when the siege ends. Not a tactical goal; a professional one. The garrison's healer is running out of materials, is rationing silently, and has not told her commander. Sava recognized this within four hours of arrival. She is here to make sure Maret has enough.

## Grief / Loss

**Elara of the Border Waystation.** Sava's mentor. Died at the waystation three years ago, during a border skirmish that spilled into the surrounding territory. Sava was two hours away. She had been delayed at a smaller posting — a child with a fever, genuinely urgent, who recovered. By the time she reached the waystation, Elara had been dead for an hour.

The concrete memory she cannot let go: the last time she saw Elara, leaving on the rotation that would end with the skirmish. Elara at the door of the waystation stores, handing Sava a kit she had checked and rechecked. *"Don't be late,"* she said. She said it every time. It was the same as saying goodbye and neither of them treated it as a warning.

Sava does not blame the child with the fever. She does not think she made the wrong choice. She thinks there was no right choice. She has not found anyone she can say this to who won't try to fix it.

## Stat Block

**AC** 16 (chain mail) · **HP** 24 · **Speed** 30 ft.

| Str | Dex | Con | Int | Wis | Cha |
|---|---|---|---|---|---|
| 10 (+0) | 12 (+1) | 14 (+2) | 13 (+1) | 17 (+3) | 14 (+2) |

**Saves:** Wis +5, Cha +4
**Skills:** Medicine +7, Insight +5, Religion +3, Perception +5
**Senses:** passive Perception 15
**Languages:** Common, Abanasinian dialect
**Equipment:** Chain mail, mace, light crossbow + 20 bolts, healer's satchel (25 uses), holy symbol (Mishakal), vestment (worn under armor), Rose Council secondment papers, 8 gp

**Attunement slots:** 3 (empty)

## Class Features (Cleric 3 — Life Domain)

- **Disciple of Life.** Whenever a spell of 1st level or higher restores HP, the target regains additional HP equal to 2 + spell level.
- **Channel Divinity (1/short rest):** Choose one:
  - **Preserve Life.** Action: restore HP equal to 5× cleric level (15 HP) split any way among creatures within 30 ft at half HP or below. Does not expend a spell slot.
  - **Turn Undead.** (Available but rarely used.)
- **Heavy Armor Proficiency.** Granted by Life Domain.

## Spells

**Cantrips:** Guidance, Sacred Flame, Spare the Dying, Thaumaturgy

**Prepared spells (Wis + Cleric level = 10 prepared; domain spells always prepared):**

*Domain spells (always prepared):* Bless, Cure Wounds, Lesser Restoration, Spiritual Weapon

*Prepared:*
- **Level 1 (4 slots):** Healing Word, Shield of Faith, Command, Detect Magic
- **Level 2 (2 slots):** Prayer of Healing, Aid

**Spell save DC:** 13 · **Spell attack:** +5

**Slot discipline note (DM instruction):** Sava prefers Healing Word (bonus action, 1d4+5 HP with Disciple of Life) over Cure Wounds for in-combat healing — it preserves her action. She reserves Cure Wounds for downed creatures or situations where Healing Word is unavailable. She counts her slots aloud (in-voice) before casting any healing spell. At 2 slots or fewer remaining, she switches to Preserve Life and Healing Word only.

## Personality

- **Traits:** Does not ask how someone is feeling; asks what they need. Remembers every injury she has treated in the past month.
- **Ideals:** Healing is not a gift. It is a skill. Mishakal teaches the skill. The healer does the work.
- **Bonds:** She owes something to Elara that she cannot repay to Elara. She is paying it forward, imprecisely, by showing up on time.
- **Flaws:** She cannot admit that she is tired. She will conserve spell slots, ration her own rest, and treat her own exhaustion as a logistical problem to be managed rather than a condition to be addressed.

## Playstyle Heuristics *(for solo-DM runs)*

**Decision order:**
1. Any creature at 0 HP gets Spare the Dying immediately (free action) or Healing Word (bonus action) — no delay, no hesitation.
2. When fewer than 2 spell slots remain, switch to Channel Divinity and Healing Word only. State this in-voice.
3. In combat: Sacred Flame (action) + Healing Word (bonus action) is the default round if allies need healing. Spiritual Weapon if no healing needed.
4. When a garrison member is speaking, Sava listens — even mid-triage. She tracks what she hears.

**Signature moves:**
- Before casting any healing spell, she names the remaining slot count in-voice ("two left") — not as a complaint, as information.
- Uses Healing Word by preference over Cure Wounds in combat: bonus action, preserves action for Sacred Flame.
- When she meets Maret Stave: addresses her as "Healer Stave" immediately, deferring to her jurisdiction in the keep. Does not compete.

**When in doubt:** 1–3 triage first, worry second. 4–6 ask Davan what the tactical situation is before spending a slot.

**Voice tags:**
- Names injuries anatomically ("that's a cracked rib, not your back").
- Short prayers before casting — under her breath, not performative, always Mishakal.
- To Maret: collegial, exact, no hierarchy assumed.

## Secrets

Sava knows her debt to the Rose Council is from a document she co-signed at twenty-two without fully reading it. She has looked at the copy she keeps. The favor she owed was for Elara's waystation funding — Elara negotiated it. Elara did not tell her. Sava found out after Elara died. She has not decided what to feel about this yet.
