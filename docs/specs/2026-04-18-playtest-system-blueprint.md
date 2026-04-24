---
title: QUEST Playtest System — Blueprint
date: 2026-04-18
status: living
author: brainstorm session + chronicle-port analysis
supersedes: none
related:
  - docs/specs/2026-04-18-dnd-workshop-design.md
  - C:\src\chronicle (prior art — read `skills/` end-to-end for the engine)
---

# QUEST Playtest System — Blueprint

A living reference for how the QUEST workshop runs playtests of its adventures. This document captures the full design as of **2026-04-18** and is intended to be read cold by future-Claude or any future collaborator.

The core design principle — **the skills are the process** — is ported from the `C:\src\chronicle` LUCIA project, where 14 skills orchestrate an 11-stage pipeline that teaches itself through an innovation-feedback loop.

---

## 1. Context & Decisions To-Date

### What already exists (workshop side)

- 6 rooms, 5 personas, 4 MVP skills + `adventure-lint`, 1 tier-1 Dragonlance adventure (`0001-tomb-of-the-silver-rose`), compiled to a table-ready `module.md`.
- 5 persona reviews of the adventure (Gygax, Jaquays, Schick, Moldvay, Stuart) at revision 1; revision 2 applied after convergent-suggestion pass; quality gates now baked into the skill files.
- All content markdown-only per CLAUDE.md conventions.

### What this blueprint adds

A **playtest subsystem** — skills, artifacts, and pipeline stages to stress-test adventures by running them with real (file-based) parties, honest dice, and emergent player-style discovery.

### Anchored decisions (from this session)

| Dimension | Decision |
|---|---|
| Playtest style for first pass (S01-S02) | **Option A — Solo DM, party as files** |
| Option C (spawn PC agents at key decisions) | **ADOPTED 2026-04-19 post-S02.** S03+ use Option C at meaningful-decision scenes. See `skills/session-runner/SKILL.md` Section 2.3. |
| Option B (4 full PC agents + DM) | Deferred indefinitely unless A + C prove insufficient |
| First party archetype | **Balanced-classic** (paladin + rogue + wizard + cleric) |
| First party name | **The Varduin Muster** |
| First playtest target | `adventures/0001-tomb-of-the-silver-rose` (revision 2) |
| Dice fairness | **Never faked.** All rolls via `scripts/dice.sh`. Session logs every roll. |
| Build order | Build 3 skills → run S01 → build remaining 4 skills informed by what S01 surfaces |
| Engine inspiration | LUCIA/chronicle — pipeline-as-OS, living rubric, innovation feedback loop |

---

## 2. What's Driving Chronicle (and therefore this port)

Chronicle is **not** driven by its rubric. It's driven by a feedback loop between five artifact types:

1. **The Pipeline** (11 stages in `chronicle-e2e/SKILL.md`) — strict order, gates block forward progress.
2. **The Rubric** (`scoring/RUBRIC.md`, versioned, forward-only) — scoring grid.
3. **The Innovations Log** (`scoring/INNOVATIONS.md`) — append-only log of techniques the rubric did not anticipate.
4. **The Voice Spectrum** (`guides/VOICE-SPECTRUM.md`) — 45+ prose registers that *emerged* from clustered innovations, not designed up front.
5. **The Panel** (`.craft/roles/panel/` — 5 voices) — reviewers whose productive tension sharpens the system.

**The engine:** write → score → notice surprises → log surprises → cluster surprises → update rubric → write the next chapter at the raised bar. Voice registers emerge when 3+ innovations cluster around a prose-register theme. The rubric evolves when 2+ innovations land in the same dimension.

Key discipline: **no session ends without a `chronicle-handoff`.** Punchlist, metrics, innovation-threshold recheck, commit, push. The system never forgets where it was.

### What we're porting

