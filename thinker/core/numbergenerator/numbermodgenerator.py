class GeneratorModNumbers:

    def generateNumbers(self, values, possibleNumbers):
        return [possibleNumber for possibleNumber in possibleNumbers if self.evaluateMod(possibleNumber, values)]

    ###########################################################
    #
    # evaluateMod(value, answers)
    #
    # value: value to test
    # answers: list of 'mod' that have to be passed by value
    #
    # This method determine if value has one or several 'mod'
    #
    #
    ###########################################################

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