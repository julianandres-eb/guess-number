import unittest
from thinker.core.numbergenerator.numbergoodregulargenerator import GeneratorGoodregularNumbers as g

class TestNumberGoodRegularGenerator(unittest.TestCase):

    # calculateCorrectAndRegular
    def test_positiveCalculateCorrectAndRegular(self):
        # correctNumber: 1234, userShot: 1273 == correct: 2, regular: 1
        self.assertEqual(g().calculateCorrectAndRegular(1273, 1234), [2, 1])

        # correctNumber: 1234, userShot: 8564 == correct: 1, regular: 0
        self.assertEqual(g().calculateCorrectAndRegular(8564, 1234), [1, 0])

        # correctNumber: 1234, userShot: 4321 == correct: 0, regular: 4
        self.assertEqual(g().calculateCorrectAndRegular(4321, 1234), [0, 4])

        # correctNumber: 1234, userShot: 1234 == correct: 4, regular: 0
        self.assertEqual(g().calculateCorrectAndRegular(1234, 1234), [4, 0])

    def test_negativeCalculateCorrectAndRegular(self):
        # correctNumber: 1234, userShot: 1273 != correct: 0, regular: 0
        self.assertIsNot(g().calculateCorrectAndRegular(1273, 1234), [0, 0])

        # correctNumber: 1234, userShot: 8564 != correct: 4, regular: 0
        self.assertIsNot(g().calculateCorrectAndRegular(8564, 1234), [4, 0])

        # correctNumber: 1234, userShot: 4321 != correct: 2, regular: 2
        self.assertIsNot(g().calculateCorrectAndRegular(4321, 1234), [2, 2])

        # correctNumber: 1234, userShot: 1234 != correct: 1, regular: 0
        self.assertIsNot(g().calculateCorrectAndRegular(1234, 1234), [1, 0])