from __future__ import annotations

import math

from antgorithm.ant_brain.ant_brain import AntBrain, DummyAntBrain
from antgorithm.position import Position


class Ant:
    def __init__(self,
                 ant_brain: AntBrain = DummyAntBrain(),
                 position: Position = Position(x=0, y=0),
                 ):
        self._ant_brain = ant_brain
        self._position = position
        self._next_direction: float = 0

    @property
    def current_position(self) -> Position:
        return self._position

    def move(self):
        self._next_direction += self._ant_brain.next_direction_change()
        next_movement = self.compute_next_movement()
        self._position += next_movement

    def compute_next_movement(self):
        x = math.sin(self._next_direction / 180 * math.pi)
        y = math.cos(self._next_direction / 180 * math.pi)
        return Position(x=x, y=y)

    def rotate(self, angle: float):
        self._next_direction += angle
