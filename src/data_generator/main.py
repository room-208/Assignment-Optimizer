import json
import random
from pathlib import Path

import pandas as pd


def save_params(params: dict, save_dir: Path) -> None:
    with open(save_dir / "params.json", "w") as file:
        json.dump(params, file, indent=4)
    print("Save params")


def generate_lots(N: int, H: int, W: int, T: int, save_dir: Path) -> None:
    lots = []
    for _ in range(N):
        start_time = random.randint(0, T - 1)
        end_time = random.randint(start_time, T - 1)
        lot_height = random.randint(1, H)
        lot_width = random.randint(1, W)
        lots.append(
            {
                "start_time": start_time,
                "end_time": end_time,
                "height": lot_height,
                "width": lot_width,
            }
        )

    lots_df = pd.DataFrame(lots)
    lots_df.to_csv(save_dir / "lots.csv", index=False)
    print(f"Generated lots.csv with {N} lots in {save_dir}.")


def generate_yards(M: int, H: int, W: int, save_dir: Path) -> None:
    yards = []
    for _ in range(M):
        yards.append({"height": H, "width": W})

    yards_df = pd.DataFrame(yards)
    yards_df.to_csv(save_dir / "yards.csv", index=False)
    print(f"Generated yards.csv with {M} yards in {save_dir}.")


if __name__ == "__main__":
    N = 100
    M = 2
    H = 500
    W = 100
    T = 100
    SAVE_DIR = Path("../../data")

    save_params({"N": N, "M": M, "H": H, "W": W, "T": T}, SAVE_DIR)
    generate_lots(N, H // 2, W // 2, T, SAVE_DIR)
    generate_yards(M, H, W, SAVE_DIR)
