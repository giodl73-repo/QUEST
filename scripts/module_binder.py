#!/usr/bin/env python3
"""
module_binder.py — Compile an adventure directory into a single table-ready module.md.

Reads:
  adventures/<slug>/premise.md
  adventures/<slug>/rooms/map.md
  adventures/<slug>/rooms/NN-*.md  (numeric order)
  adventures/<slug>/treasures/*.md  (excluding *-manifest.md)
  adventures/<slug>/encounters/*.md
  adventures/<slug>/npcs/*.md

Writes:
  adventures/<slug>/module.md  (or module.vN.md if it already exists)

Output is structured for loader.py (scripts/engine/loader.py):
  - YAML frontmatter with adventure: <slug>
  - ### Scene N — <Name> headers (H3) for each room
  - Blockquote read-aloud in each scene
  - **Name — CR X, Y XP.** **AC** N · **HP** N stat block lines
  - ## NPCs with Arc-Completion in loader format
  - ### Quick Reference — Key DCs (by scene) DC table
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

import yaml

_REPO_ROOT = Path(__file__).resolve().parent.parent

# Premise H2 sections excluded from the background block (technical, not narrative)
_PREMISE_BG_EXCLUDED = frozenset({
    "__pre__", "Constraints", "Key Files in This Adventure",
    "Themes", "The Real Decision", "Central Artifact (seed)",
    "Encounters", "Prior Bearers",
})

# ---------------------------------------------------------------------------
# File reading
# ---------------------------------------------------------------------------

_YAML_FRONT = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def _read(path: Path) -> tuple[dict, str]:
    """Return (frontmatter_dict, body_text) for a markdown file."""
    text = path.read_text(encoding="utf-8")
    m = _YAML_FRONT.match(text)
    if m:
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except Exception:
            fm = {}
        return fm, text[m.end():]
    return {}, text


def _split_h2(body: str) -> dict[str, str]:
    """Split body on H2 headers. Returns {header_name: section_body}."""
    parts = re.split(r"^## (.+?)$", body, flags=re.MULTILINE)
    out: dict[str, str] = {"__pre__": parts[0]}
    for i in range(1, len(parts), 2):
        if i + 1 < len(parts):
            out[parts[i].strip()] = parts[i + 1].strip()
    return out


# ---------------------------------------------------------------------------
# DC extraction
# ---------------------------------------------------------------------------

_DC_RE = re.compile(r"\bDC\s+(\d+)\b")


def _extract_dcs(features: str, scene_num: int) -> list[dict]:
    rows = []
    for line in features.splitlines():
        line = line.strip()
        if not line:
            continue
        dc_match = _DC_RE.search(line)  # cache — only search once
        if not dc_match:
            continue
        dc_val = int(dc_match.group(1))
        ctx = re.search(
            r"DC\s+\d+\s+([A-Za-z /]+?)(?:\s+to\s+|\s+\()(.+?)(?:\.|;|\)|$)",
            line, re.IGNORECASE,
        )
        if ctx:
            check = ctx.group(1).strip()[:35]
            consequence = ctx.group(2).strip()[:55]
        else:
            clean = re.sub(r"\*\*([^*]+)\*\*", r"\1", line).lstrip("- ")
            check = clean[:35].strip()
            consequence = ""
        rows.append({"dc": dc_val, "check": check, "scene": scene_num, "consequence": consequence})
    return rows


# ---------------------------------------------------------------------------
# Stat block handling
# ---------------------------------------------------------------------------

_KNOWN_CR_XP: dict[str, tuple[str, int]] = {
    "swarm of rats": ("¼", 50),
    "swarm": ("¼", 50),
    "giant rat": ("⅛", 25),
    "goblin": ("¼", 50),
    "skeleton": ("¼", 50),
    "zombie": ("¼", 50),
    "ghoul": ("1", 200),
    "animated armor": ("1", 200),
    "wolf": ("¼", 50),
    "cultist": ("⅛", 25),
    "bandit": ("⅛", 25),
}
_DEFAULT_CR_XP = ("¼", 50)

# Match: ### Name\n*... HP N ... AC N ...*
_COMBATANT_BLOCK = re.compile(
    r"^### (.+?)\n\*[^*]*?HP\s+(\d+)[^*]*?AC\s+(\d+)",
    re.MULTILINE | re.IGNORECASE,
)
# Match: **HP:** N · **AC:** N  (alternative format)
_HP_AC_STAR = re.compile(r"\*\*HP:\*\*\s*(\d+)[^·]*·[^A]*\*\*AC:\*\*\s*(\d+)")


def _cr_xp(name: str) -> tuple[str, int]:
    lower = name.lower()
    for key, vals in _KNOWN_CR_XP.items():
        if key in lower:
            return vals
    return _DEFAULT_CR_XP


def _stat_line(name: str, ac: int, hp: int) -> str:
    cr, xp = _cr_xp(name)
    return f"**{name} — CR {cr}, {xp} XP.** **AC** {ac} · **HP** {hp}"


def _parse_stat_blocks_from_encounter(body: str) -> list[str]:
    lines = []
    for m in _COMBATANT_BLOCK.finditer(body):
        name, hp, ac = m.group(1).strip(), int(m.group(2)), int(m.group(3))
        lines.append(_stat_line(name, ac, hp))
    if not lines:
        m = _HP_AC_STAR.search(body)
        if m:
            hp, ac = int(m.group(1)), int(m.group(2))
            nm = re.search(r"^### (.+?)$", body, re.MULTILINE)
            name = nm.group(1).strip() if nm else "Unnamed"
            lines.append(_stat_line(name, ac, hp))
    return lines


# ---------------------------------------------------------------------------
# Inlining helpers
# ---------------------------------------------------------------------------

_ENC_REF = re.compile(r"See `encounters/([^`]+\.md)`", re.IGNORECASE)
# Require backtick delimiters to avoid false-positive matches on prose paths
_TREAS_REF = re.compile(r"(?:See\s+)?`treasures/([^`\s]+\.md)`", re.IGNORECASE)

# Headers to downgrade when inlining encounter files into scene bodies
_INLINE_HEADER = re.compile(r"^(#{1,3})\s+(.+?)$", re.MULTILINE)


def _strip_headers(text: str) -> str:
    """Downgrade H1/H2/H3 to bold text in content inlined into scene bodies."""
    return _INLINE_HEADER.sub(r"**\2**", text)


def _inline_encounter(enc_section: str, adv_dir: Path) -> tuple[str, list[str]]:
    """Replace encounter file references with inlined content. Returns (text, stat_blocks)."""
    stat_blocks: list[str] = []

    def replace(m: re.Match) -> str:
        path = adv_dir / "encounters" / m.group(1)
        if not path.exists():
            return m.group(0)
        _, body = _read(path)
        sb = _parse_stat_blocks_from_encounter(body)
        stat_blocks.extend(sb)
        # Strip H1-H3 headers and inline first 5 paragraphs
        body = _strip_headers(body)
        paras = [p.strip() for p in body.split("\n\n") if p.strip()]
        return "\n\n".join(paras[:5])

    return _ENC_REF.sub(replace, enc_section), stat_blocks


def _inline_treasure(treas_section: str, adv_dir: Path) -> str:
    def replace(m: re.Match) -> str:
        fname = m.group(1)
        if "-manifest" in fname:
            return m.group(0)
        path = adv_dir / "treasures" / fname
        if not path.exists():
            return m.group(0)
        _, body = _read(path)
        secs = _split_h2(body)
        parts = []
        for key in ("Appearance", "Presence / Desire", "Properties (Mechanical)", "Relic Test", "Ending the Curse"):
            if key in secs:
                parts.append(f"##### {key}\n\n{secs[key]}")
        return "\n\n".join(parts) if parts else body[:600]

    return _TREAS_REF.sub(replace, treas_section)


# ---------------------------------------------------------------------------
# NPC arc-completion format conversion
# ---------------------------------------------------------------------------

_ARC_BLOCK = re.compile(
    r"## Arc-Completion\s+(.+?)(?=^## |\Z)",
    re.MULTILINE | re.DOTALL,
)


def _convert_arc(body: str) -> str:
    """Convert ## Arc-Completion from NPC-file format to loader format."""

    def rewrite(m: re.Match) -> str:
        block = m.group(1)
        cond_m = re.search(r"\*\*Condition:\*\*\s*(.+?)(?=\n\n|\n\*\*|\Z)", block, re.DOTALL)
        act_m = re.search(r"\*\*The act:\*\*\s*(.+?)(?=\n\n|\n\*\*|\Z)", block, re.DOTALL)
        if not (cond_m or act_m):
            return m.group(0)
        moment = (act_m.group(1).strip() if act_m else "Arc fires when condition is met.")
        condition = (cond_m.group(1).strip() if cond_m else "See NPC notes.")
        return f"#### Arc-Completion\n**The moment:** {moment}\n**The condition:** {condition}\n"

    return _ARC_BLOCK.sub(rewrite, body)


