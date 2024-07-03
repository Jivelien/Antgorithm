from __future__ import annotations

import random


class AntBrain:
    ...

    def next_direction_change(self):
        pass


class DummyAntBrain(AntBrain):
    def next_direction_change(self) -> float:
        return 0


class RandomAntBrain(AntBrain):
    def __init__(self, angle: float):
        self.angle = angle

    def next_direction_change(self) -> float:
        return random.uniform(-self.angle, self.angle)
