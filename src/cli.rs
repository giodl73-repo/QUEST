use rally_core::{DiceRoller as RallyDiceRoller, RollKeep};
use serde::{Deserialize, Serialize};
use serde_json::{json, Value};
use std::collections::BTreeMap;
use std::env;
use std::fs;
use std::io::{self, Read};
use std::path::{Path, PathBuf};

const VALID_EVENT_TYPES: &[&str] = &[
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
];

#[derive(Debug, Clone, Serialize, Deserialize)]
struct PcState {
    hp: i32,
    hp_max: i32,
    #[serde(default)]
    spell_slots: BTreeMap<String, i32>,
    #[serde(default)]
    attunements: Vec<String>,
    #[serde(default)]
    lay_on_hands: i32,
    concentration: Option<String>,
    #[serde(default)]
    conditions: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
struct SessionState {
    adventure: String,
    session: String,
    dice_seed: String,
    scene_index: usize,
    #[serde(default)]
    scenes_completed: Vec<usize>,
    pending_checkpoint: Option<String>,
    #[serde(default = "default_party_slug")]
    party_slug: String,
    route: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
struct CampaignFacts {
    #[serde(default)]
    hints: BTreeMap<String, String>,
    #[serde(default)]
    campaign_permanent: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
struct PersistedState {
    party: BTreeMap<String, PcState>,
    session: SessionState,
    campaign: CampaignFacts,
}

#[derive(Debug, Clone)]
struct Pc {
    slug: String,
    ac: i32,
    hp: i32,
    hp_max: i32,
}

#[derive(Debug, Clone)]
struct Scene {
    id: usize,
    name: String,
    read_aloud: String,
    body: String,
    stat_blocks: Vec<StatBlock>,
}

#[derive(Debug, Clone)]
struct StatBlock {
    name: String,
    ac: i32,
    hp: i32,
}

#[derive(Debug, Clone)]
struct Adventure {
    scenes: Vec<Scene>,
    dc_table: Vec<Value>,
}

#[derive(Debug, Clone, Serialize, PartialEq, Eq)]
pub struct RollResult {
    pub expression: String,
    pub rolls: Vec<u32>,
    pub kept: Option<u32>,
    pub mod_value: i32,
    pub bless_roll: Option<u32>,
    pub total: i32,
    pub crit: bool,
    pub fumble: bool,
    pub seed_position: Option<u64>,
    pub scene_id: Option<usize>,
    pub beat_index: Option<usize>,
    pub log_stub: Option<String>,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct RollOptions {
    pub expression: String,
    pub advantage: bool,
    pub disadvantage: bool,
    pub bless: bool,
    pub scene_id: Option<usize>,
    pub beat_index: Option<usize>,
    pub log_stub: Option<String>,
}

fn default_party_slug() -> String {
    "compact-wardens".to_string()
}

pub fn run_cli(args: Vec<String>) -> i32 {
    let Some(command) = args.first().map(String::as_str) else {
        print_usage();
        return 2;
    };
    match command {
        "status" => cmd_status(),
        "start" => cmd_start(&args[1..]),
        "resume" => cmd_resume(),
        "set-route" => cmd_set_route(args.get(1)),
        "roll" => cmd_roll(&args[1..]),
        "bind-module" => cmd_bind_module(&args[1..]),
        "--help" | "-h" => {
            print_usage();
            0
        }
        other => {
            eprintln!("unknown command: {other}");
            print_usage();
            2
        }
    }
}

fn print_usage() {
    eprintln!("usage: quest <status|start|resume|set-route|roll|bind-module> [options]");
}

fn state_dir() -> PathBuf {
    env::var("MARATHON_STATE_DIR")
        .map(PathBuf::from)
        .unwrap_or_else(|_| PathBuf::from("state"))
}

fn session_path() -> PathBuf {
    state_dir().join("session.json")
}

fn checkpoint_path() -> PathBuf {
    state_dir().join("checkpoint.json")
}

fn event_log_path() -> PathBuf {
    state_dir().join("event_log.jsonl")
}

fn dice_log_path() -> PathBuf {
    state_dir().join("dice_log.jsonl")
}

fn read_state() -> Result<Option<PersistedState>, String> {
    let path = session_path();
    if !path.exists() {
        return Ok(None);
    }
    let raw = fs::read_to_string(&path)
        .map_err(|error| format!("failed to read {}: {error}", path.display()))?;
    serde_json::from_str(&raw)
        .map(Some)
        .map_err(|error| format!("corrupted session.json: {error}"))
}

fn write_state(state: &PersistedState) -> Result<(), String> {
    fs::create_dir_all(state_dir())
        .map_err(|error| format!("failed to create state dir: {error}"))?;
    let path = session_path();
    let tmp = path.with_extension("json.tmp");
    let raw = serde_json::to_string_pretty(state).map_err(|error| error.to_string())?;
    fs::write(&tmp, raw).map_err(|error| format!("failed to write {}: {error}", tmp.display()))?;
    fs::rename(&tmp, &path)
        .map_err(|error| format!("failed to replace {}: {error}", path.display()))
}

fn cmd_status() -> i32 {
    let loaded = match read_state() {
        Ok(Some(state)) => state,
        Ok(None) => {
            println!("No active session. Start one with:");
            println!("  quest start --adventure <slug> --session <name>");
            return 0;
        }
        Err(error) => {
            eprintln!("{error}");
            return 1;
        }
    };
    println!("{}", "=".repeat(50));
    println!(
        "SESSION: {} | ADVENTURE: {}",
        loaded.session.session, loaded.session.adventure
    );
    println!(
        "SCENE: index={} | COMPLETED: {:?}",
        loaded.session.scene_index, loaded.session.scenes_completed
    );
    if let Some(route) = &loaded.session.route {
        println!("ROUTE: {route}");
    }
    println!();
    println!("PARTY STATE:");
    for (slug, pc) in &loaded.party {
        let slots = if pc.spell_slots.is_empty() {
            "-".to_string()
        } else {
            pc.spell_slots
                .iter()
                .map(|(key, value)| format!("{key}:{value}"))
                .collect::<Vec<_>>()
                .join(" ")
        };
        let attune = if pc.attunements.is_empty() {
            "-".to_string()
        } else {
            pc.attunements.join(", ")
        };
        let conditions = if pc.conditions.is_empty() {
            "-".to_string()
        } else {
            pc.conditions.join(", ")
        };
        println!(
            "  {slug:<28} HP {}/{}  Slots {}  Attune: {}  Conds: {}",
            pc.hp, pc.hp_max, slots, attune, conditions
        );
    }
    println!();
    if let Some(checkpoint) = read_checkpoint() {
        let beat = checkpoint
            .get("beat_type")
            .and_then(Value::as_str)
            .unwrap_or("unknown");
        let scene = checkpoint
            .get("scene_id")
            .map(Value::to_string)
            .unwrap_or_else(|| "?".to_string());
        println!("PENDING CHECKPOINT: scene_{scene}_{beat}");
        println!("  (resume with: quest resume)");
    } else {
        println!("PENDING CHECKPOINT: none");
    }
    let dice_count = count_jsonl(&dice_log_path());
    println!(
        "DICE LOG: {dice_count} rolls this session (seed: {})",
        loaded.session.dice_seed
    );
    let summary = event_summary();
    if summary.is_empty() {
        println!("EVENT LOG: no events recorded yet");
    } else {
        println!("EVENT LOG:");
        for (event_type, count) in summary {
            println!("  {event_type:<22} {count}");
        }
    }
    println!("{}", "=".repeat(50));
    0
}

fn cmd_start(args: &[String]) -> i32 {
    let Some(adventure_slug) = option_value(args, "--adventure") else {
        eprintln!("missing --adventure");
        return 2;
    };
    let Some(session_name) = option_value(args, "--session") else {
        eprintln!("missing --session");
        return 2;
    };
    let party_slug = option_value(args, "--party").unwrap_or_else(default_party_slug);
    let module_path = Path::new("adventures")
        .join(&adventure_slug)
        .join("module.md");
    let party_dir = Path::new("personas").join("parties").join(&party_slug);
    let adventure = match load_adventure(&module_path) {
        Ok(adventure) => adventure,
        Err(error) => {
            eprintln!("ERROR: {error}");
            return 1;
        }
    };
    let pcs = match load_party(&party_dir) {
        Ok(pcs) => pcs,
        Err(error) => {
            eprintln!("ERROR: {error}");
            return 1;
        }
    };
    let party = pcs
        .iter()
        .map(|pc| {
            (
                pc.slug.clone(),
                PcState {
                    hp: pc.hp,
                    hp_max: pc.hp_max,
                    spell_slots: BTreeMap::new(),
                    attunements: Vec::new(),
                    lay_on_hands: 0,
                    concentration: None,
                    conditions: Vec::new(),
                },
            )
        })
        .collect::<BTreeMap<_, _>>();
    let session = SessionState {
        adventure: adventure_slug.clone(),
        session: session_name.clone(),
        dice_seed: format!("{session_name}-{}", "rust"),
        scene_index: 0,
        scenes_completed: Vec::new(),
        pending_checkpoint: None,
        party_slug: party_slug.clone(),
        route: None,
    };
    let state = PersistedState {
        party,
        session,
        campaign: CampaignFacts {
            hints: BTreeMap::new(),
            campaign_permanent: Vec::new(),
        },
    };
    if let Err(error) = write_state(&state) {
        eprintln!("{error}");
        return 1;
    }
    let _ = fs::remove_file(event_log_path());
    println!(
        "Loaded adventure: {adventure_slug} ({} scenes, {} key DCs)",
        adventure.scenes.len(),
        adventure.dc_table.len()
    );
    for scene in &adventure.scenes {
        println!(
            "  scene {}: {} ({} stat blocks, {} read-aloud chars, {} body chars)",
            scene.id + 1,
            scene.name,
            scene.stat_blocks.len(),
            scene.read_aloud.len(),
            scene.body.len()
        );
        for stat in &scene.stat_blocks {
            println!("    enemy: {} AC {} HP {}", stat.name, stat.ac, stat.hp);
        }
    }
    println!("Loaded party: {party_slug} ({} PCs)", pcs.len());
    for pc in &pcs {
        println!("  pc: {} AC {} HP {}", pc.slug, pc.ac, pc.hp);
    }
    println!("State written to {}", session_path().display());
    println!("Dice log: {}", dice_log_path().display());
    0
}

fn cmd_resume() -> i32 {
    let Some(checkpoint) = read_checkpoint() else {
        println!("No checkpoint found. Use 'start' to begin a new session.");
        return 1;
    };
    let mut state = match read_state() {
        Ok(Some(state)) => state,
        Ok(None) => {
            eprintln!("no active session");
            return 1;
        }
        Err(error) => {
            eprintln!("{error}");
            return 1;
        }
    };
    println!("{}", "=".repeat(50));
    println!(
        "RESUMING: {} | SCENE {} - {}",
        checkpoint
            .get("session")
            .and_then(Value::as_str)
            .unwrap_or("?"),
        checkpoint
            .get("scene_id")
            .map(Value::to_string)
            .unwrap_or_else(|| "?".to_string()),
        checkpoint
            .get("scene_name")
            .and_then(Value::as_str)
            .unwrap_or("?")
    );
    println!(
        "BEAT: {}",
        checkpoint
            .get("beat_type")
            .and_then(Value::as_str)
            .unwrap_or("?")
    );
    println!();
    let mut stdin = String::new();
    if let Err(error) = io::stdin().read_to_string(&mut stdin) {
        eprintln!("failed to read inbound response: {error}");
        return 1;
    }
    let inbound: Value = match serde_json::from_str(stdin.trim()) {
        Ok(value) => value,
        Err(error) => {
            eprintln!("invalid JSON response: {error}");
            return 1;
        }
    };
    if let Err(error) = validate_inbound(&inbound, state.session.scene_index, None, &state.party) {
        eprintln!("{error}");
        return 1;
    }
    let events = inbound
        .pointer("/state_updates/events")
        .and_then(Value::as_array)
        .cloned()
        .unwrap_or_default();
    let logged = log_events(&events);
    if let Some(route) = inbound
        .pointer("/state_updates/route")
        .and_then(Value::as_str)
    {
        state.session.route = Some(route.to_ascii_uppercase());
    }
    if let Some(next) = inbound.get("advance_to_scene").and_then(Value::as_u64) {
        state.session.scene_index = next as usize;
    }
    state.session.pending_checkpoint = None;
    if let Err(error) = write_state(&state) {
        eprintln!("{error}");
        return 1;
    }
    let _ = fs::remove_file(checkpoint_path());
    println!("Inbound response validated.");
    if logged > 0 {
        println!("Events logged: {logged}");
    }
    0
}

fn cmd_set_route(route: Option<&String>) -> i32 {
    let Some(route) = route else {
        eprintln!("missing route");
        return 2;
    };
    let route = route.to_ascii_uppercase();
    if !matches!(route.as_str(), "A" | "B" | "C" | "D" | "E") {
        eprintln!("invalid route: {route}");
        return 2;
    }
    let mut state = match read_state() {
        Ok(Some(state)) => state,
        Ok(None) => {
            eprintln!("no active session");
            return 1;
        }
        Err(error) => {
            eprintln!("{error}");
            return 1;
        }
    };
    state.session.route = Some(route.clone());
    if let Err(error) = write_state(&state) {
        eprintln!("{error}");
        return 1;
    }
    println!("Route set to: {route}");
    0
}

fn cmd_roll(args: &[String]) -> i32 {
    let expression = args.first().map(String::as_str).unwrap_or("1d20");
    let seed = option_value(args, "--seed").unwrap_or_else(|| "quest-roll".to_string());
    let adv = args.iter().any(|arg| arg == "--adv");
    let disadv = args.iter().any(|arg| arg == "--disadv");
    let bless = args.iter().any(|arg| arg == "--bless");
    let mut engine = DiceEngine::new(&seed, Some(dice_log_path()));
    match engine.roll(expression, adv, disadv, bless, None, None, None) {
        Ok(result) => {
            println!(
                "{} => rolls={:?} kept={:?} mod={} bless={:?} total={}",
                result.expression,
                result.rolls,
                result.kept,
                result.mod_value,
                result.bless_roll,
                result.total
            );
            0
        }
        Err(error) => {
            eprintln!("{error}");
            1
        }
    }
}

fn cmd_bind_module(args: &[String]) -> i32 {
    let Some(adventure_slug) = args.first() else {
        eprintln!("missing adventure slug");
        return 2;
    };
    let adv_dir = Path::new("adventures").join(adventure_slug);
    if !adv_dir.exists() {
        eprintln!("Adventure directory not found: {}", adv_dir.display());
        return 1;
    }
    let module = bind_module(&adv_dir, adventure_slug);
    let out = adv_dir.join("module.md");
    if let Err(error) = fs::write(&out, module) {
        eprintln!("failed to write {}: {error}", out.display());
        return 1;
    }
    println!("Wrote {}", out.display());
    0
}

fn option_value(args: &[String], name: &str) -> Option<String> {
    args.windows(2)
        .find(|pair| pair[0] == name)
        .map(|pair| pair[1].clone())
}

fn count_jsonl(path: &Path) -> usize {
    fs::read_to_string(path)
        .map(|raw| raw.lines().filter(|line| !line.trim().is_empty()).count())
        .unwrap_or(0)
}

fn read_checkpoint() -> Option<Value> {
    fs::read_to_string(checkpoint_path())
        .ok()
        .and_then(|raw| serde_json::from_str(&raw).ok())
}

fn validate_inbound(
    raw: &Value,
    current_scene_index: usize,
    max_scene: Option<usize>,
    party: &BTreeMap<String, PcState>,
) -> Result<(), String> {
    let narrative = raw
        .get("narrative")
        .and_then(Value::as_str)
        .ok_or_else(|| "narrative is required".to_string())?;
    if narrative.trim().is_empty() {
        return Err("narrative is empty".to_string());
    }
    let advance = raw
        .get("advance_to_scene")
        .and_then(Value::as_u64)
        .ok_or_else(|| "advance_to_scene is required".to_string())? as usize;
    if advance < current_scene_index {
        return Err("invalid scene advance".to_string());
    }
    if max_scene.is_some_and(|max| advance > max) {
        return Err("advance_to_scene exceeds max scene".to_string());
    }
    if let Some(updates) = raw.get("state_updates").and_then(Value::as_object) {
        for key in updates.keys() {
            if key != "events" && key != "route" && !party.contains_key(key) {
                return Err(format!("unknown key in state_updates: {key}"));
            }
        }
    }
    Ok(())
}

fn log_events(events: &[Value]) -> usize {
    let mut logged = 0;
    for event in events {
        let Some(event_type) = event.get("type").and_then(Value::as_str) else {
            continue;
        };
        if !VALID_EVENT_TYPES.contains(&event_type) {
            continue;
        }
        if let Ok(line) = serde_json::to_string(event) {
            if append_line(&event_log_path(), &line).is_ok() {
                logged += 1;
            }
        }
    }
    logged
}

fn append_line(path: &Path, line: &str) -> Result<(), String> {
    if let Some(parent) = path.parent() {
        fs::create_dir_all(parent).map_err(|error| error.to_string())?;
    }
    use std::io::Write;
    let mut file = fs::OpenOptions::new()
        .create(true)
        .append(true)
        .open(path)
        .map_err(|error| error.to_string())?;
    writeln!(file, "{line}").map_err(|error| error.to_string())
}

fn event_summary() -> BTreeMap<String, usize> {
    let mut summary = BTreeMap::new();
    for event in load_events() {
        if let Some(event_type) = event.get("type").and_then(Value::as_str) {
            *summary.entry(event_type.to_string()).or_insert(0) += 1;
        }
    }
    summary
}

fn load_events() -> Vec<Value> {
    fs::read_to_string(event_log_path())
        .ok()
        .map(|raw| {
            raw.lines()
                .filter_map(|line| serde_json::from_str::<Value>(line).ok())
                .collect()
        })
        .unwrap_or_default()
}

pub struct DiceEngine {
    roller: RallyDiceRoller,
    log_path: Option<PathBuf>,
}

impl DiceEngine {
    pub fn new(seed: &str, log_path: Option<PathBuf>) -> Self {
        Self {
            roller: RallyDiceRoller::new(seed),
            log_path,
        }
    }

