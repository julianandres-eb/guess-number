from .questionsolver import QuestionSolver

###########################################################
#
# QuestionSolverDigits
#
# Class that inherits from QuestionSolver. It's responsible
# of determining how many digits the correct number has,
# validates and persists it for futures uses
#
###########################################################

class QuestionSolverDigits(QuestionSolver):

    def askUserValue(self, oldResponses):
        value = 0

        try:
            value = int(input(self.getQuestion(self.key).getTitle() + "?: "))
        except ValueError:
            print("Not an integer!")
        return value

    def composeAnswer(self, answer):
        return [answer]

    def validateAnswer(self, answer):

        if answer[0] > 0:
            return True
        else:
            print("It's not a valid answer. Only numbers bigger than zero")
            return False

    def saveAnswer(self, answer):
        QuestionSolver.digits = answer[0]
        self.getQuestion(self.key).answers.append(answer)
        return answer
