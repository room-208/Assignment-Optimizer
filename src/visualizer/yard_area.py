import numpy as np
import pandas as pd

from common.const import YARDS_CSV_PATH


def make_yard_areas() -> np.ndarray:
    yards_df = pd.read_csv(YARDS_CSV_PATH)
    yards_df["area"] = yards_df["height"] * yards_df["width"]
    return yards_df["area"].to_numpy()
