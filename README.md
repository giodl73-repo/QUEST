# QUEST — A D&D Workshop That Learns From Itself

QUEST is a workshop for **designing, playtesting, and improving D&D 5e adventures** in the Dragonlance setting. It is one repository in a family of **Emergent Skills AI** projects — systems where skills, rubrics, and player archetypes are *discovered through use* rather than designed up front.

Creative principle: **the treasures are the story.** Every adventure is seeded by an artifact whose history carries the narrative weight; curses and consequences make loot a real decision.

**Review roles:** This repo uses
[ROLES](https://github.com/giodl73-repo/ROLES), the `.roles` convention for
repository-local review panels.

---

## Mission

Three things happen here, in order, on a loop:

1. **Analyze** — read the session log, the panel reviews, and the gate scorecard; surface every move the rubric did not anticipate.
2. **Design** — compose adventures, parties, NPCs, treasures, and campaigns through a pipeline of small, single-purpose skills.
3. **Script** — run the adventure at the table via a deterministic Rust engine that owns the mechanical layer (dice, state, event logging, route state) and leaves narrative to the LLM.

The output of step 3 feeds step 1. The learnings from step 1 change step 2. The rubric, the player-style catalog, and the skills themselves are versioned artifacts that mutate across sessions.

---

## The Emergent Skills AI pattern

QUEST is a **port** of the pattern first built in `chronicle` (the LUCIA project, a long-form novel engine). Same skeleton, different medium:

| Chronicle (prose)              | QUEST (D&D)                            |
|---                             |---                                     |
| 11-stage writing pipeline      | 7-stage session pipeline               |
| Versioned scoring rubric       | Versioned playtest rubric              |
| Append-only innovations log    | Append-only innovations log            |
| Voice Spectrum (45+ registers) | Player-style catalog (6+ styles)       |
| 5-voice review panel           | 5 design personas + 5 playtest lenses  |
| `chronicle-handoff` ritual     | `session-handoff` ritual               |

Core discipline shared by both repos:

> **write → score → notice surprises → log surprises → cluster surprises → update rubric → write the next thing at the raised bar.**

Nothing in the catalogs is pre-seeded. Every player-style in `personas/player-styles/` was **promoted** from a cluster of observed play, not designed. Every rubric amendment was triggered by 2+ innovations landing in the same dimension. The system teaches itself.

---

## Repository layout

```
marathon/
├── CLAUDE.md                   conventions (frontmatter, naming, accessibility)
├── TRACKER.md                  living per-session score + verdict table
├── .claude/skills/             20 single-purpose skills (see below)
├── Cargo.toml                  Rust game engine crate
├── src/main.rs                 CLI: start / resume / status / roll / bind-module
├── personas/
│   ├── rubric.md               8-axis design rubric (persona reviews)
│   ├── playtest-rubric.md      8-axis play rubric (live-table scoring)
│   ├── playtest-innovations.md append-only surprise log
│   ├── gygax.md  jaquays.md  schick.md  moldvay.md  patrick-stuart.md
│   ├── player-lenses/          5 live-play lenses (tactician, roleplayer, …)
│   ├── player-styles/          EMERGENT catalog (discovered, not designed)
│   └── parties/                one directory per playable party
├── reference/
│   ├── srd/                    cached 5e SRD (CC-BY-4.0)
│   └── dragonlance/            curated lore + workshop-canon
├── adventures/NNNN-<slug>/     premise, rooms, treasures, encounters, npcs,
│                               module.md, reviews/, sessions/
├── campaign/                   per-campaign seed trackers
├── docs/
│   ├── specs/                  design docs for every major system
│   └── campaign/               per-campaign spines + retrospectives
└── state/                      runtime state (session.json, dice_log.jsonl, …)
```

---

## The skills

Twenty skills live in `.claude/skills/`. Each one does one thing. They compose into the pipeline.

**Design (build an adventure):**
`campaign-planner` → `arc-audit` → `dungeon-smith` → `treasure-forger` → `npc-architect` → `encounter-balancer` → `lore-weaver` → `adventure-lint` → `module-binder` → `persona-review` → `dm-letter`

**Play (run a session):**
`session-runner` → `dice-roller` + `rule-lookup` (mid-session)

**Learn (close the loop):**
`session-gate` → `playtest-panel` → `playtest-innovation` → `seed-tracker` → `session-handoff`

Each skill is a markdown file with frontmatter, preconditions, procedure, quality gates, and anti-patterns. See `.claude/skills/<skill>/SKILL.md`.

---

## The 7-stage session pipeline

Every playtest session passes through seven stages. No session ends without stage 7.

| # | Stage      | Skill                 | Artifact                                    |
|---|---         |---                    |---                                          |
| 1 | PREP       | `session-runner`      | `sessions/S{N}-prep.md`                     |
| 2 | PLAY       | `session-runner`      | running log + `state/*.jsonl`               |
| 3 | LOG        | `session-runner`      | `sessions/S{N}-log.md`                      |
| 4 | GATE       | `session-gate`        | `sessions/S{N}-gate.md` (scored against locked rubric version) |
| 5 | PANEL      | `playtest-panel`      | `sessions/S{N}-panel/*.md` + `SUMMARY.md`   |
| 6 | INNOVATION | `playtest-innovation` | appended entries in `playtest-innovations.md` |
| 7 | HANDOFF    | `session-handoff`     | `sessions/HANDOFF-S{N}.md` + `TRACKER.md` updated + commit |

Gates block forward progress. The rubric version is **locked at PREP** and applied at GATE — forward-only; earlier sessions are never re-scored.

---

## The learning loop — how innovations become catalog entries

`playtest-innovation` runs two threshold checks after every session:

- **Rubric amendment** — 2+ innovations in the **same dimension** → draft amendment → user ratifies → rubric version bumps → next session PREP locks the new version.
- **Player-style emergence** — 3+ innovations **clustered by theme across ≥ 2 sessions** → draft new `personas/player-styles/<slug>.md` → user ratifies → skills start treating the style as a first-class thing.

**What's already emerged (as of 2026-04-22):**

| Style | Promoted | Cross-campaign instances |
|---|---|---|
| `sheet-deep-reader`          | v1.1 | 40+ |
| `craft-witness`              | v1.1 | confirmed session-invariant |
| `act-without-announcement`   | v1.5 | 12+ (C1, C2, C4) |
| `verbal-documentation-arc`   | C3   | 3-stage arc completed end-to-end |
| `npc-arc-completion`         | C3   | 8/8 in C3, recurs in C4–C7 |
| `documentary-witness`        | C4   | proposed; validated in C5 |

The rubric has moved v1.0 → v1.12 across seven campaigns without a single retroactive rescore.

---

## The game engine (`quest`)

Live play is driven by a small Rust engine backed by `rally-core`. The LLM runs the narrative; Rust owns dice, state, event logging, route tracking, and checkpoint validation.

```bash
# start a new session
cargo run -- start --adventure 0007-the-silver-ingot-confession \
                  --session S07 \
                  --party compact-wardens

# resume at the last checkpoint (the engine writes one before every LLM beat)
cargo run -- resume

# inspect current state: party HP, slots, attunements, pending checkpoint, dice rolls,
# aggregated event-log summary
cargo run -- status

# seed-locked mechanical roll
cargo run -- roll 1d20+5 --seed S07-scene6 --adv --bless

# compile an adventure directory into module.md
cargo run -- bind-module 0007-the-silver-ingot-confession
```

Pieces:

- **`src/main.rs`** — CLI entry point; re-entrant via `state/checkpoint.json`.
- **`src/lib.rs`** — reusable crate surface for non-CLI runners, including
  `run_cli()`, `DiceEngine`, `RollOptions`, `ai_dm_muddle_surface()`, and
  `ai_dm_muddle_host()`.
- **`DiceEngine` + `rally-core::DiceRoller`** — seed-locked RNG; every CLI roll can be logged to `state/dice_log.jsonl` with a reproducible seed. No faked rolls; no mental rolls.
- **`PersistedState`** — party/session/campaign facts persisted as JSON.
- **Module + party loaders** — parse `module.md` + PC sheets into Rust structs for deterministic session setup.
- **Inbound checkpoint validator** — accepts narrative packets from the LLM, validates scene advancement and mutable state keys, writes accepted events to `state/event_log.jsonl`, and clears checkpoints.
- **`bind-module`** — compiles an adventure directory into a table-ready `module.md` with scenes and a DM cheatsheet.
- **`quest-muddle`** — product-owned MUDDLE launcher for a deterministic
  AI-DM table loop with visible threat, party focus, treasure consequence, and
  transcript/save support.
- **`quest-muddle-window`** — product-owned MUDDLE window launcher over the
  same AI-DM host and shared window runner.

The engine is what lets `session-runner` claim its "no fake rolls" quality gate with a straight face.

Reusable callers should link the crate instead of shelling out:

```rust
let code = quest::run_cli(vec!["status".to_string()]);
let mut dice = quest::DiceEngine::new("S07-scene6", None);
let roll = dice.roll_options(quest::RollOptions {
    expression: "1d20+5".to_string(),
    advantage: true,
    disadvantage: false,
    bless: true,
    scene_id: Some(6),
    beat_index: Some(0),
    log_stub: Some("library roll".to_string()),
})?;
let mut host = quest::ai_dm_muddle_host();
```

```bash
cargo run --bin quest-muddle -- --save target\quest-ai.muddle --transcript target\quest-ai.txt
cargo run --bin quest-muddle-window -- --open
```

---

## Track record

Seven campaigns, forty-nine sessions, one workshop:

| Campaign | Spine | Sessions | Route | Notable output |
|---|---|---|---|---|
| **C1 — Moon-Silver Cycle**  | "What is an emotion worth trading?"          | 7 | D×7 | Rubric v1.0 → v1.4; 2 player-styles; Silver-Ingot Confession spoken |
| **C2 — The Conclave Compact** | "When a covenant breaks, who bears the cost?" | 7 | D×7 | Rubric v1.4 → v1.5; 100% manifest every session; compact spoken |
| **C3 — The Halted Spire**    | "Who gets to decide who is worth saving?"    | 7 | D×7 | Rubric v1.8; 2 new styles; 8/8 NPC arcs; module binder built here |
| **C4 — The Thorngate Watch** | "How much of yourself do you spend on people who don't trust you yet?" | 7 | E×1 | Rubric v1.11; documentary-witness proposed; hardest-route siege resolved |
| **C5 — The Silken Ledger**   | "When the guild you serve becomes the thing you're stealing from…"     | 7 | B | RV1–RV4 all confirmed; PC-authored deliverable (false dossier) |
| **C6 — The Border Watch**    | "When orders become wrong, how do you know — and who do you tell?"     | 7 | E | RV5–RV8 all confirmed; Unit Cohesion Die mechanic validated |
| **C7 — The Convergence**     | "When people with nothing in common must act as one, what do they share?" | 7 | E | RV9–RV12 all confirmed; player-styles fire without grief/duty anchors |

Every campaign has a **design spec** in `docs/specs/` and a **retrospective** in `docs/campaign/`. Both are kept. The retrospectives are where the Research Validation verdicts (RV1 … RV12) live — the workshop's way of asking "is the thing we think we know actually true across parties we didn't design for?"

---

## Conventions

- **Markdown at the table.** No YAML/JSON migration until the medium hurts. It hasn't yet.
- **Every generated file carries frontmatter.** `adventure`, `author`, `created`, `sources`. See `CLAUDE.md`.
- **Never overwrite silently.** Skills append, write to a new file, or prompt.
- **Accessibility policy.** First use of setting-specific terms is glossed in-fiction; mechanics are translated to fiction in narrative prose. Campaign readers get the cross-adventure layer; new readers get a floor that stands alone.
- **Campaign continuity is canon.** Facts established in played sessions bind future narration. `CLAUDE.md` aggregates the campaign-permanent facts for every campaign.
- **Canon policy.** Dragonlance-native, not Dragonlance-adjacent. Invent where canon is silent; track every invented name in `reference/dragonlance/workshop-canon.md`.
- **YAGNI guardrails.** No orchestrator skill until the manual pipeline has run end-to-end twice. Every reference file earns its place by being needed.

---

## Getting oriented

- **New reader:** start with `CLAUDE.md` (conventions + campaign state), then `docs/specs/2026-04-18-dnd-workshop-design.md` (original design) and `docs/specs/2026-04-18-playtest-system-blueprint.md` (the learning loop).
- **Want to see the loop in action:** read any `docs/campaign/*-retrospective.md`. The RV verdicts show the workshop asking and answering questions about its own design.
- **Want to run a session:** read `.claude/skills/session-runner/SKILL.md`, pick an adventure with a `module.md`, pick a party, and run `cargo run -- start …`.
- **Want to propose a change:** write a spec in `docs/specs/YYYY-MM-DD-<slug>.md`. That is how every major system here started.

The workshop is a loop. Feed it a session; it feeds you a better rubric.

---

## Research

Six papers document findings from the workshop's seven campaigns. LaTeX sources in [`research/publications/`](research/publications/); build all PDFs with `make -C research`.

- [The 7-Session Campaign Spine: Evidence-Based Architecture for Emotionally Complete Narrative Arcs](research/publications/glyph-campaign-spine/main.pdf)
- [Designing NPC Arc-Completion Conditions](research/publications/glyph-npc-arc/main.pdf)
- [Emergent Player Styles in AI-Simulated TRPG](research/publications/glyph-player-style/main.pdf)
- [Resource Exhaustion as Narrative Amplifier](research/publications/glyph-resource-exhaustion/main.pdf)
- [Innovation-Cluster-Driven Rubric Amendment](research/publications/glyph-rubric-amendment/main.pdf)
- [An 8-Dimension Playtest Rubric as a Research Instrument](research/publications/glyph-rubric-instrument/main.pdf)

---

## License

QUEST is released under the **MIT License** — see [`LICENSE`](LICENSE).

Third-party content carries its own terms:

- **5e SRD** in `reference/srd/` is Wizards of the Coast's System Reference Document, used under **CC-BY-4.0**. See `reference/srd/LICENSE.md`.
- **Dragonlance** is a Wizards of the Coast setting. Files in `reference/dragonlance/` are curated notes for the workshop's use; invented names and lore added by this project are tracked in `reference/dragonlance/workshop-canon.md` and are released under the MIT License together with the rest of this repository.
