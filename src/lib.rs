use std::collections::HashMap;

use muddle_core::{
    MuddleCommand, MuddleCommandHint, MuddleCommandOutcome, MuddleError, MuddleExit, MuddleHost,
    MuddleInventoryItem, MuddleResource, MuddleRoom,
};

pub mod cli;

pub use cli::{parse_roll_expression, run_cli, DiceEngine, RollOptions, RollResult};

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct QuestMuddleSurface {
    pub host_name: &'static str,
    pub title: &'static str,
    pub start_room: &'static str,
    pub rooms: Vec<QuestMuddleRoom>,
    pub commands: Vec<QuestMuddleCommand>,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct QuestMuddleRoom {
    pub id: &'static str,
    pub title: &'static str,
    pub description: &'static str,
    pub exits: Vec<QuestMuddleExit>,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct QuestMuddleExit {
    pub command: &'static str,
    pub target_room: &'static str,
    pub label: &'static str,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct QuestMuddleCommand {
    pub room_id: &'static str,
    pub command: &'static str,
    pub description: &'static str,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct QuestAiDmMuddleHost {
    rooms: HashMap<String, MuddleRoom>,
    commands: Vec<QuestMuddleCommand>,
    state: QuestAiDmState,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct QuestAiDmState {
    pub scene: u32,
    pub party_hp: i32,
    pub party_focus: i32,
    pub threat: u32,
    pub treasure_sealed: bool,
    pub last_dm_move: String,
}

pub fn ai_dm_muddle_surface() -> QuestMuddleSurface {
    QuestMuddleSurface {
        host_name: "quest-ai-dm",
        title: "QUEST AI DM Table",
        start_room: "table",
        rooms: vec![
            QuestMuddleRoom {
                id: "table",
                title: "Session Table",
                description: "A solo D&D workshop table where the AI DM runs scene pressure.",
                exits: vec![QuestMuddleExit {
                    command: "go scene",
                    target_room: "scene",
                    label: "Active Scene",
                }],
            },
            QuestMuddleRoom {
                id: "scene",
                title: "Active Scene",
                description:
                    "Scout the room, advance the fiction, and let the AI DM answer with pressure.",
                exits: vec![
                    QuestMuddleExit {
                        command: "go table",
                        target_room: "table",
                        label: "Session Table",
                    },
                    QuestMuddleExit {
                        command: "go encounter",
                        target_room: "encounter",
                        label: "Encounter",
                    },
                ],
            },
            QuestMuddleRoom {
                id: "encounter",
                title: "Encounter",
                description: "Resolve AI DM opposition without faking dice or hiding state.",
                exits: vec![
                    QuestMuddleExit {
                        command: "go scene",
                        target_room: "scene",
                        label: "Active Scene",
                    },
                    QuestMuddleExit {
                        command: "go treasure",
                        target_room: "treasure",
                        label: "Treasure",
                    },
                ],
            },
            QuestMuddleRoom {
                id: "treasure",
                title: "Treasure Decision",
                description: "The treasure is the story: choose whether to unseal the consequence.",
                exits: vec![QuestMuddleExit {
                    command: "go table",
                    target_room: "table",
                    label: "Session Table",
                }],
            },
        ],
        commands: vec![
            QuestMuddleCommand {
                room_id: "table",
                command: "status",
                description: "Show the current AI DM table state.",
            },
            QuestMuddleCommand {
                room_id: "scene",
                command: "scout room",
                description: "Spend focus to lower immediate threat.",
            },
            QuestMuddleCommand {
                room_id: "scene",
                command: "advance scene",
                description: "Move to the next scene beat and raise pressure.",
            },
            QuestMuddleCommand {
                room_id: "encounter",
                command: "enemy turn",
                description: "Let the deterministic AI DM take an opposition turn.",
            },
            QuestMuddleCommand {
                room_id: "encounter",
                command: "rally party",
                description: "Recover focus before the next AI DM move.",
            },
            QuestMuddleCommand {
                room_id: "treasure",
                command: "unseal treasure",
                description: "Accept the treasure and its consequence.",
            },
        ],
    }
}

pub fn ai_dm_muddle_host() -> QuestAiDmMuddleHost {
    QuestAiDmMuddleHost::new(ai_dm_muddle_surface())
}

impl QuestAiDmMuddleHost {
    pub fn new(surface: QuestMuddleSurface) -> Self {
        let rooms = surface
            .rooms
            .into_iter()
            .map(|room| {
                (
                    room.id.to_string(),
                    MuddleRoom {
                        id: room.id.to_string(),
                        title: room.title.to_string(),
                        description: room.description.to_string(),
                        exits: room
                            .exits
                            .into_iter()
                            .map(|exit| MuddleExit {
                                command: exit.command.to_string(),
                                target_room: exit.target_room.to_string(),
                                label: exit.label.to_string(),
                            })
                            .collect(),
                    },
                )
            })
            .collect();

        Self {
            rooms,
            commands: surface.commands,
            state: QuestAiDmState {
                scene: 1,
                party_hp: 24,
                party_focus: 3,
                threat: 1,
                treasure_sealed: true,
                last_dm_move: "AI DM frames the first room and waits for a scout.".to_string(),
            },
        }
    }

    pub fn state(&self) -> &QuestAiDmState {
        &self.state
    }

    fn look(&self, room_id: &str) -> Result<MuddleCommandOutcome, MuddleError> {
        let room = self
            .room(room_id)
            .ok_or_else(|| MuddleError::RoomNotFound {
                room_id: room_id.to_string(),
            })?;
        Ok(MuddleCommandOutcome::stay(format!(
            "{}\n| quest: scene={} hp={} focus={} threat={} treasure={} dm={}",
            room.ascii_card(),
            self.state.scene,
            self.state.party_hp,
            self.state.party_focus,
            self.state.threat,
            if self.state.treasure_sealed {
                "sealed"
            } else {
                "claimed"
            },
            self.state.last_dm_move
        )))
    }

    fn enemy_turn(&mut self) -> String {
        if self.state.threat >= 3 {
            self.state.party_hp = (self.state.party_hp - 5).max(0);
            self.state.threat = 1;
            self.state.last_dm_move =
                "AI DM spends built threat: the wardens take 5 damage and the room resets."
                    .to_string();
            return self.state.last_dm_move.clone();
        }

        self.state.party_focus = (self.state.party_focus - 1).max(0);
        self.state.threat += 1;
        self.state.last_dm_move =
            "AI DM escalates the scene clock and pressures party focus.".to_string();
        self.state.last_dm_move.clone()
    }
}

impl MuddleHost for QuestAiDmMuddleHost {
    fn start_room(&self) -> &str {
        "table"
    }

    fn room(&self, room_id: &str) -> Option<&MuddleRoom> {
        self.rooms.get(room_id)
    }

    fn resource_panel(&self) -> Vec<MuddleResource> {
        vec![
            MuddleResource {
                label: "scene".to_string(),
                value: self.state.scene.to_string(),
            },
            MuddleResource {
                label: "hp".to_string(),
                value: self.state.party_hp.to_string(),
            },
            MuddleResource {
                label: "focus".to_string(),
                value: self.state.party_focus.to_string(),
            },
            MuddleResource {
                label: "threat".to_string(),
                value: self.state.threat.to_string(),
            },
        ]
    }

    fn inventory_panel(&self) -> Vec<MuddleInventoryItem> {
        vec![
            MuddleInventoryItem {
                label: "party sheet".to_string(),
                detail: format!(
                    "hp={} focus={}",
                    self.state.party_hp, self.state.party_focus
                ),
            },
            MuddleInventoryItem {
                label: "treasure".to_string(),
                detail: if self.state.treasure_sealed {
                    "silver oath still sealed".to_string()
                } else {
                    "silver oath claimed; consequence logged".to_string()
                },
            },
            MuddleInventoryItem {
                label: "ai dm move".to_string(),
                detail: self.state.last_dm_move.clone(),
            },
        ]
    }

    fn map_panel(&self, current_room: &str) -> Option<String> {
        Some(format!(
            "[table] -> [scene] -> [encounter] -> [treasure] | current={current_room}"
        ))
    }

    fn objective_panel(&self, current_room: &str) -> Vec<String> {
        match current_room {
            "table" => vec!["Go scene to begin the AI DM table loop.".to_string()],
            "scene" => vec![
                "Scout before advancing if focus is available.".to_string(),
                "Advance scene to put pressure in front of the party.".to_string(),
            ],
            "encounter" => vec![
                "Use enemy turn to let the AI DM oppose the party.".to_string(),
                "Rally party when focus is low.".to_string(),
            ],
            "treasure" => vec!["Unseal treasure only when accepting consequence.".to_string()],
            _ => Vec::new(),
        }
    }

    fn command_panel(&self, current_room: &str) -> Vec<MuddleCommandHint> {
        self.commands
            .iter()
            .filter(|command| command.room_id == current_room)
            .map(|command| MuddleCommandHint {
                command: command.command.to_string(),
                description: command.description.to_string(),
            })
            .collect()
    }

    fn handle_command(
        &mut self,
        room_id: &str,
        command: &MuddleCommand,
    ) -> Result<MuddleCommandOutcome, MuddleError> {
        let normalized = command.normalized();
        if normalized == "look" || normalized == "status" {
            return self.look(room_id);
        }

        match (room_id, normalized.as_str()) {
            ("table", "go scene") => Ok(MuddleCommandOutcome::move_to(
                "The table opens on the active scene.",
                "scene",
            )),
            ("scene", "go table") => Ok(MuddleCommandOutcome::move_to(
                "You return to the session table.",
                "table",
            )),
            ("scene", "go encounter") => Ok(MuddleCommandOutcome::move_to(
                "You step into the encounter frame.",
                "encounter",
            )),
            ("encounter", "go scene") => Ok(MuddleCommandOutcome::move_to(
                "You pull back to the active scene.",
                "scene",
            )),
            ("encounter", "go treasure") => Ok(MuddleCommandOutcome::move_to(
                "You move to the treasure decision.",
                "treasure",
            )),
            ("treasure", "go table") => Ok(MuddleCommandOutcome::move_to(
                "You return to the session table with the consequence in view.",
                "table",
            )),
            ("scene", "scout room") => {
                if self.state.party_focus > 0 {
                    self.state.party_focus -= 1;
                    self.state.threat = self.state.threat.saturating_sub(1).max(1);
                    Ok(MuddleCommandOutcome::stay(
                        "The party scouts carefully. Focus drops by 1 and threat is held.",
                    ))
                } else {
                    self.state.threat += 1;
                    Ok(MuddleCommandOutcome::stay(
                        "No focus remains for scouting. The AI DM advances threat.",
                    ))
                }
            }
            ("scene", "advance scene") => {
                self.state.scene += 1;
                self.state.threat += 1;
                self.state.last_dm_move =
                    "AI DM reveals a harder scene beat and raises threat.".to_string();
                Ok(MuddleCommandOutcome::move_to(
                    "Scene advances. The next beat creates encounter pressure.",
                    "encounter",
                ))
            }
            ("encounter", "enemy turn") => {
                let dm_move = self.enemy_turn();
                Ok(MuddleCommandOutcome::stay(format!("Enemy turn. {dm_move}")))
            }
            ("encounter", "rally party") => {
                self.state.party_focus += 1;
                Ok(MuddleCommandOutcome::stay(
                    "The party rallies around the table plan and recovers 1 focus.",
                ))
            }
            ("treasure", "unseal treasure") => {
                self.state.treasure_sealed = false;
                self.state.threat += 1;
                Ok(MuddleCommandOutcome::stay(
                    "The silver oath is claimed. Treasure enters the story and threat rises.",
                ))
            }
            _ => Err(MuddleError::UnknownCommand {
                room_id: room_id.to_string(),
                command: command.clone(),
            }),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn ai_dm_enemy_turn_spends_armed_threat() {
        let mut host = ai_dm_muddle_host();

        host.handle_command("scene", &MuddleCommand::parse("advance scene"))
            .expect("advance succeeds");
        host.handle_command("encounter", &MuddleCommand::parse("enemy turn"))
            .expect("first enemy turn succeeds");
        let outcome = host
            .handle_command("encounter", &MuddleCommand::parse("enemy turn"))
            .expect("second enemy turn succeeds");

        assert!(outcome.response.contains("wardens take 5 damage"));
        assert_eq!(host.state().party_hp, 19);
        assert_eq!(host.state().threat, 1);
    }

    #[test]
    fn treasure_unseal_changes_inventory_state() {
        let mut host = ai_dm_muddle_host();

        host.handle_command("treasure", &MuddleCommand::parse("unseal treasure"))
            .expect("unseal succeeds");

        assert!(!host.state().treasure_sealed);
        assert!(host
            .inventory_panel()
            .iter()
            .any(|item| item.detail.contains("claimed")));
    }

    #[test]
    fn scene_exit_moves_to_encounter() {
        let mut host = ai_dm_muddle_host();

        let outcome = host
            .handle_command("scene", &MuddleCommand::parse("go encounter"))
            .expect("exit succeeds");

        assert_eq!(outcome.next_room, Some("encounter".to_string()));
    }
}
