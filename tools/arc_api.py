import os
import json
import requests

ARC_ENDPOINT = "https://api.three.arcprize.org/v1/scorecards"

def upload_score(game: str, score: int, steps: int) -> str:
    """Send one game’s result to ARC and return the scorecard URL."""
    payload = {"game_id": game, "score": score, "steps": steps}
    headers = {
        "Authorization": f"Bearer {os.environ['ARC_API_KEY']}",
        "Content-Type": "application/json",
    }
    r = requests.post(ARC_ENDPOINT, headers=headers, data=json.dumps(payload), timeout=30)
    r.raise_for_status()
    return r.json()["scorecard_url"]
