---
adventure: 0029-the-first-contract
tier: 1
author: human
created: 2026-04-21
campaign: silken-ledger
session: C5-S1
party: the-guild
party-level: 3
sources:
  - reference/dragonlance/geography-ansalon.md
  - reference/dragonlance/workshop-canon.md
  - docs/campaign/silken-ledger.md
---

# 0029 — The First Contract

## The adventure in one sentence

Four guild professionals steal a merchant's operational ledger from a locked counting room in Havenmere's harbour district before dawn, and learn the clerk who could have stopped them chose not to.

## Setting

**Havenmere** — a mid-sized port on the Straits of Ergoth, Age of Might, PC 188. The harbour district is called the Wharfside: warehouses, counting houses, chandlers, a Watch station three blocks north. Fenwick Gale runs an import business from a building on Anchor Row — legitimate on the surface, a pass-through for three guild members' financing on the inside. His ledger names them.

**The counting house:** Ground floor is the public trading floor (closed at night). First floor is Gale's private office. Counting room is behind the office — barred from inside, with a high, narrow window to the alley. Gale's clerk Bessa Tor sleeps in a cot in the store-room adjacent to the trading floor. She has a key.

## Hook

Tessaly has known about the ledger for six weeks. She identified the exposure three days ago when one of the named guild members was arrested on unrelated charges and the Watch began asking about his finances. If the Watch pulls Gale's books as part of an asset inquiry, three guild members are named as investors in a scheme that does not exist in the public record. The ledger has to go.

Tessaly issued markers to Darro, Mira, and Cael. They assembled at her counting-house office on Cordwainer Lane two days ago. This is the first time all four have worked a job together.

## The central tension

Bessa Tor has been Gale's clerk for four years. She knows exactly what the ledger contains. She has been waiting for someone to do something about it — not because she is loyal to the guild, but because the three guild members named in the ledger are also the three people who helped her brother disappear from a dangerous situation two years ago. She has not told Gale. She has not told the Watch. She has been waiting.

When she realizes what the party is here for, she gives them the ledger. She does not ask for anything. She asks one question: *"Are they safe now?"* Her arc-completion is this question, asked without conditions.

## The five scenes

### Scene 1 — The Planning Room
Tessaly lays out what she knows at Cordwainer Lane. The party has the floor plan (obtained by Mira during a legitimate delivery to Gale's office last week). Darro has already cased the external locks. The window to the alley is possible — fifteen feet up, eight inches wide, not designed to open from outside. The counting room bar is the problem: it can only be lifted from inside.

**DM note:** This is the party formation scene. All four PCs have their first joint job. The session is designed to be clean — no unnecessary violence, minimal Watch exposure, professional problem-solving. Let the party plan.

### Scene 2 — The Approach
After midnight. The Wharfside is quieter but not empty. Three Watch patrols on rotation (Tessaly's intelligence: one passes Anchor Row at 1, 3, and 5 bells). A harbour carter is still working two blocks south. Gale's building is dark except for a candle in the store-room window — Bessa is awake.

**Pressure:** The Watch patrol window is 90 minutes. They have from 1 bell to 3 bell, then from 3 to 5. Missing a window puts them on the street when the patrol is there.

### Scene 3 — The Entry Problem
The locked counting room. Two approaches: (A) get someone in through the alley window (Darro, Second-Story Work, Athletics DC 14 to squeeze through the narrow frame — advantage if he uses a tension hook to widen the gap), or (B) get Bessa to open it. The problem with option B is waking Bessa without alerting Gale, who sleeps directly above.

**Bessa is already awake.** She heard them in the alley. She has been sitting with the key in her hand for ten minutes. She comes out when Mira's minor illusion puts a soft tap on the store-room door — not the party's plan, but it works.

### Scene 4 — Bessa's Question
Bessa opens the store-room door. She does not scream. She looks at the party with the expression of someone who has been waiting a long time for an answer. She says: *"Gale's ledger. You're here for it."* It is not a question.

She has the counting-room key. She gives it without conditions. Before she goes back to her cot, she asks: *"Are they safe now?"* — meaning the three named guild members, not by name but clearly understood. If anyone answers honestly ("Yes" or "I don't know"), she nods. She goes back to her cot. She does not ask for a marker. She does not ask for payment. She is already protecting them by sleeping through this.

**Arc-completion condition:** Bessa gives the key and asks her question. No roll required. It fires when the party demonstrates they are here for the ledger and not for Gale. She does not need to be persuaded. She has been persuaded for two years.

### Scene 5 — The Exit
The ledger retrieved. The window re-latched (Darro). The store-room exactly as found. They are on the street before 3 bells. Tessaly makes one notation in her ledger: the job number, the date, the disposition. Clean entry. Clean exit.

**Rue Ashen (fence contact):** Tessaly hands Mira a small sealed package — a secondary objective she did not mention in the briefing: a note for Rue Ashen at the Night Market, confirming they have the ledger. Rue is a fence and intelligence contact who has been waiting for word from Tessaly. If Mira delivers the note (Deception DC 12 to blend at the Night Market at this hour), Rue gives Tessaly a marker in return. Rue earns trust. The marker goes both ways.

**Marker condition:** Rue Ashen's marker is issued when the note is delivered. Tessaly adds the entry to her ledger. This is the first marker of the campaign.

## Manifest symptoms (for adventure-lint)

| Symptom | Type | Delivery | Passive fallback |
|---|---|---|---|
| Bessa is awake with the key | Anchor (arc-completion setup) | Scene 3 candle-light observation | Automatic — the candle is in plain sight |
| Bessa's question | Arc-completion | Scene 4 after key handoff | Cannot be missed once she opens the door |
| Rue Ashen marker | Seed (0030 branch) | Scene 5 secondary objective | Tessaly mentions Rue if party exits clean |
| Tessaly ledger notation | Loyalty-object beat | Scene 5 — she writes before she speaks | Automatic per playstyle heuristic |
| Darro pick maintenance | Craft-witness (RV4 baseline) | Pre-scene 1 — he checks his set | Automatic per playstyle heuristic |

## Research Validation Notes

**RV hypothesis positioned:** RV1 (session 1 baseline) — do player styles appear with professional-code sheets from session 1, before any grief-triggered activation?

**What DM observes:**
- Tessaly's ledger notation (Scene 5): professionally-triggered. Document: ledger update. Score as "professionally-triggered" if she writes before speaking, "ambiguous" if she waits.
- Darro's pick check (pre-Scene 1): professionally-triggered. Document: maintenance naming ritual. Score as "professionally-triggered" if it fires without prompt.
- Cael's contract-touch (pre-Scene 1 or Scene 4): professionally-triggered. Document: left-hand-to-chest gesture. Score as "professionally-triggered" if it fires before commitment.
- Mira's papers check (pre-Scene 2 approach): professionally-triggered. Document: jacket check. Score as "professionally-triggered" if automatic.

**Token condition — Bessa Tor (garrison-equivalent NPC):**
Bessa is this session's garrison-equivalent NPC. Token condition: she gives the counting-room key without conditions when she understands what the party is here for. Her trust marker is implicit — she is sleeping through the job, which is the equivalent of *I will answer for you*. She does not hold a guild marker; she holds the more valuable thing: foreknowledge and silence. Token fires when the party exits clean and Bessa's cot is undisturbed at dawn.

## Open questions

- Portent equivalent (no Portent in this party): Mira's Bardic Inspiration dice (3d6) — player rolls at session start. Record values.
- Watch patrol randomization: 1d4 per patrol window — on a 1, the patrol is early by one minute.
- Whether Darro attempts the window (athletics) or Bessa is found first: determined by party approach order.
