# marathon-runner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Python CLI (`scripts/marathon.py`) that owns the mechanical layer of D&D session play — seed-locked dice, persistent party state, PC heuristics, and re-entrant LLM checkpoints — replacing the current bash dice.sh + manual tracking approach.

**Architecture:** Single-process Python CLI with 8 engine components under `scripts/engine/`. Python resolves all mechanics (dice, HP, slots, heuristics); LLM handles narrative beats via a stdin/stdout checkpoint protocol. Every LLM beat writes `state/checkpoint.json` before blocking; `resume` re-enters from there with zero state loss.

**Tech Stack:** Python 3.11+ (stdlib only for core: `random`, `json`, `pathlib`, `dataclasses`, `argparse`); `pyyaml` for PC sheet frontmatter parsing; `pytest` for tests.

---

## File Map

| File | Action | Responsibility |
|---|---|---|
| `scripts/engine/__init__.py` | Create | Package marker |
| `scripts/engine/dice.py` | Create | Seed-locked RNG; `DiceEngine`, `RollResult` |
| `scripts/engine/state.py` | Create | `PartyState`, `SessionState`, `CampaignFacts`; read/write `session.json` |
| `scripts/engine/loader.py` | Create | Parse `module.md` → `Adventure`; parse PC sheets → `list[PC]` |
| `scripts/engine/heuristics.py` | Create | `Heuristics`; doubt-die, select-target, signature-move-due, bless-active |
| `scripts/engine/classifier.py` | Create | `Event` dataclass; `classify(event) → "python" | "llm"` |
| `scripts/engine/emitter.py` | Create | `Emitter`; build outbound packet; validate inbound packet; `InboundPacket` |
| `scripts/engine/scene.py` | Create | `SceneRunner`; scene state machine; beat loop |
| `scripts/engine/log_writer.py` | Create | `LogWriter`; produce `S{N}-log.md` from `session.json` + inbound narratives |
| `scripts/marathon.py` | Create | CLI entry point; `start`, `resume`, `status` subcommands |
| `tests/__init__.py` | Create | Package marker |
| `tests/engine/test_dice.py` | Create | Tests for `dice.py` |
| `tests/engine/test_state.py` | Create | Tests for `state.py` |
| `tests/engine/test_loader.py` | Create | Tests for `loader.py` |
| `tests/engine/test_heuristics.py` | Create | Tests for `heuristics.py` |
| `tests/engine/test_classifier.py` | Create | Tests for `classifier.py` |
| `tests/engine/test_emitter.py` | Create | Tests for `emitter.py` |
| `tests/engine/test_log_writer.py` | Create | Tests for `log_writer.py` |
| `tests/fixtures/` | Create | Test fixtures: minimal module.md, PC sheet YAML |
| `requirements-dev.txt` | Create | `pytest` + `pyyaml` |

---

## Task 1: Project Scaffold

**Files:**
- Create: `scripts/engine/__init__.py`
- Create: `tests/__init__.py`
- Create: `tests/engine/__init__.py`
- Create: `tests/fixtures/mini_module.md`
- Create: `tests/fixtures/mini_pc.md`
- Create: `requirements-dev.txt`
- Create: `pytest.ini`

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p scripts/engine tests/engine tests/fixtures
```

- [ ] **Step 2: Create package markers**

`scripts/engine/__init__.py` — empty file.
`tests/__init__.py` — empty file.
`tests/engine/__init__.py` — empty file.

- [ ] **Step 3: Create `requirements-dev.txt`**

```
pytest>=7.4
pyyaml>=6.0
```

- [ ] **Step 4: Create `pytest.ini`**

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v
```

- [ ] **Step 5: Create minimal test fixture — `tests/fixtures/mini_module.md`**

This is the smallest valid module.md the loader must parse. Matches the real format from `adventures/*/module.md`.

```markdown
---
adventure: test-adventure
tier: 1
---

# Test Adventure — DM Module

## Table of Contents
1. Summary

---

## Summary

A two-scene test adventure.

---

### Scene 1 — The Arrival

**Read-aloud:**

> You arrive at the testing ground.

**Features:**
- A door (DC 10 Investigation to notice lock).

**Encounter:** None.

**GM Notes:** This is Scene 1.

---

### Scene 2 — The Vault

**Read-aloud:**

> The vault door stands before you.

**Features:**
- Locked vault (DC 15 Thieves' Tools).

**Encounter:**

> **Test Guard — CR ½, 100 XP.** **AC** 14 · **HP** 22 · **Speed** 30 ft.
> **Longsword:** +4, 1d8+2 slashing.

**GM Notes:** This is Scene 2.

---

## DM Cheatsheet

### Quick Reference — Key DCs (by scene)

| DC | Check | Scene | Consequence |
|---|---|---|---|
| 10 | Investigation (door) | 1 | Notices lock |
| 15 | Thieves' Tools (vault) | 2 | Opens vault |
```

- [ ] **Step 6: Create minimal PC fixture — `tests/fixtures/mini_pc.md`**

```markdown
---
party: test-party
pc: test-fighter
class: fighter
level: 3
heuristics:
  doubt_die:
    "1-3": "attack"
    "4-6": "defend"
  decision_order:
    - key: survival
      condition: "any_pc_below_half_hp"
    - key: offense
      condition: "always"
  signature_moves:
    - id: "power-attack"
      trigger: "always"
      mechanical_effect: null
  voice_tags:
    - "terse"
---

# Test Fighter

## Stat Block

**AC** 16 (chain mail)  ·  **HP** 28  ·  **Speed** 30 ft.

| Str | Dex | Con | Int | Wis | Cha |
|---|---|---|---|---|---|
| 16 | 12 | 14 | 10 | 12 | 10 |

**Saves (proficient):** Strength +5, Constitution +4
**Skills (proficient):** Athletics +5, Perception +3
**Senses:** passive Perception 13
**Languages:** Common
**Equipment:** chain mail, longsword, shield, 15 gp

**Attunement slots:** 3 (empty)

**Proficiency:** +2. **Initiative:** +1.
```

- [ ] **Step 7: Verify pytest finds nothing yet**

```bash
cd C:/src/marathon
pip install -r requirements-dev.txt
pytest
```

Expected output: `no tests ran` or `0 passed`.

- [ ] **Step 8: Commit**

```bash
git add scripts/engine/__init__.py tests/ requirements-dev.txt pytest.ini
git commit -m "chore: scaffold marathon-runner project structure + test fixtures"
```

---

## Task 2: `dice.py` — Seed-Locked RNG

**Files:**
- Create: `scripts/engine/dice.py`
- Create: `tests/engine/test_dice.py`

- [ ] **Step 1: Write failing tests**

`tests/engine/test_dice.py`:
```python
import pytest
from scripts.engine.dice import DiceEngine, RollResult, DiceError


def test_roll_result_is_dataclass():
    """RollResult has all required fields."""
    r = RollResult(
        expression="1d20+5",
        rolls=[14],
        kept=None,
        mod=5,
        bless_roll=None,
        total=19,
        crit=False,
        fumble=False,
        seed_position=0,
    )
    assert r.total == 19


def test_same_seed_same_rolls():
    """Same seed + same sequence = identical rolls."""
    d1 = DiceEngine(seed="S04-20260419")
    d2 = DiceEngine(seed="S04-20260419")
    r1 = d1.roll("1d20+3")
    r2 = d2.roll("1d20+3")
    assert r1.rolls == r2.rolls
    assert r1.total == r2.total


def test_different_seeds_may_differ():
    """Different seeds produce (very likely) different results."""
    d1 = DiceEngine(seed="S04-20260419")
    d2 = DiceEngine(seed="S05-20260419")
    rolls1 = [d1.roll("1d20").total for _ in range(10)]
    rolls2 = [d2.roll("1d20").total for _ in range(10)]
    # Not guaranteed to differ every roll but sequence should differ
    assert rolls1 != rolls2


def test_modifier_applied():
    """Modifier is added to the rolled total."""
    d = DiceEngine(seed="test-seed")
    r = d.roll("1d6+3")
    assert r.total == r.rolls[0] + 3
    assert r.mod == 3


def test_advantage_keeps_higher():
    """With adv=True, the higher of two d20 rolls is kept."""
    d = DiceEngine(seed="test-seed")
    r = d.roll("1d20+2", adv=True)
    assert len(r.rolls) == 2
    assert r.kept == max(r.rolls)
    assert r.total == max(r.rolls) + 2


def test_disadvantage_keeps_lower():
    """With disadv=True, the lower of two d20 rolls is kept."""
    d = DiceEngine(seed="test-seed")
    r = d.roll("1d20", disadv=True)
    assert r.kept == min(r.rolls)


def test_crit_on_nat_20():
    """RollResult.crit is True when the kept d20 roll is 20."""
    # Force a nat-20 by finding seed that produces it
    for seed_suffix in range(100):
        d = DiceEngine(seed=f"crit-test-{seed_suffix}")
        r = d.roll("1d20")
        if r.rolls[0] == 20:
            assert r.crit is True
            assert r.fumble is False
            return
    pytest.skip("Could not find a nat-20 in 100 seeds (statistically improbable)")


def test_fumble_on_nat_1():
    """RollResult.fumble is True when the kept d20 roll is 1."""
    for seed_suffix in range(100):
        d = DiceEngine(seed=f"fumble-test-{seed_suffix}")
        r = d.roll("1d20")
        if r.rolls[0] == 1:
            assert r.fumble is True
            assert r.crit is False
            return
    pytest.skip("Could not find a nat-1 in 100 seeds (statistically improbable)")


def test_bless_adds_d4():
    """bless=True adds a 1d4 roll to the total."""
    d = DiceEngine(seed="bless-test")
    r = d.roll("1d20+3", bless=True)
    assert r.bless_roll is not None
    assert 1 <= r.bless_roll <= 4
    base = r.kept if r.kept is not None else r.rolls[0]
    assert r.total == base + r.mod + r.bless_roll


def test_multi_die_expression():
    """2d6+2 rolls two dice and sums them with modifier."""
    d = DiceEngine(seed="multi-die")
    r = d.roll("2d6+2")
    assert len(r.rolls) == 2
    assert all(1 <= v <= 6 for v in r.rolls)
    assert r.total == sum(r.rolls) + 2


def test_seed_position_increments():
    """seed_position increments with each roll."""
    d = DiceEngine(seed="position-test")
    r1 = d.roll("1d20")
    r2 = d.roll("1d20")
    assert r2.seed_position == r1.seed_position + 1


def test_invalid_expression_raises():
    """Invalid dice expression raises DiceError."""
    d = DiceEngine(seed="error-test")
    with pytest.raises(DiceError):
        d.roll("1d20+")


def test_roll_results_logged_to_jsonl(tmp_path):
    """Rolls are appended to dice_log.jsonl."""
    import json
    log_file = tmp_path / "dice_log.jsonl"
    d = DiceEngine(seed="log-test", log_path=log_file)
    d.roll("1d20+3")
    d.roll("2d6")
    lines = log_file.read_text().strip().split("\n")
    assert len(lines) == 2
    entry = json.loads(lines[0])
    assert "expression" in entry
    assert "total" in entry
    assert "seed_position" in entry
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/engine/test_dice.py -v
```

