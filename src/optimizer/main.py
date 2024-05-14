import random
from pathlib import Path

import numpy as np

from optimizer.data_structure.state import State
from optimizer.greedy.greedy_by_sorted_area import greedy_by_sorted_area


def seed_everything(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)


if __name__ == "__main__":
    SEED = 0
    DATA_DIR = Path("data")
    OUTPUTS_DIR = Path("outputs")

    seed_everything(SEED)

    state = State(DATA_DIR)
    state.writeAssignments(OUTPUTS_DIR, 0)

    state = greedy_by_sorted_area(state)
    state.writeAssignments(OUTPUTS_DIR, 1)
