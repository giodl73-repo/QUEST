from __future__ import annotations
import json
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class PCState:
    hp: int
    hp_max: int
    spell_slots: dict[str, int]
    attunements: list[str]
    lay_on_hands: int
    concentration: str | None
    conditions: list[str]


class PartyState:
    def __init__(self, pcs: dict[str, PCState]) -> None:
        self._pcs = pcs

    def __getitem__(self, slug: str) -> PCState:
        return self._pcs[slug]

    def __iter__(self):
        return iter(self._pcs)

    def slugs(self) -> list[str]:
        return list(self._pcs.keys())

    @classmethod
    def from_dict(cls, data: dict) -> "PartyState":
        pcs = {slug: PCState(**vals) for slug, vals in data.items()}
        return cls(pcs)

    def to_dict(self) -> dict:
        return {slug: asdict(pc) for slug, pc in self._pcs.items()}

    def apply_hp_delta(self, slug: str, delta: int) -> None:
        pc = self._pcs[slug]
        pc.hp = max(0, min(pc.hp_max, pc.hp + delta))

    def use_spell_slot(self, slug: str, level: str) -> None:
        pc = self._pcs[slug]
        if pc.spell_slots.get(level, 0) <= 0:
            raise ValueError(f"no {level} slots remaining for {slug}")
        pc.spell_slots[level] -= 1

    def any_below_half_hp(self) -> bool:
        return any(pc.hp < pc.hp_max * 0.5 for pc in self._pcs.values())


@dataclass
class SessionState:
    adventure: str
    session: str
    dice_seed: str
    scene_index: int
    scenes_completed: list[int]
    pending_checkpoint: str | None

    @classmethod
    def from_dict(cls, data: dict) -> "SessionState":
        return cls(**data)

    def to_dict(self) -> dict:
        return asdict(self)

    def advance_scene(self) -> None:
        self.scenes_completed.append(self.scene_index)
        self.scene_index += 1


@dataclass
class CampaignFacts:
    hints: dict[str, str]
    campaign_permanent: list[str]

    @classmethod
    def from_dict(cls, data: dict) -> "CampaignFacts":
        return cls(**data)

    def to_dict(self) -> dict:
        return asdict(self)


class StateManager:
    def __init__(self, state_dir: Path | None = None) -> None:
        self._dir = state_dir or Path("state")
        self._dir.mkdir(parents=True, exist_ok=True)

    @property
    def session_path(self) -> Path:
        return self._dir / "session.json"

    @property
    def checkpoint_path(self) -> Path:
        return self._dir / "checkpoint.json"

    def write_session(
        self,
        party: PartyState,
        session: SessionState,
        campaign: CampaignFacts,
    ) -> None:
        payload = {
            "party": party.to_dict(),
            "session": session.to_dict(),
            "campaign": campaign.to_dict(),
        }
        tmp = self.session_path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        tmp.replace(self.session_path)

    def read_session(self) -> dict | None:
        if not self.session_path.exists():
            return None
        try:
            data = json.loads(self.session_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            raise RuntimeError(
                f"Session state corrupted: {self.session_path}. "
                "Cannot recover automatically."
            )
        return {
            "party": PartyState.from_dict(data["party"]),
            "session": SessionState.from_dict(data["session"]),
            "campaign": CampaignFacts.from_dict(data["campaign"]),
        }

    def write_checkpoint(self, packet: dict) -> None:
        self.checkpoint_path.write_text(json.dumps(packet, indent=2), encoding="utf-8")

    def read_checkpoint(self) -> dict | None:
        if not self.checkpoint_path.exists():
            return None
        try:
            return json.loads(self.checkpoint_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return None  # treat corrupted checkpoint as absent; caller decides

    def delete_checkpoint(self) -> None:
        if self.checkpoint_path.exists():
            self.checkpoint_path.unlink()
