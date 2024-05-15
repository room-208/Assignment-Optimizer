import random

import numpy as np

from common.const import M, N, T
from optimizer.data_structure.state import State


def insert(state: State) -> bool:
    index = random.randint(0, N - 1)

    yard_areas = np.array([yard.area for yard in state.yards])
    empty_areas = yard_areas - np.max(
        state.cumulative_sums[
            :, state.lots[index].start_time : state.lots[index].end_time + 1
        ],
        axis=1,
    )
    empty_areas[state.lots[index].assignment] += state.lots[index].area

    (new_assignments,) = np.where(empty_areas == np.max(empty_areas))
    if len(new_assignments) > 1:
        index_ = np.argmin(
            [
                np.sum(state.cumulative_sums[new_assignment])
                / (yard_areas[new_assignment] * T)
                for new_assignment in new_assignments
            ]
        )
        new_assignment = int(new_assignments[int(index_)])
    else:
        new_assignment = int(new_assignments[0])

    if new_assignment != state.lots[index].assignment:
        for t in range(state.lots[index].start_time, state.lots[index].end_time + 1):
            state.cumulative_sums[state.lots[index].assignment][t] -= state.lots[
                index
            ].area
            state.cumulative_sums[new_assignment][t] += state.lots[index].area
        state.lots[index].assignment = new_assignment
        return True
    else:
        return False
