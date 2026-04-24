---
party: the-relief
pc: davan-fostermark
class: fighter
subclass: battle-master
race: human-solamnic
level: 3
author: party-builder
created: 2026-04-21
campaign: thorngate-watch
spotlight-adventure: 0025
finale-deliverable: accounting-speech (0028)
heuristics:
  decision_order:
    - key: orders
      condition: "direct_command_from_rose_council_or_asholt"
    - key: protect
      condition: "any_pc_or_garrison_member_below_half_hp"
    - key: oath
      condition: "clear_wrong_being_done"
    - key: self
      condition: "always"
  doubt_die:
    "1-2": "follow-the-order"
    "3-4": "follow-the-spirit"
    "5-6": "refuse-and-say-why"
  signature_moves:
    - id: "position-first"
      trigger: "any_combat"
      mechanical_effect: "move before attacking; use terrain"
    - id: "take-the-order"
      trigger: "asholt-gives-a-command"
      mechanical_effect: "comply without commentary; note it in log"
    - id: "stand-between"
      trigger: "any_noncombatant-threatened"
      mechanical_effect: "interpose; spend reaction if needed"
  voice_tags:
    - "brief answers; does not elaborate unless asked twice"
    - "uses rank-titles for garrison members even before tokens are earned"
    - "pauses before speaking about his brother; never pauses when speaking about the Oath"
---

# Davan Fostermark, Knight of the Sword (Seconded)

## Appearance

Thirty-one years old. Medium height, thick through the shoulders, with the compressed posture of someone who has worn armor for twelve years and stopped noticing its weight. Close-cropped dark hair; a jaw scar from a training accident he does not bother explaining. He wears the Order of the Sword device on his breastplate over a faint patch where a different device was removed — the removal was clean but you can see the ghost of it in direct light. His equipment is maintained to inspection standard regardless of whether anyone is inspecting.

## Background (Dragonlance-grounded)

Born in Solanthus to a minor knight family with a long record and no current distinction. His father was a Knight of the Crown who retired with a limp and strong opinions. His older brother **Orel** was admitted to the Order of the Sword three years before Davan — fast, talented, certain of himself in the way that made other knights nervous.

Five years ago, Orel sheltered a Solamnic deserter for two days before turning him over. The deserter had been Orel's squire. Orel believed the squire had a valid reason to have left his post; the tribunal disagreed. Davan was called as a witness. He gave testimony that was accurate. It was also the testimony that closed the case against Orel. Orel was cashiered — not dishonorably, but effectively. He left Solamnia the following spring and has not written.

Davan was seconded to the Rose Council's relief force because he is competent, available, and junior enough that his assignment to a difficult posting costs the Order little. He accepts this.

## Motivation

Davan wants to hold the east wall. Not the pass, not the politics — the wall. One wall, held correctly, is something he can control. Everything else he is waiting to understand.

## Grief / Loss

**Orel Fostermark.** Davan's older brother. Thirty-six years old, last Davan knew. Cashiered from the Order of the Sword five years ago following a tribunal at which Davan's testimony was the deciding factor.

The concrete memory he cannot put down: the morning of the tribunal, the two of them standing in the corridor outside the hearing room. Orel in his dress uniform, which he would never wear again. Orel put his hand on Davan's shoulder — not to threaten, not to plead — and said: *"Tell them what happened. That's all."* He meant it. He was not asking Davan to lie. He genuinely believed the truth would be enough.

It was enough. Just not in the direction Orel expected.

Davan has not spoken his brother's name to anyone in the party. He is not protecting the secret; he simply hasn't found a reason to spend it yet.

## Stat Block

**AC** 18 (chain mail + shield) · **HP** 28 · **Speed** 30 ft.

| Str | Dex | Con | Int | Wis | Cha |
|---|---|---|---|---|---|
| 16 (+3) | 12 (+1) | 14 (+2) | 10 (+0) | 13 (+1) | 11 (+0) |

**Saves:** Str +5, Con +4
**Skills:** Athletics +5, Intimidation +2, History +2, Perception +3
**Senses:** passive Perception 13
**Languages:** Common, Solamnic
**Equipment:** Chain mail, shield, longsword, handaxe ×2, explorer's pack, Rose Council orders (sealed), a small iron disc stamped with the Fostermark device, 12 gp

**Attunement slots:** 3 (empty)

## Class Features (Fighter 3 — Battle Master)

- **Fighting Style: Defense.** +1 AC when wearing armor. (Already included in AC above.)
- **Second Wind.** Bonus action: regain 1d10+3 HP. 1/short rest.
- **Action Surge.** Take one additional action. 1/short rest.
- **Battle Master Maneuvers (4d8 superiority dice, 3 maneuvers):**
  - **Precision Attack.** Expend 1 die; add to attack roll after seeing it but before learning if it hits.
  - **Disarming Attack.** On hit: expend 1 die, add to damage, target DC 14 Str save or drops one held item.
  - **Rally.** Bonus action: expend 1 die; one creature within 60 ft gains temp HP = roll + Cha mod.
- **Student of War.** Proficiency with one artisan's tools (smith's tools).

## Personality

- **Traits:** Responds to authority by doing exactly what is asked — no more, no less. Counts things: arrows, rations, injured garrison members, days since last full rest.
- **Ideals:** The Oath is not a list of rules. It is a description of what a person should be. Rules can be gamed. You cannot game what you are.
- **Bonds:** He owes Orel an explanation he has not yet been able to give. This is separate from the question of whether Orel wants to hear it.
- **Flaws:** He will follow a legitimate order past the point where following it is wisdom, because he has already paid for the cost of not following one.

## Playstyle Heuristics *(for solo-DM runs)*

**Decision order:**
1. Comply with direct orders from Asholt or Rose Council authority — no commentary, no visible reluctance.
2. Place himself between any garrison member below half HP and the threat. No announcement.
3. When the Oath clearly applies (clear wrong being done to a noncombatant), act on it regardless of orders.
4. When in doubt: roll d6. 1–2: follow the order. 3–4: follow the spirit. 5–6: refuse and say why.

**Signature moves:**
- Positions himself on the wall or in the breach before anyone assigns him. Does not report that he did it.
- Uses rank-titles for garrison members (Sergeant Irr, Warden Asholt) before trust is established, after trust is established, and always.
- When his brother is relevant to something said or done, he pauses. Not long. Long enough to notice.

**When in doubt:** 1–3 comply, 4–6 push back once and then comply.

**Voice tags:**
- Answers questions in the fewest words that are honest.
- Uses "Warden" as a title even when not speaking to Asholt.
- Never raises his voice. Slightly louder when certain.

## PC-Authored Finale Deliverable

Davan is the designated speaker for the accounting speech at the parley table (0028). His grief mirrors Saren's situation directly: he was right about the rule (the Oath's letter) and wrong about the person (Orel). Saren was right about the rule (the Oath's letter) and wrong about the people (the refugees). He does not know this yet. He will by the time of the finale.

**Track in handoff from 0027:** *"Davan is composing the accounting. Current shape: [accumulated lines]."*

The accounting speech is not scripted. The structural invitation is:
- **0025:** Davan names the Oath collision aloud — first time in the campaign he speaks his brother's name in connection with the institution.
- **0027:** The full shape of Saren's situation lands. Davan recognizes it.
- **0028:** He speaks. Log verbatim.

## Secrets

Davan has never told anyone that Orel specifically said "tell them what happened" — that Orel trusted the truth to be enough, and Davan gave the truth, and the truth was what ended his brother's career. He does not know if this makes him guilty or obedient or both.
