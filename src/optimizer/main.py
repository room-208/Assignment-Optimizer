import random

from common.cleanup import cleanup_csv
from common.const import OUTPUTS_DIR, SEED
from common.seed import seed_everything
from optimizer.data_structure.state import State
from optimizer.greedy.greedy_by_sorted_area import greedy_by_sorted_area
from optimizer.neighborhood.insert import insert
from optimizer.neighborhood.swap import swap

if __name__ == "__main__":
    seed_everything(SEED)

    cleanup_csv(OUTPUTS_DIR)

    state = State()
    state.writeAssignments()

    # state = greedy_by_sorted_area(state)
    # state.writeAssignments()

    for i in range(1000):
        r = random.randint(0, 1)
        if r == 0:
            is_transitioned = insert(state)
        elif r == 1:
            is_transitioned = swap(state)

        if is_transitioned:
            state.writeAssignments()
