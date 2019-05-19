import random

import numpy as np


# Auxiliar Functions

# Method to find the first repeated value (if there's one),
# as it won't have to look the rest of the numbers once it finds it

def findRepeat(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return True
        seen.add(num)
    return False


# Method that generates a number between 1000 and 9000 and verifies that there's
# repeated number on the 4 digits

def generateNumber():
    hasNoRepeatedNumbers = False
    generatedNumber = 0
    while hasNoRepeatedNumbers is False:
        generatedNumber = random.randint(1000, 9999)
        if findRepeat(list(str(generatedNumber))) is False:
            hasNoRepeatedNumbers = True

    return generatedNumber


# Method that asks to user for any idea of the correct numbers verifying
# that it has 4 digits
def askToUserShot():
    hasFourDigits = False
    response = 0

    while hasFourDigits is False:
        response = int(input("Enter a four-digit number: "))

        if len(str(response)) == 4:
            hasFourDigits = True
        else:
            print("The number has " + str(len(str(response))) + " digits, not 4")

    return response


# Method that returns how many "corrects" and "regulars" are
def calculateCorrectAndRegular(shot, correctNumber):
    # Convert to use them with np.sum
    _shot = np.array([int(x) for x in str(shot)])
    _correctNumber = np.array([int(x) for x in str(correctNumber)])

    # How many corrects are?
    corrects = np.sum(_shot == _correctNumber)
    regulars = 0

    # After determining which numbers match with the correct response,
    # we eliminate them to determine the regular numbers
    shotLeft = _shot[_shot != _correctNumber]
    correctNumberLeft = list(_correctNumber[_shot != _correctNumber])

    for num in shotLeft:
        regulars = regulars + correctNumberLeft.count(num)

    return [corrects, regulars]
