from __future__ import annotations
import json
from pathlib import Path
from datetime import date
from scripts.engine.event_log import EventLogger


class LogWriter:
    def __init__(
        self,
        adventure_slug: str,
        session: dict,
        party_start: dict,
        party_end: dict,
        narratives: dict[str, str],
        dice_log_path: Path,
        output_dir: Path,
        party_slug: str = "compact-wardens",
        duration: str = "",
        outcome: str = "",
        rubric_version: str = "v1.5",
        innovations_flagged: list[str] | None = None,
        event_log_path: Path | None = None,
    ) -> None:
        self._slug = adventure_slug
        self._session = session
        self._party_start = party_start
        self._party_end = party_end
        self._narratives = narratives
        self._dice_log_path = dice_log_path
        self._output_dir = output_dir
        self._party_slug = party_slug
        self._duration = duration
        self._outcome = outcome
        self._rubric_version = rubric_version
        self._innovations = innovations_flagged or []
        self._event_log_path = event_log_path

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
        suffix = " CRIT" if entry.get("crit") else (" FUMBLE" if entry.get("fumble") else "")
        return (
            f"**🎲 {pc} {label}** — `{entry['expression']}` "
            f"→ rolls={rolls_str} mod={mod:+d} **total={total}{suffix}**"
        )

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
            f"party: {self._party_slug}",
            f"date: {date.today().isoformat()}",
            f"dice-seed: {s['dice_seed']}",
            f"duration: {self._duration}",
            f"outcome: {self._outcome}",
            f"rubric-version: {self._rubric_version}",
            "author: session-runner",
            "---",
            "",
            f"# {session_name} LOG — {self._slug}",
            "",
        ]

        summary = s.get("summary", "")
        lines += ["## Session Summary", "", summary or "(no summary provided)", ""]

        lines += ["## Party state (delta)", ""]
        lines += ["| PC | HP start → end | Spells used | Attune | Notable |",
                  "|---|---|---|---|---|"]
        for slug, end in self._party_end.items():
            start = self._party_start.get(slug, end)
            hp_start = start.get("hp_start", start.get("hp_max", "?"))
            hp_end = end["hp"]
            attunes = ", ".join(end.get("attunements", [])) or "—"
            lines.append(f"| {slug} | {hp_start} → {hp_end} | — | {attunes} | — |")
        lines.append("")

        lines += ["## Scenes", ""]
        for scene_id_str, narrative in sorted(
            self._narratives.items(), key=lambda x: int(x[0])
        ):
            text = narrative
            for stub, formatted in stub_map.items():
                text = text.replace(stub, formatted)
            lines += [f"### Scene {scene_id_str}", "", text, "---", ""]

        lines += ["## Curse symptoms landed", "", "(none recorded)", ""]
        lines += ["## Player-style surprises", "", "(none recorded)", ""]

        # Event log summary
        if self._event_log_path:
            el = EventLogger(self._event_log_path)
            spells = el.spells_table()
            features = el.features_table()
            near_deaths = el.near_death_events()
            summary = el.summary()

            lines += ["## Mechanical events", ""]
            if summary:
                lines += ["### By type", ""]
                lines += ["| Type | Count |", "|---|---:|"]
                for etype, count in sorted(summary.items()):
                    lines.append(f"| {etype} | {count} |")
                lines.append("")

            if spells:
                lines += ["### Spells cast", ""]
                lines += ["| PC | Spell | Level | Scene | Context |", "|---|---|---|---|---|"]
                for s in spells:
                    pc = s.get("pc", "?")
                    spell = s.get("spell", "?")
                    level = s.get("level", "?")
                    scene = s.get("scene", "?")
                    ctx = s.get("context", "—")
                    lines.append(f"| {pc} | {spell} | {level} | {scene} | {ctx} |")
                lines.append("")

            if features:
                lines += ["### Class features used", ""]
                lines += ["| PC | Feature | Scene | Result |", "|---|---|---|---|"]
                for f in features:
                    pc = f.get("pc", "?")
                    feat = f.get("feature", "?")
                    scene = f.get("scene", "?")
                    result = f.get("result", "—")
                    lines.append(f"| {pc} | {feat} | {scene} | {result} |")
                lines.append("")

            if near_deaths:
                lines += ["### Near-death events", ""]
                for nd in near_deaths:
                    pc = nd.get("pc", "?")
                    cause = nd.get("cause", "?")
                    scene = nd.get("scene", "?")
                    lines.append(f"- **{pc}** at scene {scene}: {cause}")
                lines.append("")
            elif not summary:
                lines += ["*(no events logged — include `events` in state_updates)*", ""]

        lines += ["## Open threads for next session", "", "(none recorded)", ""]

        output = self._output_dir / f"{session_name}-log.md"
        tmp = output.with_suffix(".md.tmp")
        tmp.write_text("\n".join(lines), encoding="utf-8")
        tmp.replace(output)
        return output
