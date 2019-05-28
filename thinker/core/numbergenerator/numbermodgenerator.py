class GeneratorModNumbers:

    def generateNumbers(self, values, possibleNumbers):

        # We 'filter' what we received
        return list(filter(lambda x: self.evaluateMod(x, values), [possibleNumber for possibleNumber in possibleNumbers]))

    ###########################################################
    #
    # evaluateMod(value, answers)
    #
    # value: value to test
    # answers: list of 'mod' that have to be passed by value
    #
    # This method determine if value has one or several 'mod'
    #
    ###########################################################

    def evaluateMod(self, value, answers):
        if len(answers) > 0:
            answer, mod = answers[0]

            if answer is 'y':
                return True and self.evaluateMod(value, answers[1:]) if value % mod == 0 else False

            if answer is 'n':
                return False if value % mod == 0 else True and self.evaluateMod(value, answers[1:])

        else:
            return True