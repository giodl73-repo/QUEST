---
name: rubric
description: Shared 8-axis 1-10 scoring rubric for persona reviews of adventures
author: human
created: 2026-04-18
---

# Adventure Review Rubric

Every persona scores an adventure on these eight axes. Score 1-10; total out of 80. Personas weight axes differently (see each persona file for weights); weighted totals are computed in `reviews/SUMMARY.md`.

## Axes

### 1. Premise clarity (1-10)
Can a DM pitch the hook in one sentence? Is the central tension obvious after reading `premise.md`?

- **1-3:** Confused, buried, or missing.
- **4-6:** Present but requires effort to extract.
- **7-9:** Crisp; fits in a sentence.
- **10:** Crisp AND irresistible.

### 2. Treasure-as-story (1-10)
Does the central artifact carry the narrative? Would cutting the treasure kill the adventure (good) or barely affect it (bad)?

- **1-3:** Treasure is incidental loot.
- **4-6:** Treasure is tied to plot but the plot could exist without it.
- **7-9:** Treasure IS the plot; finding/using it advances the story.
- **10:** Treasure is the protagonist; the dungeon is its biography.

### 3. Dungeon integrity (1-10)
Map logic, room purpose, navigation choices. Does the topology reward exploration?

- **1-3:** Linear corridor with rooms.
- **4-6:** Some branching; no loops/verticality.
- **7-9:** Loops, shortcuts, or verticality; player choice matters.
- **10:** "Jaquaysed" — multiple entries/paths, factions shift, player skill rewarded.

### 4. Encounter craft (1-10)
Balance, variety, tactical interest. Is every fight a puzzle or just HP attrition?

- **1-3:** Random monsters in square rooms.
- **4-6:** Balanced but forgettable.
- **7-9:** Terrain matters, each encounter has a distinct shape.
- **10:** Every encounter is a set-piece with real player decisions.

### 5. Lore grounding (1-10)
Setting-consistent, non-hallucinated. Does it feel like Dragonlance or generic fantasy with the serial numbers filed off?

- **1-3:** Generic; could be any setting.
- **4-6:** Surface references to Dragonlance names.
- **7-9:** Uses the age/faction/geography right; references are accurate.
- **10:** The adventure could only happen in *this* world.

### 6. Curse/consequence (1-10)
Real stakes of owning the treasure. Is the curse a mechanic, a moral weight, or both?

- **1-3:** No curse or a throwaway penalty.
- **4-6:** Curse exists but easily dispelled/ignored.
- **7-9:** Curse creates genuine dilemma; mechanical AND narrative weight.
- **10:** Owning the treasure changes the party, world, or future adventures.

### 7. Table-readiness (1-10)
Can a DM run it cold from `module.md` with no prep?

- **1-3:** Requires significant DM work to run.
- **4-6:** Runnable with 30-60 min prep.
- **7-9:** Runnable cold; stat blocks, read-aloud, and DC targets all inline.
- **10:** Runnable cold AND legible at the table under real lighting.

### 8. Player agency (1-10)
Meaningful choices. Can players shape the outcome in ways the DM didn't pre-script?

- **1-3:** Railroaded; one path through.
- **4-6:** Linear with some choice of tactics.
- **7-9:** Multiple valid routes and multiple valid endings.
- **10:** The players' choices matter so much the DM doesn't know how it ends.

## Total & Interpretation

- **65-80:** Shippable. Run it as-is.
- **50-64:** Strong draft. One more pass.
- **35-49:** Core is there; real revision needed.
- **Below 35:** Rethink the premise.

## Usage

Each review file is saved to `adventures/NNNN-<slug>/reviews/<persona-slug>-YYYY-MM-DD.md`. `SUMMARY.md` in the same directory aggregates weighted scores and dissenting opinions.
