from collections import Counter

class GeneratorDigitsNumbers:

    def generateNumbers(self, digits, possiblenumbers):

        numbersToClean = []
        possibleNumbers = []

        # Generate necessary values
        if len(possiblenumbers) == 0:
            numbersToClean = [i for i in range(pow(10, digits[0] - 1), pow(10, digits[0]) - 1)]

            for number in numbersToClean:
                appearances = len(Counter(list(str(number))))

                if appearances is digits[0]:
                    possibleNumbers.append(number)

        else:
            numbersToClean = possiblenumbers

            for number in numbersToClean:
                appearances = len(Counter(list(str(number))))

                if appearances is not digits[0]:
                    possibleNumbers.remove(number)

        return possibleNumbers