import time

import four_number_game.four_number_game as fg
import thinker as tk


def main():
    print("------------------------------------------------------------------------------------")

    print("Select a game")
    print("1. Guess our Number")
    print("2. Thinker: We (try to) guess your number")

    correct = False

    while correct is False:
        index = input("> (e to exit) ")
        if index is "1":
            time.sleep(1.0)
            fg.main()

        if index is "2":
            time.sleep(1.0)
            tk.main()

        if index is "e":
            correct = True

        if index is not "1" and index is not "2" and index is not "e":
            print("It's not correct, try again")


if __name__ == "__main__":
    main()
