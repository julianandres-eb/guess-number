import random

from .questionsolver import QuestionSolver

class QuestionSolverBetween(QuestionSolver):
    lowLimit: int
    bigLimit: int

    def __init__(self, question):
        super().__init__(question)
        self.lowLimit = self.bigLimit = 0

    def askUserValue(self, oldResponses):
        correctValue = False
        correctLimit = False
        value = 0
        lastAnswer = self.getQuestion(self.key).answers

        while correctValue is False:
            while correctLimit is False:
                self.lowLimit = random.randint(pow(10, QuestionSolver.digits - 1), pow(10, QuestionSolver.digits) - 1)
                self.bigLimit = random.randint(pow(10, QuestionSolver.digits - 1), pow(10, QuestionSolver.digits) - 1)

                if self.lowLimit < self.bigLimit:
                    correctLimit = True

            value = input(self.getQuestion(self.key).getTitle() + " " + str(self.lowLimit) + " and " + str(
                self.bigLimit) + "? (y/n): ")

            if value is "y" or value is "n":
                correctValue = True
                return value
            else:
                correctLimit = False

    def composeAnswer(self, value):
        return [self.lowLimit, self.bigLimit, value]

    def validateAnswer(self, answer):
        if answer[0] < answer[1]:
            return True
        else:
            return False

    def saveAnswer(self, answer):
        self.getQuestion(self.key).answers.append(answer)
        return self.getQuestion(self.key).answers