| Chronicle artifact/pattern | QUEST playtest equivalent |
|---|---|
| 11-stage pipeline (chronicle-e2e) | 7-stage pipeline (session-runner + downstream) |
| `scoring/RUBRIC.md` (versioned) | `personas/playtest-rubric.md` |
| `scoring/INNOVATIONS.md` | `personas/playtest-innovations.md` |
| `guides/VOICE-SPECTRUM.md` (emergent registers) | `personas/player-styles/` (emergent player archetypes) |
| `.craft/roles/panel/` (5 editorial voices) | `personas/player-lenses/` (5 *player-experience* voices — distinct from our 5 *designer* personas) |
| `agents/LUCY-HANDOFF-S{N}.md` | `adventures/*/sessions/HANDOFF-S{N}.md` |
| `TRACKER.md` (root-level metrics) | `TRACKER.md` (root-level; to be created) |
| Cross-compare every 3 chapters | Cross-compare every 3 sessions |
| Gate thresholds (24/30 opening, 48/60 chapter) | Session gate (56/80 suggested; tune from S01) |
| Pre-stage rubric sync | PREP stage reads rubric version + records it in prep file |

### What we're NOT porting

- **Chronicle's 4-month timeline with 26 regions, 259 peoples.** Playtest cadence is sessions (days/weeks), not chapters (hours).
- **Artifact-per-innovation** requires locked chapters. Our "locked" artifact is the session log post-finalize.
- **5 fixed intellectual voices** (Tuchman et al.). Our 5 player-lenses are role-based, not named after real critics, because player-experience is less canonized than historical-writing criticism.

---

## 3. The 7-Stage Session Pipeline

```
PREP → PLAY → LOG → GATE → PANEL → INNOVATE → HANDOFF
```

| # | Stage | Skill | Input | Output | Gate |
|---|---|---|---|---|---|
| 1 | PREP | `session-runner` | adventure + party | `sessions/S{N}-prep.md` (state, open questions, seed, rubric version) | none |
| 2 | PLAY | `session-runner` | prep file | running log | no forward block |
| 3 | LOG | `session-runner` | running log | `sessions/S{N}-log.md` (canonical) | ≥ 2,000 words; every roll logged; ≥ 3 manifest symptoms |
| 4 | GATE | `session-gate` | session log | `sessions/S{N}-gate.md` scorecard | 56+ / 80 (tune after S01) |
| 5 | PANEL | `playtest-panel` | session log | `sessions/S{N}-panel/<lens>.md` (5 files) | all 5 written |
| 6 | INNOVATE | `playtest-innovation` | session log + prior innovations | append to `personas/playtest-innovations.md`; propose at threshold | threshold recheck |
| 7 | HANDOFF | `session-handoff` | everything | `sessions/HANDOFF-S{N}.md`; `TRACKER.md` updated | committed |

**Gate discipline:** GATE and PANEL block forward progress ONLY IF WE WANT THEM TO. First few sessions, gates are *advisory* — we're learning. After S03, we lock the gate thresholds.

---

## 4. Skill Roster

Status as of 2026-04-18:

### Workshop skills (pre-existing, revised)
- ✅ `dungeon-smith` — Quality Gates added, cross-skill contract with `treasure-forger`
- ✅ `treasure-forger` — Presence/Desire required; emits Curse Symptoms Manifest
- ✅ `module-binder` — inlines critical SRD rules on cheatsheet
- ✅ `adventure-lint` — pre-compile gate validator (pipeline position: pre-`module-binder`)
- ⏳ `lore-weaver` — deferred to Phase 6
- ⏳ `encounter-balancer` — deferred to Phase 6
- ⏳ `rule-lookup` — deferred to Phase 6
- ⏳ `persona-review` — deferred; to be informed by `playtest-panel`

### Playtest skills (new)
- ✅ `party-builder` — produces `personas/parties/<slug>/` dir
- ✅ `dice-roller` — wraps `scripts/dice.sh`
- ✅ `session-runner` — PREP + PLAY + LOG stages; Claude-as-DM
- ⏳ `session-gate` — stage 4; scores session against living rubric
- ⏳ `playtest-panel` — stage 5; 5 player-experience lenses
- ⏳ `playtest-innovation` — stage 6; scouts session log for surprises; threshold check
- ⏳ `session-handoff` — stage 7; metrics, punchlist, commit