# ---------------------------------------------------------------------------
# Read-aloud extraction (last blockquote = trimmed version)
# ---------------------------------------------------------------------------

_BLOCKQUOTE_BLOCK = re.compile(
    r"(?:^>[ \t]?.+$(?:\n>[ \t]?.+$)*)",
    re.MULTILINE,
)


def _last_blockquote(text: str) -> str:
    """Return the last contiguous blockquote block in text (the trimmed version)."""
    matches = _BLOCKQUOTE_BLOCK.findall(text)
    return matches[-1].strip() if matches else ""


# ---------------------------------------------------------------------------
# Scene builder
# ---------------------------------------------------------------------------

def _build_scene(scene_num: int, room_path: Path, adv_dir: Path) -> tuple[str, list[dict], dict, str]:
    """Build a ### Scene N — Name block. Returns (text, dc_rows, sections, body)."""
    _, body = _read(room_path)
    secs = _split_h2(body)

    # Room name from H1
    h1 = re.search(r"^# Room \d+ — (.+?)$", secs["__pre__"], re.MULTILINE)
    room_name = h1.group(1).strip() if h1 else room_path.stem

    read_aloud_raw = secs.get("Read-aloud", "")
    read_aloud = _last_blockquote(read_aloud_raw) or read_aloud_raw

    features = secs.get("Features", "")
    dc_rows = _extract_dcs(features, scene_num)

    enc_text = secs.get("Encounter", "None.")
    enc_inlined, stat_blocks = _inline_encounter(enc_text, adv_dir)

    treas_text = secs.get("Treasure", "None.")
    treas_inlined = _inline_treasure(treas_text, adv_dir)

    connections = secs.get("Connections", "")
    gm_notes = secs.get("GM Notes", "")

    sb_section = ""
    if stat_blocks:
        sb_section = "\n\n**Stat blocks:**\n\n" + "\n\n".join(stat_blocks)

    scene_text = f"""\
### Scene {scene_num} — {room_name}

{read_aloud}

#### Features

{features}

#### Encounter

{enc_inlined}{sb_section}

#### Treasure

{treas_inlined}

#### Connections

{connections}

#### GM Notes

{gm_notes}"""

    return scene_text, dc_rows, secs, body