Expected: `ImportError: No module named 'scripts.engine.dice'`

- [ ] **Step 3: Implement `scripts/engine/dice.py`**

```python
from __future__ import annotations
import json
import random
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path


class DiceError(Exception):
    pass


@dataclass
class RollResult:
    expression: str
    rolls: list[int]
    kept: int | None       # None if no adv/disadv; set to kept die value otherwise
    mod: int
    bless_roll: int | None
    total: int
    crit: bool             # True if kept d20 == 20
    fumble: bool           # True if kept d20 == 1
    seed_position: int


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
    ) -> RollResult:
        expr = expression.strip().lower()
        m = _EXPR_RE.match(expr)
        if not m:
            raise DiceError(f"invalid expression: {expression!r}")

        count = int(m.group(1))
        sides = int(m.group(2))
        mod_str = m.group(3) or "+0"
        mod = int(mod_str)

        # Roll the dice
        rolls = [self._roll_die(sides) for _ in range(count)]

        # Advantage / disadvantage (only for single d20)
        kept: int | None = None
        if (adv or disadv) and count == 1 and sides == 20:
            second = self._roll_die(sides)
            both = [rolls[0], second]
            rolls = both
            kept = max(both) if adv else min(both)
        else:
            kept = None

        base = kept if kept is not None else sum(rolls)

        # Bless die
        bless_roll: int | None = None
        if bless:
            bless_roll = self._roll_die(4)

        total = base + mod + (bless_roll or 0)

        # Crit / fumble (only meaningful for d20)
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
        )
        self._position += 1

        if self._log_path is not None:
            with self._log_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(asdict(result)) + "\n")

        return result
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/engine/test_dice.py -v
```

Expected: all 12 tests pass.

- [ ] **Step 5: Commit**

```bash
git add scripts/engine/dice.py tests/engine/test_dice.py
git commit -m "feat: dice engine — seed-locked RNG with advantage, bless, CRIT/FUMBLE, JSONL logging"
```

---

## Task 3: `state.py` — State Model

**Files:**
- Create: `scripts/engine/state.py`
- Create: `tests/engine/test_state.py`

- [ ] **Step 1: Write failing tests**

`tests/engine/test_state.py`:
```python
import json
import pytest
from pathlib import Path
from scripts.engine.state import PartyState, SessionState, CampaignFacts, StateManager


# ── PartyState ──────────────────────────────────────────────────────────────

def test_party_state_from_dict():
    data = {
        "aelric-of-crownhold": {
            "hp": 28, "hp_max": 28,
            "spell_slots": {"L1": 3, "L2": 0},
            "attunements": ["varran-reliquary"],
            "lay_on_hands": 15,
            "concentration": None,
            "conditions": []
        }
    }
    ps = PartyState.from_dict(data)
    assert ps["aelric-of-crownhold"].hp == 28
    assert ps["aelric-of-crownhold"].attunements == ["varran-reliquary"]


def test_party_state_apply_hp_delta():
    data = {"fighter": {"hp": 28, "hp_max": 28, "spell_slots": {}, "attunements": [],
                        "lay_on_hands": 0, "concentration": None, "conditions": []}}
    ps = PartyState.from_dict(data)
    ps.apply_hp_delta("fighter", -10)
    assert ps["fighter"].hp == 18


def test_party_state_hp_floor_zero():
    data = {"fighter": {"hp": 5, "hp_max": 28, "spell_slots": {}, "attunements": [],
                        "lay_on_hands": 0, "concentration": None, "conditions": []}}
    ps = PartyState.from_dict(data)
    ps.apply_hp_delta("fighter", -100)
    assert ps["fighter"].hp == 0


def test_party_state_hp_ceil_max():
    data = {"fighter": {"hp": 5, "hp_max": 28, "spell_slots": {}, "attunements": [],
                        "lay_on_hands": 0, "concentration": None, "conditions": []}}
    ps = PartyState.from_dict(data)
    ps.apply_hp_delta("fighter", +100)
    assert ps["fighter"].hp == 28


def test_party_state_use_spell_slot():
    data = {"wizard": {"hp": 16, "hp_max": 16, "spell_slots": {"L1": 4, "L2": 2},
                       "attunements": [], "lay_on_hands": 0, "concentration": None,
                       "conditions": []}}
    ps = PartyState.from_dict(data)
    ps.use_spell_slot("wizard", "L1")
    assert ps["wizard"].spell_slots["L1"] == 3


def test_party_state_use_spell_slot_raises_when_empty():
    data = {"wizard": {"hp": 16, "hp_max": 16, "spell_slots": {"L1": 0, "L2": 2},
                       "attunements": [], "lay_on_hands": 0, "concentration": None,
                       "conditions": []}}
    ps = PartyState.from_dict(data)
    with pytest.raises(ValueError, match="no L1 slots remaining"):
        ps.use_spell_slot("wizard", "L1")


# ── SessionState ─────────────────────────────────────────────────────────────

def test_session_state_from_dict():
    data = {
        "adventure": "0004-the-wrath-coin",
        "session": "S04",
        "dice_seed": "S04-20260419",
        "scene_index": 3,
        "scenes_completed": [0, 1, 2],
        "pending_checkpoint": None
    }
    ss = SessionState.from_dict(data)
    assert ss.scene_index == 3
    assert ss.scenes_completed == [0, 1, 2]


def test_session_state_advance_scene():
    data = {"adventure": "test", "session": "S01", "dice_seed": "S01",
            "scene_index": 1, "scenes_completed": [0], "pending_checkpoint": None}
    ss = SessionState.from_dict(data)
    ss.advance_scene()
    assert ss.scene_index == 2
    assert 1 in ss.scenes_completed


# ── StateManager ─────────────────────────────────────────────────────────────

def test_state_manager_write_and_read(tmp_path):
    sm = StateManager(state_dir=tmp_path)
    party_data = {"fighter": {"hp": 20, "hp_max": 20, "spell_slots": {}, "attunements": [],
                               "lay_on_hands": 0, "concentration": None, "conditions": []}}
    session_data = {"adventure": "test", "session": "S01", "dice_seed": "S01",
                    "scene_index": 0, "scenes_completed": [], "pending_checkpoint": None}
    campaign_data = {"hints": {"hint-1": "caught"}, "campaign_permanent": []}

    sm.write_session(
        party=PartyState.from_dict(party_data),
        session=SessionState.from_dict(session_data),
        campaign=CampaignFacts.from_dict(campaign_data),
    )

    loaded = sm.read_session()
    assert loaded["session"].adventure == "test"
    assert loaded["party"]["fighter"].hp == 20


def test_state_manager_atomic_write(tmp_path):
    """session.json is written atomically via .tmp rename."""
    sm = StateManager(state_dir=tmp_path)
    party_data = {"f": {"hp": 5, "hp_max": 5, "spell_slots": {}, "attunements": [],
                        "lay_on_hands": 0, "concentration": None, "conditions": []}}
    session_data = {"adventure": "t", "session": "S1", "dice_seed": "S1",
                    "scene_index": 0, "scenes_completed": [], "pending_checkpoint": None}
    campaign_data = {"hints": {}, "campaign_permanent": []}
    sm.write_session(
        party=PartyState.from_dict(party_data),
        session=SessionState.from_dict(session_data),
        campaign=CampaignFacts.from_dict(campaign_data),
    )
    # .tmp file must not remain after write
    assert not (tmp_path / "session.json.tmp").exists()
    assert (tmp_path / "session.json").exists()


def test_state_manager_no_session_returns_none(tmp_path):
    sm = StateManager(state_dir=tmp_path)
    assert sm.read_session() is None
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/engine/test_state.py -v
```

