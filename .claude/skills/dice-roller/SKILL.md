---
name: dice-roller
description: Roll D&D dice deterministically via the Rust QUEST CLI, never by Claude-faking numbers. Use for every resolution roll during a playtest session — attacks, saves, skill checks, damage, curse saves. Supports NdS+M, advantage, disadvantage, bless, and d20-crit detection. Logs every roll to the session log with a seed for reproducibility.
---

# dice-roller

**Claude does not fake dice.** Every die in a playtest goes through `cargo run -- roll ...` so rolls are real, reproducible, and auditable.

## Why this skill exists

A DM running a session needs to roll dice honestly. Claude improvising numbers is forbidden in this workshop — it poisons playtest data and makes the persona-panel reviews meaningless. Every roll is:

1. **Rolled by the Rust engine** (`rally-core::RunSeed`, seeded at session start).
2. **Logged to the session log** with context (who, what, against what DC).
3. **Auditable** — anyone can re-roll from the seed and see the same sequence.

## Usage

From the QUEST repo root:

```bash
cargo run -- roll 1d20+5 --seed S01-scene01
# → rolls=[14] mod=5 total=19

cargo run -- roll 1d20+3 --seed S01-scene01 --adv
# → rolls=[7, 18] (adv → 18) mod=3 total=21

cargo run -- roll 2d6+2 --seed S01-scene01
# → rolls=[4 3] mod=2 total=9
```

Expressions:

- `NdS` or `NdS+M` or `NdS-M` — N dice of S sides with optional modifier.
- `--adv` — only valid on `1d20`. Rolls twice, keeps higher.
- `--disadv` — only valid on `1d20`. Rolls twice, keeps lower.
- `--bless` — adds a seed-locked `1d4`.

Crit detection on `1d20`: if any die is 20, the output includes `CRIT`; if 1, includes `FUMBLE`.

## Seeding

At session start, `session-runner` names the deterministic seed:

```bash
cargo run -- roll 1d20 --seed S{N}-<YYYY-MM-DD>-scene01
```

For **reproducible playtests**, always pass an explicit `--seed`.

## Integration with session-runner

`session-runner` calls `dice-roller` for every mechanical resolution. Each call must also append a line to the session log:

```markdown
**🎲 Aelric attacks skeleton A (warhammer)** — `1d20+5` → rolls=[14] mod=5 **total=19 (hit)** · damage `1d8+3` → rolls=[5] mod=3 **7 bludgeoning**
```

Format: PC name + action + attack/save roll + (hit/miss) + damage if hit. Include the raw dice output so audits are possible.

## Rolls the DM must NEVER fake

This list is explicit. These rolls MUST go through the script:

- Attack rolls and damage
- Saving throws (all)
- Ability / skill checks
- Wisdom saves for the Silver Rose curse (DC 11, escalating)
- Wandering-pressure table rolls (d6 every 30 min)
- Cold Pulse table rolls (d6 every 10 min)
- Death saving throws
- Initiative
- Any d6 "in doubt" PC-behavior roll from Playstyle Heuristics
- Percentile rolls

## What Claude DOES decide

The skill does not replace DM judgment — it replaces RNG fakery. Claude still:

- Sets DCs based on the room's features and 5e conventions.
- Narrates outcomes, interpreting the number into the fiction.
- Decides whether advantage / disadvantage applies.
- Decides target priority for NPCs (per monster tactics in the encounter file).
- Decides whether to apply a modifier (e.g., Bless +1d4, which itself rolls via the script).

## Output

Nothing written to files by this skill directly. It produces numbers that the calling skill (session-runner, or a human user) writes into the session log.

## The script

Lives in `src/main.rs` as the `roll` command. Any fork or sibling implementation MUST match the output contract above: lines of the form

```
rolls=[<space-separated-ints>] mod=<int> total=<int> [CRIT|FUMBLE]
```

so `session-runner` can parse consistently.

## Quality gates

- [ ] Every session log has at least one `🎲` line per combat round.
- [ ] No session log contains a resolution without a corresponding dice line upstream.
- [ ] DICE_SEED is set at session start and logged in the PREP stage.
- [ ] For playtest reproducibility: the same seed + same PC decisions = the same session log.

## Anti-patterns

- "Let me check if this hits... yes, it hits." (No roll logged.)
- "Rolling mentally... 14." (Not real.)
- Rolls that happen to always succeed when it's convenient.
- Damage rolls rounded to "average."
- Saves decided by tension rather than DC.
