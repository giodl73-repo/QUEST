from __future__ import annotations
import random
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from scripts.engine.loader import PC
    from scripts.engine.state import PartyState


class HeuristicsError(Exception):
    pass


@dataclass
class DoubtDieResult:
    roll: int
    interpretation: str


class Heuristics:
    _CONDITIONS = {
        "always": lambda ctx: True,
        "any_pc_below_half_hp": lambda ctx: ctx["party"].any_below_half_hp()
            if ctx.get("party") else False,
        "involves_evil": lambda ctx: ctx.get("involves_evil", False),
        "involves_undead": lambda ctx: ctx.get("involves_undead", False),
        "has_council_interest": lambda ctx: ctx.get("has_council_interest", False),
    }

    def __init__(self, pcs: "list[PC]") -> None:
        self._pcs: dict[str, "PC"] = {pc.slug: pc for pc in pcs}
        self._bless: dict[str, bool] = {pc.slug: False for pc in pcs}

    def _get_pc(self, slug: str) -> "PC":
        if slug not in self._pcs:
            raise HeuristicsError(f"unknown PC: {slug!r}")
        return self._pcs[slug]

    def doubt_die(self, slug: str, context: str, seed: str) -> DoubtDieResult:
        pc = self._get_pc(slug)
        dd = pc.heuristics.get("doubt_die", {})
        rng = random.Random(f"{seed}-{slug}")
        roll = rng.randint(1, 6)
        for range_str, result in dd.items():
            lo, hi = (int(x) for x in range_str.split("-"))
            if lo <= roll <= hi:
                return DoubtDieResult(roll=roll, interpretation=result)
        raise HeuristicsError(
            f"doubt_die roll {roll} matched no range in PC {slug!r}. "
            f"Check heuristics.doubt_die YAML for gaps."
        )

    def select_target(self, slug: str, enemies: list, scene_context: dict):
        """Select target enemy per PC's decision order. Returns first enemy or None."""
        if not enemies:
            return None
        return enemies[0]  # default: first enemy (full implementation in scene.py v2)

    def bless_active(self, slug: str) -> bool:
        return self._bless.get(slug, False)

    def set_bless(self, slug: str, active: bool) -> None:
        self._bless[slug] = active

    def signature_move_due(self, slug: str, moves_used_this_session: list[str]) -> str | None:
        pc = self._get_pc(slug)
        moves = pc.heuristics.get("signature_moves", [])
        for move in moves:
            if move["id"] not in moves_used_this_session:
                return move["id"]
        return None

    def eval_condition(self, condition_str: str, party: "PartyState | None" = None) -> bool:
        tokens = condition_str.split()
        return self._eval_tokens(tokens, {"party": party})

    def _eval_tokens(self, tokens: list[str], ctx: dict) -> bool:
        if not tokens:
            return False
        if "OR" in tokens:
            idx = tokens.index("OR")
            return self._eval_tokens(tokens[:idx], ctx) or self._eval_tokens(tokens[idx+1:], ctx)
        if "AND" in tokens:
            idx = tokens.index("AND")
            return self._eval_tokens(tokens[:idx], ctx) and self._eval_tokens(tokens[idx+1:], ctx)
        if tokens[0] == "NOT":
            return not self._eval_tokens(tokens[1:], ctx)
        token = tokens[0]
        if token not in self._CONDITIONS:
            raise HeuristicsError(f"unknown condition token: {token!r}")
        return self._CONDITIONS[token](ctx)
