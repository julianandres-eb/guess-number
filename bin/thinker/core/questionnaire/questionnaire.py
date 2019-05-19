from .questionsgenerator import QuestionsGenerator

from bin.thinker.core.questionsolver.questionsolvergoodregular import QuestionSolverGoodregular
from bin.thinker.core.questionsolver.questionsolverdigits import QuestionSolverDigits
from bin.thinker.core.questionsolver.questionsolverposition import QuestionSolverPosition
from bin.thinker.core.questionsolver.questionsolverbetween import QuestionSolverBetween
from bin.thinker.core.questionsolver.questionsolvermod import QuestionSolverMod

class Questionnaire:
    questions = []
    answers = {}
    oldResponses = []

    def __init__(self):
        self.initQuestionaire()

    def initQuestionaire(self):

        if not bool(self.questions):
            self.questions = QuestionsGenerator().getQuestions()

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

        return answer

    def askForResponses(self, oldResponses):

        self.oldResponses = oldResponses

        if self.canContinue():
            for question in self.questions:
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
        for question in self.questions:
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
