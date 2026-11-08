import copy
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


def load_config(path=None):
    path = Path(path) if path else ROOT / "configs" / "default.yaml"
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def with_overrides(cfg, preprocess_steps=None):
    """Copy of cfg with some preprocessing steps switched on/off."""
    cfg = copy.deepcopy(cfg)
    for step, on in (preprocess_steps or {}).items():
        cfg["preprocess"][step] = on
    return cfg
