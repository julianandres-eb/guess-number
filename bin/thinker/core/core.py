import bin.thinker.core.numbergenerator.numbergenerator as tg
import bin.thinker.core.questions.questionnaire as qt


class Core:

    def __init__(self):
        pass

    def main(self):

        guessing: bool = False

        # Do questions!
        questionnaire = qt.Questionnaire()

        while guessing is False:
            answers = questionnaire.askForResponses()

            # Generate number
            possibleNumber = tg.NumberGenerator(answers).generateNumbers()
            if possibleNumber is 0:
                break
            else:
                response = input("Is " + str(int(possibleNumber)) + " correct(y/n)?: ")
                if response is "y":
                    self.guessing = True
                    print("We win!")
                    return False

        print("We asked you almost everything but it didn't work out. Sorry")
        return True
