from pathlib import Path

from optimizer.data_structure.state import State
from optimizer.greedy.greedy_by_sorted_area import greedy_by_sorted_area

if __name__ == "__main__":
    DATA_DIR = Path("data")
    OUTPUTS_DIR = Path("outputs")

    state = State(DATA_DIR)
    state.writeAssignments(OUTPUTS_DIR, 0)

    state = greedy_by_sorted_area(state)
    state.writeAssignments(OUTPUTS_DIR, 1)
