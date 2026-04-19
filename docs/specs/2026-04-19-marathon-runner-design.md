---
title: marathon-runner — Python CLI Game Engine
date: 2026-04-19
status: revised-post-board-review
author: brainstorming
---

# marathon-runner — Design Spec

## Purpose

Replace the current bash-dice + LLM-only session pipeline with a Python CLI that owns the mechanical layer (dice, state, PC heuristics) while keeping the LLM in the loop for narrative decisions. The script is re-entrant: every LLM-required beat writes a checkpoint before waiting; `resume` re-enters from the last unanswered prompt.

**Core problem solved:**
- Bash dice.sh has a seed-overflow warning on every roll and requires manual state tracking
- Session state (HP, slots, attunements, Hint status) lives only in my head during play
- PC heuristics (doubt-die, decision-order, signature moves) are re-derived per beat
- Session logs require post-play consolidation of scattered notes

---

## Architecture

```
scripts/
  marathon.py          ← entry point (CLI: start, resume, status)
  engine/
    loader.py          ← parses module.md + PC sheets → Python objects
    dice.py            ← seed-locked RNG; replaces dice.sh
    state.py           ← party state + session state + campaign facts
    heuristics.py      ← mechanical PC decision-making from encoded sheets
    classifier.py      ← "Python can resolve" vs "LLM required" router
    scene.py           ← scene state machine; advances module scenes
    emitter.py         ← builds JSON decision-packets for LLM beats
    log_writer.py      ← produces S{N}-log.md in the established format
state/
  checkpoint.json      ← written before every LLM beat; deleted on resume
  session.json         ← full session state; updated per scene boundary
```

**Run modes:**
```bash
python marathon.py start --adventure 0004-the-wrath-coin --session S04
python marathon.py resume          # re-enter from last checkpoint
python marathon.py status          # print current state snapshot
```

---

## Component Specs

### 1. `loader.py` — Module + Party Parser

**Input:** adventure slug (maps to `adventures/<slug>/module.md`) + party slug (maps to `personas/parties/<party>/`)

**Outputs:**
- `Adventure` object: list of `Scene` objects (keyed by scene index); each Scene has read-aloud text, encounter data, DC table, treasure list, manifest symptoms
- `PC` list: one `PC` object per file; contains stat block, spell slots, attunements, heuristics

**Parsing strategy:**
- Adventure: parse module.md **eagerly at load time** (all scenes at once). Section headers `### Scene N` delimit scenes. DC table in cheatsheet parsed into `{dc: int, check: str, scene: int, consequence: str}[]`. Stat blocks parsed by detecting `**AC** N · **HP** N` pattern inline.
- PC sheets: parse YAML frontmatter for stat block; parse `## Playstyle Heuristics` section for decision-order list + doubt-die interpretation + signature moves. **Parsed once at session start; held in memory; not re-parsed mid-session.**

**Failure modes:** missing section → raise `LoadError` with file + line; incomplete stat block → raise with specific missing field

---

### 2. `dice.py` — Seed-Locked RNG

**Interface:**
```python
dice = DiceEngine(seed="S04-20260419")
dice.roll("1d20+5")          # → RollResult(rolls=[14], mod=5, total=19)
dice.roll("2d6+3")           # → RollResult(rolls=[4,2], mod=3, total=9)
dice.roll("1d20+3", adv=True) # → RollResult(rolls=[9,6], kept=9, mod=3, total=12)
dice.roll("1d20", bless=True) # → applies 1d4 bless die automatically
```

**`RollResult`:**
```python
@dataclass
class RollResult:
    expression: str
    rolls: list[int]
    kept: int | None      # None if no adv/disadv
    mod: int
    bless_roll: int | None
    total: int
    crit: bool            # True if kept d20 == 20
    fumble: bool          # True if kept d20 == 1
    seed_position: int    # for reproducibility audit
```

**Implementation:** `random.Random(seed_string)` where seed is derived from session name. Seed position tracked so any roll can be reproduced by index. All rolls logged to `state/dice_log.jsonl` (append-only).

**Replaces:** `scripts/dice.sh` entirely. No bash required.

---

### 3. `state.py` — State Model

Three state layers, all persisted in `state/session.json`:

