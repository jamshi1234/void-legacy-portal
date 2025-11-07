import os, yaml

def load_config(path="config/settings.yaml"):
    with open(path) as fh:
        return yaml.safe_load(fh) or {}
