class GeneratorPositionNumbers:

    def generateNumbers(self, positionNumbers, possibleNumbers):
        numbersToReturn = []
        for positionNumber in positionNumbers:
            for possibleNumber in possibleNumbers:
                if int(str(list(str(possibleNumber))[positionNumber[0] - 1])) is positionNumber[1]:
                    numbersToReturn.append(possibleNumber)

        return numbersToReturn