#### Party state (per PC, updated per scene)
```json
{
  "aelric-of-crownhold": {
    "hp": 28, "hp_max": 28,
    "spell_slots": {"L1": 3, "L2": 0},
    "attunements": ["varran-reliquary"],
    "lay_on_hands": 15,
    "concentration": null,
    "conditions": []
  }
}
```

#### Session state
```json
{
  "adventure": "0004-the-wrath-coin",
  "session": "S04",
  "dice_seed": "S04-20260419",
  "scene_index": 3,
  "scenes_completed": [0, 1, 2],
  "pending_checkpoint": null
}
```

#### Campaign facts (sourced from CLAUDE.md + seed-tracker, read-only during session)
```json
{
  "hints": {
    "hint-1": "caught",
    "hint-2": "unlocked",
    "hint-3": "planted",
    "hint-4": "pre-planted"
  },
  "campaign_permanent": [
    "aelric-varran-memory-loss",
    "mirror-destroyed",
    "wrath-coin-destroyed"
  ]
}
```

**Write discipline (explicit ordering to prevent conflicts):**

1. **Dice roll occurs** → append to `state/dice_log.jsonl` (append-only; never re-written)
2. **Beat resolves (Python)** → update in-memory state only; do NOT write `session.json` yet
3. **Scene COMPLETE** → write party state deltas to `session.json` (atomic rename from `.tmp`)
4. **LLM beat emitted** → write checkpoint.json BEFORE blocking; do NOT update session.json yet
5. **LLM response received + validated** → update session.json atomically; then delete checkpoint.json

**Why this ordering:** dice_log.jsonl is append-only and safe to write any time. session.json is written only at scene boundaries and after validated LLM responses — never mid-scene during Python-resolved beats. This prevents a partial-write leaving session.json in an inconsistent state.

Campaign facts are read-only (written by session-handoff pipeline, not during play).

---

### 4. `heuristics.py` — Mechanical PC Decision-Making

**Encodes:** the mechanical (not narrative) parts of each PC's Playstyle Heuristics from their sheet.

**Interface:**
```python
h = Heuristics(pcs)

# Doubt-die: rolls 1d6, applies PC's doubt-die table
h.doubt_die("grom", context="artifact-decision")
# → DiceResult + interpretation ("mend" or "stand-between")

# Target selection: picks enemy per PC's decision order
h.select_target("thera", enemies, scene_context)
# → Enemy | None

# Signature move check: should PC use signature move this scene?
h.signature_move_due("grom", session_log)
# → SignatureMove | None

# Bless check: is bless active for this PC?
h.bless_active("aelric")
# → bool
```

**Source format — PC sheet YAML heuristics block:**

PC sheets encode decision order in a structured YAML section under `## Playstyle Heuristics`:

```yaml
# In personas/parties/varduin-muster/aelric-of-crownhold.md YAML frontmatter:
heuristics:
  doubt_die:
    "1-3": "follow-measure-strictly"
    "4-6": "follow-measure-spirit"
  decision_order:
    - key: oath
      condition: "involves_evil OR involves_undead"
    - key: order
      condition: "has_council_interest"
    - key: party
      condition: "any_pc_below_half_hp"
    - key: self
      condition: "always"   # fallback
  signature_moves:
    - id: "oath-spoken"
      trigger: "facing_obvious_evil OR undead"
      mechanical_effect: null       # narrative only; Python flags, LLM narrates
    - id: "lay-on-hands-reserved"
      trigger: "ally_at_or_below_half_hp"
      mechanical_effect: "lay_on_hands"
  voice_tags:
    - "formal-register"
    - "est-sularus-spoken-aloud"
    - "terse-under-stress"
```

`loader.py` parses this block into `PC.heuristics` at session start. **A new PC requires only a new YAML block in their frontmatter — no code changes.** The condition strings are evaluated by a small safe interpreter in `heuristics.py` against the `SceneContext` object.

**Condition string vocabulary** (safe interpreter recognises these tokens):
- `involves_evil`, `involves_undead`, `has_council_interest` — event flags
- `any_pc_below_half_hp` — party state query
- `always` — unconditional fallback
- `OR`, `AND`, `NOT` — boolean operators

**Failure mode:** unrecognised condition string → `LoadError("unknown condition token: X", pc_file, line_number)` at parse time.

