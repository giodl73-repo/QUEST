import subprocess
import sys
import pytest
from pathlib import Path


def run_cli(*args):
    result = subprocess.run(
        [sys.executable, "scripts/marathon.py"] + list(args),
        capture_output=True, text=True, cwd=Path(__file__).parent.parent,
        env={**__import__("os").environ, "PYTHONUTF8": "1"},
    )
    return result


def test_cli_no_args_prints_help():
    r = run_cli()
    assert r.returncode == 2
    assert "usage" in r.stderr.lower() or "usage" in r.stdout.lower()


def test_cli_status_no_session(tmp_path):
    # Run with a state dir that has no session
    r = subprocess.run(
        [sys.executable, "scripts/marathon.py", "status"],
        capture_output=True, text=True,
        cwd=Path(__file__).parent.parent,
        env={**__import__("os").environ, "PYTHONUTF8": "1",
             "MARATHON_STATE_DIR": str(tmp_path)},
    )
    assert r.returncode == 0
    assert "No active session" in r.stdout


def test_cli_resume_no_checkpoint(tmp_path):
    r = subprocess.run(
        [sys.executable, "scripts/marathon.py", "resume"],
        capture_output=True, text=True,
        cwd=Path(__file__).parent.parent,
        env={**__import__("os").environ, "PYTHONUTF8": "1",
             "MARATHON_STATE_DIR": str(tmp_path)},
    )
    assert r.returncode == 1
    assert "No checkpoint found" in r.stdout


def test_cli_set_route_no_session(tmp_path):
    r = subprocess.run(
        [sys.executable, "scripts/marathon.py", "set-route", "D"],
        capture_output=True, text=True,
        cwd=Path(__file__).parent.parent,
        env={**__import__("os").environ, "PYTHONUTF8": "1",
             "MARATHON_STATE_DIR": str(tmp_path)},
    )
    assert r.returncode == 1
    assert "no active session" in r.stderr.lower()


def test_cli_set_route_invalid_value(tmp_path):
    r = subprocess.run(
        [sys.executable, "scripts/marathon.py", "set-route", "X"],
        capture_output=True, text=True,
        cwd=Path(__file__).parent.parent,
        env={**__import__("os").environ, "PYTHONUTF8": "1",
             "MARATHON_STATE_DIR": str(tmp_path)},
    )
    # argparse should reject invalid choice before cmd_set_route runs
    assert r.returncode != 0


def test_cli_status_shows_event_log_when_empty(tmp_path):
    r = subprocess.run(
        [sys.executable, "scripts/marathon.py", "status"],
        capture_output=True, text=True,
        cwd=Path(__file__).parent.parent,
        env={**__import__("os").environ, "PYTHONUTF8": "1",
             "MARATHON_STATE_DIR": str(tmp_path)},
    )
    # No session exists — just check it doesn't crash
    assert r.returncode == 0
