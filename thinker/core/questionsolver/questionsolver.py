from abc import ABC, abstractmethod

###########################################################
#
# QuestionSolver(Abstract Class)
#
# questions: all questions with the answers associated
# digits: how many digits the number has
# key: value to separate the solvers
#
# This class help us to separate the logic for each question into divided class
# Also it's useful because we can define the questions behaviour in the same way
# Not worrying about what if one modification affects other parts of the code
#
###########################################################

class QuestionSolver(ABC):
    questions: list = []
    digits: int = 0
    key: str

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
        return [q for q in self.questions if q.key is key][-1]

    def getAnswers(self, key):
        return self.getQuestion(key).answers

    def getDigits(self):
        return self.digits
