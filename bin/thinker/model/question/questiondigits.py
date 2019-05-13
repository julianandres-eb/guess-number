from .question import Question


class QuestionDigits(Question):

    def __init__(self, title, answers, key, reiterable):
        super().__init__(title, answers, key, reiterable)

    def addAnswer(self, answer):
        if len(self.answers) is 0:
            self.answers.append(answer)
