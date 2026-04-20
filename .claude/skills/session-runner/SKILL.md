---
name: session-runner
description: Claude-as-DM skill. Runs a D&D session of a compiled adventure with a file-based party. Orchestrates PREP → PLAY → LOG stages of the 7-stage session pipeline. Rolls dice via dice-roller (no faking). Plays all PCs per their Playstyle Heuristics. Supports Option A (solo DM playing all PCs) and Option C (per-PC Agent-spawn at meaningful decision points). Produces sessions/S{N}-log.md as the canonical session artifact. Use once an adventure has a module.md and a party has been built.
---

# session-runner

Run a D&D 5e playtest session. Claude plays the DM *and* all PCs (per each PC's Playstyle Heuristics). Dice go through `dice-roller`. Every scene lands in `sessions/S{N}-log.md`.

## Pipeline position

This skill covers **PREP → PLAY → LOG** (stages 1-3) of the 7-stage playtest pipeline. Downstream stages (`session-gate`, `playtest-panel`, `playtest-innovation`, `session-handoff`) consume this skill's output.

## Preconditions

- Adventure has a compiled `module.md`.
- Party directory exists at `personas/parties/<party-slug>/` with README + PC files.
- `scripts/dice.sh` is executable.
- Session number N determined by counting existing `sessions/S*-log.md` files + 1.

## Stage 1 — PREP

### 1.1 Read everything
- Adventure: `premise.md`, `module.md`, all `npcs/*.md`, `treasures/silver-rose-manifest.md` (for curse symptoms).
- Party: `personas/parties/<slug>/README.md` and every PC file.
- Any prior sessions: `sessions/HANDOFF-S*.md` for context.
- Encounter pressure tables if the module includes them.

### 1.2 Seed the RNG
```bash
export DICE_SEED=S{N}-<YYYY-MM-DD>
```

Log this seed at the top of the prep file.

### 1.3 Write `sessions/S{N}-prep.md`

```markdown
---
session: S{N}
adventure: <slug>
party: <party-slug>
date: <today>
dice-seed: <seed>
author: session-runner
---
# S{N} PREP — <Adventure Title>

## Party at start
<Table: PC, HP, spell slots, attunement slots, inventory highlights. Refer back to PC files for fine details.>

## Open questions for this session
<2-4 explicit things we want to learn. E.g., "Does the Room 04 shaft shortcut get discovered by a balanced-classic party, or only by curiosity-driven parties?">

## Curse-symptoms seeded
<List the manifest symptoms in the adventure and which rooms they live in, so the DM remembers to land them.>

## Party-specific threads
<For each PC's grief paragraph, write one line about how their specific loss may interact with this adventure's curse or NPCs.>

## Rubric version locked
<Read personas/playtest-rubric.md top. Record version here so the gate stage uses the same rubric the session was played against.>
```

## Stage 2 — PLAY

The running rules. The DM (Claude) narrates the adventure, prompts each PC in turn, resolves with dice.

### 2.1 Scene discipline

Play **scene by scene**, not free-flow. A scene is one location or one encounter. Each scene opens with the module's read-aloud (verbatim) and closes when the party leaves the location or resolves the encounter.

For each scene, write to the session log:

```markdown
---
## Scene {N.M} — <Room Name or Scene Title>

### Setup
<Read-aloud, verbatim from module.md.>

### Beats
<Narrative + actions + dice rolls, interleaved. See 2.2 below.>

### Resolution
<What ended the scene. HP/spell/resource deltas for each PC. Any curse-symptom landed here.>
```

### 2.2 How to play the PCs (Option A — solo-DM)

For **every PC action under Option A**, the DM:

1. **Consults the PC's Playstyle Heuristics.** Decision order is binding: the top-priority drive wins unless narratively absurd.
2. **Narrates in third person.** "Aelric grips his warhammer and steps forward," not "I step forward." PCs are characters being run, not Claude speaking.
3. **Rolls dice for everything mechanical.** No fake numbers. Use the log format from `dice-roller`:
   ```
   **🎲 <PC> <action>** — `<expr>` → rolls=[...] mod=<m> **total=<T> (<result>)** · [damage if hit]
   ```
4. **Uses signature moves when fitting.** Each PC's sheet lists 1-2 signature moves — use at least one per session per PC.
5. **Speaks the PC's voice-tags** when they have a line of dialogue. Verbal tics matter.
6. **Rolls d6 "in doubt"** when the Heuristics don't cleanly decide. Log the roll.
7. **Tracks resources honestly.** HP, spell slots, hit dice, attunement slots, hunger/rest if relevant. Update the party-state table at scene boundaries.

### 2.3 Option C — Per-PC Agent-spawn at meaningful decision points *(rev 2, post-S02)*

S01 and S02 surfaced an Option-A limitation: when a PC faces a session-defining decision (attune the Varran-reliquary? speak Caen's name? show the Pella-drawing? destroy the reliquary via Reorx-rite?), the DM plays both sides of the dialogue solo. The decision's drama is real but the *voice-distinction* is thin.

**Option C augmentation:** at designated meaningful decision points, the DM **spawns the affected PC as a subagent** via the `Agent` tool, hands off a single decision, and re-absorbs the response.

#### When to use Option C

**Updated guidance (post-S05, I-S04-03 + I-S05-02):** Option C is **available**, not mandatory, for parties with ratified player-styles (`sheet-deep-reader` + `craft-witness`). Two consecutive sessions (S04: Grom's Reorx-exile; S05: Aelric's Circlet decision) showed that ratified player-styles deliver voice-distinction natively for their spotlight moments, making Option C unnecessary. **Downgrade "strongly recommended" to "available"** when the PC whose decision is at stake has a ratified player-style and a clear decision-order that can resolve the beat without grief-paragraph adjudication.

Spawn an agent when **all three** conditions are met:

1. The decision shapes the session's final state (not just the current scene).
2. The decision is specific to one PC's backstory, grief-paragraph, or playstyle heuristics.
3. The decision would be played inauthentically by the solo DM — specifically when the solo DM would produce a generic answer where the PC's specific voice would produce a distinct one.

**When NOT to spawn (post-S05 guidance):** If the PC's decision-order resolves the beat cleanly (e.g., Aelric: Oath → Order → Party → Self; "The Oath was sufficient"), do not spawn. The absence of a spawn is not a failure — it is evidence the player-styles are working.

**Examples of Option-C-appropriate moments:**
- Aelric's decision to attune the Varran-reliquary.
- Grom's decision to perform the Reorx-shattering rite (or not).
- Kessa's decision to attune Keloth's mother's bracelet (if it ever arises).
- Thera's decision to accept Pella's *"I go with you"* or route her to Varduin.
- A PC's decision to speak a dead loved one's name aloud for the first time.

**Examples of NOT Option-C-appropriate:**
- Combat actions (solo DM is fine).
- Movement, positioning, minor skill checks.
- Any roll where the PC's heuristic cleanly decides.

#### How to spawn

```
Agent({
  description: "Aelric attunement decision",
  subagent_type: "general-purpose",
  prompt: "You are Aelric of Crownhold, Knight of the Crown (initiate) of the Varduin Muster. Your full PC sheet is at personas/parties/varduin-muster/aelric-of-crownhold.md. READ THAT SHEET FIRST.

  Context: You are at the Reliquary Vault in Gavek's Rest. Keloth — a Bone-Priest — has just offered you a trade. If you attune to the Varran-reliquary on the altar, you will hear your brother Varran's last minute in his own voice. You will permanently lose every other memory of him — childhood, training, the blue-leather saddle-lashing morning, all of it. In exchange, Pella (a nine-year-old girl bound to the altar) walks free, and Keloth's cell is not pursued.

  Your party-mate Grom has just counter-argued against attunement in his own voice: 'If you take this, Varran is gone. Not just the body. The living-figure of him. You will only be able to remember him dying. The rose did not take your brother from you and this does not need to either. Brother. Don't.'

  Pella is looking at you. She has asked: 'Are you the knight my papa said would come?' She has decided the answer is yes.

  Your task: decide, in Aelric's voice, whether to accept the trade. Respond in a single paragraph of first-person narration (Aelric's actual line plus whatever he says or does). Do not break character. Do not meta-comment. Consult the PC sheet's Decision Order and speak as your character would."
})
```

The subagent returns Aelric's single-paragraph response. The DM writes it into the session log as Aelric's action, then continues solo.

#### Discipline

- **Max one agent per meaningful-decision scene.** Do not spawn a chain.
- **The agent's response is binding** — the DM does not override. If the agent decides for Aelric to attune, Aelric attunes.
- **Include the full PC sheet path** in every spawn prompt. Never shortcut with "you are Aelric."
- **Include the counter-argument from other PCs if any** — the agent needs to hear what Grom said to decide honestly.
- **Log the spawn** in the session log: note that Option C fired; cite the agent's response verbatim.

#### Why not always Option C?

- **Cost.** Spawning agents is expensive; one per scene is reasonable, one per PC per scene is not.
- **Pacing.** Option A scenes flow faster. Option C scenes need a real pause.
- **Session-reviewability.** Option A logs are single-author; Option C logs carry subagent voices. Both are readable, but they read differently.

#### When the Minute plays (specifically)

The Varran-reliquary's 60-second Minute is an **Option C strongly-recommended** moment. Spawn an Aelric-agent with the Minute's prewritten content (cold, Hern's fall, Doriel's name) as context, ask the agent to *describe* the Minute in Aelric's voice (what he sees, feels, understands, mourns). This is the single moment the workshop has most wanted voice-distinction for — S02 played it solo and the Roleplayer lens noted the cost.

**Post-S02 commitment:** S03 and future sessions use Option C for Minute-style attunement beats. Option A holds for everything else unless a similar-weight moment arises.

### 2.3 DM discipline

The DM:
- Does not signpost puzzle solutions. If the party misses Room 04 because they took the east archway, they miss it.
- Lands manifest symptoms when they land — VANOR drift on the lintel when noticed; repeated phrase at Rose-lift; fresco heal on a Perception check.
- Rolls wandering-pressure tables on schedule (d6 per 10 min Cold Pulse; d6 per 30 min Wandering). Log the rolls.
- When a curse save comes up, walks through it with the player-voice: the DM asks *the PC's player* (which is also Claude, but playing that character) to describe the memory being taken. Write it into the session log as a specific entity.
- Narrates the Memory Echo scene at climax with the repeated-phrase callback. Silence for her line even mid-combat.
- Does **not** rescue the party from consequences of their own decisions.

### 2.4 What the DM must log every turn

- Every dice roll, with context.
- Every decision point and which PC made the call (with reference to their Heuristics).
- Every resource change (HP, spells, etc.).
- Every curse symptom landed (so the innovation skill can audit manifest compliance).
- Every player-style surprise — a move the Heuristics didn't obviously predict but the PC sheet could justify. Tag these `<!-- SURPRISE -->` so `playtest-innovation` can find them later.

## Stage 3 — LOG (finalize)

### 3.1 Consolidate the session log

At session end, rewrite the running log as `sessions/S{N}-log.md`. Required sections:

```markdown
---
session: S{N}
adventure: <slug>
party: <party-slug>
date: <today>
dice-seed: <seed>
duration: <in-fiction hours>
outcome: <one-line: "Rose retrieved via Option B; party kept it.">
route: [A|C|D]   # A = charter/fallback, C = destruction/default, D = inversion/optimal
author: session-runner
---

# S{N} LOG — <Adventure Title>

## Session Summary
3-5 sentences. What happened. What choice the party made. Where they ended up.

## Party state (delta)
Table: PC | HP start → end | Spells used | Hit dice used | Attunements | Notable inventory changes.

## Scenes
(The scene-by-scene playthrough, cleaned up. Keep dice rolls intact.)

## Curse symptoms landed
Bulleted list of manifest symptoms the party encountered this session, with scene reference. Cross-check against `treasures/*-manifest.md`.

## Player-style surprises
Bulleted list of `<!-- SURPRISE -->` tags from the running log, with one-line notes. These are inputs to `playtest-innovation`.

## Open threads for next session
- What did the party commit to?
- What consequences are in motion? (e.g., Brother Laen's response; Bone-Collectors closing in.)

## Questions this session raised about the module itself
- Did any gate violation surface in play? (E.g., a player asked about the VANOR lintel twice and the module didn't have a second prompt.)
- Did the wandering-pressure pacing feel right?

## Rubric version locked
<same as PREP — the gate stage scores against this version.>
```

### 3.2 Update the party shared log

Append a one-paragraph summary to `personas/parties/<slug>/shared-log.md` so the party carries memory into future sessions.

### 3.3 Never overwrite silently

If `sessions/S{N}-log.md` exists, bump to `S{N}.v2-log.md` and report.

## Output to user

- Session outcome (one line).
- Number of dice rolls, surprises, curse symptoms landed.
- Which of the PREP open questions got answered.
- Suggested next stage: `session-gate`.

## Quality gates

- [ ] Every PC acted at least twice per scene they were present in.
- [ ] Every PC used at least one signature move during the session.
- [ ] No fake dice rolls (every mechanical resolution has a `🎲` line).
- [ ] All dice go through Python DiceEngine (marathon-runner CLI). Do not call `scripts/dice.sh` directly for session dice — it bypasses the JSONL audit log. If running without marathon-runner, use `scripts/dice.sh` for every roll but note the logging gap.
- [ ] ≥ 3 manifest symptoms landed (if the adventure has a manifest).
- [ ] Wandering-pressure tables rolled on schedule.
- [ ] Session log ≥ 2,000 words (a real playthrough should produce substance).
- [ ] `<!-- SURPRISE -->` tags captured (expect 3-8 in a first session).
- [ ] Dice seed logged in both PREP and LOG frontmatter.
- [ ] `route:` field set in LOG frontmatter (A, C, or D).

## Anti-patterns

- PCs speaking in first person ("I grip my hammer"). Third person always.
- Fake rolls or "rolled mentally."
- Rescuing the party from consequences.
- Signposting solutions.
- Collapsing scenes into summary paragraphs.
- Resource amnesia (spells cast but never marked).
- Ignoring curse triggers because they're "inconvenient."
- Skipping a PC's turn because they're "quiet."
