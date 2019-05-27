import unittest
from unittest.mock import patch
from thinker.core.numbergenerator.numberbetweengenerator import GeneratorBetweenNumbers
from thinker.core.questionsolver.questionsolver import QuestionSolver

class TestNumberBetweenGenerator(unittest.TestCase):

    def test_generateNumberWithOneYesBoundary(self):
        allValues: list = [i for i in range(1, 10)]
        with patch.object(QuestionSolver, 'digits', 1):
            assert GeneratorBetweenNumbers().generateNumbers([[2, 6, "y"]], allValues) == [2, 3, 4, 5, 6]

    def test_generateNumberWithOneNoBoundary(self):
        allValues: list = [i for i in range(1, 10)]
        with patch.object(QuestionSolver, 'digits', 1):
            assert GeneratorBetweenNumbers().generateNumbers([[2, 6, "n"]], allValues) == [1, 7, 8, 9]

    def test_generateNumberWithOneYesBoundaryAndOneNoBoundary(self):
        allValues: list = [i for i in range(1, 10)]
        with patch.object(QuestionSolver, 'digits', 1):
            assert GeneratorBetweenNumbers().generateNumbers([[2, 6, "y"], [4, 8, "n"]], allValues) == [2, 3]