# ---------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------

_SRD_ATTUNEMENT = (
    "**Attunement (SRD):** Short rest (1 hour) focused on the item to attune. "
    "Max 3 attuned items per creature. Curse revealed on attunement (not before). "
    "*Remove curse* ends the curse on the current owner; the item retains the curse."
)

_SRD_SWARM_RULES = (
    "**Swarm rules (SRD):** A swarm occupies another creature's space and vice versa. "
    "A swarm can move through any opening large enough for a Tiny creature. "
    "A swarm can't regain HP or gain temporary HP."
)

_XP_BUDGET = (
    "**XP Budget (4 PCs, level 3):** "
    "Easy 300 · Medium 600 · Hard 900 · Deadly 1,600"
)


def _dc_table(rows: list[dict]) -> str:
    header = "| DC | Check | Scene | Consequence |\n|---|---|---|---|"
    if not rows:
        return header + "\n| — | — | — | — |"
    body = "\n".join(
        f"| {r['dc']} | {r['check']} | {r['scene']} | {r['consequence']} |"
        for r in sorted(rows, key=lambda x: (x["scene"], x["dc"]))
    )
    return f"{header}\n{body}"


def _cheatsheet(dc_rows: list[dict]) -> str:
    return f"""\
## DM Cheatsheet

### Quick Reference — Key DCs (by scene)

{_dc_table(dc_rows)}

### Rules Inlined

{_SRD_ATTUNEMENT}

{_SRD_SWARM_RULES}

{_XP_BUDGET}"""


