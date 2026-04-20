---
name: npc-architect
description: Design an NPC with arc-completion potential — a character sheet that specifies their emotional position, the specific thing they are capable of saying or doing that closes their arc, and the conditions under which they do it. Use when dungeon-smith needs a significant NPC, or when an existing NPC file lacks arc-completion design. Produces npcs/<slug>.md.
---

# npc-architect

Design a significant NPC for a D&D 5e adventure. The goal is not to produce a stat block — it is to produce a character who can deliver their arc-completion moment by character logic, without DM scripting, when the conditions are right.

## When to use

Use for any NPC who:
- Has an emotional arc that intersects the adventure's central emotion (grief, shame, longing, etc.)
- Will speak a line or take an action that changes the scene's direction.
- Matters to the PC whose spotlight this adventure is.

Do not use for generic combatants, background characters, or NPCs who only exist to deliver information. Those go in dungeon-smith's NPC skeleton step. This skill is for the NPCs whose lines you want to remember.

## Preconditions

- `adventures/<slug>/premise.md` exists with the adventure's central emotion and the spotlight PC identified.
- You know what role this NPC plays in the party's arc (witness, obstacle, mirror, catalyst).

## Procedure

### 1. Read the adventure's emotional context

- The central emotion of this adventure.
- The spotlight PC's grief-paragraph and decision-order.
- Any prior-adventure notes about this NPC (if they've appeared before).
- The three-route outcomes (A/C/D) — which route does this NPC's arc-completion enable?

### 2. Design the emotional position

Before writing the NPC's stat block or appearance, answer these three questions in one sentence each:

1. **What does this NPC want?** (The drive that governs all their behavior. Not a goal — a want.)
2. **What can't they say?** (The specific thing they have not yet named. The unsaid word that the scene might unlock.)
3. **What is the condition under which they say it?** (Not "if the party is kind." Specific: "if a PC names their own longing first," "if someone asks about the door rather than the room," "if no one pushes.")

These three answers are the NPC's core. Everything else — stat block, history, behavior matrix — exists to serve them.

### 3. Write `npcs/<slug>.md`

Required sections:

```markdown
---
adventure: <slug>
npc: <slug>
author: npc-architect
created: <today>
---

# <NPC Full Name>

## Appearance
2-3 sentences. What the party sees when they first look. One specific detail that makes them real (a scarred hand, a habit of looking at the door, the way they hold their cup).

## Stat block
AC <N> | HP <N> | Speed 30 ft.
Type: [combatant / non-combatant]
<If combatant: relevant attacks, saves, resistances — inline, not a link.>
<If non-combatant: "This NPC will not fight unless [specific condition].">

## What they know (public)
Bulleted. What they will say if asked. What any Insight 10 reveals.

## What they know (private)
Bulleted. What they will not say. What a high Insight or successful social roll reveals. What they will say only under their arc-completion conditions.

## Emotional position

**What they want:** <one sentence>

**What they can't say:** <one sentence — the specific thing they have not yet named>

**The condition:** <specific — not "if the party is kind." What exact thing must happen first?>

## Behavior matrix

| Party action | NPC response |
|---|---|
| Direct question about <the unsaid thing> | <what they do — probably deflect; how> |
| Named their own grief/shame/longing first | <what this unlocks in the NPC> |
| Asks about the object rather than the story | <what this unlocks> |
| Pushes too hard | <how they close> |
| Says nothing and waits | <how they respond to space> |
| Tries to leave without engaging | <what the NPC does or doesn't do> |

## Arc-completion

**The moment:** <What the NPC says or does when the condition is met. Specific. Written as if it is happening now. Not "Mira might say something about her mother." "Mira writes her mother's name in ink for the first time in thirty years on the Council file-note and gives it to Grom. She says: 'A daughter's note. My mother's name was Seralen. I am grateful.'">

**What it produces:** <What changes in the scene. What the party now knows or has. Which route (A/C/D) this enables.>

**What happens if the condition is never met:** <The NPC does not complete their arc. What state they leave in. Is there a recovery path in a future adventure?>

## GM Notes

- What the DM should NOT say until the arc-completion condition is met.
- Any DM-letter cross-reference: see `adventures/<slug>/dm-letter-<scene-slug>.md` if this NPC is involved in a rite/confession scene.
- Whether this NPC has any cross-adventure thread (seed-tracker entry to plant/retrieve here).
```

### 4. Validate against the adventure

Before declaring done:
- Does the arc-completion moment support the adventure's Route D (or at minimum Route C)?
- Is the condition specific enough that the DM will know when it has been met?
- Is the "what happens if never met" path also a valid session outcome?
- Is the behavior matrix honest — does it include failure modes (pushes too hard, asks too directly)?

### 5. Never overwrite silently

If `npcs/<slug>.md` exists, write `npcs/<slug>.v2.md` and report.

## Quality gates

- [ ] Emotional position section is complete (want / can't say / condition).
- [ ] Arc-completion moment is written in present tense, specific, quotable.
- [ ] Behavior matrix includes at least one failure mode (NPC closes, deflects, or goes cold).
- [ ] "What happens if condition never met" is written.
- [ ] At least one GM Note about what NOT to say prematurely.
- [ ] If this NPC involves a rite/confession scene: DM-letter cross-reference included.

## What separates a good NPC-architect NPC from a generic one

A generic NPC has: appearance, stat block, what they know, how they fight.

An npc-architect NPC has all of that plus: **a specific sentence they haven't said yet, and the exact conditions under which they say it.** When they say it, the DM did not make them say it. The conditions did. That is the difference.

## Anti-patterns

- Arc-completion that requires the party to do something clever (arc-completion is not a puzzle).
- A condition that is "if the party is nice to them" (too vague; write the specific act).
- An arc-completion moment that is abstract ("she finally lets herself grieve") instead of physical/verbal ("she writes the name").
- Behavior matrices that only describe success modes (no failure modes).
- Forgetting to write what happens if the condition is never met.
