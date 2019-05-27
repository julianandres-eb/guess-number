import random

from .questionsolver import QuestionSolver

###########################################################
#
# QuestionSolverBetween
#
# Class that inherits from QuestionSolver. It's responsible of creating possible boundaries,
# validates and persists them for futures uses
#
###########################################################

class QuestionSolverBetween(QuestionSolver):

    # Declaration of class variables
    lastLowLimit: int
    lastBigLimit: int

    # Init class
    def __init__(self, question):
        super().__init__(question)
        self.lastLowLimit = self.lastBigLimit = 0

    ###########################################################
    #
    # askUserValue(oldResponses)
    #
    # oldResponses: list of old responses related to QuestionBetween
    # possibleNumbers: list of all values that can be considered as the user number
    #
    # This method creates different boundaries that remove values from possibleNumbers
    #
    ###########################################################

    def askUserValue(self, oldResponses):
        correctLimit: bool  = False
        correctAnswer: bool  = False

        # Creating a boundary and checking if lowLimit is < than bigLimit
        while correctLimit is False:
            self.lastLowLimit = random.randint(pow(10, QuestionSolver.digits - 1), pow(10, QuestionSolver.digits) - 1)
            self.lastBigLimit = random.randint(pow(10, QuestionSolver.digits - 1), pow(10, QuestionSolver.digits) - 1)

            if self.lastLowLimit < self.lastBigLimit:
                correctLimit = True

        while correctAnswer is False:
            i = input(self.getQuestion(self.key).getTitle() + " " + str(self.lastLowLimit) + " and " + str(
                self.lastBigLimit) + "? (y/n): ")

            if i is "y" or i is "n":
                self.correctAnswer = True
                return i


    def composeAnswer(self, value):
        return [self.lastLowLimit, self.lastBigLimit, value]

    def validateAnswer(self, answer):

        if answer[2] is "y" or answer[2] is "n":
            return True
        else:
            print("It's not a valid answer. Only 'y' and 'n' are possible")
            return False

    def saveAnswer(self, answer):
        self.getQuestion(self.key).answers.append(answer)
        return self.getQuestion(self.key).answers