**Decision order encoding** (Python runtime representation, derived from YAML):
```python
# Derived by loader.py from YAML; never hardcoded in heuristics.py
AELRIC_DECISIONS = [
    DecisionRule(key="oath",  condition="involves_evil OR involves_undead"),
    DecisionRule(key="order", condition="has_council_interest"),
    DecisionRule(key="party", condition="any_pc_below_half_hp"),
    DecisionRule(key="self",  condition="always"),
]
```

**What heuristics.py does NOT decide:** Option C moments, narrative dialogue, read-aloud delivery, cross-PC atmospheric chains, any decision involving a grief-paragraph. Those go to the classifier.

---

### 5. `classifier.py` — Decision Router

**Foundational rule (state first, everything else derives from it):** False-LLM-required is cheap — one extra prompt, a few seconds. False-Python-resolved corrupts voice — a mechanical system making a narrative call it isn't sure about breaks the thing the whole engine is protecting. When in doubt, route to LLM.

**`Event` dataclass:**
```python
@dataclass
class Event:
    type: str                       # "dice_roll" | "hp_delta" | "dialogue" | "option_c" | etc.
    pc_slug: str | None             # which PC is acting, if any
    involves_grief_paragraph: bool  # True if the event touches a PC's grief-paragraph content
    is_option_c: bool               # True if session-defining personal decision
    is_hint_delivery: bool          # True if a Hint (1-4) is being delivered this beat
    is_read_aloud: bool             # True if the scene's read-aloud text needs delivering
    has_npc_dialogue: bool          # True if an NPC speaks with named voice
    is_key_loot: bool               # True if item is tagged KEY in minor-loot table
    scene_context: dict             # current scene state snapshot
```

**Single function:** `classify(event: Event) → "python" | "llm"`

**Python resolves — complete list:**

| Event type | Condition | Python handles |
|---|---|---|
| `dice_roll` | any | All dice rolls, all modifiers, CRIT/FUMBLE detection |
| `hp_delta` | any | Damage, healing, Lay on Hands |
| `resource_use` | any | Spell slots, Channel Divinity, Bless tracking |
| `doubt_die` | any | Roll 1d6, map to PC's interpretation table |
| `signature_move` | timing only | Flag when due; Python does NOT narrate it |
| `condition_apply` | any | Prone, bless, concentration, exhaustion |
| `scene_advance` | exit conditions met | Python checks mechanical conditions; LLM narrates the transition |

**LLM required — complete list:**

| Event type | Condition | Why LLM owns it |
|---|---|---|
| `read_aloud` | `is_read_aloud == True` | Scene-opening narration requires voice |
| `option_c` | `is_option_c == True` | Session-defining PC decision; Python cannot weigh a grief-paragraph |
| `dialogue` | `has_npc_dialogue == True` | NPC voice is narrative, not mechanical |
| `memory_fragment` | any | Optional atmospheric beats — pure voice |
| `atmospheric_chain` | any | One PC's reception triggering another's interior |
| `grief_beat` | `involves_grief_paragraph == True` | Python cannot adjudicate emotional weight |
| `hint_delivery` | `is_hint_delivery == True` | Hints 1-4 require narrative framing to land |
| `key_loot_narration` | `is_key_loot == True` | KEY items carry story; narration must match |
| `any` | classifier uncertain | Default: route to LLM |

---

### 6. `emitter.py` — LLM Packet Builder

**Outbound packet** (Python → LLM, written to `state/checkpoint.json` before blocking):
```json
{
  "session": "S04",
  "scene_id": 3,
  "scene_name": "Duren's Grave / The Reorx-rite",
  "beat_type": "hint-delivery",
  "state_snapshot": { "...current party state..." },
  "dice_results": [
    {"expr": "1d20+3 adv", "rolls": [9,6], "total": 12, "label": "Grom Religion DC15"}
  ],
  "resolved_mechanics": {
    "rite_result": "fail",
    "portent_available": {"kessa": [10, 4]},
    "bless_active": ["grom"],
    "bless_die_result": 2
  },
  "decision_point": {
    "type": "hint-delivery",
    "description": "Grom's rite completed (15 exactly via Portent+Bless rescue). Hint 2 unlocks. Hint 3 plants silently. Narrate the seventh-ring moment.",
    "options": null,
    "llm_required": true
  },
  "context": {
    "read_aloud": "At the instant of the clean seventh ring...",
    "gm_notes": "Hint 2: Vethrenn's margin surfaces. Hint 3: craft-witness silent reception. Self-check DC10 needed for articulation."
  },
  "scene_narrative_so_far": [
    "Scene opening read-aloud: 'The east slope is still grey when the party and Sigga walk out...'",
    "Beat 1 (Python resolved): Grom speaks the Invocation in Dwarvish...",
    "Beat 1 LLM narrative: 'Grom begins the rite. The silver-headed mallet in his left hand...'"
  ]
}
```

