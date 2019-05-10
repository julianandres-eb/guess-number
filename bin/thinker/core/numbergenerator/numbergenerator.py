import random

class NumberGenerator:
    _PossibleNumbers = []
    answers = []

    def __init__(self, answers):
        self.answers = answers


    def generateNumbers(self):
        self._initPossibleNumber(self.answers)
        return self._selectPossibleNumber(self._initPossibleNumber(self.answers))

    def addFromBoundaries(self, answers):
        listPossibleValues = []

        for i in range(answers[3], answers[4]):
            listPossibleValues.append(list(str(i)))

        return listPossibleValues

    def addFromNumberPosition(self, position, number, listPossibleValues):
        listValues = []

        for value in listPossibleValues:
            if value[position - 1] == str(number):
                listValues.append(value)

        return listValues

    def _initPossibleNumber(self, answers):

        # Using boundaries defined by the user
        values = self.addFromBoundaries(answers)

        # Generate tree of possible number
        # Using the position and number
        # answers[1] : position
        # answers[2] : number value in that position
        values = self.addFromNumberPosition(answers[1], answers[2], values)

        return values

    def _selectPossibleNumber(self, values):
        return values[random.randint(0, len(values))]