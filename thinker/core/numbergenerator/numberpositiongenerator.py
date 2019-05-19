
class GeneratorPositionNumbers:

    ###########################################################
    #
    # generateNumbers(positionNumbers, possibleNumbers)
    #
    # positionNumbers: list of lists where each has 2 values,
    # a position and the value for that position
    # possibleNumbers: list of all values that can be considered as the user number
    #
    # This method filters the numbers who matches the tuples (position, number)
    #
    ###########################################################

    def generateNumbers(self, positionNumbers, possibleNumbers):
        numbersToReturn : list = []

        for possibleNumber in possibleNumbers:
            for positionNumber in positionNumbers:

                # Convert the number into a list of strings to separate and make a comparision with positionNumber
                # And if not, we append it and return it
                if int(str(list(str(possibleNumber))[positionNumber[0] - 1])) is positionNumber[1]:
                    numbersToReturn.append(possibleNumber)

        return numbersToReturn