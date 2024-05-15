import random

import pandas as pd

from common.const import LOTS_CSV_PATH, SEED, YARDS_CSV_PATH, H, M, N, T, W
from common.seed import seed_everything


def generate_lots() -> None:
    lots = []
    for _ in range(N):
        start_time = random.randint(0, T - 1)
        end_time = random.randint(start_time, T - 1)
        lot_height = random.randint(1, H // 2)
        lot_width = random.randint(1, W // 2)
        lots.append(
            {
                "start_time": start_time,
                "end_time": end_time,
                "height": lot_height,
                "width": lot_width,
            }
        )

    lots_df = pd.DataFrame(lots)
    lots_df.to_csv(LOTS_CSV_PATH, index=False)
    print(f"Generated lots.csv with {N} lots in {LOTS_CSV_PATH.resolve()}.")


def generate_yards() -> None:
    yards = []
    for _ in range(M):
        height = random.randint(int(0.7 * H), H)
        width = random.randint(int(0.7 * W), W)
        yards.append({"height": height, "width": width})

    yards_df = pd.DataFrame(yards)
    yards_df.to_csv(YARDS_CSV_PATH, index=False)
    print(f"Generated yards.csv with {M} yards in {YARDS_CSV_PATH.resolve()}.")


if __name__ == "__main__":
    seed_everything(SEED)
    generate_lots()
    generate_yards()
