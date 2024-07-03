from __future__ import annotations

import unittest

from antgorithm.position import Position


class PositionTest(unittest.TestCase):
    def test_addition(self):
        p1 = Position(x=1, y=2)
        p2 = Position(x=8, y=4)

        sut = p1 + p2
        self.assertEqual(Position(x=1 + 8, y=2 + 4), sut)

    def test_sub(self):
        p1 = Position(x=1, y=2)
        p2 = Position(x=8, y=4)

        sut = p1 - p2
        self.assertEqual(Position(x=1 - 8, y=2 - 4), sut)
