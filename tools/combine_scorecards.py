#!/usr/bin/env python3
"""
Combine individual ARC-AGI-3 scorecards into a single JSON.

Usage (repo root, venv activated)
---------------------------------
python tools/combine_scorecards.py \
    --inputs scorecard_tilehover.json scorecard_stumps.json scorecard_snails.json \
    --output scorecard.json
"""

import argparse, json, sys
from pathlib import Path

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--inputs", nargs="+", required=True,
                   help="One or more per-game scorecard JSON files.")
    p.add_argument("--output", default="scorecard.json",
                   help="File to write combined result.")
    args = p.parse_args()

    total = 0
    details = []

    for fp in args.inputs:
        f = Path(fp)
        if not f.exists():
            sys.exit(f"[!] Missing file: {fp}")
        card = json.loads(f.read_text())
        total += card.get("score", 0)
        details.append(card)

    combined = {"total_score": total, "details": details}
    Path(args.output).write_text(json.dumps(combined, indent=2))
    print(f"[✓] Wrote combined score to {args.output}")

if __name__ == "__main__":
    main()
