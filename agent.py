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

import yaml
from policy import SimpleHeuristicPolicy
from tools.arc_api import upload_score   # ← NEW

# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--game",
        required=True,
        help="ARC-AGI-3 game id (e.g., tilehover, stumps, snails)",
    )
    p.add_argument(
        "--config",
        default="config.yaml",
        help="Path to YAML config (hyper-params, model keys, etc.)",
    )
    p.add_argument(
        "--output",
        default="scorecard.json",
        help="Where to write local scorecard JSON",
    )
    return p.parse_args()


# --------------------------------------------------------------------------- #
# Driver
# --------------------------------------------------------------------------- #
def main() -> None:
    args = parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text())

    # Instantiate our (toy) policy
    policy = SimpleHeuristicPolicy(cfg)

    # Step through the environment (mock loop for demo)
    env_state = {"step": 0, "score": 0}
    done = False
    while not done:
        action = policy.act(env_state)
        env_state["step"] += 1
        env_state["score"] += action
        done = env_state["step"] >= 10  # stop after 10 steps (placeholder)

    # Final metrics
    result_score = env_state["score"]
    result_steps = env_state["step"]

    # Local scorecard (for repo reproducibility)
    scorecard = {
        "game": args.game,
        "score": result_score,
        "steps": result_steps,
    }
    Path(args.output).write_text(json.dumps(scorecard, indent=2))

    # Upload to ARC API, print live URL
    url = upload_score(args.game, result_score, result_steps)
    print(f"[✓] Scorecard URL: {url}")


if __name__ == "__main__":
    main()

