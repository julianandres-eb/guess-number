import bin.thinker.core.questions.questionnaire as qt
import bin.thinker.core.numbergenerator.numbergenerator as tg

def main():

    guessing = False

    while guessing is False:
        # Do questions!
        questionnaire = qt.Questionnaire()
        questionnaire.initQuestionaire()
        answers = questionnaire.askForResponses()

        # Generate number
        possibleNumber = tg.NumberGenerator(answers).generateNumbers()

        # Format list of string to int
        possibleNumber = int(''.join(str(i) for i in possibleNumber))

        response = input("Is " + str(int(possibleNumber)) + " correct(y/n)?: ")

        if response is "y":
            guessing = True
            print("We win!")
        else:
            guessing = True
            print("Game Over")
