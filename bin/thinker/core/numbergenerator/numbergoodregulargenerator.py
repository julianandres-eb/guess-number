import numpy as np

class GeneratorGoodregularNumbers:

    def generateNumbers(self, values, oldPossibleNumbers):
        if len(values) > 0:
            newPossibleNumbers = []
            for possibleNumber in oldPossibleNumbers:
                if self.testGoodRegular(values, possibleNumber):
                    newPossibleNumbers.append(possibleNumber)

            return newPossibleNumbers
        else:

            return oldPossibleNumbers

    def testGoodRegular(self, valuesForTest, numberToTest):

        if len(valuesForTest) > 0:
            oldNumberToTest = valuesForTest[0][0]
            oldGood = valuesForTest[0][1]
            oldRegular = valuesForTest[0][2]

            if oldNumberToTest is not 0:
                [good, regular] = self.calculateCorrectAndRegular(oldNumberToTest, numberToTest)
                if good == oldGood and regular == oldRegular:
                    return True and self.testGoodRegular(valuesForTest[1:], numberToTest)
                else:
                    return False
            else:
                return True and self.testGoodRegular(valuesForTest[1:], numberToTest)

        else:
            return True

    # Method that returns how many "corrects" and "regulars" are
    def calculateCorrectAndRegular(self, shot, correctNumber):
        # Convert to use them with np.sum
        _shot = np.array([int(x) for x in str(shot)])
        _correctNumber = np.array([int(x) for x in str(correctNumber)])

        # How many corrects are?
        corrects = np.sum(_shot == _correctNumber)
        regulars = 0

        # After determining which numbers match with the correct response,
        # we eliminate them to determine the regular numbers
        shotLeft = _shot[_shot != _correctNumber]
        correctNumberLeft = list(_correctNumber[_shot != _correctNumber])

        for num in shotLeft:
            regulars = regulars + correctNumberLeft.count(num)

        return [corrects, regulars]
