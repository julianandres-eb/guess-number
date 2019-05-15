from .questionsgenerator import QuestionsGenerator

from bin.thinker.core.questions.questionsolver.questionsolvermod import QuestionSolverMod
from bin.thinker.core.questions.questionsolver.questionsolverbetween import QuestionSolverBetween
from bin.thinker.core.questions.questionsolver.questionsolverposition import QuestionSolverPosition
from bin.thinker.core.questions.questionsolver.questionsolverdigits import QuestionSolverDigits
from bin.thinker.core.questions.questionsolver.questionsolvergoodregular import QuestionSolverGoodregular

class Questionnaire:
    _questions = []
    answers = {}
    oldResponses = []

    def __init__(self):
        self.initQuestionaire()

    def initQuestionaire(self):

        if not bool(self._questions):
            self._questions = QuestionsGenerator().getQuestions()

    def ask(self, question):

        solver = self.getSolver(question)
        correct = False
        answer = []

        while correct is False:
            value = solver.askUserValue(self.oldResponses)
            answer = solver.composeAnswer(value)
            if solver.validateAnswer(answer):
                answer = solver.saveAnswer(answer)
                correct = True
            else:
                print("It's not a valid answer")

        return answer

    def askForResponses(self, oldResponses):

        self.oldResponses = oldResponses

        if self.canContinue():
            for question in self._questions:
                if question.getReiterable() is "n":
                    if len(question.getAnswers()) is 0:
                        self.answers[question.key] = self.ask(question)
                else:
                    self.answers[question.key] = self.ask(question)

        return self.answers

    def composeNameClass(self, key):
        return "QuestionSolver" + key.capitalize()

    def getSolver(self, question):
        return globals()[self.composeNameClass(question.key)](question)

    def canContinue(self):
        digits = 0
        positions = []
        for question in self._questions:
            if len(question.getAnswers()) > 0:
                if question.getKey() is "digits":
                    digits = question.getAnswers()[0]

                if question.getKey() is "position":
                    positions = question.getAnswers()

            if len(positions) is 0 and digits is 0:
                return True
            else:
                if len(positions) is not digits:
                    return True
                else:
                    return False