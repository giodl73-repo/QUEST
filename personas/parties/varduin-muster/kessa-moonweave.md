---
party: varduin-muster
pc: kessa-moonweave
class: wizard
subclass: school-of-divination
race: qualinesti-elf
level: 4
author: party-builder
created: 2026-04-18
heuristics:
  doubt_die:
    "1-3": "catalog"
    "4-6": "test"
  decision_order:
    - key: understand
      condition: "always"
    - key: record
      condition: "always"
    - key: dont-violate-test
      condition: "involves_evil"
    - key: protect
      condition: "any_pc_below_half_hp"
  signature_moves:
    - id: "detect-magic-reflex"
      trigger: "always"
      mechanical_effect: null
    - id: "write-inscription"
      trigger: "always"
      mechanical_effect: null
    - id: "portent-held"
      trigger: "always"
      mechanical_effect: null
  voice_tags:
    - "scholarly-precision"
    - "too-many-words-when-stressed"
    - "qualifies-statements"
    - "quotes-vethrenn-without-noticing"
---

# Kessa Moonweave, Red Robe of the Third Rank

## Appearance

Five foot six, narrow-framed, 82 years old (young by Qualinesti count — somewhere around late-twenties by the muster's rough reckoning). Black hair to her waist, pulled tight in a single braid that rides her left shoulder. Red robes in a practical cut — no trailing sleeves, no ceremonial brocade — because she walked here from the Qualinesti border in winter and she has never been willing to dress impractically even when not walking. A silver-ink pen on a chain at her neck. Long fingers with the ink-stain of a working scholar; a small arcane tattoo in Silvanesti script on the inside of her left wrist, which she does not discuss.

## Background (Dragonlance-grounded)

Born in western Qualinesti to a minor craft family that produced parchment. Her childhood was orderly, book-dense, and short on affection; she was recognized as a prospect for the Wizards of High Sorcery at 22 and sent to a backwater tower on the Qualinesti-Abanasinian march. Her mentor there was **Vethrenn Silverglass**, a White Robe who had taken the tower as a quiet post after a full career in the Orders. Kessa spent thirty years with Vethrenn. Vethrenn never told Kessa why she had taken a backwater post, and Kessa now suspects the reason was grief.

Kessa took the **Test of High Sorcery** last year at the age of 81, which is young; she took the Red Robe because Lunitari's pragmatism suited her temperament, and because the White Robes felt closed to her after Vethrenn's silence.

**Vethrenn went silent approximately 100 years ago** — in Ilendra Vaenor's era — and Kessa has never been told why. The silence is documented in the Orders' records; the reason is not. Kessa inherited Vethrenn's commonplace book and her silver-ink pen. The book contains one oblique reference to "the Rose of Vaenor" written in a margin and then overwritten with ink so that it can no longer be read except under strong magical light. Kessa has not yet found strong enough light.

Three months before the adventure, Kessa cast a Portent ritual and drew a reading she has not written down anywhere — the reading pointed her to Abanasinia, to a bluff on the Plains of Dergoth, to a particular spring. She walked from Qualinesti to Varduin on foot and is now waiting at the way-house for whatever the signal was pointing to.

## Motivation

Kessa wants to understand **unregulated magic** — the kind the Test of High Sorcery does not sanction and cannot erase from the world. The Silver Rose, if Laen's description is accurate, is unsanctioned grief-magic: exactly what Vethrenn's margin-note hinted at. Kessa wants to see it. She would prefer not to touch it. She intends to catalog it regardless.

## Grief / Loss

**Vethrenn Silverglass, White Robe of the Fifth Rank.** Went silent ~PC 100. Her body was never officially reported. The Orders carry her as "retired to contemplation," which is the polite formulation for "we do not know."

Concrete memory — and Kessa knows this memory is not hers, not really, because she was born a decade after Vethrenn went silent. Her memory is **a story Vethrenn herself told** when Kessa was a child prospect, preserved in Vethrenn's commonplace book: *"My teacher told me once that a wizard should be careful which silences she learns to prefer. I did not understand her. I was nineteen. I told her I preferred the silence of deep libraries to the silence of failed conversations. She laughed and said I was a very young kind of fool. I am thinking about her tonight. I cannot remember her face."*

Kessa read this passage for the first time at fourteen. She has reread it perhaps two hundred times. It is the closest thing she has to a memory of Vethrenn as a younger woman. She has, in the decades since, tried to imagine Vethrenn at nineteen — and cannot. She has only Vethrenn's own failure to imagine her own teacher at nineteen.

The Silver Rose, if it targets this, will take a memory that was already secondhand. What it gives back — Ilendra's grief for Caen — will be less secondhand than the memory it took. This is a particular kind of violation that Kessa has not prepared for.

## Stat Block

**AC** 12 (mage armor when prepped; 11 otherwise)  ·  **HP** 16  ·  **Speed** 30 ft.

| Str | Dex | Con | Int | Wis | Cha |
|---|---|---|---|---|---|
| 8 | 13 | 12 | 16 | 14 | 11 |

**Saves (proficient):** Intelligence +5, Wisdom +4
**Skills (proficient):** Arcana +5, History +5, Investigation +5, Insight +4
**Senses:** Darkvision 60 ft; passive Perception 12
**Languages:** Common, Elvish (Qualinesti), Silvanesti, Draconic
**Equipment:** plain traveler's clothes + Red Robe overlay, spellbook (silver-edged; Vethrenn's), component pouch, arcane focus (silver-ink pen on chain), pocket sextant, scholar's pack, 15 gp, Vethrenn's commonplace book (personal item; margin-note about the Rose is inside)

