---
name: player-lenses-readme
description: The 5 player-experience review lenses used by playtest-panel — distinct from the 5 design-canon personas
author: human
created: 2026-04-18
---

# Player Lenses

Five archetypal player-experience voices that review sessions. **Distinct from the 5 design-canon personas** (Gygax et al.), who review *adventures as designed*. Player lenses review *sessions as played*.

Chronicle's analog: `.craft/roles/panel/` (Tuchman, Ibn Khaldun, Achebe, Davis, Kapuscinski). Ours are role-based rather than named-after-critics because player-experience criticism is less canonized than historical-writing criticism — but the structural discipline is the same: five productive tensions.

## Roster

| Lens | Core question they push on |
|---|---|
| [The Tactician](tactician.md) | "Were encounters fair, was positioning tactical, did mechanics matter?" |
| [The Roleplayer](roleplayer.md) | "Did my PC get to be someone specific? Did the session ask questions only my character could answer?" |
| [The Lorekeeper](lorekeeper.md) | "Did the setting feel lived in? Did the world reward attention?" |
| [The Improviser](improviser.md) | "When I went off-book, did the DM say yes?" |
| [The Fresh Face](fresh-face.md) | "Could a new player have followed this? Were conventions explained in-fiction?" |

## Why five, why these five

The five lenses tension against each other by design:

- **Tactician vs. Improviser** — "mechanical rigor" vs. "say yes to the fiction."
- **Roleplayer vs. Fresh Face** — "my PC's deep choices" vs. "a new player could follow."
- **Lorekeeper vs. Tactician** — "the world's density" vs. "the encounter's clarity."

A session that satisfies all five has held real scrutiny. A session that satisfies only one is probably tilted.

## File Format

Each lens file has:

1. **Core question** (bold, one sentence).
2. **Voice & tone** — how the lens writes.
3. **What they read for** — specific signals in the session log.
4. **Rubric weights** — their multipliers across the 8 dimensions (sum to 8.0, same convention as design personas).
5. **Red flags** — things they dock for.
6. **Greenlights** — things they elevate.

## Usage

`playtest-panel` invokes all 5 lenses against a session log, writing one review per lens to `sessions/S{N}-panel/<lens-slug>.md`. A `SUMMARY.md` aggregates weighted scores.

Playtest panels do **one round only** — sessions don't get revised (they happened). Chronicle's Round 2 has no playtest analog.

## Ethical note

These are archetypes, not impersonations. Reviews are in the voice of the *role*, not of a named critic. No real person's opinions are being simulated.
