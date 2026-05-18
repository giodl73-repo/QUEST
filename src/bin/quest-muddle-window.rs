use muddle_window::{run_muddle_window_hosts_from_env_args, MuddleWindowHostRegistration};
use quest::ai_dm_muddle_host;

fn main() -> std::io::Result<()> {
    run_muddle_window_hosts_from_env_args(vec![MuddleWindowHostRegistration {
        name: "quest-ai-dm",
        category: "Games",
        description: "QUEST: product-owned MUDDLE window host with a deterministic AI DM opponent.",
        suggested_commands:
            "`go scene`, `scout room`, `advance scene`, `enemy turn`, `rally party`.",
        create: || Box::new(ai_dm_muddle_host()),
    }])
}