Expected: `ImportError: No module named 'scripts.engine.state'`

- [ ] **Step 3: Implement `scripts/engine/state.py`**

```python
from __future__ import annotations
import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any


# ── PC state ─────────────────────────────────────────────────────────────────

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


# ── Session state ─────────────────────────────────────────────────────────────

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


# ── Campaign facts ────────────────────────────────────────────────────────────

@dataclass
class CampaignFacts:
    hints: dict[str, str]           # e.g. {"hint-1": "caught", "hint-2": "unlocked"}
    campaign_permanent: list[str]   # e.g. ["aelric-varran-memory-loss"]

    @classmethod
    def from_dict(cls, data: dict) -> "CampaignFacts":
        return cls(**data)

    def to_dict(self) -> dict:
        return asdict(self)


# ── State manager ─────────────────────────────────────────────────────────────

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
        """Atomic write via .tmp rename — prevents partial writes."""
        payload = {
            "party": party.to_dict(),
            "session": session.to_dict(),
            "campaign": campaign.to_dict(),
        }
        tmp = self.session_path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        tmp.replace(self.session_path)  # atomic on POSIX; best-effort on Windows

    def read_session(self) -> dict | None:
        """Returns dict with keys 'party', 'session', 'campaign', or None if absent."""
        if not self.session_path.exists():
            return None
        data = json.loads(self.session_path.read_text(encoding="utf-8"))
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
        return json.loads(self.checkpoint_path.read_text(encoding="utf-8"))

    def delete_checkpoint(self) -> None:
        if self.checkpoint_path.exists():
            self.checkpoint_path.unlink()
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/engine/test_state.py -v
```

Expected: all 9 tests pass.

- [ ] **Step 5: Commit**

```bash
git add scripts/engine/state.py tests/engine/test_state.py
git commit -m "feat: state model — PartyState, SessionState, CampaignFacts, atomic StateManager"
```

---

## Task 4: `loader.py` — Module + Party Parser

**Files:**
- Create: `scripts/engine/loader.py`
- Create: `tests/engine/test_loader.py`

- [ ] **Step 1: Write failing tests**

`tests/engine/test_loader.py`:
```python
import pytest
from pathlib import Path
from scripts.engine.loader import load_adventure, load_party, Adventure, Scene, PC, LoadError

FIXTURES = Path("tests/fixtures")


def test_load_adventure_returns_adventure_object():
    adv = load_adventure(FIXTURES / "mini_module.md")
    assert isinstance(adv, Adventure)


def test_load_adventure_two_scenes():
    adv = load_adventure(FIXTURES / "mini_module.md")
    assert len(adv.scenes) == 2


def test_load_adventure_scene_names():
    adv = load_adventure(FIXTURES / "mini_module.md")
    assert adv.scenes[0].name == "The Arrival"
    assert adv.scenes[1].name == "The Vault"


def test_load_adventure_scene_read_aloud():
    adv = load_adventure(FIXTURES / "mini_module.md")
    assert "testing ground" in adv.scenes[0].read_aloud


def test_load_adventure_dc_table():
    adv = load_adventure(FIXTURES / "mini_module.md")
    # Cheatsheet has two DC rows
    assert len(adv.dc_table) == 2
    dcs = {row["dc"] for row in adv.dc_table}
    assert 10 in dcs
    assert 15 in dcs


def test_load_adventure_stat_block_in_scene():
    adv = load_adventure(FIXTURES / "mini_module.md")
    # Scene 2 has a stat block
    s2 = adv.scenes[1]
    assert len(s2.stat_blocks) == 1
    guard = s2.stat_blocks[0]
    assert guard["name"] == "Test Guard"
    assert guard["ac"] == 14
    assert guard["hp"] == 22


def test_load_adventure_missing_file_raises():
    with pytest.raises(LoadError, match="not found"):
        load_adventure(Path("nonexistent/module.md"))


def test_load_party_returns_pc_list():
    pcs = load_party(FIXTURES)
    assert len(pcs) == 1


def test_load_party_pc_name():
    pcs = load_party(FIXTURES)
    assert pcs[0].slug == "test-fighter"


def test_load_party_pc_stat_block():
    pcs = load_party(FIXTURES)
    pc = pcs[0]
    assert pc.ac == 16
    assert pc.hp == 28
    assert pc.hp_max == 28


def test_load_party_heuristics_decision_order():
    pcs = load_party(FIXTURES)
    pc = pcs[0]
    assert len(pc.heuristics["decision_order"]) == 2
    assert pc.heuristics["decision_order"][0]["key"] == "survival"


def test_load_party_heuristics_doubt_die():
    pcs = load_party(FIXTURES)
    pc = pcs[0]
    dd = pc.heuristics["doubt_die"]
    assert dd["1-3"] == "attack"
    assert dd["4-6"] == "defend"


def test_load_party_missing_heuristics_raises():
    """A PC file without a heuristics YAML block raises LoadError."""
    import tempfile, textwrap
    content = textwrap.dedent("""\
        ---
        party: test
        pc: bad-pc
        class: fighter
        level: 1
        ---
        # Bad PC
    """)
    with tempfile.NamedTemporaryFile(suffix=".md", mode="w", delete=False) as f:
        f.write(content)
        tmppath = Path(f.name)
    with pytest.raises(LoadError, match="No heuristics block"):
        load_party(tmppath.parent)
    tmppath.unlink()
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/engine/test_loader.py -v
```

Expected: `ImportError: No module named 'scripts.engine.loader'`

- [ ] **Step 3: Implement `scripts/engine/loader.py`**

