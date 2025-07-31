"""
SimpleHeuristicPolicy
---------------------
A placeholder policy that returns a constant action defined in config.yaml.
In a real submission, replace with chain-of-thought calls or RL policy.
"""

class SimpleHeuristicPolicy:
    def __init__(self, cfg: dict):
        self.action_value = cfg.get("default_action", 1)

    def act(self, env_state: dict) -> int:
        # Example: alternate 1 / 0 each step
        return self.action_value if env_state["step"] % 2 == 0 else 0
