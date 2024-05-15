import random

from common.cleanup import cleanup_csv
from common.const import OUTPUTS_DIR, SEED
from common.seed import seed_everything
from optimizer.data_structure.state import State
from optimizer.neighborhood.insert import insert

if __name__ == "__main__":
    seed_everything(SEED)

    cleanup_csv(OUTPUTS_DIR)

    state = State()
    state.writeAssignments()

    for i in range(500):
        r = random.randint(0, 0)
        if r == 0:
            is_transitioned = insert(state)

        if is_transitioned:
            state.writeAssignments()