def _treasures_section(treasure_files: list[Path]) -> str:
    parts = ["## Treasures"]
    for t in treasure_files:
        if "-manifest" in t.name:
            continue
        _, body = _read(t)
        parts.append(body.strip())
    return "\n\n---\n\n".join(parts)


def _npcs_section(npc_files: list[Path]) -> str:
    parts = ["## NPCs"]
    for npc in sorted(npc_files):
        _, body = _read(npc)
        parts.append(_convert_arc(body).strip())
    return "\n\n".join(parts)


def _encounters_appendix(enc_dir: Path) -> str:
    if not enc_dir.exists():
        return "## Encounters Appendix\n\n*None.*"
    parts = ["## Encounters Appendix"]
    for enc in sorted(enc_dir.glob("*.md")):
        if enc.stem == "wandering-pressure":
            continue
        _, body = _read(enc)
        title = enc.stem.replace("-", " ").title()
        parts.append(f"### {title}\n\n{body.strip()}")
    return "\n\n---\n\n".join(parts)


def _wandering_section(wp: Path) -> str:
    _, body = _read(wp)
    return f"## Wandering Pressure\n\n{body.strip()}"


# ---------------------------------------------------------------------------
# Consistency checker (accepts pre-read room data to avoid re-reading)
# ---------------------------------------------------------------------------

def _check(
    adv_dir: Path,
    room_files: list[Path],
    npc_files: list[Path],
    room_sections: list[dict] | None = None,
) -> list[str]:
    """Run consistency checks. Pass room_sections to avoid re-reading room files."""
    warnings = []
    npc_slugs = {f.stem for f in npc_files}
    enc_dir = adv_dir / "encounters"

    for i, rf in enumerate(room_files):
        # Use pre-read data if available; otherwise read once
        if room_sections and i < len(room_sections):
            secs = room_sections[i]
            # Reconstruct body for encounter ref scanning
            enc_text = secs.get("Encounter", "")
        else:
            _, body = _read(rf)
            secs = _split_h2(body)
            enc_text = secs.get("Encounter", "")

        # Check encounter file refs
        for m in _ENC_REF.finditer(enc_text):
            if enc_dir.exists() and not (enc_dir / m.group(1)).exists():
                warnings.append(f"MISSING: encounters/{m.group(1)} referenced in {rf.name}")

        # Check read-aloud length
        ra = _last_blockquote(secs.get("Read-aloud", ""))
        words = len(ra.split())
        if words > 60:
            warnings.append(f"READ-ALOUD OVER 60 WORDS: Scene {i+1} ({rf.name}) — {words} words")

    # NPC refs in premise
    premise = adv_dir / "premise.md"
    if premise.exists():
        for m in re.finditer(r"`npcs/([^`]+)\.md`", premise.read_text(encoding="utf-8")):
            slug = m.group(1)
            if slug not in npc_slugs and "<" not in slug:  # skip template placeholders
                warnings.append(f"MISSING: npcs/{slug}.md referenced in premise")

    return warnings


# ---------------------------------------------------------------------------
# Main bind function
# ---------------------------------------------------------------------------

