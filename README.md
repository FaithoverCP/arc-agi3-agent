# arc-agi3-agent

Directional AI agent submission for **ARC-AGI-3 Developer Preview** (July 2025)

| **Benchmark** | **Public preview score (local tests)** |
|---------------|----------------------------------------|
| ARC-AGI-3 Game 1 |  ✎ _fill after first run_ |
| ARC-AGI-3 Game 2 |  ✎ |
| ARC-AGI-3 Game 3 |  ✎ |

---

## Quick-start (10 sec)

```bash
# 1. Clone repo
git clone https://github.com/FaithoverCP/arc-agi3-agent.git
cd arc-agi3-agent

# 2. Create env & install deps (Python 3.10+)
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Export API key (get from https://three.arcprize.org/)
export ARC_API_KEY="sk-...redacted..."

# 4. Run agent on the three public games:
bash run.sh             # or: python agent.py --games all
