from math import ceil
from pathlib import Path

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

from common.cleanup import cleanup_gif
from common.const import ANIMATION_GIT_PATH, NUM_COLS, OUTPUTS_DIR, M, T
from visualizer.cumulative_sum import make_cumulative_sums
from visualizer.yard_area import make_yard_areas


def get_num_stages() -> int:
    return len(list(OUTPUTS_DIR.glob("assignments_stage_*.csv")))


def vizualize_gif() -> None:
    num_rows = ceil(M / NUM_COLS)

    fig, axes = plt.subplots(num_rows, NUM_COLS, figsize=(5 * NUM_COLS, 5 * num_rows))
    axes = axes.flatten()

    def update(stage: int) -> None:
        for ax in axes:
            ax.clear()

        cumulative_sums = make_cumulative_sums(stage)
        yard_areas = make_yard_areas()

        for i, cumulative_sum in enumerate(cumulative_sums):
            dates = [t for t in range(T)]
            axes[i].clear()
            axes[i].bar(dates, cumulative_sum, color="skyblue")
            axes[i].plot(dates, [yard_areas[i]] * len(dates), color="r")
            axes[i].set_ylim(0, np.max(yard_areas) * 1.5)
            axes[i].set_title(f"Yard {i} Stage {stage}")
            axes[i].set_xlabel("Date")
            axes[i].set_ylabel("Area")
            axes[i].grid(True, axis="y")

        for j in range(M, len(axes)):
            fig.delaxes(axes[j])

    ani = animation.FuncAnimation(fig, update, frames=get_num_stages())

    ani.save(ANIMATION_GIT_PATH)

    plt.tight_layout()
    plt.show()

    print(f"Generated animation.gif in {ANIMATION_GIT_PATH.resolve()}.")


if __name__ == "__main__":
    cleanup_gif(OUTPUTS_DIR)

    vizualize_gif()
