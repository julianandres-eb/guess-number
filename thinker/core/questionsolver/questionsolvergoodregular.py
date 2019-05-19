from .questionsolver import QuestionSolver

###########################################################
#
# QuestionSolverGoodregular
#
# Class that inherits from QuestionSolver. It's responsible of
# determining how many good and regular digits the correct number has,
# validates them and persists them for futures uses
#
###########################################################

class QuestionSolverGoodregular(QuestionSolver):

    # Declaration of class variables
    oldResponses = []

    def askUserValue(self, oldResponses):

        # Declaration of Variables
        self.oldResponses = oldResponses
        value: list = []

        # Validate if it's first time, that means that the computer hasn't determined a possible number
        if len(oldResponses) > 0:
            print(self.getQuestion(self.key).getTitle())

            # Ask for both values
            value.append(self.askFor('Good'))
            value.append(self.askFor('Regular'))

        return value

    # Function to ask user for values and don't repeat code
    def askFor(self, typeValue):

        # Declaration of Variables
        correct: bool = False
        valueToReturn: int = 0

        # Iterate until the number is bigger than zero
        while correct is False:

            # Check if it's a number
            try:
                valueToReturn = int(input("> " + typeValue + " "))
            except ValueError:
                print("Not an integer!")
            else:
                if valueToReturn >= 0:
                    correct = True

        return valueToReturn

    def composeAnswer(self, answer):

        # Validate if the computer has determined a possible number
        if len(self.oldResponses) is not 0:

            # Use the last value (the current) and compose the answer
            return [self.oldResponses[-1], answer[0], answer[1]]

        else:
            return []

    def validateAnswer(self, answer):

        # Check if we have an answer
        if len(answer) > 0:

            # Check if both good and regular are bigger than number of digits
            if answer[0] + answer[1] is not self.digits:
                return True
            else:
                print("It's not a valid answer. 'Good' and 'Regular' together are bigger than the number of digits")
                return False
        else:
            # If not, that means that it's first time in SolverGoodQuestion
            return True

    def saveAnswer(self, answer):
        if len(answer) is not 0:
            self.getQuestion(self.key).answers.append(answer)

        return self.getQuestion(self.key).answers
