---
party: the-relief
pc: talis-oremm
class: ranger
subclass: hunter
race: half-elf
level: 3
author: party-builder
created: 2026-04-21
campaign: thorngate-watch
spotlight-adventure: 0024
heuristics:
  decision_order:
    - key: terrain
      condition: "entering-any-new-location"
    - key: intel
      condition: "before-any-action-sequence"
    - key: solo
      condition: "reconnaissance-or-stealth"
    - key: cover
      condition: "ranged-combat"
  signature_moves:
    - id: "read-the-ground"
      trigger: "entering-new-location"
      mechanical_effect: "free Perception or Survival check; state what she notices; does not wait to be asked"
    - id: "goes-alone"
      trigger: "reconnaissance-required"
      mechanical_effect: "volunteers to go solo; does not invite accompaniment"
    - id: "covers-retreat"
      trigger: "any-party-member-withdrawing"
      mechanical_effect: "stays between the party and the threat; last one through any door"
  voice_tags:
    - "gives directions as cardinal bearings and distances, not landmarks"
    - "does not explain conclusions, just states them: 'three, maybe four hours old'"
    - "uses 'we' to mean the party; uses 'I' only for solo assessments"
---

# Talis Oremm, Scout (Rose Council Contracted)

## Appearance

Twenty-nine years old. Lean and long-limbed, with the unhurried economy of movement that comes from years of keeping pace with terrain rather than fighting it. Her half-elven heritage shows in the slight taper of her ears and the unusual stillness of her eyes — she watches exits before she watches faces. Dark hair pulled back with a cord of the same kind she uses for bowstrings. Shortbow worn across her back, shortswords at both hips. She dresses in the grays and muted greens of the Kharolis foothills and smells faintly of pine resin, which she uses to weatherproof her bowstring.

## Background (Dragonlance-grounded)

Born in a border-country settlement in the Kharolis foothills to a human mother and an elven father who was passing through. The elven half of her inheritance gave her the patience and the ears; the border-country gave her the practical skills. She has been contracting as a scout and guide since she was nineteen — work for Solamnic survey parties, merchant escorts, the occasional Rose Council assignment when they needed someone who knew the passes.

She and her working partner **Asha** ran together for four years. Asha was the better climber; Talis was the better tracker. They divided terrain between them by instinct and had not needed to negotiate it in three years when Talis walked them into an ambush she had read wrong. The first volley took Asha. Talis was twenty-six feet ahead and did not see it happen.

She has not taken a partner since. The Rose Council contract to reinforce Thorngate came through a Palanthas intermediary; she accepted because she knows The Needle's terrain better than anyone currently alive, and she does not have a better reason to be somewhere else.

## Motivation

Talis wants a route out of the keep — an escape path, a secondary exit, something that isn't the main gate — identified before the next major assault. She has not told the garrison she is looking. She does not ask for permission for reconnaissance.

## Grief / Loss

**Asha Coldpath.** Talis's working partner of four years. Died three years ago in an ambush on a secondary pass twenty miles northwest of The Needle — an ambush Talis read wrong. Asha had trusted Talis's assessment of the terrain. Talis had said: *"Probably clear."* She had known it was a maybe, not a probably.

The concrete memory: Asha's voice on the morning of the patrol, before they moved out. She was re-lashing her pack — always re-lashing her pack, three times before every patrol, left strap before right — and she said, without looking up: *"You've got that face. What do you see?"* Talis said: *"Probably nothing."* Asha tightened the right strap and stood up and that was the last time they spoke where Talis could answer.

Talis has not said the word "probably" in three years. She says "likely" or "unclear" or "I don't know." The verbal edit is the only external sign of what she carries.

## Stat Block

**AC** 15 (studded leather) · **HP** 28 · **Speed** 30 ft.

| Str | Dex | Con | Int | Wis | Cha |
|---|---|---|---|---|---|
| 12 (+1) | 17 (+3) | 14 (+2) | 11 (+0) | 15 (+2) | 10 (+0) |

**Saves:** Str +3, Dex +5
**Skills:** Perception +6, Stealth +7, Survival +6, Athletics +3, Nature +2
**Senses:** passive Perception 16; darkvision 60 ft.
**Languages:** Common, Elvish, Kharolis border-dialect
**Equipment:** Studded leather, shortbow + 40 arrows, shortsword ×2, explorer's pack, climber's kit, 50 ft hempen rope, Rose Council contract (letter), 14 gp, a cord of braided bowstring (Asha made it; Talis has never used it)

**Attunement slots:** 3 (empty)

## Class Features (Ranger 3 — Hunter)

- **Favored Enemy: Humanoids (two types: Solamnic, Nerakan).** Advantage on Survival checks to track; advantage on Int checks to recall info about them.
- **Natural Explorer: Mountain.** Difficult terrain doesn't slow group travel; always alert for danger; advantage on Initiative in favored terrain; group can't become lost by non-magical means.
- **Primeval Awareness.** Expend a spell slot to sense favored enemies within 1 mile (6 miles in favored terrain) for 1 minute per slot level.
- **Hunter Archetype — Colossus Slayer.** Once per turn, deal extra 1d8 damage to a creature below its HP maximum.

## Spells

**Spell slots:** 3 × Level 1

**Known spells:**
- **Level 1:** Hunter's Mark, Longstrider, Cure Wounds, Alarm

**Spell save DC:** 12 · **Spell attack:** +4

**Spell discipline note:** Talis treats Hunter's Mark as her primary combat spell — tracking the highest-threat target and moving it if that target goes down. She uses her remaining slots for Longstrider (before going outside the walls) and Cure Wounds only as emergency backup if Sava is down.

## Personality

- **Traits:** Reports what she observes, not what she infers, unless asked. Checks exits before sitting down.
- **Ideals:** Accurate information is more valuable than reassuring information. Give the real read, even when it's "I don't know."
- **Bonds:** She owes Asha a better read than the one she gave. She pays the debt by not saying "probably" again.
- **Flaws:** She will not ask for help with reconnaissance. She will work alone past the point where it is wise, because she does not trust her own assessment of terrain enough to bet anyone else's life on it.

## Playstyle Heuristics *(for solo-DM runs)*

**Decision order:**
1. On entering any new space: Perception or Survival check, state what she sees, do not wait to be asked.
2. Before any action sequence: state the terrain — exits, cover, lines of sight. One sentence.
3. If reconnaissance is required, she volunteers to go alone. Does not invite company.
4. In ranged combat: find cover, use Hunter's Mark, use Colossus Slayer on the most damaged target.

**Signature moves:**
- Last one through any door or bottleneck — she covers the retreat.
- Does not say "probably." Uses "likely," "unclear," or "I need to look again."
- When she gives Luca permission to come with her in 0026 (if the party goes after him), she says it once and does not repeat the offer.

**When in doubt:** 1–3 go alone and report back. 4–6 ask Davan to come and take point.

**Voice tags:**
- Directions by bearing and distance: "forty meters, northeast, behind the second buttress."
- Conclusions stated, not argued: "three hours old, maybe four."
- Does not say "probably."

## Secrets

The cord braided from Asha's bowstring has been in Talis's kit for three years, coiled under everything else. She has not thrown it away. She has not used it. She does not know what she is waiting for.
