import unittest

from thinker.core.numbergenerator.numberbetweengenerator import GeneratorBetweenNumbers as gnb


class TestNumberBetweenGenerator(unittest.TestCase):

    allValues: list

    def __init__(self):
        super().__init__()
        self.allValues = [i for i in range(1, 20)]

    def test_generateNumberWithYesBoundary(self):
        self.assertIs(gnb().generateNumbers([2, 6, 'y'], self.allValues), [2, 3, 4, 5, 6])

    ## casos positivos
    ## - solo con y
    ## - solo con n
    ## - uno de cada uno