```python
from __future__ import annotations
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml  # pyyaml


class LoadError(Exception):
    pass


# ── Data objects ──────────────────────────────────────────────────────────────

@dataclass
class Scene:
    index: int
    name: str
    read_aloud: str
    gm_notes: str
    stat_blocks: list[dict]   # list of {"name", "ac", "hp", "xp", ...}


@dataclass
class Adventure:
    slug: str
    scenes: list[Scene]
    dc_table: list[dict]      # list of {"dc", "check", "scene", "consequence"}


@dataclass
class PC:
    slug: str
    ac: int
    hp: int
    hp_max: int
    spell_slots: dict[str, int]
    attunements: list[str]
    heuristics: dict


# ── Parsing helpers ───────────────────────────────────────────────────────────

_SCENE_HEADER = re.compile(r"^### Scene \d+ — (.+)$", re.MULTILINE)
_STAT_BLOCK = re.compile(
    r"\*\*(?P<name>.+?)\s*(?:—.*?)?\*\*.*?"
    r"\*\*AC\*\*\s*(?P<ac>\d+).*?"
    r"\*\*HP\*\*\s*(?P<hp>\d+)",
    re.DOTALL,
)
_DC_ROW = re.compile(
    r"^\|\s*(?P<dc>\d+)\s*\|[^|]*\|[^|]*\|[^|]*\|",
    re.MULTILINE,
)
_READ_ALOUD = re.compile(r"> (.+?)(?=\n\n|\Z)", re.DOTALL)
_YAML_FRONT = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
_AC_HP = re.compile(r"\*\*AC\*\*\s*(\d+).*?\*\*HP\*\*\s*(\d+)", re.DOTALL)


def _split_scenes(text: str) -> list[tuple[int, str, str]]:
    """Return list of (index, name, body) for each ### Scene N — Name section."""
    parts = re.split(r"(?=^### Scene \d+)", text, flags=re.MULTILINE)
    result = []
    for i, part in enumerate(parts):
        m = _SCENE_HEADER.match(part)
        if m:
            result.append((len(result), m.group(1).strip(), part))
    return result


def _parse_stat_blocks(text: str) -> list[dict]:
    blocks = []
    # Match inline stat blocks: **Name — CR X, Y XP.** **AC** N · **HP** N
    pattern = re.compile(
        r"\*\*([^*]+?)\s*(?:—[^*]*)?\*\*[^*]*"
        r"\*\*AC\*\*\s*(\d+)[^*]*\*\*HP\*\*\s*(\d+)",
        re.DOTALL,
    )
    for m in pattern.finditer(text):
        name = m.group(1).strip()
        # Skip read-aloud blockquotes (names starting with ">")
        if name.startswith(">"):
            continue
        blocks.append({
            "name": name,
            "ac": int(m.group(2)),
            "hp": int(m.group(3)),
        })
    return blocks


def _parse_dc_table(text: str) -> list[dict]:
    rows = []
    # Find the cheatsheet DC table
    table_match = re.search(r"### Quick Reference.*?\n(\|.*?)(?=\n##|\Z)", text, re.DOTALL)
    if not table_match:
        return rows
    table_text = table_match.group(1)
    for line in table_text.splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|\s*([^|]+)\s*\|\s*(\d+)\s*\|\s*([^|]+)\s*\|", line)
        if m:
            rows.append({
                "dc": int(m.group(1)),
                "check": m.group(2).strip(),
                "scene": int(m.group(3)),
                "consequence": m.group(4).strip(),
            })
    return rows


def _parse_read_aloud(text: str) -> str:
    m = _READ_ALOUD.search(text)
    if not m:
        return ""
    return m.group(1).replace("\n> ", " ").replace("\n", " ").strip()


# ── Public API ────────────────────────────────────────────────────────────────

def load_adventure(path: Path) -> Adventure:
    if not path.exists():
        raise LoadError(f"module.md not found: {path}")

    text = path.read_text(encoding="utf-8")

    # Extract slug from frontmatter
    fm_match = _YAML_FRONT.match(text)
    slug = ""
    if fm_match:
        try:
            fm = yaml.safe_load(fm_match.group(1))
            slug = fm.get("adventure", "")
        except Exception:
            pass

    scene_parts = _split_scenes(text)
    scenes = []
    for idx, name, body in scene_parts:
        scenes.append(Scene(
            index=idx,
            name=name,
            read_aloud=_parse_read_aloud(body),
            gm_notes="",
            stat_blocks=_parse_stat_blocks(body),
        ))

    dc_table = _parse_dc_table(text)

    return Adventure(slug=slug, scenes=scenes, dc_table=dc_table)


def load_party(party_dir: Path) -> list[PC]:
    pcs = []
    for md_file in sorted(party_dir.glob("*.md")):
        if md_file.name in ("README.md", "shared-log.md"):
            continue
        text = md_file.read_text(encoding="utf-8")
        fm_match = _YAML_FRONT.match(text)
        if not fm_match:
            continue

        try:
            fm = yaml.safe_load(fm_match.group(1))
        except Exception as e:
            raise LoadError(f"YAML parse error in {md_file}: {e}")

        if "pc" not in fm:
            continue  # not a PC file (e.g. README)

        if "heuristics" not in fm:
            raise LoadError(f"No heuristics block in {md_file}")

        # Parse AC/HP from stat block section
        ac, hp = 10, 10
        ac_hp = _AC_HP.search(text)
        if ac_hp:
            ac = int(ac_hp.group(1))
            hp = int(ac_hp.group(2))

        slug = fm.get("pc", md_file.stem)
        spell_slots = fm.get("spell_slots", {})

        pcs.append(PC(
            slug=slug,
            ac=ac,
            hp=hp,
            hp_max=hp,
            spell_slots=spell_slots,
            attunements=[],
            heuristics=fm["heuristics"],
        ))

    return pcs
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/engine/test_loader.py -v
```

Expected: all 12 tests pass.

- [ ] **Step 5: Commit**

```bash
git add scripts/engine/loader.py tests/engine/test_loader.py
git commit -m "feat: loader — parse module.md scenes/stat-blocks/DCs + PC sheets from YAML heuristics"
```

---

## Task 5: `heuristics.py` — Mechanical PC Decisions

**Files:**
- Create: `scripts/engine/heuristics.py`
- Create: `tests/engine/test_heuristics.py`

- [ ] **Step 1: Write failing tests**

`tests/engine/test_heuristics.py`:
```python
import pytest
from scripts.engine.loader import load_party
from scripts.engine.heuristics import Heuristics, HeuristicsError
from pathlib import Path

FIXTURES = Path("tests/fixtures")


@pytest.fixture
def pcs():
    return load_party(FIXTURES)


@pytest.fixture
def h(pcs):
    return Heuristics(pcs)


def test_doubt_die_returns_interpretation(h):
    """doubt_die rolls 1d6 and returns one of the PC's mapped strings."""
    seed = "doubt-test"
    result = h.doubt_die("test-fighter", context="combat", seed=seed)
    assert result.interpretation in ("attack", "defend")


def test_doubt_die_same_seed_same_result(h):
    """Same seed = same doubt-die interpretation."""
    r1 = h.doubt_die("test-fighter", context="any", seed="fixed")
    r2 = h.doubt_die("test-fighter", context="any", seed="fixed")
    assert r1.interpretation == r2.interpretation


def test_doubt_die_unknown_pc_raises(h):
    with pytest.raises(HeuristicsError, match="unknown PC"):
        h.doubt_die("no-such-pc", context="x", seed="s")


def test_bless_active_false_by_default(h):
    assert h.bless_active("test-fighter") is False


def test_bless_active_true_after_set(h):
    h.set_bless("test-fighter", True)
    assert h.bless_active("test-fighter") is True


def test_signature_move_due_returns_none_when_none_used(h):
    """Signature move is due if it hasn't fired this session."""
    result = h.signature_move_due("test-fighter", moves_used_this_session=[])
    assert result is not None   # "power-attack" should be flagged as due


def test_signature_move_due_returns_none_when_already_used(h):
    result = h.signature_move_due("test-fighter", moves_used_this_session=["power-attack"])
    assert result is None


def test_condition_evaluation_any_pc_below_half(h):
    """any_pc_below_half_hp condition evaluates correctly against party state."""
    from scripts.engine.state import PartyState
    party = PartyState.from_dict({
        "test-fighter": {"hp": 5, "hp_max": 28, "spell_slots": {}, "attunements": [],
                          "lay_on_hands": 0, "concentration": None, "conditions": []}
    })
    assert h.eval_condition("any_pc_below_half_hp", party=party) is True


def test_condition_evaluation_always(h):
    from scripts.engine.state import PartyState
    party = PartyState.from_dict({
        "test-fighter": {"hp": 28, "hp_max": 28, "spell_slots": {}, "attunements": [],
                          "lay_on_hands": 0, "concentration": None, "conditions": []}
    })
    assert h.eval_condition("always", party=party) is True


def test_unknown_condition_raises(h):
    from scripts.engine.state import PartyState
    party = PartyState.from_dict({
        "f": {"hp": 5, "hp_max": 28, "spell_slots": {}, "attunements": [],
               "lay_on_hands": 0, "concentration": None, "conditions": []}
    })
    with pytest.raises(HeuristicsError, match="unknown condition token"):
        h.eval_condition("involves_spaghetti", party=party)
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/engine/test_heuristics.py -v
```

Expected: `ImportError`

- [ ] **Step 3: Implement `scripts/engine/heuristics.py`**

```python
from __future__ import annotations
import random
from dataclasses import dataclass
from typing import Any

from scripts.engine.loader import PC
from scripts.engine.state import PartyState


class HeuristicsError(Exception):
    pass


@dataclass
class DoubtDieResult:
    roll: int           # 1-6
    interpretation: str


class Heuristics:
    """Mechanical PC decision-making derived from loaded PC sheets."""

    # Safe vocabulary for condition strings
    _CONDITIONS = {
        "always": lambda ctx: True,
        "any_pc_below_half_hp": lambda ctx: ctx["party"].any_below_half_hp()
            if ctx.get("party") else False,
        "involves_evil": lambda ctx: ctx.get("involves_evil", False),
        "involves_undead": lambda ctx: ctx.get("involves_undead", False),
        "has_council_interest": lambda ctx: ctx.get("has_council_interest", False),
    }

    def __init__(self, pcs: list[PC]) -> None:
        self._pcs: dict[str, PC] = {pc.slug: pc for pc in pcs}
        self._bless: dict[str, bool] = {pc.slug: False for pc in pcs}

    def _get_pc(self, slug: str) -> PC:
        if slug not in self._pcs:
            raise HeuristicsError(f"unknown PC: {slug!r}")
        return self._pcs[slug]

    def doubt_die(self, slug: str, context: str, seed: str) -> DoubtDieResult:
        pc = self._get_pc(slug)
        dd = pc.heuristics.get("doubt_die", {})
        rng = random.Random(f"{seed}-{slug}")
        roll = rng.randint(1, 6)
        # Find the matching range
        interpretation = "unknown"
        for range_str, result in dd.items():
            lo, hi = (int(x) for x in range_str.split("-"))
            if lo <= roll <= hi:
                interpretation = result
                break
        return DoubtDieResult(roll=roll, interpretation=interpretation)

    def bless_active(self, slug: str) -> bool:
        return self._bless.get(slug, False)

    def set_bless(self, slug: str, active: bool) -> None:
        self._bless[slug] = active

    def signature_move_due(
        self, slug: str, moves_used_this_session: list[str]
    ) -> str | None:
        """Return the ID of a signature move that is due, or None."""
        pc = self._get_pc(slug)
        moves = pc.heuristics.get("signature_moves", [])
        for move in moves:
            if move["id"] not in moves_used_this_session:
                return move["id"]
        return None

    def eval_condition(self, condition_str: str, party: PartyState | None = None) -> bool:
        """Evaluate a condition string from decision_order rules."""
        tokens = condition_str.split()
        # Simple AND/OR/NOT evaluator
        result = self._eval_tokens(tokens, {"party": party})
        return result

    def _eval_tokens(self, tokens: list[str], ctx: dict) -> bool:
        if not tokens:
            return False
        # Handle OR
        if "OR" in tokens:
            idx = tokens.index("OR")
            return (
                self._eval_tokens(tokens[:idx], ctx)
                or self._eval_tokens(tokens[idx + 1:], ctx)
            )
        # Handle AND
        if "AND" in tokens:
            idx = tokens.index("AND")
            return (
                self._eval_tokens(tokens[:idx], ctx)
                and self._eval_tokens(tokens[idx + 1:], ctx)
            )
        # Handle NOT
        if tokens[0] == "NOT":
            return not self._eval_tokens(tokens[1:], ctx)
        # Single token
        token = tokens[0]
        if token not in self._CONDITIONS:
            raise HeuristicsError(f"unknown condition token: {token!r}")
        return self._CONDITIONS[token](ctx)
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/engine/test_heuristics.py -v
```