    pub fn position(&self) -> u64 {
        self.roller.position()
    }

    pub fn roll_options(&mut self, options: RollOptions) -> Result<RollResult, String> {
        self.roll(
            &options.expression,
            options.advantage,
            options.disadvantage,
            options.bless,
            options.scene_id,
            options.beat_index,
            options.log_stub,
        )
    }

    pub fn roll(
        &mut self,
        expression: &str,
        adv: bool,
        disadv: bool,
        bless: bool,
        scene_id: Option<usize>,
        beat_index: Option<usize>,
        log_stub: Option<String>,
    ) -> Result<RollResult, String> {
        let (count, sides, _) = parse_roll_expression(expression)?;
        let keep = if adv {
            RollKeep::Highest
        } else if disadv {
            RollKeep::Lowest
        } else {
            RollKeep::Sum
        };
        let extra_rolls = u32::from((adv || disadv) && count == 1 && sides == 20);
        let outcome = self.roller.roll_with_extra(expression, keep, extra_rolls)?;
        let bless_roll = if bless {
            Some(self.roller.roll_die_value(4))
        } else {
            None
        };
        let effective_d20 = if sides == 20 && count == 1 {
            outcome.kept.or_else(|| outcome.rolls.first().copied())
        } else {
            None
        };
        let result = RollResult {
            expression: expression.to_string(),
            rolls: outcome.rolls,
            kept: outcome.kept,
            mod_value: outcome.spec.modifier,
            bless_roll,
            total: outcome.total + bless_roll.unwrap_or(0) as i32,
            crit: effective_d20 == Some(20),
            fumble: effective_d20 == Some(1),
            seed_position: Some(outcome.seed_position),
            scene_id,
            beat_index,
            log_stub,
        };
        self.log_roll(&result)?;
        Ok(result)
    }

