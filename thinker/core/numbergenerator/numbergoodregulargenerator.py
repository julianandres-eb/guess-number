import numpy as np

class GeneratorGoodregularNumbers:

    ###########################################################
    #
    # generateNumbers(values, possibleNumbers)
    #
    # values: list of lists where each has [machine Shot, correct, regular]
    # oldPossibleNumbers: list of all values that can be considered as the user number
    #
    # This method removes values which don't correspond to corrects and regular
    #
    ###########################################################

    def generateNumbers(self, values, possibleNumbers):

        # We 'filter' what we receive
        return list(filter(lambda x: self.testGoodRegular(values, x), [possibleNumber for possibleNumber in possibleNumbers]))

    ###########################################################
    #
    # testGoodRegular(valuesForTest, numberToTest)
    #
    # valuesForTest: list of lists where each has [machine Shot, correct, regular]
    # numberToTest: number we have to determine if it can pass all the good/regular test
    #
    # This method tests if numberToTest corresponds to all the conditions included in valuesToTest
    # It works with recursion testing all values included in valuesForTest
    #
    ###########################################################

    def testGoodRegular(self, valuesForTest, numberToTest):

        # If we already have valuesToTest
        if len(valuesForTest) > 0:

            # Declaration of Variables in that recursion
            oldNumberToTest : int = valuesForTest[0][0]
            oldGood : int = valuesForTest[0][1]
            oldRegular : int = valuesForTest[0][2]

            [good, regular] = self.calculateCorrectAndRegular(oldNumberToTest, numberToTest)

            if good == oldGood and regular == oldRegular:
                return True and self.testGoodRegular(valuesForTest[1:], numberToTest)
            else:
                return False
        else:
            return True


    ###########################################################
    #
    # calculateCorrectAndRegular(shot, correctNumber)
    #
    # shot: machine value
    # correctNumber: user value
    #
    # Method that returns how many "corrects" and "regulars" are
    #
    ###########################################################

    def calculateCorrectAndRegular(self, shot, correctNumber):

        # Convert to use them with np.sum
        shot = np.array([int(x) for x in str(shot)])
        correctNumber = np.array([int(x) for x in str(correctNumber)])

        # How many corrects are?
        corrects = np.sum(shot == correctNumber)
        regulars = 0

        # After determining which numbers match with the correct response,
        # we eliminate them to determine the regular numbers
        shotLeft = shot[shot != correctNumber]
        correctNumberLeft = list(correctNumber[shot != correctNumber])

        # How many regulars are?
        for num in shotLeft:
            regulars = regulars + correctNumberLeft.count(num)

        return [corrects, regulars]
