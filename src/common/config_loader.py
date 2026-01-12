import yaml
import os

def load_config(env):
    base_path = "configs/base/pipeline.yaml"
    env_path = f"configs/{env}/pipeline.yaml"

    with open(base_path) as f:
        base = yaml.safe_load(f)

    with open(env_path) as f:
        env_cfg = yaml.safe_load(f)

    return {**base, **env_cfg}
