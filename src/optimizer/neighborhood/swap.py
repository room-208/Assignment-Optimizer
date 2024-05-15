import random
from copy import deepcopy

import numpy as np

from common.const import M, N, T
from optimizer.data_structure.state import State


def get_pair_lot_indice(state: State) -> tuple[int, int]:
    indices = list(range(N))
    while True:
        index1, index2 = random.sample(indices, 2)

        if state.lots[index1].assignment != state.lots[index2].assignment and (
            state.lots[index1].end_time <= state.lots[index2].start_time
            or state.lots[index2].end_time <= state.lots[index1].start_time
        ):
            return index1, index2


def swap(state: State) -> bool:
    index1, index2 = get_pair_lot_indice(state)

    yard_areas = np.array([yard.area for yard in state.yards])
    new_cumulative_sums = deepcopy(state.cumulative_sums)
    for t in range(state.lots[index1].start_time, state.lots[index1].end_time + 1):
        new_cumulative_sums[state.lots[index1].assignment][t] -= state.lots[index1].area
        new_cumulative_sums[state.lots[index2].assignment][t] += state.lots[index1].area
    for t in range(state.lots[index2].start_time, state.lots[index2].end_time + 1):
        new_cumulative_sums[state.lots[index2].assignment][t] -= state.lots[index2].area
        new_cumulative_sums[state.lots[index1].assignment][t] += state.lots[index2].area

    start_time = min(state.lots[index1].start_time, state.lots[index2].start_time)
    end_time = max(state.lots[index1].end_time, state.lots[index2].end_time)

    empty_areas = yard_areas - np.max(
        state.cumulative_sums[:, start_time : end_time + 1],
        axis=1,
    )
    new_empty_areas = yard_areas - np.max(
        new_cumulative_sums[:, start_time : end_time + 1],
        axis=1,
    )

    score = (
        empty_areas[state.lots[index1].assignment]
        + empty_areas[state.lots[index2].assignment]
    )
    new_score = (
        new_empty_areas[state.lots[index1].assignment]
        + new_empty_areas[state.lots[index2].assignment]
    )

    if new_score > score:
        state.lots[index1].assignment, state.lots[index2].assignment = (
            state.lots[index2].assignment,
            state.lots[index1].assignment,
        )
        state.cumulative_sums = deepcopy(new_cumulative_sums)
        return True
    else:
        return False
