"""scene.py — Scene state machine for the Marathon session engine.

Each scene is processed as an ordered sequence of beats:
  0. read_aloud       — LLM-required; emits scene read-aloud text
  1. encounter_dice   — Python-resolved; only if scene.stat_blocks is non-empty;
                        rolls 1d20 initiative per enemy
  2. scene_narration  — LLM-required; DM narrates main scene content
  3. scene_exit       — Python-resolved; marks scene complete, advances session

Beat progress is tracked in session.pending_checkpoint using the format:
  "scene_{scene_index}_beat_{beat_index}"

After scene_exit: advance to next scene (beat_index resets to 0, scene_index += 1).
If no more scenes: status = "session_complete".
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from scripts.engine.loader import Adventure, Scene
    from scripts.engine.state import PartyState, SessionState, CampaignFacts
    from scripts.engine.dice import DiceEngine, RollResult
    from scripts.engine.heuristics import Heuristics
    from scripts.engine.emitter import Emitter
    from scripts.engine.state import StateManager


@dataclass
class RunResult:
    status: str           # "python_resolved" | "llm_required" | "scene_complete" | "session_complete"
    beat_type: str        # e.g. "read_aloud", "encounter_dice", "scene_narration", "scene_exit"
    dice_results: list    # list of RollResult (may be empty)
    narrative_so_far: list[str]  # accumulated scene narrative from this run
    checkpoint_written: bool


# ---------------------------------------------------------------------------
# Beat index → beat name mapping
# ---------------------------------------------------------------------------
# Beats are positional. For a scene WITHOUT stat_blocks:
#   0: read_aloud, 1: scene_narration, 2: scene_exit
# For a scene WITH stat_blocks:
#   0: read_aloud, 1: encounter_dice, 2: scene_narration, 3: scene_exit
#
# We derive these dynamically based on scene content.

_BEAT_NO_ENCOUNTER = ["read_aloud", "scene_narration", "scene_exit"]
_BEAT_WITH_ENCOUNTER = ["read_aloud", "encounter_dice", "scene_narration", "scene_exit"]


def _beats_for_scene(scene: "Scene") -> list[str]:
    if scene.stat_blocks:
        return _BEAT_WITH_ENCOUNTER
    return _BEAT_NO_ENCOUNTER


# ---------------------------------------------------------------------------
# Cursor helpers
# ---------------------------------------------------------------------------

def _parse_cursor(cursor: str | None) -> tuple[int, int]:
    """Parse "scene_{si}_beat_{bi}" → (scene_index, beat_index).

    Returns (0, 0) if cursor is None or unparseable.
    """
    if not cursor:
        return 0, 0
    try:
        parts = cursor.split("_")
        # format: ["scene", si, "beat", bi]
        if len(parts) == 4 and parts[0] == "scene" and parts[2] == "beat":
            return int(parts[1]), int(parts[3])
    except (ValueError, IndexError):
        pass
    return 0, 0


def _make_cursor(scene_index: int, beat_index: int) -> str:
    return f"scene_{scene_index}_beat_{beat_index}"


# ---------------------------------------------------------------------------
# SceneRunner
# ---------------------------------------------------------------------------

class SceneRunner:
    """Orchestrates beat-by-beat execution of scenes in an adventure."""

    def __init__(
        self,
        adventure: "Adventure",
        dice: "DiceEngine",
        heuristics: "Heuristics",
        emitter: "Emitter",
        state_dir: Path,
    ) -> None:
        self._adventure = adventure
        self._dice = dice
        self._heuristics = heuristics
        self._emitter = emitter
        self._state_dir = state_dir

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def run_next_beat(
        self,
        party: "PartyState",
        session: "SessionState",
        campaign: "CampaignFacts",
        narrative_so_far: list[str] | None = None,
    ) -> RunResult:
        """Run the next beat and return a RunResult.

        Mutates session.pending_checkpoint to track progress.
        """
        if narrative_so_far is None:
            narrative_so_far = []

        scenes = self._adventure.scenes
        scene_index = session.scene_index

        # Determine beat_index from pending_checkpoint
        cursor_si, cursor_bi = _parse_cursor(session.pending_checkpoint)
        if cursor_si == scene_index:
            beat_index = cursor_bi
        else:
            # New scene — start at beat 0
            beat_index = 0

        # Bounds check: are we past all scenes?
        if scene_index >= len(scenes):
            session.pending_checkpoint = _make_cursor(scene_index, beat_index)
            return RunResult(
                status="session_complete",
                beat_type="scene_exit",
                dice_results=[],
                narrative_so_far=narrative_so_far,
                checkpoint_written=False,
            )

        scene = scenes[scene_index]
        beat_sequence = _beats_for_scene(scene)

        if beat_index >= len(beat_sequence):
            # Shouldn't happen under normal flow, but treat as scene exhausted
            beat_index = len(beat_sequence) - 1

        beat_type = beat_sequence[beat_index]
        cursor = _make_cursor(scene_index, beat_index)

        # Dispatch to the appropriate beat handler
        if beat_type == "read_aloud":
            return self._handle_read_aloud(
                scene, scene_index, beat_index, cursor,
                session, party, campaign, narrative_so_far,
            )
        elif beat_type == "encounter_dice":
            return self._handle_encounter_dice(
                scene, scene_index, beat_index, cursor,
                session, party, campaign, narrative_so_far,
            )
        elif beat_type == "scene_narration":
            return self._handle_scene_narration(
                scene, scene_index, beat_index, cursor,
                session, party, campaign, narrative_so_far,
            )
        elif beat_type == "scene_exit":
            return self._handle_scene_exit(
                scene, scene_index, beat_index, cursor,
                session, party, campaign, narrative_so_far,
            )
        else:
            raise RuntimeError(f"Unknown beat type: {beat_type!r}")

    # ------------------------------------------------------------------
    # Beat handlers
    # ------------------------------------------------------------------

    def _handle_read_aloud(
        self,
        scene: "Scene",
        scene_index: int,
        beat_index: int,
        cursor: str,
        session: "SessionState",
        party: "PartyState",
        campaign: "CampaignFacts",
        narrative_so_far: list[str],
    ) -> RunResult:
        """LLM-required: emit the scene read-aloud text for the DM to narrate."""
        session.pending_checkpoint = cursor

        packet = self._emitter.build_outbound(
            session=session.session,
            scene_id=scene_index,
            scene_name=scene.name,
            beat_type="read_aloud",
            state_snapshot=party.to_dict(),
            dice_results=[],
            resolved_mechanics={},
            decision_point={
                "type": "read_aloud",
                "description": (
                    f"Narrate the read-aloud text for scene '{scene.name}'. "
                    "Deliver it in the voice of the setting — do not embellish mechanics."
                ),
            },
            context={
                "read_aloud": scene.read_aloud,
                "scene_index": scene_index,
                "scene_name": scene.name,
            },
            scene_narrative_so_far=list(narrative_so_far),
        )
        self._emitter.write_checkpoint(packet)

        return RunResult(
            status="llm_required",
            beat_type="read_aloud",
            dice_results=[],
            narrative_so_far=list(narrative_so_far),
            checkpoint_written=True,
        )

    def _handle_encounter_dice(
        self,
        scene: "Scene",
        scene_index: int,
        beat_index: int,
        cursor: str,
        session: "SessionState",
        party: "PartyState",
        campaign: "CampaignFacts",
        narrative_so_far: list[str],
    ) -> RunResult:
        """Python-resolved: roll 1d20 initiative for each stat_block enemy."""
        dice_results = []
        dice_dicts = []
        for enemy in scene.stat_blocks:
            roll = self._dice.roll("1d20")
            dice_results.append(roll)
            dice_dicts.append({
                "enemy": enemy["name"],
                "ac": enemy["ac"],
                "hp": enemy["hp"],
                "initiative": roll.total,
                "rolls": roll.rolls,
                "total": roll.total,
                "expr": roll.expression,
                "label": f"{enemy['name']} initiative",
            })

        # Advance beat index
        next_beat_index = beat_index + 1
        session.pending_checkpoint = _make_cursor(scene_index, next_beat_index)

        return RunResult(
            status="python_resolved",
            beat_type="encounter_dice",
            dice_results=dice_results,
            narrative_so_far=list(narrative_so_far),
            checkpoint_written=False,
        )

    def _handle_scene_narration(
        self,
        scene: "Scene",
        scene_index: int,
        beat_index: int,
        cursor: str,
        session: "SessionState",
        party: "PartyState",
        campaign: "CampaignFacts",
        narrative_so_far: list[str],
    ) -> RunResult:
        """LLM-required: DM narrates the scene's main content."""
        session.pending_checkpoint = cursor

        packet = self._emitter.build_outbound(
            session=session.session,
            scene_id=scene_index,
            scene_name=scene.name,
            beat_type="scene_narration",
            state_snapshot=party.to_dict(),
            dice_results=[],
            resolved_mechanics={},
            decision_point={
                "type": "scene_narration",
                "description": (
                    f"Narrate scene '{scene.name}'. "
                    "Describe features, atmosphere, and any available player choices. "
                    "Do not resolve encounters — the DM will handle those at the table."
                ),
            },
            context={
                "read_aloud": "",   # read_aloud was already delivered
                "scene_index": scene_index,
                "scene_name": scene.name,
                "gm_notes": scene.gm_notes,
                "hints": campaign.hints,
            },
            scene_narrative_so_far=list(narrative_so_far),
        )
        self._emitter.write_checkpoint(packet)

        return RunResult(
            status="llm_required",
            beat_type="scene_narration",
            dice_results=[],
            narrative_so_far=list(narrative_so_far),
            checkpoint_written=True,
        )

    def _handle_scene_exit(
        self,
        scene: "Scene",
        scene_index: int,
        beat_index: int,
        cursor: str,
        session: "SessionState",
        party: "PartyState",
        campaign: "CampaignFacts",
        narrative_so_far: list[str],
    ) -> RunResult:
        """Python-resolved: mark scene complete and advance to the next scene."""
        session.advance_scene()
        # scene_index is now scene_index + 1 after advance_scene()
        new_scene_index = session.scene_index
        session.pending_checkpoint = _make_cursor(new_scene_index, 0)

        is_last = new_scene_index >= len(self._adventure.scenes)
        status = "session_complete" if is_last else "scene_complete"

        return RunResult(
            status=status,
            beat_type="scene_exit",
            dice_results=[],
            narrative_so_far=list(narrative_so_far),
            checkpoint_written=False,
        )