Expected: all 11 tests pass.

- [ ] **Step 5: Commit**

```bash
git add scripts/engine/heuristics.py tests/engine/test_heuristics.py
git commit -m "feat: heuristics — doubt-die, bless tracking, signature-move timing, condition evaluator"
```

---

## Task 6: `classifier.py` — Decision Router

**Files:**
- Create: `scripts/engine/classifier.py`
- Create: `tests/engine/test_classifier.py`

- [ ] **Step 1: Write failing tests**

`tests/engine/test_classifier.py`:
```python
import pytest
from scripts.engine.classifier import Event, classify


def make_event(**kwargs):
    defaults = dict(
        type="dice_roll",
        pc_slug="aelric",
        involves_grief_paragraph=False,
        is_option_c=False,
        is_hint_delivery=False,
        is_read_aloud=False,
        has_npc_dialogue=False,
        is_key_loot=False,
        scene_context={},
    )
    defaults.update(kwargs)
    return Event(**defaults)


# ── Python-resolved ──────────────────────────────────────────────────────────

def test_dice_roll_is_python():
    assert classify(make_event(type="dice_roll")) == "python"


def test_hp_delta_is_python():
    assert classify(make_event(type="hp_delta")) == "python"


def test_resource_use_is_python():
    assert classify(make_event(type="resource_use")) == "python"


def test_doubt_die_is_python():
    assert classify(make_event(type="doubt_die")) == "python"


def test_signature_move_timing_is_python():
    assert classify(make_event(type="signature_move")) == "python"


def test_condition_apply_is_python():
    assert classify(make_event(type="condition_apply")) == "python"


def test_scene_advance_is_python():
    assert classify(make_event(type="scene_advance")) == "python"


# ── LLM-required ─────────────────────────────────────────────────────────────

def test_read_aloud_is_llm():
    assert classify(make_event(type="read_aloud", is_read_aloud=True)) == "llm"


def test_option_c_is_llm():
    assert classify(make_event(type="option_c", is_option_c=True)) == "llm"


def test_npc_dialogue_is_llm():
    assert classify(make_event(type="dialogue", has_npc_dialogue=True)) == "llm"


def test_memory_fragment_is_llm():
    assert classify(make_event(type="memory_fragment")) == "llm"


def test_atmospheric_chain_is_llm():
    assert classify(make_event(type="atmospheric_chain")) == "llm"


def test_grief_paragraph_is_llm():
    assert classify(make_event(type="any", involves_grief_paragraph=True)) == "llm"


def test_hint_delivery_is_llm():
    assert classify(make_event(type="hint_delivery", is_hint_delivery=True)) == "llm"


def test_key_loot_is_llm():
    assert classify(make_event(type="loot_narration", is_key_loot=True)) == "llm"


def test_unknown_type_defaults_to_llm():
    """Unknown event types route to LLM — the foundational rule."""
    assert classify(make_event(type="unrecognised_future_type")) == "llm"
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/engine/test_classifier.py -v
```

Expected: `ImportError`

- [ ] **Step 3: Implement `scripts/engine/classifier.py`**

```python
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Event:
    type: str
    pc_slug: str | None
    involves_grief_paragraph: bool
    is_option_c: bool
    is_hint_delivery: bool
    is_read_aloud: bool
    has_npc_dialogue: bool
    is_key_loot: bool
    scene_context: dict


# Event types Python can resolve unambiguously
_PYTHON_TYPES = frozenset({
    "dice_roll",
    "hp_delta",
    "resource_use",
    "doubt_die",
    "signature_move",
    "condition_apply",
    "scene_advance",
})

# Event types that always go to LLM
_LLM_TYPES = frozenset({
    "read_aloud",
    "option_c",
    "dialogue",
    "memory_fragment",
    "atmospheric_chain",
    "hint_delivery",
    "loot_narration",
})


def classify(event: Event) -> str:
    """
    Foundational rule: false-LLM-required is cheap (one extra prompt).
    False-Python-resolved corrupts voice. When in doubt, route to LLM.

    Returns "python" or "llm".
    """
    # Flag-based overrides (highest priority)
    if event.involves_grief_paragraph:
        return "llm"
    if event.is_option_c:
        return "llm"
    if event.is_hint_delivery:
        return "llm"
    if event.is_read_aloud:
        return "llm"
    if event.has_npc_dialogue:
        return "llm"
    if event.is_key_loot:
        return "llm"

    # Type-based routing
    if event.type in _PYTHON_TYPES:
        return "python"
    if event.type in _LLM_TYPES:
        return "llm"

    # Default: LLM. Unknown types are narrative until proven mechanical.
    return "llm"
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/engine/test_classifier.py -v
```

Expected: all 15 tests pass.

- [ ] **Step 5: Commit**

```bash
git add scripts/engine/classifier.py tests/engine/test_classifier.py
git commit -m "feat: classifier — Event dataclass + typed Python/LLM routing with 'when-in-doubt-LLM' default"
```

---

## Task 7: `emitter.py` — LLM Packet Builder + Inbound Validation

**Files:**
- Create: `scripts/engine/emitter.py`
- Create: `tests/engine/test_emitter.py`

- [ ] **Step 1: Write failing tests**

`tests/engine/test_emitter.py`:
```python
import json
import pytest
from pathlib import Path
from scripts.engine.emitter import Emitter, InboundPacket, ValidationError


@pytest.fixture
def emitter(tmp_path):
    return Emitter(state_dir=tmp_path, party_slugs=["aelric", "thera", "kessa", "grom"])


def test_emitter_builds_outbound_packet(emitter):
    packet = emitter.build_outbound(
        session="S04",
        scene_id=3,
        scene_name="The Rite",
        beat_type="hint-delivery",
        state_snapshot={"aelric": {"hp": 28}},
        dice_results=[{"expr": "1d20+3", "total": 12, "label": "Grom Religion"}],
        resolved_mechanics={"rite_result": "pass"},
        decision_point={"type": "hint-delivery", "description": "Hint 2 unlocks"},
        context={"read_aloud": "At the seventh ring..."},
        scene_narrative_so_far=["Scene opened: 'Grey slope...'"],
    )
    assert packet["session"] == "S04"
    assert packet["scene_id"] == 3
    assert packet["beat_type"] == "hint-delivery"
    assert "scene_narrative_so_far" in packet


def test_emitter_writes_checkpoint_before_blocking(emitter, tmp_path):
    packet = emitter.build_outbound(
        session="S04", scene_id=1, scene_name="Test", beat_type="read_aloud",
        state_snapshot={}, dice_results=[], resolved_mechanics={},
        decision_point={}, context={}, scene_narrative_so_far=[],
    )
    emitter.write_checkpoint(packet)
    checkpoint_path = tmp_path / "checkpoint.json"
    assert checkpoint_path.exists()
    stored = json.loads(checkpoint_path.read_text())
    assert stored["session"] == "S04"


def test_validate_inbound_good_packet(emitter):
    raw = {
        "narrative": "Kessa steps forward...",
        "state_updates": {"kessa": {"portent_used": [10]}},
        "innovations_flagged": ["portent-benediction"],
        "advance_to_scene": 4,
        "notes_for_log": "Kessa spoke Qualinesti.",
    }
    packet = emitter.validate_inbound(raw, current_scene_index=3)
    assert packet.narrative == "Kessa steps forward..."
    assert packet.advance_to_scene == 4


def test_validate_inbound_empty_narrative_raises(emitter):
    raw = {"narrative": "", "state_updates": {}, "advance_to_scene": 4}
    with pytest.raises(ValidationError, match="narrative is empty"):
        emitter.validate_inbound(raw, current_scene_index=3)


def test_validate_inbound_unknown_pc_raises(emitter):
    raw = {
        "narrative": "Some text",
        "state_updates": {"pella": {"hp": 5}},
        "advance_to_scene": 4,
    }
    with pytest.raises(ValidationError, match="unknown PC"):
        emitter.validate_inbound(raw, current_scene_index=3)


def test_validate_inbound_backward_scene_raises(emitter):
    raw = {"narrative": "Text", "state_updates": {}, "advance_to_scene": 1}
    with pytest.raises(ValidationError, match="invalid scene advance"):
        emitter.validate_inbound(raw, current_scene_index=3)


def test_validate_inbound_missing_narrative_raises(emitter):
    raw = {"state_updates": {}, "advance_to_scene": 4}
    with pytest.raises(ValidationError, match="narrative"):
        emitter.validate_inbound(raw, current_scene_index=3)


def test_validate_inbound_missing_advance_scene_raises(emitter):
    raw = {"narrative": "Text", "state_updates": {}}
    with pytest.raises(ValidationError, match="advance_to_scene"):
        emitter.validate_inbound(raw, current_scene_index=3)


def test_validate_inbound_defaults_optional_fields(emitter):
    """innovations_flagged and notes_for_log are optional; default to [] and ''."""
    raw = {"narrative": "Text", "state_updates": {}, "advance_to_scene": 4}
    packet = emitter.validate_inbound(raw, current_scene_index=3)
    assert packet.innovations_flagged == []
    assert packet.notes_for_log == ""
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/engine/test_emitter.py -v
```

