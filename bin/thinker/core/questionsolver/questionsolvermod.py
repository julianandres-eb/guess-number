import random

from bin.thinker.utils.utils import Utils
from .questionsolver import QuestionSolver


class QuestionSolverMod(QuestionSolver):

    lastMod: int = 0

    def askUserValue(self, oldResponses):
        correctValue: bool = False
        modCorrect: bool = False
        value: str = ''

        # QUE NO SE REPITA EL MOD
        oldMods = [answer[1] for answer in self.getQuestion(self.key).getAnswers()]
        # POR SI ME QUEDO SIN MOD
        if len(oldMods) is not len(Utils().primes()):
            while modCorrect is False:
                self.mod = random.choice(Utils().primes())
                if self.mod not in oldMods:
                    modCorrect = True

            while correctValue is False:
                value = input(self.getQuestion(self.key).getTitle() + " " + str(self.mod) + "? (y/n): ")
                if value is "y" or value is "n":
                    correctValue = True

            return value

        else:
            return []

    def composeAnswer(self, answer):
        if len(answer) is not 0:
            return [answer, self.mod]
        else:
            return []

    def validateAnswer(self, answer):
        if len(answer) > 0:
            if answer[0] is "y" or answer[0] is "n" and (0 < answer[1] < 10):
                return True
            else:
                return False
        else:
            return False

    def saveAnswer(self, answer):
        if len(answer) is not 0:
            self.getQuestion(self.key).answers.append(answer)
            return self.getQuestion(self.key).answers

        else:
            return []
