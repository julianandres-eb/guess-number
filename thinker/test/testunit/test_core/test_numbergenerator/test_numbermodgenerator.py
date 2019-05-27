import unittest
from thinker.core.numbergenerator.numbermodgenerator import GeneratorModNumbers as g

class TestNumberModGenerator(unittest.TestCase):

    def test_generateNumberWithOneYesMod(self):
        possibleNumbers = [i for i in range(1, 10)]
        self.assertListEqual(g().generateNumbers([['y', 3]], possibleNumbers), [3, 6, 9])

    def test_generateNumberWithOneNoMod(self):
        possibleNumbers = [i for i in range(1, 10)]
        self.assertListEqual(g().generateNumbers([['n', 3]], possibleNumbers), [1, 2, 4, 5, 7, 8])

    def test_generateNumberWithTwoYesMod(self):
        possibleNumbers = [i for i in range(1, 100)]
        self.assertListEqual(g().generateNumbers([['y', 3], ['y', 5]], possibleNumbers), [15, 30, 45, 60, 75, 90])

    def test_generateNumberWithOneYesAndNoMod(self):
        possibleNumbers = [i for i in range(1, 10)]
        self.assertListEqual(g().generateNumbers([['n', 3], ['y', 5]], possibleNumbers), [5])

    def test_generateNumberWithTwoNoMod(self):
        possibleNumbers = [i for i in range(1, 10)]
        self.assertListEqual(g().generateNumbers([['n', 3], ['n', 2]], possibleNumbers), [1, 5, 7])
