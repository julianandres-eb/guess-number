# Imports
import time

import guesser.auxiliarFunctions.auxiliarFunctions as auxF


def main():
    # Instructions
    print("------------------------------------------------------------------------------------")

    print("Welcome to '4NG', our 'tiny' game to guess which number we're hiding from you")
    print("Let's get started!")
    print("The instructions are the following:")
    print("- You have to guess a number between 1000 and 9999 (that means 4 digits)")
    print("- These 4 digits cannot be repeated, for example: 1224")
    print("- After you tell us, which number you think is correct, we'll help you by saying")
    print("how many numbers are in the right position (Good) and how many correspond to")
    print("the correct number but they aren't placed properly (Regular).")
    print("For example: if the correct number is 1234 and you write down 1273,")
    print("our response will be '2 Good, 1 Regular'")

    print("------------------------------------------------------------------------------------")

    # Variables
    guessing = False
    numberToGuess = auxF.generateNumber()

    time.sleep(4.0)

    while guessing is False:

        # We ask the user to an answer and make sure that this response accomplishes our requirements
        userShot = auxF.askToUserShot()

        # We calculate how many "correct" and "regular" are
        calculate = auxF.calculateCorrectAndRegular(userShot, numberToGuess)

        if calculate[0] == 4:
            guessing = True
            print("Good 4, You win")
        else:
            print("Good " + str(calculate[0]) + ", Regular " + str(calculate[1]))


if __name__ == "__main__":
    main()
