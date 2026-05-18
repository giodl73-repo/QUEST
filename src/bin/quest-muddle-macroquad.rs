use macroquad::prelude::*;
use muddle_core::MuddleClientHostRegistration;
use muddle_macroquad::{
    apply_default_macroquad_paths, macroquad_usage, macroquad_window_conf,
    parse_macroquad_run_options, run_muddle_macroquad_hosts, MuddleMacroquadRunConfig,
};
use quest::ai_dm_muddle_host;

const HOST_NAME: &str = "quest-ai-dm";

fn window_conf() -> Conf {
    macroquad_window_conf("QUEST AI DM")
}

#[macroquad::main(window_conf)]
async fn main() {
    let mut options = match parse_macroquad_run_options(std::env::args().skip(1)) {
        Ok(options) => options,
        Err(error) => {
            eprintln!("{error}");
            eprintln!("{}", macroquad_usage());
            std::process::exit(1);
        }
    };
    if options.host_name.is_none() && !options.list_hosts && !options.show_help {
        options.host_name = Some(HOST_NAME.to_string());
    }
    apply_default_macroquad_paths(
        &mut options,
        "quest-ai-dm.macroquad.muddle",
        "quest-ai-dm.macroquad.txt",
        "quest-ai-dm.import.muddle",
        "quest-ai-dm.export.muddle",
    );

    let registrations = vec![MuddleClientHostRegistration {
        name: HOST_NAME,
        category: "Games",
        description: "QUEST: native AI-DM table slice.",
        suggested_commands:
            "`go scene`, `scout room`, `advance scene`, `enemy turn`, `rally party`, `go treasure`, `unseal treasure`.",
        create: || Box::new(ai_dm_muddle_host()),
    }];

    if let Err(error) = run_muddle_macroquad_hosts(
        registrations,
        options,
        MuddleMacroquadRunConfig {
            screen_title: "QUEST AI DM".to_string(),
        },
    )
    .await
    {
        eprintln!("{error}");
        std::process::exit(1);
    }
}
