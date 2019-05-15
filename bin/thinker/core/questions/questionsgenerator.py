import json

from bin.thinker.utils.singleton import Singleton
from bin.thinker.utils.utils import Utils
from bin.thinker.core.questions.questionscreator.questioncreator import QuestionCreator
from bin.thinker.core.questions.questionscreator.creatordigitsquestion import CreatorDigitsQuestion
from bin.thinker.core.questions.questionscreator.creatorpositionquestion import CreatorPositionQuestion
from bin.thinker.core.questions.questionscreator.creatorbetweenquestion import CreatorBetweenQuestion
from bin.thinker.core.questions.questionscreator.creatormodquestion import CreatorModQuestion
from bin.thinker.core.questions.questionscreator.creatorgoodregularquestion import CreatorGoodregularQuestion

class QuestionsGenerator(metaclass=Singleton):
    questions = []

    def __init__(self):
        self.questions = self.generateQuestions()

    def setQuestions(self, questions):
        self.questions = questions

    def getQuestions(self):
        return self.questions

    def getQuestion(self, key):
        questionToReturn = []
        for q in self.questions:
            if q.key == key:
                questionToReturn.append(q)
                break
        return questionToReturn

    def composeNameClass(self, key):
        return "Creator" + key.capitalize() + "Question"

    def generateQuestions(self):
        questionsToReturn = []

        # Create Questions from File
        # - Read file and generate a dict
        with open(Utils.getQuestionsPath(), 'r') as JSON:
            allQuestions = json.load(JSON)

        for key, value in allQuestions.items():
            creator = globals()[self.composeNameClass(key)]()
            questionsToReturn.append(creator._createQuestion(value))

        return questionsToReturn