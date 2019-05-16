class GeneratorBetweenNumbers:

    def generateNumbers(self, value, possibleNumbers):
        boundariesToInsert = []
        boundariesToDelete = []

        for boundary in value:
            if boundary[2] is "y":
                boundariesToInsert.append(boundary)
            if boundary[2] is "n":
                boundariesToDelete.append(boundary)

        for boundaryToInsert in boundariesToInsert:
            [lowLimit, bigLimit, _] = boundaryToInsert
            for i in range(lowLimit, bigLimit + 1):
                if i not in possibleNumbers:
                    possibleNumbers.append(i)

        for boundaryToDelete in boundariesToDelete:
            [lowLimit, bigLimit, _] = boundaryToDelete

            for i in range(lowLimit, bigLimit):
                if i in possibleNumbers:
                    possibleNumbers.remove(i)

        return possibleNumbers