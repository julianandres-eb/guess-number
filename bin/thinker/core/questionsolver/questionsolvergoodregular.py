from .questionsolver import QuestionSolver


class QuestionSolverGoodregular(QuestionSolver):

    oldResponses = []

    def askUserValue(self, oldResponses):
        self.oldResponses = oldResponses

        correctGood = correctRegular = False
        good = regular = -1
        value = [good, regular]

        if len(oldResponses) > 0:
            print(self.getQuestion(self.key).getTitle())

            while correctGood is False:
                try:
                    good = int(input("> Good: "))
                except ValueError:
                    print("Not an integer!")
                    continue
                else:
                    if good >= 0:
                        self.correctGood = True
                        value[0] = good
                    break

            while correctRegular is False:
                try:
                    regular = int(input("> Regular: "))
                except ValueError:
                    print("Not an integer!")
                    continue
                else:
                    if regular >= 0:
                        self.correctRegular = True
                        value[1] = regular
                    break

        return value

    def composeAnswer(self, answer):
        if len(self.oldResponses) is 0:
            return []
        else:
            return [self.oldResponses[-1], answer[0], answer[1]]

    def validateAnswer(self, answer):
        if len(answer) > 0:
            if answer[0] >= 0:
                return True
            else:
                return False
        else:
            return True ## fue por el caso de el primer valor

    def saveAnswer(self, answer):
        if len(answer) is not 0:
            self.getQuestion(self.key).answers.append(answer)

        return self.getQuestion(self.key).answers
