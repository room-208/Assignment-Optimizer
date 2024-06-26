from math import inf

import numpy as np

from optimizer.data_structure.state import State


def greedy_by_sorted_volume(state: State) -> State:
    state.lots.sort(
        key=lambda lot: lot.area * (lot.end_time + 1 - lot.start_time), reverse=True
    )

    for i, lot in enumerate(state.lots):
        cumulative_sums = np.max(
            state.cumulative_sums[:, lot.start_time : lot.end_time + 1], axis=1
        ) + np.random.randn(state.M)
        assignment = np.argmin(cumulative_sums)

        state.lots[i].assignment = assignment

        for t in range(lot.start_time, lot.end_time + 1):
            state.cumulative_sums[assignment][t] += lot.area

    return state
