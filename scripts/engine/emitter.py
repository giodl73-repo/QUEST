from __future__ import annotations
import json
from dataclasses import dataclass
from pathlib import Path


class ValidationError(Exception):
    pass


@dataclass
class InboundPacket:
    narrative: str
    state_updates: dict
    innovations_flagged: list[str]
    advance_to_scene: int
    notes_for_log: str


class Emitter:
    def __init__(self, state_dir: Path, party_slugs: list[str]) -> None:
        self._state_dir = state_dir
        self._party_slugs = set(party_slugs)

    @property
    def _checkpoint_path(self) -> Path:
        return self._state_dir / "checkpoint.json"

    def build_outbound(
        self,
        session: str,
        scene_id: int,
        scene_name: str,
        beat_type: str,
        state_snapshot: dict,
        dice_results: list[dict],
        resolved_mechanics: dict,
        decision_point: dict,
        context: dict,
        scene_narrative_so_far: list[str],
    ) -> dict:
        return {
            "session": session,
            "scene_id": scene_id,
            "scene_name": scene_name,
            "beat_type": beat_type,
            "state_snapshot": state_snapshot,
            "dice_results": dice_results,
            "resolved_mechanics": resolved_mechanics,
            "decision_point": decision_point,
            "context": context,
            "scene_narrative_so_far": scene_narrative_so_far,
        }

    def write_checkpoint(self, packet: dict) -> None:
        self._checkpoint_path.write_text(json.dumps(packet, indent=2), encoding="utf-8")

    def read_checkpoint(self) -> dict | None:
        if not self._checkpoint_path.exists():
            return None
        return json.loads(self._checkpoint_path.read_text(encoding="utf-8"))

    def delete_checkpoint(self) -> None:
        if self._checkpoint_path.exists():
            self._checkpoint_path.unlink()

    def validate_inbound(self, raw: dict, current_scene_index: int,
                         max_scene: int | None = None) -> InboundPacket:
        if "narrative" not in raw:
            raise ValidationError("narrative field is required")
        if not raw["narrative"]:
            raise ValidationError("narrative is empty — please provide narration")
        if "advance_to_scene" not in raw:
            raise ValidationError("advance_to_scene field is required")

        advance = raw["advance_to_scene"]
        if not isinstance(advance, int):
            raise ValidationError(
                f"advance_to_scene must be an integer, got {type(advance).__name__!r}"
            )
        if advance < current_scene_index:
            raise ValidationError(
                f"invalid scene advance: {advance} is less than current scene "
                f"{current_scene_index} — scene advances must be forward"
            )
        if max_scene is not None and advance > max_scene:
            raise ValidationError(
                f"invalid scene advance: {advance} exceeds max scene {max_scene}"
            )

        updates = raw.get("state_updates", {})
        valid_keys = self._party_slugs | {"hints", "route", "external_rolls"}
        for key in updates:
            if key not in valid_keys:
                raise ValidationError(
                    f"unknown key {key!r} in state_updates. "
                    f"Valid keys: {', '.join(sorted(valid_keys))}"
                )

        return InboundPacket(
            narrative=raw["narrative"],
            state_updates=updates,
            innovations_flagged=raw.get("innovations_flagged", []),
            advance_to_scene=advance,
            notes_for_log=raw.get("notes_for_log", ""),
        )
