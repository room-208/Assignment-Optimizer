import json
from pathlib import Path

import pandas as pd

from optimizer.data_structure.lot import Lot
from optimizer.data_structure.yard import Yard


class State:
    def __init__(self, save_dir: Path) -> None:
        self.N: int
        self.M: int
        self.H: int
        self.W: int
        self.T: int
        self.readParams(save_dir / "params.json")

        self.lots: list[Lot]
        self.readLots(save_dir / "lots.csv")

        self.yards: list[Yard]
        self.readYards(save_dir / "yards.csv")

        self.cumulative_sums: list[list[int]] = [[0] * self.T] * self.M

    def readParams(self, file_path: Path) -> None:
        with open(file_path, "r") as file:
            params = json.load(file)
            self.N = params.get("N")
            self.M = params.get("M")
            self.H = params.get("H")
            self.W = params.get("W")
            self.T = params.get("T")

    def readLots(self, file_path: Path) -> None:
        df = pd.read_csv(file_path)
        self.lots = [
            Lot(row["start_time"], row["end_time"], row["height"], row["width"], self.M)
            for _, row in df.iterrows()
        ]

    def readYards(self, file_path: Path) -> None:
        df = pd.read_csv(file_path)
        self.yards = [Yard(row["height"], row["width"]) for _, row in df.iterrows()]

    def writeAssignments(self, outputs_dir: Path, stage: int) -> None:
        assignments = []
        for lot in self.lots:
            assignment = {"assignment": lot.assignment}
            assignments.append(assignment)

        assignments_df = pd.DataFrame(assignments)
        assignments_df.to_csv(
            outputs_dir / f"assignments_stage_{stage}.csv", index=False
        )
        print(f"Generated assignments_stage_{stage}.csv in {outputs_dir}.")


if __name__ == "__main__":
    state = State(Path("data"))
    state.writeAssignments(Path("outputs"), 0)
