import random

import numpy as np

from common.const import N
from optimizer.data_structure.state import State


def insert(state: State) -> bool:
    index = random.randint(0, N - 1)
    cumulative_sums = np.max(
        state.cumulative_sums[
            :, state.lots[index].start_time : state.lots[index].end_time + 1
        ],
        axis=1,
    )
    cumulative_sums[state.lots[index].assignment] -= state.lots[index].area

    values = [yard.area for yard in state.yards] - cumulative_sums

    new_assignment = np.argmax(values)

    if cumulative_sums[new_assignment] != cumulative_sums[state.lots[index].assignment]:
        for t in range(state.lots[index].start_time, state.lots[index].end_time + 1):
            state.cumulative_sums[state.lots[index].assignment][t] -= state.lots[
                index
            ].area
            state.cumulative_sums[new_assignment][t] += state.lots[index].area
        state.lots[index].assignment = new_assignment
        return True
    else:
        return False
