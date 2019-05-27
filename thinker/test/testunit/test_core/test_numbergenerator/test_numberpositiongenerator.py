import unittest
from thinker.core.numbergenerator.numberpositiongenerator import GeneratorPositionNumbers as g

class TestNumberModGenerator(unittest.TestCase):

    def test_generateNumbersWithEmptyPositions(self):
        self.assertListEqual(g().generateNumbers([], [i for i in range(0, 10)]), [])

    def test_generateNumbersWithEmptyPossibleNumbers(self):
        self.assertListEqual(g().generateNumbers([[1, 2]], []), [])

    def test_generateNumbers(self):
        # Values from 10 to 100 --> Position: 2, Value: 5
        self.assertListEqual(g().generateNumbers([[2, 5]], [i for i in range(10, 100)]), [15, 25, 35, 45, 55, 65, 75, 85, 95])