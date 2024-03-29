import thinker.core.numbergenerator.numbergenerator as tg
from thinker.core.questionnaire.questionnaire import Questionnaire


###########################################################
#
# Core
#
# Class that leads all the process of 'thinking' the number
# that the user has thought
#
###########################################################

class Core:

    def main(self):

        # Declaration of variables
        counterAnswers: int = 0
        guessing: bool = False
        oldResponses : list = []

        # Do questionnaire!
        questionnaire = Questionnaire()

        # Until the user checks if the number is correct or we have tried enough
        while guessing is False:
            answers = questionnaire.askForResponses(oldResponses)

            # Generate number
            possibleNumber = tg.NumberGenerator(answers, oldResponses).generate()
            if possibleNumber is 0:
                print("We can't see the real answer, try it later. Sorry")
                return False
            else:

                # Ask the user if our possible number is correct
                correctAnswer: bool = False
                response: str
                while correctAnswer is False:
                    response = input("Is " + str(possibleNumber) + " correct(y/n)?: ")
                    if response is "y" or response is "n":
                        correctAnswer = True
                    else:
                        print("Not a valid answer, only y or n. Try again!")

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