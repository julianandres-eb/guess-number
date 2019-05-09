import bin.thinker.core.core as core

def main():

    # Instructions and Rules
    print("------------------------------------------------------------------------------------")
    print("Welcome to 'Thinker', our 'tiny' game that guesses numbers from the user")
    print("Let's get started!")
    print("The instructions are the followings:")
    print("- We'll start making some questions like 'How many digits has the number?'")
    print("- Then we make our stuff trying to determine the 'secret number'")
    print("- After that you'll tell us, if the number is correct.")
    print("If not, we'll keep bothering you with questions until we determine the number")
    print("------------------------------------------------------------------------------------")

    print("As we said before, we need to know something to start our process, let's help us!")

    core.main()


if __name__ == '__main__':
    main()