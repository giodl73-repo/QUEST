from __future__ import annotations
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml


class LoadError(Exception):
    pass


@dataclass
class Scene:
    index: int
    name: str
    read_aloud: str
    gm_notes: str
    stat_blocks: list[dict]
    npc_arc_candidates: list[dict] = field(default_factory=list)
    # Each entry: {"npc": str, "arc_completion": str, "condition": str}


@dataclass
class Adventure:
    slug: str
    scenes: list[Scene]
    dc_table: list[dict]


@dataclass
class PC:
    slug: str
    ac: int
    hp: int
    hp_max: int
    spell_slots: dict[str, int]
    attunements: list[str]
    heuristics: dict


_YAML_FRONT = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
_SCENE_HEADER = re.compile(r"^### Scene \d+ — (.+)$", re.MULTILINE)
_READ_ALOUD = re.compile(r"> (.+?)(?=\n\n|\Z)", re.DOTALL)
_AC_HP = re.compile(r"\*\*AC\*\*\s*(\d+).*?\*\*HP\*\*\s*(\d+)", re.DOTALL)


def _parse_read_aloud(text: str) -> str:
    m = _READ_ALOUD.search(text)
    if not m:
        return ""
    return m.group(1).replace("\n> ", " ").replace("\n", " ").strip()


def _parse_stat_blocks(text: str) -> list[dict]:
    blocks = []
    # Match: **Name — CR X, Y XP.** **AC** N · **HP** N
    pattern = re.compile(
        r"\*\*([^*\n]+?)\s*(?:—[^*\n]*)?\*\*[^\n]*\*\*AC\*\*\s*(\d+)[^\n]*\*\*HP\*\*\s*(\d+)",
    )
    for m in pattern.finditer(text):
        name = m.group(1).strip()
        if name.startswith(">"):
            continue
        blocks.append({"name": name, "ac": int(m.group(2)), "hp": int(m.group(3))})
    return blocks


def _parse_npc_arc_completions(text: str) -> dict[str, dict]:
    """Extract Arc-Completion sections from the NPCs section of module.md.

    Returns a dict mapping NPC name (lowercase) to
    {"arc_completion": <moment text>, "condition": <condition text>}.
    """
    arcs: dict[str, dict] = {}
    # Find NPC blocks: ## NPCs ... each NPC headed by ### <Name>
    npc_section = re.search(r"^## NPCs\b(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    if not npc_section:
        return arcs

    npc_blocks = re.split(r"^### ", npc_section.group(1), flags=re.MULTILINE)
    for block in npc_blocks:
        if not block.strip():
            continue
        # First line is the NPC name
        name_line = block.splitlines()[0].strip()
        npc_name = name_line.lower()

        arc_m = re.search(
            r"#{2,4} Arc-Completion\s*\n\*\*The moment:\*\*\s*(.+?)(?=\*\*What it produces|\Z)",
            block, re.DOTALL,
        )
        cond_m = re.search(r"\*\*The condition:\*\*\s*(.+?)(?=\n\n|\n##|\Z)", block, re.DOTALL)

        if arc_m:
            arcs[npc_name] = {
                "npc": name_line,
                "arc_completion": arc_m.group(1).strip(),
                "condition": cond_m.group(1).strip() if cond_m else "",
            }
    return arcs


def _match_arc_candidates(scene_body: str, arcs: dict[str, dict]) -> list[dict]:
    """Return arc candidates whose NPC name appears in the scene body."""
    candidates = []
    for npc_name_lower, arc in arcs.items():
        # Match on first word of name to catch "Mira" matching "Mira Vaenshold"
        first_word = npc_name_lower.split()[0] if npc_name_lower else ""
        if first_word and re.search(r"\b" + re.escape(first_word) + r"\b", scene_body, re.IGNORECASE):
            candidates.append(arc)
    return candidates


def _parse_dc_table(text: str) -> list[dict]:
    rows = []
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


def _split_scenes(text: str) -> list[tuple[int, str, str]]:
    parts = re.split(r"(?=^### Scene \d+)", text, flags=re.MULTILINE)
    result = []
    for part in parts:
        m = _SCENE_HEADER.match(part)
        if m:
            result.append((len(result), m.group(1).strip(), part))
    return result


def load_adventure(path: Path) -> Adventure:
    if not path.exists():
        raise LoadError(f"module.md not found: {path}")

    text = path.read_text(encoding="utf-8")

    slug = ""
    fm_match = _YAML_FRONT.match(text)
    if fm_match:
        try:
            fm = yaml.safe_load(fm_match.group(1))
            slug = fm.get("adventure", "")
        except Exception:
            pass

    npc_arcs = _parse_npc_arc_completions(text)
    scene_parts = _split_scenes(text)
    scenes = []
    for idx, name, body in scene_parts:
        scenes.append(Scene(
            index=idx,
            name=name,
            read_aloud=_parse_read_aloud(body),
            gm_notes="",
            stat_blocks=_parse_stat_blocks(body),
            npc_arc_candidates=_match_arc_candidates(body, npc_arcs),
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
            continue

        if "heuristics" not in fm:
            raise LoadError(f"No heuristics block in {md_file}")

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
