use muddle_cli::{run_muddle_host_from_env_args, MuddleCliHostInfo};
use quest::ai_dm_muddle_host;

fn main() -> std::io::Result<()> {
    let mut host = ai_dm_muddle_host();
    run_muddle_host_from_env_args(
        &mut host,
        MuddleCliHostInfo {
            name: "quest-ai-dm",
            description: "QUEST: product-owned MUDDLE host with a deterministic AI DM opponent.",
            suggested_commands:
                "`go scene`, `scout room`, `advance scene`, `enemy turn`, `rally party`, `quit`.",
        },
    )
    .map(|_| ())
}
