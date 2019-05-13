import random

from bin.thinker.utils.utils import Utils
from .questionsolver import QuestionSolver


class QuestionSolverMod(QuestionSolver):
    mod = 0

    def askUserValue(self):
        correctValue = False
        value = 0
        self.mod = random.choice(Utils().primes(10))
        a = [answer[1] for answer in self.getQuestion(self.key).getAnswers()]
        if self.mod not in a:
            while correctValue is False:
                value = input(self.getQuestion(self.key).getTitle() + " " + str(self.mod) + "? (y/n): ")
                if value is "y" or value is "n":
                    correctValue = True
        else:
            value = "x"
        return value

    def composeAnswer(self, answer):
        return [answer, self.mod]

    def validateAnswer(self, answer):
        if answer[0] is "y" or answer[0] is "n" or answer[0] is "x" and (0 < answer[1] < 10):
            return True
        else:
            return False

    def saveAnswer(self, answer):
        if answer[0] is not "x":
            self.getQuestion(self.key).answers.append(answer)
        return self.getQuestion(self.key).answers
