import unittest

import guesser.auxiliarFunctions.auxiliarFunctions as auxF


class TestAuxiliarFunctions(unittest.TestCase):

    # findRepeat
    def test_FindRepeatWithNoRepeatedValues(self):
        # No repeated values
        self.assertEqual(auxF.findRepeat(list(str(1234))), False)

    def test_FindRepeatWithOneRepeatedValue(self):
        # 1 repeated value
        self.assertEqual(auxF.findRepeat(list(str(1224))), True)

    def test_FindRepeatWithTwoRepeatedValues(self):
        # 2 repeated values
        self.assertEqual(auxF.findRepeat(list(str(1333))), True)

    def test_FindRepeatWithZero(self):
        # Zero
        self.assertEqual(auxF.findRepeat(list(str(0))), False)

    # generateNumber
    def test_generateNumberAmongBoundaries(self):
        generatedNumber = auxF.generateNumber()

        # number >= 1000
        self.assertGreaterEqual(generatedNumber, 1000)

        # number <= 9999
        self.assertLessEqual(generatedNumber, 9999)

    # askUserToShot
    def test_askUserToShot(self):
        shot = auxF.askToUserShot()

        # number >= 1000
        self.assertGreaterEqual(shot, 1000)

        # number <= 9999
        self.assertLessEqual(shot, 9999)

    # calculateCorrectAndRegular
    def test_positiveCalculateCorrectAndRegular(self):
        # correctNumber: 1234, userShot: 1273 == correct: 2, regular: 1
        self.assertEqual(auxF.calculateCorrectAndRegular(1273, 1234), [2, 1])

        # correctNumber: 1234, userShot: 8564 == correct: 1, regular: 0
        self.assertEqual(auxF.calculateCorrectAndRegular(8564, 1234), [1, 0])

        # correctNumber: 1234, userShot: 4321 == correct: 0, regular: 4
        self.assertEqual(auxF.calculateCorrectAndRegular(4321, 1234), [0, 4])

        # correctNumber: 1234, userShot: 1234 == correct: 4, regular: 0
        self.assertEqual(auxF.calculateCorrectAndRegular(1234, 1234), [4, 0])

    def test_negativeCalculateCorrectAndRegular(self):
        # correctNumber: 1234, userShot: 1273 != correct: 0, regular: 0
        self.assertIsNot(auxF.calculateCorrectAndRegular(1273, 1234), [0, 0])

        # correctNumber: 1234, userShot: 8564 != correct: 4, regular: 0
        self.assertIsNot(auxF.calculateCorrectAndRegular(8564, 1234), [4, 0])

        # correctNumber: 1234, userShot: 4321 != correct: 2, regular: 2
        self.assertIsNot(auxF.calculateCorrectAndRegular(4321, 1234), [2, 2])

        # correctNumber: 1234, userShot: 1234 != correct: 1, regular: 0
        self.assertIsNot(auxF.calculateCorrectAndRegular(1234, 1234), [1, 0])