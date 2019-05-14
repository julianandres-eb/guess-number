from bin.thinker.core.core import Core

def main():
    # Instructions and Rules
    print("------------------------------------------------------------------------------------")
    print("Welcome to 'Thinker', our 'tiny' game that guesses numbers from the user")
    print("Let's get started!")
    print("The instructions are the followings:")
    print("- You have to choose a number and it doesn't have to have doubled numbers. For example: 1224")
    print("- We'll start making some questions like 'How many digits has the number?'")
    print("- Then we make our stuff trying to determine the 'secret number'")
    print("- After that you'll tell us, if the number is correct.")
    print("- After you tell us, which number we think is correct, you'll help us by saying")
    print("  how many numbers are in the right position (Good) and how many correspond to")
    print("  the correct number but they aren't placed properly (Regular).")
    print("  For example: if the correct number is 1234 and you write down 1273,")
    print("  our response will be '2 Good, 1 Regular'")
    print("  If not, we'll keep bothering you with questions until we determine the number")
    print("------------------------------------------------------------------------------------")

    print("As we said before, we need to know something to start our process, let's help us!")

    ended = False
    while ended is False:
        if not Core().main():
            ended = True


if __name__ == '__main__':
    main()
