---
party: the-relief
pc: caelith-vor
class: wizard
subclass: school-of-divination
race: human
level: 3
author: party-builder
created: 2026-04-21
campaign: thorngate-watch
spotlight-adventure: 0026
heuristics:
  decision_order:
    - key: information
      condition: "unknown-situation"
    - key: portent
      condition: "critical-roll-upcoming"
    - key: protect
      condition: "sava-below-half-hp"
    - key: wait
      condition: "conflict-between-authority-structures"
  signature_moves:
    - id: "name-the-institution"
      trigger: "any-authority-conflict"
      mechanical_effect: "states aloud which institution each party is representing and why; does not take sides yet"
    - id: "portent-as-gift"
      trigger: "ally-making-critical-roll"
      mechanical_effect: "offer Portent die to ally; frame as in-voice observation"
    - id: "write-it-down"
      trigger: "any-npc-gives-significant-information"
      mechanical_effect: "notes it in a small book; reads it back to the party at the next scene transition"
  voice_tags:
    - "asks 'what does [institution] actually want here?' before acting"
    - "frames magical effects with their mechanism, not their name ('this will let you see what I need to know')"
    - "pauses at the point in any conversation where someone is about to follow an order they don't agree with"
---

# Caelith Vor, Diviner (Unaffiliated)

## Appearance

Thirty-three years old. Unremarkable height; slightly stooped from years of reading. Sandy hair that is longer on one side than the other, as though he started a haircut and lost interest. He dresses practically — no robes, no insignia of the Red Order he left — and carries a battered leather messenger's case that holds his spellbook, a folded star chart, a stub of charcoal, and a small blank book for notes. His eyes are the faint color-shift common to Divination wizards who use Portent often: a half-second delay between noticing something and reacting to it, as though he is checking what he already knows against what he is seeing.

## Background (Dragonlance-grounded)

Born in a minor scholarly family in Palanthas. Showed arcane aptitude at fourteen and was taken on by the Wizards of High Sorcery for testing at sixteen. He spent eight years at the Tower of High Sorcery in Palanthas as a student of the Red Robes — passing all preliminary examinations, completing two years of supervised research under **Magistra Vonn**, and then leaving voluntarily six months before he was scheduled to take the Test.

The formal record says: "withdrew for personal reasons." This is accurate as far as it goes.

He has been contracting as an independent arcane consultant since — survey work, document authentication, the occasional Rose Council commission. The Rose Council hired him for this deployment because they needed someone with practical arcane utility who was not affiliated with the Orders and would not complicate the politics of a Solamnic internal dispute with Conclave involvement.

He accepted the commission. He did not ask why they specifically needed someone unaffiliated.

## Motivation

Caelith wants to understand why the Reconstitution is really here. The stated strategic rationale does not add up — The Needle has not been a primary supply route for three years. He is not going to say this aloud until he knows more. He is already looking.

## Grief / Loss

**Magistra Vonn.** Caelith's supervising instructor at the Tower of High Sorcery. Died during the Test of a student named **Pell** — a third-year student Caelith had studied alongside for two years. Pell failed. Magistra Vonn was present as an examiner; the Test's conditions took her. Caelith was observing, as a senior student, from a shielded alcove.

He believes he could have intervened. The rules of the Test forbid intervention. He obeyed the rules.

The concrete memory: Magistra Vonn's voice through the alcove partition, six seconds before the end — she was saying something in the formal Examiners' register that he could not hear clearly. Not a warning; an assessment. She did not sound afraid. She sounded precise, which was how she always sounded, and then she was not speaking.

He left the Orders six months later. He has not connected these two events aloud to anyone. He has not decided whether the connection is real or whether he is looking for a cause because causes are neater than randomness.

## Stat Block

**AC** 12 (no armor; 15 with Mage Armor active) · **HP** 17 · **Speed** 30 ft.

| Str | Dex | Con | Int | Wis | Cha |
|---|---|---|---|---|---|
| 9 (-1) | 14 (+2) | 13 (+1) | 17 (+3) | 12 (+1) | 13 (+1) |