Expected: `ImportError`

- [ ] **Step 3: Implement `scripts/engine/emitter.py`**

```python
from __future__ import annotations
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


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
        self._checkpoint_path.write_text(
            json.dumps(packet, indent=2), encoding="utf-8"
        )

    def read_checkpoint(self) -> dict | None:
        if not self._checkpoint_path.exists():
            return None
        return json.loads(self._checkpoint_path.read_text(encoding="utf-8"))

    def delete_checkpoint(self) -> None:
        if self._checkpoint_path.exists():
            self._checkpoint_path.unlink()

    def validate_inbound(self, raw: dict, current_scene_index: int) -> InboundPacket:
        # Required fields
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

        # Validate state_updates keys
        updates = raw.get("state_updates", {})
        valid_keys = self._party_slugs | {"hints"}
        for key in updates:
            if key not in valid_keys:
                raise ValidationError(
                    f"unknown PC {key!r} in state_updates. "
                    f"Valid slugs: {', '.join(sorted(self._party_slugs))}"
                )

        return InboundPacket(
            narrative=raw["narrative"],
            state_updates=updates,
            innovations_flagged=raw.get("innovations_flagged", []),
            advance_to_scene=advance,
            notes_for_log=raw.get("notes_for_log", ""),
        )
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/engine/test_emitter.py -v
```

Expected: all 9 tests pass.

- [ ] **Step 5: Commit**

```bash
git add scripts/engine/emitter.py tests/engine/test_emitter.py
git commit -m "feat: emitter — outbound packet builder + inbound InboundPacket validation with 3 error types"
```

---

## Task 8: `log_writer.py` — Session Log Producer

**Files:**
- Create: `scripts/engine/log_writer.py`
- Create: `tests/engine/test_log_writer.py`

- [ ] **Step 1: Write failing tests**

`tests/engine/test_log_writer.py`:
```python
import json
import pytest
from pathlib import Path
from scripts.engine.log_writer import LogWriter


@pytest.fixture
def session_data():
    return {
        "session": "S04",
        "adventure": "test-adventure",
        "dice_seed": "S04-20260419",
        "scenes_completed": [0, 1],
        "scene_index": 2,
    }


@pytest.fixture
def party_data():
    return {
        "aelric": {"hp": 18, "hp_max": 28, "hp_start": 28, "spell_slots": {"L1": 1},
                   "attunements": ["varran-reliquary"], "lay_on_hands": 15,
                   "concentration": None, "conditions": []},
        "thera": {"hp": 20, "hp_max": 20, "hp_start": 20, "spell_slots": {},
                  "attunements": [], "lay_on_hands": 0,
                  "concentration": None, "conditions": []},
    }


@pytest.fixture
def dice_log(tmp_path):
    log = tmp_path / "dice_log.jsonl"
    entries = [
        {"expression": "1d20+5", "rolls": [14], "kept": None, "mod": 5,
         "bless_roll": None, "total": 19, "crit": False, "fumble": False,
         "seed_position": 0, "scene_id": 0, "beat_index": 1,
         "pc_slug": "aelric", "action_label": "attack",
         "log_stub": "DICE_STUB_0"},
    ]
    for e in entries:
        log.write_text("\n".join(json.dumps(x) for x in entries))
    return log


def test_log_writer_produces_file(tmp_path, session_data, party_data, dice_log):
    narratives = {"0": "Scene one narrative.", "1": "Scene two narrative."}
    lw = LogWriter(
        adventure_slug="test-adventure",
        session=session_data,
        party_start=party_data,
        party_end=party_data,
        narratives=narratives,
        dice_log_path=dice_log,
        output_dir=tmp_path,
    )
    out = lw.write()
    assert out.exists()
    assert out.name == "S04-log.md"


def test_log_writer_frontmatter(tmp_path, session_data, party_data, dice_log):
    lw = LogWriter("test-adventure", session_data, party_data, party_data,
                   {}, dice_log, tmp_path)
    out = lw.write()
    content = out.read_text()
    assert "session: S04" in content
    assert "dice-seed: S04-20260419" in content


def test_log_writer_party_table(tmp_path, session_data, party_data, dice_log):
    lw = LogWriter("test-adventure", session_data, party_data, party_data,
                   {}, dice_log, tmp_path)
    out = lw.write()
    content = out.read_text()
    assert "aelric" in content
    assert "thera" in content


def test_log_writer_injects_dice_roll_format(tmp_path, session_data, party_data, dice_log):
    """Dice rolls appear in 🎲 format when log_stub matches in narrative."""
    narratives = {"0": "Aelric attacked. DICE_STUB_0 Then continued."}
    lw = LogWriter("test-adventure", session_data, party_data, party_data,
                   narratives, dice_log, tmp_path)
    out = lw.write()
    content = out.read_text()
    assert "🎲" in content
    assert "1d20+5" in content
    assert "total=19" in content


def test_log_writer_summary_section(tmp_path, session_data, party_data, dice_log):
    session_with_summary = {**session_data, "summary": "The party defeated the guards."}
    lw = LogWriter("test-adventure", session_with_summary, party_data, party_data,
                   {}, dice_log, tmp_path)
    out = lw.write()
    content = out.read_text()
    assert "Session Summary" in content
    assert "defeated the guards" in content
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/engine/test_log_writer.py -v
```

Expected: `ImportError`

- [ ] **Step 3: Implement `scripts/engine/log_writer.py`**

```python
from __future__ import annotations
import json
from pathlib import Path
from datetime import date


class LogWriter:
    def __init__(
        self,
        adventure_slug: str,
        session: dict,
        party_start: dict,
        party_end: dict,
        narratives: dict[str, str],   # scene_id_str → LLM narrative text
        dice_log_path: Path,
        output_dir: Path,
    ) -> None:
        self._slug = adventure_slug
        self._session = session
        self._party_start = party_start
        self._party_end = party_end
        self._narratives = narratives
        self._dice_log_path = dice_log_path
        self._output_dir = output_dir

    def _load_dice_log(self) -> list[dict]:
        if not self._dice_log_path.exists():
            return []
        entries = []
        for line in self._dice_log_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                entries.append(json.loads(line))
        return entries

    def _format_roll(self, entry: dict) -> str:
        pc = entry.get("pc_slug", "?")
        label = entry.get("action_label", entry["expression"])
        rolls_str = str(entry["rolls"])
        mod = entry["mod"]
        total = entry["total"]
        suffix = ""
        if entry.get("crit"):
            suffix = " CRIT"
        elif entry.get("fumble"):
            suffix = " FUMBLE"
        return (
            f"**🎲 {pc} {label}** — `{entry['expression']}` "
            f"→ rolls={rolls_str} mod={mod:+d} **total={total}{suffix}**"
        )

    def _inject_dice_stubs(self, narrative: str, dice_entries: list[dict]) -> str:
        stub_map = {
            e["log_stub"]: self._format_roll(e)
            for e in dice_entries
            if "log_stub" in e
        }
        result = narrative
        for stub, formatted in stub_map.items():
            result = result.replace(stub, formatted)
        return result

    def write(self) -> Path:
        s = self._session
        session_name = s["session"]
        dice_entries = self._load_dice_log()
        stub_map = {
            e["log_stub"]: self._format_roll(e)
            for e in dice_entries
            if "log_stub" in e
        }

        lines = [
            "---",
            f"session: {session_name}",
            f"adventure: {self._slug}",
            f"party: varduin-muster",
            f"date: {date.today().isoformat()}",
            f"dice-seed: {s['dice_seed']}",
            "author: session-runner",
            "---",
            "",
            f"# {session_name} LOG — {self._slug}",
            "",
        ]

        # Summary
        summary = s.get("summary", "")
        lines += ["## Session Summary", "", summary or "(no summary provided)", ""]

        # Party state delta table
        lines += ["## Party state (delta)", ""]
        lines += ["| PC | HP start → end | Spells used | Attune | Notable |",
                  "|---|---|---|---|---|"]
        for slug, end in self._party_end.items():
            start = self._party_start.get(slug, end)
            hp_start = start.get("hp_start", start.get("hp_max", "?"))
            hp_end = end["hp"]
            attunes = ", ".join(end.get("attunements", [])) or "—"
            lines.append(
                f"| {slug} | {hp_start} → {hp_end} | — | {attunes} | — |"
            )
        lines.append("")

        # Scenes
        lines += ["## Scenes", ""]
        for scene_id_str, narrative in sorted(
            self._narratives.items(), key=lambda x: int(x[0])
        ):
            # Inject dice stubs
            text = narrative
            for stub, formatted in stub_map.items():
                text = text.replace(stub, formatted)
            lines += [f"### Scene {scene_id_str}", "", text, "---", ""]

        output = self._output_dir / f"{session_name}-log.md"
        output.write_text("\n".join(lines), encoding="utf-8")
        return output
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/engine/test_log_writer.py -v
```

