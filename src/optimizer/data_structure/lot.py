import random


class Lot:
    def __init__(
        self, start_time: int, end_time: int, height: int, width: int, M: int
    ) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.height = height
        self.width = width

        self.area = self.height * self.width
        self.assignment = random.randint(0, M - 1)
