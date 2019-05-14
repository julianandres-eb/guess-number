import bin.thinker.core.numbergenerator.numbergenerator as tg
import bin.thinker.core.questions.questionnaire as qt


class Core:

    def __init__(self):
        pass

    def main(self):
        counterAnswers: int = 0
        guessing: bool = False
        oldResponses = []

        # Do questions!
        questionnaire = qt.Questionnaire()

        while guessing is False:
            answers = questionnaire.askForResponses(oldResponses)

            # Generate number
            possibleNumber = tg.NumberGenerator(answers).generateNumbers()
            if possibleNumber is 0:
                print("We asked you almost everything but it didn't work out. Sorry")
                return False
            else:
                response = input("Is " + str(int(possibleNumber)) + " correct(y/n)?: ")
                if response is "y":
                    self.guessing = True
                    print("We win!")
                    return True
                else:
                    if response is "n":
                        counterAnswers = counterAnswers + 1
                        oldResponses.append(possibleNumber)
                        if counterAnswers is 15:
                            print("We asked you almost everything but it didn't work out. Sorry")
                            return False