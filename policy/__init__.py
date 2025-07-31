"""
SimpleHeuristicPolicy
---------------------
A placeholder policy that returns a constant action defined in config.yaml.
In a real submission, replace with chain-of-thought calls or RL policy.
"""

class SimpleHeuristicPolicy:
    def __init__(self, cfg: dict):
        # A single integer action to emit (ARC games use int IDs)
        self.action_value = cfg.get("default_action", 1)

    def act(self, env_state: dict) -> int:
        # Trivial policy: alternate every step
        # Replace with something smarter.
        return self.action_value if env_state["step"] % 2 == 0 else 0
