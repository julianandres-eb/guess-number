import bin.four_number_game.four_number_game as fg
import bin.thinker.thinker as tk
import time

def main():

    print("------------------------------------------------------------------------------------")

    print("Select a game")
    print("1. Guess our Number")
    print("2. Thinker: We (try to) guess your number")

    correct = False

    while correct is False:
        index = input("> ")
        if index is "1":
            correct = True
            time.sleep(1.0)
            fg.main()

        if index is "2":
            correct = False
            time.sleep(1.0)
            tk.main()

        print("It's not correct, try again")

if __name__ == "__main__":
    main()



