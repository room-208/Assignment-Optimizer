import numpy as np
import pandas as pd

from common.const import ASSIGNMENTS_CSV_PATH, LOTS_CSV_PATH, YARDS_CSV_PATH, M, T
from optimizer.data_structure.lot import Lot
from optimizer.data_structure.yard import Yard


class State:
    def __init__(self) -> None:
        self.lots: list[Lot]
        self.readLots()

        self.yards: list[Yard]
        self.readYards()

        self.cumulative_sums = np.zeros((M, T))
        self.updateCumulativeSumsWithImos()

        self.stage = 0

    def readLots(self) -> None:
        df = pd.read_csv(LOTS_CSV_PATH)
        self.lots = [
            Lot(row["start_time"], row["end_time"], row["height"], row["width"], M)
            for _, row in df.iterrows()
        ]

    def readYards(self) -> None:
        df = pd.read_csv(YARDS_CSV_PATH)
        self.yards = [Yard(row["height"], row["width"]) for _, row in df.iterrows()]

    def updateCumulativeSumsWithImos(self) -> None:
        self.cumulative_sums = np.zeros((M, T))

        for lot in self.lots:
            self.cumulative_sums[lot.assignment][lot.start_time] += lot.area
            if lot.end_time + 1 < T:
                self.cumulative_sums[lot.assignment][lot.end_time + 1] -= lot.area

        for i in range(len(self.cumulative_sums)):
            self.cumulative_sums[i] = np.cumsum(self.cumulative_sums[i])

    def writeAssignments(self) -> None:
        assignments = []
        for lot in self.lots:
            assignment = {"assignment": lot.assignment}
            assignments.append(assignment)

        assignments_df = pd.DataFrame(assignments)
        assignments_df.to_csv(ASSIGNMENTS_CSV_PATH(self.stage), index=False)
        print(
            f"Generated assignments_stage_{self.stage}.csv in {ASSIGNMENTS_CSV_PATH(self.stage).resolve()}."
        )

        self.stage += 1
