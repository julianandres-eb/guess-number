from bin.thinker.core.questionsolver.questionsolver import QuestionSolver

class GeneratorBetweenNumbers:

    ###########################################################
    #
    # generateNumbers(value, possibleNumbers)
    #
    # positionNumbers: list of lists where each has [lowLimit, bigLimit, y/n]
    # possibleNumbers: list of all values that can be considered as the user number
    #
    # This method creates different boundaries that remove values from possibleNumbers
    #
    ###########################################################

    def generateNumbers(self, value, possibleNumbers):

        # List of lists which contains all boundaries to remove
        boundaries: list = []

        # We insert the boundaries, we do this every time we execute this method to be transparent
        # for the others, that means that this method doesn't remember anything
        for boundary in value:

            # If the user says that the value is in [lowLimit, bigLimit, y],
            # we create 2 lists from 0 to lowLimit and from bigLimit
            # to pow(10, digits) - 1 to eliminate the unnecessary values
            if boundary[2] is "y":
                boundaries.append([0, boundary[0], boundary[2]])
                boundaries.append([boundary[1], pow(10, QuestionSolver.digits) - 1, boundary[2]])

            # If the user says that the value is in [lowLimit, bigLimit, y],
            # we only append the boundary
            if boundary[2] is "n":
                boundaries.append(boundary)

        # And then we eliminate the values that doesn't have to be in there
        for b in boundaries:
            for i in range(b[0], b[1] + 1):
                if i in possibleNumbers:
                    possibleNumbers.remove(i)

        return possibleNumbers