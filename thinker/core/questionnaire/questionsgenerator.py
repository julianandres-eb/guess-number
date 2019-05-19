import json

from thinker.utils.singleton import Singleton
from thinker.utils.utils import Utils
from thinker.core.numbergenerator.numberpositiongenerator import GeneratorPositionNumbers
from thinker.core.numbergenerator.numbermodgenerator import GeneratorModNumbers
from thinker.core.numbergenerator.numbergoodregulargenerator import GeneratorGoodregularNumbers
from thinker.core.numbergenerator.numberdigitsgenerator import GeneratorDigitsNumbers
from thinker.core.numbergenerator.numberbetweengenerator import GeneratorBetweenNumbers

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
        with open(Utils.getQuestionsPath(), 'r') as JSON:
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