    fn log_roll(&self, result: &RollResult) -> Result<(), String> {
        let Some(path) = &self.log_path else {
            return Ok(());
        };
        let mut value = serde_json::to_value(result).map_err(|error| error.to_string())?;
        if let Some(object) = value.as_object_mut() {
            if let Some(mod_value) = object.remove("mod_value") {
                object.insert("mod".to_string(), mod_value);
            }
        }
        append_line(
            path,
            &serde_json::to_string(&value).map_err(|error| error.to_string())?,
        )
    }
}

pub fn parse_roll_expression(expression: &str) -> Result<(u32, u32, i32), String> {
    let spec = rally_core::parse_roll_expression(expression)?;
    Ok((spec.count, spec.sides, spec.modifier))
}

fn load_adventure(path: &Path) -> Result<Adventure, String> {
    let raw =
        fs::read_to_string(path).map_err(|_| format!("module not found: {}", path.display()))?;
    let scenes = parse_scenes(&raw);
    let dc_table = parse_dc_table(&raw);
    Ok(Adventure { scenes, dc_table })
}

fn parse_scenes(raw: &str) -> Vec<Scene> {
    let mut starts = raw
        .lines()
        .enumerate()
        .filter_map(|(idx, line)| {
            line.strip_prefix("### Scene ")
                .map(|rest| (idx, rest.to_string()))
        })
        .collect::<Vec<_>>();
    let lines = raw.lines().collect::<Vec<_>>();
    let mut scenes = Vec::new();
    for pos in 0..starts.len() {
        let (line_idx, title) = starts[pos].clone();
        let end = starts
            .get(pos + 1)
            .map(|(idx, _)| *idx)
            .unwrap_or(lines.len());
        let body = lines[line_idx + 1..end].join("\n");
        let id = title
            .split_whitespace()
            .next()
            .and_then(|num| num.parse::<usize>().ok())
            .unwrap_or(pos + 1)
            .saturating_sub(1);
        let name = title
            .split_once('—')
            .map(|(_, name)| name.trim().to_string())
            .unwrap_or_else(|| title.trim().to_string());
        let read_aloud = last_blockquote(&body);
        let stat_blocks = parse_stat_blocks(&body);
        scenes.push(Scene {
            id,
            name,
            read_aloud,
            body,
            stat_blocks,
        });
    }
    starts.clear();
    scenes
}

fn last_blockquote(text: &str) -> String {
    let mut current = Vec::new();
    let mut last = Vec::new();
    for line in text.lines() {
        if let Some(stripped) = line.trim_start().strip_prefix('>') {
            current.push(stripped.trim_start().to_string());
        } else if !current.is_empty() {
            last = current;
            current = Vec::new();
        }
    }
    if !current.is_empty() {
        last = current;
    }
    last.join("\n")
}

fn parse_stat_blocks(text: &str) -> Vec<StatBlock> {
    text.lines()
        .filter_map(|line| {
            if !line.contains("**AC**") || !line.contains("**HP**") {
                return None;
            }
            let clean = line.trim_start_matches('>').trim();
            let name = clean
                .strip_prefix("**")
                .and_then(|rest| rest.split("—").next())
                .unwrap_or("Unknown")
                .trim()
                .trim_matches('*')
                .to_string();
            let ac = number_after(clean, "**AC**")?;
            let hp = number_after(clean, "**HP**")?;
            Some(StatBlock { name, ac, hp })
        })
        .collect()
}

fn number_after(text: &str, marker: &str) -> Option<i32> {
    let after = text.split_once(marker)?.1.trim();
    after
        .split(|ch: char| !ch.is_ascii_digit())
        .find(|part| !part.is_empty())?
        .parse()
        .ok()
}

fn parse_dc_table(raw: &str) -> Vec<Value> {
    raw.lines()
        .filter(|line| line.trim_start().starts_with('|'))
        .filter_map(|line| {
            let cells = line
                .trim()
                .trim_matches('|')
                .split('|')
                .map(str::trim)
                .collect::<Vec<_>>();
            if cells.len() != 4 || cells[0] == "DC" || cells[0].starts_with("---") {
                return None;
            }
            let dc = cells[0].parse::<u64>().ok()?;
            let scene = cells[2].parse::<u64>().ok()?;
            Some(json!({
                "dc": dc,
                "check": cells[1],
                "scene": scene,
                "consequence": cells[3],
            }))
        })
        .collect()
}

fn load_party(path: &Path) -> Result<Vec<Pc>, String> {
    if !path.exists() {
        return Err(format!("party path not found: {}", path.display()));
    }
    let files = if path.is_file() {
        vec![path.to_path_buf()]
    } else {
        fs::read_dir(path)
            .map_err(|error| error.to_string())?
            .filter_map(Result::ok)
            .map(|entry| entry.path())
            .filter(|path| path.extension().is_some_and(|ext| ext == "md"))
            .collect::<Vec<_>>()
    };
    let mut pcs = Vec::new();
    for file in files {
        let raw = fs::read_to_string(&file).map_err(|error| error.to_string())?;
        if file
            .file_name()
            .and_then(|name| name.to_str())
            .is_some_and(|name| {
                name.eq_ignore_ascii_case("README.md") || name.eq_ignore_ascii_case("shared-log.md")
            })
            || !raw.contains("pc:")
        {
            continue;
        }
        if !raw.contains("heuristics:") {
            return Err(format!("No heuristics block in {}", file.display()));
        }
        let slug = frontmatter_value(&raw, "pc").unwrap_or_else(|| {
            file.file_stem()
                .unwrap_or_default()
                .to_string_lossy()
                .to_string()
        });
        let ac = number_after(&raw, "**AC**").unwrap_or(10);
        let hp = number_after(&raw, "**HP**").unwrap_or(10);
        pcs.push(Pc {
            slug,
            ac,
            hp,
            hp_max: hp,
        });
    }
    if pcs.is_empty() {
        return Err(format!(
            "no playable PC markdown files found in {}",
            path.display()
        ));
    }
    Ok(pcs)
}

fn frontmatter_value(raw: &str, key: &str) -> Option<String> {
    raw.lines().find_map(|line| {
        line.split_once(':').and_then(|(left, right)| {
            if left.trim() == key {
                Some(right.trim().trim_matches('"').to_string())
            } else {
                None
            }
        })
    })
}

fn bind_module(adv_dir: &Path, slug: &str) -> String {
    let mut out = format!(
        "---\nadventure: {slug}\n---\n\n# {} — DM Module\n\n## Summary\n\n",
        title_case(slug)
    );
    let premise = adv_dir.join("premise.md");
    if let Ok(raw) = fs::read_to_string(&premise) {
        out.push_str(strip_frontmatter(&raw).trim());
    } else {
        out.push_str("Compiled QUEST module.");
    }
    let room_dir = adv_dir.join("rooms");
    let mut dc_rows = Vec::new();
    for (scene, path) in module_room_paths(&room_dir).into_iter().enumerate() {
        if let Ok(raw) = fs::read_to_string(&path) {
            out.push_str("\n\n---\n\n");
            out.push_str(&format!(
                "### Scene {} — {}\n\n",
                scene + 1,
                room_title(&raw, &path)
            ));
            out.push_str(strip_frontmatter(&raw).trim());
            dc_rows.extend(extract_dcs(&raw, scene + 1));
        }
    }
    let map = room_dir.join("map.md");
    if let Ok(raw) = fs::read_to_string(&map) {
        out.push_str("\n\n---\n\n## Map\n\n");
        out.push_str(demote_headings(strip_frontmatter(&raw).trim(), 3).trim());
    }
    out.push_str("\n\n---\n\n## DM Cheatsheet\n\n### Quick Reference — Key DCs (by scene)\n\n");
    out.push_str(&dc_table(&dc_rows));
    out.push('\n');
    out
}

fn module_room_paths(room_dir: &Path) -> Vec<PathBuf> {
    let mut paths = fs::read_dir(room_dir)
        .map(|entries| {
            entries
                .filter_map(Result::ok)
                .map(|entry| entry.path())
                .filter(|path| {
                    path.extension().is_some_and(|ext| ext == "md")
                        && path.file_name().is_some_and(|name| name != "map.md")
                })
                .collect::<Vec<_>>()
        })
        .unwrap_or_default();
    paths.sort_by(|left, right| {
        let left_key = room_sort_key(left);
        let right_key = room_sort_key(right);
        left_key.cmp(&right_key)
    });
    paths
}

fn room_sort_key(path: &Path) -> (u32, String) {
    let stem = path
        .file_stem()
        .unwrap_or_default()
        .to_string_lossy()
        .to_string();
    let numeric_prefix = stem
        .split_once('-')
        .and_then(|(prefix, _)| prefix.parse::<u32>().ok())
        .unwrap_or(u32::MAX);
    (numeric_prefix, stem)
}

fn demote_headings(raw: &str, levels: usize) -> String {
    raw.lines()
        .map(|line| {
            if line.starts_with('#') {
                let hashes = line.chars().take_while(|ch| *ch == '#').count();
                if line.chars().nth(hashes) == Some(' ') {
                    return format!("{}{}", "#".repeat(levels), line);
                }
            }
            line.to_string()
        })
        .collect::<Vec<_>>()
        .join("\n")
}

fn strip_frontmatter(raw: &str) -> &str {
    if let Some(rest) = raw.strip_prefix("---") {
        if let Some((_, body)) = rest.split_once("---") {
            return body;
        }
    }
    raw
}

fn room_title(raw: &str, path: &Path) -> String {
    raw.lines()
        .find_map(|line| {
            line.strip_prefix("# Room ")
                .or_else(|| line.strip_prefix("# Scene "))
                .and_then(|rest| {
                    rest.split_once('—')
                        .map(|(_, title)| title.trim().to_string())
                })
        })
        .unwrap_or_else(|| {
            path.file_stem()
                .unwrap_or_default()
                .to_string_lossy()
                .to_string()
        })
}

fn extract_dcs(raw: &str, scene: usize) -> Vec<Value> {
    let mut rows = Vec::new();
    for line in raw.lines() {
        if line.contains('|') || line.contains('×') || !line.contains("DC ") {
            continue;
        }
        let Some((before, after)) = line.split_once("DC ") else {
            continue;
        };
        let Some(dc) = after
            .split(|ch: char| !ch.is_ascii_digit())
            .next()
            .and_then(|value| value.parse::<u64>().ok())
        else {
            continue;
        };
        let check = compact_check(before);
        if check.is_empty() {
            continue;
        }
        let consequence = after
            .find(|ch: char| matches!(ch, '.' | ';' | ')' | ']'))
            .map(|idx| &after[..=idx])
            .unwrap_or(after)
            .trim();
        let consequence = compact_consequence(consequence);
        if consequence.is_empty() || consequence.chars().all(|ch| !ch.is_alphanumeric()) {
            continue;
        }
        rows.push(json!({
            "dc": dc,
            "check": check,
            "scene": scene,
            "consequence": consequence,
        }));
    }
    rows
}

fn dc_table(rows: &[Value]) -> String {
    let mut out = String::from("| DC | Check | Scene | Consequence |\n|---|---|---|---|\n");
    if rows.is_empty() {
        out.push_str("| - | - | - | - |");
        return out;
    }
    for row in rows {
        out.push_str(&format!(
            "| {} | {} | {} | {} |\n",
            row["dc"],
            row["check"].as_str().unwrap_or(""),
            row["scene"],
            row["consequence"].as_str().unwrap_or("")
        ));
    }
    out
}

fn sanitize_table_cell(value: &str) -> String {
    value
        .replace('|', "/")
        .replace('🎲', "")
        .replace('\n', " ")
        .replace("**", "")
        .split_whitespace()
        .collect::<Vec<_>>()
        .join(" ")
}

fn compact_check(value: &str) -> String {
    let cleaned = sanitize_table_cell(value)
        .trim_start_matches('-')
        .trim_start_matches('*')
        .trim_start_matches('>')
        .trim()
        .trim_end_matches(':')
        .trim()
        .to_string();
    let segment = cleaned
        .rsplit_once('.')
        .map(|(_, right)| right)
        .unwrap_or(&cleaned)
        .trim();
    let segment = segment
        .rsplit_once(':')
        .map(|(_, right)| right)
        .unwrap_or(segment)
        .trim();
    let segment = segment
        .rsplit_once(')')
        .map(|(_, right)| right)
        .unwrap_or(segment)
        .trim();
    let segment = segment
        .rsplit_once('(')
        .map(|(_, right)| right)
        .unwrap_or(segment)
        .trim();
    sanitize_table_cell(segment)
}

fn compact_consequence(value: &str) -> String {
    let cleaned = sanitize_table_cell(value);
    cleaned
        .trim_start_matches(|ch: char| ch.is_ascii_digit() || ch.is_whitespace())
        .trim_start_matches(':')
        .trim()
        .to_string()
}

fn title_case(slug: &str) -> String {
    slug.split('-')
        .map(|part| {
            let mut chars = part.chars();
            match chars.next() {
                Some(first) => format!("{}{}", first.to_ascii_uppercase(), chars.as_str()),
                None => String::new(),
            }
        })
        .collect::<Vec<_>>()
        .join(" ")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn roll_parser_handles_modifier() {
        assert_eq!(parse_roll_expression("1d20+3").unwrap(), (1, 20, 3));
        assert_eq!(parse_roll_expression("2d6-1").unwrap(), (2, 6, -1));
        assert!(parse_roll_expression("1d20+").is_err());
    }

    #[test]
    fn dice_rolls_are_seeded_and_logged_shape_is_json() {
        let mut left = DiceEngine::new("seed", None);
        let mut right = DiceEngine::new("seed", None);
        let l = left
            .roll("1d20+2", true, false, true, Some(1), Some(0), None)
            .unwrap();
        let r = right
            .roll("1d20+2", true, false, true, Some(1), Some(0), None)
            .unwrap();
        assert_eq!(l.rolls, r.rolls);
        assert_eq!(l.total, r.total);
        assert_eq!(l.seed_position, Some(0));
    }

    #[test]
    fn dice_engine_supports_public_roll_options() {
        let mut engine = DiceEngine::new("library-seed", None);
        let result = engine
            .roll_options(RollOptions {
                expression: "1d20+2".to_string(),
                advantage: true,
                disadvantage: false,
                bless: true,
                scene_id: Some(3),
                beat_index: Some(1),
                log_stub: Some("library-call".to_string()),
            })
            .expect("library roll succeeds");

        assert_eq!(result.expression, "1d20+2");
        assert_eq!(result.scene_id, Some(3));
        assert_eq!(result.beat_index, Some(1));
        assert_eq!(result.log_stub.as_deref(), Some("library-call"));
        assert_eq!(result.seed_position, Some(0));
        assert_eq!(engine.position(), 1);
    }

    #[test]
    fn validation_rejects_unknown_pc_but_accepts_events_and_route() {
        let mut party = BTreeMap::new();
        party.insert(
            "aelric".to_string(),
            PcState {
                hp: 1,
                hp_max: 1,
                spell_slots: BTreeMap::new(),
                attunements: Vec::new(),
                lay_on_hands: 0,
                concentration: None,
                conditions: Vec::new(),
            },
        );
        assert!(validate_inbound(
            &json!({"narrative":"x","state_updates":{"events":[],"route":"D"},"advance_to_scene":1}),
            0,
            None,
            &party
        )
        .is_ok());
        assert!(validate_inbound(
            &json!({"narrative":"x","state_updates":{"pella":{"hp":1}},"advance_to_scene":1}),
            0,
            None,
            &party
        )
        .is_err());
    }

    #[test]
    fn parses_fixture_like_module() {
        let raw = "### Scene 1 — The Arrival\n\n> You arrive.\n\n- Door DC 10 Investigation.\n\n### Scene 2 — The Vault\n\n> Vault.\n\n> **Test Guard — CR 1.** **AC** 14 · **HP** 22";
        let scenes = parse_scenes(raw);
        assert_eq!(scenes.len(), 2);
        assert_eq!(scenes[0].name, "The Arrival");
        assert_eq!(scenes[1].stat_blocks[0].name, "Test Guard");
    }

    #[test]
    fn module_binder_orders_numbered_rooms_and_keeps_map_out_of_scene_count() {
        let root = env::temp_dir().join(format!("quest-bind-module-test-{}", std::process::id()));
        let adv_dir = root.join("adventures").join("0007-test");
        let rooms_dir = adv_dir.join("rooms");
        let _ = fs::remove_dir_all(&root);
        fs::create_dir_all(&rooms_dir).unwrap();
        fs::write(
            adv_dir.join("premise.md"),
            "---\nadventure: test\n---\n\n# Premise\n\nSummary.",
        )
        .unwrap();
        fs::write(
            rooms_dir.join("02-second.md"),
            "---\nadventure: test\n---\n\n# Scene 02 — Second\n\n- Door DC 12 Investigation to open safely.",
        )
        .unwrap();
        fs::write(
            rooms_dir.join("01-first.md"),
            "---\nadventure: test\n---\n\n# Scene 01 — First\n\n- Trap DC 10 Dexterity; failure costs time.",
        )
        .unwrap();
        fs::write(
            rooms_dir.join("map.md"),
            "---\nadventure: test\n---\n\n# Map\n\n| A | B |\n|---|---|\n| x | y |",
        )
        .unwrap();

        let module = bind_module(&adv_dir, "0007-test");

        assert!(module.contains("### Scene 1 — First"));
        assert!(module.contains("### Scene 2 — Second"));
        assert!(!module.contains("### Scene 3 — map"));
        assert!(module.contains("## Map"));
        assert!(module.contains("| 10 | Trap | 1 | Dexterity; |"));
        assert!(module.contains("| 12 | Door | 2 | Investigation to open safely. |"));

        let _ = fs::remove_dir_all(&root);
    }
}
