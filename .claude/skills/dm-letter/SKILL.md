---
name: dm-letter
description: Write a one-page hold-space guide for a DM running a rite, confession, or emotionally dense climactic scene. Separate from the module — addressed directly to the DM. Use when dungeon-smith produces a scene where a PC must speak aloud, name something, or perform a ritual that requires the DM to witness rather than direct.
---

# dm-letter

Write a DM-letter for a rite or confession-type scene. This is not part of the module — it is a separate artifact addressed directly to the DM, written in second person, explaining how to hold the space rather than fill it.

## When to use

A scene needs a DM-letter when **all three** are true:
1. A PC must speak aloud, name something, confess something, or perform a ritual.
2. The quality of the session depends on the DM *not* interrupting.
3. The DM (human or LLM) might reasonably fill silence with narration when they should be waiting.

Signs you need a DM-letter: the GM Notes say "let the party have this scene" but don't explain *how*; the scene involves a player producing their own confession text; the scene is a rite rather than a puzzle.

## Preconditions

- The scene exists in `rooms/NN-<slug>.md` or `module.md`.
- You have read the scene's full GM Notes and the PC sheet(s) most affected.
- The scene has a defined end-state (the DM needs to know when the scene is over).

## Procedure

### 1. Read first

- The room/scene file in full.
- The affected PC's sheet — grief-paragraph, decision-order, voice-tags.
- Any scaffold versions in the GM Notes (short/medium/long confession text, if written).
- The three-route outcomes (A/C/D) and what this scene's outcome produces.

### 2. Write the letter

The letter goes to `adventures/<slug>/dm-letter-<scene-slug>.md`.

Structure:

```markdown
---
adventure: <slug>
scene: <scene-slug>
author: dm-letter
created: <today>
---

# DM Letter — <Scene Name>

*This letter is for you, the DM. It does not go in the module. It is not read aloud. It is what you read before the session so you know how to be present for what's about to happen.*

---

## What this scene is

One paragraph. Not mechanics. Not read-aloud. What is actually happening between people. Why it matters. What the PC is doing — not mechanically but emotionally.

Example: "Grom is about to name a shame that is not his to carry. He is doing it anyway because no one else can. The silver will respond to the naming. Your job is not to explain this to anyone. Your job is to be the room."

## What to do before it starts

Specific preparation the DM should do:
- Read the scaffold versions (short/medium/long) before the session. You may never use them — but you need to know what they contain so you can recognize when the player is finding the words on their own.
- Note the three things the confession/rite must name (if applicable). Hold them in mind; don't prompt unless the player reaches for them and comes up empty.
- Decide how you will signal that the scene has begun. (Marathon-runner: the scene_narration beat handles this. Human DM: read the last line of read-aloud and then stop.)

## What to do during

The DM's actions during this scene, ordered by what might happen:

**If the player speaks:** Listen. Do not narrate over them. Do not add atmospheric beats. Let the words land before the silver flows / the fresco changes / the outcome occurs. The outcome's timing is yours; don't rush it.

**If the player hesitates:** Wait. Count to ten silently. If they ask "what should I say?", offer the short scaffold version (≤20 words) as a starting point — explicitly frame it as a starting point, not the answer. "Here's one way it could begin: [short version]. Take it or leave it."

**If the player freezes entirely:** Offer the short scaffold as a gift, not a prompt. "This is one way. You don't have to use it." Then wait.

**If the player goes long:** Let them. If they are still speaking, the scene is still happening. Do not interrupt to narrate the outcome. Wait for them to reach a natural stopping point.

**What you must NOT do:** Narrate the PC's internal state. The PC's words are the scene. The DM's job is to receive them, not interpret them.

## What ends the scene

The scene ends when:
- The PC has named the required things (or the closest they will get).
- The mechanical trigger fires (roll passed / passive DC / auto-deliver).
- The outcome is narrated (fresco changes / silver flows / the thing that was broken heals).

Then and only then: resume normal session narration.

## What happens if it goes wrong

If the roll fails (graceful failure state applies):
- <Describe what changes. What is different. What the session still has.>

If the player opts out entirely:
- <Describe Route A fallback. What happens instead. The campaign still continues.>

---

*The scene is not yours. You are the room it happens in.*
```

### 3. Link from GM Notes

Add one line to the scene's GM Notes in `rooms/NN-<slug>.md` and in `module.md`:

```markdown
**DM-letter:** See `adventures/<slug>/dm-letter-<scene-slug>.md` before running this scene.
```

### 4. Never overwrite silently

If `dm-letter-<scene-slug>.md` exists, write `dm-letter-<scene-slug>.v2.md` and report.

## Quality gates

- [ ] Letter is addressed to the DM, not the players.
- [ ] Letter explains what the scene IS (not what happens mechanically).
- [ ] "If the player hesitates" path is written with specific DM actions.
- [ ] "What ends the scene" is specific and unambiguous.
- [ ] Failure state (graceful) is described.
- [ ] Route A fallback is described.
- [ ] Scaffold versions (short/medium/long) are referenced if they exist in GM Notes.
- [ ] Letter is ≤ 1 page equivalent (500 words). If longer, cut.

## What a DM-letter is NOT

- Not a summary of the scene mechanics (those are in GM Notes).
- Not permission to skip the scene.
- Not a script for what to say.
- Not a guarantee the player will engage.

The DM-letter exists because some scenes require the DM to *do less* than usual — and doing less deliberately is harder than doing more. The letter explains how.

## Anti-patterns

- Letters that tell the DM what the PC is feeling (the PC's words are the only authority on that).
- Letters that script the outcome before the player speaks.
- Letters that are so long they cannot be read before the session.
- Letters that don't include the "if hesitates / freezes / goes long" trio.
- Skipping the letter because "the GM Notes already say let the party have this scene" — they don't explain how.