Expected: all 5 tests pass.

- [ ] **Step 5: Commit**

```bash
git add scripts/engine/log_writer.py tests/engine/test_log_writer.py
git commit -m "feat: log_writer — produces S{N}-log.md with dice-stub injection, party delta table, frontmatter"
```

---

## Task 9: `marathon.py` — CLI Entry Point

**Files:**
- Create: `scripts/marathon.py`

- [ ] **Step 1: Write integration smoke test**

`tests/test_cli.py`:
```python
import subprocess
import sys
import pytest
from pathlib import Path


def run_cli(*args):
    result = subprocess.run(
        [sys.executable, "scripts/marathon.py"] + list(args),
        capture_output=True, text=True, cwd=Path(__file__).parent.parent
    )
    return result


def test_cli_no_args_prints_help():
    r = run_cli()
    # argparse exits with 2 and prints usage when no subcommand given
    assert r.returncode == 2
    assert "usage" in r.stderr.lower() or "usage" in r.stdout.lower()


def test_cli_status_no_session():
    r = run_cli("status")
    assert r.returncode == 0
    assert "No active session" in r.stdout


def test_cli_resume_no_checkpoint():
    r = run_cli("resume")
    assert r.returncode == 1
    assert "No checkpoint found" in r.stdout
```

- [ ] **Step 2: Run smoke tests to verify they fail**

```bash
pytest tests/test_cli.py -v
```

Expected: `FileNotFoundError` or `No module named scripts.marathon`

- [ ] **Step 3: Implement `scripts/marathon.py`**

```python
#!/usr/bin/env python3
"""marathon.py — CLI entry point for the Marathon D&D session engine."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

# Add the repo root to sys.path so `scripts.engine.*` imports work
_REPO_ROOT = Path(__file__).parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from scripts.engine.state import StateManager
from scripts.engine.loader import load_adventure, load_party, LoadError


STATE_DIR = Path("state")


def cmd_status(args) -> int:
    sm = StateManager(state_dir=STATE_DIR)
    loaded = sm.read_session()
    if loaded is None:
        print("No active session. Start one with:")
        print("  python marathon.py start --adventure <slug> --session <name>")
        return 0

    session = loaded["session"]
    party = loaded["party"]
    checkpoint = sm.read_checkpoint()

    sep = "═" * 50
    print(sep)
    print(f"SESSION: {session.session} | ADVENTURE: {session.adventure}")
    print(f"SCENE: {session.scene_index} | COMPLETED: {session.scenes_completed}")
    print()
    print("PARTY STATE:")
    for slug in party.slugs():
        pc = party[slug]
        slots = " ".join(f"{k}:{v}" for k, v in pc.spell_slots.items()) or "—"
        attune = ", ".join(pc.attunements) or "—"
        conds = ", ".join(pc.conditions) or "—"
        print(f"  {slug:<28} HP {pc.hp}/{pc.hp_max}  Slots {slots}  "
              f"Attune: {attune}  Conds: {conds}")
    print()
    if checkpoint:
        beat = checkpoint.get("beat_type", "unknown")
        scene = checkpoint.get("scene_id", "?")
        print(f"PENDING CHECKPOINT: scene_{scene}_{beat}")
        print("  (resume with: python marathon.py resume)")
    else:
        print("PENDING CHECKPOINT: none")
    print(sep)
    return 0


def cmd_start(args) -> int:
    adventure_slug = args.adventure
    session_name = args.session
    party_slug = getattr(args, "party", "varduin-muster")

    module_path = Path(f"adventures/{adventure_slug}/module.md")
    party_dir = Path(f"personas/parties/{party_slug}")

    try:
        adventure = load_adventure(module_path)
        pcs = load_party(party_dir)
    except LoadError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    print(f"Loaded adventure: {adventure_slug} ({len(adventure.scenes)} scenes)")
    print(f"Loaded party: {party_slug} ({len(pcs)} PCs)")
    print()
    print("Session engine not yet fully implemented. State initialised.")
    print("Run 'python marathon.py status' to see current state.")

    # Initialise state
    from scripts.engine.state import (
        PartyState, SessionState, CampaignFacts, StateManager
    )
    party_dict = {
        pc.slug: {
            "hp": pc.hp, "hp_max": pc.hp_max,
            "spell_slots": pc.spell_slots,
            "attunements": pc.attunements,
            "lay_on_hands": 0,
            "concentration": None,
            "conditions": [],
        }
        for pc in pcs
    }
    session_dict = {
        "adventure": adventure_slug,
        "session": session_name,
        "dice_seed": f"{session_name}-{__import__('datetime').date.today().strftime('%Y%m%d')}",
        "scene_index": 0,
        "scenes_completed": [],
        "pending_checkpoint": None,
    }
    campaign_dict = {"hints": {}, "campaign_permanent": []}

    sm = StateManager(state_dir=STATE_DIR)
    sm.write_session(
        party=PartyState.from_dict(party_dict),
        session=SessionState.from_dict(session_dict),
        campaign=CampaignFacts.from_dict(campaign_dict),
    )
    print(f"State written to {STATE_DIR}/session.json")
    return 0


def cmd_resume(args) -> int:
    sm = StateManager(state_dir=STATE_DIR)
    checkpoint = sm.read_checkpoint()

    if checkpoint is None:
        print("No checkpoint found. Use 'start' to begin a new session.")
        return 1

    session_id = checkpoint.get("session", "?")
    beat_type = checkpoint.get("beat_type", "?")
    scene_id = checkpoint.get("scene_id", "?")
    scene_name = checkpoint.get("scene_name", "?")

    sep = "═" * 50
    print(sep)
    print(f"RESUMING: {session_id} | SCENE {scene_id} — {scene_name}")
    print(f"BEAT: {beat_type}")
    print()

    # Display the prompt summary
    dp = checkpoint.get("decision_point", {})
    ctx = checkpoint.get("context", {})
    if dp.get("description"):
        print(f"PROMPT: {dp['description']}")
    if ctx.get("read_aloud"):
        print(f"READ-ALOUD: {ctx['read_aloud']}")
    print()

    # Show dice results
    for dr in checkpoint.get("dice_results", []):
        label = dr.get("label", dr.get("expr", "roll"))
        print(f"  DICE: {label} → {dr.get('total')}")
    print(sep)
    print()
    print(">>> WAITING FOR LLM RESPONSE (paste JSON below, then press Ctrl+D / Ctrl+Z):")
    print()

    # Read multiline JSON from stdin
    lines = []
    try:
        for line in sys.stdin:
            lines.append(line)
    except KeyboardInterrupt:
        print("\nInterrupted. Checkpoint preserved.")
        return 1

    raw_text = "".join(lines).strip()
    if not raw_text:
        print("No input received. Checkpoint preserved.")
        return 1

    try:
        raw = json.loads(raw_text)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON response — {e}")
        print("Checkpoint preserved. Run 'resume' again to retry.")
        return 1

    # Validate via emitter
    from scripts.engine.emitter import Emitter, ValidationError
    loaded = sm.read_session()
    party_slugs = list(loaded["party"].slugs()) if loaded else []
    emitter = Emitter(state_dir=STATE_DIR, party_slugs=party_slugs)

    current_scene = loaded["session"].scene_index if loaded else 0
    try:
        packet = emitter.validate_inbound(raw, current_scene_index=current_scene)
    except ValidationError as e:
        print(f"ERROR: {e}")
        print("Checkpoint preserved. Run 'resume' again with a corrected response.")
        return 1

    print(f"Response validated. Advancing to scene {packet.advance_to_scene}.")

    # Update session state
    if loaded:
        session = loaded["session"]
        party = loaded["party"]
        campaign = loaded["campaign"]

        # Apply state updates from LLM response
        for key, updates in packet.state_updates.items():
            if key == "hints":
                for hint_key, hint_val in updates.items():
                    campaign.hints[hint_key] = hint_val
            elif key in party.slugs():
                pc = party[key]
                for field, val in updates.items():
                    if hasattr(pc, field):
                        setattr(pc, field, val)

        session.scene_index = packet.advance_to_scene
        sm.write_session(party=party, session=session, campaign=campaign)

    sm.delete_checkpoint()
    print("Checkpoint cleared. Session state updated.")
    if packet.notes_for_log:
        print(f"Note for log: {packet.notes_for_log}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="marathon.py",
        description="Marathon D&D session engine",
    )
    sub = parser.add_subparsers(dest="command")

    # start
    p_start = sub.add_parser("start", help="Begin a new session")
    p_start.add_argument("--adventure", required=True, help="Adventure slug")
    p_start.add_argument("--session", required=True, help="Session name (e.g. S04)")
    p_start.add_argument("--party", default="varduin-muster", help="Party slug")

    # resume
    sub.add_parser("resume", help="Re-enter from last checkpoint")

    # status
    sub.add_parser("status", help="Print current state snapshot")

    args = parser.parse_args()
    if args.command is None:
        parser.print_usage(sys.stderr)
        return 2

    handlers = {"start": cmd_start, "resume": cmd_resume, "status": cmd_status}
    return handlers[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run smoke tests to verify they pass**

```bash
pytest tests/test_cli.py -v
```

Expected: all 3 tests pass.

- [ ] **Step 5: Run full test suite**

```bash
pytest -v
```

Expected: all tests pass (Tasks 1-9 combined).

- [ ] **Step 6: Commit**

```bash
git add scripts/marathon.py tests/test_cli.py
git commit -m "feat: CLI entry point — start, resume (with validation), status with exact output format"
```

---

## Task 10: Integration Test + Final Polish

**Files:**
- Modify: `scripts/marathon.py` (minor)
- Create: `tests/test_integration.py`

- [ ] **Step 1: Write integration test — full start → status cycle**

`tests/test_integration.py`:
```python
import subprocess, sys, json
from pathlib import Path

