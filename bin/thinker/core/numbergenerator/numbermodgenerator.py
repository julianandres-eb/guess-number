class GeneratorModNumbers:

    def generateNumbers(self, values, possibleNumbers):

        for possibleNumber in possibleNumbers:
            if not self.evaluateMod(possibleNumber, values):
                possibleNumbers.remove(possibleNumber)

        return possibleNumbers



    def evaluateMod(self, value, answers):
        if len(answers) > 0:
            answer, mod = answers[0]
            if answer is 'y':
                if value % mod == 0:
                    return True and self.evaluateMod(value, answers[1:])
                else:
                    return False
            if answer is 'n':
                a = value % mod
                if a == 0:
                    return False
                else:
                    return True and self.evaluateMod(value, answers[1:])
        else:
            return True