### Build order

Build first, run, then build the rest:
1. `party-builder` ✅ done
2. `dice-roller` + `scripts/dice.sh` ✅ done
3. `session-runner` ✅ done
4. **Pause: run S01** (Varduin Muster vs. Tomb of the Silver Rose).
5. Build `session-gate` — informed by S01's outcomes.
6. Build `playtest-panel` — lens catalog informed by what S01 revealed about player experience.
7. Build `playtest-innovation` — pattern catalog informed by S01's `<!-- SURPRISE -->` tags.
8. Build `session-handoff` — informed by what state we actually need to carry forward.

---

## 5. The Three Living Artifacts

These files evolve across sessions. They are the workshop's memory.

### 5.1 `personas/playtest-rubric.md` (TO BE CREATED)

Versioned scoring grid for session quality. Forward-only: a new version applies to sessions scored **after** the amendment, never retroactively. Amendments logged with rationale.

Seed dimensions (tentative — will evolve):
1. **Engagement** — did the table (DM + PCs) stay invested?
2. **Mechanical fairness** — did rolls land honestly; were DCs appropriate?
3. **Pacing** — did scenes earn their length?
4. **Character agency** — did PCs matter; were choices real?
5. **Module fidelity** — did the adventure deliver what it designed?
6. **Atmospheric landing** — did intended moments (curse reveal, fresco heal, Memory Echo) hit?
7. **Surprise** — did anything emergent happen?
8. **Table readiness** — could a human DM have run this session cold from the artifacts?

8 axes × 10 pts = /80. Gate threshold: 56+ (70%) initially; tune after S03.

### 5.2 `personas/playtest-innovations.md` (TO BE CREATED)

Append-only log. Each entry:
- Source session + scene
- Dimension touched
- What happened (quoted from session log where possible)
- Why the rubric didn't anticipate it
- Scope: party-specific / adventure-specific / universal
- Status: `logged` / `proposed` / `adopted (vX.X)` / `reviewed — not adopted`

**Thresholds:**
- 2+ in a dimension → propose rubric amendment
- 3+ clustered by theme (across different sessions/adventures) → propose new **player-style** entry

### 5.3 `personas/player-styles/` (TO BE POPULATED — empty at start)

Emergent archetypes. Each entry is a markdown file with:
- Style name (e.g., "The Unexpected Alliance," "The Rules Lawyer," "The Question-Asker")
- Source sessions/PCs (≥ 3 instances across ≥ 2 sessions)
- Definition of the style
- Triggers / signals
- Cross-applicability (which party archetypes would benefit from this style)
- Seeded innovations (the innovations that clustered into this style)

**We start with 0 styles.** Styles emerge. Chronicle needed ~15 chapters before Voice Spectrum v1.4 — we shouldn't expect styles to settle before ~5 sessions.

---

## 6. Directory Structure (target state)

