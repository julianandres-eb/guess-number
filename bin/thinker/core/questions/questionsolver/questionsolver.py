from abc import ABC, abstractmethod


class QuestionSolver(ABC):
    questions = []
    digits = 0
    key = ""

    def __init__(self, question):
        super(QuestionSolver, self).__init__()
        self.questions.append(question)
        self.key = question.key

    @abstractmethod
    def askUserValue(self, oldResponses):
        pass

    @abstractmethod
    def composeAnswer(self, value):
        pass

    @abstractmethod
    def validateAnswer(self, answer):
        pass

    @abstractmethod
    def saveAnswer(self, answer):
        pass

    def getQuestion(self, key):
        questionToReturn = []
        for q in self.questions:
            if q.key == key:
                questionToReturn.append(q)
                break
        return questionToReturn[-1]

    def getAnswers(self, key):
        return self.getQuestion(key).answers
