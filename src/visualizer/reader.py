import json
from pathlib import Path


def read_params(data_dir: Path) -> tuple[int, int, int, int, int]:
    with open(data_dir / "params.json", "r") as file:
        params = json.load(file)
        N = params.get("N")
        M = params.get("M")
        H = params.get("H")
        W = params.get("W")
        T = params.get("T")
    return N, M, H, W, T
