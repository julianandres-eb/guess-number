from .questionsolver import QuestionSolver


class QuestionSolverDigits(QuestionSolver):

    def askUserValue(self, oldResponses):
        correctValue = False
        value = 0
        while correctValue is False:
            try:
                value = int(input(self.getQuestion(self.key).getTitle() + "?: "))
            except ValueError:
                print("Not an integer!")
                continue
            else:
                if value > 0:
                    correctValue = True
                break

        return value

    def composeAnswer(self, answer):
        return [answer]

    def validateAnswer(self, answer):
        if answer[0] > 0:
            return True
        else:
            return False

    def saveAnswer(self, answer):
        QuestionSolver.digits = answer[0]
        self.getQuestion(self.key).answers.append(answer)
        return answer
