"""event_log.py — structured D&D mechanical event logger.

Every major game action the LLM narrates gets a structured JSON entry so
we can analyse spell usage, encounter load, and resource patterns across
the campaign without manually reading session logs.

The LLM provides events via state_updates["events"] in its checkpoint
response. marathon.py resume writes them here. log_writer.py reads them
for the session log summary table.

Supported types and their required/optional fields:

  spell_cast       pc, spell, level, scene, context(combat|social|exploration)
                   [targets, concentration, expended]
  feature_used     pc, feature, scene  [result, resource_spent]
  attack           pc, target, roll, total, hit, scene  [damage, crit, fumble]
  saving_throw     pc, save, dc, roll, outcome, scene  [effect, source]
  reaction         pc, reaction, trigger, scene  [detail, target]
  condition_applied pc, condition, source, scene  [duration]
  condition_cleared pc, condition, scene
  near_death       pc, scene  [hp_before, cause, stabilized_by]
  social_roll      pc, skill, dc, roll, outcome, scene  [target, context]
  advantage_event  pc, roll_type, source, adv_or_dis, scene
  resource_recovery pc, resource, amount, scene  [rest_type]
"""
from __future__ import annotations
import json
from pathlib import Path


VALID_TYPES = frozenset({
    "spell_cast",
    "feature_used",
    "attack",
    "saving_throw",
    "reaction",
    "condition_applied",
    "condition_cleared",
    "near_death",
    "social_roll",
    "advantage_event",
    "resource_recovery",
})


class EventLogger:
    def __init__(self, log_path: Path) -> None:
        self._path = log_path

    def log(self, event: dict) -> None:
        event_type = event.get("type")
        if event_type not in VALID_TYPES:
            return  # silently drop unknown types
        with self._path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(event) + "\n")

    def log_many(self, events: list[dict]) -> None:
        for e in events:
            self.log(e)

    def load(self) -> list[dict]:
        if not self._path.exists():
            return []
        entries = []
        for line in self._path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        return entries

    def summary(self) -> dict[str, int]:
        """Return event counts by type."""
        counts: dict[str, int] = {}
        for entry in self.load():
            t = entry.get("type", "unknown")
            counts[t] = counts.get(t, 0) + 1
        return counts

    def spells_table(self) -> list[dict]:
        """Return all spell_cast events, sorted by scene."""
        return sorted(
            [e for e in self.load() if e.get("type") == "spell_cast"],
            key=lambda e: e.get("scene", 0),
        )

    def features_table(self) -> list[dict]:
        """Return all feature_used events, sorted by scene."""
        return sorted(
            [e for e in self.load() if e.get("type") == "feature_used"],
            key=lambda e: e.get("scene", 0),
        )

    def near_death_events(self) -> list[dict]:
        return [e for e in self.load() if e.get("type") == "near_death"]
