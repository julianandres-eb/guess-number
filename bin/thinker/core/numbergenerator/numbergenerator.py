import random

from .numberbetweengenerator import GeneratorBetweenNumbers
from .numberdigitsgenerator import GeneratorDigitsNumbers
from .numbergoodregulargenerator import GeneratorGoodregularNumbers
from .numbermodgenerator import GeneratorModNumbers
from .numberpositiongenerator import GeneratorPositionNumbers

class NumberGenerator:

    # Declaration of variables
    possibleNumbers : list = []
    oldResponses : list = []
    questions : list = []
    answers : dict = {}

    # Class init
    def __init__(self, answers):
        self.answers = answers

    # Main Function
    def generate(self):
        self.generateNumbers()
        return self.selectValue()

    def generateNumbers(self):

        # For each answer, we generate the values related to those
        for key, value in self.answers.items():
            try:
                # We create the class who manages the answer
                generator = globals()[self.composeNameClass(key)]()

            # If there's not that generator, we keep going
            except ModuleNotFoundError:
                pass

            # Otherwise we generate the possibleNumbers
            else:
                self.possibleNumbers = generator.generateNumbers(value, self.possibleNumbers)

    # After all hard work of generateNumbers, we choose one value to be the answer's machine
    def selectValue(self):
        lastPossibleNumber = self.selectPossibleNumber(self.possibleNumbers)
        self.oldResponses.append(lastPossibleNumber)
        return lastPossibleNumber

    # Simple 'Random' Function
    def selectPossibleNumber(self, values):
        if len(values) > 0:
            return random.choice(values)
        else:
            return 0

    # Function that returns the name of the generator class
    def composeNameClass(self, key):
        return "Generator" + key.capitalize() + "Numbers"
