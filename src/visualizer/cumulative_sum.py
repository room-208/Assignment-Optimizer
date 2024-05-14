from pathlib import Path

import numpy as np
import pandas as pd

from visualizer.reader import read_params


def make_cumulative_sums(data_dir: Path, outputs_dir: Path, stage: int) -> np.ndarray:
    _, M, _, _, T = read_params(data_dir)

    lots_df = pd.read_csv(data_dir / "lots.csv")
    assignments_df = pd.read_csv(outputs_dir / f"assignments_stage_{stage}.csv")

    merged_df = pd.merge(lots_df, assignments_df, left_index=True, right_index=True)
    merged_df["area"] = merged_df["height"] * merged_df["width"]

    cumulative_sums = np.zeros((M, T))

    for _, row in merged_df.iterrows():
        assignment = row["assignment"]
        area = row["area"]
        start_time = row["start_time"]
        end_time = row["end_time"]

        cumulative_sums[assignment][start_time] += area

        if end_time + 1 < T:
            cumulative_sums[assignment][end_time + 1] -= area

    for i in range(len(cumulative_sums)):
        cumulative_sums[i] = np.cumsum(cumulative_sums[i])

    cumulative_sums = np.array(cumulative_sums)

    return cumulative_sums