```
marathon/
├── CLAUDE.md
├── TRACKER.md                                # root metrics (to be created)
├── scripts/
│   └── dice.sh                               # ✅
├── docs/specs/
│   ├── 2026-04-18-dnd-workshop-design.md     # initial spec
│   └── 2026-04-18-playtest-system-blueprint.md   # this file
├── skills/
│   ├── dungeon-smith/                        # ✅
│   ├── treasure-forger/                      # ✅
│   ├── module-binder/                        # ✅
│   ├── adventure-lint/                       # ✅
│   ├── party-builder/                        # ✅
│   ├── dice-roller/                          # ✅
│   ├── session-runner/                       # ✅
│   ├── session-gate/                         # ⏳ post-S01
│   ├── playtest-panel/                       # ⏳ post-S01
│   ├── playtest-innovation/                  # ⏳ post-S01
│   └── session-handoff/                      # ⏳ post-S01
├── reference/
│   ├── srd/
│   └── dragonlance/
├── personas/
│   ├── rubric.md                             # design rubric (adventures)
│   ├── playtest-rubric.md                    # ⏳ session rubric (to be created with session-gate)
│   ├── playtest-innovations.md               # ⏳ living log (append-only)
│   ├── player-styles/                        # ⏳ empty at start; emergent
│   ├── player-lenses/                        # ⏳ 5 voice files for playtest-panel
│   ├── gygax.md · jaquays.md · schick.md · moldvay.md · patrick-stuart.md    # ✅
│   └── parties/
│       └── varduin-muster/                   # ✅ being built
│           ├── README.md
│           ├── aelric-of-crownhold.md        # paladin
│           ├── thera-hillfoot.md             # rogue
│           ├── kessa-moonweave.md            # wizard
│           ├── grom-ironhand.md              # cleric
│           └── shared-log.md                 # session carryover
└── adventures/
    └── 0001-tomb-of-the-silver-rose/
        ├── premise.md · module.md · etc.     # ✅
        └── sessions/                         # ⏳ created on S01
            ├── S01-prep.md
            ├── S01-log.md
            ├── S01-gate.md                   # post-S01
            ├── S01-panel/                    # post-S01
            │   ├── tactician.md
            │   ├── roleplayer.md
            │   ├── lorekeeper.md
            │   ├── improviser.md
            │   └── fresh-face.md
            └── HANDOFF-S01.md
```

---

## 7. The Five Player-Lenses (for `playtest-panel` stage 5)

These are **different** from our 5 design personas (Gygax et al.). Design personas review the *adventure as designed*; player-lenses review the *session as played*.

| Lens | Question they push on |
|---|---|
| **The Tactician** | Were encounters fair? Did positioning / resources matter? Were crits and fumbles consequential? |
| **The Roleplayer** | Did my PC get to be someone specific? Did the adventure ask questions only my character could answer? |
| **The Lorekeeper** | Did the setting feel lived in? Were there references that rewarded attention? Did the world react to my curiosity? |
| **The Improviser** | When I went off-book, did the DM say yes? Or did the adventure funnel me? |
| **The Fresh Face** | Could a new player have followed this session? Were conventions explained in-fiction? |

Each lens will get a `personas/player-lenses/<slug>.md` file (structure like our existing persona files) **once we build `playtest-panel`**. Deferred to post-S01 so the lens definitions are informed by what S01 actually surfaces.

---

## 8. First Playtest Scope — S01

- **Party:** The Varduin Muster (balanced-classic, level 3).
- **Adventure:** `0001-tomb-of-the-silver-rose` revision 2.
- **Pipeline:** stages 1-3 automated (`session-runner`). Stages 4-7 run as human-assisted afterthoughts (we build the skills after).
- **Dice seed:** `S01-2026-04-18`.
- **Expected session length:** ~3 real hours of Claude-DM playing; ~3-4 in-fiction hours of adventure time.
- **Expected outputs:** `sessions/S01-prep.md`, `sessions/S01-log.md` (≥ 2,000 words), `personas/parties/varduin-muster/shared-log.md` updated.
- **Expected surprises:** 3-8 `<!-- SURPRISE -->` tags in the log. These seed `playtest-innovations.md`.
- **No player-styles will emerge.** Styles need clustering across ≥ 3 sessions.

### What we're specifically testing in S01

1. **Module fidelity** — does the `module.md` work cold, or are there gate violations the lint missed?
2. **Manifest-symptom landing** — do the curse symptoms (VANOR drift, repeated phrase, fresco heal, attribution drift) actually hit in play, or do they die on the page?
3. **Option B discovery** — does a balanced-classic party find the Notched Longsword → sarcophagus-slot connection unprompted?
4. **Brother Laen's negotiation matrix** — when the party returns, does the matrix produce realistic-feeling outcomes, or does it read as spreadsheet?
5. **Curse reveal pacing** — the rose curse first reveals on the third long rest. We're running one session; can the reveal land in-session or does it require a second session to bite?

---

## 9. YAGNI Guardrails

