import numpy as np


def pelanty(empty_areas: np.ndarray, alpha: float) -> np.ndarray:
    return np.array(
        [
            empty_area if empty_area > 0 else alpha * empty_area
            for empty_area in empty_areas
        ]
    )
