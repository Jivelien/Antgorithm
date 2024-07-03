from __future__ import annotations

import unittest

from anthgorithm.ant import Ant
from anthgorithm.position import Position


class AntTest(unittest.TestCase):
    def test_movement(self):
        an_ant = Ant(position=Position(x=0, y=0))

        an_ant.move()

        sut = an_ant.position
        self.assertEqual(Position(x=0, y=1), sut)

    def test_movement2(self):
        an_ant = Ant(position=Position(x=26, y=14))

        an_ant.move()

        sut = an_ant.position
        self.assertEqual(Position(x=26, y=15), sut)

    def test_rotate(self):
        an_ant = Ant(position=Position(x=0, y=0))

        an_ant.rotate(angle=90)
        an_ant.move()

        sut = an_ant.position
        self.assertAlmostEqual(1., sut.x, 5)
        self.assertAlmostEqual(0., sut.y, 5)
