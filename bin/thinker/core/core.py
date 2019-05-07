import bin.thinker.core.questions.question as qt


def main():

    guessing = False

    while guessing is False:

        # Do questions!
        answers = qt.initQuestions()

        # Generar arbol de entrada

        # Resolver arbol y generar un numero tentativo de respuesta
        supposedNumber = 1234

        response = input("Is " + str(supposedNumber) + " correct?(y/n): ")
        if response is "y":
            guessing = True
            print("We win!")
