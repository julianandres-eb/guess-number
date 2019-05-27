import random

from thinker.utils.utils import Utils
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

class QuestionSolverMod(QuestionSolver):

    # Declaration of class variables
    lastMod: int = 0

    def askUserValue(self, oldResponses):

        # Declaration of variables
        correctValue: bool = False
        modCorrect: bool = False
        value: str = ''

        # Have we used any other mod?
        oldMods = [answer[1] for answer in self.getQuestion(self.key).getAnswers()]

        # If we haven't used them all
        if len(oldMods) is not len(Utils().primes()):

            # We determine the new mod
            while modCorrect is False:
                self.mod = random.choice(Utils().primes())
                if self.mod not in oldMods:
                    modCorrect = True

            # We ask the user for an answer
            while correctValue is False:
                value = input(self.getQuestion(self.key).getTitle() + " " + str(self.mod) + "? (y/n): ")
                if value is "y" or value is "n":
                    correctValue = True

            return value

        # If yes, we return empty
        else:
            return []

    def composeAnswer(self, answer):

        # Check if we performed a mod
        return [answer, self.mod] if len(answer) is not 0 else []

    def validateAnswer(self, composedAnswer):

        # Check if we have an answer
        if len(composedAnswer) > 0:

            # Check if correct
            if composedAnswer[0] is "y" or composedAnswer[0] is "n":
                    return True

            # Otherwise, we retry
            else:
                print("It's not a valid answer. Only 'y' and 'n' are possible")
                return False
        else:
            return False

    def saveAnswer(self, answer):
        if len(answer) is not 0:
            self.getQuestion(self.key).answers.append(answer)

        return self.getQuestion(self.key).answers