- **No `session-gate` until we have one session to score.** Building the rubric before play produces a rubric that plays nothing.
- **No `playtest-panel` until we see what lenses the session log wants.** The 5-lens sketch above is provisional.
- **No `player-styles/` entries until clustering threshold hits.** The directory is empty until ≥ 3 innovations cluster.
- **No Option C (per-PC agents) until Option A's limitations are concrete.** "Sometimes the DM plays all PCs too similarly" is not yet an observed failure — it's a prediction.
- **No orchestrator skill** until the pipeline has run end-to-end manually ≥ 2 times.
- **No publishing format** until someone asks to share a session log externally.

---

## 10. Feedback-Loop Discipline (the core of the port)

After every session, these steps are mandatory:

1. **`session-gate`** scores it.
2. **`playtest-panel`** reviews it across 5 lenses.
3. **`playtest-innovation`** scans for surprises.
4. **Threshold check:**
   - Any dimension with 2+ `logged` innovations → propose rubric amendment.
   - Any 3+ thematic cluster across sessions → propose new player-style.
5. **Amendments** (if approved): update rubric version, mark innovations `adopted (vX.Y)`, write amendment entry to history table.
6. **`session-handoff`** writes the punchlist for next session.
7. **Commit.**

**Without this loop, playtesting is just session recordings.** The loop is what makes playtesting a learning system.

---

## 11. Glossary

- **Adventure** — A designed, versioned, reviewable module. e.g., `0001-tomb-of-the-silver-rose`. Artifact of `dungeon-smith` + `treasure-forger` + `module-binder`.
- **Session** — A single playthrough. Artifact of `session-runner`. Numbered globally (S01, S02, ...) across all adventures for this workshop's traceability.
- **Party** — A file-based group of PCs. Lives in `personas/parties/<slug>/`.
- **Manifest** — A cross-skill contract file emitted by `treasure-forger` listing curse symptoms `dungeon-smith` must express.
- **Curse Symptom** — A dungeon-level reaction to a cursed artifact's presence (attribution drift, orthographic drift, repeated phrase, etc.).
- **Innovation** — A technique/move/surprise not anticipated by the current rubric. Logged in `personas/playtest-innovations.md`.
- **Player Style** — An emergent player archetype (≥ 3 clustered innovations across ≥ 2 sessions). Promoted to `personas/player-styles/<slug>.md`.
- **Design Persona** — The 5 design-canon voices (Gygax, Jaquays, Schick, Moldvay, Stuart). Review adventures.
- **Player Lens** — The 5 player-experience voices (Tactician, Roleplayer, Lorekeeper, Improviser, Fresh Face). Review sessions. Different from design personas.
- **Gate** — A stage-boundary quality threshold. Blocks forward progress (or is advisory in early sessions).

---

## 12. Next Actions (as of this blueprint's creation)

- ⏳ Finish building The Varduin Muster (README + 4 PC sheets). *In flight.*
- ⏳ Run S01 — `session-runner` on 0001 with the Muster.
- ⏳ Post-S01, harvest lessons and build skills 4-7.
- ⏳ After 3 sessions, expect rubric amendments. After 5+, expect first player-style to emerge.

## 13. Post-S02 Update (2026-04-19)

**Rubric:** v1.2 (two amendments adopted: anchor-level passive-Perception fallback + finder-vs-receiver separation with silent-reception recognition).

**Player-styles promoted — FIRST EVER** (2 clusters fired post-S02):
- `sheet-deep-reader` — PC-sheet-hidden content drives session-level agency.
- `craft-witness` — Craft-ritual PCs deliver non-standard atmospheric reception.

**Option C adopted.** At meaningful-decision scenes, `session-runner` spawns a per-PC subagent via the `Agent` tool. See `skills/session-runner/SKILL.md` Section 2.3.

**Campaign-mode reconciliation.** QUEST is a campaign with anthology-floor: accessibility for new readers; cross-adventure reward for campaign readers. See `CLAUDE.md#accessibility-policy` (updated).

**Aelric's attuned-memory state is campaign-permanent.** See `CLAUDE.md#campaign-continuity`.

**Expected rate-of-cluster was slower than actual.** The blueprint predicted first player-style between S03-S05; actual was post-S02. Re-calibrate future predictions accordingly.