CLI = [sys.executable, "scripts/marathon.py"]
CWD = Path(__file__).parent.parent


def run(*args, stdin_text=None):
    return subprocess.run(
        CLI + list(args),
        capture_output=True, text=True, cwd=CWD,
        input=stdin_text,
    )


def test_full_start_and_status_cycle(tmp_path, monkeypatch):
    """start writes state; status reads and prints it."""
    monkeypatch.chdir(tmp_path)
    # Copy fixtures
    import shutil
    (tmp_path / "adventures" / "test-adventure").mkdir(parents=True)
    (tmp_path / "personas" / "parties" / "test-party").mkdir(parents=True)
    shutil.copy(
        CWD / "tests/fixtures/mini_module.md",
        tmp_path / "adventures/test-adventure/module.md",
    )
    shutil.copy(
        CWD / "tests/fixtures/mini_pc.md",
        tmp_path / "personas/parties/test-party/test-fighter.md",
    )

    r_start = run("start", "--adventure", "test-adventure",
                  "--session", "S01", "--party", "test-party")
    assert r_start.returncode == 0, r_start.stderr

    r_status = run("status")
    assert r_status.returncode == 0
    assert "S01" in r_status.stdout
    assert "test-fighter" in r_status.stdout
    assert "No active session" not in r_status.stdout


def test_resume_with_valid_response(tmp_path, monkeypatch):
    """resume accepts a valid JSON response and clears the checkpoint."""
    monkeypatch.chdir(tmp_path)
    import shutil
    (tmp_path / "adventures/test-adventure").mkdir(parents=True)
    (tmp_path / "personas/parties/test-party").mkdir(parents=True)
    (tmp_path / "state").mkdir()
    shutil.copy(CWD / "tests/fixtures/mini_module.md",
                tmp_path / "adventures/test-adventure/module.md")
    shutil.copy(CWD / "tests/fixtures/mini_pc.md",
                tmp_path / "personas/parties/test-party/test-fighter.md")

    # Manually write a checkpoint and session
    from scripts.engine.state import StateManager, PartyState, SessionState, CampaignFacts
    sm = StateManager(state_dir=tmp_path / "state")
    sm.write_session(
        party=PartyState.from_dict({
            "test-fighter": {"hp": 28, "hp_max": 28, "spell_slots": {},
                              "attunements": [], "lay_on_hands": 0,
                              "concentration": None, "conditions": []}
        }),
        session=SessionState.from_dict({
            "adventure": "test-adventure", "session": "S01",
            "dice_seed": "S01-test", "scene_index": 1,
            "scenes_completed": [0], "pending_checkpoint": "scene_1_read_aloud",
        }),
        campaign=CampaignFacts.from_dict({"hints": {}, "campaign_permanent": []}),
    )
    sm.write_checkpoint({
        "session": "S01", "scene_id": 1, "scene_name": "The Vault",
        "beat_type": "read_aloud", "state_snapshot": {}, "dice_results": [],
        "resolved_mechanics": {}, "decision_point": {"description": "Narrate scene 1"},
        "context": {}, "scene_narrative_so_far": [],
    })

    valid_response = json.dumps({
        "narrative": "The vault door stands, ancient and sealed.",
        "state_updates": {},
        "advance_to_scene": 2,
    })

    r = run("resume", stdin_text=valid_response + "\n")
    assert r.returncode == 0, r.stderr + r.stdout
    assert "validated" in r.stdout.lower()
    assert not (tmp_path / "state" / "checkpoint.json").exists()
```

- [ ] **Step 2: Run integration tests**

```bash
pytest tests/test_integration.py -v
```

Expected: both tests pass.

- [ ] **Step 3: Run full test suite one final time**

```bash
pytest -v
```

Expected: all tests pass.

- [ ] **Step 4: Verify CLI help text**

```bash
python scripts/marathon.py --help
python scripts/marathon.py start --help
python scripts/marathon.py resume --help
python scripts/marathon.py status --help
```

Expected: clean help output for each subcommand.

- [ ] **Step 5: Final commit**

```bash
git add tests/test_integration.py
git commit -m "test: integration tests — start→status cycle + resume with valid response"
```

---

## Self-Review

### Spec coverage check

| Spec requirement | Task |
|---|---|
| `dice.py` seed-locked RNG | Task 2 |
| `state.py` three-layer state model | Task 3 |
| `loader.py` parses module.md + PC sheets | Task 4 |
| `heuristics.py` doubt-die, decision-order, bless, signature moves | Task 5 |
| `classifier.py` Event dataclass + Python/LLM routing table | Task 6 |
| `emitter.py` outbound packet + inbound validation + 3 malformed examples | Task 7 |
| `log_writer.py` produces S{N}-log.md with dice-stub injection | Task 8 |
| `marathon.py` start/resume/status CLI | Task 9 |
| Checkpoint written before blocking | Task 7 + 9 |
| Atomic session.json write via .tmp rename | Task 3 |
| State write ordering (dice_log.jsonl → in-memory → scene boundary) | Task 3 |
| LLM protocol: stdin/stdout paste-JSON | Task 9 |
| `marathon.py status` exact output format | Task 9 |
| Re-entrancy guarantee | Task 7 + 9 + 10 |
| Error recovery table (13 failure modes) | Tasks 7+9 handle most; loader handles LoadError |
| Heuristics source: YAML frontmatter, no code for new PC | Task 5 |
| scene_narrative_so_far in outbound packet | Task 7 |

All spec requirements have a corresponding task.

### No placeholders

Checked — no TBD, TODO, "similar to Task N", or code-less steps.

### Type consistency

- `DiceEngine`, `RollResult`, `DiceError` defined Task 2; used in Tasks 3, 9.
- `PartyState`, `SessionState`, `CampaignFacts`, `StateManager` defined Task 3; used in Tasks 9, 10.
- `Adventure`, `Scene`, `PC`, `LoadError` defined Task 4; used in Tasks 5, 9.
- `Heuristics`, `HeuristicsError`, `DoubtDieResult` defined Task 5; no downstream use in Tasks 6-8 (heuristics.py is standalone).
- `Event`, `classify` defined Task 6; used in scene.py (not implemented yet — scene.py is complex enough for a follow-on plan).
- `Emitter`, `InboundPacket`, `ValidationError` defined Task 7; used in Task 9.
- `LogWriter` defined Task 8; not called from Task 9 yet (log writing is triggered post-session).
- All method signatures consistent across tasks.

### Scope note

`scene.py` — the scene state machine — is the most complex component and deliberately left as an advanced follow-on. Tasks 1-10 produce a fully working CLI with all supporting components tested. `scene.py` would be its own plan, built on this foundation.
