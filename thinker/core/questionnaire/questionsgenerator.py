import json

from thinker.utils.singleton import Singleton
from thinker.utils.utils import Utils
from thinker.core.questionscreator.creatordigitsquestion import CreatorDigitsQuestion
from thinker.core.questionscreator.creatorpositionquestion import CreatorPositionQuestion
from thinker.core.questionscreator.creatorbetweenquestion import CreatorBetweenQuestion
from thinker.core.questionscreator.creatormodquestion import CreatorModQuestion
from thinker.core.questionscreator.creatorgoodregularquestion import CreatorGoodregularQuestion

###########################################################
#
# QuestionsGenerator
#
# Singleton class that generates all possible questions in program
#
###########################################################

class QuestionsGenerator(metaclass=Singleton):

    # Declaration of class variables
    questions = []

    # Init class
    def __init__(self):
        self.questions = self.generateQuestions()

    def generateQuestions(self):

        # Declaration of class variables
        questionsToReturn:list = []

        # Create Questions from File
        # - Read file and generate a dict
        try:
            JSON = open(Utils().getQuestionsPath(), 'r')
        except IOError:
            print("Problems opening questions file")
            exit(IOError.filename)
        else:
            allQuestions = json.load(JSON)

        # For each question, we create the questions model
        for key, value in allQuestions.items():
            try:
                # We create the class who manages the creation
                creator = globals()[self.composeNameClass(key)]()

            # If there's not that creator, we keep going
            except ModuleNotFoundError:
                pass

            # Otherwise we append it
            else:
                questionsToReturn.append(creator._createQuestion(value))

        return questionsToReturn

    def setQuestions(self, questions):
        self.questions = questions

    def getAllQuestions(self):
        return self.questions

    def getQuestionsWithKey(self, key):
        return [q for q in self.questions if q.key is key]

    def composeNameClass(self, key):
        return "Creator" + key.capitalize() + "Question"
