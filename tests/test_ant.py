from __future__ import annotations

import unittest

from antgorithm.ant import Ant
from antgorithm.ant_brain.ant_brain import AntBrain
from antgorithm.position import Position


class StubAntBrain(AntBrain):
    def __init__(self, rotate: float):
        self._rotate = rotate

    def next_direction_change(self) -> float:
        return self._rotate


class AntTest(unittest.TestCase):
    def test_movement(self):
        an_ant = Ant()

        an_ant.move()

        sut = an_ant.current_position
        self.assertEqual(Position(x=0, y=1), sut)

    def test_movement2(self):
        an_ant = Ant(position=Position(x=26, y=14))

        an_ant.move()

        sut = an_ant.current_position
        self.assertEqual(Position(x=26, y=15), sut)

    def test_rotate(self):
        an_ant = Ant(ant_brain=StubAntBrain(rotate=90))

        an_ant.move()

        sut = an_ant.current_position
        self.assertAlmostEqual(1., sut.x, 2)
        self.assertAlmostEqual(0., sut.y, 2)
