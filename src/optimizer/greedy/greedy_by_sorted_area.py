import numpy as np

from common.const import M, T
from optimizer.data_structure.state import State


def greedy_by_sorted_area(state: State) -> State:
    state.lots.sort(key=lambda lot: lot.area, reverse=True)

    state.cumulative_sums = np.zeros((M, T))

    for i, lot in enumerate(state.lots):
        yard_areas = np.array([yard.area for yard in state.yards])
        empty_areas = yard_areas - np.max(
            state.cumulative_sums[:, lot.start_time : lot.end_time + 1], axis=1
        )

        assignments = np.where(empty_areas == np.max(empty_areas))
        if len(assignments) > 1:
            index = np.argmin(
                [
                    np.sum(state.cumulative_sums[assignment])
                    / (yard_areas[assignment] * T)
                    for assignment in assignments
                ]
            )
            assignment = int(assignments[int(index)])
        else:
            assignment = int(assignments[0])

        state.lots[i].assignment = assignment

        for t in range(lot.start_time, lot.end_time + 1):
            state.cumulative_sums[assignment][t] += lot.area

    return state
