import os, json, requests

ARC_ENDPOINT = "https://api.three.arcprize.org/v1/scorecards"

def upload_score(game_id: str, score: int, steps: int) -> str:
    """Send a single-game score to ARC, return the public scorecard URL."""
    headers = {
        "Authorization": f"Bearer {os.environ['ARC_API_KEY']}",
        "Content-Type": "application/json",
    }
    payload = {"game_id": game_id, "score": score, "steps": steps}
    r = requests.post(ARC_ENDPOINT, headers=headers, data=json.dumps(payload), timeout=30)
    r.raise_for_status()
    return r.json()["scorecard_url"]

