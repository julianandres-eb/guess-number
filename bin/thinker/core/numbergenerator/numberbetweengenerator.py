from bin.thinker.core.questions.questionsolver.questionsolver import QuestionSolver

class GeneratorBetweenNumbers:

    def generateNumbers(self, value, possibleNumbers):
        boundaries = []

        for boundary in value:
            if boundary[2] is "y":
                boundaries.append([0, boundary[0], boundary[2]])
                boundaries.append([boundary[1], pow(10, QuestionSolver.digits) - 1, boundary[2]])

            if boundary[2] is "n":
                boundaries.append(boundary)

        for b in boundaries:
            [lowLimit, bigLimit, _] = b
            for i in range(lowLimit, bigLimit + 1):
                if i in possibleNumbers:
                    possibleNumbers.remove(i)

        return possibleNumbers