import numpy as np

import collections

from collections import Counter

class GeneratorDigitsNumbers:

    def generateNumbers(self, digits, possiblenumbers):
        possiblenumbers = []
        for possibleNumber in range(pow(10, digits[0] - 1), pow(10, digits[0]) - 1):
            appearances = len(Counter(list(str(possibleNumber))))

            if appearances is digits[0]:
                possiblenumbers.append(possibleNumber)


        return possiblenumbers