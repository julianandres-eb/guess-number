import random

from .question import question as q

class Questionnaire:
    _questions = []
    _answers = []

    def __init__(self):
        self.initQuestionaire()

    def initQuestionaire(self):

        if len(self._questions) is 0:
            self._questions = q.createQuestions()

    def getAnswers(self):
        return self._answers

    def setAnswers(self, ans):
        self._answers = ans

    def askForResponses(self):

        digitsCorrect = False
        positionCorrect = False
        limitCorrect = False

        while digitsCorrect is False:
            digits = int(input(self._questions[0].getTitle() + "?: "))
            if digits > 0:
                self._answers.append(digits)
                digitsCorrect = True

        while positionCorrect is False:
            position = random.randint(1, self._answers[0])
            number = int(input(self._questions[1].getTitle() + " " + str(position) + "?: "))
            if number > 0:
                self._answers.append(position)
                self._answers.append(number)
                positionCorrect = True

        len(self._answers)
        while limitCorrect is False:

            correct = False
            lowLimit = bigLimit = 0

            while correct is False:
                lowLimit = random.randint(pow(10, self._answers[0] - 1), pow(10, self._answers[0]) - 1)

                if self._answers[1] == 1:
                    lowLimit = random.randint(self._answers[2] * pow(10, self._answers[0] - 1), pow(10, self._answers[0]) - 1)

                bigLimit = random.randint(pow(10, self._answers[0] - 1), pow(10, self._answers[0]) - 1)

                if lowLimit < bigLimit:
                    correct = True

            response = input(self._questions[2].getTitle() + " " + str(lowLimit) + " and " + str(bigLimit) + " (y/n)?: ")

            if response is "y":
                self._answers.append(lowLimit)
                self._answers.append(bigLimit)
                limitCorrect = True
            else:
                print("Try again")

        return self._answers