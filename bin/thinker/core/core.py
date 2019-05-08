import bin.thinker.core.questions.question as qt
import bin.thinker.core.treegenerator.treegenerator as tg


def main():

    guessing = False

    while guessing is False:

        # Do questions!
        answers = qt.Questionaire()

        # Generate 2 trees (Possible number and No possible numbers) from answers
        trees = tg.TreesGenerator(answers.getAnswers())

        # Resolver arbol y generar un numero tentativo de respuesta
        supposedNumber = 1234

        response = input("Is " + str(supposedNumber) + " correct(y/n)?: ")
        if response is "y":
            guessing = True
            print("We win!")
