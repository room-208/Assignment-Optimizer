import numpy as np
import pandas as pd

from common.const import ASSIGNMENTS_CSV_PATH, LOTS_CSV_PATH, M, T


def make_merged_df(stage: int) -> pd.DataFrame:
    lots_df = pd.read_csv(LOTS_CSV_PATH)
    assignments_df = pd.read_csv(ASSIGNMENTS_CSV_PATH(stage))
    merged_df = pd.merge(lots_df, assignments_df, left_index=True, right_index=True)
    merged_df["area"] = merged_df["height"] * merged_df["width"]
    return merged_df


def make_cumulative_sums(stage: int) -> np.ndarray:
    merged_df = make_merged_df(stage)

    cumulative_sums = np.zeros((M, T))

    for _, row in merged_df.iterrows():
        assignment = row["assignment"]
        area = row["area"]
        start_time = row["start_time"]
        end_time = row["end_time"]

        cumulative_sums[assignment][start_time] += area

        if end_time + 1 < T:
            cumulative_sums[assignment][end_time + 1] -= area

    for i in range(M):
        cumulative_sums[i] = np.cumsum(cumulative_sums[i])

    return cumulative_sums
