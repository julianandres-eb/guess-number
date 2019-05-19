import random

from .questionsolver import QuestionSolver

###########################################################
#
# QuestionSolverMod
#
# Class that inherits from QuestionSolver. It's responsible
# of determining which mod the correct number has,
# validates and persists it for futures uses
#
###########################################################

class QuestionSolverPosition(QuestionSolver):

    # Declaration of class variables
    position = 0

    def askUserValue(self, oldResponses):

        # Declaration of variables
        correctValue: bool = False
        positionCorrect: bool = False
        value: int = -1
        answers = self.getQuestion(self.key).answers
        numberOfKnownPositions = len(answers)

        # Iterate until we have a selected position
        while positionCorrect is False:

            # Create a possible value
            randomValue = random.randint(1, QuestionSolver.digits)

            # If we already have positions
            if numberOfKnownPositions > 0:

                # And the number of positions are lower than number of digits
                if numberOfKnownPositions is not QuestionSolver.digits - 1:

                    # We determine which position were selected
                    oldPositions : list = []
                    for answer in answers:
                        oldPositions.append(answer[0])

                    # We check if our value wasn't selected before
                    if randomValue not in oldPositions:
                        self.position = randomValue
                        positionCorrect = True

                # We selected all
                else:
                    positionCorrect = True

            # Otherwise, we select it at the first time
            else:
                self.position = randomValue
                positionCorrect = True

        # We ask for the value related for that position
        if self.position > 0:
            while correctValue is False:
                try:
                    value = int(input(self.getQuestion(self.key).getTitle() + " " + str(self.position) + "?: "))
                except ValueError:
                    print("Not an integer!")
                    continue
                else:
                    if value > 0:
                        correctValue = True
                    break

        return value

    def composeAnswer(self, value):
        return [self.position, value]

    def validateAnswer(self, answer):

        # If we have selected a position
        if answer[0] > 0:

            # Check that the related value is correct
            if 0 <= answer[1] <= 9:
                return True

            # Otherwise, we retry
            else:
                print("It's not a valid answer. Only numbers bigger than zero and lower than 10")
                return False

        else:
            return True

    def saveAnswer(self, answer):
        if answer[0] > 0:
            self.getQuestion(self.key).answers.append(answer)

        return self.getQuestion(self.key).answers
