import random

from .questionsolver import QuestionSolver


class QuestionSolverPosition(QuestionSolver):
    position = 0

    def askUserValue(self, oldResponses):
        correctValue = False
        positionCorrect = False
        value = 0
        while positionCorrect is False:
            randomValue = random.randint(1, QuestionSolver.digits)
            answers = self.getQuestion(self.key).answers
            numberOfKnownPositions = len(answers)
            if numberOfKnownPositions > 0:
                if numberOfKnownPositions is not QuestionSolver.digits - 1:
                    oldPositions = []
                    for answer in self.getQuestion(self.key).answers:
                        oldPositions.append(answer[0])

                    if randomValue not in oldPositions:
                        self.position = randomValue
                        positionCorrect = True
                else:
                    self.position = 0
                    positionCorrect = True
            else:
                self.position = randomValue
                positionCorrect = True

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
        if answer[0] >= 0 and 0 <= answer[1] <= 9:
            return True
        else:
            return False

    def saveAnswer(self, answer):
        if answer[0] > 0:
            self.getQuestion(self.key).answers.append(answer)

        return self.getQuestion(self.key).answers
