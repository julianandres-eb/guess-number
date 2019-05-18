
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

        for possibleNumber in possibleNumbers:
            for positionNumber in positionNumbers:

                # Convert the number into a list of strings to separate and make a comparision with positionNumber
                # And if not, we remove it and don't keep testing with that number
                if int(str(list(str(possibleNumber))[positionNumber[0] - 1])) is not positionNumber[1]:
                    possibleNumbers.remove(possibleNumber)
                    break

        return possibleNumbers