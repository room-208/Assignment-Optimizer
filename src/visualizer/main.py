from math import ceil
from pathlib import Path

import matplotlib.animation as animation
import matplotlib.pyplot as plt

from visualizer.cumulative_sum import make_cumulative_sums
from visualizer.reader import read_params
from visualizer.yard_area import make_yard_areas


def vizualize_gif(
    data_dir: Path, outputs_dir: Path, num_cols: int, num_stages: int
) -> None:
    _, M, _, _, _ = read_params(data_dir)
    num_rows = ceil(M / num_cols)

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(5 * num_cols, 5 * num_rows))
    axes = axes.flatten()

    def update(stage: int) -> None:
        for ax in axes:
            ax.clear()

        cumulative_sums = make_cumulative_sums(data_dir, outputs_dir, stage)
        yard_areas = make_yard_areas(data_dir)

        for i, cumulative_sum in enumerate(cumulative_sums):
            dates = [i for i in range(len(cumulative_sum))]
            axes[i].clear()
            axes[i].bar(dates, cumulative_sum, color="skyblue")
            axes[i].plot(dates, [yard_areas[i]] * len(dates), color="r")
            axes[i].set_ylim(0, yard_areas[i] * 1.5)
            axes[i].set_title(f"Yard {i} Stage {stage}")
            axes[i].set_xlabel("Date")
            axes[i].set_ylabel("Area")
            axes[i].grid(True, axis="y")

        for j in range(M, len(axes)):
            fig.delaxes(axes[j])

    ani = animation.FuncAnimation(fig, update, frames=num_stages)

    ani.save(outputs_dir / "animation.gif")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    DATA_DIR = Path("data")
    OUTPUTS_DIR = Path("outputs")

    vizualize_gif(DATA_DIR, OUTPUTS_DIR, 2, 10)