**Inbound packet** (LLM → Python, written by LLM in response to checkpoint prompt):
```json
{
  "narrative": "At the seventh ring, Kessa steps forward...",
  "state_updates": {
    "kessa": {"portent_used": [10]},
    "hints": {"hint-2": "unlocked"}
  },
  "innovations_flagged": ["portent-as-benediction-second-instance"],
  "advance_to_scene": 4,
  "notes_for_log": "Kessa spoke Qualinesti aloud for first time in 3 sessions."
}
```

**Inbound packet schema and validation:**

```python
@dataclass
class InboundPacket:
    narrative: str                      # required; non-empty string
    state_updates: dict                 # required; may be empty {}; keys must be known PC slugs or "hints"
    innovations_flagged: list[str]      # optional; defaults to []
    advance_to_scene: int               # required; must be >= current scene_index
    notes_for_log: str                  # optional; defaults to ""
```

**Validation rules (applied before state is written):**

| Field | Rule | On failure |
|---|---|---|
| `narrative` | Non-empty string | `ValidationError("narrative is empty")` → re-prompt |
| `state_updates` keys | Must be PC slug in loaded party OR `"hints"` | `ValidationError("unknown PC: X")` → re-prompt |
| `advance_to_scene` | Integer >= current `scene_index`; <= `len(scenes)` | `ValidationError("invalid scene advance: X")` → re-prompt |
| All fields | Valid JSON | `ValidationError("malformed JSON")` → checkpoint persists; re-prompt |

**Malformed inbound examples and handling:**

*Example 1 — empty narrative:*
```json
{"narrative": "", "state_updates": {}, "advance_to_scene": 4}
```
→ Python prints `ERROR: narrative is empty. Please revise.` Re-displays original prompt. Checkpoint persists.

*Example 2 — unknown PC in state_updates:*
```json
{"narrative": "Kessa speaks...", "state_updates": {"pella": {"hp": 5}}, "advance_to_scene": 4}
```
→ Python prints `ERROR: unknown PC slug "pella". Valid slugs: aelric-of-crownhold, thera-hillfoot, kessa-moonweave, grom-ironhand.` Re-prompt.

*Example 3 — backward scene advance:*
```json
{"narrative": "Grom acts...", "state_updates": {}, "advance_to_scene": 1}
```
→ Python prints `ERROR: advance_to_scene (1) is less than current scene (3). Scene advances must be forward.` Re-prompt.

**Checkpoint discipline:** packet written to `state/checkpoint.json` BEFORE blocking for LLM input. On `resume`, script reads checkpoint, re-displays the prompt, waits for response. When response received AND validated, checkpoint deleted and session.json updated atomically (write to `session.json.tmp`, then rename — prevents partial writes).

---

### 7. `scene.py` — Scene State Machine

**Scene lifecycle per session:**
```
PENDING → SETUP → RUNNING → RESOLVED → COMPLETE
```

**Scene engine loop:**
1. Load next scene from adventure
2. Emit read-aloud packet → LLM narrates
3. For each beat in scene:
   a. Classify: Python or LLM?
   b. If Python: resolve, update state, log
   c. If LLM: emit checkpoint packet, block, receive response, update state
4. Check scene-exit conditions (encounter resolved? trust established? key loot found?)
5. Mark scene COMPLETE, advance scene_index, write session.json

**Parallel beats** (things Python tracks while LLM narrates): wandering-pressure table rolls, per-scene manifest symptom tracking, resource delta accumulation.

---

### 8. `log_writer.py` — Session Log Producer

**Output:** `adventures/<slug>/sessions/S{N}-log.md`

**Input:** completed `session.json` + all LLM narrative responses (from inbound packets) collected during play + `dice_log.jsonl`.

**Log format template:**

