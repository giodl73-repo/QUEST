from __future__ import annotations
import json
import random
import re
from dataclasses import dataclass, asdict
from pathlib import Path


class DiceError(Exception):
    pass


@dataclass
class RollResult:
    expression: str
    rolls: list[int]
    kept: int | None
    mod: int
    bless_roll: int | None
    total: int
    crit: bool
    fumble: bool
    seed_position: int
    scene_id: int | None = None
    beat_index: int | None = None
    log_stub: str | None = None


_EXPR_RE = re.compile(r"^(\d+)d(\d+)([+-]\d+)?$", re.IGNORECASE)


class DiceEngine:
    def __init__(self, seed: str, log_path: Path | None = None) -> None:
        self._rng = random.Random(seed)
        self._position = 0
        self._log_path = log_path

    def _roll_die(self, sides: int) -> int:
        return self._rng.randint(1, sides)

    def roll(
        self,
        expression: str,
        adv: bool = False,
        disadv: bool = False,
        bless: bool = False,
        scene_id: int | None = None,
        beat_index: int | None = None,
        log_stub: str | None = None,
    ) -> RollResult:
        expr = expression.strip().lower()
        m = _EXPR_RE.match(expr)
        if not m:
            raise DiceError(f"invalid expression: {expression!r}")

        count = int(m.group(1))
        sides = int(m.group(2))
        mod_str = m.group(3) or "+0"
        mod = int(mod_str)

        rolls = [self._roll_die(sides) for _ in range(count)]

        kept: int | None = None
        if (adv or disadv) and count == 1 and sides == 20:
            second = self._roll_die(sides)
            both = [rolls[0], second]
            rolls = both
            kept = max(both) if adv else min(both)

        base = kept if kept is not None else sum(rolls)

        bless_roll: int | None = None
        if bless:
            bless_roll = self._roll_die(4)

        total = base + mod + (bless_roll or 0)

        effective_d20 = kept if kept is not None else (rolls[0] if count == 1 else None)
        crit = (sides == 20 and effective_d20 == 20)
        fumble = (sides == 20 and effective_d20 == 1)

        result = RollResult(
            expression=expression,
            rolls=rolls,
            kept=kept,
            mod=mod,
            bless_roll=bless_roll,
            total=total,
            crit=crit,
            fumble=fumble,
            seed_position=self._position,
            scene_id=scene_id,
            beat_index=beat_index,
            log_stub=log_stub,
        )
        self._position += 1

        if self._log_path is not None:
            with self._log_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(asdict(result)) + "\n")

        return result
