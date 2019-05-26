import unittest
from collections import Counter
from thinker.core.numbergenerator.numberdigitsgenerator import GeneratorDigitsNumbers as g

class TestNumberDigitsGenerator(unittest.TestCase):

    def test_generateNumbersIsNotEmptyInCaseOfEmptyPossibleValues(self, digits=2):
        self.assertIsNot(len(g().generateNumbers([digits], [])), 0)

    def test_generateNumbersIsNotEmptyInCaseOfPossibleValues(self, digits=2):
        self.assertListEqual(g().generateNumbers([digits], [11, 12, 13, 14, 15]), [12, 13, 14, 15])

    def test_generateNumbersAllValuesHasCorrectNumberOfDigits(self, digits=2):
        self.assertIs(len([i for i in g().generateNumbers([digits], []) if len(list(str(i))) is not digits]), 0)