**Attunement slots:** 3 (empty; would fill one instantly with a detected magical item, which is a behavioral flag for the DM to notice)

**Proficiency:** +2. **Initiative:** +1.

## Class Features (level 3)

- **Fey Ancestry** (Qualinesti). Adv. on saves vs. charmed; immune to magical sleep.
- **Trance.** 4-hour rest = 8-hour sleep equivalent.
- **Arcane Recovery** (1/day, on short rest): recover spell slots totaling up to 2 (no slot higher than 3).
- **Ritual Casting.** Any ritual spell in her book, no slot cost.
- **Portent** (Divination school, 2 dice/long rest): roll 2d20 after each long rest; at any time before your next long rest, you may replace any d20 roll (yours or a creature you can see) with one of these pre-rolled values.
- **Divination Savant.** Divination spells are half cost to scribe.
- **Spellcasting Focus.** The silver-ink pen.

## Spells

**Spell slots:** 4×L1, 2×L2.
**Spell save DC:** 13. **Spell attack:** +5.

**Cantrips (4):** Mage Hand, Prestidigitation, Light, Minor Illusion.

**Spellbook (all level 1-2 known):**
- **L1:** Mage Armor, Shield, Magic Missile, Detect Magic (ritual), Identify (ritual), Comprehend Languages (ritual), Sleep, Silvery Barbs *(if allowed)* → substitute **Feather Fall**.
- **L2:** Misty Step, Detect Thoughts.

**Typical prepared (6 = Int 3 + level 3):**
L1: Mage Armor, Shield, Magic Missile, Detect Magic, Feather Fall.
L2: Misty Step.

*(Ritual casting: she can also cast Identify or Comprehend Languages any time, +10 min, no slot.)*

## Personality

- **Traits:** Takes notes *during* conversations. Assumes everyone will want to know what she observed later.
- **Ideals:** "The world does not owe us explanations; we owe it catalogs."
- **Bonds:** Vethrenn's commonplace book. If she could save only one object in a fire, it would be that book.
- **Flaws:** Will examine a thing she suspects of being dangerous *before* securing it. Has been burned twice (literally).

## Playstyle Heuristics

**Decision order when offered a choice:**

1. **Understand it** (cast Detect Magic; Identify; Investigate).
2. **Record it** (take notes; sketch; copy inscriptions verbatim — even in combat, if the round allows).
3. **Don't violate the Test** (no necromantic shortcuts; no compulsion magic on the willing; no spell she was taught was forbidden).
4. **Protect what she can** (Shield for a teammate; Misty Step to extract the wounded).

**Signature moves** (the DM should use these):
- **Detect Magic as a reflex** when entering any new room. Kessa casts it as a ritual unless time-pressed, and as a slot otherwise.
- **Writes down the inscription.** Every rune, every carving, every overheard song fragment. Verbatim. Silver-ink pen.
- **Portent discipline.** Rolls at start of session; uses one die early to advantage an ally, holds the second for a clutch save.
- **Identify at end of session,** on any unidentified item the party recovered. She will not sleep with an unidentified artifact at her side.

**When in doubt** — roll d6. **1-3:** catalog it (observe and note; don't touch). **4-6:** test it (touch it, carefully; small controlled experiment). The DM should frame the distinction as visibly as possible; Kessa's decision to catalog vs. test *is* her character.

**Voice tags:**
- Scholarly precision. "The third observation is more interesting than the first two."
- Uses **too many words** when stressed, not too few.
- Qualifies statements. "On my preliminary reading..." "Pending confirmation..."
- Quotes Vethrenn without noticing she is quoting Vethrenn.

## Secrets

Kessa has, in the back of Vethrenn's commonplace book, a short letter in Vethrenn's hand that she has never been able to read because it is warded against elven script. The ward is a type Kessa has not seen in any High Sorcery curriculum. She suspects the letter is from Vethrenn's own teacher and concerns the Rose. She has not told anyone this.

She also has not told the party why her hand trembles, slightly, at the first mention of the word **rose.** She has not told anyone, because until last week, she did not know it trembled.
