from collections import Counter


class GeneratorDigitsNumbers:

    ###########################################################
    #
    # generateNumbers(digits, possibleNumbers)
    #
    # positionNumbers: list of one value that contains how many digits the number has
    # possibleNumbers: list of all values that can be considered as the user number
    #
    # This method creates all possible values that doesn't have repeated values
    #
    ###########################################################

    def generateNumbers(self, digits, possibleNumbers):

        # If possibleNumbers is empty
        if len(possibleNumbers) == 0:

            # We return a list with all the values
            return [i for i in range(pow(10, digits[0] - 1), pow(10, digits[0]) - 1)

                    # That doesn't have repeated values
                    if len(Counter(list(str(i)))) is digits[0]]

        # If possibleNumbers has already values
        else:

            # We only return a list which we remove values that have repeated values
            return [i for i in possibleNumbers if len(Counter(list(str(i)))) is digits[0]]