```markdown
---
session: S{N}
adventure: {adventure_slug}
party: {party_slug}
date: {date}
dice-seed: {dice_seed}
duration: {duration}
outcome: {one-line outcome}
rubric-version: {rubric_version}
author: session-runner
---

# S{N} LOG — {Adventure Title}

## Session Summary
{3-5 sentences from LLM's session-summary beat response}

## Party state (delta)

| PC | HP start → end | Spells used | Attune | Notable |
|---|---|---|---|---|
{one row per PC, populated from session.json state deltas}

## Scenes

---

### Scene {N.M} — {Scene Name}

{LLM narrative response for this scene, with dice rolls injected inline}

---

## Curse symptoms landed
{from manifest tracking in session.json}

## Player-style surprises
{from innovations_flagged fields in inbound packets}

## Open threads for next session
{from LLM's final-beat response}
```

**Dice roll injection:** each `RollResult` in `dice_log.jsonl` carries a `scene_id`, `beat_index`, and `log_stub` field (set by emitter.py when the outbound packet is built). The log writer inserts the formatted roll at the `{log_stub_placeholder}` marker in the LLM narrative. If no placeholder found, appends the roll to the end of the beat's paragraph.

**Dice roll inline format:**
```
**🎲 {pc_name} {action_label}** — `{expression}` → rolls=[{rolls}] mod={mod} **total={total} ({crit_or_normal})**
```

Example:
```
**🎲 Grom Religion (Reorx-rite DC 15)** — `1d20+3 adv` → rolls=[9,6] mod=+3 **total=12 (FAIL)**
```

**Key constraint:** log writer does NOT parse LLM narrative text to find dice numbers. It uses `dice_log.jsonl` as the authoritative source and the `log_stub` field for injection point. The LLM can write `"Grom rolled poorly"` — the actual numbers come from the dice engine.

---

## Re-entrancy Contract

1. **Before every LLM beat:** write `state/checkpoint.json` (full packet + current state)
2. **On `marathon.py resume`:** read checkpoint, display beat prompt, wait for LLM response
3. **After LLM response received:** delete checkpoint, update session.json, continue
4. **On `marathon.py status`:** see exact output format below

**`marathon.py status` output format:**
```
══════════════════════════════════════════
SESSION: S04 | ADVENTURE: 0004-the-wrath-coin
SCENE: 3 — Duren's Grave / The Reorx-rite [RUNNING]
COMPLETED SCENES: 0, 1, 2

PARTY STATE:
  Aelric  HP 28/28  Slots L1:3  Attune: varran-reliquary  Conditions: —
  Thera   HP 20/20  Slots —     Attune: —                 Conditions: —
  Kessa   HP 16/16  Slots L1:4 L2:2  Attune: —  Portent: [10,4]
  Grom    HP 27/27  Slots L1:4 L2:2  Attune: —  Bless: active

PENDING CHECKPOINT: scene_3_beat_2_hint-delivery
  (resume with: python marathon.py resume)

DICE LOG: 12 rolls this session (seed: S04-20260419, position: 12)
══════════════════════════════════════════
```

If no active session: `No active session. Start one with: python marathon.py start --adventure <slug> --session <name>`
If no checkpoint: `PENDING CHECKPOINT: none`

**Guarantee:** a session interrupted at any point can be resumed with zero state loss. The only thing lost is the LLM's in-context narration — but the checkpoint packet provides full context to reconstruct it.

---

## File I/O Summary

| File | Written by | Read by | Frequency |
|---|---|---|---|
| `state/session.json` | scene.py, emitter.py | all engine components | per dice roll |
| `state/checkpoint.json` | emitter.py | marathon.py resume | per LLM beat |
| `state/dice_log.jsonl` | dice.py | log_writer.py | per roll (append) |
| `adventures/.../sessions/S{N}-prep.md` | marathon.py start | loader.py | once at start |
| `adventures/.../sessions/S{N}-log.md` | log_writer.py | pipeline (gate etc) | once at end |
| `personas/parties/.../shared-log.md` | log_writer.py | loader.py next session | once at end |

---

## Out of Scope (YAGNI)

- Multi-party support (one party, Varduin Muster)
- LLM-provider abstraction (stdin/stdout; no API calls from Python)
- Web UI or browser interface
- Campaign state mutation during play (campaign facts are read-only; session-handoff writes CLAUDE.md post-session as today)
- Automated session-gate / playtest-panel (those stay LLM-run post-session)
- Windows/Linux/Mac portability testing (Windows + bash assumed per current env)

