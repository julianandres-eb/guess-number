from .question import Question


class QuestionMod(Question):

    def __init__(self, title, answers, key, reiterable):
        super().__init__(title, answers, key, reiterable)

    def addAnswer(self, answer):
        self.answers.append(answer)
