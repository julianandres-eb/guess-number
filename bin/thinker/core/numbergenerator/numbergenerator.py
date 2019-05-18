import random

from .numberbetweengenerator import GeneratorBetweenNumbers
from .numberdigitsgenerator import GeneratorDigitsNumbers
from .numbergoodregulargenerator import GeneratorGoodregularNumbers
from .numbermodgenerator import GeneratorModNumbers
from .numberpositiongenerator import GeneratorPositionNumbers

class NumberGenerator:
    possibleNumbers = []
    answers = {}
    oldResponses = []
    questions = []

    def __init__(self, answers):
        self.answers = answers

    def generateNumbers(self):

        for key, value in self.answers.items():

            generator = globals()[self.composeNameClass(key)]()
            self.possibleNumbers = generator.generateNumbers(value, self.possibleNumbers)

        lastPossibleNumber = self.selectPossibleNumber(self.possibleNumbers)
        self.oldResponses.append(lastPossibleNumber)
        return lastPossibleNumber



    def composeNameClass(self, key):
        return "Generator" + key.capitalize() + "Numbers"

    def selectPossibleNumber(self, values):
        if len(values) > 0:
            return random.choice(values)
        else:
            return 0