---

## Dependencies

- Python 3.11+ (standard library only for core: `random`, `json`, `pathlib`, `dataclasses`, `argparse`)
- Optional: `pyyaml` for YAML frontmatter parsing (PC sheets have YAML frontmatter)
- No external dice libraries; no LLM SDK calls from Python

---

## LLM Interaction Protocol

**How the LLM loop works (stdin/stdout):**

1. Python prints the checkpoint JSON packet to the terminal, followed by a separator and a plain-English summary of the decision point.
2. Python writes `>>> WAITING FOR LLM RESPONSE (paste JSON below, end with EOF):` and enters `sys.stdin` read mode.
3. User (or automated pipe) pastes the LLM's inbound JSON response.
4. Python validates the inbound packet, updates state, deletes checkpoint, continues.

**Example terminal output at an LLM beat:**
```
══════════════════════════════════════════
SCENE 3 — Duren's Grave / The Reorx-rite
BEAT: hint-delivery
STATE: Grom HP 27/27 | Kessa HP 16/16 | Portent [10,4]
DICE: Grom Religion 1d20+3 adv → [9,6] → 12 (FAIL DC15)
      Portent [10] applied → 10+3+Bless(2) = 15 PASS
CONTEXT: Rite completed. Hint 2 unlocks. Hint 3 plants silently (silent RC DC10 fail).
PROMPT: Narrate the seventh-ring moment. Deliver Hint 2 (Vethrenn margin surfaces in Kessa's book).
         Hint 3 is silent craft-witness to Grom — do not articulate.
══════════════════════════════════════════
>>> WAITING FOR LLM RESPONSE (paste JSON below, end with EOF):
```

This protocol works whether the LLM is Claude Code in a terminal, a piped script, or copy-paste from a chat interface.

---

## Recovery and Failure

| Failure | Detection | Recovery |
|---|---|---|
| `checkpoint.json` missing on `resume` | File not found | Print `No checkpoint found. Use 'start' to begin a new session.` Exit 1. |
| `checkpoint.json` corrupted (invalid JSON) | JSON parse error | Print `Checkpoint is corrupted. Last good state: session.json scene {N}.` Offer: `(r) retry last beat  (s) skip to next scene  (q) quit`. |
| `session.json` corrupted | JSON parse error | Print `Session state corrupted. Cannot recover automatically.` Exit 1. Manual repair needed. |
| LLM response malformed JSON | JSON parse error | Print `Invalid JSON response. Please paste valid JSON.` Re-display prompt. Checkpoint persists. |
| LLM response fails validation | `ValidationError` | Print specific error (see emitter.py section). Re-display prompt. Checkpoint persists. |
| `module.md` missing `### Scene N` header | Section not found | `LoadError("Scene {N} not found in {file}")`. Exit 1. |
| Stat block incomplete (AC present, HP missing) | Pattern match fails | `LoadError("Missing HP in stat block at {file}:{line}")`. Exit 1. |
| PC sheet missing `heuristics` YAML block | Key not found | `LoadError("No heuristics block in {file}")`. Exit 1. |
| Unknown condition token in decision order | Interpreter lookup fails | `LoadError("unknown condition token: {token} in {file}:{line}")`. Exit 1. |
| Invalid dice expression (`"1d20+"`) | Parse error in dice.py | `DiceError("invalid expression: {expr}")`. Log to dice_log.jsonl; skip roll; continue. Print warning to terminal. |
| `advance_to_scene` backward | Validation | Re-prompt (see emitter.py section). |
| Stale checkpoint (session_id mismatch) | Compare checkpoint.session vs session.json.session | Print `Checkpoint is from a different session ({checkpoint.session} vs {current.session}). Delete it? (y/n)` |
| `session.json.tmp` exists on start (prior crashed write) | File exists check | Print `Found incomplete session write. Recovering...` Complete the rename. Continue. |

---

## Success Criteria

1. `python marathon.py start` runs a scene without requiring any bash dice calls
2. `python marathon.py resume` re-enters from a checkpoint with no state loss
3. HP, spell slots, attunements are accurate at every scene boundary
4. LLM-required beats emit a packet with enough context to narrate without reading the module
5. Final S{N}-log.md matches the format of S01-S04 logs
6. Dice rolls are reproducible: same seed + same scene sequence = same rolls