def bind(adv_slug: str, force: bool = False) -> Path:
    """Compile adventure directory to module.md. Returns output path."""
    adv_dir = _REPO_ROOT / "adventures" / adv_slug
    if not adv_dir.exists():
        raise FileNotFoundError(f"Adventure directory not found: {adv_dir}")

    # Named file existence checks before any I/O
    premise_path = adv_dir / "premise.md"
    if not premise_path.exists():
        raise FileNotFoundError(f"Missing premise.md in {adv_dir}")
    rooms_dir = adv_dir / "rooms"
    map_path = rooms_dir / "map.md"
    if not map_path.exists():
        raise FileNotFoundError(f"Missing rooms/map.md in {adv_dir}")

    out_path = adv_dir / "module.md"
    if out_path.exists() and not force:
        v = 2
        while (adv_dir / f"module.v{v}.md").exists():
            v += 1
        out_path = adv_dir / f"module.v{v}.md"
        print(f"[module-binder] module.md exists — writing {out_path.name}")

    premise_fm, premise_body = _read(premise_path)

    # Directory listings — guard against missing dirs
    room_files = sorted(rooms_dir.glob("[0-9][0-9]-*.md")) if rooms_dir.exists() else []
    treasures_dir = adv_dir / "treasures"
    treasure_files = (
        sorted(f for f in treasures_dir.glob("*.md") if "-manifest" not in f.name)
        if treasures_dir.exists() else []
    )
    encounters_dir = adv_dir / "encounters"
    npcs_dir = adv_dir / "npcs"
    npc_files = sorted(npcs_dir.glob("*.md")) if npcs_dir.exists() else []

    # Title from slug
    title_words = adv_slug.split("-")[1:]
    title = " ".join(w.capitalize() for w in title_words)

    # Logline from premise
    logline_m = re.search(r"\*\*Logline:\*\*\s*(.+?)$", premise_body, re.MULTILINE)
    logline = logline_m.group(1).strip() if logline_m else ""

    tier = premise_fm.get("tier", 1)
    party = premise_fm.get("party", "4 characters, level 3")

    # Frontmatter
    compiled_from = [str(f.relative_to(_REPO_ROOT)).replace("\\", "/") for f in room_files]
    fm_lines = ["---", f"adventure: {adv_slug}", f"compiled: {date.today().isoformat()}"]
    fm_lines += ["compiled-from:"] + [f"  - {p}" for p in compiled_from]
    fm_lines += ["author: module-binder", "---", ""]
    frontmatter = "\n".join(fm_lines)

    # Background: all narrative H2 sections from premise, excluding technical ones
    premise_secs = _split_h2(premise_body)
    bg_parts = [
        v.strip() for k, v in premise_secs.items()
        if k not in _PREMISE_BG_EXCLUDED and v.strip()
    ]
    background = "## Setting & Background\n\n" + "\n\n".join(bg_parts)

    # Map
    _, map_body = _read(map_path)
    map_section = f"## Map\n\n{map_body.strip()}"

    # Scenes — collect sections for re-use in _check (avoid re-reading)
    all_dc_rows: list[dict] = []
    scene_texts: list[str] = []
    all_room_sections: list[dict] = []
    for i, rf in enumerate(room_files, 1):
        scene_text, dc_rows, secs, _ = _build_scene(i, rf, adv_dir)
        scene_texts.append(scene_text)
        all_dc_rows.extend(dc_rows)
        all_room_sections.append(secs)

    # Assemble
    toc = """\
## Table of Contents

1. Setting & Background
2. Map
3. Scenes
4. Treasures
5. NPCs
6. Encounters Appendix
7. Wandering Pressure
8. DM Cheatsheet"""

    header_block = (
        f"# {title} — DM Module\n\n"
        f"*{logline}*\n\n"
        f"**Tier:** {tier}  |  **Party:** {party}  |  **Expected playtime:** 1 session (3–4 hours)\n\n"
        f"{toc}"
    )

    major: list[str] = [
        frontmatter + header_block,
        background,
        map_section,
        "\n\n---\n\n".join(scene_texts),
        _treasures_section(treasure_files),
        _npcs_section(npc_files),
        _encounters_appendix(encounters_dir),
    ]

    wp = encounters_dir / "wandering-pressure.md"
    if wp.exists():
        major.append(_wandering_section(wp))

    major.append(_cheatsheet(all_dc_rows))

    output = "\n\n---\n\n".join(major)
    out_path.write_text(output, encoding="utf-8")

    # Report
    wc = len(output.split())
    print(f"[module-binder] Written: {out_path.relative_to(_REPO_ROOT)}")
    print(f"[module-binder] {len(room_files)} scenes | {len(treasure_files)} treasures | "
          f"{len(npc_files)} NPCs | {wc:,} words | {len(all_dc_rows)} DCs")

    warnings = _check(adv_dir, room_files, npc_files, room_sections=all_room_sections)
    for w in warnings:
        print(f"[module-binder] WARNING: {w}", file=sys.stderr)
    if not warnings:
        print("[module-binder] No consistency warnings.")

    return out_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    import argparse
    p = argparse.ArgumentParser(description="Compile adventure directory to module.md")
    p.add_argument("adventure", help="Adventure slug, e.g. 0015-the-gatehouse-watch")
    p.add_argument("--force", action="store_true", help="Overwrite existing module.md")
    args = p.parse_args()
    try:
        bind(args.adventure, force=args.force)
        return 0
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
