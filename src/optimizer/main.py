import random
from pathlib import Path

import numpy as np

from optimizer.data_structure.state import State
from optimizer.neighborhood.insert import insert
from optimizer.neighborhood.swap import swap


def seed_everything(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)


if __name__ == "__main__":
    SEED = 0
    DATA_DIR = Path("data")
    OUTPUTS_DIR = Path("outputs")

    seed_everything(SEED)

    state = State(DATA_DIR)
    state.writeAssignments(OUTPUTS_DIR)

    for i in range(500):
        r = random.randint(0, 1)
        if r == 0:
            is_transitioned = insert(state)
        elif r == 1:
            is_transitioned = insert(state)

        if is_transitioned:
            state.writeAssignments(OUTPUTS_DIR)
