#!/usr/bin/env bash
# Usage: bash run.sh tilehover
set -e
GAME=${1:-tilehover}

echo "[*] Installing deps..."
python -m pip install -r requirements.txt

echo "[*] Running agent locally..."
python agent.py --game "${GAME}" --output "scorecard_${GAME}.json"

echo "[✓] Done. Scorecard saved to scorecard_${GAME}.json"
