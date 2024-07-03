from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Position:
    x: float
    y: float

    def __add__(self, other):
        return Position(x=self.x+other.x,
                        y=self.y+other.y)

    def __sub__(self, other):
        return Position(x=self.x-other.x,
                        y=self.y-other.y)