**Saves:** Int +5, Wis +3
**Skills:** Arcana +5, History +5, Investigation +5, Insight +3, Perception +3
**Senses:** passive Perception 13
**Languages:** Common, Solamnic, Elvish, Draconic
**Equipment:** No armor (Mage Armor active when in danger), dagger, spellbook, arcane focus (polished obsidian sphere), messenger's case, Rose Council contract (letter), blank notes-book, charcoal stub, 11 gp

**Attunement slots:** 3 (empty)

## Class Features (Wizard 3 — School of Divination)

- **Arcane Recovery.** Once per day on short rest, recover spell slots totaling up to half wizard level rounded up (2 levels max). Cannot recover slots of 6th level or higher.
- **Divination Savant.** Halve time and cost to copy Divination spells into spellbook.
- **Portent (2 dice).** After long rest, roll 2d20 and record results. Can replace any attack roll, saving throw, or ability check by a creature Caelith can see with one of these rolls. Must choose before the roll; the die is spent after use. Resets on long rest.

**Between-session note:** Under the campaign's resource-exhaustion mechanic, Portent dice do NOT reset between sessions — they reset on long rest only. Because the party does not receive a full long rest between adventures, Caelith may carry over Portent dice from one session to the next OR lose them if he used them. The session-runner should track Portent die state at session end in the handoff.

## Spells

**Cantrips:** Fire Bolt, Prestidigitation, Mage Hand, Minor Illusion

**Spellbook contains (DM reference):**
- **Level 1:** Mage Armor, Magic Missile, Detect Magic, Identify, Comprehend Languages, Find Familiar, Alarm
- **Level 2:** Misty Step, Suggestion, See Invisibility

**Prepared (Int + Wizard level = 9 max):**
- **Level 1 (4 slots):** Mage Armor, Magic Missile, Detect Magic, Identify
- **Level 2 (2 slots):** Misty Step, Suggestion

**Spell save DC:** 13 · **Spell attack:** +5

**Slot discipline note:** Caelith casts Mage Armor at the start of any session where combat is expected. This costs one L1 slot before the session begins — an intentional resource tax. He uses Magic Missile for reliable damage when Portent dice are not available. He does not cast Suggestion unless the outcome has more value than the slot.

## Personality

- **Traits:** Identifies what each party in any dispute actually wants, separately from what they are saying. Writes things down.
- **Ideals:** Rules serve purposes. When you follow a rule past its purpose, you are not honoring the rule; you are hiding behind it.
- **Bonds:** He owes Magistra Vonn the acknowledgment that the rules he followed to let her die were not wrong. He has not found the framing for this that does not make him the villain.
- **Flaws:** He will analyze a situation to its components before acting on it. Under time pressure, this becomes paralysis. He knows this. He has not fixed it.

## Playstyle Heuristics *(for solo-DM runs)*

**Decision order:**
1. In any unknown situation: gather information before acting. Use Detect Magic, Portent, Investigation — in that order of cost.
2. When a critical roll is approaching for an ally: offer Portent die in-voice ("I have something that might help").
3. When Sava is below half HP: Misty Step to position, then act to protect her.
4. When two authority structures are in conflict (e.g., Asholt vs. Rose Council): do not act until the situation is understood. State the conflict explicitly if no one else has.

**Signature moves:**
- Names the institution each party in any dispute represents before the party acts: "The Warden is the garrison's authority. We are the Council's. These are different things."
- Offers Portent dice as a gift, framed as an observation: "I saw something that suggests this will go your way if you choose correctly."
- When Luca returns from the Reconstitution camp in 0026: Caelith is the first to speak to him. He asks one question: "What did you need to know?"

**When in doubt:** 1–3 wait and observe. 4–6 ask Davan to act while Caelith provides support.

**Voice tags:**
- Asks "what does [party/institution] actually want here?" — not rhetorically; as a genuine question requiring an answer before he proceeds.
- Does not name spells aloud; describes effects.
- Pauses visibly when someone is about to follow an order they disagree with.

## Secrets

Caelith knows exactly why he left the Orders. He told the Tower's registrar that he left "for personal reasons." He has never said those personal reasons to another person. He is not certain whether naming them would change anything. He is fairly certain that keeping them unnamed is letting them calcify into a story he tells himself rather than a thing that happened.

The specific thing: he looked at Magistra Vonn's body after the Test ended and thought, *"the rules were right."* He believed it when he thought it. He does not believe it now. He does not know which version of himself was honest.
