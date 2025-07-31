#!/usr/bin/env python3
"""
Directional AI – ARC-AGI-3 Developer Preview Agent
See README.md for architecture & references.

Usage:
  python agent.py --game tilehover
"""
import argparse
import json
from pathlib import Path
from policy import SimpleHeuristicPolicy
import yaml

# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--game", required=True,
                   help="ARC-AGI-3 game id (e.g., tilehover, stumps, snails)")
    p.add_argument("--config", default="config.yaml",
                   help="Path to YAML config (hyper-params, model keys, etc.)")
    p.add_argument("--output", default="scorecard.json",
                   help="Where to write local scorecard JSON")
    return p.parse_args()

# --------------------------------------------------------------------------- #
# Driver
# --------------------------------------------------------------------------- #
def main() -> None:
    args = parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text())

    # Instantiate our (toy) policy
    policy = SimpleHeuristicPolicy(cfg)

    # Step through the environment
    # NOTE: ARC-Prize provides an SDK; here we mock with a loop so repo is
    # 100% self-contained. Replace with `from arcagi3 import make_env` etc.
    env_state = {"step": 0, "score": 0}
    done = False
    while not done:
        action = policy.act(env_state)
        # mock transition
        env_state["step"] += 1
        env_state["score"] += action
        done = env_state["step"] >= 10  # stop after 10 steps (placeholder)

    # Record scorecard
    scorecard = {
        "game": args.game,
        "score": env_state["score"],
        "steps": env_state["step"],
    }
    Path(args.output).write_text(json.dumps(scorecard, indent=2))
    print(f"[✓] finished {args.game}, score {env_state['score']}")

if __name__ == "__main__":
    main()
