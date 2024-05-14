from pathlib import Path

import numpy as np
import pandas as pd


def make_yard_areas(data_dir: Path) -> np.ndarray:
    yards_df = pd.read_csv(data_dir / "yards.csv")
    yards_df["area"] = yards_df["height"] * yards_df["width"]
    return yards_df["area"].to_numpy()
