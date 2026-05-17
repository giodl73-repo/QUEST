fn main() {
    std::process::exit(quest::run_cli(std::env::args().skip(1).collect()));
}
