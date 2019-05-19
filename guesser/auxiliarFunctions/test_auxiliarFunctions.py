import unittest

import guesser.auxiliarFunctions.auxiliarFunctions as auxF


class TestAuxiliarFunctions(unittest.TestCase):

    def test_FindRepeat(self):
        # No repeated values
        self.assertEqual(auxF.findRepeat(list(str(1234))), False)

        # 1 repeated value
        self.assertEqual(auxF.findRepeat(list(str(1224))), True)

        # 2 repeated value
        self.assertEqual(auxF.findRepeat(list(str(1333))), True)

        # Zero
        self.assertEqual(auxF.findRepeat(list(str(0))), False)

    # generateNumber
    def test_generateNumber(self):
        # number >= 1000
        self.assertGreaterEqual(auxF.generateNumber(), 1000)

        # number <= 9999
        self.assertLessEqual(auxF.generateNumber(), 9999)

    # askUserToShot
    def test_askUserToShot(self):
        # number >= 1000
        self.assertGreaterEqual(auxF.askToUserShot(), 1000)

        # number <= 9999
        self.assertLessEqual(auxF.askToUserShot(), 9999)

    # calculateCorrectAndRegular
    def test_calculateCorrectAndRegular(self):
        # correctNumber: 1234, userShot: 1273
        self.assertEqual(auxF.calculateCorrectAndRegular(1273, 1234), [2, 1])

        # correctNumber: 1234, userShot: 8564
        self.assertEqual(auxF.calculateCorrectAndRegular(8564, 1234), [1, 0])

        # correctNumber: 1234, userShot: 4321
        self.assertEqual(auxF.calculateCorrectAndRegular(4321, 1234), [0, 4])

        # correctNumber: 1234, userShot: 1234
        self.assertEqual(auxF.calculateCorrectAndRegular(1234, 1234), [4, 0])
