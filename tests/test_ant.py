from __future__ import annotations

import math
import unittest
from dataclasses import dataclass


@dataclass
class Position:
    x: float
    y: float

    def __add__(self, other):
        return Position(x=self.x+other.x,
                        y=self.y+other.y)

class Ant:
    def __init__(self, position : Position):
        self._position = position
        self._direction: float = 0

    @property
    def position(self) -> Position:
        return self._position

    def move(self):
        x = math.sin(self._direction)
        y = math.cos(self._direction)
        self._position += Position(x=x,y=y)

    def rotate(self, angle: float):
        self._direction += angle


class PositionTest(unittest.TestCase):
    def test_addition(self):
        p1 = Position(x=1,y=2)
        p2= Position(x=8,y=4)

        sut = p1 + p2
        self.assertEqual(Position(x=1+8, y=2+4), sut)

class AntTest(unittest.TestCase):
    def test_movement(self):
        an_ant = Ant(position=Position(x=0,y=0))

        an_ant.move()

        sut = an_ant.position
        self.assertEqual(Position(x=0,y=1), sut)

    def test_movement2(self):
        an_ant = Ant(position=Position(x=26,y=14))

        an_ant.move()

        sut = an_ant.position
        self.assertEqual(Position(x=26,y=15), sut)

    def test_rotate(self):
        an_ant = Ant(position=Position(x=0,y=0))

        an_ant.rotate(angle=90)
        an_ant.move()

        an_ant = Ant(position=Position(x=1,y=0))
