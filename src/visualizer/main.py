from math import ceil

import matplotlib.pyplot as plt


def show_schedules(
    cumulative_sums: list[list[int]], yard_areas: list[int], num_cols: int
):
    M = len(cumulative_sums)
    num_rows = ceil(M / num_cols)
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(5 * num_cols, 5 * num_rows))

    axes = axes.flatten()

    for i, cumulative_sum in enumerate(cumulative_sums):
        dates = [j for j in range(len(cumulative_sum))]
        axes[i].bar(dates, cumulative_sum, color="skyblue")
        axes[i].plot(dates, [yard_areas[i]] * len(dates), color="r")
        axes[i].set_title(f"Yard {i}")
        axes[i].set_xlabel("Date")
        axes[i].set_ylabel("Area")
        axes[i].grid(True, axis="y")

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()
