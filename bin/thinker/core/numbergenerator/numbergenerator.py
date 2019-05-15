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
            print(key)
            print(self.possibleNumbers)

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



    def addFromBoundaries(self, answers):
        listPossibleValues = []
        boundariesToInsert = []
        boundariesToDelete = []

        for boundary in answers['between']:
            if boundary[2] is "y":
                boundariesToInsert.append(boundary)
            if boundary[2] is "n":
                boundariesToDelete.append(boundary)

        for boundaryToInsert in boundariesToInsert:
            [lowLimit, bigLimit, _] = boundaryToInsert
            for i in range(lowLimit, bigLimit + 1):
                if i not in listPossibleValues:
                    listPossibleValues.append(list(str(i)))

        for boundaryToDelete in boundariesToDelete:
            [lowLimit, bigLimit, _] = boundaryToDelete

            for i in range(lowLimit, bigLimit):
                if i in listPossibleValues:
                    listPossibleValues.remove(i)

        return listPossibleValues

    def addFromNumberPosition(self, position, number, listPossibleValues, answers):
        listValues = []

        for value in listPossibleValues:
            if len(str(value)) is answers['digits'][0]:
                if str(list(str(value))[position - 1]) == str(number):
                    listValues.append(value)

        return listValues

    def deleteFromMod(self, values, answers):

        for value in values:
            if self.evaluateMod(value, answers):
                pass
            else:
                values.remove(value)

        return values

    def evaluateMod(self, value, answers):
        if len(answers) > 0:
            answer, mod = answers[0]
            if answer is 'y':
                if value % mod == 0:
                    return True and self.evaluateMod(value, answers[1:])
                else:
                    return False and self.evaluateMod(value, answers[1:])
            if answer is 'n':
                if value % mod == 0:
                    return False and self.evaluateMod(value, answers[1:])
                else:
                    return True and self.evaluateMod(value, answers[1:])
        else:
            return True

    def _initPossibleNumber(self, answers):

        # Using boundaries defined by the user
        values = self.addFromBoundaries(answers)

        # Generate tree of possible number
        # Using the position and number
        for answer in answers['position']:
            position, numberInPosition = tuple(answer)
            values = self.addFromNumberPosition(position, numberInPosition, values, answers)

        values = self.deleteFromMod(values, answers['mod'])

        return values