from __future__ import annotations

import math

from anthgorithm.position import Position


class Ant:
    def __init__(self, position : Position):
        self._position = position
        self._direction: float = 0

    @property
    def position(self) -> Position:
        return self._position

    def move(self):
        x = math.sin(self._direction/180*math.pi)
        y = math.cos(self._direction/180*math.pi)
        self._position += Position(x=x,y=y)

    def rotate(self, angle: float):
        self._direction += angle
